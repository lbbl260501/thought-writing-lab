# B → HQ 可视化迁移交接｜HTML-first / PDF-as-curated-lecture (proposal)

**日期：2026-10-15** · B Issue [#3](https://github.com/lbbl260501/thought-writing-lab/issues/3) · Program #7 · 不修改共享 schema / 主分支 / 私人索引。

## 0. 要交给 HQ 的决策

用户明确提出：**HTML 是项目的主要“可视化”媒介；PDF 用于不定期、经过教学编排的专题讲义总结。**

B 组建议定义项目级原则：
1. GitHub 内经过审核的结构化知识/Markdown 是内容来源；HTML 是**可交互的多视图投影**而不是独立真相来源。
2. **可视化有问题驱动的语义**：论文论证链、词句关联图、证据对照、研究流程/空间关系、复习知识结构；不为了图而图，也不默认 3D/游戏风格。
3. **PDF 是专题快照**，需要重新筛选内容、安排教学顺序、解释/练习/答案与正式来源，不把网页一键打印充作“教材”。
4. 所有用户作答、私人笔记、原始/受版权限制的文献保留在私域；GitHub Pages 若启用，仅部署可公开资料和原创可分享材料。
5. 发布、稳定 ID、公共路由、共享类型/关系字典、GitHub Pages 权限及 PDF Release 全由 HQ 审核。当前子组不自动改共享目录。

此文件只描述 B 的输入接口与跨组建议，不代表其他组已采纳。

## 1. 从 GitHub 已核对的各组进度（不能推断其他对话消息自动同步）

| 研究组 | 已有可用输出 | HTML 首选视图 | PDF 适合的专题 |
|---|---|---|---|
| A / PR #18 | MICCAI 2025 13 篇分章节精读 | 论文章节/叙事动作路线、证据—贡献对照、跨论文比较 | 代表性引言及 Discussion 精读专题 |
| B / PR #19 | 2026 40 条来源、5 篇引言、2 篇全篇语言分析；B04/05 两册应用词句库 | 论证结构图、词句关联、真实来源定位、表达意图反查 | 科研动词/搭配/问题构建、PET/CT、规划 |
| C / PR #21 | 8 大类、24 子类叙事功能候选；18 篇研究源，准确区分原句和教学改写 | 句段功能高亮、主客体结构、功能类别对照、语境检索 | 学术句子/段落方法论与迁移 |
| D / PR #20 | 科学问题、竞争解释、证据/实验设计；16 来源与精读札记 | claim–ground–warrant 链、假设—替代解释—判别实验流程 | 理论构建、问题定义与科学论证 |
| E / Issue #6 | 长期哲学/文学/认知任务已定义；暂无已核对可集成 PR | 原著→思想机制→适用条件→科研迁移的关系图（有材料后上线） | 哲学/认知机制的科学迁移专题 |
| F / PR #22 | D08–D14 学习单元、独立讲解答案 | 学习目标→先修→训练→反馈导航（不能公开私人得分） | 某一能力链的独立练习册 |
| HQ / #1 | 共享 taxonomy、稳定 ID、仓库/隐私边界、审核与合并 | 统一门户、跨组聚合与权限审查 | 确定正式版本和发布口径 |

上表是发布输入提议，不擅自导入未经 HQ/Q 审查的子组候选类型。

## 2. 首批产品视图，而不是先做巨型知识图谱

**V1 论文阅读/论证轨道**：全文分节、段落/句子精读单元、科学问题→方法→实验→结论；点选后展示来源 URL、版本、页码及真实性等级。

**V2 词句关系与表达反查**：以“我想表达什么”为入口，进入词义对比、主谓宾科学动作、搭配槽位、原始短引或原创示范、段落位置；显示关联边类型；以 B04 36 卡+B05 48 卡为首个验证集，但注意**完整 ZIP 尚未全部入 GitHub**。

**V3 解释—证据—反例图**：结论、支持依据、适用条件、替代解释和待验证实验并列，明确标注 `AUTHOR_CLAIM`/`REVIEWER_OPINION`/`ANALYST_INTERPRETATION`/`TRANSFER_HYPOTHESIS`，防止不同可信等级的边被画成同类事实。

**V4 学习目标地图**：课程先修关系、具体课次、可选练习、独立答案入口、专题 PDF；真实学习记录仍在私人日志。

不要把图谱当唯一界面：论文原文精读更适合**有连续阅读主体的双栏文本/结构**；大图只用于发现关系。建议默认从检索与正文进入，图谱是切换视图。

## 3. B 愿意提供的最小数据契约（候选，不修改全局 schema）

```json
{
  "local_key": "miccai:2026:5533",
  "kind": "paper",
  "display_title": "3D Classification of Paramagnetic Rim Lesions in Multiple Sclerosis via Asymmetric QSM–FLAIR Modeling",
  "source": {
    "uri": "https://papers.miccai.org/miccai-2026/0002-Paper5533.html",
    "version": "MICCAI 2026 open accepted version",
    "locator": "PDF Section 1, pages 1–3"
  },
  "checked_scope": "introduction_read",
  "claim_origin": "AUTHOR_CLAIM",
  "review_status": "working_annotated_not_Q_audited",
  "relations": [
    {
      "target": "draft:B:modality-role-versus-conditioning",
      "type": "ANALYST_ILLUSTRATION",
      "rationale": "Observation roles motivate directional conditioning; this is analysis, not a causal finding."
    }
  ]
}
```

需要区分**对象类型**（论文、章节、词、搭配、句式、科学问题、假设、实验、题目、课程、PDF 专题）与**关系类型**（原文证明/作者主张/研究者解释、近义辨析/部分-整体/先修/应用例/互为对照）。每条关系要能回到实际来源或注明是编辑性/教学性关系。

## 4. 建议技术层次（官方技术文档已调研；仍待 HQ 选型）

- **内容源层**：保留现有 Markdown、CSV、JSON/JSONL；继续把版权受限 PDF 放私人 Zotero/Drive 而非公开 repo。
- **阅读门户层**：Astro Starlight（Markdown/MDX、搜索、双语与可复用自定义组件）。候选而非已部署事实。
- **图与分析组件**：Cytoscape.js（论文/词句关系）；Mermaid（小型稳定论证流程）；Observable Plot（来源覆盖/实验比较）；React Flow 仅在未来需要节点拖动编辑时引入。
- **专题出版层**：Quarto Books 适合章节跨格式输出；复杂中文数学/高质量印刷可以使用独立 LaTeX/Typst 模板；HTML→PDF 一键打印不等于教学编辑。
- **分发**：HQ 决定 GitHub Pages 的构建与权限；静态页面只发布公开内容。请核验真实 Pages 配置，不要宣称已经上线。

参考官方文档：
- https://starlight.astro.build/
- https://js.cytoscape.org/
- https://reactflow.dev/
- https://observablehq.com/plot/
- https://quarto.org/docs/books/
- https://pagedjs.org/

## 5. 职责与迁移过程

1. **HQ**：决定公共数据契约/统一 ID/正式 UI 路由，建立单独、明确可写目录的短期 GitHub Issue 和分支；制定来源/隐私/版权/教学四重发布门。
2. **A、B**：交付带 `paper_id / official_url / verified_scope / version / paragraph_role / evidence_location` 的可视化投影候选记录；B 首批连接 Paper5533、Paper4859 与词句库两册。
3. **C**：将 `language_move` 候选代码映射到统一分类；原文、分析、原创例句分别上色/标记，不将 paraphrase 当成原文引文。
4. **D**：将科学推理图类型化，保证支持证据、假设、竞争解释与待做实验在界面上清楚分离。
5. **E**：保留来源传统/版本/段落和跨领域类比的适用边界；尚无核验产物时不预生成确定论断。
6. **F**：以真实独立作答为中心设计学习路线/练习/答案；专项 PDF 经过主题选择、教学编排与发布审校；个人练习/得分不进入公共网页。
7. **B 的边界**：只提交本文件/自己的样例视图与可溯源记录，不能改别组文件、main、工作流或正式网址。

## 6. 提请 HQ 的验收里程碑

- **M0 决策**：批准 HTML = 可视化投影、PDF = 专题讲义、结构化 Git 内容为来源；批准命名、授权目录、构建/审核工作流。
- **M1 阅读能力**：上线只读跨组门户样本：至少 1 张论文结构图 + 1 个词句关联页 + 1 个证据链视图，所有节点可追溯、有来源等级。
- **M2 关联能力**：同一个 source key 在论文、词句、问题与练习间可跳转；禁止悬空引用和“来源级别提升”。
- **M3 出版能力**：选定单一专题，从共同内容编排 PDF + 独立答案 + 版本清单；检查来源、排版和练习可作答。
- **M4 质量反馈**：由 C/D/Q 对准确性抽样，F/HQ 对学习成效评价；公开内容与私人反馈彻底隔离。

**注意**：现在这份文档是 B 的跨对话协作建议，尚不能代表 HQ/A/C/D/E/F 的正式接受。