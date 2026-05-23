Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Project VVV-QMRF Class C — Master Index

**Project name:** VVV-QMRF Class C (VietVunVut Quantum Measurement Registration Framework — Class C testable)
**Status:** Class C (qualified) — structurally testable, empirically pending
**Version:** v28 final (2026-05-23)
**Zenodo DOI:** [10.5281/zenodo.20289261](https://doi.org/10.5281/zenodo.20289261) (Working Paper v2.0)
**License:** CC BY 4.0

> **DISCLAIMER:** VVV-QMRF is independent Class C personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 1. What is VVV-QMRF?

Standard Quantum Mechanics has four physical postulates (P1–P4) describing state space, observables, measurement, and dynamics. These postulates are silent on the **registration architecture** of measurement — they do not specify what certifies a measurement, what distinguishes measurement from interaction, or what constitutes the registering system.

VVV-QMRF proposes a **registration-logic structure K**, axiomatized via K1–K8 (Layer 1, frozen) with bridge theorems T1–T7 (Layer 2). The framework identifies where standard QM interpretations lack the structural machinery to formalize registration-layer conditions. The K-space carrier supports 16 registration-layer postulates (E1–E16) derived from structural analysis of Buddhist Pramana epistemology (Dignaga–Dharmakirti tradition).

VVV-QMRF conjectures the existence of a structure-preserving map phi: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space (Class D conjecture; Track B Phases 1–3 complete).

## 2. What is Class C (qualified)?

**Class C** means VVV-QMRF K9_E provides a probability postulate (P9) motivated by K1–K8 structure that produces predictions **structurally different** from Standard QM (delta_S != 0 when beta > 0), passes all adversarial tests (4/4), avoids the Frauchiger–Renner paradox via K5 V_prov mechanism, and reduces Copenhagen/MWI as special cases. K9_E is a postulate, not a derivation from K1–K8; the axioms define structural properties only (see §3).

**Qualified** means the distinguishing signal lies **below current experimental detection threshold** — the fit to reconstructed Proietti D1 data yields beta = 0 (K9_E = Standard QM exactly), with 1-sigma upper bound beta <= 0.175 (circular fit — see §4 ERRATUM). K9_E demonstrates internal consistency but no empirical distinguishability from QM at current precision. Confirmation or rejection requires a 3-observer experiment (prediction: delta_M3 = -0.223 at beta=0.3, illustrative).

See [Final Verdict](04_governance/K_Space_Axiomatization_plan.md) for the full 3-round RCA synthesis (aggregate 4.06/5).

---

## 3. Architecture Overview

```
Layer 1 (FROZEN)     K1–K8 Registration-logic axioms
       |              binary cert/V in {0,1}, bot_K, AdmJoint
       v
Layer 2 (UPDATABLE)  T1–T7 Bridge theorems
       |              K_joint construction, colimit, relativization
       v
Layer 3 (Class C)    K9_E Probability postulate (P9)
       |              P(o|K) = Tr(E_o rho) * f_perp(K_ctx)
       |              1 parameter beta, 8 terms with K-space provenance
       |              1 assumption A1 (K5 prospective firing, Class D pending)
       v              K9_E is a POSTULATE, not derivable from K1–K8 alone
Layer 4 (Class D)    Multi-paper data fit
       |              D1 Proietti CHSH: beta=0, PATH A beta<=0.175
       |              D2 Bong LF: Phase 10b analysis INVALIDATED (K9-S8 marginalization)
       |              D3 Frauchiger–Renner: AVOIDED via K5 V_prov
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
P(o | K) = Tr(E_o rho) * f_perp(K_ctx)

where:
  f_perp(K_ctx) = 1 - beta * K_ctx
  K_ctx = sum_{i != j} I(k_i bot k_j) / N_pairs
  beta in [0, 1] — single free parameter
  Born limit: beta = 0 => P(o|K) = Tr(E_o rho) (exact — K9_E reduces to QM)
  Distinguishability: delta_S(beta=0.5) = -0.055 (theoretical — no empirical detection yet)
```

---

## 4. Class C (qualified) — 3-Round RCA Decision

> **ERRATUM (2026-05-23 RCA Logic Audit):** Round 2 (Empirical evidence, 3.63/5 FAIL) uses a **circular fit** as its primary data input. Phase 10's Proietti D1 "data" was reconstructed as `E_exp = V_exp * E_QM`, and K9_E at beta=0 reduces to QM. The chi^2 minimization of `(V*E_QM - V*E_QM*(1-beta*g))^2` is mathematically guaranteed to yield beta=0. The Phase 10 result demonstrates **internal consistency** of K9_E (constraint satisfaction, normalization), not empirical comparison with real experimental data. The "qualified" status is correct (empirically pending), but the Round 2 score and PATH A bounds below derive from a tautological fit, not from raw Proietti Figure 3 data. See [Phase 10 ERRATUM](02_derivation_chain/Phase10_data_fitting.md) and [Phase 10 Joint Verdict](02_derivation_chain/Phase10_joint_verdict.md).

| Round | Focus | Score | Threshold 4/5 |
|-------|-------|-------|---------------|
| Round 1 | Derivational purity | **4.25/5** | PASS |
| Round 2 | Empirical evidence | **3.63/5** | FAIL (circular fit — see ERRATUM above) |
| Round 3 | Synthesis classification | **4.30/5** | PASS |

**Aggregate: 4.06/5** — PASS (>=4/5). Arithmetic mean of three rounds. Round 2 FAIL is not weighted differently from Round 1/3 PASS scores; the "qualified" qualifier directly reflects the Round 2 failure — structural Class C is achieved, but empirical evidence is insufficient (circular fit + no raw experimental data).

### Final Classification

> **VVV-QMRF K9_E = Class C (qualified) — structurally testable, empirically pending.**
>
> K9_E achieves Class C structurally: probability postulate P9 motivated by K1–K8 structure, generates distinguishability != Standard QM (delta_S != 0 when beta > 0), avoids FR paradox via K5 V_prov, reduces Copenhagen/MWI as special cases.
>
> **3 conditions:**
> 1. **A1 upgrade (required):** K5 prospective firing must be promoted from "semantic extension" to axiom text. Until then, K9_E carries 1 Class D assumption.
> 2. **Phase 10->9 feedback (applied):** P9-C6 "Class C confirmed" qualified by beta=0 empirical limitation.
> 3. **3-observer experiment (future):** Confirmation or rejection requires experiment measuring delta_M3 = -0.223 (11x amplification).

---

## 5. Key Numbers

> **NOTE (2026-05-23 RCA Logic Audit):** Items marked `[C]` derive from a **circular fit** (data reconstructed from QM, not from raw experimental data — see §4 ERRATUM). These values demonstrate internal consistency, not empirical constraint. Items marked `[T]` are theoretical/structural results independent of the fit. Items marked `[I]` are illustrative predictions at a chosen beta value, not predictions from best-fit.

| Quantity | Value | Meaning | Source type |
|----------|-------|---------|-------------|
| beta (best-fit, Proietti D1) | 0 | K9_E = Standard QM at best-fit | `[C]` circular fit |
| PATH A upper bound (1-sigma) | beta <= 0.175 | Distinguishability not excluded up to this value (from reconstructed data) | `[C]` circular fit |
| delta_S (beta=0.5, CHSH) | -0.055 | Theoretical distinguishability magnitude | `[T]` structural |
| delta_M3 (beta=0.3, 3-observer) | -0.223 | 11x amplification over 2-observer (illustrative: beta=0.3 is above PATH A 1-sigma bound) | `[I]` illustrative |
| chi2/DOF (beta=0) | 0 | Perfect fit (degenerate — K9_E = QM at beta=0) | `[C]` circular fit |
| FR paradox | AVOIDED | K5 V_prov breaks assumption chain C | `[T]` structural |
| Born recovery | cert=1 and V=1 => Born exact | Verified | `[T]` structural |
| Adversarial tests | 4/4 PASS | No counterexample, 0 axiom violations | `[T]` structural |
| Operationalizability gates | 3/3 PASS | G1/G2/G3 all 5.0/5 | `[T]` structural |

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
| How do interpretations reduce? | [02_derivation_chain/Phase12_structural_reduction.md](02_derivation_chain/Phase12_structural_reduction.md) |
| What is the honest assessment? | [02_derivation_chain/Phase13_honest_assessment.md](02_derivation_chain/Phase13_honest_assessment.md) |
| What is the full plan with RCA verdicts? | [04_governance/K_Space_Axiomatization_plan.md](04_governance/K_Space_Axiomatization_plan.md) |
| What was the K9_A/B/C pre-proposal? | [04_governance/K_Space_Axiomatization_plan_v3.md](04_governance/K_Space_Axiomatization_plan_v3.md) (SUPERSEDED) |
| What decisions shaped the project? | [04_governance/decisions/](04_governance/decisions/) |
| What EX intelligence informed prioritization? | [05_ex_compass/ex_compass_index.md](05_ex_compass/ex_compass_index.md) |
| How do I reproduce the numerical fits? | [07_fits/](07_fits/) — see section 7 below |
| Where are the source papers? | [00_source_papers/](00_source_papers/) |
| What is the testability status after K9-S12? | [03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md](03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md) |

### Folder Index

| Folder | Contents | File count |
|--------|----------|------------|
| `00_source_papers/` | arXiv sources for D1 (Proietti), D2 (Bong), D3 (FR) | ~25 |
| `01_axiomatization/` | K_Space_Axiomatization.md + K->BH map + meta-architecture documents | 10 |
| `02_derivation_chain/` | Phase 7–13 deliverables + supporting analyses | 15 |
| `03_k9_sprints/` | K9 analysis chain (S1–S12) + K9 analysis plan | ~22 |
| `04_governance/` | Master plan v28 + v3 SUPERSEDED + CHANGELOG + decisions + pre-plan | ~16 |
| `05_ex_compass/` | VVV-QMRF-EX snapshot (compass reference, not structure import) | ~65 |
| `06_references/` | VVV-QMRF core terminology + bridge documents | 8 |
| `07_fits/` | Python reproduction scripts + requirements.txt | 12 |
| `08_archives/` | Archived meta-architecture documents | 7 |

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

**Note:** Data is extracted inline from arXiv source `.tex` files in `00_source_papers/`. See individual scripts for extraction methodology.

> **CAUTION (2026-05-23 RCA Logic Audit):** `d1_blk1_4point_fit.py` and `proietti_chsh_fit.py` use **reconstructed data** (visibility model E_exp = V_exp * E_QM), not raw experimental values from Proietti Figure 3. The resulting beta=0 fit is a tautology — see §4 ERRATUM. To obtain a genuine empirical constraint, raw individual correlator values from Proietti Figure 3 are needed.

---

## 8. Open Items

| # | Item | Status | Priority |
|---|------|--------|----------|
| A1 | K5 prospective firing — promote from "semantic extension" to axiom text in K9_E derivation | **REQUIRED** for unqualified Class C | HIGH |
| 3-OBS | 3-observer experiment — delta_M3 = -0.223 (11x) prediction ready, experimental design deferred | **FUTURE WORK** | HIGH |
| P10-TIM | Null-model N0 fit omitted — requires raw event-level data; deferred | DECISION-LOCKED (RCA R4) | MEDIUM |
| BONG | Bong LF modified protocol proposal (K9-S12) | In progress | MEDIUM |
| PUB | Publication path — Foundations of Physics / Phys Rev A submission readiness | Outlined in Phase 13 | MEDIUM |

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

*Project VVV-QMRF Class C — Master Index v1.0 (2026-05-23). Generated from plan v28 final (3-round RCA). Class C (qualified) — structurally testable, empirically pending.*
