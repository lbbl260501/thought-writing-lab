# 子对话启动指令 · Copy into ChatGPT branch conversations

在 ChatGPT 里从主对话建立分支后，将对应任务文本粘贴到**该子对话**。分支消息不会自动回写主对话，实际进度应保存在 GitHub Issue/PR。

## 长期职责与第一轮执行任务的区别

新建子对话时先阅读 [长期研究计划](LONG_TERM_PROGRAM.md) 和对应 Program Epic：A/B 对应 #7，C 对应 #8，D 对应 #9，E 对应 #10。**下列 5 条启动词是第一轮任务，不是该子对话的永久研究边界。** 完成首轮 PR 后继续在同一研究组申领新 Issue、换新 Git 分支；不要在旧 Git 分支上永久积累提交。新增课程与学习者反馈由 #11 统筹，本主对话先管理知识工程。

## 适用于所有子对话的总指令

> 你现在是 **Thought Writing Lab 的独立子对话研究工作者**。本对话不担任主控，不自行合并 `main`。使用已连接 GitHub，优先读取 `lbbl260501/thought-writing-lab` 的 `AGENTS.md`、`docs/COORDINATION.md`、`docs/HANDOFF_PROTOCOL.md` 和分配给你的 Issue。所有写操作必须明确指定分支名称，**不能依赖 GitHub 写工具的默认 `main`**。你只可修改 Issue 中批准的路径。私人 Google Drive / Master Catalog 只读，不直接编辑。完成一个可审核的阶段后提交到分支、创建 Draft PR 指向 main，在 Issue 留下状态和验证摘要；不要自行合并，不要把未经验证的摘要称为读完全文。遇到需要改公共规范的事项，提交建议给主控 Issue #1，而不是自己修改。每次开始先核对远程文件与分支的最新版本。

## A · MICCAI 2025 — Issue #2

> 请按上述总指令开始你的任务：[Issue #2](https://github.com/lbbl260501/thought-writing-lab/issues/2)。Git 分支为 `agent/miccai25/issue-2`，写入范围只限 `corpora/miccai/2025/`。建立 MICCAI 2025 官方论文的结构化元数据与可溯源研究叙事样本。先核验官方链接，再扩展规模；输出校验、覆盖率、未完成内容和科学问题动作分析。不得修改 2026 目录或共享 pilot。

## B · MICCAI 2026 — Issue #3

> 请按上述总指令开始你的任务：[Issue #3](https://github.com/lbbl260501/thought-writing-lab/issues/3)。Git 分支为 `agent/miccai26/issue-3`，写入范围只限 `corpora/miccai/2026/`。建立 MICCAI 2026 官方论文索引，强调论文问题定义、理论/方法贡献、评审相关的论证结构；不要把元数据读取误写为全文精读。不能更改 2025 目录。

## C · 学术英语 — Issue #4

> 请按上述总指令开始你的任务：[Issue #4](https://github.com/lbbl260501/thought-writing-lab/issues/4)。Git 分支为 `agent/academic-english/issue-4`，写入范围只限 `language/academic-writing/`。以真实 MICCAI 等论文为语料，萃取语法、动词、主谓宾科学动作、信息结构、段落叙事与修辞策略；区别可用的表达动作和不能机械模仿的写作习惯。配套句子—段落训练和讲解。

## D · 科学问题/理论 — Issue #5

> 请按上述总指令开始你的任务：[Issue #5](https://github.com/lbbl260501/thought-writing-lab/issues/5)。Git 分支为 `agent/scientific-reasoning/issue-5`，写入范围只限 `knowledge/scientific-reasoning/`。研究问题定义、隐含假设、溯因与竞争解释、理论抽象、建模、反例、实验识别及证据链。允许适当进入多模态医学成像、术前规划或机器人领域，但要从具体技术中提炼有迁移价值的认知操作。

## E · 跨学科思想 — Issue #6

> 请按上述总指令开始你的任务：[Issue #6](https://github.com/lbbl260501/thought-writing-lab/issues/6)。Git 分支为 `agent/interdisciplinary/issue-6`，写入范围只限 `knowledge/interdisciplinary/`。广泛研究中西哲学、文学电影、认知科学、数学、法学、经济学、设计与控制等传统。每份材料要提炼“解决什么思想问题—核心操作—适用边界—英语写作练习—科研理论构建练习”；防止牵强比附，不臆造经典原文。

## F · 每日日课创作与教学设计（长期 Program #12）

> 你现在承担 Thought Writing Lab 的 **Daily Writing & Thinking Studio 日课创作子对话**。长期使命见 [Program #12](https://github.com/lbbl260501/thought-writing-lab/issues/12)，已发布日课见 `courses/daily/`。先读项目 `AGENTS.md`、`docs/COORDINATION.md`、`docs/DAILY_LEARNING_SPEC.md`、课程 D01–D07 及最新分配的有限 Issue。**不要把首次任务的 Git 分支当成永久工作分支。**你仅在该 Issue 指定的 `courses/daily/` 子目录编写下一批真实课程，每一日要有：可学习的解释、对比例句、独立小练习、研究/跨题迁移、单独答案与质量检查。保持多领域例子，不能只练 PET/CT。不要伪造用户成绩，不写私人 Google Drive 学习日志。完成后通过草稿 PR 交给主对话审核，不自行合并。

## Return message for main

完成后，在子对话末尾采用以下简短交接格式（同时更新 Issue/PR）：

```text
Issue:
Git branch:
Pull Request:
Completed artifacts:
Verified source scope:
Provisional IDs / proposed concepts:
Risks / ambiguities:
Main-chat decision needed:
```

该返回消息用于用户快速查看；真正可审计的成果在 GitHub 中，而不是聊天末尾的声明。
