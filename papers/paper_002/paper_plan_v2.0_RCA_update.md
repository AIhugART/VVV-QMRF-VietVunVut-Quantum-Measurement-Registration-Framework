Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Paper 002 — RCA Update Plan v2.0

**Type:** RCA-driven update / governance plan (NOT a re-write of the 2026-05-23 writing plan)
**Scope:** `papers/paper_002/manuscript.md` (currently **v94**) + `papers/paper_002/supplemental/`
**Aligned to:** `documents/research_documents/project_vvv_qmrf_class_c/` — **index v36 (2026-05-29)**, Class C (qualified)
**Method:** RULE ZERO — RCA five-step (Define → Trace → Isolate → Fix-cause → Verify), 5-Whys, scoring threshold 4/5
**Date:** 2026-05-30
**Status:** PLAN — execution NOT started. This file is the deliverable; fixes are deferred to a future approved session.

---

## 0. Why this plan exists (one-sentence root cause)

> **The manuscript advanced to v94 through four RCA rounds, but its satellite artifacts — `SOT/paper_002_SOT.md`, `README.md`, `CHANGELOG.md`, and parts of `supplemental/` — were last synchronized at the v21/v25/v88 mileposts. The single root cause is a broken artifact-synchronization discipline; it surfaces as multiple downstream symptoms (stale density matrix, divergent FOM table, un-downgraded `cos θ` language, untraced versions).**

This plan does NOT patch each symptom in isolation (that would violate RULE ZERO step 4). It isolates the desync, fixes it at the source (re-sync from the v94 manuscript + the verified script outputs as the source of truth), and verifies the root cause is gone — not merely the visible mismatch.

---

## 1. Requirements restatement

1. Bring `manuscript.md` and `supplemental/` into **internal consistency** (no number/claim contradicts another within the paper bundle).
2. Bring the bundle into **alignment with the `class_c` framework** at index v36 — headline numbers, classification status, and terminology.
3. Preserve all valid v94 RCA outcomes (**extend, not overwrite**); respect existing freezes (title, §2.3, §3.5).
4. Produce a single auditable plan (this file) recording the RCA chain and the fix order.

---

## 2. Root-Cause Gap Inventory (Define + Trace + Isolate)

### Group A — Satellite desync (artifacts behind manuscript v94)

| # | Symptom | Trace (5-Whys, condensed) | Isolated root cause | Severity |
|---|---------|---------------------------|---------------------|----------|
| **A1** | `SOT §6.1` (line ~289) still states `ρ_μ = μ\|Φ⁻⟩⟨Φ⁻\| + (1−μ)I/4`. Manuscript §5 (line ~472) already uses `ρ_μ = μ\|Φ⁻⟩⟨Φ⁻\| + (1−μ)/2·(\|HV⟩⟨HV\|+\|VH⟩⟨VH\|)`. | Why mismatch? SOT synthesized at v25. → Why not updated? Density-matrix fix (review Finding 1, v91) applied to manuscript only. → Why? No re-sync pass after the fix. | SOT never re-synced after the v91 density-matrix correction. | **BLOCKING** (physics error in SOT: `I/4` gives ⟨A₁B₁⟩ = −0.95, not −1.0000) |
| **A2** | FOM-vs-θ tables **diverge**. Manuscript §4.1: `5.8 (20°) / 8.6 (31°) / 8.8 (35°) / 6.0 (45°) / 0 (58°) / 0 (90°)`, window `θ∈[20°,45°]`. SOT §4.6 & §6.5: `9.6 (20°) / 8.6 (31°) / 7.1 (45°) / 5.0 (58°) / 0 (90°)`, window `θ∈[20°,55°]`. | Why two tables? Manuscript applied per-θ azimuthal re-optimization (review Finding 2). → Why SOT differs? Re-optimization not propagated. | Per-θ re-optimization landed in manuscript, not SOT. | **BLOCKING** (numeric contradiction) |
| **A3** | SOT §8.3 ("delta proportional to cos theta") and §11.1 ("map the cos theta dependence") retain exact-proportionality language. Manuscript v94 downgraded this to "δ = 0 iff θ=π/2; non-zero otherwise; exact θ-dependence numerical (`cos θ` overestimates \|δ\| by ~5.5×)". | Why? v94 RCA round 4 fix not propagated to SOT. | SOT not updated for the v94 `cos θ` downgrade. | HIGH |
| **A4** | SOT labels θ=31° "optimal"; manuscript v94 softened to "near-optimal" (θ=35° → FOM 8.8 on a broad plateau). | Same as A3. | Same. | LOW |
| **A5** | `CHANGELOG.md` top entry is **v88**; manuscript header is **v94** → v89–v94 untraced. | Why? Changelog discipline lapsed after v88. | Missing changelog entries v89–v94. | MEDIUM (traceability) |
| **A6** | `README.md` states "manuscript.md Draft v19 — 10 sections + 16 refs"; actual = v94, Sections 1–9 + Abstract, 18 refs `[1]–[18]`, arXiv-submitted 2026-05-27. | Why? README frozen at an early milestone. | README never updated past early drafts. | MEDIUM |

