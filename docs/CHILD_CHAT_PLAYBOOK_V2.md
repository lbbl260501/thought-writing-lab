# 子对话操作手册与交接模板 v2

## 主对话 / HQ（本对话）

职责：批准 Program 与 Issue、限定可修改路径；解答跨组定义/引用冲突；对 PR 做科学与教学审查；协调个人每日训练与私有学习反馈；分配正式编号并维护总索引；发布版本。

一次主对话调度顺序：
1. 读取 GitHub main 最新提交、开放 Issues、PRs 和各分支是否超前或落后。
2. 选至多几个能够独立推进的任务；确认依赖和写入目录没有重叠。
3. 对缺陷明确说明“哪些结论需要哪种新证据”，而不是只要求更多内容。
4. 合并通过的 PR，验证 main，再更新私有索引和 HQ 任务状态。
5. 从个人真实写作错误中提炼可共享的课程改进请求；**不分享私人原稿**。

## 所有子对话统一开场指令（可复制）

> 你是 Thought Writing Lab 项目的专题研究子对话。请先读取 GitHub 仓库 lbbl260501/thought-writing-lab 的 AGENTS.md、docs/OPERATING_MODEL_V2.md、docs/WORKSTREAM_DATA_CONTRACTS.md、docs/GITHUB_PROJECT_AND_REVIEW.md，再读取分配给我的 Program Issue 与 Finite Task Issue。以 GitHub 最新已验证状态而非旧聊天记忆为准。只在该 Issue 指定目录与任务 Git 分支写入；不得默认提交到 main、擅自调整全局编号、编辑私人 Google Sheets 或公开原始 PDF。完成一个可审核成果时，附来源核读级别、文件清单、未解决问题，创建指向 main 的 Draft PR。不要自行合并。若发现跨组依赖，在 Issue 提出明确请求。

## 专题任务组合

- **A/B 文献语料**：先核验元数据与官方入口，再萃取作者真正提出的问题、叙事链及审稿质疑。来源核读程度必须清晰。
- **C 语言修辞**：从真实科研材料解剖语义、科学动词、主谓宾、信息结构与句段叙事，说明何时使用、何时不能用。
- **D 理论研究**：识别可检验问题、形式化条件、竞争解释、反例与实验；不得把方法模块名当理论贡献。
- **E 思想方法**：从哲学/文学/数学等原著抽象可执行操作，明确原始语境、相似结构、类比边界和科研写作迁移。
- **F 每日课程**：只生成面向学习者的课程与答案解释，保持微训练、科研迁移、复习和诊断；真实个人作答、评分和进度归 HQ。
- **G 工程**：只按当前 Issue 授权修改自动验证、知识索引和导入方案。
- **Q 挑战式复核**：默认只读 PR，对主张与证据、句法意义、替代解释和可教性提出具体问题。

## 不同协作模式

1. **独立并行**：A/B 各自索引一届 MICCAI；无共享目录写冲突。
2. **流水协作**：A/B → C/D/E → F → HQ；通过固定 source_id、locator、语义动作交接。
3. **双路线竞争**：C/D 对同一段落分别构建语言/科学解释；Q 对比证据，HQ 选用或保留两种。
4. **对抗式审稿**：Q 用竞争解释、反例、可能的实验漏洞检验 D 的科学命题。
5. **回授式教学**：HQ 从私人错误记录提炼匿名“能力缺口”，F/C/D 设计下一份练习，HQ 再测试迁移。
6. **修订/维护**：发现材料过时、引用失效或理论改变，开新的修订 Issue/PR，不悄悄覆盖历史决定。

## 子对话结束一轮时的交接格式

```text
Program / Issue:
Task branch / commit:
Pull Request:
Changed public files:
Original sources actually checked (scope and locators):
Author claims vs reviewer opinions vs our interpretations:
Validated outputs:
Cross-workstream candidates / temporary IDs:
Risks and unresolved scientific questions:
Specific next decision requested from main:
```

## 不要依赖“后台自动协作”

开启了多个 ChatGPT 对话并不意味着这些对话会定时运行、互相通信或持续自动更新。工作只在真正被发起、运行或另有明确任务调度时发生；GitHub 状态才是持久交接面板。把长对话换成新聊天时，用 GitHub handoff 恢复任务，而非试图让新聊天自动记住全部历史。
