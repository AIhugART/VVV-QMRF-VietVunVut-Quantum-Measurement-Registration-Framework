# CHANGELOG — "Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?"

**Paper ID:** paper_002 | **Target:** arXiv quant-ph → Phys. Rev. A
**Author:** VietVunVut (Viet — Nguyen Xuan)

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
- v13 ESP boundary: PRESERVED (L55-59)
- v14 SME precedent: PRESERVED (L150-162)
- v15 VVV-QMRF removal: PRESERVED
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED
- v17 constraints “not exhaustive” + β meaning: PRESERVED
- v18 ontological IS-NOT + null test: PRESERVED
- v19 physical intuition + novelty hedge: PRESERVED (L233-234)
- v20 class-representative framing + η-direction analysis: PRESERVED
- v21 μ-threshold + honest abstract + §9.2→S3: PRESERVED
- v22 intuitive gloss + structural blind-spot: PRESERVED (L240-246)

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
- v13 ESP boundary: PRESERVED (L55-59)
- v14 SME precedent: PRESERVED (L150-162)
- v15 VVV-QMRF removal: PRESERVED
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED
- v17 constraints "not exhaustive" + β meaning: PRESERVED
- v18 ontological IS-NOT + null test: PRESERVED
- v19 physical intuition + novelty hedge: PRESERVED (L233-234)
- v20 class-representative framing + η-direction analysis: PRESERVED
- v21 μ-threshold + honest abstract + §9.2→S3: PRESERVED

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
- v13 ESP boundary: PRESERVED (L52-56)
- v14 SME precedent: PRESERVED (L147-158)
- v15 VVV-QMRF removal: PRESERVED
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED
- v17 constraints "not exhaustive" + β meaning: PRESERVED
- v18 ontological IS-NOT + null test: PRESERVED
- v19 physical intuition + novelty hedge: PRESERVED (L230-231)
- v20 class-representative framing + η-direction analysis: PRESERVED

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
- v14 SME precedent: PRESERVED
- v15 VVV-QMRF removal: PRESERVED (no re-addition)
- v16 S1 search audit + θ-sensitivity FOM: PRESERVED
- v17 constraint scope ("not exhaustive") + 2-observation loophole + β meaning: PRESERVED
- v18 ontological classification + null test framing + θ trade-off: PRESERVED
- v19 physical intuition paragraph + compressed (i-iii) + novelty hedge: PRESERVED

---

## v19 (2026-05-25) — Physical intuition + §2.3 compression + novelty hedge

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §7.3 | Fair-sampling β meaning: +"β constraint applies to detected subset under fair-sampling. If future loophole-free confirms → validated. If disagrees → reinterpret as detection-efficiency-dependent effect (itself new physics)." | 3.5/5 | Clarify what fair-sampling β means AND doesn't mean |
| 2 | §2.3 | Physical intuition paragraph: measurement incompatibility between observers. Friend produces record with Bloch sphere orientation. Superobserver probes at relative angle via \|⟨b\|d⟩\|². QM factorization assumption → no dependence. Eq.(2) parametrizes residual geometric dependence. | 4.0/5 | "Outcome-dependent registration là gì về mặt vật lý?" → geometric measurement incompatibility |
| 3 | §2.3 | **Compressed** constraints (i-iii) from 3 bullet paragraphs → 4-sentence inline paragraph. Merged expansion + scope limitation. ~35 lines → ~15 lines. | 3.5/5 | "Đọc như reverse-engineering" → compact presentation, less "justify ngược" feel |
| 4 | §3.3 | Novelty hedge: "To the best of our knowledge" → "Based on the systematic search documented in Supplemental S1, we find no evidence" | 3.0/5 | Tie claim to methodology, not personal knowledge |

### Regression check
- v14 SME precedent: PRESERVED
- v15 VVV-QMRF removal: PRESERVED
- v16 θ-sensitivity + proposal framing: PRESERVED
- v17 constraint scope + 2-observation loophole + β meaning: PRESERVED
- v18 ontological classification + null test + optical hardware + θ trade-off: PRESERVED

---

## v18 (2026-05-25) — Ontological clarity + null test framing

| # | Section | Change | RCA Score | Rationale |
|---|---------|--------|-----------|-----------|
| 1 | §2.3 | Ontological classification: Eq.(2) explicitly defined as phenomenological parametrization — NOT hidden-variable, NOT collapse modification, NOT observer interaction. Parametrizes "basis alignment dependence" that QM marginalizes over. | 4.5/5 | "Outcome-dependent registration là khái niệm mơ" → classify what it IS NOT |
| 2 | §2.3 | Null test framing: "Standard QM predicts the same LF violation regardless of θ. If θ-dependent signal detected → new physics regardless of model class. Primary result = θ-dependence, not β value." | 4.5/5 | Deflect "tại sao class này?" → experiment tests θ-dependence, class just quantifies sensitivity |
| 3 | §4.2 | "only hardware change" → "only **optical** hardware change" + SNSPD replaces existing detectors at same position. | 4.0/5 | Fix internal contradiction: SNSPD ≠ "no new components" without qualification |
| 4 | §4.1 | θ=31° trade-off explanation: θ→0° → signal max but LF violation weakens (settings collapse). θ→90° → LF max but signal vanishes. 31° = intermediate balance. Broad plateau means exact optimum not critical. | 4.0/5 | "Tại sao θ=31°?" → physical trade-off, not just numerical optimization |

### Regression check
- v14 SME precedent: PRESERVED
- v15 VVV-QMRF removal: PRESERVED (no re-addition)
- v16 θ-sensitivity data: PRESERVED
- v17 constraint scope limitation: PRESERVED
- v17 2-observation loophole defense: PRESERVED
- v17 β physical meaning: PRESERVED

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

---

## RCA methodology

All v13→v23 changes applied via:
1. **5-step RCA** (Define → Trace → Isolate → Fix cause → Verify) per CLAUDE.md Rule Zero
2. **5-Whys** root cause drill (minimum 3 iterations per issue)
3. **Scoring ≥4/5** threshold for mandatory implementation
4. **ESP framework** (Epistemic-Structural-Presentational) for structural audit
5. Fixes scoring 3.0–3.9/5 implemented when user explicitly flagged concern AND fix cost negligible (≤3 sentences)

---

*Generated 2026-05-25. Covers v12 (baseline) through v23 (current).*
