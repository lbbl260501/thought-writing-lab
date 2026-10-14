# Scientific English · Candidate move taxonomy v0.1

Status: **C workstream proposal** for Issue #4, not a centrally approved label set. Examples in this document are newly written teaching examples. Where a case is discussed, see [source audit](SOURCE_AUDIT.md) and [24 grounded cases](SOURCE_GROUNDED_CASES_24.md).

## 1. 三个不同层次，不能混作一个“句子功能”标签

| 层 | 分析问题 | 主要对象 | 错误混淆 |
| --- | --- | --- | --- |
| **Propositional content** | 这个句子在科学上说了什么，证据强度多大？ | 一个可反驳的命题、方法/设计、结果、条件 | 将“作者提出”当成“方法已证实有效” |
| **Linguistic operation** | 哪些语言选择让该命题可理解？ | 主语、动词、客语、修饰、焦点、时态、让步/转折 | 把 however 视为逻辑论证的替代物 |
| **Discourse move** | 为什么现在说这句，它改变了读者对问题的什么认识？ | 承认成果、具体化障碍、重设比较轴、主张贡献 | 每句都标成“提出问题”，丢失叙事动作差异 |

三层可同时出现，但其分析单元不同。句式不是科学有效性；叙事顺滑也不是论据充分。

## 2. L1 语言动作：候选类型

| Local label | 可识别的选择 | 有效写法（原创） | 常见失误 | 操作性自检 |
| --- | --- | --- | --- | --- |
| L-01 AGENCY | 主语是否是可归责的科学主体？ | **Ablation results suggest** a role for the boundary term. | *It is obviously clear that...* | 谁观察、设计、比较或主张？ |
| L-02 VERB-STRENGTH | 动词的认识论强度 | **The results are consistent with** reduced sensitivity to noise. | *prove reliability* based only on DSC | 数据允许 *show*, *suggest*, *support* 中哪一个？ |
| L-03 OBJECT-SPECIFICITY | 客体是否可被观察或检验？ | The module **preserves boundary tokens** during encoding. | *improves the whole system greatly* | 这一步改变了哪个具体对象？ |
| L-04 CONCESSION | 让步承认真实能力，再暴露剩余问题 | Although feature fusion improves average accuracy, its **stability under registration error** remains unclear. | 无证据的普遍负面结论 | 先前成果与局限是否属于同一评价维度？ |
| L-05 GIVEN→NEW | 将上句新信息转化为本句话题 | CT–MR appearance differences impair transfer. **These differences** also complicate pseudo-label selection. | 句句引入新话题 | 第二句主语能否追溯到第一句的名词对象？ |
| L-06 CONDITIONING | 条件、范围和任务设置 | **Under the evaluated noise levels**, calibration changed only modestly. | *always*, *universally* | 结论对哪些数据、模型和假设成立？ |
| L-07 CAUSAL DISCIPLINE | 因果动词是否需要机制证据 | Missing channels **alter the available input information**. | *causes failure in all hospitals* | 是观察到相关、推测机制，还是有干预证据？ |
| L-08 INFORMATION WEIGHT | 主句承载新结论，从句承载背景/限定 | Unlike early token pruning, the proposed encoder **retains uncertain boundary regions**. | 将关键科学动作埋入三层从句 | 删去修饰语，主句是否还有明确科研内容？ |
| L-09 COMPARATIVE FRAME | 谁与谁、按何标准、在何条件比较 | In the source-free setting, adaptation cannot inspect source images directly. | *better*, *more robust* 而无比较对象 | 比较轴、基线、条件是否明确？ |
| L-10 COHESIVE REFERENCE | this/these/which 是否具有清楚所指 | **This restriction** rules out direct image-level source matching. | *This is important* 指代整段模糊 | 能否用一个具体名词替换 this？ |

动词力度参考排序只是启发而非机械等级：*describe*（陈述）/ *identify*（识别）/ *suggest*（较弱证据）/ *support*（某证据支持）/ *show*（报告观察）/ *demonstrate*（较强验证语气）/ *establish*（接近明确证成）。具体语境和谓词对象比词表顺序更重要；例如 “we demonstrate the workflow” 与 “we demonstrate clinical safety” 承诺完全不同。

## 3. L2 语篇动作：本组候选对齐表

