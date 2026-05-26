Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Class C — Post-v30 Execution Plan
# K9E-PAT Resolution + K9-S12 Paper

**Version:** Post-v30 Plan v1.0 (2026-05-24)
**Status:** Plan — chưa thực hiện
**Parent project:** VVV-QMRF Class C (qualified, v30)
**RCA basis:** 3-Round RCA (aggregate 4.92/5) — IBM Quantum plan rejected (category error)
**Location:** `09_ibm_quantum/` (giữ folder structure, thay plan mới)

---

## MASTER CONTEXT BLOCK
*Paste block này vào đầu mỗi session làm việc.*

```
FRAMEWORK: VVV-QMRF K9_E — Registration-Layer Suppression
VERSION: Class C (qualified) — structurally testable, empirically UNCONFIRMED
         v30 downgrade (2026-05-24): noise sensitivity analysis FAIL
         (noise_threshold = 0.10 sigma RMS << 1.0 threshold)

K9_E POSTULATE (P9):
  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E
  β ∈ [0,1] = suppression strength (single free parameter)
  Born limit: β=0 → P(o|K) = Tr(E_o ρ) exactly

UNIVERSAL THEOREM (K9-S11c, algebraically proven):
  f_perp(+1,H) − f_perp(−1,H) = −cos(θ)
  Vanishes IFF θ = π/2 (equatorial superobserver basis)
  ALL existing EWF experiments use θ = π/2 → K9_E = QM (untestable)

K9-S12 MODIFIED BONG PROTOCOL:
  Superobserver tilt: α = 31° from z-axis (optimal)
  Hardware change: re-insert one quarter-wave plate (QWP)
  Predictions at α=31°, β=0.3:
    ⟨A₁B₂⟩_QM  = −0.857
    ⟨A₁B₂⟩_K9E = −0.893
    δ = −0.036 (20.8σ detectable)
  LF Genuine Facet 1: +0.089 (8.6σ violation simultaneously)

CURRENT STATE (v30):
  Genuine fit (Proietti raw data): beta=0.598, V=0.939, Delta_chi2=5.35 (2.31σ)
  BUT: noise sensitivity analysis FAIL — noise_threshold=0.10 sigma RMS
  A0B0 alone drives 80% of Delta_chi2 → single-setting fragility: 1.85 sigma
  → Class C downgraded genuine→qualified

K9E-PAT OPEN (HIGH priority):
  Multiplicative model (g_eff=0.146) predicts: 2BSM/1BSM ratio ≈ 2
  Proietti data shows: ratio = −0.78
  Root cause UNKNOWN — may be:
    (a) Model parameterization issue (g_eff=0.146 multiplicative)
    (b) Structural issue with K9_E functional form
    (c) Noise artifact from 4-point fit

TWO K9_E MODELS CO-EXIST:
  ADDITIVE (k9e_predictor.py):
    E_K9E = E_QM · (1 − β · n_BSM · g_ctx), g_ctx ≈ 0.039
    Calibrated from: delta_S(β=0.5) = −0.055
  MULTIPLICATIVE (proietti_raw_fit.py):
    E_K9E = E_QM · (1 − β · g_eff)^(n_BSM), g_eff = 0.146
    Calibrated from: PP-4 sanity check 4D scan
  Two models agree at first order in β·g, diverge at β > 0.3.

SCOPE BOUNDARY — IBM Quantum CANNOT test K9_E (RCA 4.92/5):
  K9_E = probability postulate (P9) operating on K-space structure (K1-K8).
  IBM Quantum = gate-model QPU executing Standard QM on physical qubits.
  Category error: IBM qubits ≠ K-space observers.
  Hardware noise ≠ K9_E signal.
  → IBM Quantum track REMOVED from this plan.
  → K9E-PAT resolved via THEORETICAL analysis (Track 1).
  → K9_E testing requires OPTICAL EWF experiment (K9-S12, future).

THIS PLAN:
  Track 1: K9E-PAT theoretical resolution (làm ngay, không cần hardware)
  Track 2: K9-S12 paper writing (medium-term, dựa trên paper plan hiện có)
  Track 3: Experimental path (future — cần optical lab access)
```

---

