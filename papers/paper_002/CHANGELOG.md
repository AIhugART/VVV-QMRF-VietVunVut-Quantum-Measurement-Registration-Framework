# CHANGELOG — "Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?"

**Paper ID:** paper_002 | **Target:** arXiv quant-ph → Phys. Rev. A
**Author:** VietVunVut (Viet — Nguyen Xuan)

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (L57-60) | ✅ Preserved — "This paper does not claim..." unchanged |
| v27 Proposition 1 math (L180) | ✅ Preserved — f_perp equation and proof identical |
| v25 novelty hedge (§3.3) | ✅ Preserved — "Within the surveyed literature (S1)" unchanged |
| v17 §9.2 interpretation-neutrality | ✅ Preserved — "interpretation-neutral by design" unchanged |
| v26 §6 Bayesian robustness | ✅ Preserved — no changes to §6 content |
| v27 GPT bridge [17] | ✅ Preserved — compressed but substance and reference intact |
| v28 physical intuition (§3) | ✅ Preserved — 8-line paragraph unchanged |
| v28 theorem preview (§1 L52-55) | ✅ Preserved — preview paragraph unchanged |

### Net line count
| Metric | Before (v28) | After (v29) | Delta |
|--------|-------------|-------------|-------|
| Abstract | 15 lines | 10 lines | −5 |
| §1 Claim A | 2 lines | 2 lines | 0 (wording only) |
| §2.3 Status | 7 lines | 3 lines | −4 |
| §2.3 GPT | 12 lines | 6 lines | −6 |
| §3.3 operational bridge | 0 lines | 4 lines | +4 |
| §5.4 | 9 lines | 4 lines | −5 |
| §7.3 detection loophole | 50 lines | 20 lines | −30 |
| §10 Conclusion | 19 lines | 11 lines | −8 |
| **Net** | **706 lines** | **652 lines** | **−54 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (L57-61) | ✅ Preserved — added theorem preview + "to our knowledge" without altering ESP structure |
| v27 Proposition 1 math | ✅ Preserved — only title and surrounding prose changed; mathematical content identical |
| v25 novelty hedge (§3.3) | ✅ Preserved — no changes to §3.3 novelty sentence |
| v17 §9.2 interpretation-neutrality | ✅ Preserved — only "registration" → "coupling"; no theory claims added |
| v26 §6 Bayesian robustness | ✅ Preserved — no changes to §6 content |

### Net line count
| Metric | Before (v27) | After (v28) | Delta |
|--------|-------------|-------------|-------|
| §2.3 IS-NOT block | 10 lines | 6 lines | −4 |
| §2.3 Contextuality block | 10 lines | 5 lines | −5 |
| §2.3 Status block | 13 lines | 7 lines | −6 |
| Physical intuition (§3) | 0 lines | 8 lines | +8 |
| Theorem preview (§1) | 0 lines | 4 lines | +4 |
| **Net** | — | — | **−3 lines** |

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

### Rejected changes (below threshold)
None — all 6 issues scored ≥ 4.0/5.

### Regression check
- v13 ESP boundary (L54-58): PRESERVED — "This paper does not claim..." unchanged
- v14 SME precedent (L156-168): PRESERVED — full SME paragraph + Fermi/EFT precedent untouched
- v15 VVV-QMRF removal: PRESERVED — no re-addition
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED — main text pipeline summary + FOM values untouched
- v17 constraints "not exhaustive" (L128) + β meaning: PRESERVED — Proposition 1 doesn't claim exhaustivity
- v18 ontological IS-NOT (L134-143) + null test (L181-187): PRESERVED
- v19 physical intuition + novelty hedge: hedge unified (Issue 5) — substance preserved, form improved
- v20 class-representative framing (L93, L113, L122): PRESERVED
- v21 μ-threshold + honest abstract: PRESERVED — abstract adds priority but preserves all disclosures
- v22 intuitive gloss (L43-44) + structural blind-spot explanation: PRESERVED
- v23 generality examples: incorporated into Proposition 1 Examples block — content preserved, formalized
- v24 §2.3 succinct opening + search pipeline + temperature: PRESERVED
- v25 tone softening + contextuality § + systematic table + discriminator: PRESERVED
- v26 POVM bridge (EXTENDED to GPT) + non-absorption proof + naturalness + stats (EXTENDED with Bayesian): all extended, none deleted

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

