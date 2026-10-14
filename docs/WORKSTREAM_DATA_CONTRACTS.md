# 跨研究组数据契约 · Workstream Interfaces v2

科研知识库最大的协作难点不是文件冲突，而是不同对话产出的概念、论文结论和练习**彼此不能复用**。因此每组必须交付可追溯对象。

## 上下游交付

| 交付物 | 上游 | 下游 | 最小要素 |
| --- | --- | --- | --- |
| Source Record | A/B | C/D/E/F/HQ | 来源标识、正式网址、版本、作者、核读范围、许可说明 |
| Argument/Paragraph Note | A/B | C/D | 章节定位、作者原主张、叙事动作、实验依据、待核疑问 |
| Language Move | C | F/HQ | 科学主体/动词/客体、语义与句法、使用条件、对比实例 |
| Research Move | D | F/HQ | 核心问题、定义、假设、替代解释、判别性实验、适用边界 |
| Cross-domain Mechanism | E | C/D/F | 原著版本与章节、原有问题、可迁移操作、类比失效条件 |
| Daily Lesson | F | HQ/Q | 教学目标、先修、讲解、独立小题、研究迁移、分离答案 |
| Audit | Q | HQ/作者 | 检查的 PR/commit、位置、严重度、理由、可执行修改 |
| Personal Feedback | HQ | HQ | 私人原稿、修订、错误、间隔复习、真实迁移表现 |

## 核心证据规范

区分 `METADATA_VERIFIED`、`ABSTRACT_VERIFIED`、`INTRODUCTION_READ`、`FULLTEXT_AUDITED` 的阅读范围，并将 `AUTHOR_CLAIM`、`REVIEWER_OPINION`、`ANALYST_INTERPRETATION` 和 `TRANSFER_HYPOTHESIS` 分开。

“文章作者说过”不等于“实验事实得到独立复现”；“原著思想与新问题存在联系”不等于“原著证明了新理论”。

## 编号与去重

子对话只使用可核验的外部 ID（如 `miccai:2025:2322`）或临时 ID（如 `draft:issue-24:move-03`）；**不自行分配全局的 PAPER/MOVE/EX 序列号**。HQ 核查 DOI/ISBN、题名、出版版本、同义术语与重复论证，再在中央索引分配永久编号。

已存在的稳定编号不得重置、复用或被未经审查的子对话覆盖。

## 对象文件的推荐结构

```yaml
local_key: "draft:issue-24:case-03"
source_key: "miccai:2025:2322"
official_url: "https://papers.miccai.org/miccai-2025/0124-Paper2322.html"
checked_scope: "abstract_verified"
locator: "Abstract"
source_claim: "source-based paraphrase, not a new result"
claim_status: "AUTHOR_CLAIM"
language_move: "CONTRAST"
science_move: "QUESTION_ASSUMPTION"
possible_application: "Write a short contrast and a testable question"
interpretation_status: "ANALYST_INTERPRETATION"
open_questions:
  - "What would falsify this explanation?"
```

以上只是格式实例，不表示已核验该文献的具体科学主张。无证据的数据字段可以留空，不得补造页码、实验或引用。

## 交接时必须说明

1. 具体修改了哪些文件（相对路径）和 Git commit。
2. 实际访问了什么原始资料、核读到什么深度。
3. 哪些判断来自作者、审稿人或本库解释。
4. 哪些内容可以迁移到语言、理论、教材；需要什么后续检验。
5. 哪些存在重复、定义冲突、版权与来源风险。
6. 提出给主对话的明确决策事项，避免“已完成，请查收”的模糊交接。

## 处理分歧的原则

- 事实不一致：回原文、版本与数据。
- 科学解释不一致：保留相互竞争的假设和前提。
- 术语与分类不一致：HQ 发布公共词典的版本化决定。
- 教材难度不一致：以真实学习者独立作答结果为反馈，必要时保留分层版本。
- 个人数据与公开内容不一致：以私有权限边界为先，不把用户作答公开到仓库。

详细参见 [Operating Model](OPERATING_MODEL_V2.md)。
