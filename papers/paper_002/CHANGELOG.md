# CHANGELOG — "Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?"

**Paper ID:** paper_002 | **Target:** arXiv quant-ph → Phys. Rev. A
**Author:** VietVunVut (Viet — Nguyen Xuan)

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (§1) | ✅ Preserved — untouched |
| v27 Proposition 1 math | ✅ Preserved — Definition + Proposition intact |
| v25 novelty hedge "Within the surveyed literature (S1)" | ✅ Preserved — kept in §3.6 |
| v17 §8.2 interpretation-neutrality | ✅ Preserved — "interpretation-neutral by design" in merged §8.2 |
| v26 §6 Bayesian robustness | ✅ Preserved — untouched |
| v27 GPT bridge [17] | ✅ Preserved — untouched |
| v28 physical intuition | ✅ Compressed but content preserved — geometric symmetry + measurement disturbance + directional probe + mathematical observation all intact |
| v28 theorem preview (§1) | ✅ Preserved — untouched |
| v29 abstract 3-beat | ✅ Preserved — untouched |
| v30 "benchmark parametrization" | ✅ Preserved |
| v30 "overlap-dependent deformation" | ✅ Preserved |
| v12 exact numerical values | ✅ Preserved — untouched |
| v32 §2.3 Core idea ↔ constraints | ✅ Preserved — untouched |
| v32 theory-space constraint framing | ✅ Preserved — untouched |
| v32 practical sensitivity range | ✅ Preserved — untouched in §5.3 |
| v34 S1-tied novelty softening (§9) | ✅ Preserved — untouched |

### Rejected changes (below 4.5/5 threshold)
| # | Issue | RCA Score | Reason |
|---|-------|-----------|--------|
| R1 | Novelty overclaim — further soften "every published EWF" | 3.8/5 | Already heavily hedged (v25 "Within surveyed literature", v31 consistent "to our knowledge", v34 S1-tied §9). Remaining absolute statements are backed by S1 audit methodology. |
| R2 | Model β ad-hoc — add more theoretical motivation | 3.5/5 | User acknowledges "paper đã làm rồi." GPT bridge (v27), benchmark terminology (v30), measurement disturbance (v32), structural observation (v33) — 4 layers of motivation already present. |
| R3 | Physical motivation not "inevitable" | 4.2/5 | SME "search before theory" framing already in §2.3 (v14, v33 "phenomenological parameter searches"). The paper's framing is already correct: it's a symmetry-class search, not a theory prediction. |
| R4 | β~0.04 optimistic — add more caveats | 4.0/5 | Practical range β∼0.05–0.10 already quoted (v32), Bayesian analysis in §6 (v26), "order-of-magnitude" qualifier (v28). Three layers of caveats already present. |

### Net line count
| Metric | Before (v34) | After (v35) | Delta |
|--------|-------------|-------------|-------|
| §3.4 | 18 lines | 8 lines | −10 |
| §3.6 search | 22 lines | 13 lines | −9 |
| §8.2 + §8.3 | 15 lines | 5 lines | −10 |
| §5.3 Scale context | 5 lines | 3 lines | −2 |
| §3.5 | 23 lines | 19 lines | −4 |
| Other (line reflow) | — | — | +8 |
| **Net** | **~627 lines** | **~600 lines** | **−27 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (§1 L58-61) | ✅ Preserved — untouched |
| v27 Proposition 1 math | ✅ Preserved — same content, reformatted with Definition |
| v25 novelty hedge "Within the surveyed literature (S1)" | ✅ Preserved — in §3.6; now ALSO in §9 (consistent S1-tying) |
| v17 §8.2 interpretation-neutrality | ✅ Preserved — untouched |
| v26 §6 Bayesian robustness | ✅ Preserved — untouched |
| v27 GPT bridge [17] | ✅ Preserved — reference intact at §2.3 L97 |
| v28 physical intuition | ✅ Preserved — §3.5 intact |
| v28 theorem preview (§1 L53-56) | ✅ Preserved — untouched |
| v29 abstract 3-beat structure | ✅ Preserved — observation → theorem → consequence → experiment → scope |
| v30 "benchmark parametrization" | ✅ Preserved |
| v30 "overlap-dependent deformation" | ✅ Preserved |
| v12 exact numerical values | ✅ Preserved — untouched |
| v32 §2.3 Core idea ↔ L129 consistency | ✅ Preserved — "simplest leading-order form" + "three constraints force the leading-order Taylor expansion" harmonized |
| v32 theory-space constraint across Abstract/§3.6/§9 | ✅ Preserved — Abstract compact canonical, §3.6 varied, §9 S1-tied |
| v32 practical sensitivity range | ✅ Preserved — untouched in §5.3 |

