# Worked Answers & Reasoning · 10 Scientific English Drills

**Editorial/answer edition.** Read [the independent tasks](EXERCISES_10.md) first. All responses below are **new writing examples** and are not quotations from the papers. Several acceptable answers may exist. The hypothetical tasks E02/E07/E10 do **not** report real experimental outcomes. The examples model evidence-aware reasoning; they do not certify an actual learner's achievement.

## E01 · Replace nominalization with an accountable scientific action

**Possible answer**

> The authors introduce gradient- and noise-based supervision losses to constrain how predicted uncertainty responds to image boundaries and perturbations.

**Dissection:** S = *The authors*; V = *introduce*; O = *supervision losses*. The infinitive *to constrain* specifies the target operation. Information flow moves from the general goal of uncertainty interpretability to a defined mechanism. **Improvement over weak draft:** drops empty *the improvement ... was achieved by the introduction ...*, which presents an outcome as established without supporting evidence. The answer states design, not independent success.

**Also acceptable:** *The proposed losses regularize the relationship between uncertainty estimates, boundary gradients, and noise.* This makes the design component rather than the authors the agent. **Avoid:** *prove that uncertainty is interpretable*.

## E02 · Match the claim to a single reported comparison

**Possible answer**

> On one held-out cohort, adding the boundary-aware loss increased mean Dice by two percentage points. Its robustness to domain shift and its clinical utility were not assessed.

**Dissection:** The first sentence reports the defined outcome and evaluation sample; the second delimits what is *not* known. Neither “universally reliable” nor “ready for clinical use” is supported. *Increased* is acceptable given the hypothetical comparison; *demonstrates superior clinical reliability* is not. If the protocol provides only a nonrandomized comparison, even causal language about the loss may need softening to *was associated with*.

**Transfer principle:** a strong scientific verb is not automatically bad; it becomes problematic when the **object** exceeds the measured variable.

## E03 · Establish the real ViT segmentation trade-off

**Possible answer**

> Vision Transformers can model long-range image dependencies, but their computational cost grows with the number of tokens under standard full attention. Medical image segmentation also needs fine spatial information to delineate boundaries, so removing tokens too early may reduce the detail available for dense predictions.

**Dissection:** S1 acknowledges capability and introduces sequence-length cost; S2 supplies a concrete counterrequirement. The main tension is not a vague *accuracy versus speed* slogan, but the conflict between **token-budget reduction and spatial detail retention**. *May reduce* correctly describes a design risk instead of declaring all token pruning ineffective.

**Reader test:** if input resolution were low and dense boundaries irrelevant, this motivation would be weaker. The conditional dependence is precisely why this contrast is useful.

## E04 · Three-sentence source-free information chain

**Possible answer**

> Medical images are often stored across institutions, where privacy restrictions can limit the sharing of raw data. **These restrictions** motivate source-free domain adaptation, which transfers knowledge through a pretrained source model rather than direct access to source images. **Without the source images**, adaptation must obtain useful training signals from the target data and the available model predictions.

**Dissection:** *raw data sharing* (new in S1) → *these restrictions* (given in S2) → *without the source images* (reused constraint in S3). Each sentence poses the next requirement. The source-free model is not assumed to have zero source knowledge; that would alter the method definition.

**Weak alternative:** *This is a problem. This is addressed with another approach. This can help.* All three instances of *this* lose a precise antecedent.

## E05 · Define complete and arbitrary missingness

**Possible answer**

> Under complete missingness, a client lacks a particular modality throughout its local samples. Under arbitrary missingness, different samples from the same client may contain different subsets of modalities. A method assuming a fixed input pattern for each client may therefore need modification when modality availability changes within that client.

**Dissection:** The comparison axis is the **unit across which availability varies**. Both conditions involve unavailable channels; they differ in whether each client's pattern remains stable across samples. The last sentence spells out the modeling consequence without claiming all existing methods fail.

**Rejected version:** *One case loses data and the other loses more data.* This changes an organizational distinction into an unsupported magnitude distinction.

## E06 · Explain the actual pipeline, not its advertising slogan

**Possible answer**

> The encoder first halts relatively easy background and interior tokens, while retaining edge tokens for deeper processing. It then refines the selected boundary representations and restores the token layout. The reconstructed representation is passed to the decoder to generate dense segmentation predictions.

**Dissection:** Main verbs = **halts → retains → refines → restores → passes → generates**. These are operation-bearing predicates; *advanced, effective, sophisticated* would not tell the reader what happens. The sentence sequence mirrors processing order. Note that *relatively easy* is a design assumption/observation in the source, not an error-rate guarantee.

**Transfer principle:** a method paragraph should often be drawable as a flowchart without first seeing the architecture figure.

## E07 · State conformal coverage carefully

**Possible answer**

> The hypothetical procedure calibrates a morphological margin using held-out data and adds it to each predicted mask to form a prediction set. Under the required exchangeability and calibration conditions, the chosen 90% level concerns marginal coverage of the target mask by that set. It does not say that every predicted pixel is correct, or that each individual case is guaranteed to satisfy the target coverage.

**Dissection:** The statistical **object** is the calibrated prediction set, not a corrected pixel probability. “90%” is a **requested hypothetical setting**, not an empirical result reported in our task. The guarantee is conditional on data assumptions and concerns repeated-sample/marginal behavior, not deterministic correctness for each image.

**Important nuance:** Depending on the construction, readers must verify the definition of set coverage, the distributional assumptions, calibration method and the finite-sample statement in the full paper before making a theorem-level claim. The Intro pages support the broad wording; this exercise is not a proof.

**Rejected version:** *The model achieves 90% pixelwise accuracy with no assumptions.* It changes coverage into accuracy and removes the assumptions.

