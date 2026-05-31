Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Phase 0 — RCA Verdict for C2 & C3 (paper_002 Update Plan v2.0)

**Date:** 2026-05-30
**Scope:** VVV-QMRF (core). **VVV-QMRF-EX:** compass only (no structure import).
**Method:** RULE ZERO — 3-round RCA × 5-Why × scoring threshold 4/5.
**Gate role:** Phase 0 of `paper_plan_v2.0_RCA_update.md`. Determines whether the manuscript-update scope stays "update" (paper bundle only) or expands into the frozen K9_E framework.
**Inputs traced (canonical sources):**
- `02_derivation_chain/Phase8_candidate_equation.md` (K9_E canonical equation + term table + T8/T9)
- `K_to_p_bridge_law.md` (single-entry bridge law, RCA 4.8/5)
- `SOT/paper_002_SOT.md` §1, §2.4, §15 (paper-side f_perp + deliberate vocabulary decoupling)
- `manuscript.md` §2.3, §3 (paper-side f_perp + Proposition 1)
- `index.md` §3 (the abbreviated form that triggered the C2 question)
- EX compass: `05_ex_compass/ex_compass_index.md` (EX_NODE_K5_CTX, KE-SC 4.0)

---

## 0. TL;DR / Kết luận nhanh

| Item | Verdict | Aggregate score | Gate effect |
|------|---------|-----------------|-------------|
| **C2** — `f_perp` dual meaning | **INTENDED BRIDGE (structure-preserving), NOT a category error** | **4.53/5** ✅ | Scope stays "update". **PROCEED** to Phase 1. |
| **C3** — paper honest-status note | **KEEP DECOUPLED** (no new disclaimer sentence; verify existing framing intact) | **4.43/5** ✅ | No framework re-coupling. |
| **F-IDX** (spun-off finding) | ~~`index.md §3` notation imprecise~~ → **reclassified** as *undocumented equivalent dual convention* (no wrong numbers). **RESOLVED 2026-05-30 (4.50/5, Option B)** — reconciliation note added to `VVV_QMRF_Definitions.md §3.4` + `index.md §3` (extend-only); code/CLAUDE.md untouched. | — | Framework-side; handled. See `04_governance/RCA_F_IDX_fperp_notation_2026_05_30.md`. |

**VN:** Hai `f_perp` KHÔNG phải lỗi phạm trù. Bài báo dùng `f_perp(b,d)=1−|⟨b|d⟩|²` chính là **bản hiện thực N=2 (Born) của `f_perp` khung** = `E[I(K5 fires)]` (T8). Cái làm nó *trông như* mâu thuẫn là **cách viết tắt trong `index.md §3`**, không phải bản canonical. → Giữ nguyên phạm vi "update", tiếp tục Phase 1.

---

## 1. C2 — Are the two `f_perp` the same object?

### 1.0 Define (symptom vs cause)

- **Symptom (as stated in plan v2.0):** framework `f_perp(K_ctx)=1−β·K_ctx` (geometry-free incommensurability) vs paper `f_perp(b,d)=1−|⟨b|d⟩|²` (geometric overlap) look like two different objects sharing one name.
- **Suspected cause (to test):** category error (same name, different meaning) — which would force a framework-level fix and blow the "update" scope.

### 1.1 Round 1 — Source-trace (Define + Trace, 5-Why) — **4.5/5**

The canonical K9_E equation is NOT the index abbreviation. `Phase8_candidate_equation.md` L21-25 and `K_to_p_bridge_law.md` §1:

```
P(o | k_i, Exp) = Tr(E_o ρ_i) · [1 − β · f_perp(o, k_i, K_ctx)] / Z_E(k_i)
```

with (Phase8 term table, T3): **`f_perp` = fraction of contextual observers whose registered outcomes are ⊥_K-incompatible with `o`** — i.e. `f_perp` is the *multiplicand of β*, NOT the whole factor.

