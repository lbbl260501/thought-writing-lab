# Coverage & verification audit · MICCAI 2026 / Issue #3

Updated: **2026-10-14, batch 02**. Stage: expanded purposive sample with PDF introduction close readings; still a Draft PR, not a complete conference census.

## Current canonical counts

| Item | Count | Interpretation |
|---|---:|---|
| Unique source records in `sources.csv` | 40 | 19 retained seed records plus 21 new official-paper records |
| Highest recorded status: `metadata_verified` | 29 | Metadata and the specifically visible text checked; not necessarily a complete abstract audit |
| Highest recorded status: `abstract_and_reviews_verified` | 6 | Abstract and selected review passages; not complete review consensus |
| Highest recorded status: `introduction_read` | 5 | Entire Introduction section checked in the official PDF, plus individually specified evidence spot-checks |
| `fulltext_audited` | 0 | No complete methods/results/citations/implementation audit is claimed |
| Initial abstract-level case notes | 10 | Historical first-batch analytical snapshot in `problem_framing_cases.md` |
| New introduction-level close readings | 5 | 5533, 4859, 1806, 6055, 5049 |
| Distinct papers covered by either analytical artifact | 11 | Four deep readings upgrade earlier cases; FRODO/5533 is one additional analyzed paper; do not report 15 unique analyzed papers |
| Verified DOI fields | 0 | Blank rather than guessed |
| Verified presentation-type fields | 0 | No Oral/Spotlight ranking or weighting has been performed |

The current source inventory is `sources.csv`; the prior casebook remains an abstract-level snapshot. Its old reading-limit statements are not a report of the latest inventory. Current reading depth is established by the CSV and `introductions/evidence.jsonl`.

## What changed in this pass

- Added 21 official records across computational allocation, uncertainty/calibration, incomplete multimodal information, registration/planning, representation evaluation and reasoning-oriented clinical tasks.
- Read five complete PDF introductions and inspected their actual page boundaries. MA-MoE's Introduction extends through the contribution paragraph on page 4; the large Figure 1 on page 3 is not the end of the Introduction.
- Added a Chinese original analytical casebook with paragraph-function maps, problem–method bridges, original English contrast examples and claim-to-evidence checks.
- Revisited selected methods/results instead of treating generic critique as a source fact. Failure-detection validation thresholds and confidence intervals are already present. OncoAgent already includes a GTV-prior comparator and blinded clinician ratings.
- Preserved the distinction between actual paper evidence and proposed experiments. None of the proposals was executed by this project.

## Source anchors and version

Official archive: https://papers.miccai.org/miccai-2026/

Per-paper exact official URLs, author strings and linked PDF locators are preserved in the CSV. The deep-reading manifest records the official accepted-version PDF, one-based PDF pages, checked sections and unverified areas. Page images were inspected where figures/tables or paragraph boundaries mattered. Source PDFs and screenshots are not redistributed in this repository.

This pass did not independently reconcile the full archive against a final proceedings census. The conference-wide denominator shown in the previous coverage draft is therefore not carried forward as a verified denominator, and no percentage-of-conference coverage is reported.

## Sampling design and limitations

Batch 01 retains the first 18 consecutive official listing entries (`0001`–`0018`) plus targeted entry `0273`. Batch 02 deliberately broadens the comparison set using the 21 fixed IDs and group rationale in `BATCH02_SELECTION.md`.

This is **purposive selection**, not probability sampling or a balanced stratified sample. The fixed manifest makes the selection reproducible, but does not justify prevalence estimates, year-to-year trend claims, or claims about conference-wide writing norms. Biomedical multimodality, trustworthiness, geometry and planning remain over-represented relative to an unmeasured conference population.

## Data quality exceptions

- Paper2389 and Paper4147 have visibly truncated landing-page abstracts; their `checked_scope` explicitly records this. Metadata verification does not certify complete abstract text.
- Paper4499 has a malformed volume string in the official BibTeX. That field is not imported.
- Paper authors come from the paper-author section/BibTeX rather than the webpage byline.
- Leading-zero external IDs are preserved as strings.
- Paper4853 and Paper4859 have related authors/topics but distinct official IDs/titles; they are not treated as duplicate sources.
- A linked PDF URL is not, by itself, evidence that the entire PDF has been read. This distinction applies particularly to the 21 new intake records.

## Interpretation controls

`AUTHOR_CLAIM`: what the source reports, not independently reproduced results.

`REVIEWER_OPINION`: a specific reviewer's judgment, not consensus or verified scientific fact. The expanded notes do not claim complete rebuttal/meta-review reconciliation.

`ANALYST_INTERPRETATION`: our reconstruction of paragraph function, information flow and problem formulation. Function-unit labels do not mechanically count physical paragraphs.

`TRANSFER_HYPOTHESIS`: a proposed research comparison or experiment. Original English examples are writing demonstrations, not source quotations or empirical results.

Important distinctions discovered in the deeper pass:

1. QSM-primary/FLAIR-conditioning and shared-versus-specific experts are different modeling relationships.
2. Fast forward prediction, expanded candidate search and correct final decisions require different evidence.
3. Clinically unacceptable segmentation is not synonymous with an out-of-distribution input.
4. No target-task training annotations is not the same as no labeled inputs or pretrained components anywhere in the workflow.
5. Tool-call transfer across guidelines is not automatically geometric segmentation transfer or clinical benefit.

## Review and remaining work

The authoring pass has delivered the expanded index, original deep readings and evidence locators. **Independent HQ/Q review remains outstanding.** No merge, stable-ID allocation, private Master Catalog update, source-code execution or learner evaluation has occurred.

Next bounded research candidates are paired Introduction comparisons: FRODO vs MA-MoE for modality roles; Paper4859 vs Paper4853 for forward search vs inverse inference; Paper6055 vs Paper1236/4499 for failure, calibration and uncertainty. The latter newly ingested papers must actually be read before being promoted.

Further corpus expansion remains within this task's up-to-100 scope, but count growth should not substitute for evidence depth. Oral status, DOI validation, complete review reconciliation and cross-year representativeness still require separate checks.
