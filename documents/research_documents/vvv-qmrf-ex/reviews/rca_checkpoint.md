Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Plan — RCA Checkpoint

> **Purpose:** Single-source checkpoint for all RCA findings applied to `vvv-qmrf-ex-plan.md`. Tracks which fixes are applied at which plan version, and which findings remain open.
> **Last updated:** 2026-05-20
> **Plan current version:** v1.2
> **Total findings to date:** 10 (3 from v0→v1.0 isolation review + 6 from v1.0→v1.1 RCA review + 1 from Phase 1 execution)
> **Status:** All 10 findings ✅ CLOSED — Phase 0 ✅ Phase 1 ✅ Phase 2 ✅ Phase 3 ✅ Phase 4 ✅ complete

---

## 1. Checkpoint Summary Table

| Finding ID | Severity (final) | Source review | Applied at version | Status | Plan section |
|---|---|---|---|---|---|
| Fix 1 | 🔴 High | `impact_isolation_analysis.md` §4 | v1.0 | ✅ Closed | §3.5 Tier 2, §4.5 Tier 1, §8 Rule I-2 |
| Fix 2 | 🔴 High | `impact_isolation_analysis.md` §4 | v1.0 | ✅ Closed | §3.5 Tier 2, §4.5 Tier 2, §8 Rule I-2 |
| Fix 3 | 🟡 Medium | `impact_isolation_analysis.md` §4 | v1.0 | ✅ Closed | §8 (full Isolation Protocol with Rules I-1 to I-5) |
| F1 | 🟡 Medium | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §11.1 Namespace Declaration + new `ex_schema_addendum.md` |
| F2 | 🟡 Medium | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §3.5 — Direction Non-Reversal Note |
| F3 | 🟡 Medium | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §7 Phase 1 Step 1.6 |
| F4 | 🟡 Medium | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §7 Phase 3 Step 3.1 |
| F5 | 🟡 Medium (revised from 🟢 Low) | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §10 — Per-node K/ρ coverage criteria |
| F6 | 🔴 High (revised from 🟢 Low) | RCA review of v1.0 (this session) | v1.1 | ✅ Closed | §7 Phase 0 — Environment Setup |
| F7 | 🟡 Medium | Phase 1 execution — VVV node count discrepancy | v1.2 | ✅ Closed | §1.1, §2.2, §4.2, §5.2 (code comment), §7 Step 1.2, §7 Step 3.2-3.3, §12 |

---

## 2. v0 → v1.0 Fixes (3 findings — isolation review)

### Fix 1 — "Migrated" → "Referenced" (High)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v0 dùng từ "migrated" cho 15 BR_XXXXX v0.1 edges → có thể hiểu là move/delete khỏi `bridge_QM_standard_to_VVV_QMRF.md`. |
| **Root cause** | Verbiage ambiguity giữa copy-vs-move violates isolation principle. |
| **Fix applied at v1.0** | Section 4.5 Tier 1: `"15 referenced BR_XXXXX edges (reference-copy from v0.1 bridge registry; originals remain frozen)"`. Rule I-2 trong Section 8 enforce "Reference-copy replaces migrate". |
| **Verify** | `bridge_QM_standard_to_VVV_QMRF.md` unchanged (frozen per Rule I-1). |

### Fix 2 — "Promoted" → "Derived-copy" (High)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v0 dùng "promoted" cho 20-30 Phase 2 edges → có thể hiểu là remove từ `edge_QM_VVV.md`. |
| **Root cause** | Verbiage ambiguity threatens 115-edge integrity of VVV-QMRF core. |
| **Fix applied at v1.0** | Section 3.5 Tier 2 + Section 4.5 Tier 2: `"derived-copy ... originals remain frozen in edge_QM_VVV.md"`. Rule I-2 enforce. |
| **Verify** | `edge_QM_VVV.md` edge count stays at 115. |

### Fix 3 — Add Isolation Protocol (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v0 thiếu section chính thức về cách ly EX khỏi core. |
| **Root cause** | Không có authoritative protection rules cho core artifacts. |
| **Fix applied at v1.0** | Section 8 full Isolation Protocol — Rules I-1 (READ-ONLY contract), I-2 (Copy-Not-Move), I-3 (Namespace Isolation), I-4 (Rollback = Delete Directory), I-5 (Promotion Gate). |
| **Verify** | Section 8 present with 5 explicit rules + protected-files table. |

