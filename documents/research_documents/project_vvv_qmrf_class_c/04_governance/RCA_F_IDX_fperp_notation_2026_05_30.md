Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — F-IDX: Dual `f_perp` / `K_ctx` Notation Convention

**Date:** 2026-05-30
**Scope:** VVV-QMRF (core, framework docs). **VVV-QMRF-EX:** compass only.
**Method:** RULE ZERO — 3-round RCA × 5-Why × threshold 4/5.
**Origin:** Spun off from `papers/paper_002/review/Phase0_RCA_C2_C3_verdict.md` (C2). Phase 0 logged this as "`index.md §3` notation imprecise." This RCA **re-examines and reclassifies** that framing.
**Decision needed:** What is the proportionate, correct fix for the `f_perp` symbol collision across framework docs?

---

## 0. TL;DR / Kết luận nhanh

| | |
|---|---|
| **Reclassification** | NOT "index.md is wrong." It is an **undocumented but mathematically-equivalent dual notation convention**. No number is wrong anywhere. |
| **Decision** | **Option B — add a reconciliation note (extend, not overwrite)** in the terminology-authority file + a one-line pointer in the overview. Do NOT rewrite the established formula; do NOT touch code. |
| **Aggregate score** | **4.50/5** ✅ (R1 4.4 / R2 4.6 / R3 4.5) |
| **Blast radius** | 2 surgical extend-only edits: `06_references/VVV_QMRF_Definitions.md §3.4`, `index.md §3`. No code, no PEER-SYNC file, no CLAUDE.md. |

> **SUPERSEDED (2026-05-30):** Option B above was the initial proportionate fix (same-day, staged). A subsequent full RCA — `RCA_NORM1_standardize_conv2_2026_05_30.md` (score 4.33/5) — applied complete standardization to Conv 2 across all framework docs, `CLAUDE.md`, and `paper_002_SOT.md`. This document remains the historical record of the reclassification and first-stage fix. NORM-1 is the final state.

**VN:** Hai cách viết `f_perp` đều đúng toán học, chỉ là **đặt tên khác nhau** và **chưa có ghi chú đối chiếu**. Sửa đúng mức = **thêm một ghi chú đối chiếu** (extend), KHÔNG viết lại công thức đã được code + Definitions + một RCA cũ dùng.

---

## 1. Define — the two conventions (both established, both correct)

| | Convention 1 (overview / definitions / code) | Convention 2 (derivation chain) |
|---|---|---|
| Formula | `P = Tr(E_oρ)·f_perp(K_ctx)/Z_E` | `P = Tr(E_oρ)·[1−β·f_perp(o,K_ctx)]/Z_E` |
| `f_perp` denotes | the **whole** suppression factor `(1−β·K_ctx)` | the **⊥_K-incompatibility fraction** (β-multiplicand) |
| `K_ctx` denotes | the **scalar** fraction `Σ_{i≠j} I(k_i⊥k_j)/N_pairs` | the **set** of contextual K-states |
| Used in | `index.md` §3+diagram, `VVV_QMRF_Definitions.md §3.4`, `07_fits/utils/k9e_predictor.py` | `02_derivation_chain/Phase8_candidate_equation.md`, `K_to_p_bridge_law.md`, `K9S7_final_lock.md` |

**Mapping (exact relabeling):** `conv1.K_ctx ≡ conv2.f_perp` (both = the fraction); `conv1.f_perp(K_ctx) ≡ conv2.[1−β·f_perp]` (both = the whole factor). The computed probability is identical. There is **no numerical contradiction** — it is purely a symbol-name swap.

---

## 2. Round 1 — Error or dual convention? — **4.4/5**

**5-Why:**
1. Why did C2 look like a category error? — Plan read framework `f_perp` from `index.md §3` (conv 1) and paper `f_perp` (geometric), saw the same name on different objects.
2. Why does `index.md` use conv 1? — It mirrors `VVV_QMRF_Definitions.md §3.4` and `k9e_predictor.py`, which all use conv 1.
3. Is conv 1 wrong? — No. It computes the same `P`. An RCA review (`08_archives/rca_review_index_md.md` L83) already PASSED it as "matches §K9_E and script."
4. Then what is the actual defect? — Conv 1 and conv 2 coexist **without a documented mapping**, so a reader crossing clusters sees `f_perp` mean two things (this caused the C2 false alarm).
5. Root cause? — **Missing reconciliation note between two equivalent conventions** — a clarity/traceability gap, LOW severity, zero wrong numbers.

**Correction to Phase 0 wording:** "index.md imprecise vs canonical" → **"undocumented equivalent dual convention."** Neither cluster is canonical-over-the-other; conv 2 is the *derivation-chain* form, conv 1 is the *operational/coded* form. *Deduction (−0.6): the Phase 0 framing overstated severity and must be corrected in the verdict + plan.*

---

## 3. Round 2 — Which fix preserves correctness + "extend, not overwrite"? — **4.6/5**

