Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Project VVV-QMRF Class C — Master Index

**Project name:** VVV-QMRF Class C (VietVunVut Quantum Measurement Registration Framework — Class C testable)
**Status:** Class C (qualified) — structurally testable, empirically UNCONFIRMED (noise not ruled out)
**Version:** v44 (2026-06-01) — Level 4 Internal Consistency Audit (RCA 4.1/5) + P3-P4 Relationship Blockers Analysis (RCA 4.3/5). v43: Long-Term Research Plan v1.0 adopted

> **Version counter note:** this `vNN` is the **master-index content version**. The detailed [`04_governance/CHANGELOG.md`](04_governance/CHANGELOG.md) maintains a **separate**, finer-grained K-Space/sprint counter (currently v51); the two `vNN` sequences are **independent and need not match** (e.g., index v43 ≠ CHANGELOG v43 content). Cite the index version for overall project state.
**Zenodo DOI (v3.0):** [10.5281/zenodo.20431310](https://zenodo.org/records/20431310) — Working Paper v3.0 **PUBLISHED 2026-05-28**
**Zenodo DOI (v2.0):** [10.5281/zenodo.20289261](https://doi.org/10.5281/zenodo.20289261) (archived)
**Concept DOI (cite-all):** [10.5281/zenodo.20289260](https://doi.org/10.5281/zenodo.20289260)
**License:** CC BY 4.0

> **DISCLAIMER:** VVV-QMRF is independent Class C personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. VVV-QMRF is a **conceptual framework**, not a physical theory — it provides formal language for analyzing measurement registration but does not modify quantum dynamics. Full boundary protocol: `DISCLAIMER.md`. Formal definitions: [`06_references/VVV_QMRF_Definitions.md`](06_references/VVV_QMRF_Definitions.md).

---

## 1. What is VVV-QMRF?

Standard Quantum Mechanics has four physical postulates (P1–P4) describing state space, observables, measurement, and dynamics. These postulates are silent on the **registration architecture** of measurement — they do not specify what certifies a measurement, what distinguishes measurement from interaction, or what constitutes the registering system.

VVV-QMRF proposes a **registration-logic structure K**, axiomatized via K1–K8 (Layer 1, frozen) with bridge theorems T1–T9 (Layer 2). The framework identifies where standard QM interpretations lack the structural machinery to formalize registration-layer conditions.

**IMPORTANT:** VVV-QMRF is a **conceptual framework**, not a physical theory. It provides language and structure for analyzing measurement registration but does not propose new physical dynamics. The framework itself is not directly falsifiable. The **testable hypothesis** emerging from this framework is K9_E (P9) — see §2 and [Formal Definitions](06_references/VVV_QMRF_Definitions.md).

### This Repository Contains Three Logically Independent Projects

| # | Project | Type | Status |
|---|---------|------|--------|
| **A** | BE↔QM Comparative Mapping | Interpretive framework (comparative philosophy) | 30 nodes, 39 edges |
| **B** | VVV-QMRF Conceptual Framework | Conceptual architecture (K1-K8, T1-T9, E1-E16) | Frozen (Layer 1) |
| **C** | K9_E Testable Hypothesis | Falsifiable hypothesis + experimental proposal | Preprint submitted to arXiv (paper_002) |

> **MOTIVATION CHAIN (one-way, not derivational):**
> Project A → (motivates) → Project B → (motivates) → Project C.
>
> K9_E (Project C) can be tested independently of Projects A and B. A null result falsifies K9_E but does not invalidate the framework. A positive result confirms the hypothesis but does not prove the framework. Each project stands or falls on its own. See [Formal Definitions §4](06_references/VVV_QMRF_Definitions.md).

VVV-QMRF conjectures the existence of a structure-preserving map phi: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space (Class D conjecture; Track B Phases 1–4 complete 2026-05-22). **Level 4 freeze declared 2026-05-31 (3-Round RCA 4.69/5):** T4 → Class C; T7 → Class C; φ-O5 N-observer extension → ACTIVE. See `04_governance/RCA_phi_map_track_b_preparation_2026_05_31.md`.

## 2. What is Class C (qualified)?

**Class C** means VVV-QMRF K9_E provides a probability postulate (P9) motivated by K1–K8 structure that produces predictions **structurally different** from Standard QM (delta_S != 0 when beta > 0), passes all adversarial tests (4/4), avoids the Frauchiger–Renner paradox via K5 V_prov mechanism, and reduces Copenhagen/MWI as special cases. K9_E is a postulate, not a derivation from K1–K8; the axioms define structural properties only (see §3).

**Qualified** means K9_E is structurally motivated by K1-K8 and produces distinguishing predictions (delta_S != 0 when beta > 0), but the empirical evidence is **not confirmed** — non-uniform noise cannot be ruled out as an alternative explanation for the non-uniform visibility pattern in Proietti Figure 3.

**Downgrade reason (v30, 2026-05-24):** Noise sensitivity analysis (Delta_chi2 Decomposition + Noise Budget Analysis, RCA 4.77/5) returned **FAIL**: noise_threshold = 0.10 sigma RMS (threshold for PASS: > 3.0 sigma). With only 4 data points and K9_E's directional sensitivity, random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations. The 2.31sigma "signal" is a noise-detection threshold, not evidence for K9_E suppression. See `07_fits/noise_sensitivity_analysis.py` and `04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md`.

**Remaining empirical path:** Confirmation or rejection requires a dedicated experiment with dedicated noise characterization (prediction: delta_M3 = -0.223 at beta=0.3, illustrative, T4-H now THEOREM — conditional only on K9_E postulate P9). **K9-S12 Modified Bong protocol paper submitted to arXiv (2026-05-27).** Track 3 (Experimental Path) now ACTIVE — awaiting optical lab collaboration. See §4 for full 3-Round RCA.

> **→ K→p(o) Bridge Law — Single Entry Point:** [K_to_p_bridge_law.md](K_to_p_bridge_law.md) —
> the formula, predictions, falsification rule, experimental protocol, and canonical source map
> in one page. Read this FIRST if you want to understand the core output of Class C.

See [RCA Final Verdict](02_derivation_chain/RCA_Final_Verdict_Class_C_Genuine.md) for the v29 upgrade RCA (aggregate 4.50/5) and [P10-NOISE Methodology Decision](04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md) for the v30 downgrade RCA (aggregate 4.77/5).

---

## 3. Architecture Overview

```
Layer 1 (FROZEN)     K1–K8 Registration-logic axioms
       |              binary cert/V in {0,1}, bot_K, AdmJoint
       v
Layer 2 (UPDATABLE)  T1–T9 Bridge theorems + conservative extensions
       |              K_joint construction, colimit, relativization
       |              K5_prospective (v29), T8 frequency bridge, T9 K_ctx morphism
       |              K7_trace + D_enc (canonical Layer 2, K_Space_Axiomatization.md v2.4, RCA 4.77/5)
       |              D_obs (Observer Set Definition, Layer 2, RCA 4.3/5, [A-Obs] ELIMINATED 2026-05-31)
       v
Layer 3 (Class C)    K9_E Probability postulate (P9) + K10_R Registration Capacity Postulate
       |              K9_E: P(o|K) = Tr(E_o rho) * [1-beta*f_perp(o,K_ctx)]/Z_E  [Conv 2]
       |              1 free parameter beta; 0 assumptions; 8 terms with K-space provenance
       |              [A-E1]–[A-E4] ELIMINATED/RECLASSIFIED (v29); K9_E is a POSTULATE
       |              K10_R: S valid K-registrar iff C₁(←K1)∧C₂(←K4)∧C₃(←K2)∧C₄(←K3)
       |              Grounds ValidReg Condition 2; fills N_QM_VVV_00012; RCA 4.67/5 (2026-05-31)
       v              Both K9_E and K10_R are POSTULATES, not derivable from K1–K8 alone
Layer 4 (Class D)    Multi-paper data fit
       |              D1 Proietti CHSH: beta=0.598 (genuine fit), V=0.939, 2.31sigma
       |              D2 Bong LF: Phase 10b analysis INVALIDATED (K9-S8 marginalization)
       |              D3 Frauchiger–Renner: AVOIDED via K5 V_prov; V_FR2 PASS (2026-05-28) — K7_trace 4th canonical consumer; FR_VVV_fit_plan.md v0.1
       |              D4 Baumann&Brukner: T_BB Class C (conditional), T_BB' CLOSED, G1 CLOSED (K7_trace+D_enc), P2-C π/8 first-principles; v2.1
       v
Layer 5 (Class D)    Prediction + Reduction + Assessment
                     3-observer: delta_M3=-0.223 at beta=0.3 (11x; illustrative)
                     Copenhagen/MWI = special cases
```

### K-Space Axioms (K1–K8)

| Axiom | Name | Core function |
|-------|------|---------------|
| K1 | Act-Result Co-instantiation | Tuple k = (o, cert, V, t) — outcome and registration status are inseparable |
| K2 | Temporal Injectivity | t1 <_R t2 — native registration order |
| K3 | Self-Certification | cert(k) = 1 — self-certification marker |
| K4 | Registration Validity | V(k) in {0,1} — validity status |
| K5 | Cross-Registration Interaction | bot_K — incommensurability firing when k bot k_prev within C_K |
| K6 | Authentication | Auth(k) — non-transitive cross-context authentication |
| K7 | Closure | t_close — irreversible closure; V_final assigned |
| K8 | Cross-Space Preservation | V_joint(i(k)) = V(k) — validity preserved under embedding |

### K9_E Postulate (P9)

K9_E is a **postulate** (probability assignment rule), not a theorem derived from K1–K8. K1–K8 define structural properties (registration, validity, incommensurability) but do not uniquely determine a probability rule. K9_E fills this gap as Postulate P9 — a Type B framework extension motivated by K-space structure (bot_K, K_ctx) but carrying its own assumption (A1: K5 prospective firing). See [Phase 8 ERRATUM](02_derivation_chain/Phase8_candidate_equation.md).

```
P(o | K) = Tr(E_o rho) * [1 - beta * f_perp(o, K_ctx)] / Z_E

where:
  f_perp(o, K_ctx) = E[I(K5_prospective fires)]  [T8 — structural derivation]
                   = |{k_j in K_ctx : k_j bot_K and outcome-inconsistent with o}| / |K_ctx|
  K_ctx  = contextual K-state set  [T9 — K1-K8 + T1]
  beta   in [0, 1] — single free parameter
  Born limit: beta = 0 => P(o|K) = Tr(E_o rho) (exact — K9_E reduces to QM)
  Distinguishability: delta_S(beta=0.5) = -0.055 (theoretical — no empirical detection yet)
```

> **Canonical form (Conv 2, standardized 2026-05-30):** `f_perp` is the bot_K fraction (T8 derivation); `[1 − beta·f_perp]` is the suppression factor; `K_ctx` is the set of contextual K-states (T9). Code (`k9e_predictor.py`) uses scalar approximation: `suppression_factor = 1 − beta·K_ctx_scalar` where `K_ctx_scalar = n_bsm·G_CTX`. In the N=2 Level 0 projection, the fraction evaluates to `1 − |⟨b|d⟩|²` — a projection, not a general identity (`f_perp ≠ f(|⟨b|d⟩|²)` in general). RCA: [`04_governance/RCA_NORM1_standardize_conv2_2026_05_30.md`](04_governance/RCA_NORM1_standardize_conv2_2026_05_30.md).

### K9_E Term-by-Term Provenance (8 terms)

> **K9_E có 8 thành phần (T1–T8). 6/8 là khái niệm mới, không có trong Standard QM.**
> K9_E has 8 terms (T1–T8). 6/8 are new concepts not present in Standard QM.
>
> *Label note / Lưu ý ký hiệu:* the `T1–T8` identifiers in the table below index the **8 K9_E formula terms** — a namespace **distinct** from the Layer-2 **bridge theorems** `T1–T9` (e.g., "T8" here = the `isNull` gate, **not** the T8 frequency-bridge theorem). See `06_references/VVV_QMRF_Definitions.md` §5.

| # | Term | Definition | Source | In Standard QM? |
|---|------|-----------|--------|-----------------|
| T1 | `Tr(E_o ρ)` | Born rule probability | Standard QM (POVM) | ✅ QM standard |
| T2 | `β` | Suppression strength, β ∈ [0,1) | **FREE PARAMETER** — không có trong QM | ❌ **NEW** |
| T3 | `f_perp(o, k_i, K_ctx)` | Fraction of contextual observers with incompatible outcomes | K5 (⊥_K structural) — không có trong QM | ❌ **NEW** |
| T4 | `C(o_i, o_j)` | Compatibility map — outcome orthogonality | Tier 4 OI-1 — không có trong QM | ❌ **NEW** |
| T5 | `K_ctx(k_i, Exp)` | Set of K-states from other observers | T3-morphism + K2 — không có trong QM | ❌ **NEW** |
| T6 | `Z_E(k_i)` | Normalization factor | Modified from QM (QM auto-normalizes; K9_E needs explicit Z) | ⚠️ **MODIFIED** |
| T7 | `V(k)=0 → no P` | Bhrānti gate — invalid registration gets no probability | K4 + K5 → PP-1 v2 — không có trong QM | ❌ **NEW** |
| T8 | `isNull(k) → no P` | Anupalabdhi gate — null event gets no probability | K4 isNull guard — không có trong QM | ❌ **NEW** |

**Summary / Tổng kết:**

```
8 terms in K9_E
├── 1 term from Standard QM (T1: Born rule)
├── 1 term modified from QM (T6: normalization)
├── 6 terms ENTIRELY NEW (T2, T3, T4, T5, T7, T8)
└── 0 orphaned assumptions. Originally 4 assumptions [A-E1]–[A-E4] + [A-Obs] (unnamed). [A-E1] FULLY ELIMINATED (T9, L1-L5). [A-E2] FULLY ELIMINATED (T8-H1). [A-E3] RECLASSIFIED: FREE PARAMETER (β — measurement target, not assumption). [A-E4] BE-anchored. [A-Obs] FULLY ELIMINATED (D_obs, 2026-05-31, RCA 4.3/5). Net: 0 assumptions, 1 free parameter (β). See [RCA A-E3 Final Verdict](04_governance/RCA_A_E3_beta_universal_final_verdict.md).
```

See [Phase 8 Term-by-Term Provenance](02_derivation_chain/Phase8_candidate_equation.md) for the full decomposition.

---

## 4. Class C (genuine) — 3-Round RCA Upgrade Decision (v29)

> **UPGRADE (2026-05-23 RCA v29):** The original Class C (qualified) status was based on a **circular fit** (E_exp = V_exp * E_QM, mathematically guaranteed beta=0). The v29 RCA replaced this with a **genuine non-circular fit** using raw Proietti Figure 3 correlator values extracted from `Wigner_figure_3.md`. Raw data is significantly different from reconstructed data (e.g., A0B0 = -0.678 vs -0.604). The genuine fit yields beta=0.598 (not 0), V=0.939 (not 0.854), and Delta_chi2=5.35 (2.31sigma) favoring K9_E over QM-uniform-visibility. Three conditions were checked: (1) genuine empirical evidence, (2) A1 upgrade to K5_prospective axiom, (3) T4-H Step 1 category proof. All three passed with aggregate 4.50/5. **Class C upgraded from "qualified" to "genuine."** Evidence is real but ambiguous — K9_E multiplicative pattern not confirmed, experimental systematics not ruled out. See [RCA Final Verdict](02_derivation_chain/RCA_Final_Verdict_Class_C_Genuine.md) and [Genuine Fit RCA Round 1](02_derivation_chain/Phase10_genuine_fit_RCA_Round1.md).

| Round | Focus | Score | Threshold |
|-------|-------|-------|---------------|
| Round 1 | Empirical evidence (genuine fit) | **4.00/5** | PASS (>=3.5/5) |
| Round 2 | Derivational purity (A1 upgrade) | **4.90/5** | PASS (>=4.0/5) |
| Round 3 | Structural foundation (T4-H weaken) | **4.60/5** | PASS (>=3.5/5) |

**Aggregate: 4.50/5 (simple average) / 4.45/5 (weighted: 40% R1 + 30% R2 + 30% R3)** — PASS (>=4/5).

### Final Classification

> **VVV-QMRF K9_E = Class C (qualified) — structurally testable, empirically UNCONFIRMED.**
>
> K9_E achieves Class C structurally (unchanged): probability postulate P9 motivated by K1-K8 structure, generates distinguishability != Standard QM (delta_S != 0 when beta > 0), avoids FR paradox via K5 V_prov, reduces Copenhagen/MWI as special cases.
>
> **v30 downgrade (2026-05-24):** Noise sensitivity analysis returned FAIL (noise_threshold = 0.10 sigma RMS << 1.0 threshold). K9_E's directional sensitivity + only 4 data points means random noise produces Delta_chi2 >= 5.35 in ~50% of realizations at any RMS magnitude. The 2.31sigma "signal" is NOT evidence for K9_E — it reflects model flexibility, not physical suppression. Class C downgraded from (genuine) to (qualified). Confirmation requires 3-observer experiment with dedicated noise characterization.
>
> **v29 upgrades (3 conditions — structural foundation remains valid):**
> 1. **Genuine empirical evidence:** Raw Proietti Figure 3 data used for non-circular fit. However, noise sensitivity analysis (v30) shows this evidence is NOT robust — single-setting perturbation of 1.85 sigma at A0B0 eliminates the K9_E advantage. A0B0 alone drives 80% of Delta_chi2.
> 2. **A1 upgraded:** K5_prospective added as conservative extension to K5. Zero Class D assumptions remain.
> 3. **T4-H THEOREM (4/4, 2026-05-28):** All 4 steps proven. K9_E only needs T1 (independent). 3-OBS upgraded to Class C.

---

## 5. Key Numbers

> **NOTE (2026-05-24 v30):** Items marked `[G]` derive from genuine fit but are **qualified by noise sensitivity analysis** (FAIL: noise_threshold = 0.10 sigma RMS, `07_fits/noise_sensitivity_analysis.py`). The 2.31sigma "signal" is NOT robust — random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations. `[T]` = theoretical/structural (unaffected by noise). `[C]` = circular fit (historical, superseded). `[I]` = illustrative (conditional on unproven assumptions). `[N]` = noise sensitivity result (new in v30).

| Quantity | Value | Meaning | Source type |
|----------|-------|---------|-------------|
| beta (best-fit, Proietti D1 raw) | 0.598 | K9_E != Standard QM at best-fit | `[G]` genuine fit |
| V (visibility, fitted) | 0.939 | Higher than circular V=0.854 — non-uniform visibility detected | `[G]` genuine fit |
| chi2/DOF | 0.670 (DOF=2) | Good fit quality, p=0.51 | `[G]` genuine fit |
| Delta_chi2 (K9_E vs QM-only) | 5.35 (2.31sigma) | K9_E improves over QM-uniform-visibility | `[G]` genuine fit |
| delta_S (beta=0.5, CHSH) | -0.055 | Theoretical distinguishability magnitude | `[T]` structural |
| delta_M3 (beta=0.3, 3-observer) | -0.223 | 11x amplification (illustrative, T4-H THEOREM — conditional on K9_E P9 only) | `[I]` illustrative |
| FR paradox | AVOIDED | K5 V_prov breaks assumption chain C | `[T]` structural |
| Born recovery | cert=1 and V=1 => Born exact | Verified | `[T]` structural |
| Adversarial tests | 4/4 PASS | No counterexample, 0 axiom violations | `[T]` structural |
| Operationalizability gates | 3/3 PASS | G1/G2/G3 all 5.0/5 | `[T]` structural |
| K9_E pattern check (2BSM/1BSM ratio) | -0.78 (predicted ~2) | Multiplicative pattern NOT confirmed | `[G]` genuine fit |
| Noise threshold (2-sigma, B4 Monte Carlo) | 0.10 sigma RMS | Noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations | `[N]` noise analysis |
| Single-setting fragility (B2) | A0B0: 1.85 sigma | Only 1.85 sigma shift at A0B0 eliminates K9_E advantage | `[N]` noise analysis |
| A0B0 share of Delta_chi2 (B1) | 80% | Nearly entire K9_E "signal" driven by one data point | `[N]` noise analysis |

---

## 6. File Map

### "I want to understand X — read Y"

| Question | File |
|----------|------|
| What are the K1–K8 axioms? | [01_axiomatization/K_Space_Axiomatization.md](01_axiomatization/K_Space_Axiomatization.md) |
| How does K map to Hilbert space? | [01_axiomatization/K_to_BH_Structure_Preserving_Map_v0_1.md](01_axiomatization/K_to_BH_Structure_Preserving_Map_v0_1.md) |
| What is the K9_E equation? | [02_derivation_chain/Phase8_candidate_equation.md](02_derivation_chain/Phase8_candidate_equation.md) |
| How was K9_E selected over K9_A/B/C? | [03_k9_sprints/k9_analysis/K9S3_ranking.md](03_k9_sprints/k9_analysis/K9S3_ranking.md) |
| How was K9_E formalized? | [03_k9_sprints/k9_analysis/K9S4_primary_formalized.md](03_k9_sprints/k9_analysis/K9S4_primary_formalized.md) |
| How was K9_E adversarially tested? | [02_derivation_chain/Phase9_adversarial_testing.md](02_derivation_chain/Phase9_adversarial_testing.md) |
| How does K9_E fit Proietti data? | [02_derivation_chain/Phase10_data_fitting.md](02_derivation_chain/Phase10_data_fitting.md) |
| What happened with Bong LF? | [02_derivation_chain/Phase10b_bong_lf.md](02_derivation_chain/Phase10b_bong_lf.md) |
| What is the Marginalization Cancellation? | [03_k9_sprints/k9_analysis/K9S8_composition_law.md](03_k9_sprints/k9_analysis/K9S8_composition_law.md) |
| Does K9_E avoid the FR paradox? | [02_derivation_chain/Phase10c_fr_consistency.md](02_derivation_chain/Phase10c_fr_consistency.md) |
| What is the 3-observer prediction? | [02_derivation_chain/Phase11_3observer_prediction.md](02_derivation_chain/Phase11_3observer_prediction.md) |
| What is the 3-OBS registration transition mechanism? | [02_derivation_chain/3observer_registration_transition.md](02_derivation_chain/3observer_registration_transition.md) (Class C — T4-H VERIFIED 2026-05-28) |
| How are T4-H Steps 3-4 proven? | [02_derivation_chain/T4_H_steps3_4_k1k8_universal.md](02_derivation_chain/T4_H_steps3_4_k1k8_universal.md) (T-PRES Lemma + K1-K8 verification + universal property, RCA 4.74/5) |
| How do interpretations reduce? | [02_derivation_chain/Phase12_structural_reduction.md](02_derivation_chain/Phase12_structural_reduction.md) |
| What is the honest assessment? | [02_derivation_chain/Phase13_honest_assessment.md](02_derivation_chain/Phase13_honest_assessment.md) |
| What is the full plan with RCA verdicts? | [04_governance/K_Space_Axiomatization_plan.md](04_governance/K_Space_Axiomatization_plan.md) |
| What was the K9_A/B/C pre-proposal? | [04_governance/K_Space_Axiomatization_plan_v3.md](04_governance/K_Space_Axiomatization_plan_v3.md) (SUPERSEDED) |
| What decisions shaped the project? | [04_governance/decisions/](04_governance/decisions/) |
| What EX intelligence informed prioritization? | [05_ex_compass/ex_compass_index.md](05_ex_compass/ex_compass_index.md) |
| How do I reproduce the numerical fits? | [07_fits/](07_fits/) — see section 7 below |
| Where are the source papers? | [00_source_papers/](00_source_papers/) |
| What is the testability status after K9-S12? | [03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md](03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md) |
| What changed in v29 (Class C genuine)? | [RCA Final Verdict](02_derivation_chain/RCA_Final_Verdict_Class_C_Genuine.md) |
| What is the genuine non-circular fit? | [Genuine Fit RCA Round 1](02_derivation_chain/Phase10_genuine_fit_RCA_Round1.md) |
| Where is the core Working Paper v3.0? | [../../papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md](../../papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md) (Finalized core paper) |
| Where is the single-waveplate child paper (paper_002)? | [../../papers/paper_002/manuscript.md](../../papers/paper_002/manuscript.md) (arXiv preprint, submitted 2026-05-27) |
| How was A1 upgraded? | [K_Space_Axiomatization.md §K5_prospective](01_axiomatization/K_Space_Axiomatization.md) |
| How was T4-H Step 1 proven? | [T4-H Step 1 Category Proof](02_derivation_chain/T4_H_step1_category_proof.md) |
| How was T4-H Step 2 colimit constructed? | [T4-H Step 2 Colimit Construction](02_derivation_chain/T4_H_step2_colimit_construction.md) |
| How does T8 bridge K5_prospective → K9_E? | [T8 + H1–H4 in K_Space_Axiomatization.md](01_axiomatization/K_Space_Axiomatization.md) (Layer 2) |
| Where is the K9_E origin investigation? | [RCA K9_E Origin Investigation](04_governance/rca_k9e_origin_investigation.md) |
| How is P10-NOISE noise sensitivity analyzed? | [RCA Methodology Decision](04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md) + [Spec](07_fits/noise_sensitivity_analysis_spec.md) |
| How was phi-map K→B(H) resolved (RCA)? | [RCA Phi-Map Round 1](04_governance/RCA_phi_map_round1_structural_audit.md) → [Round 2](04_governance/RCA_phi_map_round2_structural_resolution.md) → [Round 3 Decision](04_governance/RCA_phi_map_round3_final_decision.md) |
| How was K9E-PAT resolved (RCA)? | [T1B Model Comparison RCA](04_governance/T1B_model_comparison_RCA.md) → [T1C Resolution](04_governance/T1C_k9e_pat_resolution.md) |
| What is the Post-v30 execution plan? | [Post_v30_Execution_Plan.md](04_governance/Post_v30_Execution_Plan.md) (Tracks 1 & 2 COMPLETED) |
| What is the long-term research plan (2026-2028+)? | [Long_Term_Research_Plan_2026_05_31.md](04_governance/Long_Term_Research_Plan_2026_05_31.md) (3-Pillar × 5-Phase, RCA 4.69/5 PASS, 2026-05-31) |
| What blocks the P3-P4 relationship in VVV-QMRF? | [RCA P3-P4 Relationship Blockers](04_governance/RCA_P3_P4_Relationship_Blockers_2026_06_01.md) (4 blockers: 2 fixable, 2 fundamental, RCA 4.3/5, 2026-06-01) |
| Are D_joint, AdmJoint, requires_K_joint internally consistent? | [RCA Level 4 Internal Consistency Audit](04_governance/RCA_Level_4_Internal_Consistency_Audit_2026_06_01.md) (7 candidates, 2 structural defects FIXED, RCA 4.1/5, 2026-06-01) |
| What happened in the v31 RCA session? | [RCA Session Report](04_governance/RCA_session_post_v30_2026_05_24.md) |
| How does B&B (2024) fit VVV-QMRF? | [BB_VVV_fit_plan.md](09_Fitting_Baumann_Brukner/BB_VVV_fit_plan.md) (v1.4 — T_BB Class C, P2-C §20 first-principles) |
| What is the BB-VVV compatibility result? | [BB_VVV_compatibility_section.md](09_Fitting_Baumann_Brukner/BB_VVV_compatibility_section.md) (v2.1 — T_BB' CLOSED, P2-C π/8 exact) |
| How does FR (2018) fit VVV-QMRF? | [FR_VVV_fit_plan.md](10_Fitting_Frauchiger_Renner/FR_VVV_fit_plan.md) (v0.1 — V_FR2 PASS, K7_trace 4th canonical consumer confirmed) |
| What are K7_trace and D_enc? | [K_Space_Axiomatization.md §K7_trace/§D_enc](01_axiomatization/K_Space_Axiomatization.md) (canonical Layer 2, v2.4, RCA 4.77/5; 4 consumers: T_BB+D_enc+3-OBS+FR). Origin: [BB_VVV_fit_plan.md §18-§19](09_Fitting_Baumann_Brukner/BB_VVV_fit_plan.md) |

### Folder Index

| Folder | Contents | File count |
|--------|----------|------------|
| `00_source_papers/` | arXiv sources for D1 (Proietti), D2 (Bong), D3 (FR) | ~25 |
| `01_axiomatization/` | K_Space_Axiomatization.md + K->BH map + meta-architecture documents | 10 |
| `02_derivation_chain/` | Phase 7–13 deliverables + supporting analyses + v29 RCA + 3-OBS mechanism + T4-H Steps 3-4 proof | 21 |
| `03_k9_sprints/` | K9 analysis chain (S1–S12) + K9 analysis plan | ~22 |
| `04_governance/` | Master plan + Post-v30 plan + Long-Term Research Plan + Track 1 reports + CHANGELOG + decisions + RCA reports | ~25 |
| `05_ex_compass/` | VVV-QMRF-EX snapshot (compass reference, not structure import) | ~65 |
| `06_references/` | VVV-QMRF core terminology + bridge documents | 8 |
| `07_fits/` | Python reproduction scripts + utils/ module + SOT data + requirements.txt | 18 |
| `08_archives/` | Archived meta-architecture documents | 7 |
| `09_Fitting_Baumann_Brukner/` | B&B (2024) fit plan v1.4 + compatibility v2.1 (T_BB' CLOSED) + verification scripts (T_BB PASS, P2-C) + 5 RCA gates + source paper | 21 |
| `10_Fitting_Frauchiger_Renner/` | FR (2018) fit plan v0.1 + K7_trace consumer verification script (V_FR2 PASS 2026-05-28) | 4 |

---

## 7. How to Reproduce Numerical Fits

### Prerequisites
- Python 3.9+
- Windows / Linux / macOS

### Setup
```powershell
cd 07_fits
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows
# source .venv/bin/activate     # Linux/macOS
pip install -r requirements.txt
```

### Run Order

| # | Script | Phase | Output |
|---|--------|-------|--------|
| 1 | `proietti_chsh_fit.py` | Phase 10a | Proietti CHSH fit (beta=0, PATH A) |
| 2 | `fr_consistency.py` | Phase 10c | FR paradox avoidance verification |
| 3 | `run_all_checks.py` | Joint | 3-way consistency check |
| 4 | `K9S9_conditional_predictions.py` | K9-S9 | Conditional prediction scenarios |
| 5 | `K9S11_bong_predictions.py` | K9-S11 | Bong LF predictions |
| 6 | `universal_theorem_lf_check.py` | K9-S11c | Universal theorem LF compatibility |
| 7 | `statistical_significance.py` | K9-S11d | Statistical significance scan |
| 8 | `alpha_threshold_scan.py` | K9-S11d | Alpha threshold scan |
| 9 | `proietti_geometry_check.py` | K9-S11b | Proietti geometry check |
| 10 | `K9S12_proposal.py` | K9-S12 | Modified Bong protocol proposal |
| 11 | `d1_blk1_4point_fit.py` | — | Alternative 4-point D1 fit |
| 12 | `proietti_raw_fit.py` | Phase 10a (v29) | **Genuine non-circular fit** — beta=0.598, 2.31sigma |
| **13** | **`noise_sensitivity_analysis.py`** | **P10-NOISE (v30)** | **Noise budget analysis: FAIL — noise_threshold=0.10 sigma RMS, downgrade genuine→qualified** |

**Note:** Data is extracted inline from arXiv source `.tex` files in `00_source_papers/`. See individual scripts for extraction methodology.

> **CAUTION (2026-05-24 v30):** The genuine fit (script #12, beta=0.598, 2.31sigma) is **NOT robust to noise**. Script #13 (`noise_sensitivity_analysis.py`) demonstrates that random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations due to K9_E's directional sensitivity with only 4 data points. Class C downgraded from (genuine) to (qualified). The 2.31sigma "signal" reflects model flexibility, not physical K9_E suppression.
>
> **RESOLVED (2026-05-23):** `utils/` module (`utils.qm_standard`, `utils.k9a_predictor`, `utils.k9e_predictor`) restored. All scripts (#1, #3, #11) now run successfully. `Wigner_figure_3.md` SOT document created for raw Proietti Figure 3 data. Full suite: 9/9 sanity checks PASS, 12/12 scripts executable.
>
> **MODEL NOTE (2026-05-23):** Two K9_E implementations co-exist with different calibration paths: `utils/k9e_predictor.py` uses an **additive** model (E = E_QM * [1 − beta·n_BSM·g_ctx], g_ctx ≈ 0.039, calibrated from theoretical delta_S = −0.055 at β=0.5). `proietti_raw_fit.py` uses a **multiplicative** per-observer model (E = E_QM * [1 − beta·g_eff]^n_BSM, g_eff = 0.146, calibrated from PP-4 sanity check 4D scan). The two models agree at first order in β·g but diverge at β > 0.3. The multiplicative model produces larger suppression and is used for the genuine fit. `run_all_checks.py` uses the additive model (via `k9e_predictor`) for sanity checks only.

---

## 8. Open Items

| # | Item | Status | Priority |
|---|------|--------|----------|
| A1 | ~~K5 prospective firing — promote from "semantic extension" to axiom text~~ | **RESOLVED (v29)** — upgraded to K5_prospective clause in K_Space_Axiomatization.md | ~~HIGH~~ |
| K9E-PAT | ~~K9_E multiplicative pattern (2BSM/1BSM ratio ~2) not confirmed by raw data (ratio = -0.78)~~ | **CLOSED (UNRESOLVABLE, v31)** — empirical ratio = two sub-σ residuals divided → red herring. Both models predict ratio ~2. 4 data points insufficient. Deferred to K9-S12 experiment. See [T1C Resolution](04_governance/T1C_k9e_pat_resolution.md) | ~~HIGH~~ |
| IBM-Q | ~~IBM Quantum execution plan for K9_E testing~~ | **REJECTED (v31)** — double category error (K9_E requires K-space structure; IBM QPU has none). See [RCA Session Report](04_governance/RCA_session_post_v30_2026_05_24.md) | ~~HIGH~~ |
| POST-v30 | Post-v30 execution plan (K9E-PAT → K9-S12 paper → experiment) | **Track 1 & 2 COMPLETED** (arXiv submitted 2026-05-27). Track 3 ACTIVE — [Post_v30_Execution_Plan.md](04_governance/Post_v30_Execution_Plan.md) | HIGH |
| 3-OBS | 3-observer experiment — delta_M3 = -0.223 (11x) prediction ready, experimental design deferred | **FUTURE WORK** — mechanism file: [3observer_registration_transition.md](02_derivation_chain/3observer_registration_transition.md) (Class C — T4-H THEOREM 4/4, 2026-05-28) | HIGH |
| **[A-3O-2]** | T5 K_joint composition associativity | **RESOLVED (conditional, 2026-05-30, RCA 4.4/5)** — [T5_conditional_theorem_proof.md](02_derivation_chain/T5_conditional_theorem_proof.md). Hybrid A+B proof: (C1) T4-H THEOREM, (C2) admissibility, (C3) F7d via K5 content-basedness. | HIGH |
| **[A-NS]** | No-signaling N>2 — depends on T5 | **Conditional THEOREM (2026-05-30)** — N=2 proven (Phase 7 B-5). N>2: conditional induction via T5 (§6 of T5 proof). Same (C1)(C2)(C3) scope. See [T5_conditional_theorem_proof.md §6](02_derivation_chain/T5_conditional_theorem_proof.md). | HIGH |
| P10-NOISE | Non-uniform experimental noise cannot be ruled out as alternative explanation for genuine fit improvement | New (v29) | MEDIUM |
| P10-TIM | Null-model N0 fit omitted — requires raw event-level data; deferred | DECISION-LOCKED (RCA R4) | MEDIUM |
| BONG | Bong LF modified protocol proposal (K9-S12) | **arXiv SUBMITTED (2026-05-27)** — Paper: "A Single-Waveplate Test of Outcome-Dependent Quantum Registration in Extended Wigner's Friend Scenarios" (Draft v94, papers/paper_002/). Track 3 ACTIVE: awaiting optical lab collaboration. | ~~MEDIUM~~ |
| PUB | Publication path — Foundations of Physics / Phys Rev A submission readiness | arXiv preprint submitted (2026-05-27). Next: journal submission after community feedback. | MEDIUM |
| BB-VVV | Baumann & Brukner (2024) fit plan | **COMPLETE (v2.1, 2026-05-28)** — T_BB Class C (conditional), T_BB' CLOSED (superseded), P2-C π/8 exact (first-principles), G1 CLOSED. K7_trace + D_enc canonical Layer 2 (v2.4, RCA 4.77/5; 4 consumers). See [09_Fitting_Baumann_Brukner/](09_Fitting_Baumann_Brukner/) | ~~MEDIUM~~ |
| FR-VVV | Frauchiger & Renner (2018) fit plan | **V_FR2 PASS (2026-05-28)** — K7_trace 4th canonical consumer confirmed; T_FR 2-agent sketch Class D (G_FR2 blocks full formalization). See [10_Fitting_Frauchiger_Renner/](10_Fitting_Frauchiger_Renner/) | MEDIUM |

---

## 9. EX Compass Note

VVV-QMRF-EX (`05_ex_compass/`) is used as a **compass only** — it provides intelligence about K-rho relationships, structural stress points (KE-SC 4.0), and prioritization guidance. EX structure is **not imported** into the VVV-QMRF core. See [ex_compass_index.md](05_ex_compass/ex_compass_index.md) for stress-point summary.

Rule: `Internal-first, VVV-QMRF-EX-verified, selectively imported.`

---

## 10. Citation

```bibtex
@misc{vietvunvut2026vvvqmrf,
  author    = {VietVunVut (Viet - Nguyen Xuan)},
  title     = {VVV-QMRF Class C: Registration-Layer Probability Bridge
               from Buddhist Epistemology to Quantum Measurement},
  year      = {2026},
  doi       = {10.5281/zenodo.20289261},
  publisher = {Zenodo},
  note      = {Working Paper v2.0. Class C (qualified).
               Independent personal research, not peer-reviewed.}
}
```

---

*Project VVV-QMRF Class C — Master Index v44 (2026-06-01). Level 4 Internal Consistency Audit (RCA 4.1/5) + P3-P4 Relationship Blockers (RCA 4.3/5). D_obs Observer Set Formal Definition (RCA 4.3/5). [A-Obs] FULLY ELIMINATED. K_ctx derivation chain complete. T5 Conditional THEOREM (RCA 4.4/5). [A-3O-2] RESOLVED (conditional). [A-NS] Conditional THEOREM via induction. 0 open assumptions. 1 free parameter (β). Class C (qualified) — structurally testable, empirically UNCONFIRMED.*