### Rejected changes (below threshold)
None — all 8 issues scored ≥ 4.0/5.

### Regression check
- v13 ESP boundary (L52-56): PRESERVED — "This paper does not claim..." unchanged
- v14 SME precedent (L154-166): PRESERVED — full SME paragraph + Fermi/EFT precedent untouched
- v15 VVV-QMRF removal: PRESERVED — no re-addition
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED — main text pipeline summary + FOM values untouched
- v17 constraints "not exhaustive" (L126) + β meaning (L388-395): PRESERVED
- v18 ontological IS-NOT (L132-141) + null test (L175-181): PRESERVED — IS-NOT kept in main text; contextuality detail moved to S3 (extends, does not delete)
- v19 physical intuition + novelty hedge: PRESERVED — hedge strengthened (softer language, same S1 link); physical picture moved to S3 (preserved, not deleted)
- v20 class-representative framing (L93, L111, L120): PRESERVED
- v21 μ-threshold + honest abstract + §9.2→S3: PRESERVED — abstract still discloses fair-sampling
- v22 intuitive gloss (L41-44) + structural blind-spot explanation (L258-264): PRESERVED — gloss untouched; blind-spot explanation softened (Issue 2) but content preserved
- v23 generality examples (L221-224) + loophole bridge: PRESERVED
- v24 §2.3 succinct opening (L89-96) + search pipeline (L240-243) + temperature (L301-302): PRESERVED
- v25 tone softening + contextuality § + systematic table + discriminator + abstract: contextuality § compressed (Issue 6) but content preserved in S3; all other v25 changes preserved

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
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | Dedicated "Why THIS parametrization?" subsection | 2.5/5 | **6 prior defense layers** (v14 SME, v17 constraint scope, v18 IS-NOT, v19 intuition, v20 class-representative, v24 succinct opening). New subsection would duplicate ~40 lines and risk v13 ESP boundary regression. |
| R2 | "All existing" → "Existing canonical optical EWF implementations" (full qualifier) | 3.0/5 | S1 audit comprehensively covers all known implementations including non-optical proposals. Over-qualifying weakens the claim without adding information. Abstract changed to "All published" as minimal defense. |

### Regression check
All prior-version defenses preserved (v13–v24). Full cross-version trace in v26 regression check.

---

## v24 (2026-05-25) — §2.3 succinct opening + search pipeline + temperature detail

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | **Executive summary** at top of §2.3: "Core idea" paragraph front-loading the answer to "why this class?" — parametrize via β, form follows from 3 physical constraints (rotation invariance, alignment limit, monotonicity), simplest representative, no theory predicts it, SME-analogous parametric test. | 4.2/5 | §2.3 buried the lede: meta-commentary ("Before presenting the theorem…") before substance. Reviewer asks "why this class?" and has to read 20 lines. Fix: answer in 2 sentences, then elaborate. |
| 2 | §3.3 | **Screening pipeline** in main text: "title/abstract filtering → full-text examination of 47 candidate documents → targeted follow-up on citing/cited works." Bridges gap between "~200 screened" and full S1 audit. | 4.0/5 | "~200 papers is small" — reviewer can't assess coverage without seeing methodology. Main text showed *what* was searched but not *how*. Fix: summarize pipeline stages. |
| 3 | §4.2 | **Temperature insensitivity**: "retardance temperature coefficient ~0.01 nm/°C; lab ΔT ±2°C → ~0.02 nm drift, well within ±2 nm tolerance." | 4.0/5 | Standard experimental parameter missing. Preempts reviewer question about thermal effects on retardance. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | QWP position detail | 2.5/5 | **Already specified** at L279-284 (v18): "before the PBS, after beam displacer BD2" with fast-axis orientation and retardance tolerance. Restructuring paragraph for emphasis is marginal. |
| R2 | Lab availability ("who can do this soonest?") | 2.0/5 | **External coordination**, not text edit. Paper references Bong et al. (2020) apparatus extensively — any group with that setup can implement. Naming labs could date the paper. |