| Option | Action | Verdict |
|--------|--------|---------|
| **A** | Rewrite `index.md` + `Definitions` to conv 2 | **REJECT** — desyncs from `k9e_predictor.py` (conv 1) and from the already-passed RCA; high blast radius; overwrites established notation. Violates CLAUDE.md "extend, not overwrite." |
| **C** | Globally standardize all docs+code on one convention | **REJECT (out of bounded scope)** — touches code, multiple docs, EX snapshot; user asked to "handle then stop." Defer as possible future cleanup. |
| **B** | **Add a reconciliation note** (extend-only) in the terminology authority (`Definitions §3.4`) + a one-line pointer in `index.md §3`; restore the missing `/Z_E` in `index.md §3` (Definitions already has it) | **ACCEPT** — fixes the reader hazard at its root (the missing mapping), preserves every existing formula/number/code, minimal footprint. |

*Deduction (−0.4): Option B leaves the dual convention in place (by design); future readers still meet two forms, now bridged by an explicit note rather than unified. Acceptable given scope + extend-not-overwrite.*

---

## 4. Round 3 — Does the note risk contradicting `Falsification_Hierarchy §2.5`? (adversarial / Verify) — **4.5/5**

`Falsification_Hierarchy.md §2.5` L108-112 deliberately separates:
- **❌ Falsified by K9-S12:** `g(|⟨b|d⟩|²)` (the geometric overlap-only, Level 0).
- **✅ Survives:** "f_perp framework … with `f_perp ≠ f(|⟨b|d⟩|²)`" (contextual, Levels 1–3).

The reconciliation note must therefore state precisely: the geometric `1−|⟨b|d⟩|²` is the **N=2 overlap-only (Level 0) Born projection** of the contextual framework `f_perp`, and is **not** a general definitional identity (`f_perp ≠ f(|⟨b|d⟩|²)` in general). With that wording the note is **consistent** with both the Phase 0 C2 bridge verdict AND the Falsification Hierarchy. *Deduction (−0.5): requires careful wording; a sloppy note ("f_perp = 1−|⟨b|d⟩|²") would contradict L112 and re-introduce the very confusion. Note text is fixed below to avoid this.*

**EX compass bearing (not import):** `EX_NODE_K5_CTX` (KE-SC 4.0) flags `f_perp/⊥_K/K_ctx` as the top stress node — reinforcing that a precise, explicit mapping note is worth adding even though the defect is low-severity.

---

## 5. Decision & exact note text

**DECISION: Option B (4.50/5 ≥ 4.0).**

### 5.1 Note for `06_references/VVV_QMRF_Definitions.md §3.4` (after the formula block)

> **Notation note (two equivalent conventions).** Two symbol conventions for K9_E coexist in this repository and compute the *same* probability:
> (1) *operational/coded form* (this file, `index.md`, `k9e_predictor.py`): `f_perp(K_ctx) = 1 − β·K_ctx`, where `K_ctx` is the scalar ⊥_K-incompatibility fraction `Σ_{i≠j} I(k_i⊥k_j)/N_pairs`;
> (2) *derivation-chain form* (`Phase8_candidate_equation.md`, `K_to_p_bridge_law.md`, `K9S7_final_lock.md`): `[1 − β·f_perp(o,K_ctx)]`, where `f_perp` is that same fraction = `E[I(K5_prospective fires)]` (T8) and `K_ctx` is the set of contextual K-states. The two are an exact relabeling. In the N=2 overlap-only (Level 0) projection used by paper_002, the fraction evaluates by the Born rule to `1 − |⟨b|d⟩|²`; this is a projection, **not** a general identity (`f_perp ≠ f(|⟨b|d⟩|²)` in general — see `04_governance/Falsification_Hierarchy.md §2.5`). Full RCA: `04_governance/RCA_F_IDX_fperp_notation_2026_05_30.md`.

### 5.2 Pointer for `index.md §3` (after the K9_E formula block) + restore `/Z_E`

- Restore `/ Z_E` in the §3 formula line (consistency with `Definitions §3.4`, which already has it).
- Add one line: *"Notation: `f_perp(K_ctx)` here is the whole `(1−β·K_ctx)` factor (operational form); the derivation chain writes `[1−β·f_perp]` with `f_perp`=the fraction. Equivalent relabeling — see `06_references/VVV_QMRF_Definitions.md §3.4` and `04_governance/RCA_F_IDX_fperp_notation_2026_05_30.md`."*

### 5.3 Explicitly OUT of scope (do NOT touch now)
- `07_fits/utils/k9e_predictor.py` — conv 1 is correct and tested; changing code is risky and unnecessary.
- `CLAUDE.md` — project instructions; not required for this clarity fix.
- Global standardization (Option C) — deferred.

---

## 6. Scoring ledger

| Round | Focus | Score |
|-------|-------|-------|
| R1 | Error vs dual convention (reclassify) | 4.4 |
| R2 | Fix choice (extend-not-overwrite) | 4.6 |
| R3 | Consistency with Falsification Hierarchy (adversarial) | 4.5 |
| **Aggregate** | | **4.50** ✅ (threshold 4.0) |

---

*RCA F-IDX — 2026-05-30. Decision: Option B (reconciliation note, extend-only). Reclassified from "index error" to "undocumented equivalent dual convention." Two edits applied (Definitions §3.4 + index §3); code and CLAUDE.md untouched. EX used as compass only.*
