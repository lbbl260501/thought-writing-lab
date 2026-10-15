# MICCAI 2026｜科研问题定义与叙事机制首批案例（B / Issue #3）

**证据边界（2026-10-14）**：以下10例均已访问MICCAI 2026官方论文信息页的摘要与部分评审意见，**不声称完成论文引言或全文精读**。所有“作者”事实对应摘要中作者主张，所有“审稿人”意见是评审文本的观点；“分析动作”与“可判别实验”是本工作组提出的原创分析/待验证迁移方案，不等于已完成实验。

**采样规则**：优先覆盖不重复的科学问题类型（评价对象/任务定义/物理建模/知识可更新性/反事实/多模态/可获得性/基础模型），而非按随机概率抽取。各案例可通过 `source_key` 与 [sources.csv](sources.csv) 对接；仅使用 `miccai:2026:<官方PaperID>`，正式库ID由主控分配。

**使用方式**：L2“摘要路径”是我们根据**摘要**而非引言逐句标注的研究动作概括，适合后续进行论文引言反查。每例包含 L3 的科学主张—证据—尚缺检验及给 C/D 组的转换题，不是面向学生直接发布的定稿课程。

## 1. 血管重建：把重建问题改写为形状补全

- **来源：** [MICCAI 2026 · Paper2705](https://papers.miccai.org/miccai-2026/0001-Paper2705.html) · `miccai:2026:2705` · *Inverse-problem reframing / geometry*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** CTA提供三维血管先验，但细小血管分支可能缺失；双平面DSA提供更精细的投影观察，却缺少直接的三维结构。作者以血管形状补全而非无约束三维重建组织问题。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `INTRODUCE_OBSERVATION → IDENTIFY_TENSION → REFRAME_PROBLEM → MOTIVATE_PRINCIPLE → PROPOSE_METHOD`。
- **L3 论证与评审证据：** 作者在摘要中主张联合CTA先验和DSA投影可恢复更小的血管分支；这不是独立的临床效果证明。官网Reviewer #1质疑合成DSA与真实采集的差距，及CTA/DSA配准误差。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 针对不同配准误差、投影数量、血管先验缺损程度设定受控扰动；分开报告合成定量与真实病例定量/定性，避免将三例临床演示外推为普遍有效。
- **C/D 组迁移问题：** 在自己的多模态问题中，哪一模态承担结构先验、哪一模态弥补观测盲区？能否将一般‘融合’改为可检验的‘不完整对象补全’问题？

## 2. 癫痫诊疗：从孤立任务走向指南约束的联合决策

- **来源：** [MICCAI 2026 · Paper2852](https://papers.miccai.org/miccai-2026/0004-Paper2852.html) · `miccai:2026:2852` · *Workflow reframing / knowledge grounding*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 已有方法往往分别处理发作检测、病灶定位或预后等任务；临床诊疗需综合多来源证据和指南。作者将问题从若干单项预测转成受指南约束的多任务证据整合。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `RECOGNIZE_CAPABILITY → IDENTIFY_TENSION → REFRAME_PROBLEM → MOTIVATE_PRINCIPLE → PROPOSE_METHOD`。
- **L3 论证与评审证据：** 摘要称框架在两个数据集、六项任务上进行了评估，且结果优于部分基线；官网Reviewer #1将判别模型的结构化预测和生成式代理的文本解释视为主要构成。不能从此推断已经证明真实临床综合管理有效。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 在相同原始模型、数据和调用预算下，比较指南有/无、规则协调有/无、单独判别与纯生成方法；另外用真实专家决策或前瞻流程检验综合诊疗价值。
- **C/D 组迁移问题：** 通过‘任务集合不是工作流程’这一区分，为自己的手术规划论文建立整体性科学问题而非罗列模块。

## 3. 空间转录组：从相关结构转向方向性反事实比较

- **来源：** [MICCAI 2026 · Paper6105](https://papers.miccai.org/miccai-2026/0006-Paper6105.html) · `miccai:2026:6105` · *Estimand redefinition / counterfactual*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 已有细胞互作分析依赖相关性或预设配体—受体知识，不能直接刻画所关注的发送方影响方向。作者定义基于邻域替换和接收细胞预测变化的方向性分数。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `QUESTION_ASSUMPTION → DEFINE_OBJECT → REFRAME_PROBLEM → MOTIVATE_PRINCIPLE → REPORT_EVIDENCE`。
- **L3 论证与评审证据：** 作者在摘要中报告了置换/空间打乱零假设检验及与配体—受体分数的相关结果；Reviewer #1认可其方向性建模思路。这些证据检验的是建模评分及统计关联，**不自动等同于真实生物扰动已经识别因果效应**。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 优先采用真实配体阻断、细胞干预或外部数据验证计算分数的方向性；与匹配复杂度的无向图方法比较，讨论图模型错误与隐藏混杂。
- **C/D 组迁移问题：** 练习区分相关、模型反事实、自然实验与干预因果结论的不同动词和claim strength。

## 4. 微波消融：把推演速度转成治疗方案可优化性

- **来源：** [MICCAI 2026 · Paper4859](https://papers.miccai.org/miccai-2026/0007-Paper4859.html) · `miccai:2026:4859` · *Simulation-to-optimization / planning*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 高保真有限元模拟对患者特异消融有价值，但在临床时间约束下嵌入多次方案搜索成本很高。作者以快速替代模型为核心，把单次预测转成可迭代的天线轨迹与消融参数优化。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `ESTABLISH_TASK → IDENTIFY_TENSION → MOTIVATE_PRINCIPLE → PROPOSE_METHOD → STATE_CONTRIBUTION`。
- **L3 论证与评审证据：** 摘要报告替代模型可在毫秒级给出坏死区域预测，优化在两分钟内完成，并提及前临床验证。Reviewer #1强调替代模型相对FEM的加速和与优化循环的衔接。预测准确度与最终治疗优化有效性仍是两个需要分别检验的命题。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 采用同等算力和同等候选数的规划基线；对未参与训练的解剖、热参数及血流状态测试；验证预测误差是否改变最终所选方案的安全性。
- **C/D 组迁移问题：** 用于手术术前规划：论文叙事应从‘模型很快’过渡到‘因此能评价此前无法充分比较的候选方案’，并给出相应实验。

## 5. 放疗勾画：从标签映射转向指南可更新的决策过程

- **来源：** [MICCAI 2026 · Paper5049](https://papers.miccai.org/miccai-2026/0009-Paper5049.html) · `miccai:2026:5049` · *Rule-change adaptability / zero-shot*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 监督式靶区自动勾画对标注与训练规则依赖较强，一旦临床指南更新可能需要重训练。作者以自然语言临床指南驱动三维靶区生成，重定义了适应性的评价对象。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `RECOGNIZE_CAPABILITY → IDENTIFY_TENSION → QUESTION_ASSUMPTION → REFRAME_PROBLEM → REPORT_EVIDENCE`。
- **L3 论证与评审证据：** 作者摘要报告了食管癌勾画的Dice及医生盲评，并主张无需重训练适配不同指南；Reviewer #1描述了将自由文本指南转成分割/几何工具执行计划的机制。单个解剖部位的成功尚不等于任意指南均可安全更新。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 盲法跨指南、跨疾病部位评测；不仅测Dice，也核验剂量学、指南约束违背率、医生修订时间与高风险病例失效模式。
- **C/D 组迁移问题：** 从‘精度更高’切换为‘规则变动后的适应成本更低’，分析改变评价轴需要新增哪些证据。

## 6. 非增强CT：把可获得影像的诊断能力变成基准问题

- **来源：** [MICCAI 2026 · Paper5454](https://papers.miccai.org/miccai-2026/0013-Paper5454.html) · `miccai:2026:5454` · *Benchmark creation / accessibility*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 增强CT携带额外获取成本与潜在风险。作者将‘能否从非增强CT恢复部分临床有用的诊断信息’设为多中心数据与任务基准，而非宣称NCCT完全替代增强CT。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `ESTABLISH_TASK → IDENTIFY_TENSION → REFRAME_PROBLEM → DEFINE_OBJECT → REPORT_EVIDENCE`。
- **L3 论证与评审证据：** 摘要报道内外部多器官AUC约71.1%与66.2%；Reviewer #1提及双中心配对样本与多种基线。其主要贡献可按‘问题与基准建设’评价，不能仅以最佳模型的高分代替数据与任务可用性的论证。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 评估病种分层、外部可迁移性、漏诊风险及与仅NCCT临床读片的比较；检查报告生成是否会凭空补出只有增强期才可确定的发现。
- **C/D 组迁移问题：** 如果模型并非新颖之处，如何靠明确任务边界、质量可控的数据与公平评测形成研究贡献？

## 7. 真实分割系统：从平均Dice转向失败检测

- **来源：** [MICCAI 2026 · Paper6055](https://papers.miccai.org/miccai-2026/0017-Paper6055.html) · `miccai:2026:6055` · *Evaluation-object shift / reliability*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 分割模型在临床应用中遇到分布偏移，但常见OOD方法多在受控研究数据上评价。作者把重点放在能否识别真实工作流中的分割失败，并比较多个检测器。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `RECOGNIZE_CAPABILITY → QUESTION_ASSUMPTION → REFRAME_PROBLEM → DEFINE_OBJECT → REPORT_EVIDENCE`。
- **L3 论证与评审证据：** 摘要给出跨国家/站点的内外部验证与Pairwise Surface DSC检测表现；Reviewer #1肯定真实部署数据的价值，同时指出失效病例数量较少，影响对灵敏度的稳定性判断。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 预先固定阈值；分离失败严重度、失败类型和中心迁移；报告绝对错误例数、置信区间、阴性病例误报与工作流追加成本。
- **C/D 组迁移问题：** 把‘网络输出不确定’与‘是否可靠发现失效’分开，重写自己论文的评价对象与基线选择。

## 8. 乳腺超声：共享与特异模态的结构性先验之争

- **来源：** [MICCAI 2026 · Paper1806](https://papers.miccai.org/miccai-2026/0012-Paper1806.html) · `miccai:2026:1806` · *Modality asymmetry / reviewer counter-argument*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 临床超声诊断涉及B-mode与功能补充模态，且存在设备、病例和模态组合异质性。作者通过共享/模态特异专家与受限路由提出多模态整合方法。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `RECOGNIZE_CAPABILITY → INTRODUCE_OBSERVATION → IDENTIFY_TENSION → MOTIVATE_PRINCIPLE → PROPOSE_METHOD`。
- **L3 论证与评审证据：** 作者摘要主张临床多配对设置中优于部分融合基线。官网Reviewer #1质疑所谓‘解耦’主要由硬路由结构施加，而非由证据直接证实；同时质疑缺乏充分跨中心/跨设备实验。Reviewer #2对方法较为积极，说明评审并非一致结论。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 对比硬路由、可学习柔性路由、无专家共享、等参数简单融合；对比跨设备/跨中心和模态质量退化下是否真的学得模态可靠性，而不是把先验写进架构。
- **C/D 组迁移问题：** 对多模态论文提出可证伪问题：‘非对称性究竟是人工结构假设，还是能够被数据识别并用于样本级资源分配的性质？’

## 9. 光片显微镜：把大体积无标签数据转为跨任务能力

- **来源：** [MICCAI 2026 · Paper4243](https://papers.miccai.org/miccai-2026/0014-Paper4243.html) · `miccai:2026:4243` · *Foundation pretraining / annotation efficiency*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 光片显微镜产生高维体数据，大量未标注样本难以被昂贵的全监督模型利用。作者结合遮蔽建模与图文对齐预训练并测试分割、分类、去模糊的少样本迁移。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `ESTABLISH_TASK → IDENTIFY_TENSION → REFRAME_PROBLEM → MOTIVATE_PRINCIPLE → REPORT_EVIDENCE`。
- **L3 论证与评审证据：** 摘要宣称多个下游任务和专家评估均支持少标注收益；Reviewer #1肯定构建数据与多任务评估的努力。仅凭同分布任务收益不能证明跨所有显微成像协议的通用性。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 独立划分生物物种、组织、染色与设备；分开测预训练数据量、标签数量与计算成本；用零样本、少样本和充分监督形成迁移曲线。
- **C/D 组迁移问题：** 写作训练：区分‘规模化预训练带来高分’与‘预训练改变标注/算力需求曲线’两种贡献叙事。

## 10. 医学VLM持续学习：把误诊经验作为负向知识

- **来源：** [MICCAI 2026 · Paper0321](https://papers.miccai.org/miccai-2026/0273-Paper0321.html) · `miccai:2026:0321` · *Failure-memory / mechanism identification*
- **科学矛盾（AUTHOR_CLAIM 的原创释义）：** 作者将持续学习中的细粒度混淆和遗忘解释为常见病征、鉴别诊断信息不足，提出编码易误诊对象、相似病征与排除标准的知识图谱与检索机制。
- **L2 摘要研究动作（ANALYST_INTERPRETATION）：** `INTRODUCE_OBSERVATION → IDENTIFY_TENSION → QUESTION_ASSUMPTION → REFRAME_PROBLEM → MOTIVATE_PRINCIPLE`。
- **L3 论证与评审证据：** 摘要报告多个数据集上的任务增量学习效果。官网Reviewer #1关注正向检索与负向错误知识是否真正独立贡献，以及外部大规模记忆造成基线不公平；评审在作者澄清后支持接收，但仍保留检索对照与任务增量场景的限制。
- **L4 可判别的新增实验（TRANSFER_HYPOTHESIS）：** 所有方法共享同一外部记忆库与检索预算；设置正向知识、负向知识、结构图、简单检索四组对照；增加无已知任务边界的类增量评估。
- **C/D 组迁移问题：** 将‘方法包含多个模块’转成‘哪个知识类型和机制导致了可检验的改善’；练习设计隔离机制的实验。

## 首轮跨案例对照与局限

| 比较轴 | 案例 | 需要分开的命题 |
|---|---|---|
| **问题重定义 vs 仅改网络** | 2705 / 5049 / 6055 | 形状补全、指南变更、失效检测是不同的任务对象；改骨干结构不能自动证明新任务价值。 |
| **预测分数 vs 生物因果** | 6105 / 1600（待深读） | 模型反事实评分不等于随机生物干预；“causal-inspired”与“causal effect identified”不能混用。 |
| **物理合理性 vs 真实可部署性** | 4859 / 2705 | 替代模型很快或模拟重建很好，仍须检验优化方案和真实采集中的系统误差。 |
| **架构内置 vs 属性被学到** | 1806 / 5533（待深读） | 显式专家或主次模态设计给出了先验，不直接证明样本特异非对称性可识别。 |
| **性能改善 vs 外部知识/数据优势** | 0321 / 4243 | 增加存储/训练数据可能提高性能，机制贡献需要控制外部知识与计算预算。 |
| **模型评价 vs 新基准贡献** | 6055 / 5454 | 实际失效事件、病种范围、医生效用与指标平均分有不同证据要求。 |

**尚未完成**：这10例的全文引言逐句标注、统计代表性、评审多方观点系统编码、presentation type 官方日程确认，以及跨年份比较。下轮需选取“对照性精读小样本”，优先做相同问题/不同叙事的成对比较。

**版权**：仅有原创释义、论文题目和来源链接；不复制整段论文引言或评审文本。
