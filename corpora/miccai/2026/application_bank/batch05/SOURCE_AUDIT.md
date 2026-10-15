# Batch05 来源、计数与应用核查

2026-10-15。以下为作者自检，未经过独立教学效果测验。

## 来源与实际核读范围

| 来源 | 具体位置 | 本轮用途与边界 |
|---|---|---|
| Manchester Academic Phrasebank | https://www.phrasebank.manchester.ac.uk/writing-definitions/ | 概念定义与操作性定义的功能组织，不复制整张模板表 |
| Manchester Academic Phrasebank | https://www.phrasebank.manchester.ac.uk/discussing-findings/ ; https://www.phrasebank.manchester.ac.uk/using-cautious-language/ | 讨论功能、解释与范围；未把谨慎表达等同于取消主张 |
| Collins attribute | https://www.collinsdictionary.com/dictionary/english/attribute | 动词义、名词义及论元方向；释义概括与例句为原创 |
| Collins warrant | https://www.collinsdictionary.com/dictionary/english/warrant | 研究写作相关动词义及宾语；不声称覆盖所有词义 |
| Imai, Keele & Yamamoto (2010) | https://imai.fas.harvard.edu/research/files/mediation.pdf ; PDF pp.1–2 | 摘要与引言；中介路径、识别前提及敏感性；未核验全部定理。Statistical Science 25(1),51–71, DOI10.1214/10-STS321 |
| National Academies (2019), Chapter3 | https://www.nationalacademies.org/read/25303/chapter/6 | 计算复现定义及学科差异；本册约定不是所有学科的唯一用法 |
| MICCAI Paper1236 | https://papers.miccai.org/miccai-2026/paper/1236_paper.pdf | 完整引言pp.1–3、方法选段pp.3–5；查看p.2 Fig.1和p.5页面。只为语言/概念锚点，非全文审计 |
| MICCAI Paper4287 / SPEAR | https://papers.miccai.org/miccai-2026/paper/4287_paper.pdf | 摘要、完整引言和方法开头pp.1–2，页面视图已查看；非全文审计 |
| MICCAI Paper4853 | https://papers.miccai.org/miccai-2026/0502-Paper4853.html | 仅官方网页摘要；PDF超过本次工具大小限制，未记为引言或全文读取 |

Cambridge个别完整词典页返回403，没有记作完整词条核读；实际采用上述可读Collins条目。三篇MICCAI论文已在40篇总索引中，不新增科学来源ID，不整体升级其他条目。

## 原文与原创

只有两个简短片段作为原文：1236为10词，4287为8词。每篇不足25词。所有完整英语示范、题设数字、双语解释、连续段落与贯通研究均为原创教学假设；搭配和框架不是逐条的论文原句，也不是全会议词频研究。源码source_occurrence_claim标记为false。

因果词条区分association、attribution与mediation；匹配参数量不等于控制所有模型容量差异；校准不等于高准确率；同数据同代码的计算复现不等于新数据上的重复研究。允许明确报告题设改善，不把未测的机制、显著性、临床价值和外部范围写成已有结果。

## 计数与完整性

48个新主词条对第一册36词做不区分大小写精确去重，共84词。新192条搭配字符串不同；两册336条记录含334种不同英文字符串。新144条关系含48个跨册入口，连同第一册72条，共216条有向关系。所有引用目标存在。

本册96组词条双语例句、16类功能句式、8个单元段落、另4段贯通写作、36道编号练习均有数据。3处原文语境页的迁移提示另有答案，不计入36道题。所有限制字数的参考答案在题设范围内。新48词不与旧B03的70条观察记录简单相加。

## 排版和离线页

学习册63页，答案11页；全页文字边界、替代字符及内部链接目的页检查通过。学习册667个链接。查看全册缩略图和选定词条、练习、答案、尾页大图，未发现文字越界或黑色替代字；自动检查不等于所有语言已经审定。

离线HTML用Node作JavaScript语法检查，在系统Chromium通过set_content加载同一自包含HTML，测试84条初始结果、中文查询和跨卡跳转，无脚本报错。该浏览器环境禁止file://导航，未声称验证所有移动端文件预览器。页面不需要外部请求。

## 交付边界

完整JSON/JSONL、可编辑Markdown、PDF、离线检索页和生成器在本次对话源ZIP中。GitHub本目录只同步README、全部48卡紧凑索引、此审核和附件校验；不声称完整源库已同步。无字体文件、原论文PDF、原文全文抽取、检查截图、私人记录或全局ID。

请C/Q核查搭配自然度、概念方向、关联是否真正帮助应用和题目能否独立完成。PR保持草稿、Issue保持开放，B不合并。