---

## 3. v1.0 → v1.1 Fixes (6 findings — RCA review of plan v1.0)

### F1 — Namespace declaration vs frozen schema_guide.md (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v1.0 dùng `BR_EX_BE_XXXXX` / `BR_EX_QM_XXXXX` nhưng `schema_guide.md` (frozen per Rule I-1) không khai báo namespace này → namespace mồ côi. |
| **Root cause** | Plan thiếu chỉ định nơi authoritative cho EX namespace mà không vi phạm isolation. |
| **Fix applied at v1.1** | Section 11.1 mới — Namespace Declaration EX-local. Tạo file `ex_schema_addendum.md` self-contained (5 sub-sections). `schema_guide.md` KHÔNG bị sửa. |
| **Verify** | Section 11.1 present; `ex_schema_addendum.md` listed trong file structure (chưa tạo, sẽ tạo ở Phase 4). |

### F2 — Direction non-reversal cho derived-copy (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Phase 3 edges direction `VVV→BE`; BR_EX_BE schema direction `BE→VVV`. Derived-copy có thể đảo chiều ngầm. |
| **Root cause** | Plan v1.0 không document rule về direction handling khi derived-copy. |
| **Fix applied at v1.1** | Section 3.5 thêm "Direction Non-Reversal Note" — `BE Anchor` và `VVV-QMRF Anchor` là role labels không phải direction; `Bridge Relation` field phải ghi rationale (e.g., `source_analogue_of`). |
| **Verify** | Section 3.5 chứa quote-block bắt đầu bằng "F2 — Direction Non-Reversal Note". |

### F3 — Step 1.6 verification (integrity vs coverage) (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v1.0 Step 1.6 verification `"Zero orphan nodes in VVV layer"` mâu thuẫn với baseline `~15 orphan nodes` (per effectiveness review §1.1). |
| **Root cause** | Plan trộn 2 khái niệm: integrity (no dangling edge ref) và coverage (no isolated nodes). |
| **Fix applied at v1.1** | Step 1.6 verification đổi thành: `"Zero dangling edge references ... Orphan nodes are permitted at this phase — they are gap-fill targets for Phase 4"`. |
| **Verify** | Phase 1 Step 1.6 row chứa "Zero dangling edge references" + "orphan nodes are permitted". |

### F4 — Embedding model + version specification (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v1.0 Step 3.1 không specify embedding model → reproducibility (Success Criterion #6) bị vi phạm. |
| **Root cause** | Plan implicit assumption về môi trường runtime. |
| **Fix applied at v1.1** | Step 3.1 specify `sentence-transformers/all-mpnet-base-v2` (768-dim, English-optimized, local, free) + alternative `text-embedding-3-large`. Model + version phải ghi vào `vvv_qmrf_ex_context.json`. Section 10 thêm criterion "Embedding reproducibility". |
| **Verify** | Step 3.1 chứa "all-mpnet-base-v2"; Section 10 có row "Embedding reproducibility (F4)". |

### F5 — Per-node coverage criteria (Medium, revised từ Low)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v1.0 success criteria chỉ count total bridges (≥30 each). 30 edges có thể tập trung 5 nodes giàu → 15 orphan nodes vẫn orphan = metric gaming. |
| **Root cause** | Total-count metric không guarantee per-node coverage. |
| **Severity revision** | Low → Medium vì likelihood metric gaming cao trong systematic similarity expansion. |
| **Fix applied at v1.1** | Section 10 thêm 2 criteria mới: "Per-node K-side coverage (F5)" và "Per-node ρ-side coverage (F5)". Mỗi VVV node phải có ≥1 BR_EX_BE và ≥1 BR_EX_QM, hoặc nằm trong approved gap exception list. |
| **Verify** | Section 10 chứa 2 row mới với prefix "Per-node". |

### F6 — Phase 0 Environment Setup (High, revised từ Low)