## PLAN ARCHITECTURE

```
┌─────────────────────────────────────────────────────────┐
│ POST-v30 EXECUTION PLAN                                 │
│                                                         │
│ Track 1: K9E-PAT RESOLUTION (PRIMARY — immediate)       │
│   ├── 1A: Compute additive model 2BSM/1BSM ratio        │
│   ├── 1B: Compare additive vs multiplicative predictions │
│   ├── 1C: RCA: structural or parameterization issue?    │
│   └── 1D: If needed: K9 sprint for functional form fix  │
│                                                         │
│ Track 2: K9-S12 PAPER (PRIMARY — medium term)           │
│   ├── 2A: Run sensitivity scans (FOM vs μ, η, Δθ)      │
│   ├── 2B: Run Monte Carlo validation                    │
│   ├── 2C: Write paper sections (theorem → predictions)  │
│   └── 2D: Full paper integration + arXiv submission     │
│                                                         │
│ Track 3: EXPERIMENTAL PATH (FUTURE)                     │
│   ├── 3A: K9-S12 optical experiment proposal            │
│   └── 3B: 3-observer experiment design                  │
└─────────────────────────────────────────────────────────┘
```

---

## TRACK 1 — K9E-PAT Theoretical Resolution
**Priority:** HIGH — làm ngay, 1-2 sessions
**Input:** Hai K9_E models (additive + multiplicative), Proietti raw data
**Output:** RCA verdict — model nào khớp empirical ratio (-0.78)? Structural implication?

### Why This Matters

K9E-PAT là open issue HIGH priority từ v29. Nếu 2BSM/1BSM ratio không khớp giữa lý thuyết và dữ liệu, có 3 khả năng:

| Khả năng | Implication | Severity |
|----------|-------------|----------|
| (a) Multiplicative model sai parameterization, additive model khớp | Vấn đề model, không phải K9_E structure. Cần recalibrate hoặc chọn model khác. | MEDIUM |
| (b) Cả hai model đều fail ratio test | K9_E functional form cần revision → mở K9 sprint mới | HIGH |
| (c) Empirical ratio -0.78 là noise artifact | P10-NOISE đã xác nhận: 4 data points underdetermine mọi analysis | MEDIUM |

### Step 1A: Compute Additive Model Ratio

```
TASK: Compute 2BSM/1BSM ratio from ADDITIVE K9_E model

CONTEXT:
  Additive model (k9e_predictor.py):
    E_K9E = E_QM · (1 − β · n_BSM · g_ctx)
    g_ctx = 0.03889
    n_BSM = number of BSM operations (0, 1, or 2)

  1-BSM scenario (Proietti 2019 geometry):
    Setting (A1, B0): Alice BSM (n=1), Bob projective (n=0) → n_BSM = 1
    Setting (A0, B1): Alice projective (n=0), Bob BSM (n=1) → n_BSM = 1
    → Average n_BSM for 1-BSM settings = 1

  2-BSM scenario:
    Setting (A1, B1): Alice BSM (n=1), Bob BSM (n=1) → n_BSM = 2

  For each setting (x, y), compute:
    delta_xy = E_K9E(x, y, β) − E_QM(x, y)  at β = best-fit value
    delta_xy = −β · n_BSM · g_ctx · E_QM(x, y)

  Ratio prediction:
    For 2BSM (n=2) vs 1BSM (n=1):
    delta_2BSM / delta_1BSM = [−β·2·g_ctx·E_2BSM] / [−β·1·g_ctx·E_1BSM]
                             = 2 · (E_2BSM / E_1BSM)

    At Proietti geometry, E values are approximately equal in magnitude
    → Ratio ≈ 2.0

  BUT: Additive model is calibrated for CHSH S-values, not individual correlators.
  The actual per-correlator ratio may differ from 2.0 due to:
    - Different E_QM values at different settings
    - Different K_ctx contribution at each setting

METHOD:
  1. Define Proietti settings:
     A0 = -π/4, A1 = π/4 (Alice)
     B0 = 0, B1 = π/2 (Bob)

  2. Compute E_QM for each CHSH setting pair:
     E_QM(x, y) = −cos(θ_Ax − θ_By) for singlet

  3. Compute E_K9E_additive(x, y, β=0.598) for each setting:
     n_BSM = x + y (0, 1, or 2)
     E_K9E = E_QM · (1 − 0.598 · n_BSM · 0.03889)

  4. Compute per-setting delta:
     delta_xy = E_K9E(x,y) − E_QM(x,y)

  5. Compute 1BSM delta: average of 2 settings with n_BSM=1
     delta_1BSM = (delta_10 + delta_01) / 2

  6. Compute 2BSM delta: setting with n_BSM=2
     delta_2BSM = delta_11

  7. Ratio_additive = delta_2BSM / delta_1BSM

EXPECTED (rough): Ratio_additive ≈ 2.0 (vì model là tuyến tính theo n_BSM)
  Nếu E_10 ≈ E_01 ≈ E_11 về magnitude:
    Ratio = 2·E_11 / ((E_10+E_01)/2) ≈ 2.0

PRODUCE:
  (A) Table: | Setting | n_BSM | E_QM | E_K9E_add | delta |
  (B) Ratio_additive value
  (C) Compare với multiplicative ratio (≈2) và empirical (−0.78)
  (D) Sanity check: additive model Born recovery (β=0 → delta=0)
```

