# 去重报告与主对话交接 · Issue #2

## 去重结果（2026-10-14）

- 本轮 `index.csv` 有 **13 行不同的论文记录**（表头之外）。
- **主键**：`miccai:2025:<official paper ID>`；本批内 13 个不同 ID、13 个不同论文官方 URL；**内部重复 0**。
- **与共享 pilot 的有意重叠 3**：`miccai:2025:2322`（C²MAOT）；`miccai:2025:1908`（CAMOS）；`miccai:2025:1747`（多模态局部函数依赖配准）。
- 新增于既有 pilot 之外的 2025 官方论文索引候选：**10**。与共享 pilot 的 3 篇重叠并不是待新增全球论文实体，故未来汇总不可简单相加为 16。
- **新增 10 张分析卡**只覆盖新增的 10 篇，未复制已有 pilot 研究笔记。
- 本轮未访问所有全局索引或私有 Master Catalog，不能断言仓库其他分支或私有库中不存在更多题名级重复。

## 精确交接

**Program**: #7 / **finite Issue**: #2  
**Task branch**: `agent/miccai25/issue-2`  
**Approved paths**: only `corpora/miccai/2025/`  
**Files**: `README.md`、`index.csv`、`cases.md`、`PROVENANCE.md`、`DEDUP_AND_HANDOFF.md`。

**Source depth**：13 个官方页面题名、作者、摘要、PDF/DOI；其中 3 篇官方 PDF 的 Section 1 Introduction pp.1–2；若干评审选段。**没有全篇审核或实验复现**。

**给 C 的待入库记录**：`draft:issue-2:language-06` 准确度与自动化双轴对照（1316）；`draft:issue-2:language-04` 包含为特例的理论扩张（1381）；`draft:issue-2:language-09` 按条件选择信息的句法（5008）。

**给 D 的待入库记录**：`draft:issue-2:science-03` 个体级信息聚合与因果干预的区分（0169）；`draft:issue-2:science-07` 现有能力与新的 OOD 评价轴（0815）；`draft:issue-2:science-10` 推理文字与忠实解释的差异（3267）。

**待主对话审核**：
- 这些临时 move/key 是否存在与既有 C/D 知识单元的重复？
- 是否批准下一 Cycle 先做**有可重复抽样规则的 50–100 篇新增 metadata 批次**，并将 PDF Introduction 深读与元数据扩张分成各自可审查任务？
- 是否由 HQ 校对 `metadata_verified` 下的摘要已核读状态，升级共享验证枚举？

## 风险清单

- 目的性选样偏向可清晰说明的问题，**存在 selection bias**；不允许统计“MICCAI 常用叙事”的比例。
- 当前摘录是少量、分散的公开评审选段，尚未复核整条最终审稿轨迹。
- 有些强表述是论文作者的主张（如因果、临床、解释忠实性），所有临床或数学上的推广均仍需正文方法/结果及外部实验支持。
- 当前 `README` / `PROVENANCE` 中的 1,027 为仓库已记录的官方主会口径，需后续全量核对确认。
- 独立语言/科学复标尚未开展，不能把本批视为审核完成的训练数据。

**下一步请求**：HQ 对 Draft PR 做 G0/G1 来源抽查、C/D/Q 做异域质疑，再决定是否合并与下轮分层扩展。本组**不自行合并 main 或操作私有 Google Sheets**。
