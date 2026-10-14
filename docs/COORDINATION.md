# 多对话并行协作协议 · Coordination v1.1

> **新版本索引**：详细的研究室职责与多方协作，请以 [Operating Model v2](OPERATING_MODEL_V2.md)、[跨组数据契约](WORKSTREAM_DATA_CONTRACTS.md) 和 [GitHub 审查规范](GITHUB_PROJECT_AND_REVIEW.md) 为补充。下文保留 Cycle 0 的现有分支与任务绑定，避免丢失历史。

> **This ChatGPT conversation is the main coordination chat.** Its children are independently operating research/writing conversations. GitHub is the durable shared state; a ChatGPT branch is **not** a Git branch.

- 总控 Issue：[HQ #1](https://github.com/lbbl260501/thought-writing-lab/issues/1)
- 子对话启动词：[CHAT_BRANCH_STARTERS.md](CHAT_BRANCH_STARTERS.md)
- 交接标准：[HANDOFF_PROTOCOL.md](HANDOFF_PROTOCOL.md)
- 核心科研/写作标准：[AGENTS.md](../AGENTS.md)、[SCHEMA.md](SCHEMA.md)、[MICCAI annotation guide](../corpora/miccai/ANNOTATION_GUIDE.md)

## 0. Long-lived Program vs finite task (重要更新)

长期安排见 [LONG_TERM_PROGRAM.md](LONG_TERM_PROGRAM.md)。已有五个子对话分工是 **Cycle 0 / seed tasks**，不是终身只研究 MICCAI 2025/2026 或完成 10 张卡片就停止。

- **一个长期子对话可以连续完成多个 GitHub Issues 和多个短期任务分支**；不要把聊天分支与 Git 分支的生命周期绑定。
- **#7–#11 是长期 Program Epics**；#2–#6 是第一轮有限任务。知识工程由 HQ #1 暂行承担。
- 子对话应在当前任务完成后返回主对话申领/创建下一轮任务，从最新 `main` 创建**新分支**，并废弃/归档已合并的旧分支。
- 即使 ChatGPT 对话因篇幅需要开启继任会话，只要以 GitHub Program/Issue/PR 为上下文，研究角色仍可持续。
- 原有独占目录只对 **当前第一轮任务**有效；未来跨领域扩展需要为每个新 Issue 单独确定路径，不能私自放宽权限。

## 新增应用端：F · 每日个人学习

长期领域由 [Program #12](https://github.com/lbbl260501/thought-writing-lab/issues/12) 管理。项目公开的日课属于 `courses/daily/`，由 main 审核后进入正式课程；可由专门的 F 子对话在**下一轮有限任务 Issue**范围内撰写。私人完成记录、作文原稿、评分、补救练习调整由 main 与用户管理，**F 子对话仅负责公共教材的生产**，不直接改私人 Google Sheets。

首个 28-Day 路线与 Week 01 日课由 main 初始化；后续每个 Week 形成新 Issue + 新 Git branch，不能把课程发布当作学习者已完成。

## 1. 权威来源与角色

| What | Authoritative location | Write responsibility |
| --- | --- | --- |
| Overall project direction, common schemas, stable IDs | `main`: README, AGENTS, docs, central taxonomies | **Main coordination chat** |
| Source files, personal PDFs, permissions | Private Google Drive/Zotero | **Main coordination chat**; child chats may read authorized sources |
| Global index and relational links | Private Google Sheets Master Catalog | **Main coordination chat only** |
| Research drafts, corpus intake, candidate methods | Per-task GitHub branch, assigned folder | Child chat assigned to task |
| Final accepted published materials | Reviewed Pull Requests merged into `main` | Main coordination chat |

**Important:** All ChatGPT branches may share the same connected GitHub/Drive account. This is a **collaboration protocol**, not a technical permission boundary. A GitHub ruleset must be configured in the repository to make PR-only main updates enforceable.

## 2. Cycle 0: Five independently writable workstreams

| Chat/workstream | GitHub Issue | Exact Git branch | Only allowed paths |
| --- | --- | --- | --- |
| A · MICCAI 2025 | [Issue](https://github.com/lbbl260501/thought-writing-lab/issues/2) | `agent/miccai25/issue-2` | `corpora/miccai/2025/` |
| B · MICCAI 2026 | [Issue](https://github.com/lbbl260501/thought-writing-lab/issues/3) | `agent/miccai26/issue-3` | `corpora/miccai/2026/` |
| C · 学术英语与语篇 | [Issue](https://github.com/lbbl260501/thought-writing-lab/issues/4) | `agent/academic-english/issue-4` | `language/academic-writing/` |
| D · 科学问题与理论 | [Issue](https://github.com/lbbl260501/thought-writing-lab/issues/5) | `agent/scientific-reasoning/issue-5` | `knowledge/scientific-reasoning/` |
| E · 跨学科思想方法 | [Issue](https://github.com/lbbl260501/thought-writing-lab/issues/6) | `agent/interdisciplinary/issue-6` | `knowledge/interdisciplinary/` |

Child agents are **not** allowed to edit files outside the assigned path, even if they believe a shared standard needs improvement. Record such proposals in their Issue or PR, and let the main chat update authoritative files.

Shared main-owned files include `README.md`, `AGENTS.md`, `docs/`, `.github/`, `catalog/`, `corpora/miccai/ANNOTATION_GUIDE.md`, `corpora/miccai/pilot/`, and the existing student-facing lesson release files.

## 3. Workflow: Issue → Chat → Git branch → Draft PR → review → main

1. **Main assigns work** in a finite Issue linked to one of the persistent [Program Epics](LONG_TERM_PROGRAM.md), with objectives, accepted path range, evidence standard and checkable output.
2. **User starts a ChatGPT branch chat** (or a fresh chat in the same Project), pastes the corresponding starter from `CHAT_BRANCH_STARTERS.md`, and names the chat after the Issue.
3. **Child reads live GitHub state** — `AGENTS.md`, this file, assigned Issue, and current branch; reading previous ChatGPT messages alone is not a reliable synchronization channel.
4. **Child works only in the assigned Git branch**. Every tool write must specify the exact branch or update its ref, never default to `main`.
5. **Child opens a Draft PR to `main`** when work is substantial enough to review; leave it unmerged. Share a compact update in the Issue.
6. **Main evaluates** content, traceable evidence, deduplication, cross-track meaning conflicts and privacy; allocate global IDs and update private catalog.
7. **Main merges** accepted PRs, posts integration outcome in the HQ Issue; child closes the finite task and starts the next task from the latest `main` on a *new* Git branch. The long-term domain responsibility remains active.

GitHub PRs, not ChatGPT fork history, represent reviewable changes. Child chats are not expected to know work done in other chats after they branched.

## 4. Four kinds of conflict

| Failure mode | Prevention |
| --- | --- |
| Same-line file conflicts | Separate workstream paths; one Issue + one short-lived Git branch per task |
| Duplicate IDs or metadata | Children use `DRAFT-ISSUE-NN-XXX` or official MICCAI `year:paperID` as provisional keys; main checks deduplication before assigning `PAPER-`, `MOVE-`, `EX-` |
| Scientific/semantic conflicts | Explicit source locators, evidence levels, competing interpretations and central editorial review; Git may merge text while meanings still disagree |
| Shared-index/state races | Children do not modify Google Sheets Master Catalog, shared Drive folder organization or authoritative taxonomies; submit sanitized candidate metadata in PR |

## 5. Git discipline and readback

- Branch names should be task-scoped and short-lived, e.g. `agent/miccai25/issue-2`. Do not keep one diverging branch indefinitely.
- Make small topic commits; validate the current head before updating a branch ref. No force pushes.
- Put metadata and working files in assigned directories; do not publish raw copyrighted PDFs, private Drive IDs, API tokens or personal attachments.
- Child deliverables must be original analysis, not unreviewed mass extraction or academic text copying.
- Draft PRs are encouraged to expose progress; only the main chat can request integration.
- After each completed operation, re-read the remote file/PR and verify it exists. Do not claim a task is complete merely because a local draft exists.
- If a task needs another track, raise a dependency in the Issue rather than changing another branch's files.

## 6. Practical protection to enable in GitHub UI

At [repository settings / rulesets](https://github.com/lbbl260501/thought-writing-lab/settings/rules) or branch protection:
- Target `main`.
- Require a pull request before merging.
- Block force pushes and deletion.
- Once automated checks are active, require the `scope` check if it runs reliably.
- For a **single GitHub account**, do not require one independent review approval that you cannot grant to your own PR. Main-chat review is a workflow decision, **not** a second GitHub identity.
- Optionally use CODEOWNERS to mark ownership, not as a substitute for real human code review.

Rulesets/branch protection have not been automatically enabled merely by writing this document.

## 7. Recommended start order

Start with A (2025), B (2026), C (English), D (scientific reasoning), E (interdisciplinary methods). Main handles merge, stable identifiers, data hygiene, and later synthesis into learner-facing `courses/` and `practice/`.

**Source of truth:** If ChatGPT chat history and GitHub disagree about task status, check the verified GitHub commit and PR before deciding what happened.
