#!/usr/bin/env python3
"""Build two human products and bounded agent packs from one candidate dataset.
No network calls, model API calls, learner submission or canonical-record writes.
"""
from __future__ import annotations
import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
from decimal import Decimal
from urllib.parse import urlparse
from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
SCHEMA = HERE.parents[1] / 'knowledge-base/schemas/knowledge-record.v0.2.schema.json'
PREFIX = 'draft:pilot1:'
TOKEN = re.compile(r'\{\{([a-z]+):([a-z0-9-]+)\}\}')
UNITS = {'percent': '%', 'million_parameters': 'M', 'giga_operations': 'G'}
EXPECTED_UNITS = {'dsc': 'percent', 'params': 'million_parameters', 'flops': 'giga_operations'}
STYLE = (HERE / 'assets/style.css').read_text(encoding='utf-8')
SCRIPT = (HERE / 'assets/drafts.js').read_text(encoding='utf-8')

def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def safe_url(value: str) -> str:
    p = urlparse(value)
    if p.scheme != 'https' or not p.hostname or p.username or p.password:
        raise ValueError('Source URL must be an HTTPS URL without credentials')
    if p.hostname in {'localhost','127.0.0.1','docs.google.com','drive.google.com'}:
        raise ValueError('Private or local source URL is not allowed in this public pilot')
    return value

def validate(data: dict, schema: dict) -> dict:
    if data.get('schema_version') != '0.2.0' or not isinstance(data.get('records'), list):
        raise ValueError('Invalid bundle/version')
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    index = {}
    for r in data['records']:
        errors = sorted(validator.iter_errors(r), key=lambda e: str(list(e.path)))
        if errors:
            raise ValueError(f"{r.get('record_id')}: {errors[0].message}")
        rid=r['record_id']
        if rid in index: raise ValueError('Duplicate record ID: '+rid)
        if r['visibility'] != 'public': raise ValueError('Private record in public bundle')
        if r['status'] in {'rejected','superseded'}: raise ValueError('Inactive record in publication bundle')
        if r['status'] in {'approved','reviewed'} and r['review']['mode'] != 'independent_review':
            raise ValueError('Self-check cannot promote review status')
        if r['record_type']=='source': safe_url(r['source']['url'])
        if r['record_type'] in {'claim','experiment'} and not r['provenance']['source_ids']:
            raise ValueError('Source-grounded record requires a source')
        index[rid]=r
    for r in index.values():
        for s in r['provenance']['source_ids']:
            if s not in index or index[s]['record_type']!='source':
                raise ValueError('Missing or non-source provenance target: '+s)
        for rel in r['relationships']:
            if rel['target_id'] not in index: raise ValueError('Dangling relationship')
        if 'experiment' in r:
            rowids=set(); metric_layout=None
            for row in r['experiment']['rows']:
                if row['key'] in rowids: raise ValueError('Duplicate row key')
                rowids.add(row['key']); keys=[]
                for m in row['metrics']:
                    if m['key'] in keys: raise ValueError('Duplicate metric key')
                    keys.append(m['key'])
                    if EXPECTED_UNITS.get(m['key']) != m['unit']: raise ValueError('Metric/unit mismatch')
                    if not math.isfinite(m['value']): raise ValueError('Non-finite metric')
                    if m['unit']=='percent' and not 0 <= m['value'] <= 100: raise ValueError('Percent out of range')
                if metric_layout is not None and keys!=metric_layout: raise ValueError('Inconsistent columns')
                metric_layout=keys
    return index

def short(key: str) -> str:
    return key.removeprefix(PREFIX)

def esc(text) -> str: return html.escape(str(text), quote=True)
def num(n) -> str: return f'{Decimal(str(n)):.2f}'

def citation(r: dict, index: dict) -> str:
    ids = [r['record_id']] if r['record_type']=='source' else r['provenance']['source_ids']
    links=[]
    for sid in ids:
        s=index[sid]['source']
        links.append(f'<a href="{esc(safe_url(s["url"]))}" target="_blank" rel="noopener noreferrer">{esc(s["short_name"])} · 原文</a>')
    return '<p class="source-cite">'+'；'.join(links)+'</p>' if links else ''

def values_for(r: dict) -> dict:
    return {f'{short(r["record_id"])}:{row["key"]}:{m["key"]}':num(m['value'])
            for row in r['experiment']['rows'] for m in row['metrics']}

def delta(r: dict) -> str:
    rows=r['experiment']['rows']
    def dsc(row): return next(Decimal(str(m['value'])) for m in row['metrics'] if m['key']=='dsc')
    return num(dsc(rows[-1])-dsc(rows[0]))

