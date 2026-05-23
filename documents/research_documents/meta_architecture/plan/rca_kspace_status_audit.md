# RCA Audit: K-Space Honest Status Assessment

**Date:** 2026-05-23
**Method:** 3-Round RCA × 5-Why × Scoring Threshold 4/5
**Compass:** VVV-QMRF-EX

---

## User's Audit Table (Input)

| Item | Status |
|---|---|
| K-space axioms được viết ra | ✅ |
| K-space connected với EWF conceptually | ✅ một phần |
| K-space có equation cho probability | ❌ |
| K-space có numerical prediction | ❌ |
| K-space được compare với Proietti data | ❌ |
| K-space "fit" EWF theo bất kỳ nghĩa nào | ❌ |

---

## Round 1: Code-Level Evidence Trace

### W1: K-space có equation cho probability ❌ — CORRECT or WRONG?

**K9_E formula EXISTS** (Phase 8, k9e_predictor.py line 8):
```
P(o | k_i, Exp) = Tr(E_o ρ_i) · [1 − β · f_perp(o, k_i, K_ctx)] / Z_E
```

**But WHERE does this formula come from?**

| Component | Source | Derived from K1-K8? |
|---|---|---|
| `Tr(E_o ρ_i)` | Standard QM Born rule | ❌ External (QM) |
| `β` | Free parameter | ❌ Postulated |
| `f_perp` | Counting compatible outcomes | ⚠️ Uses K_ctx (from K8/T3), but the FRACTION form is an ansatz |
| `Z_E` | Normalization | ❌ Construction (ensures Σ P = 1) |

**The formula is an ANSATZ, not a THEOREM.** K1-K8 define structural space. K9_E is SEPARATELY proposed as a probability rule. The K-axioms alone produce ZERO probabilities.

**Verdict: ❌ CONFIRMED** — K-space (K1-K8) does NOT have an equation for probability. K9_E is a proposed modification of QM's Born rule that uses K-space concepts but is not derived from them.

### W2: K-space có numerical prediction ❌ — trace code

**k9e_predictor.py line 269:**
```python
delta = beta**2 * qm_e / (n_ctx**2)  # second-order, small
```

This is NOT the K9_E formula. The comment says "second-order, small" — it's a **hand-wave approximation**. The actual K9_E formula (lines 121-173) computes per-outcome probabilities correctly, but the CHSH-level function `k9e_expectation()` (lines 180-271) DOES NOT USE IT. Instead, it uses the ad-hoc `delta = β²·E/n²`.

**d1_blk1_4point_fit.py uses a DIFFERENT model** (lines 89-107):
```python
def k9e_expectation(E_qm, beta, setting_x):
    g_eff = 0.146  # HARDCODED constant
    if setting_x == 0:
        return E_qm
    else:
        return E_qm * (1 - beta * g_eff)
```

This is `E_K9E = E_QM · (1 − β · 0.146)`. Where does `g_eff = 0.146` come from?
→ Comment says "from PP-4 sanity check calibration" → but tracing back, this is just `f_perp ≈ 0.146` estimated from the EWF scenario.

**There are TWO DIFFERENT models in the codebase:**
1. `k9e_predictor.py`: δ = β²·E/n² (second-order, tiny)
2. `d1_blk1_4point_fit.py`: δ = β·0.146·E (first-order, larger)

These give DIFFERENT predictions. Which one IS K9_E?

**Verdict: ❌ CONFIRMED** — No consistent numerical prediction. Two code files use different formulas. Neither is rigorously derived from K9_E's actual definition.

### W3: K-space được compare với Proietti data ❌ — trace code

**d1_blk1_4point_fit.py Section 1** (lines 42-56):
```python
# Reconstruction method:
# Key insight: Proietti's experiment has a UNIFORM visibility
# degradation across all settings. The visibility V_exp ≈ S_exp/S_QM
# applies equally to all ⟨A_xB_y⟩ because:
#   (1) Same source for all settings
#   (2) Same detectors for all settings
#   (3) Figure 3 shows each sub-figure with similar error bars
#
# Therefore: ⟨A_xB_y⟩_exp ≈ V_exp · ⟨A_xB_y⟩_QM
```

