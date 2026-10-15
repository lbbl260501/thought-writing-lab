# A 组 HTML 阅读接口 → 统一交付 Issue #23

用户决定：HTML 是日常阅读、检索、关系探索与练习的主要界面；PDF 是重新选题、教学编排的专题讲义。

## 共同协调入口

本轮后续回读发现其他对话已创建 [HQ 交付 Issue #23](https://github.com/lbbl260501/thought-writing-lab/issues/23)，B 组也已在 HQ #1 登记自己的可视化提案。**A 的本目录作为 #23 的输入，不另建平行总方案。**

- [A 的阅读与专题出版交接](HTML_FIRST_HANDOFF.md)
- [A 的候选阅读单元接口](HTML_READER_CONTRACT.json)
- [B 的交接入口](https://github.com/lbbl260501/thought-writing-lab/blob/agent/miccai26/issue-3/corpora/miccai/2026/visualization/HTML_PDF_CROSSCHAT_HANDOFF.md)
- [原有 A 精读来源](../deep_readings/README.md)

目前共同方向一致；技术栈仍为候选，#23 优先 Quarto，B 另提出文档门户与专用关系组件方案。A 建议先固定源对象、段落定位与关系接口，初版优先连续阅读、段落回链、词句展开和练习；图谱和更复杂组件按明确用途追加。HQ 审定统一模板和发布方式，各组不各自搭建永久独立网站。

## 本轮对话交付

`reading_studio.html`：三篇交互选编（C²MAOT / Locor / PRECISE-AS），另含十三篇完整笔记的在线入口。实现检索跳转、同对象多尺度阅读、跨文对照、原创例句与答案展开、专题选材JSON和私人试写导出。

`reading_studio_source.zip`：可重建的 HTML 模板、JSON 样例数据、Python标准库构建脚本、交接、接口和测试记录。源码包在本次对话附件；本分支目前只保存三份接口/交接文档，没有宣称已经发布网站或完整迁移全部语料。

此样例提供可用组件与阅读方式，**不取代 #23 拟定的跨 A/B/C/D/F 联合专题试点**。也没有生成该试点的专题PDF。F仍须根据学习目标对真实材料作教学编排。

A/B/C/D/E/F的实际进度继续以各自Issue/PR为准。本轮已在HQ #1、B #3、C #4、F #14和A PR #18登记，下一步共同记录于#23。没有自动运行其他对话，没有自行合并main。