**5-Why chain:**
1. Why do the two `f_perp` look different? — Plan took the framework side from `index.md §3` (`f_perp(K_ctx)=1−β·K_ctx`).
2. Why does that read differently? — `index.md §3` folded the **entire** suppression factor `(1−β·K_ctx)` into the symbol `f_perp`, as an overview shorthand.
3. Why is that misleading? — The canonical form (Phase8, bridge-law, `K9S7_final_lock.md`) keeps `f_perp` as the **fraction inside** `[1−β·f_perp]`. The index symbol-name collides with the canonical symbol-name at a different slot.
4. Why does the canonical fraction connect to the paper? — T8 ([A-E2a], Phase8 L50): `f_perp = E[I(K5_prospective fires)]` — a statistical identity over binary K5/K6 primitives.
5. Why does that equal `1−|⟨b|d⟩|²`? — For **N=2** (one Friend record `d`, one Superobserver outcome `b`), the "fraction over other observers" collapses to a single binary indicator, whose expectation by the Born rule is `P(b ⊥ d) = 1−|⟨b|d⟩|²`.

**Isolated root cause of the apparent mismatch:** `index.md §3` notational abbreviation — **not** a substantive divergence. *Deduction (−0.5): the index defect is real and must be logged (F-IDX).*

### 1.2 Round 2 — Bridge structure-preservation test (Isolate) — **4.5/5**

**Claim under test:** paper `f_perp(b,d)=1−|⟨b|d⟩|²` is the N=2 Born instantiation of framework `f_perp = E[I(⊥_K fires)]`.

| Framework primitive (canonical) | Paper instantiation | Preserved? |
|---|---|---|
| `f_perp(o,K_ctx)` = ⊥_K-incompatibility fraction (T3) | `f_perp(b,d)` per contextual pair (b=o, d=Friend record) | ✅ same slot, same β-multiplicand |
| T8: fraction = `E[I(K5_prospective fires)]` | `1−|⟨b|d⟩|²` = Born `P(b ⊥ d)` = expectation of the single ⊥_K indicator | ✅ N=2 collapse of T8 |
| Distinguishability Condition (III): δP≠0 iff `∃ o,o': f_perp(o)≠f_perp(o')` (PP-2 v2 cancellation) | Proposition 1: δ⟨AB⟩=0 iff all `f_perp(b,d)=1/2` (θ=π/2) → constant → cancels in Z | ✅ Proposition 1 **is** Condition (III) geometric instantiation |
| Born limit (ii)/(iv): K_ctx=∅ (N=1) → P=P_QM | Single-observer / no Friend record → δ=0 | ✅ |
| Scope: K9_E needs only **T1 (N=2 constructive)** (SOT §2.2) | Paper declares N=2 throughout | ✅ in-scope |

The equatorial cancellation theorem (paper §3) and the framework PP-2 v2 cancellation insight (Phase8 L110) are the **same theorem** under two vocabularies. Structure-preservation holds. *Deduction (−0.5): bridge is rigorous only at N=2; N≥3 generalization needs T4-H (explicitly future work in both paper §8.2 and SOT §11.2) — not a defect, but the bridge's validity boundary must be stated.*

### 1.3 Round 3 — Category-error adversarial test (try to break it) — **4.6/5**

| Attack | Resolution | Survives? |
|--------|-----------|-----------|
| (a) Binary `C` (framework) vs continuous overlap (paper) | Continuous = Born **expectation** of the binary indicator (T8 `E[I]`). BSM = binary special case (Phase8 L122-129); projective tilt = continuous case. Same ⊥_K object. | ✅ no category error |
| (b) "fraction over observers" vs "per-pair overlap" | For N=2 the fraction over the single other observer **is** that pair's incommensurability expectation. Diverges only at N≥3 (out of scope). | ✅ |
| (c) o-indexing mismatch | Framework `f_perp(o,…)` is outcome-indexed; paper `f_perp(b,d)` with b=Superobserver outcome o. Same indexing. | ✅ |
| (d) "geometric" (paper) vs "registration/⊥_K" (framework) = different physics? | Geometric overlap `|⟨b|d⟩|²` **is** the Born measure of how incommensurable the Superobserver basis is with the Friend record. Same quantity, two vocabularies. SOT §15 documents the deliberate substitution ("framework of measurement registration", K9_E name removed) to keep the arXiv paper framework-neutral. | ✅ vocabulary, not category |

**Residual found:** the *only* genuine defect is F-IDX (index notation), a **framework-doc** issue — the paper is correctly aligned to the **canonical** form. *Deduction (−0.4): F-IDX leaves a live inconsistency in the framework that could re-trigger this same false alarm later.*

### 1.4 C2 aggregate & verdict

**(4.5 + 4.5 + 4.6) / 3 = 4.53/5 ≥ 4.0 → PASS.**