**CRITICAL:** The "experimental data" used in the fit is NOT extracted from Proietti Figure 3. It is RECONSTRUCTED by multiplying QM predictions by a uniform visibility factor V_exp = S_exp/S_QM = 0.854.

This means:
```
E_exp[key] = V_exp * E_QM[key]    # line 63
```

Then the K9_E model predicts:
```
E_K9E[key] = V_exp * E_QM[key] * (1 - beta * g_eff)    # lines 150-152
```

The chi² fit minimizes:
```
χ² = Σ [(V·E_QM - V·E_QM·(1-β·g))² / σ²]
   = Σ [(V·E_QM·β·g)² / σ²]
```

**This is GUARANTEED to give β = 0** because the "data" IS the QM prediction multiplied by visibility. There is NO independent data to fit against. The fit is CIRCULAR.

**Verdict: ❌ CONFIRMED** — The comparison is circular. "Data" = V · QM. K9_E = V · QM · (1−βg). Fit trivially yields β=0.

### W4: K-space "fit" EWF ❌ — what would real fit mean?

A real fit would require:
1. **Raw Proietti Figure 3 data** (individual ⟨A_xB_y⟩ with error bars, NOT reconstructed)
2. **Setting-dependent visibility** (V might differ per setting — this is the K9_E signature)
3. **Independent model comparison** (QM+noise vs K9_E model)

None of these exist in the current codebase.

**Verdict: ❌ CONFIRMED.**

**R1 Score: 5.0/5** — All ❌ verified with code evidence.

---

## Round 2: Why did we claim ✅ COMPLETE for 6 phases?

### W1: What did Phase 7-13 actually accomplish?

| Phase | Claim | Reality |
|---|---|---|
| **7** | 7/7 constraints pass | ✅ REAL — constraint checks (normalization, non-negativity, Born limit) are mathematically valid for the K9_E formula |
| **8** | Equation documented | ⚠️ ANSATZ documented, not DERIVED. "0 orphaned assumptions" is true within its own frame but doesn't make it a derivation |
| **9** | Adversarial tests pass | ⚠️ Tests check INTERNAL consistency of the ansatz, not its connection to K1-K8 |
| **10** | Data fitting | ❌ CIRCULAR — reconstructed data guarantees β=0 |
| **11** | 3-observer prediction | ❌ Based on ansatz + incorrect amplification (11× retracted, even 2.1× uses ansatz formulas) |
| **12** | Interpretation reduction | ⚠️ Conceptual mapping (Copenhagen/MWI as limits) but doesn't require K9_E |
| **13** | Honest assessment | ⚠️ PARTIALLY honest — flagged β=0 and weaknesses but didn't flag the circular fit or ansatz nature |

### W2: What is the self-deception mechanism?

1. **K9_E formula looks like physics** — it has the right structure (Born rule × correction / normalization)
2. **Constraint checks pass** — because the formula was DESIGNED to pass them
3. **"Data fitting" sounds empirical** — but the "data" is reconstructed from QM
4. **Phase 13 found β=0** — but framed it as "consistent with QM" instead of "our fit was circular"
5. **Root cause: Framework-as-theory confusion** — K-space is a FRAMEWORK (structural axioms). K9_E is a HYPOTHESIS within that framework. Phase 7-13 treated the hypothesis as if it were a derived consequence.

### W3: What is GENUINELY accomplished?