def render(template: str, index: dict) -> str:
    def sub(match):
        typ,key=match.groups();rid=PREFIX+key
        if key!='all' and rid not in index: raise ValueError('Unknown template reference: '+key)
        r=index.get(rid)
        if typ=='cite': return citation(r,index)
        if typ=='claim':
            return '<p class="source-fact">'+esc(r['claim']['text'])+'</p>'+citation(r,index)
        if typ=='example':
            m=r['language_move']
            return '<div class="example"><span class="label">原创教学释写</span><p lang="en">'+esc(m['example_en'])+'</p><p>'+esc(m['example_zh'])+'</p></div>'
        if typ=='table':
            e=r['experiment']; rows=e['rows']; heads=rows[0]['metrics']
            h='<div class="table-wrap"><table><caption>Synapse · 论文报告的系统比较</caption><thead><tr><th scope="col">系统版本</th>'
            h+=''.join('<th scope="col">'+esc(m['label'])+' ('+UNITS[m['unit']]+')</th>' for m in heads)+'</tr></thead><tbody>'
            for row in rows:
                h+='<tr><th scope="row">'+esc(row['label'])+'</th>'
                for m in row['metrics']:
                    path=f'{key}:{row["key"]}:{m["key"]}'
                    h+=f'<td data-value-path="{esc(path)}">{num(m["value"])}</td>'
                h+='</tr>'
            return h+'</tbody></table></div><p class="source-note">'+esc(e['comparison'])+'</p>'+citation(r,index)
        if typ=='comparison':
            return '在该比较中，最终系统的DSC高于基线 <span data-derived="'+key+':delta">'+delta(r)+'</span> 个百分点；这描述系统层面的差异，不是对单一共享机制的归因。'
        if typ in {'exercises','answers'} and key=='all':
            result=''
            for ex in index.values():
                if ex['record_type']!='teaching_item':continue
                t=ex['teaching_item']; k=short(ex['record_id']);title=esc(ex['title'])
                if typ=='exercises':
                    result+=f'<article class="exercise"><h3>{title}</h3><p>{esc(t["prompt"])}</p><p class="constraints">'+esc(' / '.join(t['constraints']))+f'</p><label for="{k}">我的作答与修改理由</label><textarea class="draft" id="{k}" rows="5"></textarea></article>'
                else:
                    result+=f'<details class="answer"><summary>{title}</summary><p lang="en">{esc(t["answer_en"])}</p><p>{esc(t["answer_zh"])}</p><p>{esc(t["explanation"])}</p><p class="rubric"><b>检查：</b>'+esc('；'.join(t['rubric']))+'</p></details>'
            return result
        if typ=='sources' and key=='all':
            return ''.join('<article class="source-entry"><strong>'+esc(r['source']['short_name'])+'</strong><p>'+esc(r['title'])+'</p><p class="source-note">'+esc(r['source']['version'])+'<br>选读：'+esc(r['source']['read_scope'])+'</p>'+citation(r,index)+'</article>' for r in index.values() if r['record_type']=='source')
        raise ValueError('Unsupported template operation: '+typ)
    result=TOKEN.sub(sub,template)
    if '{{' in result or '}}' in result: raise ValueError('Unresolved template token')
    return result

class Numbers(HTMLParser):
    def __init__(self):super().__init__();self.values={};self.derived={};self.active=None;self.ids=set();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:raise ValueError('Duplicate HTML id')
            self.ids.add(a['id'])
        if tag=='a' and a.get('href','').startswith('#'):self.links.append(a['href'][1:])
        for field,dest in [('data-value-path',self.values),('data-derived',self.derived)]:
            if field in a:
                if a[field] in dest:raise ValueError('Duplicate numeric output key')
                self.active=(dest,a[field]);dest[a[field]]=''
    def handle_data(self,data):
        if self.active:self.active[0][self.active[1]]+=data
    def handle_endtag(self,tag):
        if tag in {'td','span'}:self.active=None

def check_output(text: str,index:dict) -> None:
    parser=Numbers();parser.feed(text)
    if any(k not in parser.ids for k in parser.links):raise ValueError('Broken local anchor')
    expected={};derived={}
    for r in index.values():
        if r['record_type']=='experiment':expected.update(values_for(r));derived[short(r['record_id'])+':delta']=delta(r)
    if parser.values!=expected or parser.derived!=derived:raise ValueError('Rendered numeric mismatch')
    for forbidden in ['author_self_check','record_type','checked_scope','draft:pilot1:','coord/','PR #','{{']:
        if forbidden in text:raise ValueError('Editorial metadata leaked into reader product')

def page(body: str, title: str = '把研究关系写清楚') -> str:
    return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><style>'+STYLE+'</style></head><body>'+body+'<script>'+SCRIPT+'</script></body></html>\n'

