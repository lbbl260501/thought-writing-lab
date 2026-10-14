# 24 source-grounded writing-move cases · Issue #4

**Important:** Each English sentence below is an **original analytical paraphrase** of an identifiable idea in a paper, **not** an original quote, translated quote or verified experimental result. Page locations refer to the accepted-version PDF body pagination. All model evaluations are AUTHOR_CLAIM; SVO/information-flow labels are ANALYST_INTERPRETATION. Source metadata and exact official URLs are in [SOURCE_AUDIT.md](SOURCE_AUDIT.md). Labels refer only to [C's candidate taxonomy](MOVE_TAXONOMY_V0.md).

For each entry: **English** is the independently written sentence; **S/V/O** decomposes scientific actor/action/object; **Given→new** names the knowledge movement; **Use / caution** states the practical rhetorical condition. Cases are not ranked from best to worst: good science writing cannot be deduced from one conference's style.

## A. Epistemic status: uncertainty is not just accuracy

[Source 3770](https://papers.miccai.org/miccai-2025/paper/3770_paper.pdf) — Li et al., *Uncertainty-Supervised Interpretable and Robust Evidential Segmentation*, §1, pp.1–2.

### C04-01 · Credit results before exposing a second requirement
- **Locator:** §1 p.1, introductory paragraph discussing segmentation accuracy and ambiguity.
- **English:** *Deep segmentation networks have raised prediction accuracy, yet uncertain regions may still yield overconfident decisions.*
- **S/V/O:** networks / **have raised** / accuracy; regions / **may yield** / overconfident decisions.
- **Given→new:** known accuracy improvements → reliability failure on ambiguous regions.
- **Moves:** D-02 → D-05; L-04, L-06. **Use / caution:** contrast two legitimate performance dimensions; do not assert that *all* networks fail or that the paper established prevalence.

### C04-02 · Compare competing tools by their operational assumptions
- **Locator:** §1 p.2, opening paragraph comparing Bayesian, ensemble, test-time augmentation and evidential approaches.
- **English:** *Ensembles require several trained predictors, whereas evidential approaches can estimate uncertainty within a single inference pass.*
- **S/V/O:** ensembles / **require** / trained predictors; evidential approaches / **can estimate** / uncertainty.
- **Given→new:** available UQ options → a concrete difference in computational procedure.
- **Moves:** D-03; L-09. **Use / caution:** compares mechanisms, not calibrated performance; a single pass does not itself prove clinical adequacy.

### C04-03 · Name what a measurement leaves unexplained
- **Locator:** §1 p.2, final part of uncertainty-method comparison.
- **English:** *A pixelwise confidence map indicates where the model is uncertain but need not explain the source of that uncertainty.*
- **S/V/O:** confidence map / **indicates** / uncertain locations; map / **need not explain** / uncertainty source.
- **Given→new:** confidence estimation → distinction between reporting and explaining confidence.
- **Moves:** D-06; L-03, L-04. **Use / caution:** useful for a revised evaluation axis; do not equate explanation with demonstrably correct human interpretation.

### C04-04 · Convert a principle into a trainable operation
- **Locator:** §1 p.2, proposal paragraph concerning boundary gradients and noise.
- **English:** *The authors formulate supervision terms that link estimated uncertainty to image gradients and noise perturbations.*
- **S/V/O:** authors / **formulate** / supervision terms; terms / **link** / uncertainty and image properties.
- **Given→new:** desire for interpretable uncertainty → mechanism encoded in the loss.
- **Moves:** D-07 → D-08; L-01, L-03. **Use / caution:** supports a design description; does not establish an independently validated theory of human perception.

## B. Efficiency: turn a cost complaint into selective allocation

[Source 3977](https://papers.miccai.org/miccai-2025/paper/3977_paper.pdf) — Guo et al., *Edge-Aware Token Halting*, §1, pp.1–2.

### C04-05 · Connect architecture to its asymptotic bottleneck
- **Locator:** §1 p.1, first paragraph.
- **English:** *Vision Transformers capture global dependencies, but longer token sequences increase the computational burden of attention.*
- **S/V/O:** transformers / **capture** / dependencies; sequences / **increase** / burden.
- **Given→new:** capability of global representation → scaling constraint.
- **Moves:** D-02 → D-03; L-04, L-09. **Use / caution:** if claiming quadratic growth, specify ordinary full attention and the relevant operation, not all possible transformer variants.

### C04-06 · Reveal a genuine two-sided design conflict
- **Locator:** §1 p.2, discussion of dense prediction and premature token reduction.
- **English:** *Accurate boundaries demand fine spatial detail, while early token removal can discard information needed for dense predictions.*
- **S/V/O:** boundaries / **demand** / detail; token removal / **can discard** / information.
- **Given→new:** computational need to shorten sequences → countervailing segmentation need.
- **Moves:** D-05; L-04, L-06. **Use / caution:** preserve the task-specific condition; do not say pruning is inherently unsuitable for every dense-prediction design.

### C04-07 · Move from observed heterogeneity to selective computation
- **Locator:** §1 p.2, proposal paragraph on easy interiors versus ambiguous edges.
- **English:** *Because interior regions are easier to classify, the proposed encoder reserves deeper processing for less certain boundary tokens.*
- **S/V/O:** encoder / **reserves** / deeper processing; condition / interior–boundary difficulty.
- **Given→new:** unequal token difficulty → allocation rule.
- **Moves:** D-07 → D-08; L-07, L-08. **Use / caution:** this is the authors' design motivation, not an independently verified universal difficulty law.

### C04-08 · Explicitly specify what the decoder receives
- **Locator:** §1 p.2, ending of method overview.
- **English:** *After selective processing, the encoder restores the token layout before passing a dense representation to the segmentation decoder.*
- **S/V/O:** encoder / **restores, passes** / token layout and representation.
- **Given→new:** stopping tokens → retaining compatibility with dense output.
- **Moves:** D-08; L-01, L-03, L-05. **Use / caution:** precise scientific verbs explain a mechanism better than vague *improves feature learning*.

## C. Source-free adaptation: constraints determine what evidence can be used

[Source 0496](https://papers.miccai.org/miccai-2025/paper/0496_paper.pdf) — Ma et al., *Source-Free Domain Adaptation for Cross-Modality Cardiac Image Segmentation*, §1, pp.1–3.

### C04-09 · Make the context-specific problem explicit
- **Locator:** §1 pp.1–2, opening paragraph about annotation scarcity and domain shifts.
- **English:** *Limited labels and scanner-related distribution shifts jointly restrict the transfer of medical segmentation models to new domains.*
- **S/V/O:** label scarcity and shifts / **restrict** / model transfer.
- **Given→new:** successes of representation learning → two practical barriers.
- **Moves:** D-03; L-01, L-03. **Use / caution:** avoid confusing absence of target labels with absence of a target dataset.

### C04-10 · State a negative constraint as a changed information set
- **Locator:** §1 p.2, source-free setting and privacy paragraph.
- **English:** *Source-free adaptation uses a pretrained source model without direct access to the source images during target adaptation.*
- **S/V/O:** adaptation / **uses** / model; adaptation / **excludes** / source images.
- **Given→new:** general domain adaptation → narrower information-access condition.
- **Moves:** D-04; L-06, L-03. **Use / caution:** not all source-free methods are identical; this describes the setting, not the absence of all prior knowledge.

### C04-11 · Specify the mechanism the paper actually proposes
- **Locator:** §1 p.3, class-aware teacher–student contrastive-learning proposal.
- **English:** *The framework derives class-relationship signals from teacher–student predictions and uses them to construct contrastive pairs.*
- **S/V/O:** framework / **derives, uses** / class signals and contrastive pairs.
- **Given→new:** target-only adaptation → an available class-level training signal.
- **Moves:** D-08; L-01, L-03. **Use / caution:** expresses design, not a claim that all other adaptation methods ignore class structure.

### C04-12 · Narrow a sweeping domain-shift claim to a specific task
- **Locator:** §1 p.2, paragraph on the appearance discrepancy between CT and MR.
- **English:** *In the cardiac cross-modality setting considered by the authors, CT–MR appearance differences complicate discriminative feature learning.*
- **S/V/O:** appearance differences / **complicate** / feature learning.
- **Given→new:** domain shift as a category → concrete imaging manifestation.
- **Moves:** D-03, D-05; L-06, L-07. **Use / caution:** avoids universally ranking CT and MRI contrast; preserves the paper's context.

## D. Missing modalities: change the problem definition before introducing the model

[Source 1764](https://papers.miccai.org/miccai-2025/paper/1764_paper.pdf) — Shi et al., *FedAMM*, §1, pp.1–3.

### C04-13 · Replace vague complementarity with identifiable signals
- **Locator:** §1 pp.1–2, first paragraph covering T1/T1c/T2/FLAIR.
- **English:** *Different MRI sequences provide complementary contrasts that help models characterize brain tumors.*
- **S/V/O:** MRI sequences / **provide** / contrasts; contrasts / **help characterize** / tumors.
- **Given→new:** value of multimodal MRI → kind of information being combined.
- **Moves:** D-01; L-03, L-05. **Use / caution:** neither asserts that every sequence is available nor that each is always useful.

### C04-14 · Relate institutional constraints to the learning setup
- **Locator:** §1 p.2, first paragraph about hospitals and direct data pooling.
- **English:** *Patient-data sharing restrictions can prevent hospitals from pooling imaging records for centralized training.*
- **S/V/O:** restrictions / **can prevent** / pooling.
- **Given→new:** data distributed across hospitals → infeasibility of naïve central aggregation.
- **Moves:** D-03; L-01, L-06. **Use / caution:** qualified *can* avoids implying an absolute legal prohibition in every jurisdiction.

### C04-15 · Split a coarse failure category into two research settings
- **Locator:** §1 p.2, definitions of complete and arbitrary missingness.
- **English:** *A client may consistently lack one modality, or the available modality combination may vary from sample to sample within that client.*
- **S/V/O:** client / **may lack** / modality; combination / **may vary** / across samples.
- **Given→new:** generic missing modality → two different units of variability.
- **Moves:** D-04; L-04, L-06. **Use / caution:** the distinction is the conceptual payload; never conflate dataset-level, site-level and scan-level missingness.

### C04-16 · Make the proposed mechanism respond to the newly defined case
- **Locator:** §1 pp.2–3, paragraph motivating prototype distillation and server aggregation.
- **English:** *To handle variable modality availability, the method uses prototype-based knowledge sharing and modality-aware aggregation across clients.*
- **S/V/O:** method / **uses** / knowledge sharing and aggregation.
- **Given→new:** sample-level heterogeneity → two specific balancing operations.
- **Moves:** D-07 → D-08; L-01, L-03. **Use / caution:** frame as authors' proposed response; claims of success require checking results.

## E. Statistical guarantees: writing the condition is part of writing the claim

[Source 3902](https://papers.miccai.org/miccai-2025/paper/3902_paper.pdf) — Mossina & Friedrich, *Conformal Prediction for Image Segmentation Using Morphological Prediction Sets*, §1, pp.1–2.

### C04-17 · Disaggregate sources of uncertainty
- **Locator:** §1 p.1, opening about labeling and data sampling.
- **English:** *Segmentation uncertainty may reflect variation in labels or sampled data, not solely the predictor's internal confidence.*
- **S/V/O:** uncertainty / **may reflect** / labeling or sampling variation.
- **Given→new:** reliability concern → different uncertainty sources.
- **Moves:** D-04; L-06, L-03. **Use / caution:** do not say the particular method models every type of uncertainty equally.

### C04-18 · Anchor guarantees in calibration assumptions
- **Locator:** §1 pp.1–2, explanation of held-out calibration and distribution assumptions.
- **English:** *Under the relevant calibration assumptions, conformal prediction constructs sets intended to achieve a specified coverage level.*
- **S/V/O:** conformal prediction / **constructs** / coverage-oriented sets.
- **Given→new:** desire to quantify errors → a bounded statistical object and assumption.
- **Moves:** D-09; L-02, L-06. **Use / caution:** coverage is not perfect pixelwise certainty; the guarantee is not unconditionally distribution-free.

### C04-19 · Turn interface limitations into the basis of a contribution
- **Locator:** §1 p.2, contribution paragraph about black-box predictors.
- **English:** *The approach operates on predicted binary masks without requiring access to the model's internal logits.*
- **S/V/O:** approach / **operates on** / masks; approach / **does not require** / logits.
- **Given→new:** existing black-box predictor → minimal interface requirements.
- **Moves:** D-08 → D-10; L-03, L-09. **Use / caution:** distinction concerns input access, not any guarantee of deployment readiness.

### C04-20 · Describe how a prediction set is formed
- **Locator:** §1 p.2, morphological-dilation and nonconformity-score paragraph.
- **English:** *Calibrated morphological dilation adds a margin around the predicted mask to form a larger prediction set.*
- **S/V/O:** dilation / **adds** / margin; procedure / **forms** / prediction set.
- **Given→new:** mask-only interface → concrete geometric construction.
- **Moves:** D-08; L-01, L-03. **Use / caution:** do not rewrite this as *the method corrects all false negatives*.

## F. Efficiency + interpretability: persuasive framing still needs evidence

[Source 2131](https://papers.miccai.org/miccai-2025/paper/2131_paper.pdf) — Huang et al., *E-BayesSAM*, §1, pp.2–3.

### C04-21 · Separate different barriers instead of bundling them
- **Locator:** §1 p.2, opening on scale and probabilistic interpretation.
- **English:** *Adapting a large pretrained segmenter for Bayesian uncertainty estimation poses optimization and interpretability challenges.*
- **S/V/O:** Bayesian adaptation / **poses** / two distinct challenges.
- **Given→new:** SAM capability → uncertainty-specific technical obstacles.
- **Moves:** D-03, D-04; L-03. **Use / caution:** a list of barriers becomes substantive only if each leads to a design or experiment.

### C04-22 · Connect an alternative technique to a measurable cost
- **Locator:** §1 p.2, discussion of test-time augmentation.
- **English:** *Repeated inference under test-time augmentation adds computational cost when estimating segmentation uncertainty.*
- **S/V/O:** repeated inference / **adds** / computational cost.
- **Given→new:** available uncertainty mechanism → inference-resource implication.
- **Moves:** D-05; L-01, L-03. **Use / caution:** cost needs measured hardware and settings before asserting practical superiority.

### C04-23 · Show why combining existing components is not trivial
- **Locator:** §1 pp.2–3, argument that naïve Bayesian/KAN adaptation may disrupt the pretrained model.
- **English:** *A direct Bayesian adaptation may alter pretrained behavior, motivating a more restricted token-level formulation.*
- **S/V/O:** adaptation / **may alter** / behavior; risk / **motivates** / formulation.
- **Given→new:** appeal of existing components → integration-specific design constraint.
- **Moves:** D-07; L-06, L-07. **Use / caution:** clearly separate postulated risk from demonstrated failure.

### C04-24 · Precisely name the design without copying the priority claim
- **Locator:** §1 p.3, token reparameterization and self-supervised spline-based interpretation.
- **English:** *The proposed system treats output tokens as probabilistic weights and trains an auxiliary spline-based module to expose token contributions.*
- **S/V/O:** system / **treats, trains** / weights and interpretability module.
- **Given→new:** token-level alternative → concrete probabilistic and interpretability operations.
- **Moves:** D-08 → D-10; L-01, L-03. **Use / caution:** do not inherit the paper's strongest *first-ever* or clinical-deployment language. Official Review #1 challenges priority and baseline coverage; this is a reviewer opinion, not an independently adjudicated novelty finding.

---

## Cross-case findings (interpretive hypotheses, not frequency statistics)

1. **A strong English verb carries a checkable scientific relation:** *restore tokens*, *derive class relationships*, *add calibrated margins* provide more usable content than *enhance performance* alone.
2. **A scientific contradiction is sharper when the two propositions concern one design decision:** high resolution vs token reduction; missing input flexibility vs client-level fixed assumptions.
3. **“What is missing?” often determines a better Introduction than “Which network is better?”** Missing source images, missing modalities, missing guarantees and missing uncertainty explanations are different constraints requiring different logical moves.
4. **A paper's published rhetoric is evidence about what the authors wrote, not a warrant that their phrasing should be imitated.** In particular, novelty and performance superlatives need an independently checked comparison frame.
5. **The smallest useful transfer unit combines proposition, wording and limitation.** Detached phrases such as *to address the aforementioned limitations* convey no portable insight without specifying the limitations and mechanism.

## Quick self-audit

Each of 24 entries has: exact official PDF source → Introduction locator → original paraphrase → S/V/O → given/new progression → local move(s) → context/risk. Six papers × four entries each. No copyrighted paragraph reproduced. Global ID allocation and external validation remain with HQ/Q.
