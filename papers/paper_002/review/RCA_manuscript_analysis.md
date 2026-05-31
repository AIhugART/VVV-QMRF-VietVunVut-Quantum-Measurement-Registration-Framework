Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — manuscript.md (paper_002, draft v94)

**Date:** 2026-05-31 | **Method:** Independent Python recalculation of every numerical claim (v94 re-sync verification)

---

## Executive Summary

| Category | Checks | Pass | Fail | Status |
|----------|--------|------|------|--------|
| Density matrix & state | 3 | 3 | 0 | ✅ |
| Bloch sphere / f_perp (§3.3) | 8 | 8 | 0 | ✅ |
| Equatorial cancellation theorem | 5 | 5 | 0 | ✅ |
| All 9 correlators (§5.1) | 7 | 7 | 0 | ✅ |
| Gen LF 1 inequality (§5.2) | 4 | 4 | 0 | ✅ |
| δ⟨AB⟩ sensitivity table (§5.3) | 15 | 15 | 0 | ✅ |
| S2 correlator table | 13 | 13 | 0 | ✅ |
| Calibration & decision table (§4.4, §8.1) | 5 | 5 | 0 | ✅ |
| Monte Carlo (§6) | 1 | 1 | 0 | ✅ |
| FOM vs θ sweep (§4.1) | 5 | 5 | 0 | ✅ |
| Numerical θ sweep (internal) | 1 | 1 | 0 | ✅ |
| **Total** | **67** | **67** | **0** | **100% PASS** |

---

## Findings & Resolutions

### Finding 1 — RESOLVED: Density Matrix Formula (§5, line 464)
- **Status:** CLOSED (v92)
- **Action:** Updated manuscript to correct formula: $\rho_\mu = \mu|\Phi^-\rangle\langle\Phi^-| + (1-\mu)/2 \cdot (|HV\rangle\langle HV| + |VH\rangle\langle VH|)$.
- **Verification:** All 9 correlators and Gen LF 1 violation match the physical model to machine precision.

### Finding 2 — RESOLVED: FOM vs θ Sweep (§4.1)
- **Status:** CLOSED (v93)
- **Action:** Updated manuscript Section 4.1 to reflect the per-theta re-optimization FOM values: 5.8 (20°), 8.6 (31°), 8.8 (35°), 6.0 (45°), 0 (58°), 0 (90°).
- **Verification:** Grid search sweep verified using `RCA_fom_beta03.py`.

### Finding 3 — RESOLVED: All Core Physics Verified
- **Status:** CLOSED
- **Verification:** All numbers (Gen LF 1, overlaps, $\beta_{min}$ thresholds, S2 correlator values) are verified to fourth-decimal precision.

### Finding 4 — RESOLVED: Numerical θ Sweep Framing
- **Status:** CLOSED (v94)
- **Action:** Downgraded the exact proportionality "$\delta\langle AB\rangle \propto \cos\theta$" to numerical theta-dependence ("vanishing identically at $\theta = \pi/2$, determined numerically otherwise") to avoid over-characterization.

---

## Verification Scripts

| Script | Purpose |
|--------|---------|
| [RCA_manuscript_verification.py](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/papers/paper_002/supplemental/RCA_manuscript_verification.py) | Main verification script |
| [RCA_fom_beta03.py](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/papers/paper_002/supplemental/RCA_fom_beta03.py) | Verification of the re-optimized FOM values at $\beta = 0.30$ |
| [RCA_full_verification_v93.py](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/papers/paper_002/supplemental/RCA_full_verification_v93.py) | Comprehensive first-principles physics verification |

---

## Recommended Actions Status
1. **Fix density matrix formula:** [x] Done (v92)
2. **Clarify FOM definition:** [x] Done (v92/v93)
3. **Add "leading order" / numerical qualification:** [x] Done (v92/v94)
4. **Verify FOM sweep results:** [x] Done (v93/v94)
