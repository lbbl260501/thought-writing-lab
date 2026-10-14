# 来源核验表与主张来源纪律｜Issue #5

核验时间：2026-10-14。本表记录 **本轮 D 对话真正访问并检查的范围**；先前全库已有的阅读笔记只作为参考，不可自动继承为本轮全文阅读。

| 临时条目 | 一手来源和定位 | 本轮证据深度 | 当前支持的事实边界 |
|---|---|---|---|
| draft:issue-5:case-01 | [MICCAI 2025 C²MAOT](https://papers.miccai.org/miccai-2025/0124-Paper2322.html) 的 Abstract 与 Reviews；[既有 pilot](../../corpora/miccai/pilot/PAPER-000001-C2MAOT.md) | ABSTRACT_AND_REVIEWS_VERIFIED | 三类挑战、提出的两机制及作者报告的结果；PDF 未在本轮重读 |
| draft:issue-5:case-02 | [MICCAI 2025 CAMOS](https://papers.miccai.org/miccai-2025/0320-Paper1908.html)；[原文 PDF](https://papers.miccai.org/miccai-2025/paper/1908_paper.pdf) 引言印刷第 2 页 | INTRODUCTION_READ (selected) + REVIEWS | 由骨驱动到目标面貌预测的流程、作者的实验数据规模；不包含可执行骨移动计划的验证 |
| draft:issue-5:case-03 | [MICCAI 2025 Locor](https://papers.miccai.org/miccai-2025/0636-Paper1747.html)；[原文 PDF](https://papers.miccai.org/miccai-2025/paper/1747_paper.pdf) 印刷第 2–4 页，Methods 式(3)(4) | METHODS_PARTIALLY_READ | 全球/局部函数依赖、局部系数与全局学习基函数；未审计全部实验 |
| draft:issue-5:case-04 | [MICCAI 2026 MMA-LTS](https://papers.miccai.org/miccai-2026/0659-Paper1236.html) 的 Abstract 与 Reviews | ABSTRACT_AND_REVIEWS_VERIFIED | 缺失模态组合身份与空间校准假设；公式和效果未独立复核 |
| draft:issue-5:case-05 | [MICCAI 2026 CDFP-Net](https://papers.miccai.org/miccai-2026/0157-Paper2844.html) 的 Abstract 与可见评审 | ABSTRACT_AND_REVIEWS_VERIFIED | PET 锚点引导 CT、扩散先验和 MA-MIP 设计；病例级资源选择不是本文已证实内容 |
| draft:issue-5:case-06 | [Geirhos et al., Nature Machine Intelligence 2020](https://www.nature.com/articles/s42256-020-00257-z) 的元数据和 Abstract；[arXiv 摘要](https://arxiv.org/abs/2004.07780) | ABSTRACT_VERIFIED; Perspective | Shortcut 是跨基准不迁移的预测规则概念；不能据此认定具体模型存在 shortcut |
| draft:issue-5:case-07 | [Arjovsky et al., arXiv:1907.02893](https://arxiv.org/abs/1907.02893) 的 Introduction、§2、§3 Definition 3 | INTRODUCTION_AND_FORMULATION_READ | 表示+共同最优头的不变性原则；不意味着普遍因果恢复保证 |
| draft:issue-5:case-08 | [Koh et al., ICML/PMLR 2021](https://proceedings.mlr.press/v139/koh21a.html) 的 Abstract；[研究团队解读](https://www.robotics.stanford.edu/blog/wilds/) | ABSTRACT_VERIFIED | 论文摘要所述 10 数据集和真实分布偏移研究动机；未逐项复现实验 |

**注意**：部分通用协议使用 `metadata_verified`、`abstract_and_reviews_verified`、`introduction_read`、`fulltext_audited`。本表采用更细的可读范围说明而不暗示新的全局 schema；正式规范由 HQ 决定。

## 四种主张不得混淆

- **AUTHOR_CLAIM**：作者在所核读原始来源里确实声称的结果或动机；不等于本组复现事实。
- **REVIEWER_OPINION**：官网评审对新颖性、临床转化或实验充分性的意见；不能作为判定缺陷成立的充分证据。
- **ANALYST_INTERPRETATION**：D 对研究对象、隐含假设、问题改变和论证关系的解释；需接受原文与异域挑战。
- **TRANSFER_HYPOTHESIS / PROPOSED_EXPERIMENT**：将已读思想迁到 PET/CT、VSP、遥感等新任务的设计；尚无运行结果，不得写为已证明的结论。

## 首轮尚未完成的核验

1. 对 C²MAOT、MMA-LTS 和 CDFP-Net 进行逐段正文核读、关键公式和表格核对，并比较真实训练/推理开销与统计检验。
2. CAMOS 的“optimal”目标定义、专家/患者有效性及手术可行性评估，需要回到方法和实验全文，避免被英语形容词误导。
3. Locor 的 J 与局部窗口敏感性、配准计算延迟及跨病例方差，需要方法/实验全篇核验。
4. IRM 的理论前提与经典反例尚需用原文证明及后续批评文献进行对抗复核；不能宣称因果充分性。
5. WILDS 基准的具体外部域分割方式及数据集演变应独立检查；外部域 ≠ 任意真实未来域。
6. 跨 C/A/B 的候选条目去重由 HQ 决定；8 张方法卡本身不自动生成 8 个 `MOVE-` 稳定编号。
