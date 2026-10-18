# Knowledge-view pilot: canonical record → agent context + human HTML

## Goal
Prove that one evidence-aware record can produce two genuinely different, useful interfaces without duplicating factual truth.

## Scope
One small experimental report and one teaching item. Do not migrate all A–F materials. Keep raw logs and private learner data out of public GitHub.

## Deliverables
1. Canonical records validated against `knowledge-base/schemas/knowledge-record.schema.json`.
2. Agent context pack: task, relevant records, source locators, allowed tools/paths, required output fields, uncertainty and stop conditions.
3. Human HTML view: narrative explanation, source links, result table, expandable methods/limitations, glossary, and visible status labels.
4. Build/validation script: fail on missing source IDs, unsupported status values, absent units for dimensional metrics, broken local links, and numerical disagreement between canonical records and rendered output.
5. Review report with source, scientific, linguistic, pedagogical, and privacy gates.

## Pipeline
`primary source / run outputs → canonical records → schema + provenance validation → reviewed records → agent context renderer + human HTML renderer`.

Agent-generated edits return as a proposed patch. They must not overwrite canonical records until reviewed. Human narrative may explain evidence but may not silently alter source values.

## Acceptance criteria
- A fresh agent can complete a bounded audit task using only the context pack and referenced sources.
- A reader can understand the report without opening JSON/YAML.
- Every factual statement and metric links to a record or source.
- HTML numeric values match canonical records exactly.
- Teaching examples and hypothetical numbers are visibly labelled.
- Build records the schema version and source record versions.
- No learner scores, private IDs, private URLs, raw copyrighted source text, or credentials enter the public repository.

## Explicit non-goals
- No claims of scientific replication.
- No automated approval of agent claims.
- No assumption that generating a course means a learner completed it.
- No production deployment in this pilot.

## Work split
- Source/knowledge: define record identity, provenance and claim types.
- Agent interface: define context pack and task output contract.
- Human product: define the narrative HTML structure and accessible comparison views.
- Independent review: challenge evidence links, numerical consistency, ambiguity and usability.
- HQ integration: approve schemas and stable IDs only after review.