> **VERDICT C2: INTENDED, STRUCTURE-PRESERVING BRIDGE — NOT a category error.**
> Paper `f_perp(b,d)=1−|⟨b|d⟩|²` = the N=2 Born instantiation of framework `f_perp=E[I(⊥_K fires)]` (T8). Validity boundary: N=2 (T1); N≥3 deferred to T4-H. **Exit gate: PROCEED — scope stays "update" (paper bundle), no framework change required for the paper.**

**EX compass bearing (not import):** `EX_NODE_K5_CTX` is the top stress point (KE-SC 4.0, "K5 firing is the mechanism for distinguishability"). The bridge sits exactly on this node — confirming that notational precision around `f_perp/⊥_K/K_ctx` is load-bearing, and that F-IDX deserves a framework-side fix even though it is outside paper_002 scope.

---

## 2. C3 — Does the arXiv manuscript need an honest-status note?

### 2.1 Round 1 — Is honest framing already present? (Define/source) — **4.5/5**

Already present in substance:
- Manuscript §1: "This paper makes no claim about the existence of overlap-dependent deformation in nature — it proposes a null-test protocol".
- β framed as a **search parameter** (SME analogy), **no value measured** (Proietti β=0.598 deliberately removed — SOT §15 last row).
- Phase 1 = loophole-open **screening** test; Class C empirical status mirrored by bridge-law card ("Experiment NOT YET PERFORMED — proposal only").

### 2.2 Round 2 — Risk of adding a "Class C / VVV-QMRF" disclaimer — **4.4/5**

- SOT §15 + index §1 motivation chain: Project C is **logically independent**; VVV-QMRF/K9_E language was **deliberately removed** to (i) keep the physics standalone and (ii) reduce reviewer attack surface.
- Re-adding a framework disclaimer would **re-couple** the paper and invite category-confusion attacks ("physics or philosophy?").
- CLAUDE.md neutral-boundary-language rule discourages defensive caveats / re-framing standard QM as deficient.

### 2.3 Round 3 — What is actually required? — **4.4/5**

The framework `DISCLAIMER.md` serves the **framework repo**; the paper's analog is its existing honest scientific framing (null test; no β measured; fair-sampling Phase 1). Requirement reduces to **verify framing intact and not overclaimed** — it is.

### 2.4 C3 aggregate & verdict

**(4.5 + 4.4 + 4.4) / 3 = 4.43/5 ≥ 4.0 → PASS.**

> **VERDICT C3: KEEP DECOUPLED.** No new disclaimer sentence. Downstream phases only **verify** the honest framing is intact (no new prose). β stays a bare search parameter (EX_NODE_K9_BETA KE-SC 3.7 supports this).

---

## 3. Consequences for Update Plan v2.0

1. **Gate cleared — PROCEED to Phase 1.** No framework (K9_E) change is required to update the paper; scope confirmed as "paper bundle only".
2. **Plan correction:** the plan's C2 description quoted the framework side as `f_perp(K_ctx)=1−β·K_ctx` (the index abbreviation). Corrected understanding: canonical form is `[1−β·f_perp(o,K_ctx)]`, `f_perp` = ⊥_K fraction = `E[I(K5 fires)]`. Fold this into the plan's C2 row (status: RESOLVED).
3. **New spun-off finding F-IDX (framework-side, out of paper scope):** `index.md §3` should write the canonical `P(o|K)=Tr(E_oρ)·[1−β·f_perp(o,K_ctx)]/Z_E` with `f_perp` = ⊥_K-incompatibility fraction, instead of `f_perp(K_ctx)=1−β·K_ctx`. Recommend a separate framework-doc fix (PEER-SYNC-aware); **do not** bundle into the paper_002 update.
4. **C3 → Phase 4 checklist item:** add "verify honest framing intact (no β measured; null-test; Phase 1 screening)" rather than any edit.

---

## 4. Scoring ledger

| Round | C2 | C3 |
|-------|----|----|
| R1 | 4.5 | 4.5 |
| R2 | 4.5 | 4.4 |
| R3 | 4.6 | 4.4 |
| **Aggregate** | **4.53** ✅ | **4.43** ✅ |
| Threshold | 4.0 | 4.0 |

---

*Phase 0 verdict — 2026-05-30. C2: intended bridge (4.53/5). C3: keep decoupled (4.43/5). Gate: PROCEED. Spun-off F-IDX logged for framework-side correction (outside paper_002 scope). EX used as compass only.*