### Group B — Manuscript-internal stragglers

| # | Symptom | Isolated root cause | Severity |
|---|---------|---------------------|----------|
| **B1** | §2.3 (line ~148) still reads "with the **cos θ scaling** under θ-sweep (§8.2) providing the distinguishing signature". v94's fix list covered §1/§3.1/§3.2-table/§5.3/§8.1–8.2/Discussion-Table but **omitted §2.3**. | v94 downgrade incomplete — §2.3 missed. | HIGH (residual inconsistency inside the FROZEN §2.3 — see Risk R4) |
| **B2** | μ-threshold language not uniform: §4.3 table "μ required ≥ 0.86"; §7 "μ ≥ 0.92 and η ≥ 0.91"; abstract "η ≈ 0.87". Onset (0.86) vs 5σ (0.92) vs Bong-achieved η (0.87) must be unambiguous at each mention. | Thresholds introduced across versions without a single normalizing pass. | MEDIUM |
| **B3** | Confirm `review/RCA_manuscript_analysis.md` Finding 2 ("await FOM sweep results") is **closed** and the §4.1 FOM values are the final per-θ-reoptimized set. | Review doc still at v91, Finding 2 marked "under investigation". | VERIFY |

### Group C — Framework (class_c v36) alignment

| # | Item | Decision/verify | Severity |
|---|------|-----------------|----------|
| **C1** | Cross-check headline numbers against `index.md` v36 + `CLAUDE.md`: Gen LF1 `+0.0891` (8.6σ), δ⟨A₁B₂⟩ `−0.0355` (20.8σ), FOM `8.6`, α=31°, Class C **qualified**. Surface check: consistent. | Hard-verify in Phase 1. | VERIFY |
| **C2** | ~~Framework f_perp vs paper f_perp look like different objects.~~ **RESOLVED (Phase 0, 2026-05-30, 4.53/5)** — INTENDED structure-preserving BRIDGE, not a category error. Canonical form is `[1 − β·f_perp(o,K_ctx)]` with `f_perp` = ⊥_K-incompatibility fraction = `E[I(K5 fires)]` (T8); paper `f_perp(b,d)=1−\|⟨b\|d⟩\|²` is its **N=2 Born instantiation**. The apparent mismatch came from `index.md §3`'s abbreviation `f_perp(K_ctx)=1−β·K_ctx`. See `review/Phase0_RCA_C2_C3_verdict.md`. | **GATE CLEARED → PROCEED.** Scope stays "update" (paper bundle); no K9_E framework change required. | RESOLVED |
| **C3** | The arXiv-facing manuscript carries no framework-style honest-status note. | **RESOLVED (Phase 0, 4.43/5) — KEEP DECOUPLED.** No new disclaimer; Phase 4 only **verifies** honest framing intact (no β measured; null-test; Phase 1 screening). β stays a bare SME-style search parameter. | RESOLVED |
| **F-IDX** | *(Spun off by C2, framework-side, OUT OF paper_002 scope)* ~~`index.md §3` imprecise~~ → reclassified as *undocumented equivalent dual convention* (conv 1 operational/coded vs conv 2 derivation-chain; no wrong numbers). | **RESOLVED + SUPERSEDED 2026-05-30:** Stage 1 F-IDX (4.50/5, Option B) added reconciliation note. Stage 2 RCA NORM-1 (4.33/5) applied full standardization: Conv 2 canonical across `index.md §3`, `Definitions §3.4`, `Falsification_Hierarchy §2.5`, `k9e_predictor.py`, `CLAUDE.md`, `paper_002_SOT.md L83`. RCAs: `04_governance/RCA_F_IDX_fperp_notation_2026_05_30.md` (superseded) → `04_governance/RCA_NORM1_standardize_conv2_2026_05_30.md` (final). | RESOLVED |

