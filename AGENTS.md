# Instructions for AI assistants and contributors

This project cultivates English expression, academic narrative, argumentation, and cross-disciplinary research thinking.

## First principles
1. Respect the separation between **source evidence**, **interpretation**, **transfer hypothesis**, and **teaching exercise**.
2. Never invent quotations, page numbers, DOIs, bibliographic details, research results, or cited sources.
3. Scientific framing may selectively emphasize relevant strengths, but must not turn unsupported claims into conclusions.
4. Prefer concrete narrative and reasoning moves over vague writing advice or formulaic templates.
5. Keep learner-facing teaching materials separate from editorial process, metadata, audits, and progress logs.
6. A source is not "read" or "verified" until its content has actually been accessed and checked.

## Content and security
- Public GitHub: author-created notes, licensed text, schemas, exercises, teaching sources, and safe bibliographic metadata.
- Private Drive / Zotero / Catalog: original PDFs, books, attachments, private links/IDs, and permission metadata.
- Never commit access tokens, private Drive URLs/IDs, Zotero SQLite files, personal identifiers or other nonpublic data.
- New media must have provenance and a documented permission basis before public redistribution.

## Stable IDs
- Sources: BOOK-000001, PAPER-000001, ART-000001
- Concepts: CONCEPT-000001
- Thinking moves: MOVE-000001
- Exercises: EX-000001 (micro), RES-000001 (research)
- Never recycle an ID or conflate a source with a summary.

## Working sequence
1. Ground source or problem and define what is known vs unknown.
2. Find conceptual, linguistic and methodological relationships.
3. Develop a concrete artifact: annotation, move card, exercise, lecture, or research-analysis worksheet.
4. Check scientific accuracy, language, citations and link consistency.
5. Commit with a focused message; record completion only after GitHub readback.

## Parallel ChatGPT collaboration — mandatory

Read [coordination protocol](docs/COORDINATION.md), [handoff](docs/HANDOFF_PROTOCOL.md), and the assigned GitHub Issue before writing anything. Child conversations MUST explicitly target their assigned Git branch and edit only its authorized path. Never rely on tools defaulting to the `main` branch.

Only the main coordination chat may update shared schemas/taxonomies, publish global IDs, write the private Drive Master Catalog, or merge PRs. Child chats must provide source-grounded, sanitised candidate records in their PR. Different conversations do not automatically share their latest messages or state.

Existing student lessons, existing MICCAI pilot files and the top-level README are centrally managed. If an edit outside scope seems necessary, request it through the Issue. Before asserting completion, read back the remote branch content and PR status.

## Sustainable programs vs short task branches

Read [the long-term research program](docs/LONG_TERM_PROGRAM.md) and [rolling evaluation](docs/RELEASE_AND_EVALUATION.md). A domain conversation can remain responsible for multiple cycles, but a Git branch is **per small task** and should be replaced after its PR is merged. The seed tasks #2–#6 remain valid first-wave Issues. Their completion must not close the parent Program Epics #7–#11.
