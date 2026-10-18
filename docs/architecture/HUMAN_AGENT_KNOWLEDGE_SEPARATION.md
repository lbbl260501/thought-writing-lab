# Architecture Proposal · Human/Agent Separation

Status: proposal, not yet adopted. Date: 2026-10-18.

## Decision

Separate **knowledge**, **agent interface**, and **human presentation**. Do not maintain two independent factual knowledge bases. Keep one canonical, provenance-aware source of truth and generate audience-specific views from it.

## Why

Agentic applications have distinct UI, orchestration/runtime, tools, memory and model components; they should not be collapsed into one prompt or one document (Google Cloud agentic architecture guidance: https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components). Open Knowledge Format demonstrates a practical human- and agent-readable pattern using Markdown plus YAML metadata, with provenance, trust, freshness, lifecycle and attestation represented explicitly (https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md). OpenAI's harness engineering guidance similarly treats AGENTS.md as a short map to structured source-of-truth documentation, not as the encyclopedia (https://openai.com/index/harness-engineering/).

## Three-plane architecture

### 1. Knowledge plane — canonical facts and evidence

Store source records, claims, interpretations, evidence locators, method records, experiment configurations/results, uncertainty and relationships. Use stable IDs, explicit units, version, status and provenance. A claim must distinguish author claim, independently checked fact, analyst interpretation, hypothesis and teaching example. This plane is not written in polished report prose and is not a raw vector-store dump.

Suggested objects:
- `source_record`: title, authors, version, official URL/DOI, license, checked scope, exact locator.
- `claim_record`: claim text, claim type, source IDs, locator, confidence/status, counterevidence, last verified.
- `experiment_record`: hypothesis, dataset/split, intervention, controls, metrics/units, run/config/code IDs, results, limitations.
- `language_move`: narrative function, grammatical realization, semantic constraints, examples, counterexamples, source locators.

### 2. Agent plane — task-oriented machine interface

Provide small task-specific context packs and schemas, not the entire human-facing report. Include `AGENTS.md` as a short entry point, task contracts, JSON/YAML or typed Markdown records, retrieval tools, validation checks and explicit write permissions. Agents should receive only relevant context and should return structured outputs with source IDs, exact locators, uncertainty, proposed changes and validation status. Agent output remains a candidate until reviewed.

A task contract should define: objective, allowed paths/tools, input schema, output schema, evidence threshold, stop conditions, reviewer and acceptance tests.

### 3. Human plane — teaching and decision products

Render separate products from the canonical records:
- Researcher/editor view: evidence ledger, disputed claims, review status, provenance and unresolved questions.
- Learner view: coherent explanation, worked examples, exercises, answer explanations and transfer tasks. Hide repository metadata and internal workflow fields.
- Report view: scientific narrative and results with traceable references; no raw schema dumps unless useful to an appendix.
- Visual HTML: navigation, filters, expandable evidence, side-by-side comparisons and visible source links.
- PDF/LaTeX: stable, linear, printable teaching/report version.

Human-facing prose is a designed projection, not the canonical storage format. Agent-facing records are not a substitute for readable explanation.

## The critical separation for experimental reports

Separate four objects that are often mixed in a single AI-generated report:
1. **Experiment specification** — hypothesis, variables, controls, dataset, split, metrics and protocol.
2. **Execution evidence** — logs, seeds, software/config versions, raw outputs and computed metrics.
3. **Interpretation** — what the result supports, alternative explanations, uncertainty and limitations.
4. **Narrative report** — a human-readable argument that references the first three.

Never let polished prose overwrite raw evidence. Numeric tables should be generated from structured results; narrative claims should link to result IDs. If a metric or run changes, rebuild the report rather than manually editing duplicated numbers.

## Build flow

`source/evidence → normalized records → validation and review → canonical knowledge store → (A) agent context/API and (B) human HTML/PDF/report renderers`.

Agent output flows back as a proposed patch with provenance, not as a direct overwrite of canonical records. Human reviewers approve, then rebuild both projections.

## Repository layout proposal

```text
knowledge-base/
  sources/
  claims/
  experiments/
  methods/
  language-moves/
  schemas/
agent-interface/
  AGENTS.md
  task-contracts/
  context-packs/
  tools-and-validation/
human-products/
  research-reports/
  lessons/
  html/
  pdf/
```

This is a conceptual layout; it should be reconciled with the existing repository before files are moved. Avoid duplicating current records solely to fit this tree.

## Validation gates

- Provenance: every nontrivial factual claim resolves to a source or experiment record.
- Semantic: units, variables, scope and conditions survive conversion between formats.
- Reproducibility: tables and reported metrics regenerate from structured outputs.
- Agent usability: a fresh agent can complete a bounded task using only the declared task pack and tools.
- Human usability: a learner/researcher can understand the product without reading JSON/YAML or internal logs.
- Consistency: generated HTML/PDF values match canonical records; no conflicting duplicate facts.
- Security/licensing: private records and raw copyrighted material do not leak into public products.

## Recommended implementation sequence

1. Pilot one experimental report and one lesson; do not migrate all content at once.
2. Define a minimal schema for source, claim, experiment and language move; include provenance and status.
3. Store one small canonical sample and generate an agent context pack plus human HTML view from it.
4. Add automated consistency checks for IDs, locators, units, claim status and duplicated numeric values.
5. Ask an independent reviewer to test both views; only then expand to all A–F workstreams.

## Open decisions

- Whether canonical records live in Markdown/YAML, JSON, or a hybrid. Recommendation: Markdown with YAML frontmatter for durable knowledge notes; JSON for validated records, API payloads and generated indexes.
- Whether the human HTML is generated or hand-authored. Recommendation: generated from canonical records, with a separate editorial layer for narrative and pedagogy.
- Whether agents may write to canonical storage. Recommendation: no direct writes; agents submit proposed patches, validators run, and HQ/reviewer approves.

## Scope limitation

This is an architecture proposal informed by public guidance, not a claim that a complete multi-agent runtime has been deployed. The current connected tool environment exposes repository operations but no explicit subagent-spawn operation; actual parallel child-agent execution must not be claimed unless the runtime provides that capability. Independent workstreams can still be prepared and audited, but role simulation is not true agent parallelism.