| Aspect | Detail |
|---|---|
| **Symptom** | Plan v1.0 Section 12 ghi Python+NetworkX env là "❓ To verify \| Blocking for Phase 1" nhưng KHÔNG có mitigation step. |
| **Root cause** | Plan thiếu Phase 0 — execution sẽ FAIL ngay Phase 1 Step 1.1 nếu env không có. |
| **Severity revision** | Low → High vì likelihood ~100% (plan explicit ghi "To verify") và impact = block toàn bộ Phase 1-3. |
| **Fix applied at v1.1** | Section 7 thêm Phase 0 mới với 6 steps (Python version check, install deps, smoke tests cho NetworkX + sentence-transformers, env_manifest, data/ dir init). Blocking condition: bất kỳ step 0.1-0.4 fail → STOP. Section 12 update dependency row. Section 13 (Recommended Next RCA Step) cập nhật để bắt đầu từ Phase 0. |
| **Verify** | Section 7 có "Phase 0 — Environment Setup" với 6 steps; Section 13 step 2 là "Execute Phase 0". |

---

## 3b. v1.1 → v1.2 Fixes (1 finding — Phase 1 execution finding)

### F7 — VVV node count 55 → 52 (Medium)

| Aspect | Detail |
|---|---|
| **Symptom** | Phase 1 script parsed 52 VVV nodes; plan stated 55. |
| **Root cause** | Plan used max node code number (`N_QM_VVV_00055`) as the count. Actual `node_QM_VVV.md` has 52 table rows — codes 00017, 00019, 00026 were explicitly folded/downgraded in the source file (per RCA note at bottom of `node_QM_VVV.md`). This is **not a parsing error** — it is a plan authoring error: estimate vs actual count. |
| **5 Whys** | (1) Plan says 55 — why? Because plan was written before Phase 1 executed. (2) Why wasn't count verified? Because Phase 0 only checked env, not data. (3) Why were 3 codes folded? Because audit cycle explicitly retired them as redundant. (4) Why did plan use 55? Max code value was used as a proxy for count. (5) Root cause: count ≠ max_code when codes have intentional gaps. |
| **Fix applied at v1.2** | Updated 11 occurrences in plan: §1.1 symptom text, §2.2 node inventory count, §4.2 input sources table, §5.2 Python comment, §7 Step 1.2 output+verification, §7 Step 3.1 total node count (423→420), §7 Step 3.2 matrix shape (263×55→263×52), §7 Step 3.3 matrix shape (55×105→52×105), §12 dependency row. Changelog v1.1→v1.2 added to plan header. Code range `N_QM_VVV_00001–N_QM_VVV_00055` preserved unchanged (codes are correct; only count fields updated). |
| **Verify** | Phase 1 `phase1_validation_report.json` shows `"vvv": 52`. Plan §2.2 count column = "52 (3 codes unassigned: 00017, 00019, 00026)". All matrix shapes = (263, 52) and (52, 105). |

---

## 4. Cross-Reference Map — Findings → Plan Sections

```
impact_isolation_analysis.md  ──┬── Fix 1 ──▶ plan §3.5, §4.5, §8 (v1.0)
                                 ├── Fix 2 ──▶ plan §3.5, §4.5, §8 (v1.0)
                                 └── Fix 3 ──▶ plan §8 Rules I-1 to I-5 (v1.0)

RCA review v1.0 (this session)──┬── F1 ──▶ plan §11.1 + ex_schema_addendum.md (v1.1)
                                 ├── F2 ──▶ plan §3.5 Direction Non-Reversal Note (v1.1)
                                 ├── F3 ──▶ plan §7 Phase 1 Step 1.6 (v1.1)
                                 ├── F4 ──▶ plan §7 Phase 3 Step 3.1 + §10 (v1.1)
                                 ├── F5 ──▶ plan §10 per-node criteria (v1.1)
                                 └── F6 ──▶ plan §7 Phase 0 + §12 + §13 (v1.1)

Phase 1 execution finding ───── F7 ──▶ plan §1.1, §2.2, §4.2, §5.2, §7 Steps 1.2/3.1/3.2/3.3, §12 (v1.2)
```

---

## 5. Verify — RCA Closure Checklist