### Net line count
| Metric | Before (v33) | After (v34) | Delta |
|--------|-------------|-------------|-------|
| Abstract | 14 lines | 11 lines | −3 |
| §2.3 (entire) | ~60 lines | ~48 lines | −12 |
| §3.2 | 8 lines | 12 lines | +4 (Definition added) |
| §9 | 13 lines | 13 lines | 0 (wording only) |
| **Net** | **~638 lines** | **~627 lines** | **−11 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (§1 L60-64) | ✅ Preserved — untouched |
| v27 Proposition 1 math | ✅ Preserved — untouched |
| v25 novelty hedge "Within the surveyed literature (S1)" | ✅ Preserved — untouched |
| v17 §8.2 interpretation-neutrality | ✅ Preserved — untouched |
| v26 §6 Bayesian robustness | ✅ Preserved — untouched |
| v27 GPT bridge [17] | ✅ Preserved — reference and GPT framing intact |
| v28 physical intuition | ✅ Extended — geometric content preserved, structural observation added |
| v28 theorem preview (§1) | ✅ Preserved — untouched |
| v29 abstract 3-beat structure | ✅ Preserved — abstract unchanged |
| v30 "benchmark parametrization" | ✅ Preserved |
| v30 "overlap-dependent deformation" | ✅ Preserved |
| v12 exact numerical values | ✅ Preserved — untouched |
| v32 §2.3 Core idea ↔ L129 consistency | ✅ Preserved — "simplest leading-order form" + "shares the same first-order structure" harmonized |
| v32 theory-space constraint across Abstract/§3.6/§9 | ✅ Preserved — Abstract keeps canonical, §3.6/§9 intentionally varied |
| v32 practical sensitivity range | ✅ Preserved — untouched |

### Net line count
| Metric | Before (v32) | After (v33) | Delta |
|--------|-------------|-------------|-------|
| §2.3 Core idea | 16 lines | 17 lines | +1 |
| §3.4 | 17 lines | 17 lines | 0 (wording only) |
| §3.5 | 15 lines | 20 lines | +5 (structural observation) |
| §3.6 closing | 8 lines | 6 lines | −2 (de-echo) |
| §9 Conclusion | 13 lines | 13 lines | 0 (wording only) |
| **Net** | **634 lines** | **638 lines** | **+4 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (§1 L60-64) | ✅ Preserved — "This paper does not claim..." unchanged as sole canonical disclaimer |
| v27 Proposition 1 math | ✅ Preserved — mathematical content identical |
| v25 novelty hedge "Within the surveyed literature (S1)" | ✅ Preserved — unchanged (§3.6 L284) |
| v17 §8.2 interpretation-neutrality | ✅ Preserved — "interpretation-neutral by design" unchanged |
| v26 §6 Bayesian robustness | ✅ Preserved — no changes to §6 content |
| v27 GPT bridge [17] | ✅ Preserved — substance intact, extended with uniqueness + measurement disturbance |
| v28 physical intuition | ✅ Extended — original geometric content preserved, measurement-disturbance narrative added |
| v28 theorem preview (§1 L55-58) | ✅ Preserved — preview paragraph unchanged |
| v29 abstract 3-beat structure | ✅ Preserved — extended to 4-beat (observation → theorem → theory-space → experiment → scope) |
| v30 "benchmark parametrization" terminology | ✅ Preserved — running term unchanged |
| v30 "overlap-dependent deformation" terminology | ✅ Preserved — running term unchanged |
| v12 exact numerical values | ✅ Preserved — no analytical approximations introduced |

