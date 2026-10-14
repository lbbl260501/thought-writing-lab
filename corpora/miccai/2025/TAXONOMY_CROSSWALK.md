# A 组分类体系横向对照与修订建议 · Issue #2

> **状态：2026-10-14 / A 组概念级交叉核对（provisional crosswalk），不是完成了盲法复标或统计一致性实验。**
> 文件只归档 A 工作目录内的原创对照结论；不替代 HQ 管理的共享 taxonomy，不擅自修改 C/D/B 的工作分支或正式全局标签。

## 1. 实际比较了哪些“最新几套”

以下均依据 **2026-10-14 GitHub 实际读取的分支文件**，并非只凭历史聊天印象：

| 体系与版本 | GitHub 实际文件 | 实际分析单位 | 主要价值 | 尚未解决的风险 |
| --- | --- | --- | --- | --- |
| 主库 12-label move CSV | [MOVE_TAXONOMY_v0_1.csv](../MOVE_TAXONOMY_v0_1.csv)（main） | 混合微观/中观/宏观 | 12 种研究/写作动作的共享候选术语 | 混合科学操作、语言叙述和证据质检 |
| 主库五层指南中的 12-label 表 | [ANNOTATION_GUIDE.md](../ANNOTATION_GUIDE.md)（main） | 从句子到论证链 | L1–L5 + 来源级别的边界 | 与上面的 12-label CSV **不完全相同** |
| A / MICCAI 2025 | [cases.md](cases.md)（A branch） | 10 篇论文在摘要或引言中可发现的动作模式 | 从真实案例形成问题类型与证据义务 | **还不是一套有边界定义的独立 taxonomy** |
| C / Scientific English | [MOVE_TAXONOMY_V0.md](https://github.com/lbbl260501/thought-writing-lab/blob/agent/academic-english/issue-4/language/academic-writing/MOVE_TAXONOMY_V0.md) | 10 类语言操作 + 10 类语篇动作 + 4 种信息链 | 解释语段的科学主语/动词/客体和读者认知推进 | C 的 `D-xx` 是 **discourse**，不是 D 研究室的科学动作 |
| D / Scientific Reasoning | [RESEARCH_MOVE_ATLAS.md](https://github.com/lbbl260501/thought-writing-lab/blob/agent/scientific-reasoning/issue-5/knowledge/scientific-reasoning/RESEARCH_MOVE_ATLAS.md) | 5 个“创新发生位置” + 8 个科研思维操作 | 解释问题如何建立、假设如何被检验 | 某些 A 案例缺少精确科学操作子型 |
| B / MICCAI 2026 | [problem_framing_cases.md](https://github.com/lbbl260501/thought-writing-lab/blob/agent/miccai26/issue-3/corpora/miccai/2026/problem_framing_cases.md) | 10 篇 **2026 摘要**中的科学问题构造、叙事与评审挑战 | 跨年份比较，发现共同问题动作与科学差异 | B 沿用指南标签；只读摘要的案例不能按引言句序分析 |

**结论：这些框架关注不同层面，不能把全部标签简单并成 12+10+8 的单层大类表。**

### 1.1 中央 CSV 与标注指南存在实质性词表漂移

两份权威文件各有 **12** 个 `narrative/scientific move` 标签，**完全同名交集为 8**：

- **共同存在 8 个：** `ESTABLISH_TASK`、`RECOGNIZE_CAPABILITY`、`IDENTIFY_TENSION`、`QUESTION_ASSUMPTION`、`REFRAME_PROBLEM`、`MOTIVATE_PRINCIPLE`、`QUALIFY_SCOPE`、`STATE_CONTRIBUTION`。
- **仅 CSV：** `REFINE_GRANULARITY`、`MAP_MECHANISMS_TO_TENSIONS`、`CONSTRUCT_MODEL`、`CONSTRUCT_COUNTEREXAMPLE`。
- **仅指南：** `INTRODUCE_OBSERVATION`、`DEFINE_OBJECT`、`PROPOSE_METHOD`、`REPORT_EVIDENCE`。

这不意味着同义词可自动合并。例如 `DEFINE_OBJECT` 和 `CONSTRUCT_MODEL` 不是同一动作；`REPORT_EVIDENCE` 与 `QUALIFY_SCOPE` 也不能互相替代。两个术语表在版本合并前应保留原始标签集、添加命名空间与映射解释，再由 HQ 决定权威代码本。

## 2. A 组十例 → C/D/主库/B 逐例映射

记号：**≈**＝部分重叠或上下位关系；**—**＝当前没有充分精确的映射；**≠**＝表面类似但必须区分。所有映射均为 **ANALYST_INTERPRETATION**，仅可用于审查和试标，不代表已实证验证类别的稳定性。括号中 C 的 `D-##` 指 *discourse move*，D 研究室名称用完整动作名。

| A 样本（MICCAI 2025） | 主库候选（scientific/rhetorical 混合） | C 语篇动作候选 | D 科学操作候选 | 与 B 2026 的比较及判别边界 |
| --- | --- | --- | --- | --- |
| **01 / 0308** 困难—方法—证据不匹配 | `MAP_MECHANISMS_TO_TENSIONS` | C `D-07 INFER-PRINCIPLE` / `D-08 SPECIFY-MECHANISM` | ≈ `CHALLENGE_DECOMPOSITION`，但 D 主要关心研究问题如何拆分 | B **1806** 的“结构先验是否真的可学习”同属**机制举证**；语言动机不等于证明机制 |
| **02 / 2701** 从静态形态扩展到 4D 动态 | `REFRAME_PROBLEM`、`CONSTRUCT_MODEL` | C `D-04 SPLIT-CASES` / `D-06 REFRAME-AXIS` ≈ | —（D 没有完全等价的“增加状态维度”子型） | B **2705** 把重建改写成补全，两者都重定义被预测对象，但**缺时间维度 ≠ 缺血管分支** |
| **03 / 0169** 从血管单位扩大到患者—血管层 | `REFINE_GRANULARITY`、`QUESTION_ASSUMPTION` | C `D-04 SPLIT-CASES` ≈ | ≈ `REFINE_COVARIATE`；改变样本/分析单位不等于只是加入变量 | B **6105** 重新定义方向性估计对象，但**建模粒度 ≠ 因果 estimand** |
| **04 / 1381** Cox 特例与模型族推广 | `CONSTRUCT_MODEL`、`QUESTION_ASSUMPTION` | C `D-07 INFER-PRINCIPLE` / `D-10 POSITION-CONTRIBUTION` ≈ | **—，缺精确标签**：需形式化“旧模型嵌入新模型族”的包含命题 | B 十例无直接一对一的特例包含关系；**研究遗漏，不是归类失败的证据** |
| **05 / 4374** 单病种模型→急诊多发现分诊 | `REFRAME_PROBLEM` | C `D-01 SITUATE` / `D-04 SPLIT-CASES` ≈ | —，可提出“工作流任务集定义”候选 | B **2852** 从孤立任务转为指南约束的联合决策；**多标签覆盖 ≠ 决策流程整合** |
| **06 / 1316** 手工准确 vs 全自动便捷的对立 | `IDENTIFY_TENSION`、`MAP_MECHANISMS_TO_TENSIONS` | C `D-02 CREDIT-CAPABILITY` → `D-03 EXPOSE-CONSTRAINT` → `D-05 LOCATE-RESIDUAL` | ≈ `CHALLENGE_DECOMPOSITION`，须证明两种要求不能仅独立优化 | B **4859** 将高保真和规划速度一起考虑；其终点是多次方案搜索，而非术中配准 |
| **07 / 0815** ID 分类能力→OOD 可靠性 | `REFRAME_PROBLEM`、`QUALIFY_SCOPE` | C `D-06 REFRAME-AXIS` / `D-09 BOUND-EVIDENCE` | **≈ 精确类型** `REFRAME_EVALUATION` | B **6055** 从 OOD 或高 Dice 延伸到真实失败检测；**分布偏移 ≠ 预测失败**（可能发生其中任一而无另一） |
| **08 / 1387** 超声精度×速度×泛化约束 | `IDENTIFY_TENSION`、`MOTIVATE_PRINCIPLE` | C `D-03 EXPOSE-CONSTRAINT` / `D-07 INFER-PRINCIPLE` | ≈ `CHALLENGE_DECOMPOSITION`，但多目标优化还需要明确目标和约束 | B **4859** 亦受延迟制约；**单次推理延迟 ≠ 让规划优化可行的总计算成本** |
| **09 / 5008** 固定采集→患者特异按需观察 | `REFRAME_PROBLEM`、`MOTIVATE_PRINCIPLE` | C `D-06 REFRAME-AXIS` / `D-07 INFER-PRINCIPLE` | **—，缺精确标签**：按状态条件选择下一份证据/计算 | B **4859** 快速代理使反复优化可行，两者均动态处理资源，但**主动采集 ≠ 规划优化** |
| **10 / 3267** 可读推理文字 vs 忠实解释 | `QUESTION_ASSUMPTION`、`QUALIFY_SCOPE` | C `D-06 REFRAME-AXIS` / `D-09 BOUND-EVIDENCE` | ≈ `INTERVENTION_IDENTIFICATION`（若设计干预检验解释忠实性），非同义 | B **6105** 亦需区分计算反事实与真实因果，但**解释忠实性 ≠ 生物干预因果效应** |

### 2.1 三种不能直接合并的关系

- **同一科学操作，不同文本动作**：研究者重新定义了 OOD 检测目标，可以在引言中先承认旧方法、再界定限制、最后指出新任务。那是**一个科学动作、多句不同写作动作**。
- **同一文本动作，不同科学操作**：`However, ...` 后面可能是增加模态身份、建立理论特例、改变临床终点或提出端侧预算。它们都可能是 C 的 `D-03`，但在科学上彼此不同。
- **同一研究领域，相似词汇，不同估计对象**：例如评价 OOD 数据分布与评价分割失败；不能因为都叫 reliability 就共享同一细分科学标签。

## 3. 与三种已有学术话语框架的外部对照

此处选**经过长期使用的参照框架**，并不把它们误称为“2026 年刚提出的最新模型”。它们有助于检验本项目究竟增加了什么信息。

| 外部框架 | 原始关注点 | 本项目应如何借鉴 | 不应怎样理解 |
| --- | --- | --- | --- |
| **Swales CARS**（1990/2004） | 引言的 *Establishing territory → Establishing niche → Occupying niche* | 作为**篇章级 rhetorical move** 的上层位置，检查为什么此时建立某个研究空间 | 不把三段式直接视为科学问题构建算法 |
| **Argumentative Zoning, AZ / AZ-II**（Teufel 等） | 句子相对于作者工作、相关研究、比较、目标等的修辞/归属角色 | 区分新工作、既有工作、对比与论证位置 | 不把 OWN、BACKGROUND 等来源角色当作形式化科学机制 |
| **Core Scientific Concepts, CoreSC**（Liakata et al., Bioinformatics 2012） | 对科学句子标注 Hypothesis、Motivation、Goal、Object、Background、Method、Experiment、Model、Observation、Result、Conclusion 等 **11 个知识类型** | 为“这句话陈述的是假设、模型、实验还是结果”提供内容层，避免将推测混成事实 | 不把一篇论文中哪种类型的句子多，误称为哪种创新更强 |

**外部资料（本轮已公开访问核查）：**
- UMass Amherst Writing Center, [Creating a Research Space](https://www.umass.edu/writing-center/resources/creating-research-space)。
- Liakata et al. (2012), [Automatic recognition of conceptualization zones in scientific articles and two life science applications](https://doi.org/10.1093/bioinformatics/bts071)。
- [Identifying communicative functions in discourse with content types](https://doi.org/10.1007/s10579-021-09554-4)，回顾 AZ / CoreSC 的区别与互补性。

**外部对照结论**：本库潜在的原创价值不是再造 CARS 三大步或 CoreSC 11 标签，而是把**文本的叙事位置、论文的科学操作、语言的实现方式，以及作者的证据义务**关联起来并验证其跨论文、跨领域的迁移性。

## 4. 建议的正交多层结构（提交给 HQ，非擅自批准）

同一个分析片段记录四条正交轴，外加必要的 provenance/体裁元数据：

1. **R / Research Thinking Move（科学操作）**：究竟改变了研究对象、条件、变量、假设、模型族、决策政策、估计目标或评价风险中的哪一项？记录正式对象、输入/输出/前提、检验义务与反例。
2. **W / Writing & Discourse Move（语篇动作）**：为何在这句话/段落让读者知道某项已知事实、剩余问题、设计原则、贡献或证据界限？记录段落位置、顺序、信息依赖，允许循环。
3. **L / Linguistic Realization（语言实现）**：主体、动词力度、客体、焦点、已知→新信息、让步、句式与限定词；属于 C 的 `L-01…L-10`，不与 R/W 共享 label ID。
4. **E / Evidence & Argument（证据与论证）**：Claim、grounds、warrant、alternatives、qualifier，附 `AUTHOR_CLAIM / REVIEWER_OPINION / ANALYST_INTERPRETATION / TRANSFER_HYPOTHESIS` 等身份标记。内容、解释、复现证据不得混写。

所有实例还要储存 `source_id`、年份、论文页/段、语料体裁（Abstract/Introduction/Methods/Results/Discussion）、真正访问的来源层级（metadata/abstract/intro/fulltext）、研究领域与观察层级（句、段、论证链）。

**特别注意**：源文阅读深度和版权许可是数据/质量约束，不应被当成论述动作标签。

## 5. 建议新增而暂不批准的科学操作子型

以下为**提案候选**，不自动新增中央 MOVE ID；优先研究是否能归在既有 `REFRAME_PROBLEM`/ `CONSTRUCT_MODEL` 的二级标签下：

| 候选子型 | 与旧标签的关系 | 能区分的科学问题 | 核验义务 |
| --- | --- | --- | --- |
| `NESTED_MODEL_GENERALIZATION` | `CONSTRUCT_MODEL` 的严格形式性质 | 旧模型能否作为新模型族的特例被恢复？ | 参数映射、包含条件、理论推导/证明与反例 |
| `CONDITIONAL_EVIDENCE_ALLOCATION` | `REFRAME_PROBLEM` + `MOTIVATE_PRINCIPLE` 下的决策子型 | 依据当前状态决定采集何种证据/分配哪类模态计算 | 固定预算与序贯预算公平比较、策略失误风险、开销 |
| `CLINICAL_WORKFLOW_REFRAMING` | `REFRAME_PROBLEM` 的研究目标子型 | 多任务输出是否真正组成可执行、受指南约束的决策链？ | 临床角色、任务依赖、约束满足、医生决策效用 |
| `EVALUATION_TARGET_DISAMBIGUATION` | `REFRAME_EVALUATION` 的定义检查 | 数据分布变化、模型错误、校准不足或风险事件是否被偷换？ | 样本级目标、适用条件、诊断错误类型、不同失效基准 |
| `EXPLANATION_FIDELITY_TEST` | `QUESTION_ASSUMPTION` / D 的干预识别的交界 | 文本解释是事后合理化、真实机制说明，还是仅为可读记录？ | 输入/中间变量干预、反事实一致性与替代解释 |

**重要否定例**：`NESTED_MODEL_GENERALIZATION` 与 `INFER-PRINCIPLE` 可以共现，但二者不是同义词；前者有可以证明的**模型包含命题**，后者描述作者如何把研究观察推进为方法动机。

## 6. 后续应做的实证比较（现在尚未做）

1. **统一代码本的“跨层接口”**：HQ 先决定主库 CSV 与 Annotation Guide 的四对不一致标签保留/迁移规则；C/D 的任务内 label 保持独立命名空间。
2. **同源盲法复标**：从 A2025、B2026、C 的已核引言中选 24–36 个可定位句段；补足 2026 引言核读，**不要拿 2025 引言与 2026 摘要直接推断年代叙事差异**。
3. **双人独立按 R、W、L、E 标注**：每个片段分别记录主标签、必要的多标签、证据 locator、判断理由与不确定项；报告各层 Cohen's κ / Krippendorff's α 或多标签 Jaccard 与混淆表。不得事先声称分类一致性。
4. **对抗案例**：专门纳入 OOD≠failure、multitask≠workflow、causal graph≠causal effect、explanation≠fidelity、nested model≠stronger performance 等“词相近但科学不同”的反例。
5. **跨体裁复核**：再按可比 section 抽样 MICCAI、MIA、TMI、BSPC，检查是否为篇幅、学科与审稿语境驱动；禁止把顶会的高频写作样式直接写成通用规范。
6. **进化而非指数膨胀**：只有新子型具有明确判别标准、能在两个以上独立研究例子中稳定复现，并对教学/科学复核提供额外信息，才建议 HQ 批准进入正式词表；“出现于一篇论文”不是充分条件。

## 7. 本次结论与需要主对话决定的事项

**本次已完成：** GitHub 当前主库 CSV / Guide / A / B / C / D **六处具体文件**的概念级横向比较，发现中央词表有 **8 个共同 / 4+4 个独有**标签；对 A 的 **10 个案例**逐项给出 C/D/B 的候选映射或无对应原因；补充 CARS/AZ/CoreSC 的学术参照，并提出可复标框架。

**本次尚未完成：** 独立人工盲标、类别频数统计、跨年份可比抽样、严格数学模型包含证据核验及各组跨源实验。此文件不属于既定共享规范的正式修订。

**向 HQ 请求：**
- 明确两个中央 12-label 文件的正式优先级或统一术语契约；
- 认可/修改“科研操作 R、篇章 W、语言 L、证据 E”分层结构；
- 判断哪些 A 的科学子型值得单独研究、哪些是既有标签的二级细化；
- 批准未来新 Issue 对 2025/2026 **同一篇章类型**的盲法复标与跨体裁效度检验。