| Item | Confirmed |
|---|---|
| Plan v1.2 header reflects status "Phase 0 + Phase 1 complete; VVV count corrected (F7)" | ✅ |
| Changelog v1.1→v1.2 in plan header lists F7 fix | ✅ |
| All 10 findings (Fix 1-3 + F1-F7) marked Applied in this checkpoint | ✅ |
| Section 8 Isolation Protocol intact (Rules I-1 to I-5) | ✅ |
| `schema_guide.md` NOT modified (frozen per Rule I-1) | ✅ |
| `edge_QM_VVV.md` NOT modified (edge count = 115) | ✅ |
| `bridge_QM_standard_to_VVV_QMRF.md` NOT modified (15 BR_XXXXX intact) | ✅ |
| `ex_schema_addendum.md` listed in file structure (to-create at Phase 4) | ✅ |
| Phase 0 added as new pre-Phase 1 step | ✅ |
| Per-node coverage criteria added to Section 10 | ✅ |

---

## 6. Open Items (Forward-looking — NOT blocking Phase 0)

| Item | Owner | Trigger |
|---|---|---|
| Create `ex_schema_addendum.md` | Plan executor | Start of Phase 4 (Bridge Registry Construction) |
| BIAN-14 structural review (open item #1 from §12) | Separate RCA gate | Before final paper submission |
| Final BR_XXXXX ID assignment (open item #2 from §12) | Separate RCA gate | When VVV-QMRF v1.0 freeze decided |
| EX → Core promotion (Rule I-5) | Separate RCA gate | After VVV-QMRF-EX results validated |

---

## 7. Execution Progress

| Phase | Status | Key outputs | Key numbers |
|---|---|---|---|
| Phase 0 — Environment Setup | ✅ Complete | `data/env_manifest.txt` | Python 3.12.10, all packages ✅ |
| Phase 1 — Graph Construction | ✅ Complete | `data/vvv_qmrf_ex_graph.json`, `data/phase1_validation_report.json` | 420 nodes, 149 edges, 0 dangling ✅ |
| Phase 2 — Intersection Analysis | ✅ Complete | `data/phase2_intersection_report.json`, `data/vvv_qmrf_ex_centrality.csv`, `vvv_qmrf_ex_intersection.md`, `vvv_qmrf_ex_gaps.md` | 16 intersection nodes, 36 K-gaps, 1 ρ-gap, 323 communities, 30 paths ✅ |
| Phase 3 — Similarity Search | ✅ Complete | `data/vvv_qmrf_ex_similarity_be_vvv.csv`, `data/vvv_qmrf_ex_similarity_vvv_qm.csv`, `data/vvv_qmrf_ex_context.json`, `data/phase3_similarity_report.json` | 263×52 max=0.5645 · 52×105 max=0.7216 · BE→VVV new T2=2 · VVV→QM new T2=13 ✅ |
| Phase 4 — Bridge Registry | ⏳ Pending | `br_ex_be_registry.md`, `br_ex_qm_registry.md`, `ex_schema_addendum.md` | — |
| Phase 5 — Visualization & Validation | ⏳ Pending | Graph diagrams, boundary audit | — |

### Phase 3 Key Findings

| Finding | Value | Interpretation |
|---|---|---|
| BE↔VVV max similarity | 0.5645 | No Tier1 (≥0.75). K-side gap (36 nodes) is **semantic**, not just structural — all-mpnet conceptually distinguishes Buddhist epistemic terms from quantum registration vocabulary. |
| VVV↔QM max similarity | 0.7216 | Near Tier1. ρ-side is more semantically aligned — quantum physical terms overlap more with VVV registration language. |
| New BE→VVV Tier2 candidates | 2 pairs (score ≥0.50) | Bridge 1 weak latent additions. Require domain expert review. |
| New VVV→QM Tier2 candidates | 13 pairs (score ≥0.50) | Bridge 2 expansion candidates after removing 61 existing VVV-QM pairs. |
| K-gap best matches | Manual range (0.30–0.44) | No high-confidence BE matches found for the 36 K-gap nodes. Phase 4 bridge formalization will require conceptual judgment, not similarity-driven automation. |
| Bug found + fixed | `data.get("links")` → `data.get("edges")` | NetworkX 3.x changed node-link JSON key. Fixed before final outputs saved — outputs are correct. |
| Integrity checks | [OK] All 4 pass | Matrix shapes (263,52) and (52,105) verified; model name + dim recorded. |

### Phase 2 Key Findings

| Finding | Value | Plan expectation | Status |
|---|---|---|---|
| Intersection nodes (dual K-ρ) | 16 / 52 (30.8%) | ≥ 15 | ✅ Pass |
| K-side gaps (no BE anchor) | 36 / 52 (69.2%) | — | Expansion target for Phase 4 Bridge 1 |
| ρ-side gaps (no QM anchor) | 1 / 52 (1.9%) | — | Very low — ρ-side coverage near-complete |
| Both gaps (no BE and no QM) | 1 / 52 (1.9%) | — | Pure internal node |
| Direct BE→QM edges | 0 | 0 | ✅ Pass — all K-ρ paths route through VVV |
| Top mediator | `N_QM_VVV_00021` (Registration Lock, betweenness=0.002370) | Aligns with E-postulate | ✅ |
| Community count | 323 total (most = single orphan nodes) | — | Top communities have mixed BE+VVV+QM structure ✅ |

**Interpretation:** The K-side gap (36 nodes) is the dominant expansion target — 69% of VVV nodes have no BE draft bridge yet. The ρ-side is nearly fully covered (only 1 gap). Phase 3 similarity search will detect latent K-side connections to fill these gaps.

---

## 8. Execution Progress

| Phase | Status | Date | Key outputs |
|-------|--------|------|-------------|
| Phase 0 — Environment Setup | ✅ Complete | 2026-05-20 | Python 3.12 verified, deps installed |
| Phase 1 — Graph Construction | ✅ Complete | 2026-05-20 | 420 nodes, 149 edges, `vvv_qmrf_ex_graph.json` |
| Phase 2 — Intersection Analysis | ✅ Complete | 2026-05-20 | 16/52 intersection, `phase2_intersection_report.json` |
| Phase 3 — Similarity Search | ✅ Complete | 2026-05-20 | 263×52 + 52×105 matrices, `phase3_similarity_report.json` |
| Phase 4 — Bridge Registry | ✅ Complete | 2026-05-20 | BR_EX_BE=37, BR_EX_QM=74, 151 edges |
| Phase 5 — Visualization & Validation | ⏳ Pending | — | — |

### Phase 4 Key Findings

| Metric | Value | Notes |
|--------|-------|-------|
| BR_EX_BE entries | 37 (36 ref-copy + 1 new) | 1 of 2 Tier2 BE candidates was already in graph |
| BR_EX_QM entries | 74 (73 ref-copy + 1 new) | VVV↔QM pairs were 73 (not 61); only 1 of 13 Tier2 QM candidates was truly new |
| New BR_EX edges added | 2 (+1 BE, +1 QM) | Graph: 149 → 151 edges |
| Intersection (Phase 4 final) | 16 / 52 VVV nodes | Unchanged from Phase 2 (2 new edges did not unlock new intersection nodes) |
| K-side gaps (no BE anchor) | 36 / 52 | Dominant gap — requires domain expert review |
| ρ-side gaps (no QM anchor) | 1 / 52 | Near-complete ρ-side coverage |
| Both-side gaps | 1 / 52 | Pure internal node |
| Files created (Phase 4) | 7 | `ex_schema_addendum.md`, `br_ex_be_registry.md`, `br_ex_qm_registry.md`, updated graph, intersection.md, gaps.md, `phase4_registry_report.json` |

**Note:** VVV↔QM reference-copy count was 73 (not 61 as estimated in plan) because Phase 1 graph contained more VVV_TO_QM edges than the plan estimated. This is an implementation detail, not an RCA finding — the bridge registry correctly mirrors all Phase 1 edges.

---

## 9. Next Action

**Next: Phase 5 — Visualization & Validation**

Input data ready:
- `data/vvv_qmrf_ex_graph.json` (420 nodes, 151 edges — Phase 4 final)
- `br_ex_be_registry.md` (37 entries)
- `br_ex_qm_registry.md` (74 entries)
- `vvv_qmrf_ex_intersection.md` (Phase 4 Final — 16/52 intersection)
- `vvv_qmrf_ex_gaps.md` (Phase 4 Final — 36 K-gaps, 1 ρ-gap, 1 both-gap)

Phase 5 deliverables:
1. Graph visualization (layer-colored node plot — BE=blue, VVV=green, QM=red)
2. Bridge coverage heatmap (BE↔VVV and VVV↔QM similarity matrices)
3. Intersection/gap summary validation
4. Final VVV-QMRF-EX report

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