**Save output:** `09_ibm_quantum/analysis/T1A_additive_ratio.md`

### Step 1B: Compare Models — RCA

```
TASK: RCA comparison — additive vs multiplicative vs empirical

CONTEXT:
  Multiplicative model (proietti_raw_fit.py):
    E_K9E = E_QM · (1 − β · g_eff)^(n_BSM), g_eff = 0.146
    This model was used for the genuine fit (beta=0.598, 2.31σ)
    Predicts: 2BSM/1BSM ratio ≈ 2.0
    Empirical: ratio = −0.78

  Additive model (k9e_predictor.py):
    E_K9E = E_QM · (1 − β · n_BSM · g_ctx), g_ctx ≈ 0.039
    Ratio from Step 1A: [computed value]

  Key question: Is the ratio discrepancy a MODEL issue or a STRUCTURAL issue?

5-WHY ANALYSIS:
  W1: Why is empirical ratio (−0.78) different from predictions (~2)?
    → Either the model is wrong OR the data is noise-dominated.

  W2: Why would the model be wrong?
    → Multiplicative model assumes K_ctx effect compounds multiplicatively
      with n_BSM. If actual K_ctx effect is ADDITIVE (or different form),
      the 2BSM/1BSM prediction changes.

  W3: Why does the additive model predict ratio ≈ 2?
    → Because it's linear in n_BSM: delta ∝ n_BSM.
      Ratio = delta(2BSM)/delta(1BSM) = 2 automatically (if E values equal).

  W4: What ratio would match empirical −0.78?
    → A negative ratio means delta_2BSM and delta_1BSM have OPPOSITE SIGNS.
      Neither additive nor multiplicative model predicts sign flip.
      → If empirical ratio is truly negative, both models are WRONG.

  W5: Root cause — is empirical ratio reliable?
    → P10-NOISE: noise_threshold = 0.10 sigma RMS.
      With 4 data points, random noise produces Delta_chi2 ≥ 5.35 in ~50%
      of runs.
      → Empirical ratio −0.78 may be ENTIRELY noise-driven.
      → This is the most parsimonious explanation.

PRODUCE:
  (A) Comparison table:
      | Model | 2BSM delta | 1BSM delta | Ratio | Match empirical? |
      |-------|-----------|-----------|-------|------------------|
      | Multiplicative (g=0.146, β=0.598) | [val] | [val] | ~2.0 | NO |
      | Additive (g=0.039, β=0.598) | [val] | [val] | [val] | [YES/NO] |
      | Empirical (Proietti raw) | [val] | [val] | −0.78 | — |

  (B) RCA verdict — one of:
      VERDICT A: "Additive model ratio matches empirical → multiplicative
                  parameterization was wrong. Recalibrate with additive model."
      VERDICT B: "Both models fail ratio test → K9_E functional form needs
                  revision. Open K9-S13 sprint for new functional form."
      VERDICT C: "Empirical ratio is noise artifact (P10-NOISE confirms).
                  Neither model can be validated or rejected with 4 data points.
                  K9E-PAT is UNRESOLVABLE without new experimental data."

  (C) Recommendation for next step
```

