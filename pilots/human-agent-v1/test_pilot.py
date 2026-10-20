"""Regression and negative tests. These test engineering, not learning efficacy."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('pilot_build',P/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class PilotTests(unittest.TestCase):
    def setUp(self):
        self.data=b.load(P/'records.json');self.schema=b.load(b.SCHEMA)
    def record(self,key):return next(r for r in self.data['records'] if r['record_id']==b.PREFIX+key)
    def invalid(self):
        with self.assertRaises(ValueError):b.validate(self.data,self.schema)
    def test_valid_records(self):self.assertEqual(len(b.validate(self.data,self.schema)),17)
    def test_missing_experiment_payload(self):del self.record('table2')['experiment'];self.invalid()
    def test_missing_claim_payload(self):del self.record('sharing')['claim'];self.invalid()
    def test_wrong_payload(self):self.record('unetr')['claim']=copy.deepcopy(self.record('sharing')['claim']);self.invalid()
    def test_empty_claim(self):self.record('sharing')['claim']['text']='';self.invalid()
    def test_duplicate_record(self):self.data['records'].append(copy.deepcopy(self.data['records'][0]));self.invalid()
    def test_missing_source(self):self.record('sharing')['provenance']['source_ids']=['absent'];self.invalid()
    def test_non_source_provenance(self):self.record('sharing')['provenance']['source_ids']=[b.PREFIX+'x1'];self.invalid()
    def test_empty_provenance(self):self.record('sharing')['provenance']['source_ids']=[];self.invalid()
    def test_dangling_relationship(self):self.record('x1')['relationships'][0]['target_id']='absent';self.invalid()
    def test_missing_units(self):del self.record('table2')['experiment']['rows'][0]['metrics'][0]['unit'];self.invalid()
    def test_unit_mismatch(self):self.record('table2')['experiment']['rows'][0]['metrics'][0]['unit']='percent';self.invalid()
    def test_percent_range(self):self.record('table2')['experiment']['rows'][0]['metrics'][2]['value']=101;self.invalid()
    def test_negative_metric(self):self.record('table2')['experiment']['rows'][0]['metrics'][0]['value']=-1;self.invalid()
    def test_duplicate_metric(self):r=self.record('table2')['experiment']['rows'][0];r['metrics'].append(copy.deepcopy(r['metrics'][0]));self.invalid()
    def test_duplicate_row(self):e=self.record('table2')['experiment'];e['rows'].append(copy.deepcopy(e['rows'][0]));self.invalid()
    def test_inconsistent_columns(self):self.record('table2')['experiment']['rows'][0]['metrics'].reverse();self.invalid()
    def test_timestamp_format(self):self.record('unetr')['created_at']='yesterday';self.invalid()
    def test_private_record(self):self.record('x1')['visibility']='private';self.invalid()
    def test_self_approval(self):self.record('x1')['status']='approved';self.invalid()
    def test_script_url(self):self.record('unetr')['source']['url']='javascript:alert(1)';self.invalid()
    def test_private_url(self):self.record('unetr')['source']['url']='https://drive.google.com/file/d/example';self.invalid()
    def test_wrong_version(self):self.data['schema_version']='0.0';self.invalid()
    def test_unknown_template_reference(self):
        with self.assertRaises(ValueError):b.render('{{claim:unknown}}',b.validate(self.data,self.schema))
    def test_numeric_tampering(self):
        idx=b.validate(self.data,self.schema);s=b.page(b.render((P/'lesson.html.in').read_text(),idx))
        with self.assertRaises(ValueError):b.check_output(s.replace('>87.22<','>97.22<'),idx)
    def test_local_anchor_tampering(self):
        idx=b.validate(self.data,self.schema);s=b.page(b.render((P/'lesson.html.in').read_text(),idx))
        with self.assertRaises(ValueError):b.check_output(s.replace('href="#start"','href="#missing"'),idx)
    def test_escape_source_claim(self):
        self.record('sharing')['claim']['text']='<script>alert(1)</script>'
        s=b.render('{{claim:sharing}}',b.validate(self.data,self.schema))
        self.assertNotIn('<script>',s);self.assertIn('&lt;script&gt;',s)
    def test_bounded_contexts(self):
        idx=b.validate(self.data,self.schema);a=b.context('A',idx);f=b.context('F',idx)
        self.assertEqual(len(a['records']),4);self.assertGreater(len(f['records']),4)
        for name in b.TASKS:
            pack=b.context(name,idx);present={r['record_id'] for r in pack['records']}
            self.assertEqual(pack['execution']['independent_agent_runs'],0)
            for r in pack['records']:
                self.assertTrue(set(r['provenance']['source_ids'])<=present)
                self.assertTrue({x['target_id'] for x in r['relationships']}<=present)
    def test_rebuild_changes_both_views(self):
        # Mutation is a synthetic test, not an alternative scientific result.
        self.record('table2')['experiment']['rows'][-1]['metrics'][-1]['value']=88.22
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);b.build(p,self.data)
            for name in ['lesson','report']:
                s=(p/'human'/f'{name}.html').read_text();self.assertIn('>88.22<',s);self.assertIn('>9.87<',s);self.assertNotIn('>87.22<',s)
            pack=b.load(p/'agent/B.json');e=next(x for x in pack['records'] if x['record_type']=='experiment')
            self.assertEqual(e['experiment']['rows'][-1]['metrics'][-1]['value'],88.22)
    def test_deterministic_build(self):
        with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as c:
            x=b.build(Path(a));y=b.build(Path(c));self.assertEqual(x,y)
    def test_metadata_exclusion(self):
        idx=b.validate(self.data,self.schema);s=b.page(b.render((P/'lesson.html.in').read_text(),idx))
        with self.assertRaises(ValueError):b.check_output(s+'author_self_check',idx)

if __name__=='__main__':unittest.main(verbosity=2)
