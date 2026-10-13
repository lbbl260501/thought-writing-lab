# PAPER-000003 · Locor：局部函数依赖的相似性度量（MICCAI 2025）

- **原始标题**：New Multimodal Similarity Measure for Image Registration via Modeling Local Functional Dependence with Linear Combination of Learned Basis Functions
- **作者**：Joel Honkamaa, Pekka Marttinen
- **官方页面与评审**：[MICCAI 2025](https://papers.miccai.org/miccai-2025/0636-Paper1747.html)
- **全文**：[官方 PDF](https://papers.miccai.org/miccai-2025/paper/1747_paper.pdf)
- **DOI**：10.1007/978-3-032-04937-7_38
- **核验范围**：PDF Introduction + Notation/Related Work 的开头（pp. 1–3），官方评审；**未整体核验全部实验**。

## L4 · 从已有数学方法的假设出发
图像配准常被写成相似性项与正则项共同作用的优化问题。传统 multimodal 度量例如互信息（MI）与 correlation ratio（CR）均涉及模态强度之间的统计关系，而 CR 对函数依赖的约束比 MI 更强。

这篇工作不是将“配准效果差”笼统视为一个网络架构缺陷，而是定位到**相似性度量的统计假设及其空间适用范围**：
- 全球范围内的函数依赖可能过于强，无法适应空间变化。
- 更小的局部范围可能适合建模函数关系，但估计方法的效率和表达能力又成为问题。
- 作者改用可学习基函数的线性组合拟合局部强度依赖，并说明计算可以转化为卷积运算。

## L2 · 科学论证节奏
1. 医学配准和多模态影像的任务必要性；
2. 配准标准形式：相似性 + 正则化；
3. MI/CR 的既有认识；
4. **QUESTION_ASSUMPTION**：CR 在全局尺度过于严格；
5. **REDEFINE_SCOPE**：转到局部函数依赖；
6. **REPLACE_ESTIMATOR**：局部、可学习的基函数代替某些更受限或较昂贵的估计方法；
7. **CONSTRUCTIVE_EFFICIENCY**：卷积形式导出 GPU 实现上的计算便利；
8. 实验与工具贡献。

## L3/L5 · 评价关键
该方法的价值主张应同时受到三种检验：统计关系拟合能力、配准性能、推理/优化开销；“基函数可学习”并不自动证明结果更好。论文官方评审肯定了这一数学动机与有效实现的联系，这仍属于**评审意见**。

## L1 · 语言动作
这篇论文适合训练：
- 从抽象的任务困难收束到**具体数学构件**的写作；
- 用 “一般情况下过强，但在局部可能足够” 这样的受限让步表达科学条件；
- 对比新旧度量时，先说不同的**建模前提**，再说算法实现细节。

## 研究大练习
在 PET/CT 对齐或分割中，从一个看似固定的建模假设出发：它是在什么尺度、病例或模态组合下成立？将其修改为局部/条件形式，并列出验证模型必要性的反例与控制实验。