## E08 · A four-sentence research Introduction that explains the method

**Possible answer (four sentences)**

> Modern deep segmentation networks have improved anatomical delineation across a range of medical imaging tasks. Yet accurate masks do not necessarily imply trustworthy uncertainty estimates, particularly when tissue boundaries are weak or images contain noise. This gap motivates treating boundary appearance and perturbation response as explicit constraints on uncertainty estimation rather than relying on confidence maps alone. Accordingly, the study introduces supervision terms that regularize uncertainty against image gradients and noise, providing a trainable way to encode those constraints.

**Sentence role audit**

| Sentence | Scientific subject → verb → object | Main move | New information |
| --- | --- | --- | --- |
| 1 | networks → have improved → delineation | D-02 | recognized capability |
| 2 | accurate masks → do not imply → trustworthy uncertainty | D-05 | accuracy–reliability gap |
| 3 | gap → motivates → explicit constraints | D-07 | design principle |
| 4 | study → introduces → supervision terms | D-08 | concrete operation |

**Why the order matters:** If S4 appeared immediately after S1, the reader would know *what* the authors do but have little reason to see *why* uncertainty needs the proposed constraint. *Accordingly* now summarizes an inferential bridge, not a decorative transition.

**Caution:** The paragraph reinterprets verified ideas from a particular study as a new teaching model; it makes no new result claim.

## E09 · One thinking move, two audience-appropriate realizations

**Task A — research paragraph (possible answer)**

> Combining imaging data from multiple institutions could broaden the populations represented during model development. However, confidentiality obligations may prevent direct pooling of patient records, creating a practical constraint for segmentation methods that assume centralized access to raw training images.

**Research-specific properties:** restrained *could/may*; objects *populations*, *raw training images*; limitation tied to modeling assumptions. It does not claim a particular privacy-preserving technique is clinically validated.

**Task B — general argumentative essay (possible answer)**

> Hospitals should collaborate when research could benefit patients, but sharing personal medical information without safeguards would place privacy at risk. A reasonable approach is to establish clear consent and security rules so that cooperation does not require unrestricted access to sensitive records.

**General-essay properties:** evaluates a policy choice, gives a balanced judgment and names actionable safeguards. No unnecessary acronyms, SOTA claims or pseudo-experimental evidence.

**What transfers:** **recognize a benefit → reveal a constraint → propose a bounded response**. **What changes:** specificity, technical vocabulary, expected evidence, purpose and reader. Scientific *we propose a model* would be odd in a normative exam essay without an actual study.

## E10 · A hypothesis rather than a prematurely celebrated model

**Possible answer (five sentences)**

> PET and CT provide complementary observations of tumors, combining information about tracer uptake with anatomical context for lesion delineation. A fixed-fusion segmentation system processes these observations through the same pathway across cases, even though their relative usefulness may depend on lesion appearance and surrounding tissue. This raises the question of whether computation should be allocated according to case-specific modality relevance instead of being fixed by network design. We hypothesize that selective routing could improve the balance between segmentation quality and efficiency, but this remains to be tested. A fair evaluation would compare fixed and adaptive routes at matched computational budgets and measure accuracy, missing-modality robustness, and inference cost across different lesion conditions.

**Role and evidential audit**

| S | Narrative action | Epistemic status |
| --- | --- | --- |
| 1 | Establish task and distinct observations | Background task description |
| 2 | Introduce a defined **fixed-fusion scenario** and possible variation | Modeling convention + tentative possibility |
| 3 | Reframe the question from fusion to resource allocation | Research question |
| 4 | Advance an explicitly defeasible hypothesis | **TRANSFER_HYPOTHESIS** |
| 5 | Specify discriminating tests rather than a promised win | Experimental obligation |

**What would weaken the hypothesis:** no gain under matched FLOPs; adverse impact on small lesions; robustness deterioration when PET or CT is missing; routing overhead outweighing saved compute. These are *candidate tests*, not observed outcomes.

**Rejected version:** *Our adaptive framework is the first to prove that all PET/CT cases benefit from asymmetric fusion and enables deployment in every hospital.* This invents priority, observed superiority and clinical evidence at once.

---

## Guidance for F / HQ: how to turn these into instruction

- **Foundation (E01–E03):** Identify the exact agent, main verb and object; contrast overclaim versus appropriately scoped inference.
- **Discourse (E04–E06):** Require explicit antecedents, a two-case definition and operationally ordered mechanism verbs.
- **Evidence (E07–E08):** Track the object of a statistical guarantee; build a paragraph in which each sentence creates the next sentence's need.
- **Transfer (E09–E10):** Apply the *same thinking operation* across general-English and academic contexts while changing register, assumptions and evidence.

### Diagnostic feedback categories for real learner work

1. **SVO absent:** grammatical sentence but no identifiable scientific act.
2. **Claim stronger than evidence:** e.g., clinical safety deduced from overlap scores.
3. **False contrast:** two compared statements have no shared axis.
4. **Broken reference:** unclear *this*, unmotivated topic switch.
5. **Mechanism omitted:** novelty adjectives substitute for what the model changes.
6. **Genre mismatch:** exam paragraph overloaded with domain acronyms, or journal paragraph relying on unsupported personal opinion.

Feedback should name the failing **operation** and ask for a new sentence. Do not penalize one syntactic variant merely for differing from the example answer. F may design lesson-level scaffolding; HQ retains the actual student's drafts and progress in private logs.

## Final self-review checklist

Before accepting an answer, ask four substantive questions: (i) Is its scientific **subject** identifiable? (ii) Does the **verb** bear useful scientific content and the right evidential strength? (iii) Does the **object** offer a concrete point for the next sentence? (iv) Has the sentence completed a **new narrative action**, rather than simply connecting words?
