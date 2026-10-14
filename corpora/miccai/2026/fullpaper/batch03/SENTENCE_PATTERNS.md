# 句子为什么好：从语法结构到段落动作

F＝[Paper5533 PDF](https://papers.miccai.org/miccai-2026/paper/5533_paper.pdf)，M＝[Paper4859 PDF](https://papers.miccai.org/miccai-2026/paper/4859_paper.pdf)。两篇的原句短引及细读分别在[PAPER5533](PAPER5533.md)和[PAPER4859](PAPER4859.md)。本页所有完整英语示范句均为本库原创，不能回填成论文引文，也不代表已经完成的实验。

“来源位置”是促成该结构分析的原文位置；通用结构是抽象归纳，不声称作者逐字使用了槽位模板。以下16种是本轮选择的可迁移功能，不是全会议高频排行。

## 一、从题名到结论的16种功能句式

### S01｜题名：中心任务与范围

来源：F题名，p.1；M题名，p.1。

结构：`[Task] of/for [Object] under/in [Conditions] using/via [Approach]`。

原创示范：*Classification of Ambiguous Regions Using Context-Conditioned Features*。

题名的中心名词应让读者先知道任务。using/via说明途径，不应承担尚未说明的因果证明。不要机械把所有槽位塞进一个过长标题；方法名可以省略，但研究对象不能被口号取代。

### S02｜摘要：输入与输出

来源：M Abstract，p.1；F §2.1，p.4。

结构：`Given [inputs], [system] predicts/returns [output] for [unit]`。

原创示范：*Given the two registered images, the model returns a lesion-level score.*

主语model，谓语returns，宾语score；Given部分建立输入前提，lesion-level限定输出单位。这个句式不能替代后文对registered和score的定义。

### S03｜引言：承认能力，同时说明使用障碍

来源：M §1第二段，p.2。

结构：`Although [existing capability], [specific constraint] limits [use]`。

原创示范：*Although detailed simulations capture spatial variation, their cost limits repeated evaluation during planning.*

从句承认已有能力；主句把cost放在主语位置，让限制因素成为注意中心。主句客体不是泛泛的performance，而是具体的repeated evaluation。该结构比“已有方法很差”能容纳更真实的对手。

### S04｜引言/方法：让两个对象形成关系，而非并列清单

来源：F §1贡献块，p.2；§2总览，p.3。

结构：`A [does X], while B [does Y]`。

原创示范：*One stream represents the target signal, while the other supplies contextual cues.*

while可以表达对照或同时性，此处承担角色对照。两边必须保持可比较的语法层级；不要前半句谈输入，后半句突然谈最终指标。

### S05｜方法：目的与操作

来源：F §2.2，p.4；M §2.2，p.3。

结构：`To [purpose], we [operation] on/with [object]`。

原创示范：*To reduce dependence on manual labels, we initialize the encoder from unlabelled observations.*

不定式给意图，主句给实际选择。purpose不是已证明结果；后文需要用实验判断是否实现。若只是报告执行步骤，不必给每句都加To improve。

### S06｜方法：建立符号

来源：F §2.1，p.4；M §2.1，p.3。

结构：`Let [symbol] denote [object], where [scope or index definition]`。

原创示范：*Let z denote the regional representation, with one vector assigned to each candidate.*

denote是指称约定。object应足够具体，使下一条公式无需猜测维度或索引。不要把符号引入、优化目标和实验结果全部挤进这个定义句。

### S07｜方法：映射方向

来源：M §2.2架构段，p.4；F §2.2，p.4（原文方向疑点见AUDIT）。

结构：`[operator] maps [source] to [target]`。

原创示范：*A projection maps the contextual vector to the coefficients used by the modulation layer.*

source是输入，target是输出。from/to看似基础，却决定计算方向。论文公式与邻近文字发生冲突时，不能为了保留顺滑表达而自行选一个方向当作既定事实。

### S08｜方法：保持数据流对象连续

来源：F §2.1分类段，p.4。

结构：`After [operation], [resulting object] is [processed] and [passed onward]`。

原创示范：*After modulation, the adjusted features are pooled and passed to the classifier.*

被动语态让features继续占据主语位置；两个并列分词作用于同一对象。被动语态不是越少越好，关键是它是否保持读者正在追踪的对象。

### S09｜方法：说明第二个量为什么不是重复

来源：M §2.2损失说明，p.4。

结构：`X complements Y by providing [a distinct type of information]`。

原创示范：*The continuous target complements the binary label by retaining graded information near the boundary.*

complements是关系动词，不等于improves。by部分应解释差别来自哪里，不能只写“by providing complementary information”这种循环解释。

### S10｜实验：筛选规则

来源：F §3.1，p.5；M §3.2，p.7。

结构：`[Units] were included/excluded if [criterion], to/for [stated reason]`。

原创示范：*Cases with incomplete acquisition records were excluded from the comparison.*

were excluded报告已经执行的程序；from限定被排除的分析范围。不要把分析排除自动写成整个研究人群不存在这些病例。

### S11｜实验：公平比较的共同条件

来源：F §3.2 Evaluation，p.6。

结构：`All [comparators] were evaluated using the same [specified conditions]`。

原创示范：*All models were evaluated with identical case partitions and preprocessing rules.*

identical限定具体对象，不概括性宣布所有比较都公平。这个句式用于交代控制项，而不是代替对各模型训练策略的说明。

### S12｜实验：重复程序与覆盖关系

来源：F §3.2，p.6。

结构：`The procedure was repeated [schedule], such that [coverage property]`。

原创示范：*The procedure was repeated across the partitions, such that every case appeared in the test set once.*

such that给出安排形成的覆盖性质。注意test与validation不能互换；once修饰的是每个case的测试出现次数，而不是整个训练只运行一次。

### S13｜结果：比较方向和绝对变化

来源：M §3.2，p.7。

结构：`[Metric] increased/decreased from [baseline] to [new value] under [setting]`。

原创示范：*The error decreased from 8 to 5 units under the fixed evaluation protocol.*

数值为教学假设。from/to保留绝对尺度；用increased/decreased还是improved，应由指标方向决定。先说明哪一指标变化，再解释是否构成任务收益。

### S14｜结果：同时保留第二个评价轴

来源：F §3.3，p.8；M §3.1，p.7。

结构：`X [improves A] while [maintaining/reducing B]`。

原创示范：*The reduced model retained similar accuracy while requiring less memory.*

requiring的语义主体仍是model。若第二部分谈的是别的对象，可能需要完整从句。similar也不等于经过正式等效检验；应按实际证据选择表述。

### S15｜讨论：让解释接在可识别的观察之后

来源：F §3.3，p.8。

结构：`This [specific pattern] suggests/supports [interpretation]`。

原创示范：*This concentration of errors suggests that local context remains a limiting factor.*

This后加具体名词可避免指代漂移。suggests不能让缺乏前文依据的猜测突然合理；supports也不自动表示排除了其他解释。动词的选择取决于本句正在报告、定义还是推断，不是一条机械的强弱阶梯。

### S16｜结论：从已完成范围推到有对象的下一步

来源：F §4，p.9；M §4末段，p.8。

结构：`The present study addresses [scope]; extending it to [new condition] requires [specific work]`。

原创示范：*The present study considers isolated targets. Extension to interacting targets requires an explicit account of their coupled effects.*

此处拆成两句，使“范围”与“下一问题”各自明确。requires连接的应是真正缺少的对象或能力，而不是泛称more experiments。

## 二、四种关键语法选择，不能只记模板

### 1. 主动/被动由信息中心决定

原创对比：*We normalize each image before feature extraction.* 与 *Each image is normalized before feature extraction.*

第一句强调作者的程序选择，第二句让image保持数据流中心。二者都可能合适，不存在整个方法部分统一改成主动或被动就一定更好的规则。

### 2. 时态由对象决定，不仅由章节标题决定

原创对比：*The operator rescales the feature map.* 描述算子的定义或常规作用；*We rescaled the feature maps before evaluation.* 报告已经执行的操作；*We will examine other acquisition settings.* 表示未来计划。

同一方法章节可以包含前两种时态。结果表目前展示什么，与研究当时做了什么，也不一定使用同一种时态。Manchester的[方法写作说明](https://www.phrasebank.manchester.ac.uk/describing-methods/)可作为功能分类的补充，但不能替代具体论文的语境判断。

### 3. 非谓语要有明确的逻辑主体

原创较弱句：*Using the auxiliary signal, the accuracy increased.* 语法上很容易让accuracy成为using的执行者。

原创改写：*Using the auxiliary signal, the model achieved higher accuracy.* 或 *Accuracy increased when the auxiliary signal was included.* 前者明确动作主体，后者把条件放入从句；两句仍需真实比较支持。

### 4. 名词化既能衔接，也能掩盖动作

原创繁重句：*The implementation of the integration of contextual information enables the improvement of prediction.*

原创改写：*The model integrates contextual information to refine its predictions.*

但不要把名词化一律删除。*This integration…*可以把前句已知的过程打包，成为下一句讨论计算开销或限制的对象。关键是“先展开动作，再在需要时打包”，而不是每句都用抽象名词垒高。

## 三、把词、句式、中观推进和宏观问题放在一段里

以下两个段落全部原创、仅供学习，不是任何一篇的研究结果。

### 示例A：方法段，不让每句话都重新从we开始

*The two observations capture different aspects of the same region.*

*We therefore retain separate representations before specifying their interaction.*

*A conditioning operator uses contextual features to adjust the target representation.*

*The adjusted features are then passed to a shared prediction head.*

| 句子 | 已知→新增 | 主体—动作—客体 | 段落作用 |
|---|---|---|---|
| A1 | 同一区域→不同观察角色 | observations—capture—aspects | 建立设计前提 |
| A2 | 不同角色→暂时保留分别表示 | we—retain—representations | 给出设计选择 |
| A3 | 分别表示→相互作用 | operator—uses/adjusts—features/representation | 交代操作 |
| A4 | 调整产物→下游接口 | features—are passed—head | 关闭过程段落 |

段落的宏观作用是将“信息关系”变成“可实现关系”；中观结构是前提—选择—操作—接口；微观靠therefore、before、adjusted、then及主语交接实现。可见三层分析必须同时存在。

### 示例B：结果段，数值报告之外仍要完成新动作

*Both variants were assessed with the same cases and decision threshold.*

*The contextual variant produced fewer false-positive predictions.*

*The difference was largest near structures that resembled the target.*

*This pattern supports further testing of context-sensitive discrimination.*

第一句限定比较，第二句给方向，第三句定位差异，第四句提出下一步解释性检验。不是第二句说higher、第三句改说superior、第四句改说effective。这种同义重复看似学术，实际上没有推进。

## 四、图表和题注也应采用同样的读法

本页未把题注挤进16种编号句式。可分别观察F Fig.2/Table1、M Fig.2/Table1：题注需要交代“画的或列的是什么、比较谁、如何汇总、如何解释符号”。正文引用图表后，应提炼一条值得读者注意的关系，而不是重抄所有数字。

原创题注骨架：*Comparison of [objects] under [conditions]. Values summarize [aggregation unit]; [symbol] denotes [meaning].* 使用时必须填写真实单位、重复层级及符号，不能只保留漂亮形式。

**本页的验收问题**：换掉研究对象之后，你能否仍然说明每个主语指什么、动词做了什么、修饰语限定哪里、下一句为何接得上？能，才是可迁移的句式；只能替换模型名，仍然只是模仿。