### Regression check
All prior-version defenses preserved (v13–v23). Full cross-version trace in v26 regression check.

---

## v23 (2026-05-25) — Generality examples + loophole bridge sentence

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §3.2 | **Concrete examples** for universality claim: g(x) = x² → g(1/2) = 1/4 (constant, cancels in Z); g(x) = sin(πx) → g(1/2) = 1 (constant). Makes “holds for ANY g” verifiable by reader. | 4.2/5 | Proof completeness gap: universality claim without illustrative verification. Pure math, zero regression risk. |
| 2 | §7.3 | **Bridge sentence** connecting directional argument (“η < 0.91 cannot produce false positives”) to Bell-test precedent: “Analogous to first-generation Bell tests…the present proposal yields scientifically productive results under fair-sampling.” | 4.0/5 | Fragmented exposition: directional argument (v20) and Bell precedent (v15) written in separate rounds, lacked connecting sentence. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | Theoretical motivation for Eq.(2) in RQM or other interpretation (§9.2/S3) | 2.0/5 | **Quadruple regression** (v13 ESP + v17 β-meaning + v18 ontological IS-NOT + v21 S3 move). Already rejected v21-R1 at 2.0/5 with identical rationale. Existing defenses (SME precedent L150-162, null test L164-170, S3 analysis) are stronger because they don’t commit to any theoretical origin. |

### Regression check
All prior-version defenses preserved (v13–v22). Full cross-version trace in v26 regression check.

---

## v22 (2026-05-25) — Intuitive gloss + structural blind-spot explanation

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §1 | **Parenthetical gloss** of "outcome-dependent" at first structural use (L41-44): "a Superobserver's measurement statistics depend not only on the quantum state, but also on the geometric relationship between the Superobserver's measurement basis and a prior observer's recorded outcome." | 4.0/5 | Novel coinage used 7 times before §2.3 explains it. Non-specialist readers lost before technical definition. |
| 2 | §3.3 | **Structural explanation** for why community fixed θ=π/2 (L240-246): "LF inequalities optimized for maximal violation at equatorial settings. Without a θ-hypothesis, no incentive to explore polar direction." | 4.5/5 | "Why hasn't anyone thought of this?" — converts claim from insulting to sympathetic structural observation. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | Supplementals S1-S3 not in file; main text standalone | 2.0/5 | **Format issue.** S1/S2/S3 exist as separate files per PRA convention. Main text self-contained: all results (§5), novelty (§3.3), robustness (§7). L61-63 describes supplement structure. |
| R2 | β ad hoc / SME has string theory basis | 2.0/5 | Reviewer's SME claim **factually incorrect** (1997 SME had no string theory). Already corrected at L150-153 (v14/v16). 5 defense layers (v14-v18). |

### Regression check
All prior-version defenses preserved (v13–v21). Full cross-version trace in v26 regression check.

---

## v21 (2026-05-25) — μ-threshold fix + honest abstract + §9.2→S3

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | Abstract | **μ threshold 0.86→0.92(5σ)**. Detection loophole: "is discussed" → "operates under fair-sampling assumption (η ≈ 0.87); loophole closure requires SNSPD upgrade (η ≥ 0.91)". | 4.0/5 | Evasive abstract language contradicts honest §7.3 analysis. Also fixes μ threshold to match §7.1 correction. |
| 2 | §7.1 | "Threshold μ ≈ 0.86" → "Positive violation onset at μ ≈ 0.86; 5σ significance requires μ ≥ 0.92." | 4.5/5 | Internal inconsistency: text said "threshold 0.86" but table showed 0.1σ at μ=0.86. Clarify onset vs 5σ. |
| 3 | §9.2 | **MOVED** MWI + RQM paragraphs → Supplemental S3 reference. 14 lines → 5 lines. "interpretation-neutral by design." | 4.0/5 | Speculative interpretation claims create reviewer attack surface. S3 already exists. |

