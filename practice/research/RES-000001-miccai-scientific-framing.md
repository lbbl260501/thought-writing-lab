# RES-000001 — 同一研究素材的三种科学叙事

## 任务设定（假想，不是论文已验证数据）
一个 PET/CT 模型存在以下待验证的迹象：
- 部分病灶更容易在 PET 上定位，CT 对局部解剖边界更清晰；
- 不同病例可能需要不同的模态处理策略；
- 固定的双模态计算预算未必适用于全部输入。

你的工作不是立即发明模型模块，而是在 3 个竞争性的科学框架中确定哪一个值得研究、怎样为其设计证据。

## 参考原型
- [C²MAOT](../../corpora/miccai/pilot/PAPER-000001-C2MAOT.md) — challenge decomposition
- [CDFP-Net](../../corpora/miccai/pilot/PAPER-000005-CDFP-Net.md) — explicit modality asymmetry
- [MMA-LTS](../../corpora/miccai/pilot/PAPER-000004-MMA-LTS.md) — a hidden assumption about modality identity
- [Locor](../../corpora/miccai/pilot/PAPER-000003-Locor.md) — replacement of a modeling assumption

## 三个写作目标

**A. 模态融合叙事：** 研究 PET 与 CT 如何互补。你的核心贡献应是更有效地整合不同模态的任务证据。

**B. 可靠性叙事：** 研究特定模态缺失/噪声时，预测置信度是否与错误概率相符。核心评价标准不能只是 Dice。

**C. 资源选择叙事：** 研究个体输入中 PET/CT 的增量预测价值是否随预算而变化。需要明确“贡献”究竟是表征差异、遮蔽干预后性能下降，还是额外计算带来的边际收益。

## 产出
1. 三套独立的 `phenomenon → tension → research question → hypothesis`，每套英文 80–120 词。
2. 为每套提取一个潜在隐含假设，并设计一个实验可区分的替代解释。
3. 为每套写 4–5 句的引言开头，逐句标注科学主体、动作、对象和叙事功能。
4. 写一个对照表，说明三套叙事会要求不同的评价指标、消融和对照组。
5. 选择最有价值的一套，写出仍缺少的必要证据，而不是在措辞层面修饰缺口。

## 评价准则
- `scientific_object`：研究问题是否清楚、可形式化？
- `inference`：论点—依据—推理桥梁是否完整？
- `evaluation_design`：能否设计有判别力的实验？
- `narrative`：每句是否推进一个必要动作？
- `language`：语言是否准确、紧凑且符合科研语域？

## 提示
三种叙事不需要平均覆盖一切结果。选择一种合理的研究价值进行强调，但它对应的实验要求必须一并满足。不要仅凭架构中使用了非对称交互就断言模型学会了病例级模态贡献。
