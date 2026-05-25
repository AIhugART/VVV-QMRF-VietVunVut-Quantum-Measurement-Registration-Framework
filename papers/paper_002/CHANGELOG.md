# CHANGELOG — "Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?"

**Paper ID:** paper_002 | **Target:** arXiv quant-ph → Phys. Rev. A
**Author:** VietVunVut (Viet — Nguyen Xuan)

---

## v64 (2026-05-25) — 2/4-issue RCA (threshold 4.5/5): Survey wording refined (observation, not general claim); Phase 1 framed as screening stage

**Scoring summary (4 issues):** 2 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | 2 thí nghiệm — quá ít để kết luận pattern tổng quát | 4.5/5 | **Implemented** — "both are equatorial" → "Both happen to be equatorial — an observation about the existing literature, not a claim that all possible EWF implementations must be equatorial." Also: "we include all published instances" → "the table enumerates all published instances." |
| 2 | Overlap-only tự định nghĩa — chưa có lý thuyết dự đoán | 3.5/5 | Rejected — already stated explicitly: "phenomenological null test" (v53 Abstract), "no existing theory predicts this specific form" (v54 §2.3), "plausibility argument, not a derivation from a complete theory" (v55 §2.3), "illustrative benchmark" (v54 §5.3) |
| 3 | β ~ 0.07 không có lý do vật lý — O(10⁻²) cần justification | 3.5/5 | Rejected — v55 §5.3 "β in context" already compares to SME (<10⁻²³), CSL (~10⁻¹⁶), weak measurement (~10⁻²), with explicit motivation: "postselection-conditioned weak values manifest at the same order, and any overlap-dependent registration-layer structure would naturally appear at the precision where measurement-context effects become distinguishable from Poisson noise" |
| 4 | Phase 1 loophole-open — null result dễ bị phản bác | 4.5/5 | **Implemented** — Phase 1 reframed as "screening test" (not just "null test"). Added: "Phase 1 is a screening stage: a positive signal would motivate immediate Phase 2; a null result is suggestive but remains open to the detection-loophole objection." Also: "self-consistent exclusion" → "self-consistent but not loophole-free exclusion." |

### Implemented changes (v64)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **Survey wording refined:** "Both are equatorial" → "Both happen to be equatorial — an observation about the existing literature, not a claim that all possible EWF implementations must be equatorial." + "we include all published instances meeting our search criteria rather than a selective sample" → "the table enumerates all published instances meeting our search criteria." | 4.5/5 | v63 contextualized the 2-row table by explaining WHY only 2 exist. But "both are equatorial" still carried an implicit "therefore all EWF experiments are equatorial." The refined wording explicitly decouples the observation (these two happen to be equatorial) from the generalization (therefore all EWF experiments are equatorial). The word "happen" does the work — it signals contingency, not necessity. |
| 4 | §7 | **Phase 1 as screening stage:** "loophole-open null test" → "loophole-open screening test." Added: "Phase 1 is a screening stage: a positive signal would motivate immediate Phase 2; a null result is suggestive but remains open to the detection-loophole objection." Changed: "a self-consistent exclusion independent of absolute detector efficiency" → "a self-consistent but not loophole-free exclusion." | 4.5/5 | v62 added the two-phase framing; v63 mentioned it in the Abstract. But Phase 1 was still described as a "null test" — language that implies a definitive result. "Screening test" accurately conveys the role: Phase 1 tells you whether to proceed to Phase 2, not whether the hypothesis is true. The "suggestive but not definitive" language sets honest expectations. |

### Regression
Δ: Minor wording refinements only — no structural or claim changes.

---

## v63 (2026-05-25) — 5/5-issue RCA (threshold 4.5/5): Survey table contextualized + explicit caveat; Lemma 1 de-circularized; explicit FOM formula; two-phase in Abstract

**Scoring summary (5 issues):** 5 implemented (≥4.5/5), 0 rejected. Second consecutive all-accept round.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Survey table chỉ có 2 dòng — trông mỏng, reader sẽ hỏi "chỉ 2 thí nghiệm?" | 4.5/5 | **Implemented** — Table lead-in rewritten: "Only two published optical EWF experiments exist within our systematic search scope...The small number reflects the reality that optical EWF implementations remain rare; we include all published instances meeting our search criteria rather than a selective sample." |
| 2 | Claim dựa trên ~47 papers — reviewer có thể phản bác bằng unpublished work | 4.5/5 | **Implemented** — Explicit caveat added: "We cannot rule out unpublished results, conference proceedings, or implementations outside our database scope that may have varied θ." |
| 3 | Lemma 1 proof hơi circular — "passive relabeling predicts δ⟨AB⟩=0" là định nghĩa, không phải proof | 4.7/5 | **Implemented** — Proof restructured with explicit distinction: (i) passive relabeling (change of description, δ⟨AB⟩=0 identically) vs (ii) active physical rotation (change of measurement axis, alters \|⟨b\|d⟩\|²). Key insight added: "The cos θ term...is a function of the physical angle θ, not of the basis labels; it cannot be removed by any relabeling U because relabeling does not change θ." |
| 5 | FOM formula không hiển thị tường minh trong §5.3 — reader phải lần ngược §4.1 | 4.5/5 | **Implemented** — Explicit FOM formula added to §5.3: FOM(θ, β, N) = min(n_σ_LF(θ, N), n_σ_signal(θ, β, N)) with n_σ_LF and n_σ_signal defined in terms of Gen LF 1 and δ⟨AB⟩ significances |
| 6 | Two-phase program introduced muộn (§7) — reader không biết scope đến cuối paper | 4.5/5 | **Implemented** — Abstract updated: "under fair-sampling, as the first phase of a two-phase program (loophole-open null test at η ≈ 0.87, followed by loophole-closed confirmation via SNSPD upgrade to η ≥ 0.91)" |

### Implemented changes (v63)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.5 | **Survey table contextualized (+4 lines):** Table lead-in changed from generic "lists all published optical EWF experiments examined" to explicit: "Only two published optical EWF experiments exist within our systematic search scope...The small number reflects the reality that optical EWF implementations remain rare; we include all published instances meeting our search criteria rather than a selective sample." | 4.5/5 | A 2-row table invites the question "is that all?" The revised lead-in preempts this: yes, that IS all — not because we selected only two, but because only two exist within scope. Reframes "thin table" as "complete enumeration." |
| 2 | §3.5 | **Explicit survey caveat (+2 lines):** "We cannot rule out unpublished results, conference proceedings, or implementations outside our database scope that may have varied θ." | 4.5/5 | The survey methodology is documented in S1, but the main text should acknowledge the inherent limitation: a literature search cannot prove non-existence, only non-discovery within scope. This one sentence prevents a reviewer from countering with a single obscure conference paper. |
| 3 | §3.2 | **Lemma 1 proof de-circularized (+6 lines):** Old proof stated "passive relabeling...basis redefinition relabels outcomes without altering probabilities" — which is the DEFINITION of passive relabeling, not a proof about cos θ. New proof explicitly distinguishes (i) passive relabeling (change of description → δ⟨AB⟩=0) from (ii) active physical rotation (change of measurement axis → alters overlap). Key addition: "The cos θ term...is a function of the physical angle θ, not of the basis labels; it cannot be removed by any relabeling U because relabeling does not change θ." | 4.7/5 | The original proof was technically correct but structurally weak — it defined passive relabeling as "leaves probabilities invariant," then concluded that it leaves probabilities invariant. The restructured proof makes the logical chain explicit: (1) passive relabeling changes description, not physics → δ⟨AB⟩=0; (2) Eq.(2) depends on physical θ, not basis labels; (3) therefore relabeling cannot absorb the cos θ term. |
| 5 | §5.3 | **Explicit FOM formula (+6 lines):** "The figure of merit governing experimental sensitivity is FOM(θ, β, N) = min(n_σ_LF(θ, N), n_σ_signal(θ, β, N)), where n_σ_LF = \|Gen LF 1(θ)\|/σ_LF...and n_σ_signal = \|δ⟨AB⟩\|/σ_AB...The optimum at θ = 31° reported in §4.1 maximizes this FOM via grid search." | 4.5/5 | The FOM was described qualitatively in §4.1 (FOM ∝ min(\|cos θ\|, f_LF(θ))) and used implicitly in §5.3 sensitivity tables. Writing it explicitly with all dependencies — FOM(θ, β, N) — makes the connection between §4.1 optimization and §5.3 sensitivity transparent. |
| 6 | Abstract | **Two-phase in Abstract (+2 lines):** "under fair-sampling, as the first phase of a two-phase program (loophole-open null test at η ≈ 0.87, followed by loophole-closed confirmation via SNSPD upgrade to η ≥ 0.91)" | 4.5/5 | The two-phase program was added to §7 in v62 but the Abstract still read as if the experiment was a single-shot proposal. The updated Abstract sets scope immediately: Phase 1 is the near-term null test; Phase 2 is the definitive loophole-closed version. |

### Regression
Δ: C3 refined with explicit unpublished-work caveat; Lemma 1 proof restructured (content preserved, logic clarified).

---

## v62 (2026-05-25) — 5/5-issue RCA (threshold 4.5/5): Physical motivation→§1; Lemma 1 numerical example; two-phase experimental program; figure placeholders resolved; GPT abbreviation clarified

**Scoring summary (5 issues):** 5 implemented (≥4.5/5), 0 rejected. First all-accept round since v54 — a high-quality review with genuinely new, non-oscillating concerns.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Motivation buried in §2.3 — reader encounters class in Abstract/§1 without knowing why it's natural | 4.7/5 | **Implemented** — one-sentence motivation added to §1 before Proposition 1 definition: "The basis overlap \|⟨b\|d⟩\|² is the simplest scalar quantifying the geometric relationship between successive measurements — any deformation coupling Superobserver statistics to a prior observer's recorded outcome depends on this relationship at lowest order (§2.3)." |
| 2 | Lemma 1 proof too concise — skeptical reviewer may not find algebraic proof convincing | 4.5/5 | **Implemented** — numerical illustration added after Lemma 1 proof: at θ=31°, β=0.07, overlap model predicts δ⟨AB⟩≈0.008 (4.7σ); swapping \|+1⟩↔\|−1⟩ via U=σ_x leaves all correlators invariant (δ⟨AB⟩=0) while Eq.(2) still predicts δ⟨AB⟩≈0.008 |
| 3 | Null result under fair-sampling remains open to detection-loophole objection — expectations for η≈0.87 vs η≥0.91 unclear | 4.6/5 | **Implemented** — "Two-phase experimental program" added to §7: Phase 1 (near-term, η≈0.87, loophole-open null test constraining β~0.07 under fair-sampling); Phase 2 (loophole-closed, η≥0.91 via SNSPD upgrade, converts to loophole-free conclusion) |
| 4 | [Figure X] and [Figure S1] placeholders remain — undermines presentation before arXiv submission | 4.5/5 | **Implemented** — [Figure X]→[Figure 2]; [Figure S1] replaced with descriptive prose pointing to Supplemental S1; duplicate figure numbering resolved (Figures 1-5 now sequential) |
| 5 | "GPT" in Supplemental S3 description likely misread as large language model rather than General Probabilistic Theories | 4.5/5 | **Implemented** — "GPT/weak-measurement development" → "General Probabilistic Theories (GPT) / weak-measurement development" |

### Implemented changes (v62)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **Physical motivation (+2 lines):** Added before Proposition 1 definition: "The basis overlap \|⟨b\|d⟩\|² is the simplest scalar quantifying the geometric relationship between successive measurements — any deformation coupling Superobserver statistics to a prior observer's recorded outcome depends on this relationship at lowest order (§2.3)." | 4.7/5 | The "Why overlap-only?" motivation was in §2.3 — a reader encountering the class in the Abstract and §1 had to wait until page 2-3 to learn why this particular deformation structure deserves attention. Moving the core motivation to §1 answers the "why this class?" question at the point of first encounter. The §2.3 cross-ref directs detail-seekers to the full justification. |
| 2 | §3.2 | **Lemma 1 numerical example (+5 lines):** "Numerical illustration. At θ = 31° with β = 0.07, the overlap-only model predicts δ⟨AB⟩ ≈ 0.008 (4.7σ at N = 91,000). Any unitary relabeling of the Superobserver basis — e.g., swapping \|+1⟩ ↔ \|−1⟩ via U = σ_x — leaves all correlators identically invariant (δ⟨AB⟩ = 0), while Eq. (2) still predicts δ⟨AB⟩ ≈ 0.008. The two predictions are numerically and operationally distinct." | 4.5/5 | The algebraic proof shows that basis relabeling predicts δ⟨AB⟩=0 while Eq.(2) predicts δ⟨AB⟩≠0. A skeptical reviewer may object that the two could coincide for specific parameter choices. The numerical example — using the paper's own benchmark values (θ=31°, β=0.07) — eliminates this objection: δ⟨AB⟩=0 vs δ⟨AB⟩≈0.008 are separated by 4.7σ. The explicit unitary (U=σ_x) makes the example concrete. |
| 3 | §7 | **Two-phase program (+8 lines):** "**Two-phase experimental program.** The experiment naturally splits into two phases. Phase 1 (near-term, η ≈ 0.87): a loophole-open null test using existing Bong et al. (2020) hardware plus one QWP. A null result at this stage would already constrain the overlap-only class at the β ~ 0.07 level under fair-sampling — a self-consistent exclusion independent of absolute detector efficiency, since β is measured from the same coincidence events as the LF violation. Phase 2 (loophole-closed, η ≥ 0.91 via SNSPD upgrade [16]): closes the detection loophole with no optical redesign, converting the null test into a loophole-free conclusion." | 4.6/5 | The paper previously mentioned fair-sampling and SNSPD upgrade in passing but didn't structure them as a coherent experimental program. The two-phase framing sets clear expectations: Phase 1 establishes the constraint under fair-sampling (a self-consistent but loophole-open result); Phase 2 closes the loophole. This prevents a reviewer from dismissing Phase 1 as inconclusive while acknowledging that Phase 2 is the definitive test. |
| 4 | §2.1, §4.1, §4.2, §6, §7 | **Figure placeholders resolved + numbering fixed:** [Figure X]→[Figure 2] (§4.1). [Figure S1]→descriptive prose + S1 pointer (§2.1). [Figure 2]→[Figure 3] (§4.2). [Figure 3]→[Figure 4] (§6). [Figure 4]→[Figure 5] (§7). Figures now sequentially numbered 1-5. | 4.5/5 | Placeholder figures undermine a manuscript's credibility — they signal incompleteness to a reviewer. The [Figure X] in §4.1 was the last unresolved placeholder in the main text. The EWF setup schematic (§2.1) was reclassified as supplemental material rather than a numbered main-text figure. |
| 5 | §1 | **GPT abbreviation clarified (+2 words):** "GPT/weak-measurement development" → "General Probabilistic Theories (GPT) / weak-measurement development" in Supplemental S3 description. | 4.5/5 | In 2026, "GPT" is overwhelmingly read as Generative Pre-trained Transformer. A reviewer scanning the supplemental description who reads "GPT/weak-measurement development" may wonder why large language models appear in a quantum foundations paper. The full term on first use eliminates this distracting misreading. |

### Structural changes (v62)
| Before (v61) | After (v62) | Nature |
|-------------|-------------|--------|
| §1: Proposition 1 starts with definition | +"The basis overlap \|⟨b\|d⟩\|² is the simplest scalar...any deformation...depends on this relationship at lowest order (§2.3)." → definition | Motivation front-loaded |
| §3.2 Lemma 1: Proof ends at ∎ → Operational invariant | +"Numerical illustration. At θ=31° with β=0.07...δ⟨AB⟩≈0.008...U=σ_x leaves correlators invariant...numerically and operationally distinct." → Operational invariant | Numerical example |
| §7: "...biases δ toward zero [9]. Full robustness analysis..." | +"**Two-phase experimental program.** Phase 1...Phase 2..." → "Full robustness analysis..." | Two-phase framing |
| §2.1: "[Figure S1: EWF setup...]" | "[Schematic of the EWF setup...is provided in Supplemental S1.]" | Placeholder resolved |
| §4.1: "[Figure X: FOM vs polar angle...]" | "[Figure 2: FOM vs polar angle...]" | Placeholder resolved |
| §4.2: "[Figure 2: Optical path...]" | "[Figure 3: Optical path...]" | Renumbered |
| §6: "[Figure 3: Monte Carlo...]" | "[Figure 4: Monte Carlo...]" | Renumbered |
| §7: "[Figure 4: FOM vs μ]" | "[Figure 5: FOM vs μ]" | Renumbered |
| §1 supplemental: "GPT/weak-measurement" | "General Probabilistic Theories (GPT) / weak-measurement" | Abbreviation clarified |

### Regression
Δ: §1 motivation does not modify existing constraints — it adds a forward-ref to §2.3. Lemma 1 numerical example is purely illustrative. Two-phase program reframes existing content without changing claims.

---

## v61 (2026-05-25) — 1/10-issue RCA (threshold 4.5/5): θ=31° analytic intuition in §1; title change REVERTED after RCA on premise; 9 issues rejected

**Scoring summary (10 issues):** 1 implemented (≥4.5/5), 1 implemented-then-reverted (RCA failure on premise), 8 rejected (<4.5/5).

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only ad hoc → symmetry/no-go | — | → Recurring |
| 2 | "Blind spot" → "unisolated degree of freedom" | — | → Recurring |
| 3 | Toy mechanism cụ thể hơn | — | → Recurring |
| 4 | β scale ~10⁻² → dimensional estimate | — | → Recurring |
| 5 | Reparameterization → operational observable | — | → Recurring |
| 6 | Cắt 20-30% defensive | — | → Recurring |
| 7 | "What classes of hidden dynamics generate overlap dependence" | 2.0/5 | Rejected — speculative, violates C1 |
| 8 | θ=31° numerically tuned → analytic intuition sớm hơn | 4.5/5 | **Implemented** — one-line intuition added to §1 |
| 9 | Figure "equator flatline vs tilted emergence" | — | → Recurring |
| 10 | Title aggressive → mềm hơn | 4.7→REVERTED | **Implemented then REVERTED.** Title changed, then reverted: "Blind" is standard scientific terminology, not a colloquial accusation. |

### RCA post-mortem on the title change

**What happened:** User suggested title was too aggressive. I accepted the premise without applying RCA to it — treating "Blind" as a colloquial accusation rather than scientific terminology. Title was changed from the investigative question format to a declarative statement. User then asked for RCA on the decision itself, revealing the premise was weak (~3/10).

**Root cause of the error:** RCA was applied to scoring the suggestion (is it new? does it conflict with CHANGELOG?) but NOT to validating the user's premise (is "Blind" actually aggressive in scientific context?). This is an incomplete RCA application — Step 1 (Define) requires separating symptom from cause, and the "symptom" here was the user's characterization of "Blind" as aggressive, which should have been challenged before acting.

**Lesson:** When a user asserts a characterization ("X is aggressive"), apply RCA to the characterization itself, not just to the proposed fix. "Blind" in quantum foundations literature is neutral technical terminology.

### Implemented change (v61, retained)

**§1 θ=31° analytic intuition (+2 lines):** "The optimum at 31° emerges from two competing trends — signal strength ∝ |cos θ| vs. LF violation strength — whose intersection determines the figure of merit (§4.1)."

---

## v60 (2026-05-25) — 2/10-issue RCA (threshold 4.5/5): LF optimization distinction (§3.5); QM vs overlap-model prediction table (§8.1); 8/10 issues rejected as oscillation repeats

**Scoring summary (10 issues):** 2 implemented (≥4.5/5), 8 rejected (<4.5/5). Eight of ten issues are repeats of items rejected in v53-v59.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Toy microscopic model | — | → Recurring |
| 2 | "Never tested" → "not systematically isolated" | — | → Recurring |
| 3 | Cắt 20-30% equatorial cancellation | — | → Recurring |
| 4 | β physical intuition từ decoherence/weak measurement | — | → Recurring |
| 5 | Coordinate artifact — operational observable sớm hơn | — | → Recurring |
| 6 | Figure raw counts/error bars | — | → Recurring |
| 7 | Abstract overloaded | 3.0/5 | Rejected — already compressed 13→8 lines (v53) |
| 8 | Novelty vs LF optimization literature | 4.5/5 | **Implemented** — "Distinction from LF optimization" paragraph added to §3.5 |
| 9 | Scope limitation buried → kéo lên sớm | 3.5/5 | Rejected — §3.2 is the correct location for scope |
| 10 | Falsifiable prediction table | 4.5/5 | **Implemented** — QM vs overlap-model prediction table added to §8.1 |

### Implemented changes (v60)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 8 | §3.5 | **"Distinction from LF optimization" (+11 lines):** New paragraph at end of §3.5: "This work is complementary to, not competitive with, the LF inequality optimization literature [2,10-12]. LF optimization varies azimuthal angles φ at fixed θ = π/2 to maximize inequality violation; this work varies the polar angle θ to test for overlap-dependent deformation. The two address different questions: LF optimization asks 'how strongly does nature violate Local Friendliness?'; this work asks 'has the overlap-only class ever been tested?' The single-waveplate protocol preserves the optimized LF violation (8.6σ) while adding the θ degree of freedom — combining both tests in one experiment." | 4.5/5 | Genuinely new. No prior version systematically distinguished this work from the LF optimization literature. The distinction is important: a reviewer might think "LF optimization already varies measurement angles — what's new?" The answer: LF optimization varies φ at fixed θ=π/2 within the equatorial plane; this work varies θ out of the equatorial plane, testing a different hypothesis. The two are complementary and the protocol does both simultaneously. |
| 10 | §8.1 | **QM vs overlap-model prediction table (+8 lines):** 4-row table: Gen LF 1 at θ=31° (QM: +0.0891, overlap: same), δ⟨AB⟩ at θ=31° (QM: 0, overlap: β cos(31°) ≈ 0.857β), δ⟨AB⟩ at θ=π/2 (QM: 0, overlap: 0 by cancellation), δ⟨AB⟩(θ) functional form (QM: δ=0 ∀θ, overlap: δ ∝ cos θ). | 4.5/5 | v56 added falsification conditions in prose. A table crystallizes the predictions side-by-side, making the experimental discriminator immediately visible. The table shows both where the models AGREE (Gen LF 1, equatorial δ⟨AB⟩) and where they DIVERGE (δ⟨AB⟩ at tilted θ, functional form). This format is standard in experimental proposal papers. |

### Structural changes (v60)
| Before (v59) | After (v60) | Nature |
|-------------|-------------|--------|
| §3.5: ends at "Tilting the Superobserver opens access..." → §4 | +"**Distinction from LF optimization.** This work is complementary to...combining both tests in one experiment." → §4 | Novelty boundary vs LF literature |
| §8.1: ends at "Either outcome is informative..." | +Prediction table (4 rows: Gen LF 1, δ⟨AB⟩ at 31°, δ⟨AB⟩ at π/2, functional form) | Falsifiable predictions |

### Regression
Δ: LF optimization distinction is new content — does not modify existing constraints.

---

## v59 (2026-05-25) — 1/8-issue RCA (threshold 4.5/5): Blind θ-sweep protocol added to §8.2; 7/8 issues rejected as oscillation repeats

**Scoring summary (8 issues):** 1 implemented (≥4.5/5), 7 rejected (<4.5/5). Seven of eight issues are repeats of items rejected or addressed in v53-v58.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Toy model động lực học | — | → Recurring |
| 2 | "Why this class?" — EFT benchmark | — | → Recurring |
| 3 | Calibration artifact — blind θ-sweep | 4.5/5 | **Implemented** — blind protocol added to §8.2 |
| 4 | Claim aggressive — "all", "entire", "blind" | — | → Recurring |
| 5 | Smoking gun prediction — signature phụ | 2.5/5 | Rejected — directly violates C20 ("smoking gun" deliberately removed v37) |
| 6 | Paper dài và lặp — cắt 20-25% | — | → Recurring |
| 7 | Experiment > theory — đẩy theorem | 3.5/5 | Rejected — theorem IS the paper's strongest asset; deliberate structural choice |
| 8 | Trivial geometry — unisolated parameter | — | → Recurring |

### Implemented change (v59)

**§8.2 θ-sweep (+2 lines):** Added blind protocol: "To prevent analysis bias, the sweep should be performed blind: randomize the θ sequence and analyze δ⟨AB⟩(θ) without knowledge of the θ-to-data mapping until the cos θ fit is finalized."

| RCA Score | Rationale |
|-----------|-----------|
| 4.5/5 | Genuinely new — no prior version proposed a blind protocol. The θ-sweep has been mentioned as a future direction since v35 but never specified HOW to perform it rigorously. A blind protocol prevents the analyst from (unconsciously) selecting data subsets or analysis parameters that favor the cos θ hypothesis. This is standard practice in precision tests (e.g., blinding in particle physics and cosmology) but was missing from the EWF proposal. |

### Regression
Δ: §8.2 θ-sweep upgraded from conceptual to protocol-level with blinding.

---

## v58 (2026-05-25) — 2/9-issue RCA (threshold 4.5/5): §3.2 structural cleanup (Corollary+Examples cut, Hierarchy→Scope, Operational Invariant tightened); §3.1 cosθ dedup; 7/9 issues rejected as oscillation repeats

