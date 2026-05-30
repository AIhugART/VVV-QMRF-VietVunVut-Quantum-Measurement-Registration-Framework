Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — NORM-1: Standardize to Conv 2 (Derivation-Chain Canonical Form)

**Date:** 2026-05-30
**Scope:** VVV-QMRF (core). **VVV-QMRF-EX:** compass only.
**Method:** RULE ZERO — 3-round RCA × 5-Why × threshold 4/5.
**Precursor:** `RCA_F_IDX_fperp_notation_2026_05_30.md` (Option B — reconciliation note). This RCA re-opens with explicit scope: standardize to ONE canonical convention.
**Decision needed:** Is full standardization to Conv 2 warranted? If yes, which files change?

---

## 0. TL;DR

| | |
|---|---|
| **Decision** | **Standardize to Conv 2** — derivation-chain form is canonical. |
| **Aggregate score** | **4.33/5** ✅ (R1 4.3 / R2 4.5 / R3 4.2) |
| **Changes** | 4 surgical changes: `index.md §3`, `Definitions §3.4`, `Falsification_Hierarchy §2.5 L112`, `k9e_predictor.py` (rename only, math unchanged). |
| **No change** | `K_Space_Axiomatization.md` (both), `K9S7_final_lock.md`, `K_to_p_bridge_law.md`, `draft_v12.md` — already Conv 2. |
| **Extended scope** | `CLAUDE.md` — user decision (separate governance action). |

**Conv 2 canonical definition:**
```
P(o | K) = Tr(E_o rho) * [1 - beta * f_perp(o, K_ctx)] / Z_E
f_perp(o, K_ctx) = E[I(K5_prospective fires)]   [T8 structural derivation]
                 = |{k_j in K_ctx : k_j bot_K and outcome-inconsistent with o}| / |K_ctx|
K_ctx = contextual K-state set  [T9, from K1-K8 + T1]
```

---

## 1. Convention Inventory (pre-RCA)

| File | Convention | Notes |
|------|-----------|-------|
| `K_Space_Axiomatization.md` (canonical + Class C) | **Conv 2** | T8: `f_perp = E[I(K5_prospective fires)]` = fraction |
| `K9S7_final_lock.md` (LOCKED v1.0) | **Conv 2** | `[1 - beta * f_perp(o, k_i, K_ctx)]` |
| `K_to_p_bridge_law.md` (canonical, 4.8/5 RCA) | **Conv 2** | `f_perp` = fraction of bot_K-inconsistent K_ctx |
| `draft_v12.md` (paper) | **Conv 2** | `f_perp(b,d) = 1 - |<b|d>|^2` (Level 0 projection) |
| `Phase8_candidate_equation.md` | **Conv 2** | LOCKED |
| `index.md §3` | **Conv 1** | `f_perp(K_ctx) = 1 - beta * K_ctx` (whole factor) |
| `VVV_QMRF_Definitions.md §3.4` | **Conv 1** + note | whole factor + dual-convention reconciliation note |
| `Falsification_Hierarchy §2.5` | **MIXED** | L70: Conv 2 (`1 - beta * f_perp(b,d)`); L112: Conv 1 (`P = Tr * f_perp(K_ctx)`) |
| `k9e_predictor.py` | **Conv 1** | `k9e_f_perp()` returns whole factor `1 - beta * K_ctx` |

**Key observation:** Every formal, canonical, locked document uses Conv 2. Conv 1 appears only in overview docs and code, as an undesignated operational shorthand.

---

## 2. Round 1 — Is standardization structurally necessary? — **4.3/5**

**5-Why:**

1. Why is Option B (reconciliation note) insufficient long-term?
   → "Two equivalent conventions coexist" does not prescribe one canonical form. New files and new AI sessions continue propagating both.

2. Why does continued dual convention create real risk?
   → External reader hazard: `draft_v12.md` uses `f_perp(b,d)` = fraction (values 0–1). `index.md` uses `f_perp(K_ctx)` = whole factor (equals 1 at beta=0). Same symbol, different objects — paper reviewer sees apparent contradiction.

3. Why is this external-facing?
   → Paper is the primary public output. Its `f_perp` (Conv 2) will be checked against framework docs by reviewers. No reconciliation note exists in the paper itself.

4. Why does `Falsification_Hierarchy §2.5` internal inconsistency compound this?
   → L70 uses Conv 2 (`1 - beta * f_perp(b,d)`); L112 uses Conv 1 (`P = Tr * f_perp(K_ctx)`) — SAME SECTION, two meanings of `f_perp`.

5. Root cause?
   → Conv 1 emerged from `k9e_predictor.py` implementation (one function returning the whole factor). Never formally designated as canonical. Propagated into docs by inertia.

**Verdict R1:** Standardization is warranted. External reader hazard and internal inconsistency are structural issues.
*Deduction −0.7: Option B reduced severity; remaining risk is real but not currently blocking.*

---

## 3. Round 2 — Which convention is canonical? — **4.5/5**

**5-Why:**

1. Which document has highest structural authority?
   → `K_Space_Axiomatization.md` (formal axiom doc, Layer 1+2 source of truth) = Conv 2. T8 defines `f_perp` as `E[I(K5_prospective fires)]` = a DERIVED structural object.

