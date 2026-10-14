# 10 Scientific English Writing Drills · Issue #4

**Reader edition — do not read the answer key before attempting.** These drills teach **operations** rather than phrase memorization. Allow 25–40 minutes for drills 1–6, 25–45 minutes for drills 7–10; one complete sitting is not required. Prompts use verified *research ideas* from [our six-paper audit](SOURCE_AUDIT.md) or explicitly marked hypothetical scenarios; they do not ask learners to memorize copied source sentences.

**Workflow for every drill:** (i) underline the scientific object; (ii) choose the discourse move; (iii) write your English response; (iv) check whether the verb makes a stronger claim than the evidence supports; (v) only then read [worked explanations](EXERCISE_ANSWERS_10.md).

**Common rubric (5 dimensions, 0–2 each):**
1. **Scientific fidelity** — no fabricated empirical result, changed comparison or misleading inference.
2. **S–V–O** — clear scientific subject, informative action verb and inspectable object.
3. **Information flow** — each sentence changes what the reader knows; given-to-new links are recoverable.
4. **Rhetorical function** — contrast, concession, definition, mechanism or qualification actually advances the task.
5. **Register and economy** — natural English appropriate to the reader; no stock superlatives or padding.

Score is for **self-revision only**, not a claim that any student has already completed this work. Accept multiple scientifically accurate answers.

---

## Micro drills · local keys C04-E01 to E06