### Group D — Supplemental

| # | Item | Action | Severity |
|---|------|--------|----------|
| **D1** | Verify `S2_derivation.md` contains the "~5.5× overestimate" warning (v94 claims it was added) and `S2_correlator_table.md` uses numerical (not `cos θ`) values. | Verify in Phase 1. | VERIFY |
| **D2** | Re-run `supplemental/*.py` (`RCA_full_verification_v93.py`, `RCA_manuscript_verification.py`, `statistical_significance.py`, `K9S12_proposal.py`, `RCA_fom_sweep.py`, …) to reproduce every v94 number. v94 claims "updated stale RCA scripts" — must be checked. | Hard-verify; produces the source-of-truth number table. | VERIFY (high value) |
| **D3** | Confirm `S3_interpretations.md` / `S3_code_index.md` match §8/§9 prose and the 18-reference list. | Verify in Phase 1. | VERIFY |

---

## 3. Fix the cause, not the symptom — Phased execution (for the future approved session)

> Order matters: decisions gate verification; verification establishes the source-of-truth numbers; only then are satellites re-synced. Sequence prevents re-introducing drift.

### Phase 0 — RCA decisions (GATE) — items C2, C3 — ✅ DONE (2026-05-30)
- **C2 RESOLVED (4.53/5):** intended structure-preserving bridge (paper f_perp = N=2 Born instantiation of framework `E[I(K5 fires)]`, T8). Not a category error.
- **C3 RESOLVED (4.43/5):** keep decoupled — no new disclaimer; verify framing in Phase 4.
- **Exit gate:** PASSED (C2 = "intended bridge") → **PROCEED to Phase 1.** Scope confirmed "paper bundle only".
- Spun-off **F-IDX** logged (framework-side `index.md §3` notation; out of paper scope).
- Verdict: `review/Phase0_RCA_C2_C3_verdict.md`.

### Phase 1 — Establish the source of truth — items D2, B3, C1, D1, D3
- Re-run the full `supplemental/` script suite; tabulate **claim ↔ script-output** for every headline number.
- Cross-check that table against `index.md` v36 + `CLAUDE.md` (C1).
- Update `review/RCA_manuscript_analysis.md` from v91 → v94 (close Finding 2; record the final FOM set).
- Confirm D1/D3 against the regenerated numbers.

### Phase 2 — Manuscript stragglers (surgical) — items B1, B2
- **B1:** downgrade the §2.3 "cos θ scaling" clause to match the v94 numerical framing. ⚠️ §2.3 is FROZEN — requires an explicit freeze-exception (Risk R4); do not touch other §2.3 content.
- **B2:** normalize μ-threshold wording: state onset (μ ≥ 0.86), 5σ (μ ≥ 0.92), and Bong-achieved η (≈ 0.87) unambiguously at each mention. Only the threshold clauses change.

### Phase 3 — Re-sync satellites from the v94 source of truth — items A1–A6
- **A1:** SOT §6.1 density matrix `I/4` → HV/VH model.
- **A2:** SOT §4.6/§6.5 FOM table + window → manuscript's per-θ-reoptimized set (`[20°,45°]`).
- **A3:** SOT §8.3/§11.1 `cos θ` proportionality → v94 numerical framing.
- **A4:** SOT "optimal" → "near-optimal".
- **A5:** append CHANGELOG entries v89–v94 (reconstruct from manuscript headers + git log).
- **A6:** update README (v94 / Sections 1–9 + Abstract / 18 refs / arXiv-submitted).
- All edits **extend, not overwrite**; preserve author intent and existing structure.

