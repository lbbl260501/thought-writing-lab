# 标注协议 v0.1：从原文到科学思想动作

## A. 文献和核读状态（强制）

每条记录至少包含：
- `source_id`, `year`, `title`, `authors`, `official_url`, `official_pdf_url`
- `doi`（未知留空）、`presentation_type`（须官网日程核验）
- `verification_status`: `metadata_verified`, `abstract_and_reviews_verified`, `introduction_read`, `fulltext_audited`
- `checked_scope`：实际访问了摘要、评审、PDF 引言还是完整方法/结果。
- `source_locator`：页码、段落或章节；作者自己的主张与评审意见分别标注。

**不能把 `introduction_read` 写成 `fulltext_audited`，更不能把访问了摘要写成读完论文。**

## B. 五层分析表

### L1 语言层
为选定句子记录：`subject`, `scientific_verb`, `object`, `modifier`, `syntax`, `given_information`, `new_information`, `claim_strength`, `register`。
原句引文仅限获得许可或法律允许的短引；通常优先使用原创、带出处的释义与模式，而不是大段复制。

### L2 叙事层
按句序记录 `narrative_move`（可多选），例如：
- `ESTABLISH_TASK` 定义任务/意义
- `INTRODUCE_OBSERVATION` 提出现象
- `RECOGNIZE_CAPABILITY` 承认已有方法成就
- `IDENTIFY_TENSION` 建立特定矛盾
- `QUESTION_ASSUMPTION` 质疑隐含假设
- `REFRAME_PROBLEM` 重新设定问题/评价轴
- `DEFINE_OBJECT` 明确概念/对象
- `MOTIVATE_PRINCIPLE` 解释设计原则
- `PROPOSE_METHOD` 提出实现
- `REPORT_EVIDENCE` 引入结果
- `QUALIFY_SCOPE` 限定结论
- `STATE_CONTRIBUTION` 归纳贡献

同时记录 `paragraph_role`、`transition_dependency`、信息释放顺序及对手结构。

### L3 论证层
`claim → grounds → warrant → alternatives → evidence → qualifiers`。
明确区分作者的断言、论文实际验证过的事实、审稿人的质疑和知识库分析者的新推测。

### L4 科学构建层
`observed_problem` → `formal_object` → `working_hypothesis` → `method_design` → `discriminating_experiment` → `failure_modes`。
没有数学公式不意味着没有科学问题；引用公式时需核对定义、适用前提和符号。

### L5 评价与策略层
- `contribution_positioning`: performance / new task / modeling insight / robustness / efficiency / deployment / evaluation paradigm 等。
- `reviewer_challenge`: 是否担忧新颖性、实验、公平比较、复现或临床可行性。
- `framing_alternatives`: 在不改变观察事实情况下，另有何种主张可能成立？
- `required_new_evidence`: 不同主张还需要哪些具体实验？

## C. 证据分级

- `VERIFIED_SOURCE`：来源中的确有该项事实，给出页码或网址。
- `AUTHOR_CLAIM`：论文作者所主张的结果，未经本库独立复现。
- `REVIEWER_OPINION`：同行评审的看法，不能自动当作事实。
- `ANALYST_INTERPRETATION`：对文本组织的原创分析。
- `TRANSFER_HYPOTHESIS`：可用于其他任务的设想，还需要实验或实践验证。

## D. 阅读者训练输出
1. **模仿**：复现某个动作而不照抄论文句子。
2. **诊断**：指出原文论证是否充分、信息结构是否自然。
3. **重构**：在不修改事实的情况下写出另一种主张或引言路径。
4. **迁移**：将该动作带到不同领域的论文、CET/考研/雅思/托福短写作任务。
5. **设计实验**：说明何种新证据能强化或削弱不同叙事主张。

## E. 输出模板

```yaml
source_id: PAPER-XXXXXX
section: introduction
verified_scope: introduction_read
paragraph_role: specific scientific tension
move_sequence: [RECOGNIZE_CAPABILITY, QUESTION_ASSUMPTION, REFRAME_PROBLEM]
scientific_claim: "analyst paraphrase"
evidence_location: "PDF p. 2, section 1"
warrant: "why the evidence should imply the claim"
alternatives: []
linguistic_patterns: []
reviewer_challenges: []
possible_exercises: []
analyst_confidence: provisional
```

**不要将频率统计自动转化为写作规范**：顶会短论文的叙事篇幅与 MIA/TMI 的长文不同；还应比较不同体裁与审稿语境。
