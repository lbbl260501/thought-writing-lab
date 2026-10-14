# Thought Writing Lab · 长期研究计划 / Living Research Program

**本文件是长期愿景与研究组分工，而不是一次性任务清单。**
Research Program → persistent workstreams / program Issues → versioned releases → small deliverable Issues → short-lived Git branches → Pull Requests → main.

## 研究使命

以英语语法、词汇、语篇、叙事写作与修辞为表达基础，以考试短写作、科学论文写作、理论与科学问题构建为主要应用；以中西哲学、文学、电影、数学、认知科学、控制论和其他思想传统作为开放的抽象方法来源，持续探索 **ideas → evidence → scientific narrative → writing competence** 之间的关系。

研究目标不是无限扩大词句收藏，而是建立能**溯源、可操作、可教学、可评价、可迁移、持续修订**的知识体系。

## 长期工作组（Epics）

| Program | Long-term mission | First-wave task | Owner of integration |
| --- | --- | --- | --- |
| [P-Corpus #7](https://github.com/lbbl260501/thought-writing-lab/issues/7) | 开放科研论文语料、问题类型、叙事/论证案例、来源审核；随年份和期刊扩展 | [MICCAI 2025 #2](https://github.com/lbbl260501/thought-writing-lab/issues/2), [MICCAI 2026 #3](https://github.com/lbbl260501/thought-writing-lab/issues/3) | main |
| [P-Language #8](https://github.com/lbbl260501/thought-writing-lab/issues/8) | 英语句法、语义、词汇、语用、语篇和科学修辞的可迁移动作体系 | [#4](https://github.com/lbbl260501/thought-writing-lab/issues/4) | main |
| [P-Reasoning #9](https://github.com/lbbl260501/thought-writing-lab/issues/9) | 科学问题、概念定义、假设、理论抽象、竞争解释、实验设计、论证和证据链 | [#5](https://github.com/lbbl260501/thought-writing-lab/issues/5) | main |
| [P-Thought #10](https://github.com/lbbl260501/thought-writing-lab/issues/10) | 全球思想传统、文学艺术和理工社会科学中的抽象方法与跨领域迁移 | [#6](https://github.com/lbbl260501/thought-writing-lab/issues/6) | main |
| [P-Learning #11](https://github.com/lbbl260501/thought-writing-lab/issues/11) | 教材、考研/四六级/雅思托福/科研小题与论文大练习、教学试用、反馈改进 | Next finite Issue to be assigned | main |
| [P-Infrastructure HQ #1](https://github.com/lbbl260501/thought-writing-lab/issues/1) | GitHub/Drive/Zotero/索引与语义一致性、标注审校、数据质量、发布与备份 | Managed centrally until safe delegation | main |

**P-Corpus 的 A/B 两个子对话在第一轮分别处理 2025/2026；以后可以重新分配为“资料接入与验证”及“跨论文研究分析”或新的领域批次，不把年份等同终身岗位。**

## 层次与生命周期

- **Program / Epic**：长久开放。不断产生新的研究问题、任务、版本和教学资源；只有战略上不再需要此研究方向时才关闭。
- **Research Cycle / Release**：一个明确的专题与质量门槛（例如 MICCAI 引言叙事类型 v0.2，或科学问题重构课程 v1）。
- **Task Issue**：有有限范围和验收准则，通常只覆盖一次可审阅的交付。
- **Git branch**：随任务而建，PR 合并后关闭/归档；**不**因为子对话长期存续，就令 Git 分支持续数月分叉。
- **ChatGPT topic conversation**：承担一个长期角色，并通过每轮 GitHub Issues/PR 实际工作。对话可交接/换代；角色与知识不会因聊天窗口失去上下文而消失。

## 永续的研究回路

1. **Sources**：接入开放论文/经典书籍，验证出处、许可、版本与覆盖。
2. **Extract**：抽取语言动作、叙事结构、论证结构、科学建模与思想方法；区分事实和解释。
3. **Compare**：跨论文、跨年份、跨学科比较，发掘共性、分歧和潜在新机制。
4. **Construct**：形成问题定义、推理策略、研究框架与可检验假设。
5. **Teach**：开发英语微练习、段落/篇章练习和科研论文工作坊。
6. **Evaluate**：人工检验科学忠实度、教学效果、迁移能力与薄弱环节。
7. **Revise**：把新证据和学习反馈回流至语料、概念库和教学版本。

这是一条具有反馈的循环，不是“收集完论文→生成教材→结束”的一次性流水线。

## 质量度量，不把数量误认为水平

| Dimension | Worth measuring | Misleading substitute |
| --- | --- | --- |
| Corpus | 可追溯的来源覆盖、抽样多样性、核读范围、重复率 | PDF 总数 |
| Language | 语境化动作解释、同义选择的差异、跨体裁迁移效果 | 高频词组数量 |
| Reasoning | 假设可检验性、推理依据完整度、反例区分力 | 公式和模块数量 |
| Thought | 原著忠实度、机制可操作性、跨学科边界和迁移证据 | 哲学家/书名数量 |
| Learning | 学习者能否独立诊断、修改和迁移，训练前后差异 | 讲义总页数 |
| Engineering | 索引稳定、私有数据隔离、版本可追溯、审计和恢复能力 | 仓库目录数量 |

## 节奏建议（非自动计划或固定截止日期）

- **持续 / whenever useful**：专题对话产出新事实、问题卡片、训练任务，保存在自己的 PR。
- **每一批可审核工作**：单独 Issue/分支/PR，主对话审核后整合到 main。
- **每 4–6 周建议一次整理**：按实际进度检查重复、证据强度、研究方向与课程缺口；不是要求自动运行。
- **每 1–3 个月建议发布一个可用版本**：可能是抽样语料集、系统讲义、一组完整科学问题训练，而非仅新增卡片。
- **每半年重新审视计划**：是否加入新会议、科研范式、教材用户测试；可以改变研究组和目标。

## 长期边界

1. 总体思维体系开放发展，不能让 MICCAI 独占写作风格和科学问题定义。
2. 既要有 **scientific persuasion/strategic framing**，也要有概念定义、理论推导、证据设计；不能把科学贡献还原为修辞包装。
3. 学生教材和项目管理资料始终分离。
4. 私有 Google Drive/Sheets 由主对话集中治理；公开 GitHub 只发布允许公开的索引和原创分析。
5. 只有经过来源核验、修辞/科学准确性审查和适当教学测试的内容，才升级为课程稳定版本。
6. 参照 [协作协议](COORDINATION.md) 保持分支隔离；一个研究组可有多轮任务和多个短期 Git 分支。

## 如何处理当前已有任务

当前 #2–#6 是 **Cycle 0 / first-wave seed tasks**：任务、分支和交付标准保持有效。它们完成后关闭的是该任务 Issue 和相应 PR，而不是长期 Program #7–#11。后续按实际发现创建下一轮有价值的 Issue，不需要为了维持“长期”把一个有限任务改得无限宽泛。
