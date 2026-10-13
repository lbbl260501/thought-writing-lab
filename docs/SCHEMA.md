# Unified knowledge schema

This public specification matches a **private Google Sheets Master Catalog**. The private sheet is authoritative for raw-attachment locations and permissions; this GitHub repo stores only shareable derivative knowledge.

## Entities

| Entity | ID / key | Minimum information |
| --- | --- | --- |
| Source | BOOK-000001 / PAPER-000001 / ART-000001 | Type, title, authors, version/date, source URL, reading state |
| Concept | CONCEPT-000001 | Working definition, disciplinary contexts, source support |
| Thinking move | MOVE-000001 | Core mechanism, prerequisites, boundary, application |
| Exercise | EX-000001 / RES-000001 | Scale, target move, prompt, evaluation, transfer |
| Link | source_node_id + relation + target_node_id | Typed relationship with evidence/rationale |

## Private Master Catalog tabs
- `START_HERE`: intended use and privacy boundary
- `Sources`: source_id, type, title, authors, year, language, doi, isbn, source_url, zotero_key, drive_file_id, reading_status, rights_access, topics, note_path, date_added
- `Concepts`: concept_id, name_zh, name_en, working_definition, domain, supporting_sources, related_moves, open_questions
- `Thinking_Moves`: move_id, name_zh, name_en, mechanism, origin_sources, writing_applications, research_applications, exercise_ids
- `Exercises`: exercise_id, scale, context, target_move, task_path, output_requirements, evaluation_dimensions, status
- `Links`: source_node_id, relation, target_node_id, evidence_or_rationale, source_reference
- `Folders`: private storage locations

## Relationships
Recommended predicates: `defines`, `supports`, `contrasts_with`, `inspires`, `applies_to`, `prerequisite_for`, `tested_by`, `developed_into`.

**Important:** A conceptual analogy is not empirical evidence. In link notes, specify whether the relationship is source-grounded, an analytical interpretation, or a tentative transfer hypothesis.

## Ingestion protocol
1. Check duplicates by DOI, ISBN, title+edition and source URL.
2. Assign an unused ID in the private catalog.
3. Record bibliographic facts and provenance. Unverified fields remain blank.
4. Keep attachments in private Drive and references in Zotero.
5. Create or update a public Markdown note only when its contents are safe to publish.
6. Keep link IDs stable through file moves, renamed titles and storage migrations.

## Export
Generate public lists only through deliberate redaction. Do not export `drive_file_id`, private links, permission data or local file paths to GitHub.