### Rejected changes (below threshold)
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | Eq.(2-3) justification — add theoretical origin | 2.0/5 | Would **violate** v13 ESP boundary + v17 β-meaning. 5 prior fixes (v14/v16/v18/v19/v20) already address. |
| R2 | Literature novelty hedging → "To the best of our knowledge" | 1.5/5 | Would **regress** v19 fix #4. Current "Based on systematic search…S1" is strictly better. |

### Regression check
All prior-version defenses preserved (v13–v20). Full cross-version trace in v26 regression check.

---

## v20 (2026-05-25) — f_perp class-representative framing + η-direction analysis

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | Restructured f_perp motivation: "Any smooth function…same leading-order structure; Eq.(3) is the simplest representative of this class, not its unique member" as **opening sentence**. "Absorbing c₁ into β yields" → "Adopting the simplest representative and absorbing c₁ into β". | 4.5/5 | "Three conditions don't uniquely determine f_perp" → make class-representative framing the lead, not a buried subordinate clause |
| 2 | §7.3 | NEW paragraph: "Can detector inefficiency fake a β signal?" — directional analysis showing η bias suppresses cos θ signal (toward zero) rather than enhancing it. QWP transmission >99% at 810nm → no additional loss. Conclusion: η < 0.91 cannot produce false positives for β. | 4.0/5 | "Detection loophole gap for β measurement" → explicit directional argument that η insufficiency cannot mimic positive β |

### Rejected changes (below threshold)
| # | Review Point | RCA Score | Reason |
|---|-------------|-----------|--------|
| R1 | Novelty claim — contact Bong/Cavalcanti | 2.5/5 | Text already hedged (v19). External action, not text edit. |
| R2 | Figure placeholders | 2.0/5 | Production task, not content fix. |
| R3 | Question-format title | 2.5/5 | Low risk. Backup title prepared if PRA editor objects. |

### Regression check
All prior-version defenses preserved (v14–v19). Full cross-version trace in v26 regression check.

---

## v19 (2026-05-25) — Physical intuition + §2.3 compression + novelty hedge

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §7.3 | Fair-sampling β meaning: +"β constraint applies to detected subset under fair-sampling. If future loophole-free confirms → validated. If disagrees → reinterpret as detection-efficiency-dependent effect (itself new physics)." | 3.5/5 | Clarify what fair-sampling β means AND doesn't mean |
| 2 | §2.3 | Physical intuition paragraph: measurement incompatibility between observers. Friend produces record with Bloch sphere orientation. Superobserver probes at relative angle via \|⟨b\|d⟩\|². QM factorization assumption → no dependence. Eq.(2) parametrizes residual geometric dependence. | 4.0/5 | "Outcome-dependent registration là gì về mặt vật lý?" → geometric measurement incompatibility |
| 3 | §2.3 | **Compressed** constraints (i-iii) from 3 bullet paragraphs → 4-sentence inline paragraph. Merged expansion + scope limitation. ~35 lines → ~15 lines. | 3.5/5 | "Đọc như reverse-engineering" → compact presentation, less "justify ngược" feel |
| 4 | §3.3 | Novelty hedge: "To the best of our knowledge" → "Based on the systematic search documented in Supplemental S1, we find no evidence" | 3.0/5 | Tie claim to methodology, not personal knowledge |

### Regression check
All prior-version defenses preserved (v14–v18). Full cross-version trace in v26 regression check.

---