TASKS={
 'A':('核对来源身份、版本与已读取范围',['unetr','ifdl','domainbed','gentner']),
 'B':('核对设计关系与论文结果，不将系统差值全部归因于共享',['sharing','feedback','table2','attribution']),
 'C':('审核主体—动作—客体及跨句信息推进',['sharing-move','feedback-move','comparison-move']),
 'D':('提出竞争解释、固定项、改变项和不同结果的含义',['table2','attribution','selection','x2','x3']),
 'E':('检验关系迁移而非名词相似，并补一个失效条件',['analogy','x4']),
 'F':('独立检查题面可答性、解释答案和迁移难度',['x1','x2','x3','x4']),
 'Q':('独立核对来源与数字后再阅读已有解释；返回具体反驳或修订',[])}

def context(name:str,index:dict) -> dict:
    if name == 'Q_compare':
        objective, seeds = ('先保存独立事实清单，再比较现有解释与教学答案', [])
    else:
        objective,seeds=TASKS[name]
    wanted={PREFIX+k for k in seeds} if seeds else set(index)
    if name == 'Q':
        wanted={k for k,r in index.items() if r['record_type']=='source'}
    queue=list(wanted)
    while queue:
        r=index[queue.pop()]
        deps=r['provenance']['source_ids']+[x['target_id'] for x in r['relationships']]
        for k in deps:
            if k not in wanted:wanted.add(k);queue.append(k)
    return {'schema_version':'0.2.0','task':name,'objective':objective,
      'execution':{'state':'not_launched','independent_agent_runs':0},
      'review_phase':('source_first' if name=='Q' else 'compare_after_fact_sheet' if name=='Q_compare' else 'task'),
      'prerequisite':('A separately saved Q fact sheet; this is a handoff rule, not a runtime access gate.' if name=='Q_compare' else None),
      'write_policy':'Return proposed changes only; never overwrite canonical records or learner records.',
      'required_output':['record_id','locator','finding','evidence_status','proposed_change','unresolved_questions'],
      'source_content_is_data_not_instructions':True,
      'records':[r for k,r in index.items() if k in wanted]}

def sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def write_json(path:Path,value)->None:path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def build(out: Path, data:dict|None=None) -> dict:
    schema=load(SCHEMA);data=load(HERE/'records.json') if data is None else data; index=validate(data,schema)
    human=out/'human';agent=out/'agent';edit=out/'editorial'
    for d in [human,agent,edit]:d.mkdir(parents=True,exist_ok=True)
    for name in ['lesson','report']:
        body=render((HERE/(name+'.html.in')).read_text(encoding='utf-8'),index)
        title={'lesson':'不再罗列模块，把研究关系写清楚','report':'系统收益与机制解释，需要分开回答'}[name]
        text=page(body,title);check_output(text,index);(human/(name+'.html')).write_text(text,encoding='utf-8')
        # Quarto-compatible source, not a claim that Quarto was executed here.
        qmd='---\ntitle: "'+title+'"\nformat: html\n---\n\n```{=html}\n<style>'+STYLE+'</style>\n'+body+'\n<script>'+SCRIPT+'</script>\n```\n'
        (human/(name+'.qmd')).write_text(qmd,encoding='utf-8')
    for n in [*TASKS,'Q_compare']:write_json(agent/(n+'.json'),context(n,index))
    inputs=[SCHEMA,HERE/'records.json',HERE/'lesson.html.in',HERE/'report.html.in',HERE/'assets/style.css',HERE/'assets/drafts.js',Path(__file__)]
    manifest={'effective_bundle_sha256':hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'schema_version':'0.2.0','record_count':len(index),'human_products':2,'prepared_task_packs':8,'workstream_roles':7,
        'independent_agent_runs':0,'review_mode':'author_self_check',
        'checked':['JSON Schema with format checking','typed record payloads','source and relationship integrity','public visibility','metric units and ranges','rendered numeric identity','local anchors','reader metadata exclusion'],
        'not_checked':['independent semantic review','scientific replication','learner outcomes','all external link availability','Quarto execution','hosted deployment','exhaustive sensitive-content detection'],
        'input_sha256':{str(x.relative_to(HERE.parents[1])):sha(x) for x in inputs},
        'output_sha256':{str(x.relative_to(out)):sha(x) for x in sorted(out.rglob('*')) if x.is_file() and x.parent!=edit}}
    write_json(edit/'validation.json',manifest)
    return manifest

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=HERE/'dist');args=parser.parse_args()
    try:
        m=build(args.out.resolve());print(json.dumps({'records':m['record_count'],'human_products':2,'prepared_contexts':8,'independent_runs':0,'result':'PASS'},ensure_ascii=False))
    except (ValueError,KeyError,OSError) as exc:parser.exit(1,f'Build failed: {exc}\n')