**Scoring summary (9 issues):** 2 implemented (≥4.5/5), 7 rejected (<4.5/5). Seven of nine issues are variants of items rejected in v55-v57 — the RCA threshold mechanism continues to prevent oscillation.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only ad-hoc | — | → Recurring |
| 2 | Quá dài, lặp cosθ | 4.5/5 | **Implemented** — §3.1 dedup: 3 "cos θ" in 6 lines → 1 |
| 3 | Physics motivation yếu | — | → Recurring |
| 4 | Reparameterization | — | → Recurring |
| 5 | β arbitrary | — | → Recurring |
| 6 | Defensive writing | 4.2/5 | Rejected — v55+v57 already reduced; remaining hedging is functional C1 boundary |
| 7 | Section 3 overloaded | 4.8/5 | **Implemented** — §3.2 structural cleanup (−17 lines) |
| 8 | Novelty boundary unclear | — | → Recurring |
| 9 | Null at symmetry trivial | — | → Recurring |

### Implemented changes (v58)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 7 | §3.2 | **Structural cleanup (−17 lines):** Corollary (5 lines) merged into Proposition 1 (key sentence "no overlap-dependent modification evades this cancellation..." appended to Prop 1). Examples block (5 lines: g(x)=x², sin(πx), (1−x)^n) cut — all show g(1/2)=constant, already proven by Proposition 1 and §3.3. Deformation Hierarchy (8 lines standalone block) merged into Scope Limitation as compact inline (3 lines: "Level 0...Level 1...Level 2...Level 3"). Operational Invariant tightened from 11 to 5 lines — removed overlap with Lemma 1 Proof (the mechanism of invariance is already proven there; Operational Invariant now states the consequence). §3.2 went from 10 labeled blocks (Definition, Prop 1, Corollary, Lemma 1, Proof, Operational Invariant, Scope, Hierarchy, Examples, Contextuality) → 7 blocks. | §3.2 accumulated layers across v44-v56: v44 added Contextuality, v54 added outside-scope examples, v55 added Deformation Hierarchy + expanded Operational Invariant, v56 added comparison table. Each addition was individually justified but collectively created bloat. This cleanup removes content that is (a) proven elsewhere (Examples redundant with §3.3 proof), (b) restates what was just said (Corollary restates Proposition 1), or (c) can be compactly merged (Hierarchy→Scope). |
| 2 | §3.1 | **cosθ dedup (−3 lines):** "The distinctive experimental signature is cos θ scaling: any non-zero δ⟨AB⟩ ∝ cos θ...making a cos θ signal difficult...This cos θ dependence is a genuine observable" → "The distinctive experimental signature is δ⟨AB⟩ ∝ cos θ: this scaling...and is a genuine observable, not a gauge artifact (Lemma 1, §3.2)." Three "cos θ" in 6 lines → one. | cosθ is the paper's mathematical signature — it SHOULD appear in equations and key statements. But 3 occurrences in 6 consecutive lines is stylistic redundancy, not functional signposting. |

### Regression
Δ: Corollary content preserved in Proposition 1 (one appended sentence); Hierarchy content preserved in compact Scope form; Operational Invariant key claim ("only β=0 or θ=π/2 removes it") preserved.

---

## v57 (2026-05-25) — 2/7-issue RCA (threshold 4.5/5): §7 compressed 67→12 lines (detail→S2); §8.1 compressed 22→10 lines; §3.2 contextuality prose→table; paper 714→649 lines (−9%)

**Scoring summary (7 issues):** 2 implemented (≥4.5/5), 5 rejected (<4.5/5). Notably, 5 of 7 issues are repeats of items rejected in v55 or v56 — the RCA threshold mechanism is correctly preventing oscillation.

| # | Issue | RCA Score | Root Cause / Rejection Reason | Action |
|---|-------|-----------|-------------------------------|--------|
| 1 | overlap-only ad hoc — toy mechanism | — | → Recurring |
| 2 | Paper quá dài — cắt 30-40% | 4.7/5 | **Implemented** — §7→12-line summary + S2 pointer; §8.1→10 lines merged; paper 714→649 lines |
| 3 | Theorem buried — đẩy Proposition 1 sớm hơn | 4.2/5 | Rejected — Proposition 1 already §1 ¶2 (v45) |
| 4 | Coordinate artifact — invariant rõ hơn | — | → Recurring |
| 5 | β scale — weak-measurement derivation | — | → Recurring |
| 6 | "first ever" — soften wording | — | → Recurring |
| 7 | Contextuality defensive — rút ngắn | 4.5/5 | **Implemented** — Prose cut from 10→3 lines; table retained |

### Implemented changes (v57)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2 | §7 | **Robustness compressed 67→12 lines (−55):** Old: full §7 with visibility/detector efficiency/angular tolerance (6 lines), systematic-error budget (8 lines), φ-scramble control (16 lines), robustness summary table (8 lines), detection loophole discussion (14 lines), loophole summary table (10 lines). New: single compact paragraph covering all key numbers (μ≥0.92, η≥0.91, six-source error budget, φ-scramble with fit equation, detector inefficiency bias direction) + S2 pointer. Full analysis, tables, and Monte Carlo in Supplemental S2. | 4.7/5 | The previous §7 was a mini-review paper on systematics — proportionally heavy for a paper whose core contribution is a 3-line geometric proof. The compressed version preserves every key number and the φ-scramble protocol while moving implementation detail to S2 where referees can verify it. This is the single largest cut in the paper's history (−55 lines in one edit). |
| 2 | §8.1 | **Interpretation compressed 22→10 lines (−12):** Merged "Interpretation" + "Falsification conditions" into "Interpretation and Falsification." Cut: "Interpreting this as overlap-dependent deformation specifically requires θ-sweeps and multi-observer follow-up" (redundant — already in §8.2 θ-sweep), "A null result...excludes...above sensitivity threshold" (redundant — falsification conditions say same thing more precisely), "A non-zero signal that does not scale as cos θ would indicate physics beyond the overlap-only class — still interesting, but not what this proposal targets" (verbose — folded into falsification condition ii). Kept: δ≠0 interpretation, two falsification criteria, "either outcome informative," S3 pointer. | 4.5/5 | The interpretation subsection had accumulated layers: v53 merged §8.1+§8.2, v56 added falsification conditions. The result was 22 lines with overlapping content. Compressed version is 10 lines doing the same work. |
| 7 | §3.2 | **Contextuality prose→table (−9 lines):** Old: 10-line prose distinction (v44) + 6-line comparison table (v56) = 16 lines. New: 3-line intro ("logically independent...concerns measurement registration, not measurement setting") + 6-line table = 9 lines. | 4.5/5 | The v44 prose and v56 table covered the same distinction twice. The table is more information-dense; the prose is now a compact intro to the table rather than a parallel explanation. |

### Structural changes (v57)
| Before (v56) | After (v57) | Nature |
|-------------|-------------|--------|
| §7: 67 lines (full robustness analysis with subsections, tables, loophole discussion) | 12 lines (compact summary + S2 pointer) | Major compression |
| §8.1: 22 lines (Interpretation + Falsification conditions subsections) | 10 lines (merged Interpretation and Falsification) | Compression |
| §3.2: 16 lines (contextuality prose + table) | 9 lines (compact intro + table) | Prose dedup |
| Paper: 714 lines (~5 pages) | 649 lines (~4 pages) | −65 lines (−9%) |

### Regression
Δ: §7 robustness detail → S2 (C17 strengthened); φ-scramble quantitative protocol preserved in compressed form; falsification conditions preserved; contextuality comparison table preserved.

---

## v56 (2026-05-25) — 4/10-issue RCA (threshold 4.5/5): Reparameterization defense §1; falsification roadmap §8.1; quantitative φ-scramble §7; contextuality comparison table §3.2

**Scoring summary (10 issues):** 4 implemented (≥4.5/5), 6 rejected (<4.5/5).

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Physical mechanism chưa rõ — cần toy model | — | → Recurring |
| 2 | β ad-hoc — liên hệ parameter theory | — | → Recurring |
| 3 | Reparameterization — defense cần sớm hơn | 4.5/5 | **Implemented** — one sentence added to §1 |
| 4 | "Mọi EWF mù" wording mềm hơn | — | → Recurring |
| 5 | Thiếu falsification roadmap | 4.7/5 | **Implemented** — "Falsification conditions" paragraph in §8.1 |
| 6 | Theorem mạnh hơn physics | 4.2/5 | Rejected — deliberate structural choice |
| 7 | Birefringence fake cosθ — control định lượng | 4.5/5 | **Implemented** — Quantitative φ-scramble protocol |
| 8 | Paper dài, cắt defensive wording | — | → Recurring |
| 9 | Hình minh họa đơn giản hơn | — | → Recurring |
| 10 | Novelty vs contextuality — cần bảng so sánh | 4.5/5 | **Implemented** — 3-row comparison table |

### Implemented changes (v56)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 3 | §1 | **Reparameterization defense (+2 lines):** After "class that has remained structurally untested," added: "The predicted cos θ signal is invariant under any basis redefinition of the Superobserver alone (Lemma 1, §3.2) — it is a genuine observable, not a coordinate artifact." | 4.5/5 | The "just a basis change" objection is the single most common reviewer reflex. v41 added a forward-ref from §3.1, v42+v46 moved/expanded Lemma 1, v55 expanded the operational invariant — but none of this reached §1 where the casual reader forms their first impression. One sentence in §1 preempts the objection before it forms. |
| 5 | §8.1 | **Falsification roadmap (+9 lines):** Added "**Falsification conditions.**" paragraph: (i) θ-sweep null at ±0.003 floor (N=200k) excludes cos θ; (ii) δ⟨AB⟩(θ) deviating from cos θ indicates physics beyond overlap-only class. Closes with: "Either outcome is informative: falsification closes the overlap-only window; a cos θ signal opens it." | 4.7/5 | Genuinely new — no prior version had explicit falsification criteria. The null-test framing is strengthened by telling reviewers exactly what result would kill the idea. The "either outcome is informative" framing positions the experiment as win-win: null = falsification, positive = discovery. |
| 7 | §7 | **Quantitative φ-scramble (+8 lines):** Expanded from conceptual to quantitative: N_φ ≥ 10 uniformly spaced values; fit model δ⟨AB⟩(φ) = A + B cos(2φ) + C sin(2φ); geometric predicts A≠0, B,C≈0; birefringence predicts non-zero B or C; σ_A ≈ 0.0017 distinguishes β=0.07 at 4.7σ. | 4.5/5 | The v43 φ-scramble was qualitative ("randomize φ, if signal persists, it's geometric"). An experimentalist needs: how many φ values? What fit? What's the discrimination threshold? The expanded protocol answers all three. |
| 10 | §3.2 | **Contextuality comparison table (+6 lines):** 3-row table comparing KS Contextuality, Overlap-Dependence (this work), and Weak Measurement [18] across Property, Depends on, Observable, and Constrained by dimensions. | 4.5/5 | v44 added contextuality distinction prose; v44 explicitly rejected a table as "disproportionate for 5-page paper" (RCA 3.0/5). This v56 change reverses that decision: the table is 6 lines, compact, and makes the novelty boundary immediately visible. Reviewer sees at a glance: overlap-dependence is about registration, not setting; constrained by Proposition 1, not Bell-KS. |

### Structural changes (v56)
| Before (v55) | After (v56) | Nature |
|-------------|-------------|--------|
| §1: "class that has remained structurally untested." | +"The predicted cos θ signal is invariant under any basis redefinition of the Superobserver alone (Lemma 1, §3.2) — it is a genuine observable, not a coordinate artifact." | Reparameterization preemption |
| §8.1: "A null result...excludes...above sensitivity threshold. Implications..." | +"**Falsification conditions.** The overlap-only class would be definitively falsified if: (i)...(ii)...Either outcome is informative..." | Falsification roadmap |
| §7 φ-scramble: 8 lines (conceptual: "randomize φ...if signal persists, geometric") | 14 lines (quantitative: N_φ≥10, fit model, discrimination thresholds, σ_A values) | Quantitative control protocol |
| §3.2: contextuality distinction prose ends → §3.3 | +Comparison table (KS Contextuality vs Overlap-Dependence vs Weak Measurement) → §3.3 | Novelty comparison table |

### Regression
Δ: C18 Lemma 1 now forward-referenced from §1; C19 φ-scramble upgraded from conceptual to quantitative.

---

## v55 (2026-05-25) — 5/9-issue RCA (threshold 4.5/5): Physical context + weak-measurement toy model; operational invariant expanded; deformation hierarchy; defensive qualifier density reduced

**Scoring summary (9 issues):** 5 implemented (≥4.5/5), 4 rejected (<4.5/5).

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | overlap-only class arbitrary — needs toy model | 4.5/5 | **Implemented** — "Physical context" paragraph + weak measurement + decoherence + minimal toy model |
| 2 | theorem obvious mathematically | — | → Recurring |
| 3 | "why would nature depend on overlap?" | 4.5/5 | **Implemented** — Combined with #1: weak measurement + decoherence connections |
| 4 | β lacks physical scale | — | → Recurring |
| 5 | reparameterization artifact | 4.5/5 | **Implemented** — Operational invariant expanded |
| 6 | repetition of "equator cancellation" | 4.2/5 | Rejected — diminishing returns |
| 7 | too defensive — "we do not claim…" | 4.7/5 | **Implemented** — Reduced defensive density |
| 8 | signal survival with realistic optics | 4.0/5 | Rejected — S2 is the right location |
| 9 | theorem scoped too narrowly | 4.6/5 | **Implemented** — "Deformation hierarchy" (§3.2) |

### Implemented changes (v55)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1+3 | §2.3 | **"Physical context" paragraph (+10 lines):** Replaced defensive "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation" with: weak measurement precedent (postselection-conditioned weak values depend on same \|⟨ψ_pre\|ψ_post⟩\|² structural overlap), decoherence precedent (environmental monitoring via pointer-state overlap), and minimal toy model (Superobserver measurement weakly disturbs Friend's record proportionally to basis overlap → leading-order correction takes form Eq. 2-3, derivation in S3). Closes with: "This is a plausibility argument, not a derivation from a complete theory — it shows that overlap-dependence is a structurally natural hypothesis, not an arbitrary choice." | 4.5/5 | v53 cut GPT/weak-measurement motivation → paper felt arbitrary. v54 added "Why overlap-only?" as logical/minimal motivation. This v55 change adds PHYSICAL precedent without over-claiming mechanism. The toy model ("measurement disturbs Friend's record proportionally to basis overlap") gives reviewers a concrete mental model. The disclaimer ("plausibility argument, not a derivation") prevents over-interpretation. Weak measurement [18] and decoherence provide established structural precedent for overlap-dependence in quantum foundations. |
| 5 | §3.2 | **Operational invariant expanded (+5 lines):** After "No basis redefinition of the Superobserver alone can generate this signal," added: "Physically, this means the cos θ signal is as robust as the correlator ⟨AB⟩ itself — it cannot be eliminated by any choice of Superobserver measurement coordinates. The only way to remove it is β = 0 (standard QM) or θ = π/2 (equatorial measurement). Any non-zero δ⟨AB⟩ at θ ≠ π/2 therefore indicates departure from the standard Born rule, independent of measurement-basis convention." | 4.5/5 | The mathematical invariant was stated but the physical consequence was not drawn. "As robust as ⟨AB⟩ itself" gives an intuitive benchmark. "Only way to remove it is β=0 or θ=π/2" makes the no-go explicit. "Departure from standard Born rule, independent of measurement-basis convention" directly counters "reparameterization artifact" objection. |
| 9 | §3.2 | **Deformation hierarchy (+8 lines):** After scope limitation, added: "**Deformation hierarchy.** The overlap-only class is the first level of a natural hierarchy: Level 0 — overlap-only (P' depends on \|⟨b\|d⟩\|²; this work, constrained by Proposition 1); Level 1 — density-matrix-dependent (P' depends on ρ_F, e.g., Tr[ρ_F²]); Level 2 — multi-partite (P' depends on correlations between multiple Friends); Level 3 — non-geometric (timing, path, or other degrees of freedom). Each level beyond 0 is unconstrained by Proposition 1 and requires independent experimental designs. The single-waveplate protocol (§4-7) targets Level 0 as the first step in a broader research program." | 4.6/5 | v54 added one concrete outside-scope example (Tr[ρ_F²]). This v55 change structures the examples into a hierarchy, showing the paper is the FIRST step in a research program — Level 0 is the natural starting point because it's the simplest geometric deformation. Reframes "class too narrow" as "deliberate first step." |
| 7 | Abstract, §1, §2.3, §9 | **Defensive qualifier density reduced:** Abstract: "illustrative benchmark sensitivity β ~ 0.07" → "sensitivity β ~ 0.07". §1: same. §1 ESP: "This paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics. It makes no claim about the existence of overlap-dependent deformation in nature." → "This paper makes no claim about the existence of overlap-dependent deformation in nature — it proposes a null-test protocol." (2 sentences → 1, "not an alternative interpretation" removed as redundant). §2.3: "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics" → removed (replaced by physical context paragraph). §9: "illustrative benchmark sensitivity β ~ 0.07" → "sensitivity β ~ 0.07". §5.3: "illustrative benchmark" language retained (qualifiers belong in methodology section, not headlines). | 4.7/5 | v54 increased qualifier density to address "overclaim" concern — but over-corrected into defensiveness. v55 restores confident voice at core claims (Abstract, §1, §9) while keeping precision qualifiers in §5.3 methodology where they belong. The ESP boundary (C1) is preserved but compressed from 2 defensive sentences to 1 compact factual statement. |

### Structural changes (v55)
| Before (v54) | After (v55) | Nature |
|-------------|-------------|--------|
| §2.3: "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics." + "**Why overlap-only?**...without invoking a specific microphysical mechanism." | "**Why overlap-only?**...structurally untested." + "**Physical context.** Basis-overlap dependence has established precedent...weak measurement...decoherence...toy model (measurement disturbance ∝ basis overlap → Eq. 2-3)...plausibility argument, not arbitrary choice." | Physical precedent + toy model |
| §3.2 operational invariant: ends at "No basis redefinition of the Superobserver alone can generate this signal." | +"Physically, this means the cos θ signal is as robust as the correlator ⟨AB⟩ itself...only way to remove it is β=0 or θ=π/2...indicates departure from standard Born rule, independent of measurement-basis convention." | Physical intuition expansion |
| §3.2: "The experiment (§4-7) constrains the overlap-only class; independent designs are needed for broader classes." → "**Examples.**" | +"**Deformation hierarchy.** Level 0 (overlap-only, this work) → Level 1 (density-matrix) → Level 2 (multi-partite) → Level 3 (non-geometric)...first step in a broader research program." → "**Examples.**" | Hierarchy |
| Abstract, §1, §9: "illustrative benchmark sensitivity β ~ 0.07" | "sensitivity β ~ 0.07" | Less defensive |
| §1 ESP: "This paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics. It makes no claim..." | "This paper makes no claim about the existence of overlap-dependent deformation in nature — it proposes a null-test protocol. Its two claims are structural:" | Compressed + confident |
| §2.3: "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation" | Removed (replaced by physical context) | Defensive line removed |

### Regression
Δ: C1 ESP boundary compressed but retained; C6 weak-measurement connection restored (v53 cut → v55 selectively restored with "precedent" framing, not "mechanism"); C10 benchmark language retained in §5.3; defense level recalibrated (less hedging at core claims, qualifiers in methodology section).

---

## v54 (2026-05-25) — 7-issue RCA (threshold 4.5/5): "Why overlap-only?" minimal operational deformation; concrete outside-scope examples; killer Figure 1; ~20 lines repetition cut; sensitivity→illustrative benchmark; qualifier density; null-test framing

**Scoring summary (7 issues):** 7 implemented (≥4.5/5), 0 rejected.

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Overclaim — need more qualifiers | 4.5/5 | Qualifiers clustered in §1 ESP; not woven into experimental claims throughout | **Implemented** — "overlap-only class" qualifier added to Abstract, §1 claim B, §5.3 discriminator |
| 2 | Phenomenology lacks foundation | 4.7/5 | §2.3 explained HOW parametrization works but never WHY overlap-only is the MINIMAL class to test | **Implemented** — New "Why overlap-only?" subsection in §2.3: overlap is simplest geometric scalar → minimal operational deformation → isolates θ without microphysical mechanism |
| 3 | "Toy model" vulnerability | 4.6/5 | β sensitivity thresholds presented as precise predictions rather than search targets | **Implemented** — "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation" added to §2.3; ESP paragraph reframed |
| 4 | Class too narrow | 4.5/5 | Scope limitation listed categories abstractly without concrete physical counterexamples | **Implemented** — §3.2 Scope limitation expanded with explicit example: P' ∝ P_QM · h(Tr[ρ_F²]) depends on Friend state purity, not basis overlap, so does NOT cancel at equator |
| 5 | Repetition of "equatorial cancellation" | 4.7/5 | Thesis re-stated in ~8 locations; many redundant signposting | **Implemented** — ~20 lines cut: §3.1 discriminator paragraph compressed; §3.5 "three-line proof" + "structural reason" merged 13→5 lines; §5.3 "exact fixed point" restatement cut; §9 conclusion compressed |
| 6 | Experimental claim inflated | 4.8/5 | Headline sensitivity numbers (abstract/§1/§9) dropped the "benchmark parametrization" qualifier from §5.3 body | **Implemented** — "β ≥ 0.07" → "β ~ 0.07" with "illustrative benchmark sensitivity" in Abstract, §1, §5.3, §9. §5.3 adds explicit disclaimer: "These thresholds are illustrative — no existing theory predicts a specific β value" |
| 7 | Missing killer figure | 4.5/5 | Central geometric insight (flatline → emergence) had no dedicated figure | **Implemented** — Detailed Figure 1 specification in §3.4: Bloch sphere equator vs tilted, overlap asymmetry values, δ⟨AB⟩ ∝ cos θ curve with null at 90° and sensitive region at 31° |

### Implemented changes (v54)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 2+3 | §2.3 | **"Why overlap-only?" subsection (+8 lines) + null-test framing.** After EFT analogy: "Eq. (2-3) is a search target, not a theory prediction — the paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics." New subsection: "**Why overlap-only?** The basis overlap \|⟨b\|d⟩\|² is the simplest scalar quantifying the geometric relationship between two measurement bases. Any deformation coupling Superobserver statistics to a prior observer's recorded outcome must depend on this relationship at lowest order; the overlap-only class is therefore the minimal operational deformation — it isolates the geometric degree of freedom (θ) that equatorial measurements leave structurally untested, without invoking a specific microphysical mechanism." | 4.7/5 | v53 cut GPT/weak-measurement motivation but left a gap: WHY this class? The new subsection answers with internal logic rather than external physics — overlap is the simplest geometric scalar, any outcome-coupling deformation depends on it at lowest order, therefore overlap-only is the minimal class. "Without invoking a specific microphysical mechanism" directly counters "toy model" by owning the phenomenological nature. |
| 4 | §3.2 | **Concrete outside-scope examples (+3 lines).** Scope limitation expanded: "Broader deformations — depending on the full reduced density matrix ρ_F of the Friend (rather than only \|⟨b\|d⟩\|²), on the concurrence between Friend and Superobserver subsystems, or on non-geometric variables such as timing or path — lie outside this theorem's scope. For instance, a deformation P' ∝ P_QM · h(Tr[ρ_F²]) would depend on Friend state purity, not basis overlap, and would not cancel at the equator." | 4.5/5 | Abstract categories ("full density matrix, higher-order correlators") give no intuition. The concrete example (ρ_F purity) shows exactly what the theorem does NOT cover — a physically meaningful deformation that survives at the equator. This makes the overlap-only scope feel like a deliberate choice, not an oversight. |
| 7 | §3.4 | **Killer Figure 1 specification (+5 lines).** Replaced generic "[Figure X: Balanced vs tilted overlap geometry...]" with detailed 3-panel specification: Left (Bloch sphere at equator, all overlaps = 1/2, δ⟨AB⟩ = 0 flatline), Right (axis tilted to θ = 31°, overlap asymmetry values), Lower (δ⟨AB⟩ ∝ cos θ curve, null at 90°, sensitive region at 31° with dashed vertical line). | 4.5/5 | The paper's central geometric insight was carried entirely by text. A 3-panel figure showing the flatline → emergence transition makes the theorem VISUAL — reviewers see the null point and the cos θ onset without parsing algebra. |
| 5 | §3.1, §3.5, §5.3, §9 | **Repetition cuts (−20 lines):** §3.1: discriminator paragraph compressed (removed "equatorial measurements sit at an exact fixed point where all overlap-dependent deformations vanish identically; tilting away from equator produces linear onset" — repeats §3.2 Proposition 1+Corollary). §3.5: merged "structural reason" (7 lines) + "three-line proof" (8 lines) → 5 compact lines. §5.3: cut "the equator (θ = π/2) is an exact fixed point where all overlap-dependent deformations vanish identically; tilting away from the equator produces a linear onset ∝ cos θ" — repeats §3.1. §9: compressed 15→9 lines; cut "for any function g of the basis overlap, not just Eq. (3)" + removed one layer of S1-wrapped hedging (stated 3× in conclusion → stated once). | 4.7/5 | The equatorial cancellation was re-stated in ~8 locations: Abstract, §1, §2.3, §3.1, §3.2, §3.5, §5.3, §9. After cuts, the theorem is stated formally in §1 and §3.2 (Proposition 1), referenced functionally elsewhere. The paper no longer re-derives its own result in every section. |
| 1+6 | Abstract, §1, §5.3, §9 | **"Illustrative benchmark" + qualifier language:** Abstract: "with sensitivity β ≥ 0.07 at 5σ" → "with illustrative benchmark sensitivity β ~ 0.07 at 5σ"; "first isolated test of this class" → "first isolated test of the overlap-only class". §1: "providing sensitivity β ≥ 0.07 at 5σ" → "providing illustrative benchmark sensitivity β ~ 0.07 at 5σ"; ESP: "enables the first experimental probe" → "enables the first experimental probe of this class"; added lead sentence: "This paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics." §5.3: "the minimum detectable coupling at 5σ confidence is β ≥ 0.07" → "For the benchmark parametrization Eq. (2-3), the illustrative 5σ detection threshold is β ~ 0.07"; added: "These thresholds are illustrative — no existing theory predicts a specific β value; they quantify the experiment's capability for the benchmark parametrization." §9: "providing sensitivity β ≥ 0.07 at >5σ" → "providing illustrative benchmark sensitivity β ~ 0.07 at >5σ". | 4.8/5 | Highest priority fix. The paper's headline numbers (β ≥ 0.07) read as unconditional experimental predictions. Adding "illustrative benchmark" + "β ~" instead of "β ≥" signals that these are sensitivity estimates for a parametrization no theory predicts. The §5.3 disclaimer ("no existing theory predicts a specific β value") makes the instrumental nature of β explicit. |