### Phase 4 — Verify (root cause removed, not just symptom)
- Run `QC_checklist.md` (target: all PASS).
- Cross-validate SOT ↔ manuscript ↔ supplemental ↔ index v36: zero number/claim contradictions.
- Confirm the desync root cause is closed: every satellite now declares the v94 milepost and matches it.

---

## 4. Risks

| ID | Risk | Mitigation |
|----|------|------------|
| **R1 (HIGH)** | C2 resolves to "category error" → fix scope expands into the frozen K9_E framework, beyond an "update". | Phase 0 gate stops execution and escalates before any prose change. |
| **R2 (MEDIUM)** | Re-sync re-introduces oscillation (cf. v77–v88 history of accept/reject churn). | Every edit cites the v94 source-of-truth number; no re-litigation of settled RCA verdicts. |
| **R3 (MEDIUM)** | PEER duplicates of the paper exist at `04_governance/paper/draft_v1.md` and `03_k9_sprints/k9_s12/`. | Out of scope for v2.0; record a note. Do NOT silently edit peers. |
| **R4 (LOW→guard)** | §2.3 and §3.5 are FROZEN (v94); title is frozen (memory). B1 touches a §2.3 clause. | Treat B1 as a freeze-exception requiring explicit user approval at execution time; touch only the `cos θ` clause. |
| **R5 (LOW)** | Manuscript already submitted to arXiv (2026-05-27); edits diverge the local copy from the submitted version. | Record changes as a post-submission revision set; coordinate a v2 arXiv replacement if warranted. |

---

## 5. Deliverables & locations

| Deliverable | Path | Phase |
|-------------|------|-------|
| This plan | `papers/paper_002/paper_plan_v2.0_RCA_update.md` | (now) |
| Updated RCA review (v91→v94) | `papers/paper_002/review/RCA_manuscript_analysis.md` | 1 |
| C2/C3 RCA verdict | `papers/paper_002/review/` (new file) | 0 |
| Synced SOT / CHANGELOG / README | `papers/paper_002/{SOT,CHANGELOG.md,README.md}` | 3 |

Author-metadata rule: this file and all Phase-1/3 targets are **outside** `published_documents`/`public_documents`, so author metadata is required at top (present here).

---

## 6. Complexity estimate

| Phase | Effort | Note |
|-------|--------|------|
| 0 | HIGH | Decision-heavy; gates everything |
| 1 | MEDIUM | Script runs + tabulation |
| 2 | LOW | Surgical edits (guarded by freeze) |
| 3 | LOW–MEDIUM | Mechanical re-sync from SoT |
| 4 | LOW | QC + cross-validation |

---

## 7. Acceptance criteria (Verify, RULE ZERO step 5)

- [ ] Every headline number in `manuscript.md` reproduced by a `supplemental/` script (claim↔output table).
- [ ] SOT, README, CHANGELOG each declare the **v94** milepost and contain no value contradicting the manuscript.
- [ ] No `cos θ` exact-proportionality claim remains anywhere in the bundle (only the numerical / "~5.5× overestimate" framing).
- [ ] μ/η thresholds (onset 0.86 / 5σ 0.92 / Bong-η 0.87) unambiguous at every mention.
- [ ] Headline numbers + Class C (qualified) status match `class_c` index v36.
- [x] C2 verdict recorded with score ≥ 4/5; scope confirmed as "update" (not framework change). **DONE (4.53/5, 2026-05-30).**
- [ ] `QC_checklist.md` all PASS.

---

*Plan v2.0 — 2026-05-30. Source of truth for execution = manuscript.md v94 + verified supplemental script outputs + class_c index v36. Predecessor: paper_plan_single_waveplate_EWF.md (writing plan, 2026-05-23). Execution deferred pending approval; C2 (f_perp dual meaning) is a Phase 0 RCA gate.*
