# Issue #4 · Original-source audit

核读日期：2026-10-14。以 MICCAI Society 2025 官方开放版本为依据，检查六篇主论文的**摘要与 Introduction 对应 PDF 页面**，并核对官方论文详情页。下列页码指 **PDF 显示的正文页码**，不是 Springer 合卷页码。未核读完整方法、实验、相关工作、审稿答复全文；所有算法效能属于作者主张，不代表本库复现。

| Key (not a global ID) | Paper / author lead | Official paper info · PDF · DOI | Verified scope / precise locator |
| --- | --- | --- | --- |
| miccai:2025:3770 | Li et al., *Uncertainty-Supervised Interpretable and Robust Evidential Segmentation* | [Info](https://papers.miccai.org/miccai-2025/0970-Paper3770.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/3770_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-05185-1_62) | INTRODUCTION_READ — Abstract p.1, §1 pp.1–2. |
| miccai:2025:3977 | Guo et al., *Edge-Aware Token Halting for Efficient and Accurate Medical Image Segmentation* | [Info](https://papers.miccai.org/miccai-2025/0276-Paper3977.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/3977_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-04965-0_18) | INTRODUCTION_READ — Abstract p.1, §1 pp.1–2. |
| miccai:2025:0496 | Ma et al., *Source-Free Domain Adaptation for Cross-Modality Cardiac Image Segmentation with Contrastive Class Relationship Consistency* | [Info](https://papers.miccai.org/miccai-2025/0843-Paper0496.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/0496_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-04971-1_54) | INTRODUCTION_READ — Abstract p.1, §1 pp.1–3. |
| miccai:2025:1764 | Shi et al., *FedAMM: Federated Learning for Brain Tumor Segmentation with Arbitrary Missing Modalities* | [Info](https://papers.miccai.org/miccai-2025/0329-Paper1764.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/1764_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-04984-1_20) | INTRODUCTION_READ — Abstract p.1, §1 pp.1–3. |
| miccai:2025:3902 | Mossina & Friedrich, *Conformal Prediction for Image Segmentation Using Morphological Prediction Sets* | [Info](https://papers.miccai.org/miccai-2025/0169-Paper3902.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/3902_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-04965-0_8) | INTRODUCTION_READ — Abstract p.1, §1 pp.1–2; §2 not audited. |
| miccai:2025:2131 | Huang et al., *E-BayesSAM: Efficient Bayesian Adaptation of SAM with Self-Optimizing KAN-Based Interpretation for Uncertainty-Aware Ultrasonic Segmentation* | [Info](https://papers.miccai.org/miccai-2025/0270-Paper2131.html) · [PDF](https://papers.miccai.org/miccai-2025/paper/2131_paper.pdf) · [DOI](https://doi.org/10.1007/978-3-032-05185-1_13) | INTRODUCTION_READ — Abstract p.1, §1 pp.2–3. |

## Verification distinctions

1. **Source fact:** a claim or distinction is present in the cited paper's actual Introduction/Abstract (e.g. FedAMM differentiates fixed client-level from sample-level missing modalities).
2. **AUTHOR_CLAIM:** the authors' model is said to address that problem; superiority, efficiency, safety, novelty and transfer are **not** independently demonstrated by our linguistic analysis.
3. **ANALYST_INTERPRETATION:** our grammatical/SVO/information-structure annotation does not automatically establish the source author's intended mental process.
4. **TRANSFER_HYPOTHESIS:** template use in PET/CT, robotic planning, forest change detection or examinations requires renewed domain truth checks.
5. **REVIEWER_OPINION:** the [public review section for E-BayesSAM](https://papers.miccai.org/miccai-2025/0270-Paper2131.html#reviews) contains disagreement over the breadth of novelty and the sufficiency of experimental comparison (Review #1). This is a meaningful warning about copying an author's superlatives, **not** a settled priority investigation.

## Copyright and corpus reproducibility

No original full sentences were harvested into this repository. The 24 English samples are **fresh analytical paraphrases** anchored to specific ideas and page/paragraph positions, not reproduced excerpts. The official HTML and PDF remain at their owners' links. A future source audit must re-check link availability, actual textual locators, copyright status, disagreements and journal-versus-conference genre before HQ integrates records.

## Open questions for A/B/Q

- A/B: Are these six works already catalogued or duplicated under other source keys? Please supply reviewed source records with IDs assigned by HQ.
- Q: Check two source-to-paraphrase mappings per paper, especially claims about uncertainty *guarantees*, clinical utility and *first* novelty.
- HQ: Determine whether this local taxonomy maps directly to existing central narrative-move labels or requires a controlled crosswalk; no central changes made here.
