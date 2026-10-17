# R02 · 把研究判断写清楚，而不是给每句话加防线

本讲承接 D10–D13。你将练习三件事：从真实论文中辨认方法动机；把作者有依据的判断说完整；区分必要纠错与没有新增信息的限定。建议先读三个案例，再独立完成六题，最后阅读 [解释与参考答案](ANSWERS.md)。

下面的原文链接用于带读；所有题目、改写和研究情境均为原创教学设计，不是论文引文或新实验结果。

## 一、任务属性如何长成设计要求

MAE 的引言先讨论语言和视觉的不同，再解释视觉预训练的设计。作者用一个非常普通的系动词句定位差异：

> Information density is different between language and vision.

来源：[MAE，作者稿 arXiv 2111.06377v3，§1(ii)–(iii)](https://arxiv.org/html/2111.06377v3)。本讲依据该版本引言，不将它冒充逐字一致的会议终稿。

这句话的工作不是宣布“问题很复杂”，而是给出后文可以继续分析的对象。作者接着讨论图像冗余与局部恢复的关系，并由此解释遮蔽设置和编码、解码的设计。你应学习的不是把名词换成自己的任务，而是这种关系：**对象有什么性质 → 该性质使常规任务变成什么 → 训练任务需要怎样改变**。

阅读时做两项标注：圈出每句继续使用的旧对象；划出真正新增的关系。不要因为谓语是 is 就把句子改成复杂表达。

## 二、为什么先做一个较简单的判断

[HRViT，MICCAI 2025，官方论文3977，第2页引言](https://papers.miccai.org/miccai-2025/paper/3977_paper.pdf#page=2) 从高分辨率分割的处理需求出发，区分边缘与其他区域，再提出以边缘判断支持中间层令牌停算，并配合后续恢复设计。

这是作者提出的设计依据，不是我们独立证明了难度关系。值得迁移的是：**不是所有位置都需要同样深度的处理；较便宜的中间判断，可以为后续计算选择提供信息**。在自己的任务中使用这条思路，还需要明确中间判断的代价、可靠性以及错误停止的后果。

请比较两种原创写法：

A. We introduce an efficient and intelligent module to address the limitations of existing methods.

B. We use an intermediate prediction to identify inputs that can stop early, reserving later computation for those that require further processing.

B 说明了判断对象和资源去向，仍然是方法描述，而非已经证明效率或效果。正式论文需把 inputs、prediction 和处理条件换成真实设计，不能只保留句式。

## 三、第二个模块为什么必须出现

[Data Remixing，作者稿 arXiv 2506.11550v2，§1](https://arxiv.org/html/2506.11550v2) 将多模态优化中的速度问题与方向问题分开。在引出样本层面的解耦之后，作者仍讨论残余方向干扰，再引出批次层面的重组。

这里两个设计不是普通的“另外再加一项”。本讲的分析是：**第一步解决一部分问题，但留下第二步专门处理的问题**。因此，第二步应从第一步的结果接起，而不是重新宣布“此外，提出一个新模块”。

独立写作任务：使用以下纯教学设想，写出70–100词的三至四句方法动机。某系统先识别输入质量；质量估计本身不决定如何分配预算；第二阶段在固定预算下选择处理路线。写清两阶段的依赖，不报告尚不存在的性能结果。答案册提供一个可比较版本。

## 四、六项双向编辑练习

每题先作判断：保留、删去冗余、正面重述、纠正命题，或移至编辑查询。然后写出英文修改。判断依据是本题事实，不是句子看起来有多少 may 或 however。

### 1 · 实测值不需要假装不确定

教学事实：同一测试协议已测得平均 Dice 0.842。没有要求你比较其他模型。

原稿：The model might perhaps have achieved a mean Dice of 0.842 on the evaluated test set.

任务：改成一句直接结果陈述；不要自行补入显著性、优越性或临床判断。

### 2 · 范围已经明确，还需要逐项否认吗

教学事实：论文只研究完整、已配准双模态输入下的病例级计算分配。

原稿：We study case-dependent computation allocation with complete, registered multimodal inputs. We do not claim that this setting covers every missing-modality configuration or every possible deployment environment.

任务：检查第二句是否为本段增加必要信息。保留研究范围，并写明什么情境下需要另行讨论缺失输入，而不是一律删除相关问题。

### 3 · 固定结构是不是固定贡献

阅读材料：[FRODO，MICCAI 2026，论文5533，第4页，Spatial FiLM conditioning](https://papers.miccai.org/miccai-2026/paper/5533_paper.pdf#page=4)。文中调制参数由输入的 FLAIR 特征产生，再作用于 QSM 特征。

待改句：A fixed architecture necessarily assigns the same contribution to each modality in every case.

任务：纠正这项概念混同。分别说明结构是否固定、交互是否依赖输入、执行计算量是否改变。只根据给定方法描述作答，不把输入相关调制直接称作动态计算路由。

### 4 · 有用的结果，不等于另一项能力

教学事实：学生在允许 AI 辅助时交出的作文评分提高；尚没有无辅助测验。课堂成品质量本来就是研究关注的一个结果。

原稿：The higher scores prove that students developed stronger independent reasoning.

任务：保留“辅助写作产出改善”的价值，纠正独立能力的推论。用一至两句完成，不扩成一串与此无关的研究局限。

### 5 · 没读到的实验，不等于不存在

教学事实：编辑者目前只有作者的引言；全文和补充材料尚未提供给编辑者。

编辑者拟插入：The study lacks a matched-budget control and therefore cannot support its claimed contribution.

任务：这句话应不应该进入作者正文？写一条放在正文之外的具体核查请求；说明收到全文后怎样作决定。不要给未核对的研究判定“有”或“没有”实验。

### 6 · 系统贡献与组件归因

教学事实：新系统更换了模块、训练方案及预处理；同一测试集性能提高。尚未分别隔离三种改动的作用。

原稿：The new module is responsible for the entire improvement.

任务：写一条正面、成立的系统贡献陈述，再给出一项确实能检验组件作用的比较。不要把“组件归因未分离”改写成“系统改进没有价值”。

延伸阅读：[nnU-Net Revisited，MICCAI 2024，官方论文2847，第3页 Pitfall 1](https://papers.miccai.org/miccai-2024/paper/2847_paper.pdf#page=3)。本题数据和系统为假设，不来自该论文实验。

## 五、完成一段自己的研究文字

选择你真实项目中的一个段落，保留原稿，并在旁边写三行：本段要让读者接受什么；哪些事实已经支持它；下一段要接住哪个对象。修改后检查：主张没有被偷偷扩大，也没有被无依据地削弱；句间增加了关系，而非只增加连接词。

最后请用中文解释你改得最重要的一处。只说“更地道”不够，要说明读者现在能更准确理解哪项科学关系。

## 阅读说明

以上来源实际用于所注明的引言、方法或问题诊断选段，不代表全文逐字审计或实验复现。方法论文是分析对象，也需要核查，不能把发表本身当作所有措辞都正确的保证。

关于限定与纠错的区别，可参阅 [Defensive Writing in GPT Models，2610.11355v2，§3.3](https://arxiv.org/html/2610.11355v2)。该预印本区分合理的主张修正与冗余限定；本讲将此作为设计练习的依据之一，不据此宣称本课程已经改善学习成绩。