2. What does the LOCKED definition say?
   → `K9S7_final_lock.md` LOCKED v1.0: `[1 - beta * f_perp(o, k_i, K_ctx)]` with `f_perp` = fraction. Cannot change without unlocking and re-RCA-ing.

3. What does the paper use?
   → `draft_v12.md`: `f_perp(b,d) = 1 - |<b|d>|^2` = Level 0 projection of Conv 2 fraction. Standardizing to Conv 1 would require changing the paper — unacceptable.

4. What structural advantage does Conv 2 have?
   → Conv 2 preserves epistemic clarity:
   - `f_perp` = **DERIVED** from K5_prospective + T8 (structural theorem, Class C)
   - `beta` = **FREE PARAMETER** (measurement target)
   - `[1 - beta * f_perp]` = **POSTULATED combination** (K9_E)
   Conv 1 conflates all three into `f_perp(K_ctx)`, hiding that T8 derives the fraction and beta is separate.

5. What is the only argument for Conv 1?
   → Code convenience: one function returns the whole factor. Cosmetic shorthand, not a structural reason. Rename to `k9e_suppression_factor` eliminates this.

**Verdict R2:** Conv 2 is canonical. LOCKED definition, formal axiom doc, and paper all use it. Conv 1 is undesignated operational shorthand.
*Deduction −0.5: code rename step requires care.*

---

## 4. Round 3 — Blast radius and implementation risk — **4.2/5**

### Change table

| ID | File | Risk | Action |
|----|------|------|--------|
| C1 | `index.md §3` formula block + note | LOW | Rewrite formula to Conv 2; update note to "canonical form" |
| C2 | `Definitions §3.4` formula + note | LOW | Replace dual-convention note with canonical statement |
| C3 | `Falsification_Hierarchy §2.5 L112` | LOW | Fix `f_perp(K_ctx)` → `[1-beta*f_perp(K_ctx)]/Z` |
| C4 | `k9e_predictor.py` | LOW-MEDIUM | Rename `k9e_f_perp` → `k9e_suppression_factor`; update `k9e_correlator` call; math UNCHANGED |
| — | `K_Space_Axiomatization.md` (both) | — | Already Conv 2 — PEER-SYNC NOT triggered |
| — | `K9S7`, `K_to_p_bridge_law`, `Phase8`, paper | — | Already Conv 2 — no change |
| EXTENDED | `CLAUDE.md` Layer 3 | — | Uses Conv 1 — user decision pending |

**5-Why adversarial:**

1. Does code rename break external callers?
   → No. `k9e_f_perp` only called by `k9e_correlator` in the same file. No external API. SAFE.

2. Does changing `index.md` contradict any other overview doc?
   → No — aligns it with `K_Space_Axiomatization.md`, `K9S7`, `K_to_p_bridge_law.md`. Alignment IMPROVED.

3. Does `Falsification_Hierarchy L112` fix affect any theorem?
   → L112 is a descriptive table entry, not a theorem. Fix adds `/Z` (normalization), corrects `f_perp` role. No theorem modified.

4. Does PEER-SYNC trigger?
   → PEER-SYNC applies to `K_Space_Axiomatization.md` only. Both copies already Conv 2 — NOT triggered.

5. What is the residual risk?
   → `CLAUDE.md` remains Conv 1. Future AI sessions see Conv 2 in all framework docs but Conv 1 in CLAUDE.md instructions. This is the strongest residual risk. Reason for flagging as extended scope.

**Verdict R3:** Blast radius surgical and manageable. Most important docs unchanged. CLAUDE.md deferred.
*Deduction −0.8: CLAUDE.md residual; code needs sanity-check post-rename.*

---

## 5. Scoring Ledger

| Round | Focus | Score |
|-------|-------|-------|
| R1 | Standardization necessity | 4.3 |
| R2 | Conv 2 as canonical | 4.5 |
| R3 | Blast radius + risk | 4.2 |
| **Aggregate** | | **4.33/5** ✅ (threshold 4.0) |

---

## 6. Implementation Record

Changes applied 2026-05-30:

- [x] C1: `index.md §3` — formula rewritten to Conv 2; notation note → canonical statement
- [x] C2: `Definitions §3.4` — formula rewritten to Conv 2; dual-convention note → canonical statement
- [x] C3: `Falsification_Hierarchy §2.5 L112` — `f_perp(K_ctx)` → `[1-beta*f_perp(K_ctx)]/Z`
- [x] C4: `k9e_predictor.py` — `k9e_f_perp` renamed `k9e_suppression_factor`; math UNCHANGED
- [ ] EXTENDED: `CLAUDE.md` Layer 3 — user decision pending

---

## 7. EX Compass Note

`EX_NODE_K5_CTX` (KE-SC 4.0) flags `f_perp / bot_K / K_ctx` as the top stress node in VVV-QMRF-EX. This standardization reduces that stress by making Conv 2 the explicit canonical form across all docs.

EX used as compass only — no EX structure imported into core.

---

*RCA NORM-1 — 2026-05-30. Decision: Conv 2 canonical. Score 4.33/5. 4 changes applied. CLAUDE.md deferred (user decision).*
