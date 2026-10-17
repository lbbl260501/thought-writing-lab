# R03 · 六项练习的解释与参考答案

[先完成讲义中的练习](WORKSHOP.md)。以下均为原创教学表达，不是论文引文。答案不唯一；修改应服从题设，说明读者现在更清楚理解了什么。

## X1 · 遥感的研究对象

> Pixel-level differences can reflect seasonal appearance shifts as well as changes in land use. We therefore investigate a representation that associates each parcel with its attributes across observations, so that land-use transitions can be studied separately from changes in image appearance.

新句把“强大”换成可识别的对象。investigate 与研究计划一致；so that 说明用途，不表示已取得结果。可评价属性变化与真值地块变化的对应，并单独检查季节差异中的误报。无需照搬病理或点图术语。

## X2 · 反馈关系

> The detector supplies candidate regions to the segmentation model, whose accepted masks are then used to update the detector. The updated detector generates new regions for the next annotation cycle, linking mask generation to subsequent region selection.

whose 接住前面的模型产物；updated/new 表示跨轮次变化。accepted 保留题设的筛选。没有把“多轮”直接写成“更正确”，也没有凭空增加人工修正或收敛保证。

## X3 · 方法选择（86词）

> Forecasting services must accommodate requests with different context lengths and prediction horizons. Predicting an entire horizon at once requires an output size chosen in advance, while generating one time point per call requires repeated decoding. We therefore investigate a blockwise decoder that produces several future values at each step and can be called again when a longer horizon is requested. This design makes output length adjustable without reducing every prediction to a separate decoding call. Its accuracy and runtime can then be evaluated across requested horizons.

这是从题设构造的设计论证，不声称某篇来源论文使用了全部这些设置。最后一句是评价方向，不是已测结果；70–100词范围只是训练约束。

## X4 · 位置相关的表现

> In this hypothetical evaluation, accuracy was 78% with the answer-bearing document first, 59% in the middle, and 75% last. This position-dependent pattern motivates testing whether the errors arise during information retrieval or during the subsequent construction of an answer.

原句将部分退化夸成完全不能，并混同文档位置与文档内部位置。改句保留三个数值，随后拆分机制。可以设计更简单的检索任务，但不能预先宣布它已证明原因。数据全部为教学假设。

## X5 · 条件是命题的一部分

> Under assumption H and the specified precision setting, no fixed-depth model in class M can exactly represent task T.

要纠正的是对象、量词与条件，不是仅让语气更软。原句把指定模型类、精确表达、特定任务扩成所有现代模型、实际求解、所有序列任务。没有理由因为某个条件句显得谨慎就将它删去。

## X6 · 整合工作的贡献（85词）

> We study how a training schedule can connect broad object experience with precise placement behavior. The system reuses an existing visual encoder and action decoder, while assigning different roles to its two training stages. Pretraining exposes the model to varied objects and interactions; post-training concentrates on the placement behaviors required by the target task. The contribution to be evaluated is this organization of experience, rather than a new encoder or decoder. Comparisons with single-stage training would test whether the proposed division provides a useful advantage.

主动交代复用，不等于mere组合。新的评价对象是经验组织；最后一句提出对照，未假造优势。这仍是研究计划的表达，正式稿件需要据实际结果更新。

## 四项自查

- 对象与范围准确，尤其是层级、量词和条件。
- 句间新增了可解释的关系，不仅替换连接词。
- 实际观察、拟做实验和理论判断保持不同身份。
- 能在陌生任务中完成改写，并解释自己的选择。

不以句长、禁词命中或限定词数量自动判定论文质量。只有实际独立作答才能记录学习表现；本页没有为任何人生成成绩。