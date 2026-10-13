# Handoff & review protocol

A child conversation is independent. The main chat should not rely on automatic access to the child's new chat messages.

## Required GitHub handoff
A child updates its Issue and opens a draft/ready Pull Request into `main` with:

- **Issue & branch**: exact Issue number, head branch, source main commit when work began.
- **Modified files**: paths under the assigned writable directory.
- **Output**: paper-count/coverage, analytical cards, exercises or notes; avoid vague completion claims.
- **Evidence**: precise official pages/DOIs/sections actually checked; `metadata_verified` vs `abstract_and_reviews_verified` vs `introduction_read` vs `fulltext_audited`.
- **Uncertainty**: missing PDF, unverified equation, reviewer opinion, suspected duplicates, speculative analogies.
- **Cross-track proposal**: new provisional ID, potential common move, revised schema suggestion or lesson that the main chat may integrate.
- **Review request**: accept, revise, or unblock with another Issue.

## PR acceptance (main chat)
1. Scope: exact branch and changed paths.
2. Security and licensing: no private URLs/IDs, raw copyrighted material, hidden secrets.
3. Evidence: source links accessible and claims distinguish author/reviewer/analyst.
4. Compatibility: required fields, file paths, formats, duplicate checks, noncolliding IDs.
5. Pedagogy: actionable concepts and writing/research exercises, not technical reports masquerading as student lessons.
6. Strategic scientific framing: credible scientific claim, useful evaluation frame, experimental obligations.
7. Merge after review, then update global/private indexes **once**.
8. Post an integration summary and close Issue after checking remote main.

## Integration statuses
- `assigned`: Issue exists and scope agreed.
- `in_progress`: child has begun substantive work.
- `review_ready`: PR contains checked artifacts and an explicit handoff.
- `needs_revision`: main raised change requests.
- `merged`: PR merged and readback confirms main.
- `archived`: intentionally deferred/closed, not a content quality designation.

## Conflict resolution priorities
Evidence accuracy > compatibility with shared schema > scope boundaries > rhetorical elegance.

When two valid analyses disagree, preserve the disagreement with provenance; do not automatically overwrite the less recent or less fashionable interpretation.
