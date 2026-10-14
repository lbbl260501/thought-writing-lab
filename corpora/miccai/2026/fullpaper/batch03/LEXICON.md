# 从主题词到科学动作：两篇全文的词汇与搭配库

本表含70条教学记录：18条专业/主题术语、22条动词、12条研究名词、12条形容词/复合修饰语、6条副词。记录数不等于独立词数，也不代表高频排名。

**F**＝[Paper5533官方PDF](https://papers.miccai.org/miccai-2026/paper/5533_paper.pdf)；**M**＝[Paper4859官方PDF](https://papers.miccai.org/miccai-2026/paper/4859_paper.pdf)。页码从1开始。来源列表示实际观察到该词或词形的位置；搭配槽位、语义区别和教学建议为原创归纳，不伪装成连续原文摘录。基本词形与过去式、分词、名词化形式须分别理解，本轮没有自动词性计数。

## 1. 专业术语与主题词：先组织知识对象

| ID | 术语/词群 | 在阅读中要辨明的含义 | 来源锚点 | 可迁移的学习动作 |
|---|---|---|---|---|
| T01 | paramagnetic rim lesion / PRL | 病灶类别名称，不是方法名称 | F §1 pp.1–2 | 记录全称、缩写与纳入对象；不能只记PRL三个字母 |
| T02 | quantitative susceptibility mapping / QSM | 成像方法与对应数据表征 | F §1 p.2 | 区分方法、影像和估计的物理量 |
| T03 | fluid attenuated inversion recovery / FLAIR | MRI序列名称 | F §1 p.2 | 写清它提供什么信息，不能以缩写替代解释 |
| T04 | magnetic susceptibility | 物理量，不是分类置信度 | F §1 p.2 | 留意susceptibility在物理语境与普通易感性语境的区别 |
| T05 | spatial feature-wise linear modulation / FiLM | 以调制关系组织特征操作 | F §2.1 p.4 | 同时记录条件源、作用对象和作用维度 |
| T06 | contrastive regularization | 训练约束的类别 | F Abstract p.1；§2.2 pp.4–5 | 与contrastive pretraining区分，记录作用阶段 |
| T07 | precision–recall AUC / PR-AUC | 排序表现的评价量 | F §3.2 p.6；Table1 p.7 | 不能替代某一阈值下的precision或recall |
| T08 | positive predictive value / PPV | 预测阳性集合中的评价量 | F §3.2 p.6；Table2 p.8 | 看清分母所指对象，而非只背中文译名 |
| T09 | perilesional information | 病灶周围的信息 | F §3.1 p.5 | peri-限定空间关系；与病灶内部信息区分 |
| T10 | microwave ablation / MWA | 治疗方式 | M §1 pp.1–2 | ablation在此不是模型组件移除实验 |
| T11 | thermal damage map | 热损伤的空间表示 | M §2.2 p.4 | map是表示形式，damage是被表示对象 |
| T12 | necrosis mask | 坏死区域的离散表示 | M §2.2 p.4 | 区分物理结局与二值标签 |
| T13 | perfusion rate | 描述灌注的模型变量 | M §2.1 p.3；§2.3 p.5 | 记录变量单位与获得方式，不只记录名称 |
| T14 | heat-sink effect | 本文用于描述血流相关散热问题 | M §1 p.2；§2.1 p.3 | 将现象名与解释该现象的变量连接 |
| T15 | surrogate model | 用于近似另一模型响应的替代模型 | M Abstract p.1；§2.2 p.3 | surrogate说明代理关系，不等同于一般轻量网络 |
| T16 | inverse problem | 从目标或观测反求未知条件的问题 | M §1 p.2；§2.4 p.5 | 先列已知和未知，再决定是否适合这个名称 |
| T17 | finite element method / FEM | 数值求解方法 | M §1 p.2；§2.1 p.3 | 与物理方程、替代网络分别归类 |
| T18 | ablation study | 改变组件以比较作用的实验 | M §3.1 p.6 | 对照T10，理解相同词在专业搭配中的不同指向 |

这些术语可以组成检索地图：F的“病灶—观察—表征—分类—评价”；M的“治疗—条件—响应—反求—验证”。地图是阅读组织，不是以高频词自动发现出的主题模型。

## 2. 动词：学习的是主体—动作—客体，不是同义词替换

下列搭配使用开放槽位X/Y，或是原创搭配归纳，不标记为作者原句。

| ID | 动词基本形 | 建议掌握的搭配/论元 | 科学动作与近义区别 | 来源锚点 |
|---|---|---|---|---|
| V01 | model | model a process / relationship | 为对象建立表征或形式描述，不等于仅训练一个网络 | F §2 p.3；M §2.1 p.3 |
| V02 | encode | encode X in/into Y | 强调信息被表示在哪里；不是自动证明信息全部保留 | F §2 p.3；M §2.2 p.3 |
| V03 | condition | condition X on Y | 明确依赖方向；不能随意替换成fuse | F §1 p.2；M §1 p.2 |
| V04 | modulate | modulate X using Y | 强调对已有对象施加变化；需说明如何变 | F §2.1 p.4；M §2.2 p.4 |
| V05 | denote | let X denote Y | 用符号指称对象；通常是定义而不是发现 | F §2.1 p.4；M §2.1 p.3 |
| V06 | represent | X represents Y | 既可说明表示关系，也可解释变量含义；要看主语类型 | F §2.2 p.5；M §2.1 p.3 |
| V07 | generate | generate coefficients / samples | 生成对象，通常还需要来源、条件或分布 | F §2.1 p.4；M §2.3 p.5 |
| V08 | extract | extract X from Y | 指明来源和抽取对象；不要省掉空间/实例单位 | F §3.1 p.5；M §3.1 p.6 |
| V09 | preserve | preserve a property / context | 描述保留对象；比use多承诺一个“不被破坏”的性质 | F §2.1 p.4；§3.1 p.5 |
| V10 | incorporate | incorporate X into Y | 将某信息或项纳入系统；与该项已经有效不同 | F §2.2 pp.4–5；M §2.2 p.4 |
| V11 | mitigate | mitigate an effect / limitation | 减轻，而非必然消除；具体宾语比泛称problem好 | F §3.1 p.5；M §1 p.2 |
| V12 | optimize | optimize parameters with respect to an objective | 必须区分被调整的变量与用于选择的目标 | F §3.2 p.6；M §2.4 p.5 |
| V13 | evaluate | evaluate X on Y / under Z | 区分被评价对象、样本与条件 | F §3 pp.5–9；M §3 pp.6–8 |
| V14 | compare | compare X with/against Y | 明确比较单位、参照和共同条件 | F §3.3 p.6；M §3.2 p.7 |
| V15 | isolate | isolate the contribution of X | 主张区分某因素的独立作用，需要匹配对照 | F §3.3 pp.6–7 |
| V16 | yield | yield a result / representation | 连接操作与产物；不自行解释成因 | F §3.3 p.8；M §3.1 p.7 |
| V17 | indicate | a pattern indicates X | 由观察走向含义；应检查这个推断是否唯一 | F §3.3 pp.7–9；M §3.1 p.7 |
| V18 | suggest | results suggest that… | 将解释作为得到支持的可能判断，而非定义 | F §3.3 p.8 |
| V19 | improve | improve a named outcome | 必须点明改善对象、基线及方向；不能只写improve performance | F §3.3 p.8；M §3.2 p.7 |
| V20 | enable | enable X / enable Y to do Z | 描述新增可行能力；因果衔接应能说明 | F §2.1 p.4；M §1 p.2 |
| V21 | support | evidence supports an interpretation | 连接证据和主张，不表示排除了所有替代解释 | F §3.3 p.8 |
| V22 | assess | assess performance / a property | 根据所用标准作判断，需交代标准与对象 | F §3.2 p.6 |

**近义选择示范（原创）**：compute强调按规则计算；estimate强调对未知量的估计；predict强调对目标响应的预测；infer强调由证据推断；optimize强调在目标下选择。这个扩展对照是语言教学，不声称五个词都在两篇中以动词出现。

## 3. 研究名词：有的命名对象，有的把前文打包

| ID | 名词 | 常用关系/搭配槽位（原创归纳） | 应区分什么 | 来源锚点 |
|---|---|---|---|---|
| N01 | representation | a representation of X | 表示对象与表示方式；并非feature的万能替换 | F §2.1–2.2 p.4 |
| N02 | feature | features extracted from X | 数据或网络中的特征；具体层次需已知 | F §2.1 p.4 |
| N03 | embedding | an embedding in a specified space | 将对象放到某表征空间中时的表达 | F §2.2 pp.4–5 |
| N04 | objective | an objective for X | 可以是研究目的，也可以是优化目标；在方法中须消歧 | F §2.2 pp.4–5 |
| N05 | loss | a loss applied to X | 训练中的量；不是任意实验指标 | F §2.2；M §2.2 p.4 |
| N06 | constraint | a constraint on X | 限制可接受解，不等于一个被奖励的性能目标 | M §2.4 p.6 |
| N07 | metric | a metric of/for X | 衡量表现的尺度，需定义方向及单位 | F §3.2 p.6 |
| N08 | cohort | a cohort drawn from X | 指研究人群；与patch集合不是同一层对象 | F Abstract p.1；§4 p.9 |
| N09 | prevalence | prevalence of X | 描述对象在群体中的比例；与总样本数不同 | F §3.1 p.5 |
| N10 | runtime | runtime per X | 计算时间；必须交代每次推断、每病例或完整流程 | M §3.1 pp.6–7 |
| N11 | generalization | generalization to/across X | 从已见条件迁移到何种未见条件；不是无边界褒义词 | F §1 p.2；M §3.1 p.7 |
| N12 | rationale | a rationale for X | 将前面理由打包为后面选择的依据 | M §2.2 p.4 |

作为额外的衔接名词，可学习limitation、difference、pattern、choice、trade-off、finding等：先有可识别的前文，再用this/these＋具体名词接住。它们不是任何位置都能塞入的“学术词”。例如this difference应明确指前文哪一差异。

## 4. 形容词及复合修饰语：区分对象限定与评价判断

| ID | 词项 | 修饰功能 | 写作时要问什么 | 来源锚点 |
|---|---|---|---|---|
| A01 | asymmetric | 关系结构 | 不对称的两个对象和方向是什么？ | F §1 p.2 |
| A02 | primary | 角色优先性 | 是主要信号、主要目标还是主要指标？ | F §1 p.2；§2.2 p.5 |
| A03 | structural | 信息类型 | 与什么非结构信息相对？ | F §1 p.2 |
| A04 | spatial | 作用维度 | 是空间变化、空间分辨率还是空间支持？ | F §2.1 p.4 |
| A05 | threshold-independent | 评价条件 | 哪类指标不依赖单个决策阈值？ | F §3.2 p.6 |
| A06 | patient-specific | 条件来源 | 哪些量真随个体改变，哪些仍是统一参数？ | M §1 pp.1–2 |
| A07 | synthetic | 数据来源 | 是解剖、影像、标签还是完整模拟由程序生成？ | M §2.3 p.5 |
| A08 | robust | 能力判断 | 对什么变化稳定，在什么范围内得到支持？ | F §4 p.9；M §3.1 pp.6–7 |
| A09 | severe | 程度 | 程度由什么数值或比较支持？ | F §2.2 pp.4–5 |
| A10 | limited | 可用范围/数量 | 究竟是标签少、病例少还是采集条件有限？ | F §2.2 p.4 |
| A11 | efficient | 相对资源表现 | 相对谁、以什么资源单位、维持什么表现？ | M §1 p.2 |
| A12 | comparable | 比较关系 | 近似来自数值观察还是正式等效性判断？ | M §3.1 p.7 |

限定型修饰语通常增加研究信息；评价型修饰语并非不应使用，但需要明确坐标。不要为了“严谨”把所有形容词删除，也不要为了“有论文味”堆叠robust、effective、powerful。

## 5. 副词：它们常改变承诺的边界

| ID | 词项 | 信息作用 | 容易混淆的点 | 来源锚点 |
|---|---|---|---|---|
| D01 | explicitly | 说明关系被直接表达 | 显式建模不等于已经证明模型学会了该关系 | F §1 p.2；M §2.2 p.4 |
| D02 | independently | 限定操作关系 | 独立标注、独立归一化、独立采样不是同一性质 | F §3.1 p.5 |
| D03 | jointly | 说明联合动作 | 联合审阅与联合预测具有不同主体/客体 | F §3.1 p.5；M §2.2 p.4 |
| D04 | substantially | 描述幅度 | 要能回到数字，不能仅等同于统计显著 | F §3.3 pp.7–8；M §3.2 p.7 |
| D05 | exclusively | 排除其他来源/条件 | 排除范围必须附着在正确对象上 | M §1 p.2；§4 p.8 |
| D06 | approximately | 标记近似 | 应保留数量级和单位，不是忽略误差的借口 | F §3.2 p.6；M §3.1 p.7 |

## 6. 怎样用，而不是怎样背

每次围绕一个写作任务取一个小组合。例如写方法定义时选择`denote + representation + spatial`，写比较时选择`compare + runtime + per case`，写讨论时选择`indicate + pattern + under a specified condition`。先把研究对象填实，再确定语法，最后才调整措辞。

一条可复用记录至少需要“词/结构—搭配—语义区别—原文定位—本次句子功能—原创迁移”。只保留中文译名，会丢掉大部分写作价值。