# GitHub Projects、任务分支与质量审查规范 v2

## 1. 建议建立一个总看板

名称：**Thought Writing Lab — Research & Learning Board**。

使用一个 GitHub Project 统一汇聚 Issue 与 PR，通过不同视图过滤，而不是每个子对话建立独立看板。本文件只是配置方案；目前**没有创建真实 Project 看板**。

建议字段：

| 字段 | 建议选项 |
| --- | --- |
| Status | Backlog → Ready → Researching → Evidence check → Draft PR → Review → Revision → Merged → Released；另设 Blocked |
| Program | Corpus / Language / Reasoning / Thought / Pedagogy / Daily / Engineering |
| Type | Long-term Program / Research Cycle / Finite Task / Audit / Release |
| Chat role | HQ / A / B / C / D / E / F / G / Q |
| Priority | P0 / P1 / P2 |
| Iteration | 建议初期采用 2 周规划周期，允许调整 |
| Source depth | Metadata / Abstract / Introduction / Full text / NA |

视图：HQ 总览、按研究组、当前周期、PR 审查队列、Release Roadmap、Blocked 依赖。

GitHub 支持 Issues 原生父子任务与 blocking 关系；用它们把长期 Program、阶段任务与确切依赖联系起来，勿仅在标题中手工标记 #N。

## 2. 分支生命周期

```text
Program Issue
  -> scoped Task Issue
  -> git branch from current main
  -> content + metadata validation
  -> Draft Pull Request
  -> independent challenge / review
  -> HQ checks duplicate IDs, privacy, cross-group semantics
  -> merge to main
  -> central index update and release record
  -> close this task and open next cycle
```

子分支命名：`agent/<domain>/issue-<N>`；主对话协调修改：`coord/<specific-topic>`。与具体任务无关的“永久功能分支”不宜不断分叉积累提交。

## 3. 审核门槛

| Gate | 负责角色 | 必要检查 |
| --- | --- | --- |
| G0 机械检查 | 提交者、CI | 修改路径在授权范围；格式正确；无敏感文件、重复 ID、无效引用 |
| G1 来源与科学 | A/B、D 或 Q | 真实原文、实际核读范围、实验支持程度、竞争解释 |
| G2 英语与叙事 | C 或 Q | 语法词义、科学主体与动作、信息推进、受众与论证一致 |
| G3 教学可用性 | F、HQ | 可独立完成的题目、答案分析、难度先修、跨情境迁移 |
| G4 总库整合 | HQ | 稳定编号、知识关系、私人总表、隐私/版权、版本记录 |

G3 只对面向学习者的成果强制适用；论文索引不必为了满足教学门槛而编造题目。G0 无法替代科学事实的审查。

每一项 PR 至少有“提交者自检 + 异域挑战/抽样核验 + HQ 审核”的记录。所有对话当前可能使用同一个 GitHub 身份，这不是技术上独立的审批体系。

## 4. 强制保护建议

仓库目前 `main` 尚未启用分支保护。请在 GitHub 仓库 Settings → Rules → Rulesets 为 `main` 设置：
- Require pull request before merging。
- Block force pushes 和删除主分支。
- 测试已有 `workstream-scope.yml` 的真实 PR 运行结果，确认成功之后再要求 `scope` status check。
- 可启用对话解决要求；不建议只有一个 GitHub 身份时强制需要另一个账号的 PR approval。
- 检查管理员例外是否允许绕过；CODEOWNERS 不会因不同聊天窗口变成不同权限身份。

**已有范围检查脚本和 PR 模板，但在没有真实 PR 运行之前，不能声称 CI 已经验证。**

## 5. 协作冲突分类

- 文件冲突：独占目录、短期分支、拒绝跨组直接修改公共文件。
- ID 冲突：临时 key，HQ 分配全局稳定 ID。
- 语义冲突：保留两种解释，回到证据与前提；不因 Git 自动合并而消失。
- 教学冲突：真实训练、答题过程与独立评分优先，不把“教材已写好”当成学习成功。
- 私有数据竞态：Google Sheets 私人索引只由 HQ/用户写，子对话只在 PR 中交付经过清理的待入库资料。

## 6. 推荐节奏

一次研究组专注一个主要 Issue；小批次 PR，避免超大跨主题合并。HQ 每次审核可以检查 3 个维度：**这次究竟发现了什么、证据是否足够、谁能实际使用它**。月度版本评估知识品质、训练反馈和跨组重复，任务可完成而 Program 保持持续开放。

## 7. 故障恢复

对话超长时，新子对话读取 Program Issue、任务 Issue、Git 分支 head、最近 PR 与相应规范，不能只依赖聊天记忆。旧分支相对 main 落后时先核对是否有独立提交；若没有可安全快进，有则在明确冲突后整合，禁止盲目 force push。

官方参考：
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
