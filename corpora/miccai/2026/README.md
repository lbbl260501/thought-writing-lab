# MICCAI 2026 · 论文来源与全文多尺度分析（B 组）

[Issue #3](https://github.com/lbbl260501/thought-writing-lab/issues/3) · [Draft PR #19](https://github.com/lbbl260501/thought-writing-lab/pull/19) · 长期 Program #7

## 最新进展：不仅分析怎样立论，也分析具体怎样写

Batch 03在原有40篇来源、5篇引言精读基础上，完成了**2篇科学正文的全文阅读与宏观—中观—微观分析样本**：FRODO/Paper5533与微波消融替代模型/Paper4859。另建**70条带定位的词汇与搭配记录、16种功能句式**，并将句子分析接回段落与章节。

这次不扩大书目数量，先补足分析深度。2篇全文样本包含在原来的5篇引言对象中，不能重复计为新增论文；也不是40篇全部完成全文精读。

## 阅读入口

| 内容 | 入口 | 实际范围 |
|---|---|---|
| 全文多尺度分析总览 | [fullpaper/batch03/README.md](fullpaper/batch03/README.md) | 三层分析如何相接；来源与原创示范怎样区分 |
| 分类论文全文 | [PAPER5533.md](fullpaper/batch03/PAPER5533.md) | 题名到结论的21个功能单元；主题词链、方法动词、语法与结果解释 |
| 规划论文全文 | [PAPER4859.md](fullpaper/batch03/PAPER4859.md) | 23个功能单元；物理、预测、决策和验证对象的语言区别 |
| 专业词汇与搭配 | [LEXICON.md](fullpaper/batch03/LEXICON.md) | 70条记录，涵盖专业术语、动词、名词、形容词、复合修饰语和副词 |
| 句式与段落分析 | [SENTENCE_PATTERNS.md](fullpaper/batch03/SENTENCE_PATTERNS.md) | 16种功能句式、语态/时态/非谓语/名词化、原创贯通示范 |
| 本轮审校与范围 | [AUDIT.md](fullpaper/batch03/AUDIT.md) | 完整阅读范围、图表检查、定义与证据的文字疑点、交接事项 |
| 上一轮引言精读册 | [introductions/CASEBOOK.md](introductions/CASEBOOK.md) | 5篇完整引言与部分方法/结果回查 |
| 当前论文总索引 | [sources.csv](sources.csv) | 40个不同官方PaperID；保留上一轮已登记的保守阅读层级 |
| 引言证据定位 | [introductions/evidence.jsonl](introductions/evidence.jsonl) | 上一轮5条页码、章节和图表记录 |
| 第二批选择逻辑 | [BATCH02_SELECTION.md](BATCH02_SELECTION.md) | 21篇新增来源的比较分组与质量例外 |
| 上一轮覆盖说明 | [coverage.md](coverage.md) | Batch02采样偏差、阅读深度分布及来源限制 |
| 第一批摘要案例 | [problem_framing_cases.md](problem_framing_cases.md) | 历史10例摘要分析，不是最新阅读状态表 |

## 本轮新增的分析原则

主题词不只按频率排列，还要看它们怎样组织研究对象。动词连同主体和客体学习；名词区分具体对象与承接前文的概念；修饰语区分对象限定与评价判断；句式必须说明它在当前段落完成了什么动作。

三层在同一对象上连接：**全文主张 → 段落任务 → 句子动作 → 词汇与搭配 → 返回实验或论证位置**。既分析引言，也分析方法、实验设置、结果讨论、结论和图表题注。原文没有独立讨论章节时，不造出一个假章节。

“原文出现过”“两篇均出现”和“建议积累”分开。没有建立代表性词频口径前，不把本轮教学选择称为MICCAI高频规律。整句原创例子不伪装成作者引文。

## 历史状态与新增全文层

Batch02主索引登记为29条元数据级、6条摘要/部分评审级、5条引言级。Batch03不整体重写该CSV，而以新目录补充其中两篇的全文语言分析范围，供HQ审校后并入正式源记录。5篇引言和首批10例合计仍为11篇不同分析对象，本轮未增加这个去重计数。

原有引言册仍保留重要区分：模态信息角色不等于共享/特异专家；单次预测速度不等于决策质量；零样本任务训练不等于全流程无标注；已有阈值选择、医生盲评或带先验对照不应被重新列作缺项。新增的文字/公式疑点另列在Batch03审校文件，不以批评清单取代语言教学。

## 边界

全文语言分析不等于实验独立复现，也不等于每个句子已穷尽标注。DOI和Oral/Spotlight未逐条确认。样本是目的性选择，不用于统计会议总体趋势。

公开内容仅有安全元数据、来源链接、有限短引与原创分析；不镜像论文PDF。B只在`agent/miccai26/issue-3`的`corpora/miccai/2026/`内工作，由HQ/Q审查后整合，不自行合并，不修改2025、共享规范、正式编号或私人Master Catalog。
