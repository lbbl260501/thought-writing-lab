# R02 · 解释与参考答案

[返回练习](WORKSHOP.md)。示范均为原创教学表达，不是所引论文的原句。不同答案可以成立；应解释每一项修改如何改变命题与读者理解，而不是把答案当成固定模板。

## 两阶段方法动机：一种写法

> Inputs can differ in the quality of the evidence they provide for prediction. An initial quality estimate can expose this variation, but it does not specify how the available computation should be used. We therefore separate quality assessment from budgeted route selection. The first stage characterizes the input, while the second uses that assessment to choose among processing routes under a fixed budget. The quality estimate thus informs a resource decision rather than serving only as a descriptive score.

这里有三层关系：输入差异建立任务；质量估计不等于资源决策；第二阶段承接第一阶段的输出。句末说明两者为什么连接，没有增加分别训练的实现设定，也没有提前许诺性能优势。

## 题1 · 对观察直接作陈述

> The model achieved a mean Dice of 0.842 on the evaluated test set.

删去套叠可能性，但保留测试范围。这里并没有增加“显著优于”“适用于所有患者”等判断。直接报告给定观测，不需要为未知的推广能力同时辩护。

## 题2 · 用对象与条件界定研究

> We study case-dependent computation allocation with complete, registered multimodal inputs.

在给定开头中，后一句逐项否认通常重复已明确的范围。若论文确实正在与缺失模态学习比较，或完整输入是执行方法的必要条件，则该区别应放在相关比较或适用条件段说清楚。是否保留取决于功能，不取决于该句是否包含否定词。

## 题3 · 保留三个不同的对象

> A fixed architecture can produce input-dependent modality interactions; this does not by itself imply input-dependent computation allocation.

FRODO 第4页将 FLAIR 特征产生的空间调制场用于 QSM 特征。因此，固定的是结构，并不能推出每个输入的作用相同。输入相关调制又不必改变处理路径或运算量。需要分别讨论结构、交互行为和计算策略；本课不从调制权重推导真实模态价值。

核读位置：[官方论文5533，第4页](https://papers.miccai.org/miccai-2026/paper/5533_paper.pdf#page=4)。这不是要求你弱化一个正确主张，而是纠正原句把不同对象混为一谈。

## 题4 · 改正推论，保留已有价值

> AI-assisted submissions received higher scores in the evaluated course. Whether this improvement carries over to unassisted reasoning remains an open question.

第一句保留已有成果；第二句仅处理原稿正在跨越的能力判断。也可以将第二句放在后文研究问题处，而在本段只报告成品质量。不能写成“AI 没有改善学习”，因为尚未测量并不等于无效。

## 题5 · 先查资料，不向正文写入猜测

正文外查询示例：

> Please identify any matched-budget controls in the full paper or supplement and clarify which contribution each comparison tests.

下一步是读取实际对照与比较条件。已经存在的实验应纳入解释；真正缺少的控制才进入补充实验建议；如果输入仍不足，保留为待核问题，而非在作者正文断言研究没有证据。一个证据表或摘要不能自动替代全文核查。

## 题6 · 比较单位决定贡献的写法

> The revised system achieved better performance on the shared test set following changes to the architecture, training procedure, and preprocessing.

following 在这里报告改动后的系统结果，不声称每一项改动都已被确定为独立的增益来源。原句把全部提升归给某一模块；改稿保留整体改善，同时使归因对象准确。

一种有区分力的后续比较是：在更新后的训练与预处理方案保持不变时，替换或去掉目标模块，再评价系统表现。还可以在原基础系统中做对应对照以检查交互。这里的任务是区分整体系统效果与组件的归因，不要求所有优化因素天然可加。

来源启发：[nnU-Net Revisited，§2 Pitfall 1](https://papers.miccai.org/miccai-2024/paper/2847_paper.pdf#page=3)。原文还包含具体资源与预训练条件，不能概括为所有实验因素完全相同。

## 双向编辑量表：不要只奖励删词

| 检查对象 | 成功表现 | 需要修订的表现 |
|---|---|---|
| 事实与范围 | 数值、对象和比较条件保持；必要条件仍可见 | 加结果、改对象，或删去改变结论的条件 |
| 作者判断 | 有根据的结果、解释或假设被清楚表达 | 无依据地加强，或为显得谨慎而否定作者 |
| 句群关系 | 新句解释、区分、承接或推进前句 | 套式重要性、重复警告、并列模块清单 |
| 读者任务 | 读者能说出本段论点及其根据 | 正文变成审稿清单或不停自我澄清 |

不要以 hedging 词数或自动审稿分作为单一选择标准。本讲练习的目标包含保留、压缩、正面改写与纠错四种不同动作。

## 最小复习

次日不看本页，完成一题新情境：一个系统在参数数量减少后运行时延反而上升，作者写它“更高效”。请先明确效率的评价坐标，再写一句成立的结果与一句研究意义。允许突出参数节省，但必须保留改变部署判断的时延结果。

个人原稿和作答留在私有学习记录中。本文件没有记录任何人的完成、分数或掌握程度。