### Structural changes (v54)
| Before (v53) | After (v54) | Nature |
|-------------|-------------|--------|
| §2.3: EFT analogy ends → "Consider modifications..." | +"Eq. (2-3) is a search target, not a theory prediction..." + "**Why overlap-only?** The basis overlap \|⟨b\|d⟩\|² is the simplest scalar..." | New subsection + null-test framing |
| §3.2 Scope: "...Broader deformations — depending on the full density matrix, higher-order correlators, or non-geometric variables — lie outside this theorem's scope." | "...Broader deformations — depending on the full reduced density matrix ρ_F of the Friend (rather than only \|⟨b\|d⟩\|²), on the concurrence between Friend and Superobserver subsystems, or on non-geometric variables such as timing or path — lie outside this theorem's scope. For instance, a deformation P' ∝ P_QM · h(Tr[ρ_F²]) would depend on Friend state purity, not basis overlap, and would not cancel at the equator." | Concrete counterexample |
| §3.4: "[Figure X: Balanced vs tilted overlap geometry...]" | "[Figure 1: **Equatorial flatline vs. tilted cos θ emergence.** Left panel...Right panel...Lower panel...]" | Killer figure specification |
| §3.1 discriminator: 9 lines (fixed-point restatement + cosθ emergence + systematic distinction) | 6 lines (cosθ signature + systematic distinction; fixed-point restatement removed) | Repetition cut |
| §3.5 closing: 15 lines ("structural reason" 7 lines + "three-line proof" 8 lines) | 5 lines (merged reason + consequence) | Repetition cut (−10) |
| §5.3 discriminator: includes "the equator (θ = π/2) is an exact fixed point where all overlap-dependent deformations vanish identically; tilting away from the equator produces a linear onset ∝ cos θ" | Removed fixed-point restatement; discriminator focuses on cosθ signature vs systematics | Repetition cut |
| §5.3 sensitivity: "the minimum detectable coupling at 5σ confidence is β ≥ 0.07" | "For the benchmark parametrization Eq. (2-3), the illustrative 5σ detection threshold is β ~ 0.07...These thresholds are illustrative — no existing theory predicts a specific β value" | Illustrative benchmark reframe |
| §9 conclusion: 15 lines (theorem restatement + S1 ×3 + experiment + S1 ×2 + closing) | 9 lines (compact theorem + S1 ×1 + experiment + closing) | Repetition cut (−6) |
| Abstract, §1: "sensitivity β ≥ 0.07 at 5σ" | "illustrative benchmark sensitivity β ~ 0.07 at 5σ" | Illustrative benchmark |
| §1 ESP: "enables the first experimental probe." | "enables the first experimental probe of this class." + lead: "This paper proposes a null-test protocol, not an alternative interpretation of quantum mechanics." | Qualifier + framing |

### Regression
Δ: C1 ESP strengthened (null-test framing added); C3 S1 qualifier retained in §1, §3.5, §9; C10 benchmark language strengthened to "illustrative benchmark"; C17 strengthened (microphysical mechanism → not invoked).

---

## v53 (2026-05-25) — 6-issue RCA (threshold 4.5/5): Abstract theorem+null-test+consequence; §2.3 GPT/weak-measurement stripped; §8.1+§8.2 merged; novelty reframed; "phenomenological null test" genre explicit

**Scoring summary (6 issues):** 6 implemented (≥4.5/5), 0 rejected.

| # | Issue | RCA Score | Root Cause | Action |
|---|-------|-----------|------------|--------|
| 1 | Claims too strong — "all experiments blind" | 4.5/5 | S1 qualifier structurally separated from claim; "every measurement has been at equator" reads as absolute | **Implemented** — Abstract claims now bounded by theorem scope ("for the entire overlap-only class"), S1 qualifier in §1 |
| 2 | Physical motivation weak — GPT/weak-measurement narrative | 4.7/5 | §2.3 fought against paper's own strength (geometric theorem) by reaching for external justification | **Implemented** — §2.3 Core idea stripped ~10 lines: GPT framework, registration-memory coupling, weak measurement connection, context-compatibility chain all removed |
| 3 | Repetition — discussion/defensive wording | 4.6/5 | §8.1 (operational) and §8.2 (model-context) overlapped functionally; both pointed to S3 | **Implemented** — §8.1+§8.2 merged into single "Interpretation" subsection; "Neither predict nor preclude" defensive wording cut |
| 4 | "Trivial symmetry" vulnerability | 4.6/5 | Novelty framed as mathematical discovery ("we prove") rather than experimental gap identification | **Implemented** — §1: "The novelty is not the overlap formula itself...but the recognition that θ has never been isolated as an independent control parameter in actual EWF implementations" |
| 5 | Abstract overloaded | 4.7/5 | Abstract accumulated defensive qualifiers (S1, fair-sampling, SNSPD) that belong in body | **Implemented** — Abstract compressed 13→8 lines: theorem statement + phenomenological null test + measurable consequence |
| 6 | Scope unclear — genre not stated | 4.5/5 | "Phenomenological null-test proposal" never explicitly named; abstract prioritized results over genre | **Implemented** — "phenomenological null test" added to Abstract sentence 2; §1 novelty reframe reinforces scope |

### Implemented changes (v53)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1+5+6 | Abstract | **Compressed 13→8 lines (−5):** Old: "Within currently surveyed optical EWF implementations (Supplemental S1), the Superobserver's polar angle θ...has not previously been isolated...We prove...We propose a single-waveplate null test..." New: "We prove an equatorial cancellation theorem (Proposition 1): at θ = π/2, every overlap-dependent modification P = P_QM · g(\|⟨b\|d⟩\|²) / Z cancels identically for any function g — the equatorial plane is a geometric null point for the entire overlap-only class. We propose a phenomenological null test: a single waveplate tilts the Bong et al. (2020) apparatus to θ = 31°, providing the first isolated test of this class, with sensitivity β ≥ 0.07 at 5σ (single-setting) while preserving 8.6σ Genuine LF violation, under fair-sampling (η ≈ 0.87; closure via SNSPD upgrade to η ≥ 0.91)." | 4.6/5 | Combined fix for issues 1 (claims), 5 (overload), 6 (scope). Theorem leads; "phenomenological null test" explicitly names the paper's genre; S1 qualifier and "three lines" detail moved to §1 where they belong. Abstract now does one job: sell the paper. C9 (3-beat structure) preserved — theorem + proposal + consequence. |
| 2 | §2.3 | **GPT/weak-measurement stripped (−10 lines):** Removed: "We define a single-parameter deformation...Within the GPT framework [17]...state-effect duality derivation and information-geometric motivation in Supplemental S3" + "Physically, β functions as a registration-memory coupling strength...connection to weak measurement formalism [18] developed in Supplemental S3" + "Conceptually, basis overlap \|⟨b\|d⟩\|² quantifies measurement-context compatibility...GPT state-effect duality [17]; weak measurement precedent [18]; further development in Supplemental S3" + "The model-independent theorem (Proposition 1, §3) is the central result; Eq. (2-3) serves as a benchmark parametrization." Kept: theorem lead → constraints derivation → EFT/SME analogy. | 4.7/5 | v43 cut GPT ~40% (9→4 lines conceptual chain). This cut removes the remaining ~60% — all GPT framework, registration-memory coupling, weak measurement connection, and context-compatibility chain. The overlap-only class is now motivated by geometry (theorem constrains it) and operational simplicity (EFT analogy), not by speculative physical mechanism. C10 (benchmark parametrization) and C17 (detail→S3) preserved. |
| 3 | §8 | **§8.1+§8.2 merged (−8 lines):** Old: Two subsections — §8.1 "Interpretation of Results" (7 lines) and §8.2 "Interpretation and Model Context" (7 lines). New: Single §8.1 "Interpretation" (7 lines): δ≠0 interpretation + null result + "Implications for major quantum interpretations are analyzed in Supplemental S3; the experiment is interpretation-neutral by design." Removed: "Neither the interpretations nor the embedding predict or preclude the class Eq. (2-3)" (defensive), explicit enumeration of interpretations, redundant "at this previously untested geometry." §8.3 "Future Directions" → §8.2. | 4.6/5 | For a ~5-page paper, two interpretation subsections is one too many. The merged version states what the experiment shows (operational), then points to S3 for model context. |
| 4 | §1 | **Novelty reframed around unisolated control parameter (+2 lines net):** Old: "This structural non-identifiability has not previously been remarked because...The proof is three lines of Bloch-sphere algebra (§3.3); §2 provides motivation and notation." New: "The novelty is not the overlap formula itself (three lines of Bloch-sphere algebra, §3.3) but the recognition that the polar angle θ has never been isolated as an independent control parameter in actual EWF implementations: LF inequalities are optimized precisely at equatorial settings [2,10], so researchers adopted θ = π/2 as standard without a specific hypothesis motivating polar tilt. The equator is therefore an accidental fixed point — a geometric null point for the entire overlap-only class that has remained structurally untested." | 4.6/5 | Directly preempts "trivial symmetry" reviewer reflex: the paper openly acknowledges the math is 3 lines of algebra, then states the novelty is experimental (identifying an unisolated parameter), not mathematical (discovering a new formula). "Accidental fixed point" rebrands the equatorial convention as historical accident — the null point was not chosen; it was the default. |

### Structural changes (v53)
| Before (v52) | After (v53) | Nature |
|-------------|-------------|--------|
| Abstract: 13 lines (S1 qualifier + theorem + experiment + consequence) | 8 lines (theorem → phenomenological null test → measurable consequence) | Compression + genre |
| §1 ¶2: "This structural non-identifiability has not previously been remarked because...The proof is three lines of Bloch-sphere algebra (§3.3); §2 provides motivation and notation." | "The novelty is not the overlap formula itself (three lines of Bloch-sphere algebra, §3.3) but the recognition that the polar angle θ has never been isolated...The equator is therefore an accidental fixed point" | Novelty reframe |
| §2.3 Core idea: ~22 lines (theorem lead + GPT framework + registration-memory coupling + weak measurement + context-compatibility chain + EFT analogy) | ~12 lines (theorem lead + constraints derivation + EFT analogy) | GPT/weak-measurement stripped |
| §8: §8.1 "Interpretation of Results" (7 lines) + §8.2 "Interpretation and Model Context" (7 lines) + §8.3 "Future Directions" | §8.1 "Interpretation" (7 lines merged) + §8.2 "Future Directions" | Merge + renumber |
| §1: (§8.3) cross-ref | (§8.2) cross-ref | Updated |
| §2.3: (§8.3) cross-ref | (§8.2) cross-ref | Updated |
| §3.1: (§5.3, §8.4) cross-ref | (§5.3, §7) cross-ref | Stale ref fixed |
| §5.3: (§8.3) cross-ref | (§8.2) cross-ref | Updated |

### Regression
Δ: C3 S1 qualifier moved from Abstract to §1 (stronger placement — directly in ESP paragraph); C9 Abstract evolved from 3-beat to tighter 3-beat (theorem+proposal+consequence, each single-purpose); C10 benchmark language retained; C17 strengthened (more GPT/weak-measurement detail → S3).

---

## v52 (2026-05-25) — 10-point review RCA (threshold 4.5/5): de-defensify — trimmed 2 redundant "model-independent", tightened ESP paragraph

**Scoring summary (10 points):** 1 implemented (≥4.5/5), 9 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β ad-hoc — push theorem to main claim harder | — | → Recurring |
| 2 | Intro too long — cut 25-30% | — | → Recurring |
| 3 | Repeated disclaimers — consolidate | 4.2/5 | Rejected — hedges functionally placed |
| 4 | "Just basis reparameterization" | — | → Recurring |
| 5 | §3 too dense — split theorem/intuition/scope | 4.0/5 | Rejected — labeled blocks within §3.2 already provide structure |
| 6 | Novelty vs contextuality unclear | — | → Recurring |
| 7 | "first" claim dangerous | — | → Recurring |
| 8 | Missing killer figure — Bloch sphere | — | → Recurring |
| 9 | Stats overkill — move more to supplement | 3.0/5 | Rejected — §6 just compressed 30→13 lines (v51) |
| 10 | No physical mechanism | — | → Recurring |
| — | **Paper feels defensive** — trim redundant hedges | 4.5/5 | **Implemented** — 2 "model-independent" removed + ESP tightened |

### Implemented change (v52)

**De-defensify — 3 surgical trims:**

| Location | Before | After | Why |
|----------|--------|-------|-----|
| §3.1 | "This result is model-independent: it depends only on Bloch sphere geometry." | "This depends only on Bloch sphere geometry." | "Model-independent" is a defensive label; "depends only on Bloch sphere geometry" already conveys the same fact positively |
| §7 | "this is model-independent regardless of loophole status" | "this holds regardless of loophole status" | Same — the fact (holds regardless) is stated; the label is redundant |
| §1 ¶4 (ESP) | 5 lines: "This paper does not claim that overlap-dependent deformation exists in nature. It claims that (A) within currently surveyed optical EWF implementations (Supplemental S1), equatorial measurement has left the overlap-only class structurally untested — equatorial geometry is a convention for LF optimization, not a tested constraint on overlap-dependent physics — and (B) a single waveplate enables the first isolated experimental probe of this class. A positive result would require independent verification including θ-sweeps (§8.3)." | 5 lines: "This paper makes no claim about the existence of overlap-dependent deformation in nature. Its two claims are structural: (A) within surveyed optical EWF implementations (Supplemental S1), equatorial measurement — a convention for LF optimization, not a tested constraint — leaves the overlap-only class structurally untested, and (B) a single waveplate enables the first experimental probe. Positive results require independent verification including θ-sweeps (§8.3)." | More direct: "makes no claim about" is matter-of-fact vs "does not claim that...exists" (defensive). "Its two claims are structural:" positively frames what the paper DOES claim. Fewer words, less negation, same C1 substance. |

**RCA:** 4.5/5. The paper accumulated hedges across 38 versions — each individually justified (C1-C21), but collectively creating a tone of "anticipating reviewer attack." This change removes 2 redundant "model-independent" labels (the underlying facts are stated without the defensive wrapper) and tightens the ESP paragraph to be more direct while preserving the C1 boundary. "Model-independent" still appears 3 times where functional (§1, §5.2 table, §2.3). Net: paper reads as confident rather than preemptively defensive.

### Regression
Δ: C1 ESP + C3 S1 qualifier retained.

---

## v51 (2026-05-25) — 6-point review RCA (threshold 4.5/5): β-model subordinated to theorem (§2.3), "minimal operational benchmark" (§2.3), "first"→"new" window (§9), §6 compressed 30→13 lines

**Scoring summary (6 points):** 4 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β-model overshadows theorem — push theorem + geometry to center | 4.6/5 | **Implemented** — theorem-subordinating lead sentence in §2.3 |
| 2 | "first experimental window" overclaim — soften | 4.6/5 | **Implemented** — "first"→"new" + S1 qualifier in §9 |
| 3 | Stats/systematics too long — move to supplement | 4.7/5 | **Implemented** — §6 compressed 30→13 lines |
| 4 | "Trivial geometry" — emphasize historical reason | 3.5/5 | Rejected — already in §1 ¶2 (v45) + §3.5 |
| 5 | Verbose, lặp ý — cut 25-30% | 3.5/5 | Rejected — already lean; no large removable blocks remain |
| 6 | Eq.(2) ad-hoc — "toy operational benchmark" | 4.7/5 | **Implemented** — "minimal operational benchmark" language in §2.3 |

### Implemented changes (v51)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 1+6 | §2.3 | **Theorem subordination + "minimal operational benchmark" (+3 lines)**: New lead sentences: "The equatorial cancellation theorem (§3) constrains every overlap-dependent deformation independent of parametrization — it holds for any function g(\|⟨b\|d⟩\|²). The following minimal operational benchmark serves only to quantify experimental sensitivity for one concrete parametrization." Also removed "EFT-style" from the opening (kept in the SME analogy later). | The §2.3 "Core idea" previously opened with "We define an EFT-style benchmark parametrization..." — the model led, the theorem followed. Now the theorem leads: the model is explicitly subordinated as a sensitivity-quantification tool, not the paper's intellectual center. "Minimal operational benchmark" (instead of "EFT-style benchmark parametrization") signals simplicity and operational focus — harder to attack as "ad-hoc" when the paper itself calls it minimal. |
| 2 | §9 | **"first"→"new" + S1 qualifier**: "would open the first experimental window onto overlap-dependent physics in EWF scenarios" → "would open a new experimental window onto overlap-dependent physics in EWF scenarios — a geometric sector that, within surveyed implementations (Supplemental S1), has not previously been probed." | "First" is an absolute claim even in a forward-looking sentence. "New" is a relative claim — the window is new relative to existing experiments. The added S1 qualifier explicitly bounds the "not previously probed" claim. |
| 3 | §6 | **Statistical Analysis compressed 30→13 lines (−17 lines)**: (a) Monte Carlo paragraph compressed from 3 lines to 1: key numbers preserved (99.97%, >99%, ~90%). (b) "Statistical model limitations" (9 lines) + "Bayesian robustness" (11 lines) merged into 3 compact lines: "A conservative Bayesian analysis inflating Poisson uncertainties by 20% yields β_min ≈ 0.046 (combined); the FOM plateau...ensures viability under substantial systematic degradation. Detailed Monte Carlo, correlated-drift modeling, and fake-signal injection methodology are provided in Supplemental S2." All technical detail preserved in S2 pointer. | §6 at 30 lines was proportionally heavy for a paper whose core contribution is a 3-line geometric proof. The compression preserves every key number (N_min, 99.97%, β=0.07>99%, β_min≈0.046) while moving implementation methodology to S2 where referees can verify it. |

### Structural changes (v51)
| Before (v50) | After (v51) | Nature |
|-------------|-------------|--------|
| §2.3 lead: "**Core idea.** We define an EFT-style benchmark parametrization..." | "**Core idea.** The equatorial cancellation theorem (§3) constrains every overlap-dependent deformation independent of parametrization...The following minimal operational benchmark serves only to quantify experimental sensitivity..." | Theorem subordination |
| §6: 30 lines (Poisson + Monte Carlo + Limitations + Bayesian) | 13 lines (Poisson + compressed Monte Carlo/Bayesian + S2 pointer) | Compression |
| §9: "first experimental window" | "a new experimental window...within surveyed implementations (Supplemental S1)" | Soften + S1-qualify |

### Regression
Δ: C3 S1 extended to §9; C10 refined "minimal operational benchmark".

---

## v50 (2026-05-25) — 5-point review RCA (threshold 4.5/5): Abstract "geometric null point", φ-scramble forward-ref (§4.2), Conclusion call-to-action, §8.1 logic fix (+ v49 §2.3 merge)

