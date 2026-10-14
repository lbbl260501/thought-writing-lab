# Coverage & verification audit · MICCAI 2026 (Issue #3)

Audit date: **2026-10-14**. Current phase: **seed sample / draft for review**, not a complete conference census.

## Counts and sampling frame

| Item | Count / status | Meaning |
| --- | ---: | --- |
| MICCAI 2026 accepted papers, according to the conference's official publication information | 1,167 reported | Denominator is an official conference-level claim, not independently re-counted here. |
| Source metadata records in `sources.csv` | 19 | Nineteen *individual official MICCAI 2026 paper landing pages* checked. |
| Abstract + selected peer-review section checked | 10 | The ten named records in `problem_framing_cases.md`; **not** full-text or full-review audits. |
| Source metadata/landing page + abstract checked; review not encoded | 9 | Intentionally left at `metadata_verified` as a conservative status. |
| Original problem-framing analysis cases | 10 | Intentionally diverse problem mechanisms; NOT a frequency estimate. |
| PDF introductions audited | 0 | No paper should be upgraded to `introduction_read` at present. |
| Entire paper content audited | 0 | No paper should be upgraded to `fulltext_audited`. |
| Official oral/spotlight presentation type verified | 0 | `presentation_type` intentionally blank. |
| Paper-specific DOIs cross-checked | 0 | `doi` intentionally blank until publisher verification. |

**Reproducible selection logic**: `sources.csv` begins with **the first 18 consecutive titles in official paper-list order** (`0001` through `0018`) and adds one targeted theory/argumentation case at official list index `0273` (`Paper0321`). Its resulting title distribution is alphabetically biased. A subsequent selection by scientific problem type and method is needed before comparing frequencies, years, review outcomes, or genres. The 10 casebook examples are a purposive **mechanism-diversity** sample, not a random or representative sample.

## Official source anchors

- Official MICCAI 2026 paper index: <https://papers.miccai.org/miccai-2026/>
- Each index row supplies the exact `0001-Paper2705.html`-style official locator and linked PDF URL in `sources.csv`.
- The publication evidence is the *official paper landing page* containing title, authors, abstract, and accessible reviewer content. The commentary analyses use the abstract and selected reviewer sections only.
- The conference-level accepted-paper denominator was checked against the MICCAI 2026 conference/publication announcement (<https://miccai2026.org/en/>); it must be rechecked at the final-index stage if the archive expands.

## Verification dimensions & deliberately missing information

- **Known from official listing:** author strings and title, paper ID, landing URL, paper PDF link, abstract and selected available review text.
- **Not independently verified:** evaluation metrics reported in each paper beyond authors' assertions; dataset availability and licenses; complete paper methods/results; scientific correctness; reimplementation; full peer-review consensus; clinical deployment.
- **No inferred bibliometrics:** DOI, oral/spotlight status, award, acceptance percentile, citation count, and keyword frequency are not populated by guesses.
- **Distinctions used:** `AUTHOR_CLAIM` (what the authors' abstract asserts) vs `REVIEWER_OPINION` (one reviewer) vs `ANALYST_INTERPRETATION` (our reconstruction) vs `TRANSFER_HYPOTHESIS` (not-yet-run experimental proposal).
- **Copyright boundary:** no raw PDFs, bulk review text or extended source quotes committed; only metadata, links and original synthesis.

## Case-domain coverage

The deliberately distinct focal mechanisms include: incomplete inverse reconstruction (`2705`); guideline-integrated clinical decisions (`2852`); perturbation-derived directional interactions (`6105`); biomechanical/thermal simulator surrogates for planning (`4859`); updateable clinical contour rules (`5049`); dataset/benchmark contribution (`5454`); clinical error detection under distribution shift (`6055`); architecture-imposed vs actually learned modality asymmetry (`1806`); few-shot foundation learning (`4243`); and failure-memory continual learning (`0321`).

## Open issues before scientific/general writing claims

1. Broaden to **at most 100 verified records in this cycle**, with explicit sampling strata (clinical/biological problem, technique, data scale, evaluation problem, journal/meeting distinctions). Do not silently inflate the current sample.
2. Build at least one **introduction-read** case with PDF section or page locator and check whether the reconstructed abstract moves match actual introduction moves.
3. Cross-check paper abstracts' key performance figures against full experimental sections. For reviews, distinguish critical opinions, author replies, and final dispositions rather than treating one review as consensus.
4. Verify specific **presentation types using official schedule**. Do not rank examples as oral/spotlight until then.
5. Add DOI only from trustworthy proceedings/publisher sources; detect duplicates based on official PaperID and normalized title.
6. Ask HQ to assign stable `PAPER-*`, `MOVE-*` or `EX-*` identifiers at integration, not on this child branch.
7. Coordinate cross-year comparison with A through HQ. B does not modify 2025 files, the shared pilot, schemas or the private Master Catalog.

## Review checklist

- [x] Exactly one authorized folder for B.
- [x] Ten traceable, independently selected scientific-framing analyses.
- [x] Per-source `checked_scope` and provisional external identifiers.
- [x] Exposed source-bias and evidence-limits; no presentation-status guesses.
- [ ] Full introduction-level citations for chosen cases.
- [ ] Broader stratified 2026 sample with formally specified denominator/reconciliation.
- [ ] Cross-author/peer-review reconciliation and quality audit by HQ/Q.

**Verdict:** a valid, explicitly partial source-grounded seed dataset, suitable for a Draft PR and review; **not** a finished representative corpus or a validated comparative study.
