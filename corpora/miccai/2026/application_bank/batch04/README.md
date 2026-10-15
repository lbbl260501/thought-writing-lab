# 应用词句库 · Batch 04

Issue #3 / Program #7。由用户提出的新重点：借鉴词汇书、好词好句本与搭配书，建立可规模化、重应用、重关联、可转成学习PDF的素材库。不是把孤立词和句子排成清单。

## 本次已生成的学习产品

本次对话中已生成《应用词句本01》试用版：学习册41页，独立答案册7页。完整源码包包含结构化数据、学生Markdown、独立答案与PDF生成脚本。

范围：36张应用卡；144条搭配/框架记录（不同英文字符串143条）；72组词条双语例句；72条带类型的有向词间关系；12类功能句式；6个连续段落；18道练习及讲解。两个论文短片段另有精确定位，全部完整示范句为原创假设情境，不报告真实新增实验。36张卡部分复用B03词条，不与原70条直接相加。

## 远程同步范围——请勿混淆

本目录当前保存**建库和成册规范、两张完整结构化示例卡、产物交接清单**。完整36卡数据、全部学习文本及PDF生成器作为本轮对话的源码ZIP附件交付；**尚未全部写入本Git分支**。41页PDF与7页答案PDF也只在本次对话交付，未建立GitHub Release或Drive副本。

因此，本README是精确交接，不应被当成“所有词句数据已经远程同步”的证明。后续完整源数据入库应依据附件内容和校验值，由本任务继续提交或HQ整合。没有自动后台同步。

## 六个应用入口

1. 把观察变成研究问题：characterize / distinguish / account for / limitation / heterogeneous / task-specific。
2. 把信息关系写成模型操作：encode / condition / modulate / preserve / representation / complementary。
3. 把预测与方案选择分开：estimate / predict / infer / optimize / surrogate / constraint。
4. 让实验描述可复查：evaluate / compare / isolate / assess / protocol / held-out。
5. 把“更好”拆成比较：yield / outperform / comparable / reduction / trade-off / consistently。
6. 从发现走向解释：indicate / suggest / support / generalize / robust / implication。

## 库的基本关系

**写作意图 → 词义选择 → 搭配与框架 → 双语应用句 → 段落动作 → 独立练习。**

词间的“关联”需要类型：近义辨析、动作与产物、前后步骤、关系与实现、跨章节复用、研究主题。不能把condition与modulate简单当作可互换同义词，也不能把不同章节重现的同一词重复计数。

专业术语库继续借用B03的来源定位；本批重点是把可迁移表达做成可练习产品，而非新增36个互不重复的医学专业术语。未进行全会议词频研究。

## 内容与排版分开

学生正文只保留解释、双语例句、辨析、关联、题目和查阅索引。出处审计、统计口径和进度日志放在编辑层；答案独立。源码包中的JSON/JSONL负责保存关系，Markdown与PDF负责学习呈现。不同版本可围绕词汇、搭配、好句、章节或研究主题重新选编，无需重写每张卡。

参见[建库规范](BANK_DESIGN.md)、[两张结构化示例卡](CARD_SAMPLE.json)及[交接清单](HANDOFF.json)。

## 研究来源与边界

参考Cambridge《English Collocations in Use Intermediate》官方节选的语境记录和练习组织；参考Manchester Academic Phrasebank的章节/交际功能导航，以及ColloCaid论文中的词条—搭配—例句关系。未复制书籍练习或批量镜像论文原句，未声称安装过ColloCaid，也没有用户学习成绩。

B仍只在本分支的`corpora/miccai/2026/`内工作；公共词典、稳定ID、正式课程、私人学习日志由HQ治理。PR #19继续保持草稿，未合并。
