# Rolling release and evaluation · 持续版本与教学反馈

## Three independent clocks

**Corpus clock:** 新论文、新书籍和理论材料可随时进入暂存与核验。**Research clock:** 新科学问题/思想动作需要比较、论证和可能的实验验证。**Learning clock:** 一份练习或教材需要学员使用、诊断与修订。三者不强制同一天“完成”。

## Versioned products

1. **Corpus Index** — bibliographic and verification status; unique IDs, edition/DOI/official URLs; versioned snapshot and coverage statement.
2. **Scientific Story Casebook** — verified paragraph/argument/story structures, reasoned critique, author vs reviewer positions.
3. **Thinking and Writing Moves** — mechanism-oriented tags with examples, counterexamples and boundaries.
4. **Teaching Library** — micro tasks for CET/postgraduate/IELTS/TOEFL and research-writing workshops, with worked explanations and scoring rubric.
5. **Methods of Inquiry** — problem-formulation and theory-construction exercises, competing explanations, experiment planning and validity checks.
6. **Knowledge Infrastructure** — stable IDs, semantic links, safe sync, validated exports, backup and reproducible build.

## Release gate

For any proposed publishable release, state:
- What new **question or capability** this version actually addresses.
- Which sources, sections and claims were checked; what is still unverified.
- Which changed files and stable IDs were inspected.
- What cross-track relationships were checked (e.g. paper → rhetorical move → exercise).
- What learners or researchers can now **do** that they could not do before.
- Which known weaknesses and validation gaps remain.

A release is not accepted merely because it contains N PDFs, N cards or N pages.

## Recommended reviews

- **Source audit:** verify exact metadata, source locators, licenses and deduplication.
- **Scientific audit:** challenge claims, assumptions, counterexamples, experiments and uncertainty.
- **Linguistic audit:** check semantic precision, subject–action–object, information flow and genre.
- **Pedagogical audit:** test clarity, difficulty, answers, feedback and transfer.
- **Repository audit:** check public/private boundary, IDs, links, PR path scope and backup.

## Version and task naming

- Program Epics: `[PROGRAM] ...` remain open for sustained work.
- Finite task Issues: `[TASK][CORPUS] ...`, `[TASK][LANGUAGE] ...`, etc.
- Short-lived branches: `agent/<workstream>/issue-<number>`; each task branch is retired after PR integration.
- Releases: `corpus-miccai-v0.2`, `writing-moves-v0.1`, `curriculum-alpha-v0.1` (examples, not yet issued).
- Chat titles may retain a long-lived role and sequential session number `P2-English-01`, `P2-English-02`.

## Main-controlled integration

Domain research may outgrow a particular child chat. To hand over, a successor chat reads the program Epic, the latest Issues and PRs, schemas, and case/material indexes; it does not rely on the preceding chat's hidden context. Private Drive/Sheets remain main-controlled until an explicit safe synchronization workflow exists.

## Personal daily learning is not the same as course publication

The separate [daily learning program](../courses/daily/) tests what an individual learner can reproduce from memory, revise and transfer to unseen research/exam prompts. A published lesson is an **instructional artifact**; an actual session requires a learner submission. Record scores and error profiles only in the private Drive journal. A lesson remains unpublished if it only has a topic title or unchecked AI-generated answers.

Suggested checkpoints: Day 0 baseline; Day 7 unseen transfer; Day 14 new paragraph diagnosis; Day 21 introduction comparison; Day 28 unseen integrated task against Day 0. These are planned checkpoints, **not already observed learning outcomes**.