## v18 (2026-05-25) — Ontological clarity + null test framing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | Ontological classification: Eq.(2) explicitly defined as phenomenological parametrization — NOT hidden-variable, NOT collapse modification, NOT observer interaction. Parametrizes "basis alignment dependence" that QM marginalizes over. | 4.5/5 | "Outcome-dependent registration là khái niệm mơ" → classify what it IS NOT |
| 2 | §2.3 | Null test framing: "Standard QM predicts the same LF violation regardless of θ. If θ-dependent signal detected → new physics regardless of model class. Primary result = θ-dependence, not β value." | 4.5/5 | Deflect "tại sao class này?" → experiment tests θ-dependence, class just quantifies sensitivity |
| 3 | §4.2 | "only hardware change" → "only **optical** hardware change" + SNSPD replaces existing detectors at same position. | 4.0/5 | Fix internal contradiction: SNSPD ≠ "no new components" without qualification |
| 4 | §4.1 | θ=31° trade-off explanation: θ→0° → signal max but LF violation weakens (settings collapse). θ→90° → LF max but signal vanishes. 31° = intermediate balance. Broad plateau means exact optimum not critical. | 4.0/5 | "Tại sao θ=31°?" → physical trade-off, not just numerical optimization |

### Regression check
All prior-version defenses preserved (v14–v17). Full cross-version trace in v26 regression check.

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

## Version summary

| Version | Date | Focus | Pages | Refs |
|---------|------|-------|-------|------|
| v12 | 2026-05-24 | Baseline — Eq.(12) fix | 6 | 14 |
| v13 | 2026-05-24 | Title + ESP audit | 6 | 14 |
| v14 | 2026-05-25 | SME precedent + SNSPD | 6 | 16 |
| v15 | 2026-05-25 | RCA defense (VVV-QMRF, loophole, search, §9.4) | 7 | 16 |
| v16 | 2026-05-25 | Reviewer defense 1 (S1 audit, θ-sensitivity) | 7 | 16 |
| v17 | 2026-05-25 | Reviewer defense 2 (2-obs loophole, constraint scope, β meaning) | 7 | 16 |
| v18 | 2026-05-25 | Ontological clarity + null test framing (what Eq.2 IS NOT, θ trade-off) | 7 | 16 |
| v19 | 2026-05-25 | Physical intuition + §2.3 compression + novelty hedge | 7 | 16 |
| v20 | 2026-05-25 | f_perp class-representative framing + η-direction analysis | 7 | 16 |
| v21 | 2026-05-25 | μ-threshold fix + honest abstract + §9.2→S3 | 7 | 16 |
| v22 | 2026-05-25 | Intuitive gloss + structural blind-spot explanation | 7 | 16 |
| v23 | 2026-05-25 | Generality examples + loophole bridge sentence | 7 | 16 |
| v24 | 2026-05-25 | §2.3 succinct opening + search pipeline + temperature | 7 | 16 |
| v25 | 2026-05-25 | 12-point review RCA: tone, contextuality, systematics, discriminator | 7 | 16 |
| v26 | 2026-05-25 | POVM bridge, non-absorption proof, naturalness, stats, S3 move, theorem-first | 7 | 16 |
| v27 | 2026-05-25 | GPT bridge, Proposition 1, Bayesian robustness, theorem-first positioning, novelty unification | 7 | 17 |
| v28 | 2026-05-25 | Defense compression, physical intuition, universality scoping, sensitivity qualifiers, novelty softening | 7 | 17 |
| v29 | 2026-05-25 | Reviewer tone overhaul: defensive compression, novelty softening, "new physics" removal, abstract/conclusion focus | 7 | 17 |

---

## RCA methodology

All v13→v29 changes applied via:
1. **5-step RCA** (Define → Trace → Isolate → Fix cause → Verify) per CLAUDE.md Rule Zero
2. **5-Whys** root cause drill (minimum 3 iterations per issue)
3. **Scoring ≥4/5** threshold for mandatory implementation
4. **ESP framework** (Epistemic-Structural-Presentational) for structural audit
5. Fixes scoring 3.0–3.9/5 implemented when user explicitly flagged concern AND fix cost negligible (≤3 sentences)

---

*Generated 2026-05-25. Covers v12 (baseline) through v29 (current).*