### v32-specific constraints (new)
| Constraint | Status |
|------------|--------|
| §2.3 Core idea "unique to leading order" consistent with L129 "same leading-order structure" | ✅ Harmonized — both now say leading-order is shared/unique, full function has multiple representatives |
| §3.4 explicit calculation references Friend outcome d as external to Superobserver basis | ✅ Consistent with §2.3 Eq.(2) definition and §3.1 model-independence |
| Theory-space constraint framing consistent across Abstract/§3.6/§9 | ✅ Verbatim-aligned: all three locations use "constrain a smaller theory space than previously assumed" |
| Practical sensitivity range consistent with §6 Bayesian β_min ≈ 0.046 | ✅ β ∼ 0.04–0.06 (combined) brackets the Bayesian estimate; β ∼ 0.05–0.10 (single) brackets the idealized 0.075 |

### Net line count
| Metric | Before (v31) | After (v32) | Delta |
|--------|-------------|-------------|-------|
| Abstract | 11 lines | 14 lines | +3 (theory-space sentence + tightening) |
| §2.3 Core idea | 13 lines | 16 lines | +3 (uniqueness + measurement disturbance) |
| §2.3 IS-NOT | 3 lines | 2 lines | −1 |
| §3.4 | 12 lines | 17 lines | +5 (explicit no-go calculation) |
| §3.5 | 9 lines | 15 lines | +6 (observer-record alignment narrative) |
| §3.6 closing | 4 lines | 8 lines | +4 (theory-space constraint reframing) |
| §5.3 sensitivity | 7 lines | 10 lines | +3 (practical range) |
| §9 Conclusion | 9 lines | 13 lines | +4 (theory-space + closing sentence) |
| **Net** | **607 lines** | **634 lines** | **+27 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (§1 L57-61) | ✅ Preserved — "This paper does not claim..." unchanged as sole canonical disclaimer |
| v27 Proposition 1 math | ✅ Preserved — mathematical content identical; only position moved (§3.2) |
| v25 novelty hedge "Within the surveyed literature (S1)" | ✅ Preserved — unchanged (§3.6 L264) |
| v17 §8.2 interpretation-neutrality | ✅ Preserved — "interpretation-neutral by design" unchanged |
| v26 §6 Bayesian robustness | ✅ Preserved — no changes to §6 content |
| v27 GPT bridge [17] | ✅ Preserved — substance intact, repositioned earlier in §2.3 |
| v28 physical intuition | ✅ Preserved — 8-line paragraph moved to §3.5 (after proof) |
| v28 theorem preview (§1 L52-55) | ✅ Preserved — preview paragraph unchanged |
| v29 abstract 3-beat structure | ✅ Preserved — observation → experiment → scope maintained |
| v30 "benchmark parametrization" terminology | ✅ Preserved — running term unchanged |
| v30 "overlap-dependent deformation" terminology | ✅ Preserved — running term unchanged |
| v12 exact numerical values | ✅ Preserved — no analytical approximations introduced |

### Net line count
| Metric | Before (v30) | After (v31) | Delta |
|--------|-------------|-------------|-------|
| Abstract | 11 lines | 11 lines | 0 (wording only) |
| §1 | ~20 lines | ~18 lines | −2 (headline consolidation, disclaimer cut) |
| §2.3 | ~55 lines | ~50 lines | −5 (GPT moved up, defensive text compressed) |
| §3 (entire) | ~80 lines | ~95 lines | +15 (theorem-box restructure + §5.4→§3.4) |
| §4 | ~55 lines | ~63 lines | +8 (§4.5 feasibility added) |
| §5 (was §5.1-5.4) | ~75 lines | ~65 lines | −10 (§5.4 removed, §5.3 compressed) |
| §8.4 Multi-observer | 5 lines | 2 lines | −3 |
| §9 Conclusion | 12 lines | 8 lines | −4 (focused on theorem, tone reduction) |
| Defensive text (scattered) | ~30 lines | ~5 lines | −25 (global dedup) |
| **Net** | **626 lines** | **607 lines** | **−19 lines** |

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