**Save output:** `09_ibm_quantum/analysis/T1B_model_comparison_RCA.md`

### Step 1C: K9E-PAT Resolution Decision

Based on Steps 1A-1B, produce final decision record.

```
DECISION OPTIONS:

  IF VERDICT A (additive model works):
    → Action: Recalibrate genuine fit using additive model (not multiplicative)
    → Update: proietti_raw_fit.py to support additive model option
    → K9E-PAT status: RESOLVED — ratio ~2 confirmed with correct model

  IF VERDICT B (both models fail):
    → Action: Open K9-S13 sprint for K9_E functional form revision
    → Scope: Explore non-multiplicative, non-additive f_perp forms
    → Constraint: Must still satisfy Born recovery (β=0 → QM exact)
    → K9E-PAT status: OPEN — structural revision needed

  IF VERDICT C (noise artifact):
    → Action: Close K9E-PAT as UNRESOLVABLE with current data
    → Document: P10-NOISE boundary applies to K9E-PAT as well
    → Next: Only new experiment (K9-S12 optical) can resolve
    → K9E-PAT status: DEFERRED — requires experimental data

PRODUCE:
  → 09_ibm_quantum/analysis/T1C_k9e_pat_resolution.md
  → Update index.md K9E-PAT row
  → Update Top 10 hallucinations record if needed
```

**Save output:** `09_ibm_quantum/analysis/T1C_k9e_pat_resolution.md`

### Track 1 Decision Gate

```
GATE T1: After Steps 1A-1C complete
  → K9E-PAT resolved → proceed to Track 2
  → K9E-PAT requires functional form revision → open K9-S13, defer Track 2
  → K9E-PAT unresolvable → document, proceed to Track 2 with caveat
```

---

## TRACK 2 — K9-S12 Paper Writing
**Priority:** HIGH — bắt đầu sau Track 1, 3-5 sessions
**Input:** Paper plan tại `03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md`
**Output:** arXiv-ready preprint

### Context

K9-S12 paper plan đã tồn tại đầy đủ (2026-05-23) với:
- 10 sections + supplemental
- 5 figures (schematic + data plots)
- 8 references minimum
- LLM session plan (K9-S13-A đến K9-S13-K)

Track 2 thực thi paper plan đó. Mỗi step dưới đây map vào session plan.

### Step 2A: Numerical Computation Sessions

```
SESSION K9-S13-A: Sensitivity scan FOM(μ, η, Δθ)
  → Output: Numerical tables for §7 (Robustness)
  → Script: 07_fits/K9S12_sensitivity_scan.py

SESSION K9-S13-B: Monte Carlo validation (10,000 runs)
  → Output: Histogram data for §6 (Statistical Analysis)
  → Script: 07_fits/K9S12_monte_carlo.py

SESSION K9-S13-C: Full correlator table at modified angles
  → Output: Table for §5 (Predictions)
  → Script: 07_fits/K9S12_correlator_table.py

SESSION K9-S13-D: Detection loophole η_crit computation
  → Output: Number for §8 (Loophole Analysis)
  → Script: 07_fits/K9S12_eta_critical.py

PRODUCE:
  (A) 4 Python scripts in 07_fits/
  (B) Numerical results packaged as CSV/JSON
  (C) Pre-formatted tables for paper insertion
```

**Save scripts:** `07_fits/K9S12_*.py`
**Save results:** `07_fits/outputs/K9S12_*.csv`

### Step 2B: Paper Section Writing

Viết theo thứ tự recommended từ paper plan:

