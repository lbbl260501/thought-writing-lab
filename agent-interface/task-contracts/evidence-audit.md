# Task contract: evidence audit

## Objective
Audit a bounded research or experimental artifact and return reviewable findings without rewriting the canonical source of truth.

## Inputs
- Task ID and authorized path scope
- Canonical record IDs
- Source links and exact locators
- Requested audit dimensions
- Schema version

## Required output
Each finding must include:
- `finding_id` (task-local, not a global stable ID)
- `severity`: blocker / major / minor / observation
- `record_id` and source locator
- `finding_type`: provenance / scientific / numerical / language / pedagogy / privacy / build
- `observed_issue`
- `why_it_matters`
- `recommended_change`
- `evidence_status`: directly_checked / inferred / unresolved
- `reviewer_confidence`
- `requires_human_decision`

## Rules
1. Distinguish source claims, measured outputs, interpretations, hypotheses and teaching examples.
2. Never invent a DOI, page, run ID, value, quote or experimental result.
3. Preserve disagreements when evidence is insufficient to resolve them.
4. Do not write directly to canonical records; submit a proposed patch.
5. State which source sections were actually read.
6. Stop and request clarification when source version, metric definition or data split is ambiguous.
7. A clean schema check does not establish scientific validity.