### Regression watchlist
| Constraint | Status |
|------------|--------|
| v13 ESP boundary (L57-60) | ✅ Preserved — "This paper does not claim..." unchanged (wording updated: "coupling" → "deformation") |
| v27 Proposition 1 math (L206-212) | ✅ Preserved — mathematical content identical; added Scope limitation AFTER Corollary |
| v25 novelty hedge (§3.3) | ✅ Preserved — "Within the surveyed literature (S1)" unchanged |
| v17 §9.2 interpretation-neutrality | ✅ Preserved — "interpretation-neutral by design" unchanged (now §8.2) |
| v26 §6 Bayesian robustness | ✅ Extended — added specific mechanism names, substance preserved |
| v27 GPT bridge [17] | ✅ Preserved — compressed but substance and reference intact |
| v28 physical intuition (§3) | ✅ Preserved — 8-line paragraph unchanged |
| v28 theorem preview (§1 L52-55) | ✅ Preserved — preview paragraph unchanged |
| v29 abstract 3-beat structure | ✅ Preserved — observation → experiment → scope maintained |
| v29 §10 conclusion focus | ✅ Extended — added "obvious in hindsight" coda |

### Net line count
| Metric | Before (v29) | After (v30) | Delta |
|--------|-------------|-------------|-------|
| Abstract | 10 lines | 11 lines | +1 |
| §1 Claim A | 8 lines | 8 lines | 0 (wording only) |
| §2.3 | ~60 lines | ~55 lines | −5 |
| §3.1 | 6 lines | 10 lines | +4 |
| §3.2 (Scope limitation) | 0 lines | 7 lines | +7 |
| §3.3 operational significance | 4 lines | 6 lines | +2 |
| §6 Bayesian | 6 lines | 7 lines | +1 |
| §7 (was §7.1-7.4+§8) | ~95 lines | ~45 lines | −50 |
| §8 (old §8 loophole table) | 11 lines | 0 lines (merged) | −11 |
| Section renumbering | §9→§8, §10→§9 | — | 0 |
| §9 Conclusion | 11 lines | 12 lines | +1 |
| **Net** | **652 lines** | **626 lines** | **−26 lines** |

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
| v30 | 2026-05-25 | Structural blind spot framing, Eq.(2) benchmark subordination, trivial-algebra defense, uniqueness scope, statistical conservatism, paper compression, terminology shift | ~5 | 17 |
| v31 | 2026-05-25 | Novelty softening, Eq.(2) motivation repositioned, thesis repetition cuts, theorem-box restructure, experimental feasibility, reparameterization defense, multi-observer → S3, defensive tone reduction, headline consolidation | ~5 | 17 |
| v32 | 2026-05-25 | Eq.(2) uniqueness+measurement disturbance, universality sharpening, explicit δ⟨AB⟩=0 no-go, practical sensitivity range, defensive tone trim, observer-record alignment narrative, theory-space constraint reframing | ~5 | 17 |
| v33 | 2026-05-25 | uniqueness→simplest hedge, §3.4 passive-relabeling soften, scope qualifier, SME→phenomenological, repetition de-echo, registration-fidelity structural observation | ~5 | 17 |
| v34 | 2026-05-25 | Abstract compression, §2.3 de-lawyer, novelty S1-tied softening, Proposition 1 Definition+compact formalization | ~5 | 17 |
| v35 | 2026-05-25 | §3.4 compress, paper de-overpack (interpretation→S3, search compress, trim verbose sections) | ~5 | 17 |

---

## RCA methodology

All v13→v35 changes applied via:
1. **5-step RCA** (Define → Trace → Isolate → Fix cause → Verify) per CLAUDE.md Rule Zero
2. **5-Whys** root cause drill (minimum 3 iterations per issue)
3. **Scoring ≥4/5** threshold for mandatory implementation
4. **ESP framework** (Epistemic-Structural-Presentational) for structural audit
5. Fixes scoring 3.0–3.9/5 implemented when user explicitly flagged concern AND fix cost negligible (≤3 sentences)

---

*Generated 2026-05-25. Covers v12 (baseline) through v35 (current).*