```
ORDER (từ paper plan §7):

  SESSION K9-S13-E: Write §3 (Theorem + Proof)
    → Core of paper — Universal Equatorial Cancellation Theorem
    → Input: K9-S11c algebraic proof
    → Output: ~500-700 word draft

  SESSION K9-S13-F: Write §4 (Experimental Protocol)
    → Hardware description — one QWP, α=31°
    → Input: Bong 2020 supplemental, K9-S12 proposal
    → Output: ~500-700 word draft

  SESSION K9-S13-G: Write §5 (Predictions)
    → Numerical predictions from Step 2A
    → Output: ~600-800 word draft + 2 tables

  SESSION K9-S13-H: Write §6 + §7 (Statistics + Robustness)
    → Monte Carlo results + sensitivity scans
    → Output: ~1100-1400 word draft + 2 figures

  SESSION K9-S13-I: Write §8 + §9 (Loopholes + Discussion)
    → Output: ~800-1200 word draft

  SESSION K9-S13-J: Write §1 + §2 + §10 + Abstract
    → Introduction + Background + Conclusion + Abstract
    → Output: ~1500 word draft

  SESSION K9-S13-K: Full paper integration
    → Consistency check, reference formatting, figure placement
    → Output: Final draft ready for arXiv

PRODUCE:
  → 09_ibm_quantum/paper/draft_v1.md (full paper)
  → 09_ibm_quantum/paper/figures/ (generated figures)
  → 09_ibm_quantum/paper/supplemental/ (supplemental material)
```

**Save drafts:** `09_ibm_quantum/paper/`
**Save figures:** `09_ibm_quantum/paper/figures/`
**Save supplemental:** `09_ibm_quantum/paper/supplemental/`

### Step 2C: Pre-Submission Quality Check

Checklist từ paper plan §9:

```
QUALITY GATES (all must PASS before arXiv submission):
  ☐ Every symbol defined at first use
  ☐ Every number has associated uncertainty
  ☐ Every figure has self-contained caption
  ☐ All 5 loopholes addressed in §8
  ☐ Decision criteria in §5.3 cover all 4 outcome combinations
  ☐ Supplemental S3 (code) runnable by third party
  ☐ Abstract contains no undefined acronyms
  ☐ Reference list complete and formatted consistently
  ☐ FOM values in §7 match §5 and §6 (no internal inconsistency)
  ☐ Robustness table §7.5 populated with actual computed values
  ☐ K9E-PAT status reflected accurately (from Track 1)

PRODUCE:
  → 09_ibm_quantum/paper/QC_checklist.md (all items checked)
```

### Track 2 Decision Gate

```
GATE T2: After Step 2C QC PASS
  → Paper ready for arXiv → submit
  → Paper has unresolved issues → fix before submit
```

---

## TRACK 3 — Experimental Path (FUTURE)
**Priority:** MEDIUM — không cần làm ngay
**Dependency:** Optical lab access (không có sẵn)

### Step 3A: K9-S12 Experiment Proposal

```
TASK: Formalize experimental proposal for optical EWF lab

CONTEXT:
  K9-S12 paper describes the protocol. But paper ≠ proposal.
  A formal proposal needs:
    - Equipment list with specifications
    - Alignment procedure (step-by-step)
    - Expected timeline
    - Budget estimate
    - Risk assessment

  This is FUTURE WORK — không block Track 1 hoặc Track 2.

PRODUCE (future):
  → 09_ibm_quantum/proposal/K9S12_experiment_proposal.md
```

### Step 3B: 3-Observer Experiment Design

```
CONTEXT:
  delta_M3 = −0.223 at β=0.3 (11x amplification over 2-observer)
  Prediction ready (Phase 11), experimental design deferred.

  Requires T4-H Steps 2-4 (colimit completion) for full derivation.
  Currently: T4-H Step 1 proven, Steps 2-4 deferred.

PRODUCE (future):
  → 09_ibm_quantum/proposal/3observer_experiment_design.md
```

---

## FILE STRUCTURE

