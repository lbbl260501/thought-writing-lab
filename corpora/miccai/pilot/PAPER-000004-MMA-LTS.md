# PAPER-000004 · MMA-LTS：隐含假设重构（MICCAI 2026）

- **原始标题**：Missing Modality-Aware Calibration for Trustworthy Brain Tumor Segmentation
- **作者**：Sol Lee et al.
- **官网摘要和评审**：[MICCAI 2026](https://papers.miccai.org/miccai-2026/0659-Paper1236.html)
- **官方全文入口**：[PDF](https://papers.miccai.org/miccai-2026/paper/1236_paper.pdf)
- **核验范围**：官网摘要及部分公开评审；**尚未完成 PDF 引言和实验的全文核验**。因此下述结构是摘要级分析，而不是逐句精读。

## 研究问题最关键的转向
已有缺失模态分割研究侧重在不完整模态下维持分割精度，而置信度校准可能不足。更深一层的问题是：校准质量并不一定只随可用模态的数量单调改变；**缺失的是哪一种模态，以及误差位于哪个空间区域**，也会影响预测难度。

## L2/L4 · 摘要可见的动作链
1. 临床实际存在模态不完整；
2. **ACKNOWLEDGE_CAPABILITY**：现有方法可能仍维持分割精度；
3. **SHIFT_TARGET**：从预测准确率转向预测可靠性；
4. **QUESTION_ASSUMPTION**：从“模态数量”这一简化标量转到模态组合身份；
5. **LOCALIZE_PROBLEM**：进一步从整例指标转向体素级异质性；
6. **DESIGN_FROM_ASSUMPTION**：模态可用性 token + 体素难度 → 空间自适应温度估计；
7. **TARGETED_VALIDATION**：在不同缺失组合下评价校准，并保留分割精度。

## 思想方法
`QUESTION_HIDDEN_ASSUMPTION` + `REFINE_GRANULARITY` + `REDEFINE_EVALUATION_OBJECT`。

这种结构特别值得用于**新的科学问题寻找**：现有方法把一个问题压缩成什么标量？该标量是否丢失身份、位置、阶段或语境信息？

## L3/L5 · 建议的追加实验（知识库提出，非原文结果）
按**相同缺失数量、不同模态组合**报告校准误差和区域性能，检验简单的数量单调假说；同时比较全局与局部校准，判断空间依赖是否必要。

## 小练习
将一个仅讨论“可用输入数量”的英语句子改写为包含“具体构成 / 空间位置 / 置信度”三个层级的研究问题，并明确哪些是现象、哪些只是拟检验的假设。