| Item | Status | Evidence |
|---|---|---|
| K1-K8 axioms well-defined | ✅ | 8 axioms with formal statements, 31 fixes applied |
| ⊥_K derivable from EWF via T3 | ✅ | Structural theorem, not dependent on K9_E |
| K9_E internally consistent | ✅ | Normalization, non-negativity, Born limit verified |
| K9_E matches data | ❌ | β=0 from circular fit |
| K9_E predicts anything new | ❌ | All predictions at β=0 = QM exactly |
| K-space adds physical content | ⚠️ | V-status (Bhrānti) is conceptually new but has no measurable consequence |

**R2 Score: 5.0/5** — Mechanism of self-deception identified.

---

## Round 3: Corrected Status Table + Actions

### Corrected Status Table

| Item | Old Status | Corrected Status | Evidence |
|---|---|---|---|
| K-space axioms được viết ra | ✅ | ✅ | K1-K8 in K_Space_Axiomatization.md, Layer 1 frozen |
| K-space connected với EWF conceptually | ✅ phần | ✅ phần | T3 derives ⊥_K from EWF + AJVS; but AJVS itself is semantic commitment |
| K-space có equation cho probability | ❌ | ❌ | K9_E is ANSATZ, not derived from K1-K8. Two inconsistent implementations in code |
| K-space có numerical prediction | ❌ | ❌ | Predictions exist ON PAPER but from ansatz + inconsistent code |
| K-space được compare với Proietti data | ❌ | ❌ | "Data" was reconstructed (V·QM), not extracted. Fit circular |
| K-space "fit" EWF theo bất kỳ nghĩa nào | ❌ | ❌ | β=0 from circular fit. No independent evidence |

### What needs to happen for each ❌ to become ✅?

| Item | Required Action | Difficulty |
|---|---|---|
| **Equation** | Either: (A) DERIVE a probability rule from K1-K8 axiomatically, or (B) honestly label K9_E as a HYPOTHESIS/POSTULATE (not a consequence of K-space) | (A) HARD, (B) EASY but changes the paper's claim |
| **Numerical prediction** | Fix code inconsistency (one K9_E implementation). Compute predictions CORRECTLY from the formula | MEDIUM |
| **Compare with data** | Extract REAL Proietti Figure 3 values (visual reading from PDF) OR use different experimental data | MEDIUM |
| **"Fit" EWF** | Requires non-circular comparison with genuine data. May require new experimental data | HARD |

### Recommended path

Option (B) is the honest path: **K9_E is a HYPOTHESIS, not a derivation.**

This means:
- K-space (K1-K8) = structural framework ✅
- K9_E = proposed probability rule that USES K-space concepts ⚠️ HYPOTHESIS
- The paper should present K9_E as "a natural hypothesis suggested by the K-space structure" not "a consequence of K-space axioms"
- All numerical predictions should be labeled as "conditional on K9_E hypothesis"
- The circular fit should be acknowledged and the ❌ status preserved until real data comparison is done

**R3 Score: 5.0/5** — Path forward is clear.

---

## RCA Decision

```
╔═══════════════════════════════════════════════════════════════╗
║  RCA VERDICT: K-SPACE STATUS AUDIT                           ║
║                                                               ║
║  User's assessment: CONFIRMED (4 out of 4 ❌ verified)       ║
║                                                               ║
║  Root causes:                                                 ║
║    1. K9_E is ANSATZ, not DERIVATION from K1-K8              ║
║    2. Proietti "data" was reconstructed (V·QM), not real     ║
║    3. Two inconsistent K9_E implementations in code          ║
║    4. Phase 10 fit was CIRCULAR (guaranteed β=0)             ║
║                                                               ║
║  Corrective actions:                                          ║
║    (a) Relabel K9_E as HYPOTHESIS in all documents           ║
║    (b) Fix code inconsistency (k9e_predictor vs d1_blk1)    ║
║    (c) Flag circular fit in Phase 10 document                ║
║    (d) Update CHANGELOG, PP0, Phase 13 with corrected status ║
║                                                               ║
║  All 3 rounds = 5.0/5. Decision LOCKED.                     ║
╚═══════════════════════════════════════════════════════════════╝
```