```
09_ibm_quantum/                          ← existing folder, plan mới thay thế
├── README.md                            Purpose, links to Track 1/2/3
├── VVV_QMRF_Post_v30_Execution_Plan.md  ← THIS FILE
├── VVV_QMRF_IBM_Quantum_Execution_Plan.md  ← SUPERSEDED (RCA rejected)
│
├── analysis/                            Track 1 outputs
│   ├── T1A_additive_ratio.md            Additive model 2BSM/1BSM ratio
│   ├── T1B_model_comparison_RCA.md      RCA: additive vs multiplicative
│   └── T1C_k9e_pat_resolution.md        Final K9E-PAT verdict
│
├── paper/                               Track 2 outputs
│   ├── draft_v1.md                      Full paper draft
│   ├── QC_checklist.md                  Pre-submission quality check
│   ├── figures/                         Generated figures (PNG/PDF)
│   │   ├── fig1_ewf_schematic.png
│   │   ├── fig2_modified_optical_path.png
│   │   ├── fig3_monte_carlo_histogram.png
│   │   ├── fig4_fom_vs_mu.png
│   │   └── fig5_2d_heatmap.png
│   └── supplemental/                    Supplemental material
│       ├── S1_full_proof.md
│       ├── S2_correlator_table.md
│       └── S3_monte_carlo_code.py
│
├── proposal/                            Track 3 outputs (future)
│   ├── K9S12_experiment_proposal.md
│   └── 3observer_experiment_design.md
│
└── governance/                           Decision records
    ├── RCA_IBM_plan_rejection.md         3-Round RCA (4.92/5) — why IBM Quantum was rejected
    ├── DECISION_K9EPAT_resolution.md     K9E-PAT decision record
    └── CHANGELOG.md                      Version history
```

---

## DEPENDENCY MAP

```
Track 1 (K9E-PAT)
  ├── Input: k9e_predictor.py (additive model)
  ├── Input: proietti_raw_fit.py (multiplicative model)
  ├── Input: P10-NOISE RCA (noise boundary)
  └── Output → Track 2 (informs paper accuracy)

Track 2 (K9-S12 Paper)
  ├── Input: paper_plan_single_waveplate_EWF.md
  ├── Input: K9-S11c (universal theorem proof)
  ├── Input: K9-S12 (modified Bong proposal)
  ├── Input: Track 1 K9E-PAT verdict
  └── Output → arXiv preprint

Track 3 (Experiment)
  ├── Input: Track 2 paper
  ├── Input: Optical lab access (external)
  └── Output → Experimental proposal
```

---

## ESTIMATED EFFORT

| Track | Sessions | Active time | Difficulty |
|-------|----------|-------------|------------|
| Track 1 (K9E-PAT theory) | 1-2 | 2-4 hours | MEDIUM — computational + RCA |
| Track 2 (Paper writing) | 3-5 | 6-10 hours | HIGH — writing + computation |
| Track 3 (Experiment) | FUTURE | TBD | HIGH — requires lab access |

---

## DECISION GATES

```
GATE 0: START
  → Track 1 begins immediately (no prerequisites beyond existing code)

GATE T1: After Track 1 Steps 1A-1C
  Verdict A (model issue)     → recalibrate, proceed to Track 2
  Verdict B (structural issue) → open K9-S13, DEFER Track 2
  Verdict C (noise artifact)  → document, proceed to Track 2 with caveat

GATE T2: After Track 2 Step 2C
  QC PASS → submit to arXiv
  QC FAIL → fix issues, re-check

GATE T3: After arXiv submission
  → Begin Track 3 experimental proposal (if lab access available)
  → OR: pivot to 3-observer experiment design
```

---

## NOTES

**LLM model recommendation:**
- Track 1 (RCA + theory): Claude Opus — cần reasoning sâu
- Track 2 (paper writing): Claude Opus cho core sections (§3, §5, §9); Sonnet cho boilerplate (§1, §4, §8)
- Step 2A (numerical): Bất kỳ model nào — đây là code execution

**EX compass role:**
- EX_NODE_K5_CTX (KE-SC 4.0): Theo dõi K5 firing trong K9-S12 protocol
- EX_NODE_K9_BETA (KE-SC 3.7): Beta sensitivity ảnh hưởng đến cả hai model
- Không import EX structure — compass only (per CLAUDE.md)

**Anti-Hallucination Pipeline:**
- Mỗi claim trong paper phải audit được qua AHP
- Top 10 hallucinations record cập nhật sau mỗi track completion
- K9E-PAT resolution có thể thay đổi AHP scoring

---

*Post-v30 Execution Plan v1.0 — 2026-05-24. Replaces IBM Quantum plan (RCA rejected, category error 4.92/5). Two primary tracks: K9E-PAT theory + K9-S12 paper. Three decision gates.*