| Local label | 科学叙事功能 | 与中央已有概念可能关联（待 HQ 确认） | 读者认知变化 |
| --- | --- | --- | --- |
| D-01 SITUATE | 以具体任务设定讨论对象，不泛泛歌颂重要性 | ESTABLISH_TASK | 知道讨论的对象及为何需要 |
| D-02 CREDIT-CAPABILITY | 承认已有方法在哪个维度已做到什么 | RECOGNIZE_CAPABILITY | 形成公平的领域基线 |
| D-03 EXPOSE-CONSTRAINT | 命名一个设定/资源/信号的具体约束 | IDENTIFY_TENSION | 理解限制来自哪里 |
| D-04 SPLIT-CASES | 将笼统问题拆成不等价的子情形 | DEFINE_OBJECT, QUESTION_ASSUMPTION | 发现旧问题定义遗漏了什么 |
| D-05 LOCATE-RESIDUAL | 已有进展之后仍未解决哪一项可检验局限 | IDENTIFY_TENSION, QUESTION_ASSUMPTION | 知道尚未回答的问题 |
| D-06 REFRAME-AXIS | 将评价从一般“准确率”移到所需性质 | REFRAME_PROBLEM | 改变看待成功/失败的标准 |
| D-07 INFER-PRINCIPLE | 从观察或限制推导设计应遵循的原则 | MOTIVATE_PRINCIPLE | 理解为什么设计合理 |
| D-08 SPECIFY-MECHANISM | 描述方法对具体对象施加什么操作 | PROPOSE_METHOD | 能预测实现会做什么 |
| D-09 BOUND-EVIDENCE | 在特定实验/假设下陈述结果 | REPORT_EVIDENCE, QUALIFY_SCOPE | 能判定证据实际支持的范围 |
| D-10 POSITION-CONTRIBUTION | 说明贡献解决了哪一缺口，不偷换成“所有问题” | STATE_CONTRIBUTION | 把工作放到精确的比较坐标中 |

**同一个词不是固定动作：** *however* 可以引入资源约束、失败现象或价值轴转换；*to address this* 可能从限制跳到方法，但中间需要成立的机制论证仍须由读者检查。

## 4. L3 句间信息链：四种可观察转接

1. **Topic chain / 同一对象展开**：source access → missing source samples → allowable adaptation signal。
2. **Derived chain / 新信息递推**：high resolution → more tokens → greater cost → demand for selective computation。
3. **Contrast chain / 同轴比较**：average overlap improves ↔ boundary reliability remains uncertain。必须共享可理解的评价维度。
4. **Reclassification chain / 重新分类**：missing modality → client-level fixed missingness vs sample-level arbitrary missingness → differential method requirements。读者得到新的问题切分，而不只是另一个问题清单。

段落可用“首句建对象—中间句解释机制/例外—末句打开下一步”，**但不要求每个段落恰好三句**，也不以句数代替推进效果。

## 5. 小型对比诊断：把看似高级的英语还原为科研动作

**Weak (newly authored):** *It is very important to solve the uncertainty problem, and many great methods have achieved superior results.*  
问题：缺任务与评价场景；“great”“superior”没有比较轴；第二分句未推进新信息。

**Rebuilt:** *Segmentation systems can achieve high average overlap while remaining unreliable at ambiguous boundaries. This discrepancy motivates evaluating boundary-specific confidence rather than overlap alone.*  
改善：具体主体 *segmentation systems*；动词 *achieve/remain/motivates*；客体 *average overlap / boundary reliability / confidence*；第一句制造同一系统的双维矛盾，第二句引出评价轴。**它是教学假设句，不是任何论文的实验结论**。

## 6. 不同写作体裁：可迁移的是认知动作，不一定是句式

| 体裁 | 可迁移动作 | 不宜机械搬运的形式 |
| --- | --- | --- |
| MICCAI 短论文 | 问题限定、机制动机、贡献序列 | 密集缩写与 1-2 页引言节奏 |
| MIA/TMI 长论文 | 明确任务缺口、比较方法假设、证据边界 | 将顶会常见的快速“However→We propose”当作充分文献论证 |
| BSPC 等应用期刊 | 清楚的应用价值与方法动机、可解释的评估范围 | 将性能形容词堆砌成临床落地结论 |
| 考研/四六级写作 | 定义、比较、让步、因果、回应题目 | 未解释的专业缩写、论文式 novelty claim |
| IELTS/TOEFL 论证 | 观点—理由—例证—限定、反方回应 | 把科学实验 *results demonstrate* 当作没有数据时的论据 |

此表为 **TRANSFER_HYPOTHESIS**，不是经过跨语料量化的规范。下一版需要抽样真实不同体裁文本及反例验证。

## 7. 可复标协议（第一版）

- 每个例子标记 source key、章节页段、原文可核事实范围、英文**原创释写**、SVO、句内新信息、局部 L 标签和 D 标签、confidence。
- 每句允许 1 个主要 D 标签 + 1 个次级 D 标签；遇到争议记录两种解释而不是强行归一。
- 不把作者自称的“首次”“显著”作为本库自己的判断。没有表格数据不补造。
- 后续两人独立标注，记录不一致项与 adjudication 理由，再考虑统计标签一致性。
- 不主动分配 PAPER/MOVE/EX 全局 ID；使用 Issue-4 本地键。