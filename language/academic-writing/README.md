# C · Academic English, Discourse & Scientific Rhetoric

**Program:** [#8](https://github.com/lbbl260501/thought-writing-lab/issues/8) · **Finite task:** [#4](https://github.com/lbbl260501/thought-writing-lab/issues/4) · **Draft PR:** [#21](https://github.com/lbbl260501/thought-writing-lab/pull/21)。研究候选材料，未合并到main。

## 当前入口：v0.2 原文细读与分类研究

从 [v0.2读本入口](v02/README.md) 开始。本轮增加12篇科研样本的短摘录细读，并实际复核6篇旧MICCAI样本的相关页段。新版把原文、上下文释读、本库解释和原创改写分开；主分类细化为8个家族、24个子类，另记关系、证据、语言、信息与语境。

| 阅读材料 | 用途 |
|---|---|
| [原文细读A](v02/CLOSE_READING_A.md) | nnU-Net、MedSAM、Metrics Reloaded、Aurora、LiteNeXt、UNETR++：贡献位置、目标属性、评价依据与设计依赖 |
| [原文细读B](v02/CLOSE_READING_B.md) | Models Genesis、SAM、MAE、校准、DyCON、公平性：类比、问题链、信号用途与推论边界 |
| [分类手册](v02/CODEBOOK.md) | 分类定义、纳入/排除标准、近邻反例与旧标签迁移 |
| [实际核读与修订记录](v02/AUDIT_AND_REVISION.md) | 来源、阅读版本、访问失败、纠错与后续待检验事项 |
| [结构化索引](v02/CORPUS.json) | 18篇科研源、3篇方法参考、24个候选类别与12条核心标注索引 |

**重要范围：** 选读源文不等于全文审计；作者报告不等于独立复现。Models Genesis本轮因正文读取问题仅可靠核读摘要。作者稿与出版社最终稿不混同。分类尚无独立复标一致性或真实学习者效果结果。

## 研究命题

科研写作不是高级词汇与模板句的简单叠加。应同时追问：科学命题是什么；语法结构与语义角色是否准确；新信息怎样进入；此处完成了什么叙事动作；在当前读者、体裁和证据条件下是否成立。

核心单位是**语境中的科学命题与表达动作**。主谓宾是分析入口，不是全部句法：被动、系表、非谓语与疑问句不能硬填成相同结构。修辞策略可以明确定位贡献和突出有利证据，关键是不能在改写中悄悄改变主张对象、比较范围或条件。

## v0.1历史材料：保留为释写与训练资源

| 文件 | 继续保留的用途 |
|---|---|
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | 首轮来源记录；实际复核与更精确范围以v0.2审计为准 |
| [MOVE_TAXONOMY_V0.md](MOVE_TAXONOMY_V0.md) | 早期候选分类；新分类见v0.2，保留映射而不静默覆盖 |
| [SOURCE_GROUNDED_CASES_24.md](SOURCE_GROUNDED_CASES_24.md) | 24条本库独立英文释写，不是作者原句，不用于原文句法/词频统计 |
| [EXERCISES_10.md](EXERCISES_10.md) | 独立写作任务 |
| [EXERCISE_ANSWERS_10.md](EXERCISE_ANSWERS_10.md) | 单独示范答案与理由；仍需结合新版证据边界检查 |
| [HANDOFF_ISSUE4.md](HANDOFF_ISSUE4.md) | 首轮交接历史；新增研究状态见v0.2审计和PR讨论 |

## 如何使用

先在原文卡中读一个完整的局部论证，再自行判断主要动作和最近邻类别。对照分类理由，尝试改变一句表达，检查是否改动了科学含义。最后再做相应的释写训练。不要把参考答案视为唯一标准，也不要把已生成材料视为学习者已经掌握。

公开库保存原创分析、可核验短摘录与安全的来源信息，不保存原始受限PDF、私人文件链接、学生原稿或正式全局编号的自行分配。主控负责独立复核安排、中央分类整合和main合并。
