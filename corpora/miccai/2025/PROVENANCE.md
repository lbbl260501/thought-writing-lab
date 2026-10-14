# 来源和证据核验记录 · MICCAI 2025 A / Issue #2

## 确切的官方入口

- 主会官方列表：https://papers.miccai.org/miccai-2025/
- 本轮 13 篇官方专页与 PDF URL：逐条在 [index.csv](index.csv) 中列出。
- 三篇 PDF Introduction 已实际核读： [1316](https://papers.miccai.org/miccai-2025/paper/1316_paper.pdf)、[1381](https://papers.miccai.org/miccai-2025/paper/1381_paper.pdf)、[5008](https://papers.miccai.org/miccai-2025/paper/5008_paper.pdf)，均核对 PDF **pp.1–2**；不是全篇核读。
- 2025 主会目标总量 **1,027** 来源于本仓库共享 `corpora/miccai/README.md` 所记的官方统计口径；**这次没有对官方全页逐条自动重新计数**，因此本批的覆盖率分母使用“既有项目口径”，非本批再次独立计数的结果。

## 为什么选这些论文

本轮不是从题名表自动全抓取，而是质量优先的**分层探索性（目的性）样本**：报告生成、4D 心脏生成、患者个体化、统计建模、临床分诊、术中配准、OOD 评价、实时 US 配准、按需影像采集和医学推理。另把共享 pilot 的 3 篇 2025 论文纳入索引核对，**不重复新增深度案例**。

目的：验证“官方 metadata → 来源范围 → 可审稿的叙事动作 → C/D 可迁移输入”的数据链路，而不是推断 MICCAI 的方法/叙事流派频数。

## 核验层级

| 层级 | 数量 | 可声称已完成 | 不可声称 |
| --- | ---: | --- | --- |
| 官方元数据、页面摘要已逐一核对 | 13 | 题名、作者、官方页/PDF 链接、网页所列 DOI、摘要陈述 | 每篇全文阅读、实验复现 |
| 有选择地核对公开评审部分 | 6 | 仅指向已明示的评审论点，标成 REVIEWER_OPINION | 评审正确或所有评审意见已读 |
| PDF Introduction pp.1–2 已打开核读 | 3 | 三篇引言的观察、结构与语义动作 | 方法、结果及附录的全篇审计 |
| 研究论点形成原创分析 | 10 | 初步的分析者解释、写作迁移建议 | 这些解释已经得到独立双人复标 |

`verification_status` 采用共享标注指南枚举；对于“官方页面已核对摘要，但没有核读论文 PDF”的情况，保守写作 `metadata_verified`，实际访问范围在 `checked_scope`。未来若统一 schema 支持 `abstract_verified`，由 HQ 调整，不在分支自行更改共享规范。

## 科学与伦理边界

- `AUTHOR_CLAIM` 是论文作者对结果的叙述，不等于本库独立复现。
- `REVIEWER_OPINION` 是网站展示的某条评审意见，不等于最终科学事实。
- `ANALYST_INTERPRETATION` 是原创叙事/论证重构，不能当作原文引句。
- `TRANSFER_HYPOTHESIS` 是待实验检验的跨领域迁移，不强行宣称已有效。
- 不把公开摘要中的“first”、“clinically ready”、“causal”、“trustworthy”直接升级为已验证事实。
- 官网明确原版权由作者或其他权利人保留。本目录只使用可引用书目事实、链接和原创概括，没有保存 PDF/大段原文。

## 数据欠缺与下轮核验

1. **完整 1,027 条官方论文索引尚未收集**，本轮只有 13 条；未来必须明确抓取时间、字段覆盖、失败日志与去重策略。
2. `presentation_type` 仍空白，需按官方日程或会议信息独立核查；不得依据题目、发表质量猜 Oral/Spotlight。
3. 当前仅对部分公开 Review 做针对性阅读；若将审稿人质疑用于模型研发，应继续检查 rebuttal、meta-review 及正文对应实验。
4. 其余 7 篇新样本仅以官网摘要支持叙事结构分析，不能误写成引言句序/段序。
5. 本轮未运行重复标注/一致性实验，十张案例卡均为**第一位分析者的初始解释**，须 C/D/Q/HQ 异域复审。
6. DOI 虽由官网逐条抄录，跨 DOI 平台的出版记录再次校验留给正式入库时执行；不自行分配正式 PAPER 编号。

## 复核步骤

1. 打开 `index.csv` 所列每个 `official_url`，对照题名、作者、PDF 链接、DOI。
2. 以 `miccai:2025:<paper_id>` 去重，与共享 pilot 的官方 URL 去重。
3. 对三个 `introduction_read` 记录，在 PDF pp.1–2 对照 [cases.md](cases.md) 的段序。
4. 审查意见只追溯到作者论文专页的 Reviews 区域，与摘要作者论点分开。
5. 论文级争议与跨组分类冲突交给 Issue #2 / HQ #1；不在本分支修改全局标注词表。