### E01 — Replace an empty nominalization with a scientific action
**Target:** L-01 / L-03; D-08. **Source context:** [Li et al., §1 pp.1–2](https://papers.miccai.org/miccai-2025/paper/3770_paper.pdf).

**Facts available to you:** the authors propose gradient-based and noise-based supervision objectives to constrain estimated uncertainty. You have no independently replicated test results.

**Weak draft (created for this exercise):**  
*The improvement in interpretability of the uncertainty estimation was achieved by the introduction of the method and the utilization of several new losses.*

**Task:** In **one English sentence of 17–30 words**, describe what the authors *did*, identifying a scientific subject, action and object. Do not imply externally verified interpretability gains.

**Checkpoint:** Underline the main finite verb. Can you explain what its object is?

### E02 — Repair a claim whose verb exceeds the evidence
**Target:** L-02 / L-06; D-09. **Scenario:** entirely hypothetical, not a reported result.

**Facts available to you:** An imagined segmentation study tested a boundary-aware loss on **one held-out cohort** and found a **two-point improvement in mean Dice**, without evaluating domain shift or clinical endpoints.

**Weak draft:**  
*Our results prove that the new method is universally reliable and ready for clinical practice.*

**Task:** Write **one or two sentences (20–38 words)** reporting the *actual* finding, then specifying at least one unevaluated dimension. Use an appropriate evidential verb.

**Checkpoint:** Does “reliable” still have any support if no calibration or robustness test was performed?

### E03 — Make a concession and a conflict share one comparison axis
**Target:** L-04 / L-09; D-02 → D-05. **Source context:** [Guo et al., §1 pp.1–2](https://papers.miccai.org/miccai-2025/paper/3977_paper.pdf).

**Facts available:** ViT encoders model long-range dependencies; high-resolution segmentation involves numerous tokens; attention cost grows with sequence length under standard full attention. Removing tokens may sacrifice dense spatial detail.

**Task:** Write **two connected sentences (35–52 words)** that first acknowledge capability, then expose a **specific design conflict**. No methods or results yet.

**Checkpoint:** Would the conflict remain if the task did not require dense predictions?

### E04 — Build a given→new chain without repeating the topic
**Target:** L-05 / L-10; D-03 → D-08. **Source context:** [Ma et al., §1 p.2](https://papers.miccai.org/miccai-2025/paper/0496_paper.pdf).

**Facts available:** Some medical data cannot be shared across sites. Source-free adaptation relies on a pretrained source model but cannot inspect raw source images during target adaptation. Target-domain supervision must therefore be derived without direct source images.

**Task:** Write **three sentences (45–65 words)** as a progression, not three disconnected facts. Each new sentence must pick up a precise idea from the preceding one. Do **not** describe a specific algorithm unless the facts supply it.

**Checkpoint:** Replace each *this/these* mentally with its antecedent. Is the reference unambiguous?

### E05 — Define two research settings before saying which is harder
**Target:** L-03 / L-06; D-04. **Source context:** [Shi et al., §1 p.2](https://papers.miccai.org/miccai-2025/paper/1764_paper.pdf).

**Facts available:** In **complete missingness**, a particular client consistently lacks the same modality across samples; in **arbitrary missingness**, the set of observed modalities can vary among samples within that client.

**Task:** In **two or three English sentences (40–60 words)**, precisely distinguish the *unit of variation* and explain why one fixed-input assumption may not generalize. Avoid a sweeping “all earlier methods fail” claim.

**Checkpoint:** Does your definition distinguish clients, samples and modalities rather than lumping them together?

### E06 — Explain mechanism with a sequence of verifiable verbs
**Target:** L-01 / L-03 / L-08; D-07 → D-08. **Source context:** [Guo et al., §1 p.2](https://papers.miccai.org/miccai-2025/paper/3977_paper.pdf).

**Facts available:** HRViT halts relatively easy background/interior tokens, retains and refines edge tokens, and reconstructs token positions before dense decoding.

**Weak draft:**  
*The proposed framework uses an advanced effective strategy to enhance medical feature quality and increase segmentation performance.*

**Task:** Replace it with **two or three sentences (43–65 words)** using at least three informative verbs, organized by processing stage. Do not invent a numeric performance improvement.

**Checkpoint:** Could a reader sketch the sequence of operations based on your description?

---

## Paragraph drills · local keys C04-E07 to E08

### E07 — Limit a statistical guarantee to its object and assumptions
**Target:** L-02 / L-06 / L-09; D-09. **Source context:** [Mossina & Friedrich, §1 pp.1–2](https://papers.miccai.org/miccai-2025/paper/3902_paper.pdf).

**Hypothetical design choice:** a user requests **90% marginal coverage** under the relevant exchangeability/calibration assumptions. A conformal procedure constructs prediction sets by adding calibrated margins to predicted segmentation masks. **You have not measured empirical coverage in this hypothetical scenario.**

**Weak draft:**  
*Our model guarantees that each pixel of every segmentation is 90% correct.*

**Task:** Write **a 3-sentence explanation (55–80 words)**: what is constructed, what nominal coverage applies to, and why the weak draft is scientifically wrong. Distinguish *a set containing the target* from *a perfect segmentation*.

**Checkpoint:** Is the assumed coverage condition stated? Does the guarantee concern each image deterministically?

### E08 — Compose a four-move research-introduction paragraph
**Target:** D-02 → D-05 → D-07 → D-08. **Source context:** [Li et al., §1 pp.1–2](https://papers.miccai.org/miccai-2025/paper/3770_paper.pdf).

**Facts available:** deep segmentation networks can be accurate; ambiguous/noisy boundaries complicate interpretation of prediction confidence; the source paper proposes uncertainty supervision guided by gradients and perturbations. No actual numerical evaluation is supplied here.

**Task:** Write exactly **four English sentences (72–110 words)** carrying, in order: (1) previous capability, (2) a residual problem, (3) a design principle, (4) a proposed trainable operation. Mark the scientific subject and action verb of every sentence **in your private draft only**.

**Checkpoint:** Could you remove the method's name and still understand the scientific reason for choosing that design?

---

## Transfer drills · local keys C04-E09 to E10

### E09 — Transfer reasoning, not surface style, across genres
**Target:** L-04 / L-06; D-03 and audience adjustment. **Context:** original general-purpose exercise.

**Facts available:** Cross-institutional medical AI research can benefit from larger and more varied datasets; patient confidentiality restricts unrestricted data sharing. You have no particular jurisdiction, dataset size or outcome evidence.

**Task A (research):** Write **two sentences (35–55 words)** appropriate to a medical-AI paper, establishing a concrete limitation for model training.  
**Task B (general English argumentative essay):** Write **two sentences (30–50 words)** for a postgraduate/CET/IELTS-style response on whether hospitals should share data more freely; include a balanced position rather than scientific novelty.

**Checkpoint:** Which move transfers across genres? Which specialized register or evidence claim must change?

### E10 — Invent a better problem framing without inventing an experiment
**Target:** D-04 → D-06 → D-07; L-02 / L-05 / L-06. **Context:** **hypothetical transfer**, NOT a claim by the six audited source papers.

**Scenario:** Multimodal PET/CT segmentation may combine metabolic and anatomical observations. A research team is considering whether different cases require different modality contributions and computational resources, but **has not yet demonstrated this**. Its proposed evaluation would compare a fixed-fusion system and a selectively routed system under matched compute, and test missing-modality robustness.

**Task:** Write **five sentences (90–135 words)** forming a prospective Introduction paragraph: task information → current modeling convention → specific unresolved question → testable hypothesis (as hypothesis) → evidence required to judge it. Avoid claiming adaptive fusion is already superior.

**Checkpoint:** Distinguish what is generally known, what this team conjectures, and what measurements could refute it. A good final sentence names an experimental obligation, not merely *we propose a novel framework*.

---

## Post-practice reflection

Without reading the key, answer in one or two lines each: (i) Which sentence has the clearest S/V/O and why? (ii) Which verb was hardest to calibrate? (iii) Did a paragraph need a contrast that could not be expressed by adding *however*? (iv) Which move might transfer from E05 to PET/CT or another research domain? (v) What missing experiment prevented a stronger claim?

**Private work remains private:** do not upload completed answers or assessment data to the public source repository. The [answer file](EXERCISE_ANSWERS_10.md) contains illustrative possibilities, not observed learner performance.