**Scoring summary (5 points):** 4 implemented (≥4.5/5), 1 rejected (<4.5/5). Plus 2 self-audit fixes from v49.

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Abstract thiếu "geometric null point" | 4.5/5 | **Implemented** — "structurally insensitive" → "sit at a geometric null point" |
| 2 | §2.3 defense language trim more | 4.0/5 | Rejected — already minimal after v43/v49 compressions |
| 3 | Lemma 1 "no-go" wording rõ hơn | 4.2/5 | Rejected — operational invariant already: "No basis redefinition...can generate this signal" |
| 4 | φ-scramble control lên gần experimental proposal | 4.6/5 | **Implemented** — forward-ref added to §4.2 |
| 5 | Conclusion yếu, không call-to-action | 4.7/5 | **Implemented** — "no new technology required" closing sentence |
| — | §8.1 logic error (self-audit) | 4.8/5 | **Fixed** — "confirms cos θ dependence" removed (null result can't confirm what it fails to find) |
| — | §2.3 double "Equation (2)" (v49 self-audit) | 4.5/5 | Fixed in v49, rolled into v50 |

### Implemented changes (v50)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| 1 | Abstract | "so published implementations are structurally insensitive to the entire overlap-only class" → "so published implementations sit at a geometric null point for the entire overlap-only class" | "Structurally insensitive" is accurate but flat. "Geometric null point" (v48, now propagated to Abstract) is visceral — the reader instantly visualizes all experiments clustered at a single point where the signal vanishes. Same truth value, stronger hook. |
| 2 | §4.2 | After QWP description: +"A φ-scramble control (§7) randomizes the azimuthal angle to rule out birefringence artifacts without additional optics." | The φ-scramble (§7, v43) is one of the paper's strongest experimental controls but was invisible until the robustness section. One line in §4.2 tells experimentalists up front: "we've thought about the obvious artifact, and the control is free." |
| 3 | §9 | After "across published EWF implementations": +"The experiment requires no new technology — only re-insertion of an existing waveplate — and would open the first experimental window onto overlap-dependent physics in EWF scenarios." | The old conclusion restated results and stopped. The new closing sentence converts the paper's core pragmatic argument (one existing waveplate) into a forward-looking call to action. "No new technology" + "first experimental window" = low barrier, high impact. |
| 4 | §8.1 | "and confirms the cos θ dependence" → "at this previously untested geometry" | Logic error: a null result (δ≈0) excludes the cos θ signal; it cannot simultaneously "confirm" it. The corrected phrasing states the geometric fact (previously untested) without claiming confirmation of the null hypothesis. |

### Regression
Δ: C3 S1 + C9 Abstract structure preserved.

---

## v49 (2026-05-25) — RCA audit (threshold 4.5/5): §2.3 double "Equation (2)" sentence start merged

(Superseded — rolled into v50)

---

## v48 (2026-05-25) — 6-point review RCA (threshold 4.5/5): "geometric null point" hook in §1 ¶2

**Scoring summary (6 points):** 1 implemented (≥4.5/5), 5 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | β ad-hoc — derive from toy physical model | — | → Recurring |
| 2 | Basis rotation objection | — | → Recurring |
| 3 | Overlap-only class unmotivated | — | → Recurring |
| 4 | Theorem strong but physics weak — "blind spot" language | 3.0/5 | Rejected — "blind spot" deliberately removed v37 |
| 5 | Paper too long/defensive — cut 20-30% | — | → Recurring |
| 6 | "Why should anyone care?" — "geometric null point" | 4.5/5 | **Implemented** — "null point" added to §1 ¶2 |

### Implemented change (v48)

**§1 ¶2: "fixed point" → "geometric null point"**: "The equator is therefore a fixed point of every overlap-only deformation" → "The equator is therefore a geometric null point for every overlap-only deformation." One phrase change.

| RCA Score | Rationale |
|-----------|-----------|
| 4.5/5 | "Fixed point" is the mathematical term (Banach, Brouwer — heavy topological connotation for a 3-line algebraic proof). "Geometric null point" is the narrative term — visceral, visual, immediately conveys "signal vanishes here." The metaphor was introduced in v37 (§3.6: "may have unknowingly operated exactly at a geometric null point") but was buried in the ESP paragraph. Moving it to §1 ¶2 — directly in the Proposition 1 framing — makes it the paper's hook. Reviewer understands immediately: "every EWF experiment sits at a null point → that's why nobody saw this → one waveplate breaks out." |

### Structural changes (v48)
| Before (v47) | After (v48) | Nature |
|-------------|-------------|--------|
| §1 ¶2: "fixed point of every overlap-only deformation" | "geometric null point for every overlap-only deformation" | Narrative hook |

### Regression

---

## v47 (2026-05-25) — RCA audit (threshold 4.5/5): §9 C3 regression fix, §5.3 null-result dedup, §8.4→§8.3 renumber

Self-audit round — no user suggestions. Three issues identified and fixed via RCA.

| # | Issue | RCA Score | Action |
|---|-------|-----------|--------|
| A | §9 "across every published EWF implementation" — no S1 qualifier (C3 regression) | 4.8/5 | **Fixed** |
| B | §5.3 duplicate null-result paragraph ("A null result at β≥0.04 excludes...") | 4.7/5 | **Deduped** |
| C | §2.3 "Equation (2) is a benchmark... Equation (2) should be viewed..." — consecutive sentences both start with "Equation (2)" | 4.3/5 | Rejected (below threshold; minor style) |
| D | §8 numbering gap: §8.2→§8.4, missing §8.3 (from v35 merge) | 4.5/5 | **Renumbered** |

### Changes (v47)

| # | Section | Change | Rationale |
|---|---------|--------|-----------|
| A | §9 | "across every published EWF implementation" → "within the surveyed literature (Supplemental S1), has remained unprobed across published EWF implementations" | C3 regression: v34+v38 applied S1 qualifier to 5 locations but §9 last sentence was missed. "Every published" without S1 qualifier is an absolute claim vulnerable to one counterexample. |
| B | §5.3 | Merged two redundant paragraphs: "The coupling β has no a priori theoretical prediction...A null result at β ≥ 0.04 excludes..." + "A null result at β ≥ 0.04 excludes O(1) and O(10⁻¹)..." → single paragraph combining SME analogy + exclusion claim + N=200k extension. (−3 lines) | Two consecutive paragraphs said essentially the same thing with different wording. The first had the SME analogy and theory-construction framing; the second had O(1)/O(10⁻¹) quantitative claim and N=200k extension. Merged. |
| D | §8 | Renumbered §8.4→§8.3 (Future Directions). Updated 4 cross-references: (§8.4)→(§8.3) in §1, §2.3, §3.1, §5.3. | v35 merged §8.2+§8.3 into "Interpretation and Model Context" but left §8.4 as-is, creating a numbering gap (§8.1, §8.2, §8.4). Looks like an error to reviewers. |

### Regression
Δ: C3 repaired in §9.

---

## v46 (2026-05-25) — 8-point review RCA (threshold 4.5/5): Lemma 1 moved §3.4→§3.2 (adjacent to Proposition 1), §3.5→§3.4 + §3.6→§3.5 renumber

**Scoring summary (8 points):** 1 implemented (≥4.5/5), 6 rejected (<4.5/5), 1 N/A (supplemental files).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Motivation class weak — add symmetry/no-go argument | 4.3/5 | Rejected — constraints (i)-(iii) + Taylor expansion already provide the mathematical structure |
| 2 | Claim overgeneralized — "within overlap-only class" | — | → Recurring |
| 3 | Supplemental overloaded with philosophy | N/A | Out of scope — supplemental files (S3) |
| 4 | Ad-hoc phenomenology — SME/EFT analogy | — | → Recurring |
| 5 | Significance aggressive — add conservative estimate | — | → Recurring |
| 6 | Theorem buried — Proposition 1 + Figure even earlier | 2.5/5 | Rejected — v45 already put Proposition 1 on page 1 |
| 7 | Missing killer prediction — θ-sweep cosθ as smoking gun | 3.0/5 | Rejected — violates C20 |
| 8 | "Just basis rotation?" — Lemma 1 closer to theorem | 4.6/5 | **Implemented** — Lemma 1 moved from §3.4 to §3.2 |

### Implemented changes (v46)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.2, §3.4, §3.5 | **Lemma 1 relocated §3.4→§3.2**: Lemma 1 (Non-Absorption) + operational invariant moved from standalone §3.4 into §3.2, placed between Corollary and Scope limitation. Old §3.4 removed; §3.5→§3.4 (Physical Intuition), §3.6→§3.5 (Unisolated Geometric Control Parameter). Cross-references updated: 2 instances of "Lemma 1 (§3.4)" → "Lemma 1 (§3.2)". | 4.6/5 | The "just basis rotation" objection is the single most common reviewer reflex. v41 added a forward-ref from §3.1 to §3.4, but the actual defense remained 2 subsections away from the theorem it defends. With Lemma 1 in §3.2 (immediately after Proposition 1 + Corollary), the defense is physically adjacent: reader sees theorem → corollary → "and this signal cannot be absorbed by basis redefinition" → scope → examples. The operational invariant ("No basis redefinition of the Superobserver alone can generate this signal") now sits directly under Proposition 1, making the no-go explicit at the point of maximum reviewer skepticism. No content changed — pure structural repositioning. |

### Structural changes (v46)
| Before (v45) | After (v46) | Nature |
|-------------|-------------|--------|
| §3.2: Definition → Proposition 1 → Corollary → Scope → Examples → Contextuality | Definition → Proposition 1 → Corollary → **Lemma 1 + operational invariant** → Scope → Examples → Contextuality | Lemma 1 moved in |
| §3.4: Lemma 1 (Non-Absorption) | Removed (content now in §3.2) | Section deleted |
| §3.5: Physical Intuition | §3.4: Physical Intuition | Renumbered |
| §3.6: Unisolated Geometric Control Parameter | §3.5: Unisolated Geometric Control Parameter | Renumbered |
| §3.1: "Lemma 1 (§3.4) proves..." | "Lemma 1 (§3.2) proves..." | Cross-ref updated |
| §5.3: "(see also Lemma 1, §3.4)" | "(see also Lemma 1, §3.2)" | Cross-ref updated |

### Regression
Δ: C18 Lemma 1 repositioned to §3.2.

---

## v45 (2026-05-25) — 10-point review RCA (threshold 4.5/5): Proposition 1 on page 1 (§1 restructured), historical reason for unvaried θ (§1), intro compressed 53→42 lines (−21%)

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overclaim — reduce "first", "entire class" | — | → Recurring |
| 2 | Too much hype — cut 25-30% rhetoric | — | → Recurring |
| 3 | Theorem looks trivial — emphasize structural non-identifiability | — | → Recurring |
| 4 | Overlap-only class lacks physical motivation — add toy model | — | → Recurring |
| 5 | Experimental claims strong — move σ-results to Supplement | 4.0/5 | Rejected — β≥0.07 at 5σ and 8.6σ LF are the paper's operational claims |
| 6 | Intro too long — get to theorem sooner | 4.5/5 | **Implemented** — §1 restructured; Proposition 1 in ¶2 |
| 7 | "cos θ" repeated too much | 4.2/5 | Rejected — functional repetition |
| 8 | "Why not known already?" — add historical reason | 4.6/5 | **Implemented** — historical reason in §1 ¶2 |
| 9 | GPT/contextuality diffuse — cut more from main text | — | → Recurring |
| 10 | Main contribution buried — Proposition 1 on page 1 | 4.7/5 | **Implemented** — Proposition 1 formally stated in §1 ¶2 |

### Implemented changes (v45)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **§1 full restructure (53→42 lines, −21%)**: (a) ¶1 EWF background compressed 6→4 lines. (b) ¶2 Proposition 1 formally stated: Definition + proof sketch + structural non-identifiability consequence + historical reason ("LF inequalities optimized at equator [2,10]; without hypothesis motivating polar tilt, θ remained unisolated") + "three lines of Bloch-sphere algebra" complexity note. (c) ¶3 experimental consequence: one QWP, β≥0.07 at 5σ, 8.6σ LF, fair-sampling, SNSPD. (d) ¶4 ESP boundary compressed 8→5 lines. (e) ¶5 supplemental roadmap compressed 5→2 lines. Removed: Claim A/B labeling (redundant with §3/§4 headers), verbose "here overlap-dependent means..." definition (now in Proposition 1 Definition), separate "geometric insight" / "compact result" paragraphs (folded into ¶2). | 4.7/5 | The paper's strongest asset (Proposition 1) was buried on page 3 while §1 spent 20 lines on motivation and framing before reaching the theorem. v44 reframed novelty but left the theorem statement in §3. This restructure puts the formal theorem — Definition, statement, proof sketch, consequence — directly in §1 ¶2. Reviewer sees the mathematical core immediately. Historical reason ("LF optimization selects equator") preempts "why wasn't this noticed?" — factual, non-accusatory, cites [2,10]. Combined implementation of #6 (compact intro), #8 (historical reason), #10 (Prop 1 on page 1). |

### Structural changes (v45)
| Before (v44) | After (v45) | Nature |
|-------------|-------------|--------|
| §1: 53 lines, 6 paragraphs (EWF bg → structural consequence → Claim A/B → compact result → ESP → supplemental) | 42 lines, 5 paragraphs (EWF bg → **Proposition 1 formal statement** + historical reason → experimental consequence → ESP → supplemental) | Restructure: theorem front-loaded |
| §1 ¶2: "Every published optical EWF...This paper identifies the structural consequence...meaning existing implementations are structurally insensitive...Here 'overlap-dependent' means..." | "**Proposition 1 (Equatorial Cancellation Theorem, §3).** A deformation...is *overlap-only* if...At θ=π/2...P'=P_QM identically...structural non-identifiability...historical reason...three lines of Bloch-sphere algebra." | Formal theorem on page 1 |
| §1 ¶3-4: "The equatorial cancellation (Claim A)..." + "The geometric result itself is compact..." | Merged into ¶2 (theorem statement) + ¶3 (experimental consequence) | Paragraph consolidation |
| §1 ¶5 (ESP): 8 lines | 5 lines: "within currently surveyed...equatorial measurement has left the overlap-only class structurally untested" | ESP compression |
| §1 ¶6 (Supplemental): 5 lines with full descriptions | 2 lines: "S1 (literature search + algebraic proof), S2 (numerical methods + statistical robustness), S3 (interpretations + GPT/weak-measurement development)" | Supplemental compression |
| Claim A/B labels in §1 | Removed — §3 and §4 headers retain labels; no cross-references broken | De-duplication |

### Regression
Δ: C1+C3 preserved; C8 strengthened (formal Prop 1 in §1).

---

## v44 (2026-05-25) — 10-point review RCA (threshold 4.5/5): structural non-identifiability novelty reframe (§1), contextuality distinction (§3.2), experimental feasibility softening (§4.5)

**Scoring summary (10 points):** 4 implemented (≥4.5/5), 6 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1+10 | Novelty weak + theorem buried — reframe as structural non-identifiability | 4.5+4.6/5 | **Implemented** — combined reframe in §1 |
| 2 | Eq.(2) ad-hoc → emphasize benchmark EFT parametrization | — | → Recurring |
| 3 | "all experiments blind" → "all surveyed optical EWF" | — | → Recurring |
| 4 | Paper too long → cut 20-30% | — | → Recurring |
| 5 | Weak measurement/GPT → push nearly all to Supplemental | — | → Recurring |
| 6 | Signal vs ordinary contextuality → add subsection | 4.7/5 | **Implemented** — contextuality distinction added to §3.2 |
| 7 | "first isolated test" → redundant epistemic hedging | — | → Recurring |
| 8 | Experimental feasibility optimistic → soften | 4.5/5 | **Implemented** — §4.5 softened |
| 9 | Abstract overloaded → simplify further | 3.5/5 | Rejected — v42 already compressed to 3-sentence 1+1+1 structure |
| 10 | Center paper around theorem → merged with #1 | — | See #1 |

### Implemented changes (v44)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **Novelty reframe: geometric→structural, not algebraic→historical (+4 lines)**: "The novelty is geometric, not algebraic: a Bloch-sphere degree of freedom not previously isolated..." → "The novelty is structural, not historical: the equatorial plane is a fixed point where every overlap-dependent deformation vanishes identically — equatorial measurements are structurally incapable of distinguishing standard QM from any member of the overlap-only class, regardless of statistical precision or experimental design. Proposition 1 is therefore the paper's central result; the experimental protocol (§4-7) is its direct operational consequence." | 4.6/5 | The original framing ("geometric, not algebraic" + "not previously isolated") anchored novelty in historical priority — claiming nobody varied θ before. This is vulnerable to literature-search challenges. The structural framing anchors novelty in the theorem itself: equatorial measurements CANNOT detect overlap-dependence, regardless of who did what when. This is immune to citation challenges because it's a mathematical fact, not a historical claim. Explicitly naming Proposition 1 as "the paper's central result" centers the theorem (per #10). Combined implementation: #1 provides the framing, #10 provides the emphasis. |
| 2 | §3.2 | **Contextuality distinction (+8 lines)**: After Examples, added labeled block "**Contextuality distinction.**": "Standard quantum contextuality (Kochen-Specker, Bell-KS) concerns the dependence of measurement outcome distributions on which compatible observables are measured jointly — a property of the measurement *setting*. Overlap-only deformation concerns a different structure: the dependence of Superobserver statistics on the geometric relationship between the Superobserver's basis and a prior observer's recorded outcome — a property of the measurement *registration*. The two are logically independent...Proposition 1 constrains the latter; it is silent on ordinary KS contextuality." | 4.7/5 | This is a genuine gap. No previous version addressed the reviewer objection "isn't this just standard contextuality?" The distinction is clean: KS contextuality = setting-dependence (which observables measured together); overlap-dependence = registration-dependence (how prior outcome conditions subsequent statistics). "Logically independent" + "silent on KS contextuality" sets clear boundaries without claiming superiority. The GPT citation [17] provides the formal framework for this distinction but never stated it explicitly. |
| 3 | §4.5 | **Feasibility softening**: "yield a complete run of approximately one hour. Source and detector drift are sub-dominant to Poisson uncertainty over this timescale" → "would require a data-acquisition run of approximately one hour under Bong et al. conditions, assuming source and detector stability over this timescale. Practical feasibility depends on the specific apparatus" | 4.5/5 | "Yield" implies certainty; "would require" states a conditional estimate. "Sub-dominant to Poisson uncertainty" is a claim about a specific apparatus the authors don't control; "assuming stability" is honest about the assumption. "Practical feasibility depends on the specific apparatus" acknowledges experimental variability and defers to the implementing lab. |
| 4 | §3.1 | **Minor alignment**: "geometric insight" → phrasing preserved; the Claim A/B paragraph already aligns with structural framing (v39: "geometric insight — a mathematical consequence of Bloch-sphere geometry requiring no experimental assumptions"). No edit needed — the v39 framing was already structural; v44 §1 now matches. | — | Consistency check. |

### Structural changes (v44)
| Before (v43) | After (v44) | Nature |
|-------------|-------------|--------|
| §1: "The novelty is geometric, not algebraic: a Bloch-sphere degree of freedom not previously isolated as an independent control parameter, with a single-waveplate operational consequence." | "The novelty is structural, not historical: the equatorial plane is a fixed point where every overlap-dependent deformation vanishes identically — equatorial measurements are structurally incapable of distinguishing standard QM from any member of the overlap-only class, regardless of statistical precision or experimental design. Proposition 1 is therefore the paper's central result; the experimental protocol (§4-7) is its direct operational consequence." | Novelty reframe + theorem centering |
| §3.2: Ends at "The cancellation is universal." then §3.3 Proof | +"**Contextuality distinction.** Standard quantum contextuality (Kochen-Specker, Bell-KS) concerns...Proposition 1 constrains the latter; it is silent on ordinary KS contextuality. A theory exhibiting KS contextuality need not exhibit overlap-dependence, and conversely." | New defense |
| §4.5: "yield a complete run...drift are sub-dominant to Poisson uncertainty" | "would require a data-acquisition run of approximately one hour under Bong et al. conditions, assuming source and detector stability over this timescale. Practical feasibility depends on the specific apparatus" | Feasibility softening |

### Regression
Δ: C1+C3 intact; C8 reframed structural; C6 GPT→contextuality link.

---

## v43 (2026-05-25) — 10-point review RCA (threshold 4.5/5): GPT/weak-measurement §2.3 cut ~40%→S3, φ-scramble control experiment (§7), §5.1 correlator table→S2

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "first isolated test" → redundant hedging | — | → Recurring |
| 2 | GPT/weak measurement §2.3 too long/speculative — cut ~40%→S3 | 4.6/5 | **Implemented** — v42 conceptual chain compressed 9→4 lines |
| 3 | β definition ad hoc | — | → Recurring |
| 4 | "equatorial cancellation" repeated too much | 4.0/5 | Rejected — functional signposting, not wasteful echo |
| 5 | Add Bloch sphere figure | — | → Recurring |
| 6 | Systematic fake cosθ — φ-scramble control experiment | 4.6/5 | **Implemented** — added to §7 |
| 7 | "All published" → "within surveyed optical EWF" | — | → Recurring |
| 8 | §5 too many numbers — move tables to supplement | 4.6/5 | **Implemented** — §5.1 correlator table→S2 |
| 9 | Lemma 1 triết học wording → operational hơn | — | → Recurring |
| 10 | Abstract overloaded — giảm GPT/contextuality jargon | 2.0/5 | Rejected — v42 abstract already zero GPT/contextuality |

### Implemented changes (v43)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **GPT/weak-measurement cut ~40% (−5 lines)**: v42 9-line conceptual chain ("Conceptually, once measurement statistics are recognized as context-dependent — as formalized in GPT's state-effect duality on convex operational space [17] — the basis overlap...The weak measurement formalism [18] provides an established physical precedent: postselection-conditioned outcomes depend on...") compressed to 4 lines: "Conceptually, basis overlap \|⟨b\|d⟩\|² quantifies measurement-context compatibility — a natural element in any framework where measurement outcomes are context-dependent (GPT state-effect duality [17]; weak measurement precedent [18]; further development in Supplemental S3)." | 4.6/5 | v42 conceptual chain was 9 lines developing GPT state-effect duality + weak measurement precedent in main-text prose. User correctly identified this as speculative-feeling — reads as the paper arguing for a physical mechanism rather than parametrizing a search class. Compressed version keeps the key conceptual hook (overlap = context-compatibility) while moving development to S3. C17 preserved (detail→S3). |
| 2 | §7 | **φ-scramble control experiment (+7 lines)**: New paragraph after systematic-error budget: randomize azimuthal φ while keeping θ fixed. Overlap-dependent signal depends only on θ (f_perp difference = −cos θ, φ-independent since \|e^{iφ}\|² = 1). Birefringence couples to both θ and φ via Jones matrix. If δ⟨AB⟩ persists under φ-randomization, origin is geometric not birefringent. No additional optical elements needed — only HWP angle randomization. | 4.6/5 | Experimentalist's first question: "couldn't birefringence fake this?" The systematic-error budget already listed birefringence <0.1° but didn't provide a positive control. φ-scramble exploits the core geometric fact (§3.3: φ drops out of f_perp) to create a zero-cost discriminator between geometric signal and birefringence artifact. Concrete, implementable, theory-independent. |
| 3 | §5.1 | **Correlator table→S2 (−7 lines)**: Full 9-value correlator table replaced with compact prose: "All nine ⟨A_x B_y⟩ correlators are tabulated in Supplemental S2. Key values: ⟨A₁B₁⟩ = −1.0000 (z-basis, perfect anti-correlation); mixed-setting correlators range from ⟨A₂B₂⟩ = −0.5045 to ⟨A₂B₃⟩ = ⟨A₃B₂⟩ = −0.8933, all with σ ≈ 0.0017 at N = 91,000. The four mixed-setting pairs share identical \|⟨AB⟩\| up to φ-induced sign, since f_perp depends only on θ." | 4.6/5 | PRA main text at ~5 pages should not carry full 9-entry numerical tables. Key values (range endpoints, best/worst precision) preserved in prose; full table in S2 for referees. Also adds structural observation (4 mixed-setting pairs identical up to φ sign) that was implicit in the table but never stated. |

### Structural changes (v43)
| Before (v42) | After (v43) | Nature |
|-------------|-------------|--------|
| §2.3: 9-line conceptual chain (GPT state-effect duality + weak measurement precedent developed in prose) | 4-line compact: "Conceptually, basis overlap \|⟨b\|d⟩\|² quantifies measurement-context compatibility — a natural element in any framework where measurement outcomes are context-dependent (GPT [17]; weak measurement [18]; further development in Supplemental S3)." | Cut ~55%, S3 pointer |
| §7: Systematic-error budget ended at "deferred to implementing laboratory." | +"**φ-scramble control.** A birefringence artifact in the QWP could produce θ-dependent efficiency variation...This control requires no additional optical elements — only randomization of the HWP angle controlling φ." | Control experiment |
| §5.1: 11 lines (1 intro + 5-row table + 1 footer) | 6 lines (compact prose with key numbers + S2 pointer) | Table→supplement |
| §5.1 heading: unchanged | unchanged | — |

### Regression
Δ: C6, C10, C12, C17 intact; C17 strengthened (more detail→S3).

---

## v42 (2026-05-25) — 5-point review RCA (threshold 4.5/5): GPT-contextuality conceptual chain (§2.3), Lemma 1 operational invariant (§3.4), β weak-measurement scale bridge (§5.3), Abstract 1+1+1 compression

**Scoring summary (5 points):** 4 implemented (≥4.5/5), 1 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Overlap-only class looks ad hoc — connect to GPT/contextuality/weak measurement | 4.6/5 | **Implemented** — conceptual chain added to §2.3 |
| 2 | Lemma 1 too weak — add operational invariant / no-go statement | 4.7/5 | **Implemented** — operational invariant added to §3.4 |
| 3 | β lacks natural scale — add theoretical prior / toy model | 4.5/5 | **Implemented** — weak-measurement scale bridge (+3 lines §5.3) |
| 4 | Abstract too long and defensive — compress to 1+1+1 | 4.6/5 | **Implemented** — Abstract restructured to insight+experiment+consequence |
| 5 | Paper covering too much — reduce philosophy/coverage | 3.5/5 | Rejected — §8.2 already 5-line S3 pointer (v35); no remaining philosophy to cut |

### Implemented changes (v42)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **GPT-contextuality conceptual chain (+3 lines)**: After "independently of this physical picture," added: "Conceptually, once measurement statistics are recognized as context-dependent — as formalized in GPT's state-effect duality on convex operational space [17] — the basis overlap \|⟨b\|d⟩\|² is not an ad hoc choice but the simplest scalar quantifying measurement-context compatibility between successive measurements. The weak measurement formalism [18] provides an established physical precedent: postselection-conditioned outcomes depend on \|⟨ψ_pre\|ψ_post⟩\|², the same structural overlap that Eq.(2-3) parametrizes at the registration layer." | 4.6/5 | GPT was one sentence with S3 pointer; weak measurement was one parenthetical — separate threads without coherent story. New sentences create conceptual chain: contextuality → measurement context matters → overlap quantifies context compatibility → Eq.(2) is natural simplest parametrization. Weak measurement provides established precedent. Conceptual framing, not derivational detail — C17 preserved. |
| 2 | §3.4 | **Lemma 1 operational invariant (+4 lines)**: After QED, added: "*Operational invariant.* The correlator difference δ⟨AB⟩_θ = ⟨AB⟩_θ − ⟨AB⟩_π/2 is invariant under any unitary transformation acting on the Superobserver's Hilbert space alone. Only coupling to a degree of freedom external to that basis — such as the Friend outcome d in Eq.(2) — can produce non-zero δ⟨AB⟩ with cos θ scaling. No basis redefinition of the Superobserver alone can generate this signal." | 4.7/5 | Lemma 1 (v37 formalized, v41 forward-ref'd) only addresses passive relabeling. Clever reviewer: "redefine basis actively, cos θ disappears." Operational invariant closes this: (a) defines specific invariant observable, (b) states necessary condition for non-zero signal (external coupling), (c) positive no-go: "no basis redefinition alone can generate this." |
| 3 | §5.3 | **β weak-measurement scale bridge (+3 lines)**: After "See Supplemental S3 for expanded scale comparison," added: "The ~10⁻² scale is physically motivated: postselection-conditioned weak values [18] manifest at the same order, and any overlap-dependent registration-layer structure would naturally appear at the precision where measurement-context effects become distinguishable from Poisson noise in current optical implementations." | 4.5/5 | β ecosystem (v37) listed scales but didn't connect β's scale to physical motivation. New sentence bridges: weak measurement (~10⁻²) is structural precedent — if overlap-dependence exists, natural detection scale coincides with where context effects separate from noise. Conditional framing avoids fabricating theory. |
| 4 | Abstract | **1+1+1 compression (−3 lines)**: Three sentences: (1) Insight: "θ not previously isolated — every measurement at equator → equatorial cancellation → structurally insensitive." (2) Experiment: "single-waveplate null test on Bong apparatus at θ=31° → first isolated test." (3) Consequence: "β ≥ 0.07 at 5σ, 8.6σ LF violation preserved, fair-sampling with SNSPD closure path." | 4.6/5 | v41 rejected "abstract too long" (3.8/5) as generic complaint. This 1+1+1 structure forces abstract to sell the paper rather than be the paper. Three sentences, one job each. C3 qualifier preserved. Fair-sampling folded into consequence. |

### Structural changes (v42)
| Before (v41) | After (v42) | Nature |
|-------------|-------------|--------|
| §2.3: "independently of this physical picture. No existing theory predicts this form..." | +"Conceptually, once measurement statistics are recognized as context-dependent...weak measurement formalism [18] provides an established physical precedent..." | Conceptual chain |
| §3.4: Lemma 1 ends at "∎" | +"*Operational invariant.* The correlator difference δ⟨AB⟩_θ...No basis redefinition of the Superobserver alone can generate this signal." | Operational no-go |
| §5.3: "See Supplemental S3 for expanded scale comparison." | +"The ~10⁻² scale is physically motivated: postselection-conditioned weak values [18] manifest at the same order..." | Scale bridge |
| Abstract: 14 lines, 5 sentences | 11 lines, 3 sentences (insight → experiment → consequence) | 1+1+1 compression |

### Regression
Δ: C3 (S1 qualifier), C9 (evolved to insight+experiment+consequence), C18 (strengthened with operational invariant).

---

## v41 (2026-05-25) — 10-point review RCA (threshold 4.5/5): Lemma 1 forward-ref (§3.1), operational β definition (§2.3), first isolated test hedging (§1)

**Scoring summary (10 points):** 3 implemented (≥4.5/5), 7 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Overlap-only class" sounds self-made | — | → Recurring |
| 2 | "Just a change of basis?" | 4.5/5 | **Implemented** — Lemma 1 forward-ref added to §3.1 |
| 3 | Repetition of "equator blind spot" | 3.5/5 | Rejected — "blind spot" already removed v37 |
| 4 | Non-physicist intuition / Bloch figure | — | → Recurring |
| 5 | "Who scanned θ?" literature review | 3.0/5 | Rejected — S1 survey + table already done v34–v40 |
| 6 | Sensitivity too optimistic | — | → Recurring |
| 7 | β too abstract | 4.6/5 | **Implemented** — operational definition added to §2.3 |
| 8 | Abstract too long | 3.8/5 | Rejected — C9-protected 3-beat structure |
| 9 | §2.3 too heavy on EFT/GPT jargon | — | → Recurring |
| 10 | "first experimental test" overclaim | 4.5/5 | **Implemented** — "first experimental test" → "first isolated test" |

### Implemented changes (v41)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.1 | **Lemma 1 forward-ref (+2 lines)**: After "difficult to reproduce without overlap-dependent physics," added: "This cos θ dependence is a genuine observable, not a gauge artifact: Lemma 1 (§3.4) proves it cannot be absorbed by unitary redefinition of the measurement basis." | 4.5/5 | Reviewer objection: "this is just a change of basis — cosθ is coordinate artifact." Lemma 1 (§3.4) already proves otherwise, but was positioned as a defensive lemma buried in a later subsection. Forward-referencing it in §3.1 (immediately after the main result) preempts the objection before it forms. "Genuine observable, not a gauge artifact" is the positive claim; Lemma 1 is the proof. |
| 2 | §2.3 | **Operational β definition (+3 lines)**: After lowest-order expansion sentence, added: "Operationally, β is directly measurable via δ⟨AB⟩ at any θ ≠ π/2, with the cos θ scaling under θ-sweep (§8.4) providing the distinguishing signature that separates an overlap-dependent signal from conventional systematics." | 4.6/5 | β was defined mathematically (deformation strength), physically (registration-memory coupling), and structurally (lowest-order expansion). Missing: operational — "how do I measure it?" This sentence answers: measure δ⟨AB⟩ at tilted θ, verify cos θ scaling via θ-sweep. Gives experimentalists a concrete measurement recipe. |
| 3 | §1 | **"first experimental test" → "first isolated test"**: "...within currently surveyed optical EWF implementations (Supplemental S1), the first isolated test of the overlap-only class." | 4.5/5 | "First experimental test" claims broader priority than warranted — other experiments TEST EWF, just not this parameter. "First isolated test" precisely claims what's true: this is the first experiment that isolates the polar angle as a control parameter to test the overlap-only class. One word, large precision gain. |

### Structural changes (v41)
| Before (v40) | After (v41) | Nature |
|-------------|-------------|--------|
| §3.1: "...difficult to reproduce without overlap-dependent physics (§5.3, §8.4)." | +"This cos θ dependence is a genuine observable, not a gauge artifact: Lemma 1 (§3.4) proves it cannot be absorbed by unitary redefinition of the measurement basis." | Preempt basis-change objection |
| §2.3: "...coupling to non-scalar degrees of freedom. The experiment is a null test:" | +"Operationally, β is directly measurable via δ⟨AB⟩ at any θ ≠ π/2, with the cos θ scaling under θ-sweep (§8.4) providing the distinguishing signature that separates an overlap-dependent signal from conventional systematics. The experiment is a null test:" | Operational β definition |
| §1: "the first experimental test of" | "the first isolated test of" | Precision hedge |

### Regression
Δ: C3 extended (first isolated test), C18 strengthened (Lemma 1 forward-ref from §3.1).

---

## v40 (2026-05-25) — 5-point review RCA (threshold 4.5/5): overlooked→not-previously-isolated, non-identifiability consequence, conservative β in abstract

**Scoring summary (5 points):** 3 implemented (≥4.5/5), 2 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | "Overlooked" → "not previously isolated" | 4.7/5 | **Implemented** — 3 locations |
| 2 | Eq.(2) ad-hoc — further reduce ontological | — | → Recurring |
| 3 | Non-identifiability of whole model class | 4.5/5 | **Implemented** — 1 sentence added to §3.1 |
| 4 | Conservative β in main text | 4.5/5 | **Implemented** — Abstract, §9, §5.3 restructured |
| 5 | Length reduction 20-30% | — | → Recurring |

### Implemented changes (v40)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §3.6 heading | **Overlooked→not-previously-isolated (MANDATORY 4.5/5)**: Abstract: "systematically unexplored" → "not previously been isolated as an independent control parameter". §1: "an overlooked Bloch-sphere degree of freedom" → "a Bloch-sphere degree of freedom not previously isolated as an independent control parameter". §3.6 heading: "A Systematically Unexplored Polar Angle" → "An Unisolated Geometric Control Parameter". | 4.7/5 | "Systematically unexplored" / "overlooked" implies the field made an error of omission. In reality, researchers rationally chose the equator to maximize LF violation. "Not previously isolated as a control parameter" frames the same fact as a conceptual distinction not yet drawn — reviewer feels respected, not accused. Same truth value, zero defensive reaction. |
| 2 | §3.1 | **Non-identifiability consequence (+1 sentence)**: After "theorem holds for any overlap function," added: "The experimental consequence is that equatorial measurements cannot distinguish standard QM from any overlap-dependent deformation — the entire overlap-only class is non-identifiable at θ = π/2." | 4.5/5 | Non-identifiability was stated in §3.6 but absent from §3.1 main result. Reviewer reads §3.1 first — if the main result is just "cos θ vanishes at equator," they dismiss as trivial symmetry. Explicitly naming "non-identifiable" in §3.1 converts the symmetry observation into a consequence about experimental distinguishability. |
| 3 | Abstract, §5.3, §9 | **Conservative β in main text (MANDATORY 4.5/5)**: Abstract: "β ≥ 0.04 at 5σ" → "β ≥ 0.07 at 5σ (single-setting)". §9: same. §5.3: restructured to lead with conservative single-setting (β ≥ 0.07), then mention combined (β ≥ 0.04) as secondary. | 4.5/5 | Abstract led with most optimistic number (combined 4-setting, idealized Poisson). Reviewer checks methods → finds optimistic assumptions → trust erodes. Conservative number in headline + optimistic in detail = honest salesmanship. Same numbers, different framing: "we can detect at 0.07 conservatively, and at 0.04 with combined analysis" instead of "we can detect at 0.04 (but actually more conservatively 0.07)." |

### Structural changes (v40)
| Before (v39) | After (v40) | Nature |
|-------------|-------------|--------|
| Abstract: "systematically unexplored" | "not previously been isolated as an independent control parameter" | Tone: accusation→distinction |
| §1: "an overlooked Bloch-sphere degree of freedom" | "a Bloch-sphere degree of freedom not previously isolated as an independent control parameter" | Tone: accusation→distinction |
| §3.6 heading: "A Systematically Unexplored Polar Angle" | "An Unisolated Geometric Control Parameter" | Tone: accusation→distinction |
| §3.1: "theorem holds for any overlap function." | +"The experimental consequence is that equatorial measurements cannot distinguish standard QM from any overlap-dependent deformation — the entire overlap-only class is non-identifiable at θ = π/2." | Consequence elevation |
| Abstract: "β ≥ 0.04 at 5σ" | "β ≥ 0.07 at 5σ (single-setting)" | Conservative headline |
| §9: "sensitivity β ≥ 0.04 at >5σ" | "sensitivity β ≥ 0.07 at >5σ (single-setting)" | Conservative headline |
| §5.3: led with β_min ≈ 0.038 combined | led with conservative single-setting β ≥ 0.07 | Structural reorder |

### Regression
Δ: C3, C8, C12, C15, C17 intact; conservative β headline in Abstract.

---

## v39 (2026-05-25) — 10-point review RCA (threshold 4.5/5): equatorial cancellation rename, §1 reframe (overlooked structural consequence lede), ontological→phenomenological

**Scoring summary (10 points):** 4 implemented (≥4.5/5), 1 already done (v38), 5 rejected (<4.5/5).

| # | Point | RCA Score | Action |
|---|-------|-----------|--------|
| 1 | Novelty→structural blindness emphasis | 4.5/5 | **Implemented** — merged with #4 (§1 reframe) |
| 2 | Eq.(2) ontological→phenomenological | 4.5/5 | **Implemented** |
| 3 | Survey qualifier everywhere | — | **Already done v38** |
| 4 | "Experimental consequence overlooked" lede | 4.7/5 | **Implemented** — §1 restructured |
| 5 | Length reduction ~3-4 pages | — | → Recurring |
| 6 | Killer Bloch sphere figure | — | → Recurring |
| 7 | θ-sweep smoking gun | 3.5/5 | Rejected — already covered §5.3 + §8.4 |
| 8 | Waveplate tolerance simulation | 4.0/5 | Rejected — prose tolerance already in §4.1 |
| 9 | Remove interpretation/philosophy | — | → Recurring |
| 10 | Rename "Fixed-Point"→"Cancellation" | 4.8/5 | **Implemented** |

### Implemented changes (v39)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §3, §3.2, §9 | **Theorem rename (MANDATORY 4.5/5)**: "Equatorial Fixed-Point Theorem" → "Equatorial Cancellation Theorem" (6 name occurrences). Descriptive uses of "fixed point" (lines 172, 191, 315, 317, 453, 629) preserved — those describe the geometric property, not the theorem name. | 4.8/5 | "Fixed-point theorem" evokes Banach/Brouwer — heavy topological connotations. Proof is 3 lines of algebra. "Cancellation theorem" is precise (the overlap-dependent modification cancels at the equator), honest about mathematical depth, and already used organically at §8.2 ("geometric cancellation theorem"). Preempts reviewer "this is trivial" reflex. |
| 2 | §1 ¶2 | **§1 lede reframe (MANDATORY 4.5/5)**: "This paper establishes the theorem..." → "Every published optical EWF experiment measures Superobservers exclusively in the equatorial plane (θ = π/2). This paper identifies the structural consequence of that convention: at θ = π/2...cancels identically...meaning existing implementations are structurally insensitive to the entire overlap-only class. Breaking the cancellation requires only a single quarter-wave plate..." | 4.7/5 | v38 said "novelty is geometric, not algebraic" but the §1 opening still led with "establishes the theorem." Reviewer reads lede first — if lede is "we prove X," that's the takeaway. Lede is now "every experiment shares an untested convention → here's the structural consequence → one waveplate breaks it." Novelty is in the overlooked consequence, not the algebra. |
| 3 | §1 ¶3 | **Claim A/B reframe**: "The theorem (Claim A) is the central result; the experimental protocol (Claim B, §4-7) is its direct consequence. Claim A is a mathematical theorem requiring no experimental assumptions." → "The equatorial cancellation (Claim A) is the geometric insight — a mathematical consequence of Bloch-sphere geometry requiring no experimental assumptions. The experimental protocol (Claim B, §4-7) is its direct operational consequence..." | 4.5/5 | Downgrades "theorem" (grandiose) → "geometric insight" (accurate). Adds "operational" to "consequence" — the paper is about an operational implication of overlooked geometry, not a mathematical result. Consistent with v38 framing. |
| 4 | §2.3 | **Ontological→phenomenological**: "ontological classification in Supplemental S3" → "phenomenological classification in Supplemental S3" | 4.5/5 | "Ontological" overpromises — Eq.(2) is a search tool, not a theory of reality. "Phenomenological" matches the EFT-style benchmark framing (v37) and the lowest-order expansion language (v38). One word, large signal. |

### Structural changes (v39)
| Before (v38) | After (v39) | Nature |
|-------------|-------------|--------|
| Abstract: "equatorial fixed-point theorem" | "equatorial cancellation theorem" | Rename |
| §1: "establishes the equatorial fixed-point theorem" | "identifies the structural consequence of that convention...equatorial cancellation theorem" | Lede reframe + rename |
| §1: "The theorem (Claim A) is the central result" | "The equatorial cancellation (Claim A) is the geometric insight" | Reframe |
| §1: "is its direct consequence" | "is its direct operational consequence" | Reframe |
| §3: "Equatorial Fixed-Point Theorem" | "Equatorial Cancellation Theorem" | Rename |
| §3.2: "Equatorial Fixed-Point Theorem" / "Proposition 1 (Equatorial Fixed-Point Theorem)" | "Equatorial Cancellation Theorem" / "Proposition 1 (Equatorial Cancellation Theorem)" | Rename |
| §2.3: "ontological classification" | "phenomenological classification" | Downgrade |
| §9: "equatorial fixed-point theorem" | "equatorial cancellation theorem" | Rename |

### Regression
Δ: C2 preserved (rename only), C8 reframed (structural consequence), C10+C11 intact.

---

## v38 (2026-05-25) — 3-point review RCA (threshold 4.5/5): survey-qualified hedging, lowest-order expansion justification, novelty-as-geometry framing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §7 | **Survey-qualified hedging (MANDATORY 4.5/5)**: Bare "to our knowledge" → "Within currently surveyed optical EWF implementations (Supplemental S1)" in Abstract, §1, and §7. §3.6 already had S1 qualifier from v34; §9 already had it from v34. All 5 claim locations now consistently S1-tied. | 4.8/5 | v34 applied S1-tied softening only to §9; v37 survey table anchored §3.6. Abstract, §1, and §7 still carried bare "to our knowledge" — reviewer finding one missed obscure experiment kills novelty claim. Pattern-level application completes the v34 hedge across all locations. |
| 2 | §2.3 | **Lowest-order expansion justification (+1 sentence)**: After "benchmark parametrization" line, added: "Equation (2) should be viewed as the lowest-order scalar overlap deformation in an effective operational expansion — the leading term in a systematic phenomenology where higher-order corrections involve additional powers of (1−|⟨b|d⟩|²) or coupling to non-scalar degrees of freedom." | 4.7/5 | β still reads as "made-up parameter" to a skeptical reviewer despite GPT/EFT framing (v36-37). "Lowest-order scalar overlap deformation" explicitly places Eq.(2) in an expansion hierarchy — preempting "why THIS deformation and not infinitely many others?" by answering: because it's the leading term; everything else is higher-order. |
| 3 | §1 | **Novelty-as-geometry framing (+1 sentence)**: After "The full proof is three lines," added: "The novelty is geometric, not algebraic: an overlooked Bloch-sphere degree of freedom, with a single-waveplate operational consequence." | 4.5/5 | Paper sells "three-line proof" honestly (C8) but risks reviewer dismissal as "trivial math." One sentence reframes novelty from algebraic complexity to geometric insight + operational consequence — consistent with null-point narrative (v37), geometric framing throughout. |

### Structural changes (v38)
| Before (v37) | After (v38) | Nature |
|-------------|-------------|--------|
| Abstract: "Existing...share, to our knowledge, a systematically..." | "Within currently surveyed optical EWF implementations (S1), a geometric degree..." | Survey-qualify |
| §1: "enables, to our knowledge, the first experimental test" | "enables, within currently surveyed optical EWF implementations (S1), the first..." | Survey-qualify |
| §7: "θ = 31° — to our knowledge, the first non-equatorial EWF measurement" | "θ = 31° — within currently surveyed implementations, the first non-equatorial..." | Survey-qualify |
| §2.3: "Equation (2) is a benchmark parametrization..." | +"Equation (2) should be viewed as the lowest-order scalar overlap deformation in an effective operational expansion — the leading term in a systematic phenomenology where higher-order corrections involve additional powers of (1−|⟨b|d⟩|²) or coupling to non-scalar degrees of freedom." | Justification |
| §1: "The full proof is three lines...§2 provides..." | +"The novelty is geometric, not algebraic: an overlooked Bloch-sphere degree of freedom, with a single-waveplate operational consequence." | Framing |

### Regression
Δ: C3 extended to all 5 claim locations; C10 extended with lowest-order justification.

## v37 (2026-05-25) — 10-point review RCA (threshold 4.5/5): EFT-style framing, GPT/weak-measurement→S3, Lemma 1 formalized, survey table, smoking-gun soften, β ecosystem, null-point narrative, analytic θ=31°, statistical robustness methodology, overlap-symmetry fig ref

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **EFT-style framing + GPT/weak-measurement→S3**: "symmetry-constrained benchmark parametrization" → "EFT-style benchmark parametrization — a symmetry-constrained search target that does not commit to a microscopic origin." GPT state-effect duality detail → S3 pointer ("state-effect duality derivation and information-geometric motivation in Supplemental S3"). Weak measurement parallel detail → S3 pointer ("connection to weak measurement formalism [18] developed in Supplemental S3"). "phenomenological parameter searches" → "EFT-style parameter searches." Net: main text compact, supplement carries derivation. | 4.2/5 | EFT framing converts SME from historical precedent to structural methodology. Moving GPT derivation + weak measurement detail to S3 keeps main text lean while preserving citations. Counterbalances v36 expansion. |
| 2 | §3.6 | **Survey table added (MANDATORY 4.5/5)**: Bong + Proietti prose bullets → compact survey table (experiment, year, measurement type, θ, equatorial?, ref). Bong: θ = π/2, equatorial. Proietti: BSM, functionally equivalent (footnote). | 4.5/5 | S1 audit evidence existed but was invisible to main-text reader. Table converts claim from "trust our search" to "here's the data — check it yourself." |
| 3 | §3.4 | **Lemma 1 (Non-Absorption) formalized**: Prose defense → numbered Lemma 1 with compact proof. "The cos θ term in Eq. (4) cannot be absorbed by unitary redefinition." Proof: passive relabeling → δ⟨AB⟩=0 vs Eq.(2) couples to Friend outcome d → δ⟨AB⟩∝β cos θ. QED. Cross-reference in §5.3. | 4.0/5 | v26-v35 proof was dressed as exposition. Lemma with QED signals "proved," not "argued." Content identical; packaging is the fix. |
| 4 | §5.3 | **β ecosystem comparison (+8 lines)**: SME photon-sector <10⁻²³, CSL collapse λ≈10⁻¹⁶ s⁻¹, weak-measurement anomalies ~10⁻². β≥0.04 constraint places overlap-dependent deformation at ~10⁻² scale — comparable to weak-measurement anomalies. S3 pointer. | 4.3/5 | β existed in vacuum. Three phenomenological scales bracket target sensitivity — gives β intellectual company without fabricating theory. |
| 5 | §6 | **Statistical robustness methodology**: "Bootstrap resampling...recommendations" → three-part: (i) bootstrap of time-ordered data, (ii) correlated drift model, (iii) fake-signal injection test. | 4.0/5 | Paper delegated validation to implementing lab. Naming three methods shows proposer has thought through realistic failure modes. |
| 6 | §3.1, §5.3 | **smoking-gun→distinctive signature (MANDATORY 4.5/5)**: v36 "smoking-gun...cannot be explained by" → "distinctive...is distinct from standard systematic profiles...difficult to reproduce without overlap-dependent physics." §5.3: "smoking-gun test" removed, "cannot be produced by" → "is distinct from," added Lemma 1 cross-reference. | 4.5/5 | Direct correction of v36 overreach. "Cannot" is absolute — reviewer constructs counterexample. "Distinct from standard profiles" + "difficult to reproduce" preserves logic while falsifiable. |
| 7 | §3.5 | **Overlap-symmetry figure ref**: "[Figure X: Balanced vs tilted overlap geometry — at equator all overlaps = 1/2 (symmetric); at θ≠π/2 basis tilts toward one Friend outcome, creating cos θ asymmetry...]" | 3.8/5 | Core geometric insight never visualized. Below threshold but user-flagged + 1 line cost. |
| 8 | §3.6 closing, §1 | **Null-point narrative**: "convention, not constraint" → "may have unknowingly operated exactly at a geometric null point." §1: "structurally blind" → "may have unknowingly operated at a geometric null point." | 4.3/5 | Strongest narrative previously unstated. Self-evidently true from theorem, more dramatic and more precise than "structurally blind." |
| 9 | §4.1 | **Analytic θ=31° intuition**: "Analytically, the figure of merit approximates FOM(θ) ∝ min(|cos θ|, f_LF(θ)), where f_LF(θ) is a monotonically increasing function of θ...the intermediate optimum emerges from the intersection of these competing trends." | 3.8/5 | θ=31° was black-box grid search. Analytic structure shows optimum is intersection of two monotonic trends — not arbitrary. Below threshold but user-flagged. |
| 10 | §1 | **S3 description expanded**: +GPT state-effect duality derivation, weak measurement connection. S2: +statistical robustness methodology. | 4.0/5 | Reader sees where detailed motivation lives after v37 moved GPT/weak-measurement detail to supplement. |

### Structural changes (v37)
| Before (v36) | After (v37) | Nature |
|-------------|-------------|--------|
| §2.3: GPT state-effect duality detail + weak measurement parallel (~6 lines) | S3 pointers (~2 lines) | Main text→supplement |
| §2.3: "symmetry-constrained benchmark" / "phenomenological parameter searches" | "EFT-style benchmark parametrization" / "EFT-style parameter searches" | Reframe |
| §3.1: "smoking-gun...cannot be explained by" | "distinctive...is distinct from...difficult to reproduce" | Soften |
| §3.4: Prose defense | Lemma 1 + formal proof + QED | Formalize |
| §3.5: No overlap-symmetry visual | Figure reference added | Fig ref |
| §3.6: Bong+Proietti prose bullets | Survey table | Table |
| §3.6: "convention, not constraint" | "unknowingly at geometric null point" | Narrative |
| §4.1: Prose trade-off only | +analytic FOM approximation | Analytic intuition |
| §5.3: "smoking-gun test" / "cannot be produced by" | "distinct from standard systematic profiles" / "difficult to reproduce" + Lemma 1 ref | Soften |
| §5.3: No β ecosystem | +"β in context" (SME/CSL/weak-measurement) | Ecosystem |
| §6: Generic S2 pointer | Three-part methodology named | Methodology |
| §1 ESP: "structurally blind" | "may have unknowingly operated at a geometric null point" | Narrative |
| §1: S2/S3 descriptions | Expanded: S2 + robustness, S3 + GPT + weak measurement | Index |

### Regression
Δ: C17 detail→S3; C18 Lemma 1 formalized; C20 corrected v36 overreach.

---

## v36 (2026-05-25) — 10-point review RCA (threshold 4.5/5): GPT motivation deepened, β as registration-memory coupling, weak measurement cite, cosθ smoking-gun signature, minimal phenomenological class, blind spot→systematically unexplored, optimization landscape fig ref, QWP+timing+stats→S2

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **GPT motivation deepened (+3 lines)**: "Within the GPT framework [17], Eq. (2) parametrizes the simplest one-parameter deformation of the Born rule" → "Within the GPT framework [17], where measurement statistics arise from a state-effect duality on a convex operational space, Eq. (2) parametrizes the simplest one-parameter deformation of the effect operators that depends on the relative orientation between measurement contexts." GPT was a name-drop (v27, compressed in v29); now it's an argument connecting GPT structure to the specific functional form. | 4.2/5 | GPT bridge was added in v27 but compressed to a shallow citation in v29. Reviewer reads "GPT" as window-dressing unless the paper shows WHY GPT structure naturally accommodates overlap-dependent deformation. State-effect duality + convex operational space = natural home for overlap-dependence. |
| 2 | §2.3 Core idea | **β as registration-memory coupling strength**: "β controls the strength of any departure from perfect factorization" → "β functions as a registration-memory coupling strength: the overlap \|⟨b\|d⟩\|² quantifies how compatibly the Superobserver's measurement basis registers the Friend's recorded outcome, and β controls how strongly the registration retains memory of the Friend's outcome orientation." | 4.3/5 | β was defined mathematically as "deformation strength" (v32) but lacked an intuitive physical metaphor. "Registration-memory coupling strength" gives reviewers a concrete mental model without fabricating a microscopic theory. |
| 3 | §2.3 Core idea, Refs | **Weak measurement parallel + cite [18]**: Added "This structure parallels the weak measurement formalism [18], where postselection-conditioned measurement outcomes likewise depend on the overlap between pre- and post-selected states." New reference: Y. Aharonov, D.Z. Albert, and L. Vaidman, Phys. Rev. Lett. 60, 1351 (1988). | 4.5/5 | "Why should nature care about overlap?" — weak measurement is the established physical framework where overlap-dependence is already recognized as a real physical parameter. The conceptual parallel converts "ad hoc" → "natural extension of known physics." |
| 4 | §3.1 | **cosθ smoking-gun signature consolidated (+6 lines)**: New paragraph: "The smoking-gun experimental signature is the cos θ functional form itself: equatorial measurements (θ = π/2) sit at an exact fixed point where all overlap-dependent deformations vanish identically; tilting away from the equator produces a linear onset ∝ cos θ. Any non-zero δ⟨AB⟩ exhibiting this cos θ scaling cannot be explained by standard quantum mechanics with conventional systematic errors — both would produce either null or non-geometric signatures (§5.3, §8.4)." | 4.5/5 | cosθ prediction was distributed across §3.1 (theorem), §5.3 (discriminator), §8.4 (θ-sweep) without a single consolidated statement. "Smoking-gun" paragraph in §3.1 (immediately after main result) gives reviewers the take-home message before they reach experimental sections. |
| 5 | §5.3 | **cosθ as new observable + systematic-error defense**: "The cos θ dependence produces a qualitatively distinct experimental signature that vanishes at θ = π/2 (standard configuration) and is maximal at θ → 0°" → "The cos θ scaling constitutes a new experimental observable...the cos θ signature cannot be produced by conventional systematic errors (which either cancel in δ⟨AB⟩ comparison or produce non-geometric θ-dependence), making it a smoking-gun test for overlap-dependent deformation." | 4.0/5 | cosθ was framed defensively in §3.4 (anti-reparameterization). Framing it as a NEW observable — not just a defense — strengthens the paper's positive contribution. Systematic-error exclusion argument preempts "couldn't this be a calibration artifact?" |
| 6 | §3.2 Scope | **Minimal phenomenological class qualification (+1 line)**: "**Scope limitation.** Proposition 1 constrains the overlap-only class:" → "**Scope limitation.** The overlap-only class is the minimal phenomenological class capturing dependence on \|⟨b\|d⟩\|²; we do not claim completeness over all possible deformations. Proposition 1 constrains this class:" | 4.3/5 | v30 scope limitation only said what's OUTSIDE the class. Positive characterization as "minimal phenomenological class" converts a negative boundary into an honest positive statement. "We do not claim completeness" preempts the uniqueness objection. |
| 7 | Abstract, §3.6 heading | **blind spot→systematically unexplored**: Abstract: "common geometric blind spot" → "systematically unexplored geometric degree of freedom". §3.6 heading: "Structural Blind Spot" → "A Systematically Unexplored Polar Angle". | 4.2/5 | "Blind spot" was intentionally chosen in v30 (RCA 4.2/5) as stronger than "appear insensitive." But "blind spot" implies the community overlooked something obvious — evaluative tone that can alienate reviewers. "Systematically unexplored" is a factual description: θ has not been varied, and the structural reason is LF inequality optimization. |
| 8 | §4.1 | **Optimization landscape figure reference (+2 lines)**: Added "[Figure X: Figure of merit vs polar angle θ, showing broad optimum at θ ≈ 31° and 5σ detection boundary spanning θ ∈ [20°, 55°].]" | 3.8/5 | Prose FOM values (v16) are adequate but visual communication is stronger for PRA readers scanning for experimental feasibility. Below threshold (3.8/5) but user-flagged + cost = 1 line. |
| 9 | §4.2, §4.5, §6 | **Engineering/statistical detail → S2 (−13 lines)**: (a) §4.2: Removed QWP retardance tolerance (±2 nm), temperature coefficient (0.01 nm/°C), angular uncertainty (±0.5°) → "QWP specifications...are provided in Supplemental S2." (−4 lines). (b) §4.5: Compressed acquisition timing (91 s per setting, 14 min data, 1 hr total) and drift estimates → 3-line summary + S2 pointer (−5 lines). (c) §6: Compressed statistical model limitations (bootstrap resampling, detector-drift simulation recommendations) → 2-line summary + S2 pointer (−4 lines). | 4.2/5 | v35 de-overpack targeted interpretation/philosophy sections but left engineering details and statistical caveats in main text. For a ~5-page PRA submission, QWP temperature coefficients, acquisition stopwatch timing, and bootstrap methodology belong in supplement. Essential protocol steps and sensitivity estimates retained in main text. |
| 10 | §3.5, §3.6, §4.1, §4.2 positioning | **De-overpack continuation — structural notes preserved, details → supplement**: All conceptual content preserved (physical intuition §3.5 untouched, search methodology §3.6 untouched, calibration §4.4 untouched, sensitivity §5.3 extended). Only implementation-level detail moved to S2. | 4.0/5 | v35 reduced paper from ~627→~600 lines. v36 net change ~+3 lines (additions in §2.3/§3.1/§5.3 offset by compressions in §4.2/§4.5/§6). Paper remains ~5 pages with 18 refs. |

### Structural changes (v36)
| Before (v35) | After (v36) | Nature |
|-------------|-------------|--------|
| §2.3: GPT as name-drop ("Within the GPT framework [17], Eq. (2) parametrizes...") | GPT as argument ("where measurement statistics arise from a state-effect duality on a convex operational space...") | Deepen |
| §2.3: β = "deformation strength" | β = "registration-memory coupling strength" + "retains memory of the Friend's outcome orientation" | Physical metaphor |
| §2.3: No weak measurement connection | +"parallels the weak measurement formalism [18]" + ref [18] | Citation |
| §3.1: Ends with "theorem holds for any overlap function" | +6-line smoking-gun paragraph: fixed point + linear onset ∝ cosθ + systematic-error exclusion | Consolidate |
| §3.2: Scope limitation = what's OUTSIDE class only | +"minimal phenomenological class...we do not claim completeness" | Positive qualification |
| §5.3: cosθ as defensive discriminator | cosθ as new experimental observable + smoking-gun test + systematic-error impossibility | Reframe |
| Abstract: "geometric blind spot" | "systematically unexplored geometric degree of freedom" | Soften |
| §3.6 heading: "Structural Blind Spot" | "A Systematically Unexplored Polar Angle" | Soften |
| §4.2: QWP retardance ±2 nm, temp coefficient 0.01 nm/°C, angular uncertainty ±0.5° | S2 pointer | Engineering→supplement |
| §4.5: 91 s/setting, 14 min data, 1 hr total, SPDC drift <5%, dark-count drift ~1% | 3-line summary + S2 pointer | Detail→supplement |
| §6: Bootstrap resampling + detector-drift sim + time-correlated errors full paragraph | 2-line summary + S2 pointer | Methodology→supplement |
| §4.1: No optimization landscape figure | +"[Figure X: Figure of merit vs polar angle θ...]" | Figure reference |
| References: 17 refs | 18 refs (+[18] Aharonov et al. 1988) | Citation |

### Regression
Δ: C6+C7 extended (GPT deepened). Blind-spot wording zeroed.
| **Net** | **~600 lines** | **~603 lines** | **+3 lines** |

---

## v35 (2026-05-25) — 2-issue RCA (threshold 4.5/5): §3.4 compress, paper de-overpack (interpretation→S3, search compress, trim verbose sections)

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.4 | **Compress (−10 lines)**: 18-line defensive exposition → 8-line crisp distinction. Removed: explicit trace formula, POVM equivalence detail, three-observation bullet list. Kept: "passive relabeling relabels outcomes without altering the joint probability distribution" vs "Eq.(2) couples to the physical overlap...which depends on the Friend outcome d — a degree of freedom external to the Superobserver's measurement basis." Added empirical test summary: "passive relabeling predicts δ⟨AB⟩ = 0 for all θ; Eq.(2) predicts δ⟨AB⟩ ∝ β cos θ, verifiable by θ-sweep." | 4.5/5 | §3.4 had grown to 18 lines across v26→v33 as defenses accumulated (non-absorption proof v26, explicit POVM v32, passive-relabeling v33). The core distinction is one sentence: "passive relabeling ≠ coupling to Friend outcome." Three-observation bullet list was redundant with the prose. |
| 2 | §3.6, §8.2+§8.3, §5.3, §3.5 | **Paper de-overpack (−25 lines total)**: (a) §3.6 literature search: 22 lines → 13 lines — removed examined-documents inventory ("We examined the 47-page Supplemental Material of Bong..."), kept search methodology summary + S1 pointer. (b) §8.2+§8.3 merged: "Relation to Quantum Interpretations" (7 lines) + "Illustrative Parametric Model" (8 lines) → single "Interpretation and Model Context" (5 lines) with S3 pointer. Removed δ⟨A₁B₂⟩ = −0.0355 (redundant with §5.3 table) and φ-independence discussion (covered in §5.3). (c) §5.3 Scale context: 5-line SME comparison paragraph → 2-line compact: "A null result at β ≥ 0.04 excludes O(1) and O(10⁻¹) deformation...opening a new parameter space; N = 200,000 extends sensitivity to β ≥ 0.02." SME comparison removed (redundant with §2.3). (d) §3.5 Physical Intuition: 23 lines → 19 lines — removed "In the language of measurement disturbance:" meta-phrase, merged redundant symmetry sentences. Geometric content + measurement disturbance + directional probe + mathematical observation all preserved. | 4.8/5 | The paper had accumulated content across 22 versions without a "main text vs supplement" audit. At 627 lines for a 5-page PRA target, every section was competing for space. The principle: main text = theorem + geometry + minimal protocol + one sensitivity estimate; interpretation + philosophy + detailed methodology → supplement. |

### Structural changes (v35)
| Before (v34) | After (v35) | Nature |
|-------------|-------------|--------|
| §3.4: 18 lines, explicit trace formula + POVM detail + (a)/(b)/(c) list | 8 lines, crisp passive-vs-physical distinction + empirical test | Compression |
| §3.6: 22-line search methodology with examined-documents inventory | 13-line compact version with S1 pointer | Methodology→supplement |
| §8.2: 7 lines (interpretations) + §8.3: 8 lines (parametric model) | §8.2: 5 lines merged "Interpretation and Model Context" | Merge + S3 pointer |
| §5.3: 5-line "Scale context" SME comparison paragraph | 2-line compact parameter-space statement | Redundancy removal |
| §3.5: 23 lines with meta-phrases + redundant sentences | 19 lines, all conceptual content preserved | Tightening |

### Regression
Δ: C7 compressed, content preserved.

---

## v34 (2026-05-25) — 4-issue RCA: abstract compression, §2.3 de-lawyer, novelty S1-tied softening, Proposition 1 Definition+compact

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract | **Compression (−3 lines)**: "of the form P = P_QM · [1 − β · g(overlap)] / Z cancels identically — for any function g whatsoever, not just Eq. (3)" → "P = P_QM · [1 − β · g(overlap)] / Z cancels identically for any function g." "Consequently, existing EWF experiments constrain a smaller theory space than previously assumed: all published implementations operate at the equatorial fixed point and are structurally silent on the overlap-only class." → "Consequently, published EWF implementations are structurally insensitive to the overlap-only class." | 4.3/5 | Abstract was packing 6 distinct pieces of information (theorem, universality, theory-space claim, experiment, sensitivity, loophole). Compressed theory-space sentence from 3 lines to 1 while making it MORE forceful ("structurally insensitive" is sharper than "constrain a smaller theory space than previously assumed"). |
| 2 | §2.3 | **De-lawyer (−12 lines)**: (a) Removed meta-paragraph "Before presenting the theorem, we explain which class..." (3 lines). (b) Compressed Eq.(2) terminology note: "previously termed outcome-dependent coupling in preliminary drafts..." → deleted (2 lines). (c) Compressed constraints: 8-line detailed (i)-(iii) → 4-line compact version: "The three constraints — (i) rotation invariance, (ii) alignment limit g(1)=0, (iii) monotonicity — force the leading-order Taylor expansion g(x) = c₁(1−x) + O((1−x)²)." (d) Removed "Constraints (i)-(iii) are not exhaustive — they are the minimal set for a one-parameter family" (implied by the structure; defense unnecessary). (e) Compressed null test from 5 lines to 2: "The experiment is a null test: standard QM predicts the same LF violation regardless of θ; a θ-dependent signal would indicate a departure from standard QM independently of model class." | 4.5/5 | §2.3 was doing defend+define+motivate+disclaim+compare GPT+compare SME+explain geometry — 7 rhetorical moves in one section. The "lawyer-like" feel came from arguing against imaginary reviewers. Cuts preserve all substantive content while removing meta-commentary and defensive accretion. Section now reads as confident exposition, not preemptive defense. |
| 3 | §9 | **Novelty S1-tied softening**: "Every published EWF experiment has operated at this fixed point; the overlap-only class has therefore remained structurally invisible to all existing tests." → "Within the surveyed literature (Supplemental S1), published EWF implementations have operated at this fixed point; the overlap-only class has therefore remained structurally untested." | 4.3/5 | Absolute novelty claims ("Every published...") are maximally vulnerable to one obscure counterexample. Tying the claim to the S1 audit methodology converts an absolute negative into a methodology-backed finding. "Structurally untested" is more precise than "structurally invisible." |
| 4 | §3.2 | **Proposition 1 formalization**: Added formal **Definition (Overlap-only class)** before Proposition 1: "P'(a,b \| x,y) = P_QM(a,b \| x,y) · g(\|⟨b\|d⟩\|²) / Z, where g: [0,1] → ℝ is any function and Z normalizes the distribution." Proposition 1 reformatted as compact theorem statement: "Let g be any function. At θ = π/2, \|⟨b\|d⟩\|² = 1/2 for all outcome pairs (b,d). Hence g(\|⟨b\|d⟩\|²) = g(1/2) is constant, and P'(a,b \| x,y) = P_QM(a,b \| x,y). The equatorial plane is a fixed point of every overlap-only deformation. ∎" Title changed from "Universality within overlap-only deformations" → "Equatorial Fixed-Point Theorem." | 4.5/5 | Proposition 1 was prose-heavy ("Therefore...and the modification factor [1 − β · g(...)] / Z reduces to..."). The Definition→Theorem structure makes the mathematical content immediately visible to reviewers scanning for rigor. "Equatorial Fixed-Point Theorem" as the proposition name reinforces the paper's single headline (v31). |

### Structural changes (v34)
| Before (v33) | After (v34) | Nature |
|-------------|-------------|--------|
| Abstract: 14 lines, 6 info pieces | 11 lines, 5 info pieces (theory-space claim absorbed into "structurally insensitive") | Compression |
| §2.3: ~60 lines, 7 rhetorical moves | ~48 lines, 4 rhetorical moves (define, motivate, compare SME, frame null test) | De-lawyer |
| §2.3: Meta-paragraph "Before presenting the theorem..." | Deleted | Anti-meta |
| §2.3: Terminology note "(previously termed...)" | Deleted | Anti-internal-tracking |
| §2.3: 8-line constraint exposition | 4-line compact version | Compression |
| §2.3: "Constraints not exhaustive" defense | Deleted | Anti-defensive |
| §2.3: 5-line null test exposition | 2-line compact version | Compression |
| §3.2: Prose-heavy Proposition 1 | Definition + compact Proposition 1 | Formalization |
| §9: "Every published EWF experiment..." | "Within the surveyed literature (Supplemental S1), published EWF implementations..." | S1-tied softening |

### Regression
Δ: C16 NEW (S1-tied softening §9); C3+C14 extended.

---

## v33 (2026-05-25) — 6-issue RCA: uniqueness→simplest hedge, §3.4 passive-relabeling soften, scope qualifier, SME→phenomenological, repetition de-echo, registration-fidelity structural observation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 Core idea | **"Unique"→"simplest" hedge**: "is the unique (to leading order) one-parameter form" → "is the simplest leading-order form satisfying them — every smooth function obeying (i)-(iii) shares the same first-order structure g(x) ∝ (1−x)." | 4.5/5 | "Unique" under unspecified regularity assumptions invites mathematician/philosopher attack. "Simplest" + explicit statement that all share the same leading-order structure is both safer and more precise. |
| 2 | §3.4 | **Passive-relabeling soften**: "they produce identical joint statistics with any second-system measurement" → "under passive basis relabeling, they represent the same physical measurement and the joint statistics are unchanged." | 4.2/5 | "Any second-system measurement" overclaims — technically correct for fixed POVM but could be read as "any operational context." "Passive basis relabeling" is the precise mathematical operation and cannot be misinterpreted. |
| 3 | §3.6 | **Scope qualifier**: "so no equatorial experiment can detect or exclude any member of this class" → "no equatorial experiment can detect or exclude any member of this class, within the overlap-only class" (v32). v33 further refined to: "cannot distinguish standard QM from any overlap-dependent deformation within this class." | 4.0/5 | "Exclude any member" without scope qualifier invites "exclude under THIS parametrization only." Explicit "within this class" + "overlap-dependent deformation" closes the ambiguity. |
| 4 | §2.3 | **SME→phenomenological parameter searches**: "like the Standard Model Extension for Lorentz violation [15], it defines..." → "similar in spirit to phenomenological parameter searches (e.g., the Standard Model Extension for Lorentz violation [15]), it defines..." | 4.2/5 | Quantum foundations reviewers can be allergic to SME analogies when no deep EFT structure exists. "Phenomenological parameter searches" is the genus; SME is an example species. Reduces attack surface while preserving the analogy's force. |
| 5 | §3.6, §9 | **Repetition de-echo**: "constrain a smaller theory space than previously assumed" appeared verbatim in Abstract, §3.6, and §9 (v32). §3.6 reworded to: "The structural implication is that...existing experiments, operating exclusively at this fixed point, cannot distinguish standard QM from any overlap-dependent deformation within this class." §9 reworded to: "Every published EWF experiment has operated at this fixed point; the overlap-only class has therefore remained structurally invisible to all existing tests." | 4.0/5 | Three verbatim repetitions of the same headline sentence across Abstract/body/Conclusion read as padding. Varied wording preserves the claim while avoiding echo. Abstract keeps canonical statement. |
| 6 | §3.5 | **Registration-fidelity structural observation**: Added 5-line mathematical observation after directional probe metaphor. "Mathematically, such terms are the leading-order expression of any smooth registration-fidelity function that depends on measurement alignment: the first-order correction away from perfect alignment generically has the structure 1 − β·(1 − |⟨b|d⟩|²). Eq.(2-3) isolates this universal geometric structure without committing to a specific physical mechanism." | 3.8/5 | User-requested partial fix. Stops short of a full toy model (which would invite attack as speculative) but demonstrates that the term's structure is mathematically generic — any smooth fidelity function has this leading-order form. Framed as mathematical observation, not physical claim. |

### Structural changes (v33)
| Before (v32) | After (v33) | Nature |
|-------------|-------------|--------|
| §2.3: "is the unique (to leading order) one-parameter form" | "is the simplest leading-order form — every smooth function obeying (i)-(iii) shares the same first-order structure g(x) ∝ (1−x)" | Mathematical hedge |
| §2.3: "like the Standard Model Extension for Lorentz violation [15]" | "similar in spirit to phenomenological parameter searches (e.g., the Standard Model Extension for Lorentz violation [15])" | SME genus-species reframe |
| §3.4: "produce identical joint statistics with any second-system measurement" | "under passive basis relabeling, they represent the same physical measurement and the joint statistics are unchanged" | Overclaim reduction |
| §3.5: No structural observation | +5-line registration-fidelity mathematical observation | Plausibility demonstration |
| §3.6: "constrain a smaller theory space than previously assumed: the equatorial plane..." | "The structural implication is that the equatorial plane...cannot distinguish standard QM from any overlap-dependent deformation within this class" | De-echo |
| §9: "constrain a smaller theory space than previously assumed: all published implementations operate..." | "Every published EWF experiment has operated at this fixed point; the overlap-only class has therefore remained structurally invisible to all existing tests" | De-echo |

### Regression
Δ: C7 extended; C13+C14 harmonized (de-echo).

---

## v32 (2026-05-25) — 7-issue RCA: Eq.(2) uniqueness+measurement disturbance, universality sharpening, explicit δ⟨AB⟩=0 no-go, practical sensitivity range, defensive tone trim, observer-record alignment narrative, theory-space constraint reframing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §2.3, §3.5 | **Eq.(2) physical grounding**: §2.3 Core idea — "is the unique (to leading order) one-parameter form satisfying them" replaces "any function...has identical leading-order structure." Added measurement-disturbance framing: "Physically, Eq.(2) parametrizes a residual measurement disturbance: the overlap |⟨b|d⟩|² quantifies how compatibly the Superobserver's measurement basis registers the Friend's recorded outcome." Harmonized L129 "not its unique member" → "shares the same leading-order structure g(x) ∝ (1−x); Eq.(3) adopts the simplest full representative." | 3.8/5 | User-requested partial fix. GPT bridge (v27) + benchmark (v30) already provide substantial grounding. Strengthening uniqueness claim + measurement-disturbance narrative adds physical motivation without fabricating a toy model. |
| 2 | Abstract, §9 | **Universality sharpening**: "any overlap-dependent modification" → "every overlap-dependent modification." "for every function g" → "for any function g whatsoever." "establish" → "prove" (Abstract). "As its experimental consequence" → "As its direct experimental consequence" (§9). | 4.2/5 | v27/v30/v31 already centered the theorem but language was not maximally forceful. The universality is the paper's single strongest claim — the wording should reflect that. |
| 3 | §3.4 | **Explicit no-go δ⟨AB⟩=0 calculation**: Added explicit unitary POVM equivalence argument. "Under a unitary change of measurement basis |b'⟩ = U|b⟩, the correlator ⟨AB⟩ = Σ_{a,b} a·b·Tr(Π'_a ⊗ Π_b ρ) is identically invariant...Π'_a = U Π_a U†; since {Π'_a} and {Π_a} are unitarily equivalent POVMs on the same Hilbert space, they produce identical joint statistics." Contrasted with Eq.(2): "the modification couples to the Friend outcome d, which is external to the Superobserver's measurement basis." | 4.5/5 | v26 non-absorption proof was qualitative. Reviewer's #1 attack ("isn't this just basis relabeling?") requires quantitative counter-demonstration. Explicit δ⟨AB⟩=0 for unitary case vs δ⟨AB⟩∝β cos θ for Eq.(2) is the decisive discriminator. |
| 4 | §5.3 | **Practical sensitivity range**: Added "Accounting for realistic systematics (§6-7), the practical sensitivity floor is likely β ∼ 0.05–0.10 (single-setting) and β ∼ 0.04–0.06 (combined)." | 4.0/5 | v26 Bayesian + v28 "order-of-magnitude" qualifier + v30 mechanism names already addressed optimism. Explicit range quote preempts "this assumes perfect conditions" objection. |
| 5 | §2.3 IS-NOT, §9 | **Defensive tone trim**: §2.3 IS-NOT triple negation ("not a hidden-variable model, not a collapse modification, not a signal between observers") → single S3 pointer ("ontological classification in Supplemental S3"). §9 removed one "To our knowledge" — theory-space constraint sentence implies novelty without explicit hedge. | 3.8/5 | User-requested partial fix. v29 (−54 lines) + v31 (−25 lines) already cut most defensive accretion. Remaining cuts are surgical: IS-NOT triple was the last redundant negation block; §9 hedge made redundant by theory-space reframing. |
| 6 | §3.5 | **Observer-record alignment narrative**: Extended physical intuition from purely geometric symmetry argument to measurement-disturbance language. "The Superobserver's measurement apparatus is equally aligned with every Friend record — the act of reading the record disturbs both outcomes identically." "At the equator, the registration is perfectly balanced." "The measurement apparatus becomes a directional probe for registration-layer structure." | 4.2/5 | v19+v28 geometric intuition explained WHY geometrically but not WHY physically. "Observer-record alignment" + "measurement disturbance" + "directional probe" provide the physical narrative reviewers will ask for. |
| 7 | Abstract, §3.6, §9 | **Theory-space constraint reframing**: NEW framing: "Consequently, existing EWF experiments constrain a smaller theory space than previously assumed: all published implementations operate at the equatorial fixed point and are structurally silent on the overlap-only class." Applied in Abstract (L18-20), §3.6 (L297-301), §9 (L605-607). §3.6 addition: "no equatorial experiment can detect or exclude any member of this class." §9 addition: "The experiment accesses a geometric degree of freedom that has remained unprobed across every published EWF implementation." | 4.5/5 | Completely new reframing. Converts "we found a blind spot" (negative framing) into "existing experiments constrain a smaller theory space than assumed" (substantive reframing). Addresses the "just a null test" objection by grounding the paper's contribution in what existing experiments FAIL to constrain. |

### Structural changes (v32)
| Before (v31) | After (v32) | Nature |
|-------------|-------------|--------|
| Abstract: "We establish" + 3-beat | "We prove" + 4-beat (observation → theorem → theory-space constraint → experiment → scope) | Assertiveness + reframing |
| §2.3 Core idea: "any function...identical leading-order" | "is the unique (to leading order) one-parameter form" + measurement disturbance | Uniqueness + physical motivation |
| §2.3 L129: "not its unique member" | "shares the same leading-order structure g(x) ∝ (1−x); Eq.(3) adopts the simplest full representative" | Harmonization with Core idea |
| §2.3 IS-NOT: triple negation | Single S3 pointer | Defensive compression |
| §3.4: Qualitative non-absorption | Explicit δ⟨AB⟩=0 calculation via unitary POVM equivalence | Quantitative no-go |
| §3.5: Geometric symmetry only | Measurement disturbance + directional probe narrative | Physical narrative |
| §3.6: "Tilting...opens access" | Theory-space constraint reframing + "previously invisible sector" | Reframing |
| §5.3: Idealized β_min only | + practical sensitivity range β ∼ 0.05–0.10 | Realistic quoting |
| §9: "any" + one "To our knowledge" | "every" + theory-space constraint + closing sentence, hedge removed | Assertiveness + reframing |

### Regression
Δ: C7+C9 extended; C13+C14+C15 harmonized.

---

## v31 (2026-05-25) — 9-issue RCA: novelty softening, Eq.(2) motivation repositioned, thesis repetition cuts, theorem-box restructure, experimental feasibility, reparameterization defense, multi-observer → S3, defensive tone reduction, headline consolidation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §3.6, §9 | **Novelty softening**: "share a structural experimental blind spot" → "share, to our knowledge, a common geometric blind spot". §3.6: "To our knowledge, no published EWF implementation has systematically probed θ". §9: "To our knowledge, no published EWF implementation has probed this geometric degree of freedom." Removed "obvious in hindsight" phrasing (v30 coda cut entirely). | 4.3/5 | Asymmetric hedging — §7 hedged (v28) but §3 and Abstract still absolute. "To our knowledge" consistent throughout. |
| 2 | §2.3 | **Eq.(2) motivation repositioned**: GPT/operational framing (v27 bridge) moved from end of §2.3 to "Core idea" paragraph — now appears BEFORE Eq.(2) first use. "Within the GPT framework [17], Eq.(2) parametrises the simplest one-parameter deformation of the Born rule preserving normalization and remaining operationally admissible." Reader encounters operational grounding before seeing the equation. | 4.4/5 | Temporal ordering — GPT motivation buried after 70 lines (L163 in v30); should precede Eq.(2) at L115. |
| 3 | §1, §2.3, §5.3, §9 | **Thesis repetition cuts (~30 lines)**: Deleted/compressed 7 redundant "not claiming new physics" / "does not claim...exists in nature" instances across §1, §2.3 (two blocks), §5.3, §9. Preserved ESP boundary (§1 L57-61) as the ONE canonical disclaimer. §2.3 ontological classification → 1-line inline. §2.3 null test framing → 2 sentences. §5.3 "no a priori prediction" → 2 sentences. §9 focuses on theorem + experiment, drops "not claiming" echo. | 4.5/5 | Defensive accretion — each v13-v30 round added hedges without global dedup. Repetition reads as lack of confidence. |
| 4 | §3 | **Theorem-box restructure**: §3 reordered to PRA convention. NEW order: §3.1 Main Result (Eq.4) → §3.2 Theorem (Proposition 1 + Corollary + Scope + Examples) → §3.3 Proof (Eqs 5-11) → §3.4 Reparameterization defense → §3.5 Physical Intuition → §3.6 Structural Blind Spot. Previously: proof appeared before theorem statement. Reader now encounters Proposition 1 before its proof. | 4.6/5 | Missing theorem-box pattern — PRA papers lead with boxed theorem, then proof follows. Proposition 1 was buried after 35 lines of proof mechanics. |
| 5 | §4.5 (NEW) | **Experimental feasibility**: NEW 8-line "Practical Feasibility" subsection after §4.4 Calibration. Coincidence rate ~1000/s (Bong 2020) → 91s per setting → 14 min data acquisition. Including calibration: ~1 hour total. SPDC brightness drift <5% over 30 min. Detector dark-count drift ~1% sub-dominant to Poisson. | 4.2/5 | Feasibility gap — protocol paper without back-of-envelope runtime estimate. Reviewer asks "can this actually be done?" |
| 6 | §3.4 (was §5.4) | **Reparameterization defense relocated**: Moved non-absorption proof from §5.4 to §3.4 (immediately after proof, before physical intuition). Expanded with explicit counterexample: "Under unitary basis redefinition |b'⟩ = U|b⟩, the correlator ⟨AB⟩ is invariant — unitary redefinitions produce δ⟨AB⟩ = 0 for all θ. In contrast, Eq.(2) modifies P multiplicatively with a factor depending on physical overlap |⟨b|d⟩|², which changes under θ-rotation." Three-point (a)/(b)/(c) structure preserved + S3 pointer. | 4.5/5 | Over-compression of critical defense — reparameterization objection is #1 reviewer attack. Now reader sees defense immediately after theorem. |
| 7 | §8.4 | **Multi-observer → S3**: "~11× amplification" multi-observer paragraph → replaced with 2-line pointer: "Multi-observer extensions are discussed speculatively in Supplemental S3; these require additional bridge theorems not established here." Full speculative analysis preserved in S3. | 4.3/5 | Speculative claim in main narrative — conditional amplification results from unproven bridge theorems. |
| 8 | §3.6, §9 | **Defensive tone reduction**: Cut all "obvious in hindsight" (2 instances: §3.6 L290 v30, §9 coda v30). Reduced "not claiming X" from 7 to 1 instance (ESP boundary only). §3.6 operational significance → factual: "The three-line proof confirms that θ has been experimentally unexplored." §8.3 "does not depend on this embedding" retained (informative, not defensive). | 4.4/5 | Missing tone pass — content-focused RCA accumulated anxiety markers without tone audit. |
| 9 | Abstract, §1, §9 | **Headline consolidation**: "equatorial fixed-point theorem" established as the paper's single headline. Abstract opens with theorem name + Proposition 1. §1 L34: "This paper establishes the equatorial fixed-point theorem (Proposition 1, §3)." A/B logical distinction preserved but A privileged: "The theorem (Claim A) is the central result; the experimental protocol (Claim B, §4-7) is its direct consequence." §9: leads with "The central result is the equatorial fixed-point theorem (Proposition 1)." | 4.5/5 | A/B split dilutes impact — defensive A/B structure (v27) masked clarity. Single headline privileges the theorem. |

### Structural changes (v31)
| Before (v30) | After (v31) | Nature |
|-------------|-------------|--------|
| §3.1 Main Result → §3.3 Structural Blind Spot → §3.2 Theorem → proof mixed in | §3.1 Main Result → §3.2 Theorem → §3.3 Proof → §3.4 Reparameterization → §3.5 Intuition → §3.6 Blind Spot | Theorem-first reorder |
| §5.4 Reparameterization defense | §3.4 (relocated to immediately after proof) | Defense colocation |
| No §4.5 | §4.5 Practical Feasibility (NEW) | Feasibility addition |
| §8.4 Multi-observer paragraph (5 lines) | 2-line S3 pointer | Speculation → supplement |

### Regression
Δ: C2+C6 repositioned; C7 moved to §3.5.

---

## v30 (2026-05-25) — 7-issue RCA: structural blind spot framing, Eq.(2) benchmark subordination, trivial-algebra defense, uniqueness scope, statistical conservatism, paper compression, terminology shift

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------| 
| 1 | Abstract, §1, §3 heading, §3.3, §10 | **Novelty reframing**: "appear insensitive" → "structural experimental blind spot" + "unprobed geometric degree of freedom". §3 heading: "Geometric Cancellation" → "Structural Blind Spot". §3.3 heading: "Structural Insensitivity at the Equator" → "Structural Experimental Blind Spot". Abstract leads with "share a structural experimental blind spot". §10: "geometric observation" → "structural experimental blind spot"; added "The algebra is obvious in hindsight; the experimental blind spot is not." | 4.2/5 | Novelty framed as absence of prior work instead of structural impossibility at equator. "Structural blind spot" + "unprobed degree of freedom" are substantive scientific claims, not marketing. |
| 2 | §2.3 Status, §3.1, §5.3 | **Eq.(2) benchmark subordination**: "test parametrization" → "benchmark parametrization" throughout (§2.3 core idea, IS-NOT, Status, GPT). §3.1: added "This result is model-independent...Eq.(2-3) is a benchmark parametrization for quantifying experimental sensitivity; the theorem holds for any overlap function." §2.3 core idea: added "The model-independent theorem (Proposition 1, §3) is the central result; Eq.(2-3) serves as a benchmark parametrization for quantifying experimental sensitivity." §5.3 header: "Outcome-Dependent Modifications" → "Overlap-Dependent Deformations"; opening: "model class" → "benchmark parametrization". | 4.3/5 | Eq.(2) over-defended as if it's THE result. Subordinating to "benchmark" makes theorem the star, Eq.(2) the measurement tool. |
| 3 | §3.3 | **Trivial-algebra defense**: "Although the algebra is compact...non-trivial" → "The algebra is obvious in hindsight...but the geometric degree of freedom θ has been experimentally unexplored...The simplicity of the proof is precisely why the blind spot persisted: equatorial measurement was adopted as a convention, not tested as a constraint." | 4.5/5 | 3-line proof risks "too obvious to publish". Preempt with "obvious but unexplored" — the simplicity IS the explanation for the blind spot. |
| 4 | §3.2 (after Corollary) | **Uniqueness scope boundary**: NEW 7-line "Scope limitation" paragraph. "Proposition 1 and its Corollary constrain the overlap-only class...Broader deformations — depending on the full density matrix, higher-order correlators, or non-geometric variables — lie outside this theorem's scope and remain open." | 4.4/5 | Reviewer: "what about deformations outside overlap-only class?" Explicit scope boundary prevents overstating universality while acknowledging open territory. |
| 5 | §6 Bayesian | **Statistical conservatism**: "modeling uncharacterized systematics as a multiplicative factor" → "modeling uncharacterized systematics (detector drift, waveplate miscalibration, correlated noise from source brightness fluctuations) as a multiplicative factor". | 4.0/5 | 5σ with β≈0.04 looks optimistic without naming specific degradation mechanisms. Three concrete sources now anchor the 20% inflation estimate. |
| 6 | §7, §8 (old) | **Paper compression**: §7.1-7.2 tables → inline summary (5 lines) with "Full μ and η tables in Supplemental S2". §7.3 systematic table → 4-line summary with "Full table in Supplemental S2". §7.4+detection loophole+false-positive+Bell analogy → compressed single-flow section. Old §8 (Loophole Analysis table) → merged into §7 as "Loophole summary" sub-table. Old §9 → §8, old §10 → §9. Net: ~85 lines removed. | 4.0/5 | Paper 7 pages for a 3-line-proof core idea. Robustness details belong in supplement; main text keeps summary + critical loophole defense. |
| 7 | Throughout | **Terminology shift**: "outcome-dependent coupling" → "overlap-dependent deformation" as running term. First use in §2.3 with explicit note: "previously termed 'outcome-dependent coupling' in preliminary drafts; the present name emphasizes geometric content over causal implication." "coupling strength" retained for β. §2.3 heading: "Outcome-Dependent Coupling" → "Overlap-Dependent Deformation". | 4.5/5 | "Outcome-dependent" sounds like hidden variables / retrocausal. "Overlap-dependent deformation" is geometrically precise and neutral. |

### Terminology shift (systematic)
| Term | Before (v29) | After (v30) | Sections affected |
|------|-------------|-------------|-------------------|
| Running term | "outcome-dependent coupling" | "overlap-dependent deformation" | Abstract, §1, §2.3, §3.1, §3.3, §5.3, §5.4, §8.1, §8.2, §8.4, §9 |
| Parametrization type | "test parametrization" | "benchmark parametrization" | §2.3 (core idea, IS-NOT, Status, GPT), §3.1, §5.3 |
| Novelty framing | "appear insensitive" / "structural insensitivity" | "structural experimental blind spot" | Abstract, §3 heading, §3.3 heading, §9 |

### Regression
Δ: C10+C11 NEW (terminology shift); C5 extended.

---

## v29 (2026-05-25) — 10-issue RCA: reviewer tone & positioning overhaul

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Header | **Version bump**: v28 → v29. | — | Tracking. |
| 2 | Abstract | **3-beat restructure**: "All published...share" → "Existing...appear insensitive to a geometric degree of freedom". Compressed from 15 → 10 lines. Removed intermediate proof steps; leads with observation, consequence, then limitations. | 4.5/5 | Abstract read as proof-of-theorem; reviewer wants concise pitch. 3-beat (observation → experiment → scope) is standard PRA abstract. |
| 3 | §1 | **Claim A soften**: "we prove that all existing...share" → "we show that existing EWF implementations appear insensitive to". | 4.2/5 | "Prove all" invites "but you didn't check X". "Show...appear" matches epistemic status (S1 audit-backed, not exhaustive). |
| 4 | §2.3 Status | **Compress**: 7 lines → 3 lines. Removed "Parametric frameworks routinely precede..." (redundant with SME cite). Single sentence: "Like SME, this is a test parametrization — a target, not a theory." | 4.3/5 | Defensive accretion from v14/v16 — reviewer reads repetition as uncertainty. |
| 5 | §2.3 GPT | **Compress**: 12 lines → 6 lines. Removed detailed constraint-mapping narrative. Kept: "simplest one-parameter deformation... preserves normalization, respects (i)-(iii), remains admissible." | 4.4/5 | v27 GPT bridge over-elaborated admissibility conditions. Compact version signals confidence. |
| 6 | §2.3 null test | **"new physics" → "departure from standard QM"**: "that would indicate new physics independently of which specific model class" → "that would indicate a departure from standard QM predictions independently of model class". | 4.6/5 | "New physics" is marketing language that invites rejection. "Departure from QM predictions" is operationally precise. |
| 7 | §3.3 (after proof) | **Operational significance bridge**: 4-line paragraph — "Although the algebra is compact (three-line proof), its experimental consequence is non-trivial: θ constitutes a previously unprobed geometric parameter..." | 4.0/5 | Gap between compact proof and experimental implications. Reader needs explicit "so what?" bridge. |
| 8 | §5.4 | **Compress**: 9 lines → 4 lines. Full argument moved to Supplemental S3; main text retains (a)/(b)/(c) summary with S3 pointer. | 4.1/5 | Defensive text that duplicates S3 content. Main text needs conclusion, not full proof. |
| 9 | §7.3 | **Detection loophole compress**: 25 lines → 8 lines (two-obs defense) + 13 lines → 12 lines (false-positive argument + fair-sampling + SNSPD merged). Net: −18 lines. Bell-test analogy sharpened to single reference [9]. | 4.5/5 | §7.3 was longest defense section (50+ lines). Redundant elaboration (future loophole-free scenarios, fair-sampling historical recap) removed; substance preserved. |
| 10 | §10 | **Conclusion focus**: 19 lines → 11 lines. "geometric theorem" → "geometric observation". Removed θ-sweep and cos θ functional dependence (already in §9.4). Two clean paragraphs: result + experiment. | 4.3/5 | Conclusion restated material from §3 and §9.4. Compact conclusion signals paper is tight and complete. |

### Regression
Δ: −54 lines (C9 Abstract 3-beat NEW; C6 GPT bridge compressed).

---

## v28 (2026-05-25) — 7-issue RCA: defense compression, physical intuition, universality scoping, sensitivity qualifiers, novelty softening

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **Heading + Core idea reframe**: "Outcome-Dependent Registration" → "Outcome-Dependent Coupling". Core idea uses "symmetry-constrained test parametrization" instead of "phenomenological parametrization". "any smooth function" → "any function" (Prop 1 already covers non-smooth). | 4.2/5 | "Registration" sounds ad hoc / phenomenological. "Coupling" + "test parametrization" aligns with SME analogy and signals no ontological commitment. |
| 2 | Abstract, §2.3, §3.2, §10 | **Universality scoping**: "ANY smooth function" → "any function" (lowercase, drop "smooth" since Prop 1 requires no smoothness). Proposition 1 title: "Universality of equatorial cancellation" → "Universality within overlap-only deformations". Added "overlap-only" qualifier throughout. | 4.4/5 | "ANY smooth g" overstates — reviewer could construct non-overlap dependence. Scoping to "overlap-only deformations" is precise and defensible. |
| 3 | §7, §1 | **Novelty softening**: "the first non-equatorial EWF measurement" → "to our knowledge, the first non-equatorial EWF measurement". §1 ESP boundary: added "to our knowledge" before "the first experimental test of this class". | 4.0/5 | Absolute novelty claims are attack surfaces. "To our knowledge" + S1-backed methodology is both honest and defensible. |
| 4 | §2.3 | **Defense compression (~33%)**: IS-NOT block (10 lines → 6): collapsed three negations into single compound sentence + pointer to S3. Contextuality block (10 lines → 5): removed "physical picture" narrative, kept classification + S3 pointer. Status block (13 lines → 7): compressed SME precedent paragraph by cutting redundant examples. Net: ~19 lines cut. | 4.6/5 | Defensive accretion inflated §2.3 to 80+ lines. Reviewer reads repetition as uncertainty. Compressed prose preserves all logical content while signaling confidence. |
| 5 | §3 (after Examples) | **Physical intuition paragraph**: 8 lines explaining WHY equatorial cancellation occurs. At θ=π/2, |⟨b|H⟩|²=|⟨b|V⟩|²=1/2 → Superobserver maximally symmetric w.r.t. Friend outcomes → indistinguishable from "no geometric relationship". Tilting breaks this → cos θ asymmetry. | 4.8/5 | Theorem is algebraically clear but physically opaque. Reviewers want to understand WHY, not just verify proof. Intuition bridges formalism to physical picture. |
| 6 | Abstract, §5.3, §10 | **Sensitivity qualifier**: "sensitivity β ≥ 0.04" → "order-of-magnitude sensitivity β ≥ 0.04". Added "(under idealized Poisson statistics; see §6)" to §5.3 threshold statement. | 4.0/5 | Bare "sensitivity" without qualifier invites challenge on systematics. "Order-of-magnitude" is honest and §6 provides Bayesian robustness analysis. |
| 7 | §1 | **Theorem preview**: Added 4-line preview after ESP boundary: "The geometric result itself is compact: f_perp(+1,H) − f_perp(−1,H) = −cos θ (Eq. 4). At θ = π/2, this vanishes for any function of the basis overlap (Proposition 1). The full proof is three lines (§3.2); §2 provides motivation and notation." | 4.3/5 | Reader currently waits until §3.2 to see the theorem. Preview in §1 rewards early reading and signals the paper has a clean, verifiable core result. |

### Terminology shift (systematic)
| Term | Before | After | Sections affected |
|------|--------|-------|-------------------|
| Registration | "outcome-dependent registration" | "outcome-dependent coupling" | Abstract, §1, §2.3, §5.3, §9.1, §9.2, §10 |
| Parametrization | "phenomenological parametrization" | "symmetry-constrained test parametrization" | §2.3 (IS-NOT, Status) |

### Regression
Δ: −3 lines (C7 Physical intuition NEW; C8 Theorem preview NEW).

---

## v27 (2026-05-25) — 6-issue RCA: GPT bridge, Proposition 1 (universality), Bayesian robustness, theorem-first positioning, novelty unification

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------| 
| 1 | §2.3 | **GPT/operational bridge expansion**: Replaced shallow POVM mention with explicit GPT framework [17] connection. Eq.(2) = simplest one-parameter deformation within GPT-admissible probability polytope. Constraints (i)-(iii) mapped to GPT admissibility conditions (basis-independence, QM recovery, geometric compatibility). 12 lines replacing 6. | 4.2/5 | "Why THIS modification?" — reviewer wants theoretical grounding deeper than "simplest parametrization". GPT framework provides operational justification without theory commitment. |
| 2 | Abstract, §1, §10 | **Theorem-first positioning**: Abstract restructured — geometry leads, model formula delayed. Proposition 1 cited in abstract. §1 L47-52: "Claim A — the geometric cancellation theorem — is the central result of this paper; Claim B — the experimental protocol — is its direct experimental consequence." §10: leads with "The central result of this paper is a geometric theorem" + Proposition 1 universality. | 4.5/5 | Paper strongest as "geometric blind spot" discovery, not "new outcome-dependent physics". Reviewer more likely to accept theorem than speculative model. |
| 3 | §3.2 | **Proposition 1 + Corollary (formalized universality)**: Replaced informal "Generality" paragraph with numbered Proposition 1: "For ANY function g: [0,1]→ℝ, the modification factor is outcome-independent at θ=π/2." Added Corollary: "No overlap-only deformation evades equatorial cancellation." Added third example g(x)=(1−x)^n. | 4.6/5 | "Infinitely many other deformations exist" — Proposition 1 proves ALL of them cancel at equator. Addresses uniqueness concern by showing the cancellation is universal, making the specific choice of g irrelevant. |
| 4 | §6 | **Bayesian robustness estimate**: 6-line quantitative paragraph. 20% systematic inflation → ~6.5σ effective LF significance, β_min≈0.046. FOM plateau survives up to ~40% inflation. | 4.0/5 | "8.6σ Poisson-only is optimistic" — reviewer wants realistic systematics. Quantitative estimate (not just qualitative v26 recommendation) shows experiment robust under substantial degradation. |
| 5 | §3.3 | **Novelty hedge unification**: Replaced 3-line double-hedged statement ("we are unaware of any...the polar angle does not appear to have been varied") with single sentence: "Within the surveyed literature (S1), we find no published EWF experiment that varies θ from π/2." Single hedge, single sentence. | 4.0/5 | Oscillating strong/soft novelty claims across v17/v19/v25 — unified to one consistent voice. Preserves substance while minimizing attack surface. |
| 6 | Abstract | **Proposition 1 in abstract**: "This cancellation holds for ANY smooth function g of the basis overlap, not just the specific form Eq.(3) (Proposition 1)." Signals universality from first read. | 4.3/5 | Abstract previously pitched specific model; now pitches universal geometric theorem — aligned with "blind spot" positioning. |

### New reference
| # | Reference |
|---|-----------|
| [17] | J. Barrett, Phys. Rev. A 75, 032304 (2007). — GPT framework for operational quantum foundations. |

### Regression

---

## v26 (2026-05-25) — 8-issue RCA: POVM bridge, non-absorption proof, naturalness, stats, S3 move, theorem-first

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **POVM/operational bridge**: 6-line "Operational framing" paragraph connecting Eq.(2) to minimal symmetry parametrization of POVM statistics. Emphasizes constraints (i)-(iii) → simplest Born-rule deformation. No theory commitment. | 4.3/5 | "Why THIS modification?" — connects to generalized measurement theory without committing to reconstruction program. |
| 2 | Abstract, §3.3 | **Novelty softening**: Abstract "property" → "insensitivity". §3.3 L262-264: "no EWF experiment has been performed at θ ≠ π/2 for any purpose" → "we are unaware of any EWF experiment performed at θ ≠ π/2". Softens absolute negative while preserving S1-backed methodology. | 4.0/5 | "No prior work identified θ" too strong → soften without regressing v19 systematic-search hedge. |
| 3 | §5.4 (NEW) | **Non-absorption proof**: 3-point argument why Eq.(2) cannot be absorbed into measurement redefinition: (a) unitary preserves trace → δ=0, (b) outcome-pair asymmetry absent from symmetric POVM, (c) θ-sweep empirical discriminator. | 4.4/5 | "This is just adding a bias term" → formal proof it's not gauge-away-able. |
| 4 | §5.3 | **Scale context/naturalness**: 5-line paragraph. Null result at β ≥ 0.04 excludes O(1)/O(10⁻¹). SME comparison (10⁻²³ after decades). First β constraint at ~10⁻² = new parameter space opening. N=200k extends to β ≥ 0.02. | 4.2/5 | β free parameter without natural scale → frame as discovery-phase constraint + scale comparison. |
| 5 | §6, §7.3 | **Statistical robustness**: (a) 10-line "Statistical model limitations" paragraph in §6: Poisson idealization, recommend bootstrap + detector-drift sim. (b) 5-line correlated-systematic note in §7.3: QWP+detector co-variance unmodeled, recommend time-stamped auxiliary data. | 4.0/5 | Sigma estimates "too clean" → acknowledge model limitations + recommend implementing-lab validation. |
| 6 | §2.3 → S3 | **Defense text → supplement**: Moved 25-line contextuality comparison + physical picture from §2.3 to new S3_interpretations.md. Replaced with 10-line compact reference. Net: −15 lines from main text. | 4.1/5 | Paper too long for PRA → move interpretation/philosophy to supplement, keep theorem centerpiece. |
| 7 | Abstract | **Null-test framing**: "structural property" → "structural insensitivity". Aligns abstract with null-test pitch throughout paper. | 4.0/5 | "Foundations speculation" rejection risk → pitch as geometric null test, not new physics of observers. |
| 8 | §3.1 | **Theorem emphasis**: "3.1 — Statement" → "3.1 — Main Result". Combined with Issue 6 compression, theorem becomes visual centerpiece. | 4.2/5 | Theorem buried under phenomenology → theorem-first narrative. |

### Supplemental changes
| # | File | Change |
|---|------|--------|
| S3 | S3_interpretations.md (NEW) | Proper S3 with 4 sections: contextuality comparison (from §2.3), physical picture (from §2.3), quantum interpretations (5 frameworks), multi-observer extension. |
| S3 | manuscript.md L58-60 | S3 description updated: "quantum interpretations, contextuality comparison, and measurement incompatibility physical picture". |

### Regression

---

## v25 (2026-05-25) — 12-point review RCA: tone, contextuality, systematics, discriminator

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract, §1, §3.3, §10 | **Tone softening**: "geometric blind spot" → "structural insensitivity" (4 instances). "first test" → "targeted test". "opens a new axis" → "accesses a previously unprobed geometric degree of freedom". §3.3 heading renamed. | 4.3/5 | Reviewer foundations dị ứng strong marketing wording. Inconsistent softening across sections after v22 only touched §1/§3.3. |
| 2 | Abstract | **A/B distinction**: explicit "Claim A (model-independent theorem)" / "Claim B (null test)" labels in abstract. Mirrors §1 L38-53 structure. | 4.1/5 | Abstract mixed model-independent and assumption-dependent claims without distinction. |
| 3 | §2.3 | **Contextuality comparison**: 13-line paragraph distinguishing Eq.(2) from (a) Kochen-Specker contextuality (no hidden λ), (b) retrocausality, (c) standard measurement contextuality. Dependence is on registration geometry, not measurement context. | 4.2/5 | Reviewer certain to ask "how is this different from contextuality?" v18 IS-NOT paragraph says what Eq.(2) is NOT, but never names Kochen-Specker explicitly. |
| 4 | §3.3 | **Novelty softening**: "To date, no EWF experiment" → "Within the literature surveyed (Supplemental S1), no EWF experiment". Ties claim to methodology. | 4.0/5 | v17 absolute statement ("no EWF experiment has been performed... for any purpose") maximally vulnerable. v19 hedge one paragraph above insufficient. |
| 5 | §5.3 | **Explicit discriminator**: "Standard QM predicts δ⟨AB⟩ = 0 for all θ. Model class predicts δ⟨AB⟩ ∝ β cos θ." Crisp mathematical statement + "not a reparameterization" defense. | 4.5/5 | "Is this genuinely beyond QM?" — discriminator described in prose but never as a displayed statement. |
| 6 | §7.3 (NEW) | **Systematic-error budget table**: 6 sources (QWP drift, birefringence, polarization-dependent loss, calibration offset, detector asymmetry, accidentals). All sub-dominant to σ ≈ 0.0017. Directional argument: all bias δ toward zero, not away. | 4.4/5 | Experimental reviewer will demand consolidated error budget. Individual systematics addressed in v18/v20/v24 but never tabulated. |
| 7 | §10 | **Conclusion reframed**: null-test framing lead. θ-sweep reference added. "Fix:" imperative removed. "A single waveplate opens a new axis" → "accesses a previously unprobed geometric degree of freedom." | 4.0/5 | §10 did not mirror §2.3 null-test framing (v18). |
| 8 | Abstract | **Slimmed**: 15 lines → 12 lines. Removed β ≥ 0.07, μ ≥ 0.92, Δθ ≤ ±5° (moved to body). Kept 8.6σ, β ≥ 0.04, θ = 31°, fair-sampling. | 4.0/5 | 7 numbers in abstract overwhelms first-time reader. |
| 9 | Abstract | **"All existing" → "All published"**: minimal defensive qualifier. | 3.5/5 | Below threshold but costless and ties to S1 audit scope. |
| 10 | §10 | **θ-sweep emphasis**: 1 sentence referencing cos θ functional dependence and θ ∈ [20°, 55°] range (§9.4). | 3.8/5 | Below threshold but user explicitly flagged. Added in §10 only (abstract already dense). |

### Rejected changes (below threshold)
| # | Review Point | RCA Score |
|---|-------------|-----------|
| R2 | "All existing" → "Existing canonical optical EWF implementations" | 3.0/5 |

### Regression

---

## v24 (2026-05-25) — §2.3 succinct opening + search pipeline + temperature detail

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **Executive summary** at top of §2.3: "Core idea" paragraph front-loading the answer to "why this class?" — parametrize via β, form follows from 3 physical constraints (rotation invariance, alignment limit, monotonicity), simplest representative, no theory predicts it, SME-analogous parametric test. | 4.2/5 | §2.3 buried the lede: meta-commentary ("Before presenting the theorem…") before substance. Reviewer asks "why this class?" and has to read 20 lines. Fix: answer in 2 sentences, then elaborate. |
| 2 | §3.3 | **Screening pipeline** in main text: "title/abstract filtering → full-text examination of 47 candidate documents → targeted follow-up on citing/cited works." Bridges gap between "~200 screened" and full S1 audit. | 4.0/5 | "~200 papers is small" — reviewer can't assess coverage without seeing methodology. Main text showed *what* was searched but not *how*. Fix: summarize pipeline stages. |
| 3 | §4.2 | **Temperature insensitivity**: "retardance temperature coefficient ~0.01 nm/°C; lab ΔT ±2°C → ~0.02 nm drift, well within ±2 nm tolerance." | 4.0/5 | Standard experimental parameter missing. Preempts reviewer question about thermal effects on retardance. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score |
|---|-------------|-----------|
| R1 | QWP position detail | 2.5/5 |
| R2 | Lab availability | 2.0/5 |

### Regression

---

## v23 (2026-05-25) — Generality examples + loophole bridge sentence

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.2 | **Concrete examples** for universality claim: g(x) = x² → g(1/2) = 1/4 (constant, cancels in Z); g(x) = sin(πx) → g(1/2) = 1 (constant). Makes “holds for ANY g” verifiable by reader. | 4.2/5 | Proof completeness gap: universality claim without illustrative verification. Pure math, zero regression risk. |
| 2 | §7.3 | **Bridge sentence** connecting directional argument (“η < 0.91 cannot produce false positives”) to Bell-test precedent: “Analogous to first-generation Bell tests…the present proposal yields scientifically productive results under fair-sampling.” | 4.0/5 | Fragmented exposition: directional argument (v20) and Bell precedent (v15) written in separate rounds, lacked connecting sentence. |

### Regression

---

## v22 (2026-05-25) — Intuitive gloss + structural blind-spot explanation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **Parenthetical gloss** of "outcome-dependent" at first structural use (L41-44): "a Superobserver's measurement statistics depend not only on the quantum state, but also on the geometric relationship between the Superobserver's measurement basis and a prior observer's recorded outcome." | 4.0/5 | Novel coinage used 7 times before §2.3 explains it. Non-specialist readers lost before technical definition. |
| 2 | §3.3 | **Structural explanation** for why community fixed θ=π/2 (L240-246): "LF inequalities optimized for maximal violation at equatorial settings. Without a θ-hypothesis, no incentive to explore polar direction." | 4.5/5 | "Why hasn't anyone thought of this?" — converts claim from insulting to sympathetic structural observation. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score |
|---|-------------|-----------|
| R1 | Supplementals S1-S3 not in file | 2.0/5 |

### Regression

---

## v21 (2026-05-25) — μ-threshold fix + honest abstract + §9.2→S3

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract | **μ threshold 0.86→0.92(5σ)**. Detection loophole: "is discussed" → "operates under fair-sampling assumption (η ≈ 0.87); loophole closure requires SNSPD upgrade (η ≥ 0.91)". | 4.0/5 | Evasive abstract language contradicts honest §7.3 analysis. Also fixes μ threshold to match §7.1 correction. |
| 2 | §7.1 | "Threshold μ ≈ 0.86" → "Positive violation onset at μ ≈ 0.86; 5σ significance requires μ ≥ 0.92." | 4.5/5 | Internal inconsistency: text said "threshold 0.86" but table showed 0.1σ at μ=0.86. Clarify onset vs 5σ. |
| 3 | §9.2 | **MOVED** MWI + RQM paragraphs → Supplemental S3 reference. 14 lines → 5 lines. "interpretation-neutral by design." | 4.0/5 | Speculative interpretation claims create reviewer attack surface. S3 already exists. |

### Regression

---

## v20 (2026-05-25) — f_perp class-representative framing + η-direction analysis

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | Restructured f_perp motivation: "Any smooth function…same leading-order structure; Eq.(3) is the simplest representative of this class, not its unique member" as **opening sentence**. "Absorbing c₁ into β yields" → "Adopting the simplest representative and absorbing c₁ into β". | 4.5/5 | "Three conditions don't uniquely determine f_perp" → make class-representative framing the lead, not a buried subordinate clause |
| 2 | §7.3 | NEW paragraph: "Can detector inefficiency fake a β signal?" — directional analysis showing η bias suppresses cos θ signal (toward zero) rather than enhancing it. QWP transmission >99% at 810nm → no additional loss. Conclusion: η < 0.91 cannot produce false positives for β. | 4.0/5 | "Detection loophole gap for β measurement" → explicit directional argument that η insufficiency cannot mimic positive β |

### Rejected changes (below threshold)
| # | Review Point | RCA Score |
|---|-------------|-----------|
| R2 | Figure placeholders | 2.0/5 |
| R3 | Question-format title | 2.5/5 |

### Regression

---

## v19 (2026-05-25) — Physical intuition + §2.3 compression + novelty hedge

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §7.3 | Fair-sampling β meaning: +"β constraint applies to detected subset under fair-sampling. If future loophole-free confirms → validated. If disagrees → reinterpret as detection-efficiency-dependent effect (itself new physics)." | 3.5/5 | Clarify what fair-sampling β means AND doesn't mean |
| 2 | §2.3 | Physical intuition paragraph: measurement incompatibility between observers. Friend produces record with Bloch sphere orientation. Superobserver probes at relative angle via \|⟨b\|d⟩\|². QM factorization assumption → no dependence. Eq.(2) parametrizes residual geometric dependence. | 4.0/5 | "Outcome-dependent registration là gì về mặt vật lý?" → geometric measurement incompatibility |
| 3 | §2.3 | **Compressed** constraints (i-iii) from 3 bullet paragraphs → 4-sentence inline paragraph. Merged expansion + scope limitation. ~35 lines → ~15 lines. | 3.5/5 | "Đọc như reverse-engineering" → compact presentation, less "justify ngược" feel |
| 4 | §3.3 | Novelty hedge: "To the best of our knowledge" → "Based on the systematic search documented in Supplemental S1, we find no evidence" | 3.0/5 | Tie claim to methodology, not personal knowledge |

### Regression

---

## v18 (2026-05-25) — Ontological clarity + null test framing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | Ontological classification: Eq.(2) explicitly defined as phenomenological parametrization — NOT hidden-variable, NOT collapse modification, NOT observer interaction. Parametrizes "basis alignment dependence" that QM marginalizes over. | 4.5/5 | "Outcome-dependent registration là khái niệm mơ" → classify what it IS NOT |
| 2 | §2.3 | Null test framing: "Standard QM predicts the same LF violation regardless of θ. If θ-dependent signal detected → new physics regardless of model class. Primary result = θ-dependence, not β value." | 4.5/5 | Deflect "tại sao class này?" → experiment tests θ-dependence, class just quantifies sensitivity |
| 3 | §4.2 | "only hardware change" → "only **optical** hardware change" + SNSPD replaces existing detectors at same position. | 4.0/5 | Fix internal contradiction: SNSPD ≠ "no new components" without qualification |
| 4 | §4.1 | θ=31° trade-off explanation: θ→0° → signal max but LF violation weakens (settings collapse). θ→90° → LF max but signal vanishes. 31° = intermediate balance. Broad plateau means exact optimum not critical. | 4.0/5 | "Tại sao θ=31°?" → physical trade-off, not just numerical optimization |

### Regression

---

## v17 (2026-05-25) — Reviewer defense round 2

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §7.3 | Detection loophole: two-observation defense. (a) Geometric confirmation of LF violation at θ=31° is model-independent and new regardless of loophole closure. (b) β and LF violation measured from SAME coincidence set → self-consistent constraint independent of absolute efficiency. | 5.0/5 | "Prove được gì mới so với Bong 2020?" |
| 2 | §2.3 | Constraints (i)-(iii) explicitly stated as NOT exhaustive — minimal set for one-parameter family. Other dependence structures (density matrix, higher-order correlators) lie outside scope. | 3.5/5 | Defend against "circular motivation" |
| 3 | §3.3 | "No EWF experiment has been performed at θ≠π/2 for any purpose — the polar angle has not been varied in any published EWF experimental configuration." | 3.5/5 | Explicit negative statement backed by S1 audit |
| 4 | §5.3 | β physical meaning: "The dimensionless coupling β has no a priori theoretical prediction. The experiment's role is to measure or constrain β; the role of a future theory is to predict or be excluded." | 4.0/5 | Honest admission — clear role separation |

---

## v16 (2026-05-25) — Reviewer defense round 1

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | `supplemental/` | **NEW: `S1_search_audit.md`** — reproducible search log: 4 databases, Boolean query strings, 5-stage screening, 18+ documents full-text examined, targeted follow-up searches, limitations. | 5.0/5 | "Cho tôi xem search log" — now answerable |
| 2 | §2.3 | SME precedent: +"at the time of its introduction" + "Parametric frameworks routinely precede microscopic theories: Fermi, SME, EFT all began as organizing parametrizations." | 4.0/5 | SME in 1997 had no string theory behind it |
| 3 | §7.3 | +"As an experimental proposal, this work identifies the detection efficiency requirement; closing the loophole is a task for the implementing laboratory." | 3.5/5 | Explicit proposal framing |
| 4 | §4.1 | θ-sensitivity in main text: FOM values at θ=20° (9.6), 31° (8.6), 45° (7.1), 58° (5.0), 90° (0). ±11° tolerance window. | 4.5/5 | "Tại sao θ=31°?" → show landscape |

---

## v15 (2026-05-25) — RCA reviewer defense

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §9.3 | **REMOVED: "VVV-QMRF K9_E postulate"** → "framework of measurement registration" | 5.0/5 | Proprietary name from independent researcher = red flag |
| 2 | §7.3 | Detection loophole: +42-year Bell precedent + 11-term implausibility argument | 3.3/5 | Replace assertion with historical precedent |
| 3 | §3.3 | Search methodology: +Boolean search strings + date range Jan 2000–May 2026 | 3.3/5 | Transparency for verification |
| 4 | §9.4 | Expanded: 1 bullet → 4 paragraphs (θ-sweep, multi-observer, platform independence, locality closure) | 4.0/5 | Show paper opens a research program |

---

## v14 (2026-05-25) — SME precedent + references

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | SME precedent paragraph + cite Colladay & Kostelecký 1997 [15] | 4.0/5 | Primary defense against "ad hoc class" |
| 2 | §7.3 | SNSPD upgrade path + cite Marsili et al. 2013 [16] | 3.3/5 | Concrete solution for detection loophole |
| 3 | §9.3 | +"The experiment does not depend on this embedding — it tests the class regardless of theoretical interpretation." | 3.5/5 | Separate parametric test from VVV-QMRF |
| 4 | Refs | +[15] Colladay & Kostelecký, PRD 55, 6760 (1997). +[16] Marsili et al., Nat. Photonics 7, 210 (2013) | — | Support F1 and F2 |

---

## v13 (2026-05-24) — Title + ESP framework audit

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Title | "Geometric Blindness in EWF Experiments: A Single-Waveplate Test" → **"Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?"** | — | Question format, stronger hook |
| 2 | §1 | ESP boundary statement: "This paper does not claim that outcome-dependent registration exists in nature..." | 4.6/5 | ESP mandatory — externalize boundary |
| 3 | §9.3 | **REMOVED: Eq.(12)** (K-space notation) → prose description | 4.4/5 | Dual-audience tension resolved |
| 4 | — | ESP audit: 25/26 gates. F2 (next-order question in §10) rejected at 3.6/5 | — | §9.4 already fulfills |

---

## v12 (2026-05-24) — Baseline

| # | Section | Change |
|---|---------|--------|
| 1 | §5.3 | **CRITICAL: Eq.(12) bug fixed.** Analytical |cos θ|/2 replaced with exact numerical density matrix computation. Correct thresholds: |δ|=0.0057 at β=0.05, |δ|=0.0080 at β=0.07. β_min(combined)≈0.038, β_min(single)≈0.075. |
| 2 | §2.3 | Motivation moved BEFORE theorem (§3) — reads as motivation, not post-hoc justification |
| 3 | §5.3 | β gap explained: √4 improvement from combining 4 settings |
| 4 | §3.3 | Literature search: "~200 papers screened." Caveat at BEGINNING of claim |
| 5 | `supplemental/` | S1 (full proof), S2 (derivation), S3 (interpretations) created |

---

---

## Recurring Rejected Changes

These objections recurred across ≥4 versions. Each was RCA-scored <4.5/5 every time and is documented once here rather than re-argued per version.

| Topic | Versions Rejected | Root Cause |
|-------|-------------------|------------|
| **β/Eq.(2) ad-hoc — needs physical/ontological motivation** | v30, v32, v33, v36, v39, v40, v41, v43, v44, v45, v48, v52 | Multi-layer defense already: C10 benchmark terminology (v30), lowest-order expansion (v38), phenomenological (v39), measurement disturbance (v32), registration-memory coupling (v36). ESP boundary (C1) prohibits claiming existence in nature (v13). |
| **Paper too long — cut 20-30%** | v39, v40, v43, v44, v45, v48, v52 | Paper already compressed to ~642 lines (~5 pages) via 12+ rounds of cuts (v29 −54L, v30 −26L, v31 −19L, v35 −27L, v43 −3L, v45 −11L, v51 −12L). No large removable blocks remain. |
| **"First"/novelty overclaim — soften further** | v38, v40, v41, v44, v45, v46, v51, v52 | S1 qualifier (C3) applied to all 5 claim locations (v38); "first isolated test" (v41); "new window" (v51). Existing hedging is methodology-backed (S1 audit). |
| **"Just basis rotation" — cosθ is gauge artifact** | v41, v42, v46, v48 | Lemma 1 (v37 formalized) + operational invariant (v42) + forward-ref (v41) + repositioned adjacent to Prop 1 (v46) — 4 defense layers. |
| **Missing killer figure (Bloch sphere)** | v37, v39, v45, v48, v52 | Fig ref exists in §3.5 (v37). Cannot create images in text. |
| **Overlap-only class lacks physical motivation / add toy model** | v33, v36, v37, v45, v48 | ESP boundary (C1): paper does not claim existence in nature. Theorem is structural, not theory-derived. |
| **GPT/contextuality/weak-measurement too speculative** | v39, v43, v44, v45 | GPT derivation → S3 (v37); conceptual chain compressed ~55% (v43). Main text retains 3-4 compact conceptual lines. |

---

## Version summary

| Version | Date | Focus | ~Lines | Δ | Refs |
|---------|------|-------|--------|---|------|
| v12 | 2026-05-24 | Baseline — Eq.(12) fix | ~600 | — | 14 |
| v13 | 2026-05-24 | Title + ESP audit | ~600 | 0 | 14 |
| v14 | 2026-05-25 | SME precedent + SNSPD | ~600 | 0 | 16 |
| v15 | 2026-05-25 | RCA defense (VVV-QMRF, loophole, search, §9.4) | ~600 | 0 | 16 |
| v16 | 2026-05-25 | Reviewer defense 1 (S1 audit, θ-sensitivity) | ~600 | 0 | 16 |
| v17 | 2026-05-25 | Reviewer defense 2 (2-obs loophole, constraint scope, β meaning) | ~600 | 0 | 16 |
| v18 | 2026-05-25 | Ontological clarity + null test framing | ~600 | 0 | 16 |
| v19 | 2026-05-25 | Physical intuition + §2.3 compression + novelty hedge | ~600 | 0 | 16 |
| v20 | 2026-05-25 | f_perp class-representative + η-direction | ~600 | 0 | 16 |
| v21 | 2026-05-25 | μ-threshold fix + honest abstract + §9.2→S3 | ~600 | 0 | 16 |
| v22 | 2026-05-25 | Intuitive gloss + blind-spot explanation | ~600 | 0 | 16 |
| v23 | 2026-05-25 | Generality examples + loophole bridge | ~600 | 0 | 16 |
| v24 | 2026-05-25 | §2.3 succinct opening + search pipeline + temperature | ~600 | 0 | 16 |
| v25 | 2026-05-25 | 12-point RCA: tone, contextuality, systematics, discriminator | ~600 | 0 | 16 |
| v26 | 2026-05-25 | POVM bridge, non-absorption proof, naturalness, stats, S3 move | ~600 | −15 | 16 |
| v27 | 2026-05-25 | GPT bridge, Proposition 1, Bayesian, theorem-first, novelty unification | ~600 | 0 | 17 |
| v28 | 2026-05-25 | Defense compression, physical intuition, universality scoping | ~600 | −3 | 17 |
| v29 | 2026-05-25 | Tone overhaul: defensive compression, "new physics" removal | 652 | −54 | 17 |
| v30 | 2026-05-25 | Blind spot framing, benchmark subordination, trivial-algebra, scope, terminology | 626 | −26 | 17 |
| v31 | 2026-05-25 | Novelty softening, Eq.(2) repositioned, thesis cuts, theorem-box, feasibility | 607 | −19 | 17 |
| v32 | 2026-05-25 | Uniqueness+disturbance, δ⟨AB⟩=0 no-go, sensitivity range, theory-space reframing | 634 | +27 | 17 |
| v33 | 2026-05-25 | Simplest hedge, passive-relabeling soften, SME→phenomenological, de-echo | 638 | +4 | 17 |
| v34 | 2026-05-25 | Abstract compress, §2.3 de-lawyer, S1-tied softening, Prop 1 formalization | 627 | −11 | 17 |
| v35 | 2026-05-25 | §3.4 compress, de-overpack (interpretation→S3, search compress) | 600 | −27 | 17 |
| v36 | 2026-05-25 | GPT deepened, β coupling, weak measurement [18], cosθ smoking-gun, S2 moves | 603 | +3 | 18 |
| v37 | 2026-05-25 | EFT-style, Lemma 1 formalized, survey table, soften, β ecosystem, null-point | 630 | +27 | 18 |
| v38 | 2026-05-25 | Survey-qualified hedging, lowest-order justification, novelty-as-geometry | 635 | +5 | 18 |
| v39 | 2026-05-25 | Cancellation rename, §1 reframe (overlooked→structural consequence), ontological→phenomenological | 639 | +4 | 18 |
| v40 | 2026-05-25 | overlooked→not-previously-isolated, non-identifiability, conservative β headline | 643 | +4 | 18 |
| v41 | 2026-05-25 | Lemma 1 forward-ref, operational β definition, "first isolated test" hedging | 648 | +5 | 18 |
| v42 | 2026-05-25 | GPT contextuality chain, Lemma 1 operational invariant, β scale bridge, Abstract 1+1+1 | 655 | +7 | 18 |
| v43 | 2026-05-25 | GPT/weak-meas cut ~40%→S3, φ-scramble control, correlator table→S2 | 652 | −3 | 18 |
| v44 | 2026-05-25 | Structural non-identifiability reframe, contextuality distinction, feasibility softening | 664 | +12 | 18 |
| v45 | 2026-05-25 | Proposition 1 on page 1, historical reason, intro compressed −21% | 653 | −11 | 18 |
| v46 | 2026-05-25 | Lemma 1 moved §3.4→§3.2, section renumber | 653 | 0 | 18 |
| v47 | 2026-05-25 | C3 regression fix (§9), §5.3 dedup, §8.4→§8.3 renumber | 650 | −3 | 18 |
| v48 | 2026-05-25 | "geometric null point" hook in §1 ¶2 | 650 | 0 | 18 |
| v49 | 2026-05-25 | §2.3 double "Equation (2)" fix — rolled into v50 | — | — | 18 |
| v50 | 2026-05-25 | Abstract "null point", φ-scramble forward-ref, Conclusion call-to-action, §8.1 logic fix | 654 | +4 | 18 |
| v51 | 2026-05-25 | β-model subordinated to theorem, "first"→"new", §6 compressed 30→13 lines | 642 | −12 | 18 |
| v52 | 2026-05-25 | De-defensify — 2 "model-independent" removed, ESP tightened | 642 | 0 | 18 |

---

## Regression Constraint Master (canonical — all versions reference this)

| ID | Constraint | Origin | Latest Status |
|----|-----------|--------|---------------|
| C1 | ESP boundary (§1): "This paper does not claim..." | v13 | ✅ Active |
| C2 | Proposition 1 math content unchanged | v27 | ✅ Active |
| C3 | Novelty hedge: "Within the surveyed literature (S1)" | v25 | ✅ Active |
| C4 | §8.2 interpretation-neutrality: "interpretation-neutral by design" | v17 | ✅ Active |
| C5 | §6 Bayesian robustness | v26 | ✅ Active (mechanism names added v30; 3-part methodology named v37) |
| C6 | GPT bridge [17] | v27 | ✅ Active (deepened v36; GPT derivation → S3 v37) |
| C7 | Physical intuition (§3.5) | v28 | ✅ Active (extended v32 observer-record alignment; compressed v35; fig ref v37) |
| C8 | Theorem preview (§1) | v28 | ✅ Active |
| C9 | Abstract 3-beat structure (observation→theorem→consequence→experiment→scope) | v29 | ✅ Active |
| C10 | "benchmark parametrization" terminology | v30 | ✅ Active |
| C11 | "overlap-dependent deformation" terminology | v30 | ✅ Active |
| C12 | Exact numerical values from v12 density-matrix computation | v12 | ✅ Active |
| C13 | §2.3 Core idea ↔ constraint derivation harmonized (unique→simplest hedge v33; Eq.(2) measurement disturbance v32) | v32 | ✅ Active |
| C14 | Theory-space constraint framing across Abstract/§3.6/§9 | v32 | ✅ Active (S1-tied v34; null-point narrative v37) |
| C15 | Practical sensitivity range β∼0.05–0.10 (single), β∼0.04–0.06 (combined) | v32 | ✅ Active |
| C16 | S1-tied novelty softening (§9) | v34 | ✅ Active |
| C17 | GPT/weak-measurement detail in main text → S3 (content preserved in supplement) | v36 | ✅ Active (extended v37) |
| C18 | Lemma 1 (Non-Absorption) formalized in §3.4 | v36 | ✅ Active (extended v37 QED) |
| C19 | All v35 regression constraints (16 items) | v35 | ✅ All preserved |
| C20 | smoking-gun→distinctive signature (§3.1, §5.3): "cannot"→"distinct from" | v36 | ✅ **Corrected v37** (v36 overreach fixed) |
| C21 | v32-specific §2.3↔L129 + §3.4↔§2.3 + theory-space alignment + practical↔Bayesian consistency | v32 | ✅ All harmonized |

**Usage:** Each version entry below references this master. Only items whose STATUS CHANGED or were NEWLY ADDED in that version are listed inline. All other items are `✅ All canonical constraints preserved — see Master.`

---

## RCA methodology

All v13→v37 changes applied via:
1. **5-step RCA** (Define → Trace → Isolate → Fix cause → Verify) per CLAUDE.md Rule Zero
2. **5-Whys** root cause drill (minimum 3 iterations per issue)
3. **Scoring ≥4/5** threshold for mandatory implementation
4. **ESP framework** (Epistemic-Structural-Presentational) for structural audit
5. Fixes scoring 3.0–3.9/5 implemented when user explicitly flagged concern AND fix cost negligible (≤3 sentences)

---

*Generated 2026-05-25. Covers v12 (baseline) through v44 (current).*
