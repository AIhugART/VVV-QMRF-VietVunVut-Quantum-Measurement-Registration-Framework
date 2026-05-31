# Day 7 — r/SciencePreprints / r/QuantumPhysics
**Date:** 2026-06-04
**Topic:** K9-S12 experimental proposal — single waveplate at 31°
**DOI:** https://doi.org/10.5281/zenodo.20431310

---

## TITLE
**A single waveplate at 31° could falsify (or confirm) a new quantum measurement postulate — here's the proposed test.**

---

## BODY

Most proposed modifications to quantum mechanics require exotic setups. The K9-S12 proposal is deliberately minimal: take the Bong et al. (2020) photonic Extended Wigner's Friend (EWF) setup, add a **single quarter-wave plate at angle α = 31°**, and measure one extra correlator.

The testable postulate is **K9_E** — a probability rule that recovers the Born rule exactly in single-observer settings but predicts a small suppression in multi-observer EWF configurations:

```
P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o)] / Z
```

At α = 31°, K9_E predicts:
- **Genuine LF 1 = +0.0891** (8.6σ above the local-friendliness threshold)
- **δ⟨A₁B₂⟩ = −0.0355** (20.8σ deviation from standard QM)
- **Figure of Merit = 8.6** (well above detection threshold)

The β = 0 case recovers standard QM exactly, so the null hypothesis is built in: if δ⟨A₁B₂⟩ = 0 at 31° across a full angle sweep, K9_E is falsified.

Why 31°? At this angle, the compatibility map C(o_F, o_W) is outcome-dependent — some (Friend-outcome, Wigner-outcome) pairs are compatible, others are K-side incommensurable. This differential suppression is what produces an observable signal.

**Empirical status before this experiment:** A fit to Proietti et al. (2019) yields 2.31σ improvement over standard QM, but noise sensitivity analysis FAIL (noise at any magnitude produces equivalent signal in ~50% of realizations). The K9-S12 experiment is the first purpose-designed test.

A companion experimental design paper was submitted to arXiv on 2026-05-27 (arXiv ID pending confirmation).

If you work in photonic EWF experiments — or know groups who do — I'd love to connect.

---

📄 Working Paper v3.0 (§8): https://doi.org/10.5281/zenodo.20431310
📄 Experimental paper (arXiv preprint, arXiv ID pending): see §8 of working paper for full K9-S12 spec
🔗 Repository: https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework

---
*Word count: ~295*
