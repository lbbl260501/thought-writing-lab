# MICCAI 2025 · A 组语料收集（Issue #2）

**范围**：本目录是 `Program #7 → Issue #2 → agent/miccai25/issue-2` 的 Cycle 0 交付。它保留可核验的文献元数据和原创分析，不镜像论文 PDF，也不生成正式全局 `PAPER-/MOVE-/EX-` 编号。

## 本次实收情况（2026-10-14）

- **13 篇不同的 MICCAI 2025 官方论文**已经逐一访问其官方网页，并核对题名、作者、官方论文入口、PDF 链接和 DOI；其中 **10 篇为独立于共享 pilot 的新案例候选**，其余 3 篇同共享 `corpora/miccai/pilot/pilot_catalog.csv` 有重叠（2322、1908、1747）。
- 本次实际核读 **3 篇 PDF 的 Introduction（正文 pp.1–2）**：1316、1381、5008；不是“完整全文审计”。
- 提交 **10 篇跨任务原创叙事/论证动作分析**，见 [cases.md](cases.md)。对仅访问摘要的论文，只分析摘要的结构，不声称已经核读 Introduction。
- 官网列出的 2025 主会收录规模是 **1,027 篇**；本批 **13/1,027** 是目的性抽样，**绝非全量索引**、不代表总体频率，不应以本批估计 MICCAI 写作规范。

## 数据与阅读入口

| File | 内容 |
| --- | --- |
| [index.csv](index.csv) | 逐篇官方核验的来源记录、核读深度、暂定研究主题与候选动作 |
| [cases.md](cases.md) | 10 个“事实—作者主张—分析者解释—审稿意见—迁移”的案例 |
| [PROVENANCE.md](PROVENANCE.md) | 选样、来源、核验等级、尚待检查的字段和复核方法 |
| [DEDUP_AND_HANDOFF.md](DEDUP_AND_HANDOFF.md) | 以官方 Paper ID 去重、与共享 pilot 对照、给 C/D/HQ 的交接 |

## 核验与知识边界

- `source_id` 采用临时可核验外部键 `miccai:2025:<paper_id>`。全局正式编号由 HQ 分配。
- `verification_status=metadata_verified` 对只核实官方页、摘要或局部评审的记录采用**保守状态**；真实查阅范围另记于 `checked_scope`，不会把摘要核读写成引言核读。
- `verification_status=introduction_read` 仅对本次确实打开并检查 PDF Introduction 的三篇使用。
- `presentation_type` 为空白：本轮未逐项核对官方 Oral/Spotlight 日程。
- `doi` 来自每篇 MICCAI 官方专页列出的 SpringerLink DOI，不从序号推造。
- PDF、出版社附件、私人 Drive/Zotero 数据与受限全文均未进入本目录。

## 重要提醒

本批优先刻意覆盖不同论证类型：**既有能力与未解决问题之间的落差、理论推广、问题单位重定义、评价轴转换、临床约束下的资源分配、审稿人挑战作者主张**。它是后续大规模索引和分层比较的质量基线，而非随机样本。正式比较研究须独立制定分层抽样框并核验覆盖率。

官方索引：[MICCAI 2025 Open Access](https://papers.miccai.org/miccai-2025/)。
