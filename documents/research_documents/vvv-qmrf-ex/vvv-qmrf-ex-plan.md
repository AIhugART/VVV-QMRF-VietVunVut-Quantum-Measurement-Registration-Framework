Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Expansion Plan

> **Document type:** RCA expansion plan
> **Status:** Plan v1.7 — EXECUTED; v1.6 Phases 0–10 ALL COMPLETE; v1.7 Phase 11 KE-SC threshold tightening (3.5→4.0 + 1 carve-out at 3.8) applied; F1–F15 + F-RCA-01/02/05/07/08/09/10/11/12/13/14/15 applied; 9 KE-PM + 13 KE-OF + 7 KE-SC accepted (3 KE-SC reclassified to exception); Phase 11 boundary audit PASS on 140 entries; Phase 11 raw dual-anchored 45/52 = 86.5% (Stretch Tier 1+2 still PASS); rigor near-symmetric (KE-OF 4.5 vs KE-SC 4.0)
> **Date:** 2026-05-21
> **Scope:** Expand VVV-QMRF into VVV-QMRF-EX by identifying K-side ↔ ρ-side relationships via two bridge expansion directions
> **Boundary:** Structural analogy only; no BE-QM identity; no new QM law; no automatic E17+; no replacement of Standard QM
> **Tools:** NetworkX (graph analysis), Similarity Search Patterns (semantic similarity), Context Management (knowledge graph construction)
>
> **Changelog v1.0 → v1.1 (2026-05-20):** Applied 6 RCA fixes (F1–F6) — self-contained namespace declaration (F1); direction non-reversal note for derived-copy edges (F2); Step 1.6 verification clarified — integrity vs coverage (F3); embedding model + version specified (F4); per-node coverage success criterion (F5); new Phase 0 — Environment Setup (F6).
>
> **Changelog v1.1 → v1.2 (2026-05-20):** Applied RCA fix F7 — corrected VVV node count from 55 → 52. Root cause: plan used max node code (N_QM_VVV_00055) as count; actual table has 52 rows (codes 00017, 00019, 00026 explicitly folded/downgraded in `node_QM_VVV.md`). Code range `00001–00055` is unchanged; only the count fields and matrix shapes are updated.
>
> **Changelog v1.2 → v1.3 (2026-05-20):** Applied 8 RCA fixes (F8–F15) from post-execution audit. **F8:** BR v0.1 edge count clarified — 13 graphable + 2 boundary guards (BR_00002, BR_00015 are abstract anchors, not graphable node pairs). **F9:** Draft bridge count clarified — 21 directed edges from 19 unique proposals (multi-BIAN duplicates). **F10:** Section 2.3 edge decomposition updated to match Phase 1 loader output; total 149 preserved with honest per-type breakdown. **F11:** Ghost entry BR_EX_BE_00037 populated — was empty fields/cosine=0.0000; now `N_BE_00086 → N_QM_VVV_00051` (cosine=0.564). **F12:** Ghost entry BR_EX_QM_00074 populated — was empty fields/cosine=0.0000; now `N_QM_VVV_00051 → N_QM_00037` (cosine=0.614). **F13:** `context.json` edge_count corrected from 0 → 151; version updated to 0.4-phase4-f8f15. **F14:** Success criterion "≥80% intersection" replaced with staged milestones — Phase 4 actual = 30.8% (16/52); Phase 5+ target = 50% with manual review; Phase 6+ target = 80% with full expert mapping. Root cause: 0.75 threshold too aggressive for cross-domain (Sanskrit/Pāli ↔ QM) similarity — zero Tier1 candidates found. **F15:** Gap exception list framework added — per-node coverage (F5) now requires formal `k_gap_exception_list` and `rho_gap_exception_list` artifacts.
>
> **Changelog v1.4 → v1.5 (2026-05-20):** Applied 2 BLOCKING fixes from `reviews/rca_plan_implementation_audit.md` (decided via 3-round RCA × 5-Why × scoring ≥4/5). **F-RCA-01:** Phase 2 baseline restored — `data/phase2_intersection_report.json` restored from git commit `2bffc3f` (Phase 4-era state: 16 intersection, 149 edges); post-Phase 6 state preserved in new file `data/phase2_intersection_report_post_phase6.json` (25 intersection, 160 edges). Added `snapshot_phase` field to all 7 phase JSONs to prevent future baseline loss. New rule added to §7: phase reports are immutable. **F-RCA-02:** Phase 5/6 success criterion replaced with dual-criterion framework — **Primary (Completeness):** effective ≥80% coverage (covered + structural exceptions); **Secondary (Discovery quality):** raw dual-anchored ≥30%. Both met → Phase 5/6 ✅ PASS honestly. Raw ≥50% / ≥80% retained as stretch goals (future expert mapping). §10.1 and §13 lines 631-632 updated.
>
> **Changelog v1.5 → v1.6 (2026-05-20) — PROPOSED, AWAITING EXECUTION:** Added Section 14 — Stretch Expansion Plan covering Phases 7–10 with the goal of lifting raw dual-anchored from 48.1% (25/52) toward Stretch Tier 1 (≥50%, ≥26 nodes) and Stretch Tier 2 (≥80%, ≥42 nodes) by promoting up to 23 KE-OF + KE-SC nodes to direct BR_EX_BE entries (range `BR_EX_BE_00047`–`BR_EX_BE_00069`). **Decision parameters (user-confirmed 2026-05-20):** Q1=batch-approve per category; Q2=split threshold (KE-OF strict 4.5/5, KE-SC relaxed 3.5/5 due to parent inheritance support); Q3=split output files (`phase7_ke_of_rca_log.md` and `phase7_ke_sc_rca_log.md`). 3-round rejection protocol on all RCA gates. Audit closure for F-RCA-05/07/08/09/10/11. Full re-run of Phases 1–6 into immutable `_v1.6.json` snapshots (no overwrite of v1.5 files).
>
> **Changelog v1.6 EXECUTED → v1.7 EXECUTED (2026-05-21):** Phase 11 KE-SC threshold tightening to align rigor with KE-OF. Single new RCA finding **F-RCA-15** — Phase 7 §14.2 Q2 threshold (KE-SC=3.5/5) was a pragmatic floor; publication-ready rigor requires near-symmetric thresholds with KE-OF (4.5/5). Fix: raise KE-SC threshold to **4.0/5 with 1 carve-out at 3.8** (boundary-guard-justified). 3 KE-SC entries reclassified from KE-RESOLVED-STRETCH back to KE-SC exception: `BR_EX_BE_00061` (`N_QM_VVV_00008`, 3.7), `BR_EX_BE_00065` (`N_QM_VVV_00022`, 3.8), `BR_EX_BE_00066` (`N_QM_VVV_00024`, 3.7). Namespace gaps preserved (no renumber to keep v1.5/v1.6 hash invariants). Result: 143 → 140 entries; graph 183 → 180 edges; raw dual-anchored 92.3% → **86.5%** (Tier 1+2 still PASS with 6.5pt margin). See §15 for full v1.7 spec; commit chain: `9525eb8` (v1.5-final) → `d8ec025` (v1.6 Phase 9) → `c1b3168` (v1.6 Phase 10) → v1.7 commit (this batch).

> **Changelog v1.6 PROPOSED → v1.6 EXECUTED (2026-05-21):** Phase 9 + partial Phase 10 completed (commit `d8ec025` builds on `9525eb8` baseline). **Phase 9 results:** 6 `*_v1.6.json` immutable snapshots + 2 `*_v1.6.png` images written; raw dual-anchored intersection jumped 25/52 → **48/52 (92.3%)**, achieving Stretch Tier 1 (≥50%) AND Tier 2 (≥80%). Immutability invariant verified — `git diff HEAD` on 6 v1.5 phase JSONs = ZERO. **3 new RCA findings closed:** **F-RCA-12** — `phase4_bridge_registry.py` cannot safely re-run (no Phase 6/7 awareness); fixed via A.1+ workaround (new `phase4_graph_sync.py` injects 34 missing edges from registry MDs; manual gen of `phase4_registry_report_v1.6.json`). **F-RCA-13** — NetworkX `links` vs `edges` key inconsistency between phase1 (default `links`) and phase4_bridge_registry/phase5/phase6 (custom `edges`); fixed via defensive key detection in 3 scripts. **F-RCA-14** — `K_SIDE_TYPES` in phase2 was missing `BR_EX_BE_STRETCH` (Phase 7 edge type), causing intersection to stay at 25 instead of jumping to 48; fixed at `phase2_intersection_analysis.py:55`. All 6 phase scripts now accept `VVV_QMRF_EX_SUFFIX` env var (Option D-refined). Full audit: [`reviews/rca_plan_v1.6_completion_audit.md`](reviews/rca_plan_v1.6_completion_audit.md).

---

## 1. RCA Purpose

### 1.1 Define — Problem Statement

**Symptom:** VVV-QMRF currently operates within a closed scope: the K-side (registration-state layer) is defined internally through 52 `N_QM_VVV_XXXXX` nodes (codes 00001–00055; codes 00017, 00019, 00026 folded — actual count 52) and 115 `ED_QM_VVV_XXXXX` edges, with 15 `BR_XXXXX` bridge edges to Standard QM. However, the **relationship between K-side and ρ-side remains implicit** — scattered across individual node definitions and edge relations rather than systematically mapped as a unified expansion layer.

**Cause:** Two external bridge directions exist but have not been formally intersected:
- **Bridge 1 (BR_EX_BE_XXXXX):** Full 263 BE nodes → VVV-QMRF nodes (the completed 263-node audit cycle produced 19 draft bridge rows / 21 BIAN-support links, but these remain draft-only and unconnected to a systematic K-side ↔ ρ-side scope)
- **Bridge 2 (BR_EX_QM_XXXXX):** VVV-QMRF nodes → QM Standard nodes (15 `BR_XXXXX` bridge edges exist in v0.1, but systematic coverage of all VVV-QMRF nodes to their QM standard anchors is incomplete)

**Goal:** VVV-QMRF-EX systematically identifies how K-side registration concepts relate to ρ-side physical concepts by finding the **intersection** of these two bridge expansion directions at the VVV-QMRF graph.

### 1.2 Trace — 5 Whys

1. **Why is the K-side ↔ ρ-side relationship unclear?**
   Because each VVV-QMRF node's K-side/ρ-side boundary is defined locally in its own category file, not as a global graph property.

2. **Why is local definition insufficient?**
   Because cross-node patterns (e.g., which BE source concepts map to the same QM physical substrate via different VVV intermediaries) are invisible without a graph-level view.

3. **Why has graph-level analysis not been done?**
   Because the two bridge directions (BE→VVV, VVV→QM) were built in separate audit cycles and remain in separate registries.

4. **Why does intersection matter?**
   Because the intersection reveals which VVV-QMRF nodes are genuinely mediating between Buddhist epistemological source-analogues and Standard QM physical substrates — versus which are purely internal VVV constructions without clear external grounding on both sides.

5. **Root cause:** The project lacks a **unified directed multigraph** that combines all three graph layers (BE, VVV-QMRF, QM Standard) and the two inter-graph bridge edge sets, enabling systematic K-side ↔ ρ-side intersection analysis.

### 1.3 Fix — VVV-QMRF-EX Expansion

Create **VVV-QMRF-EX** as the systematic expansion layer that:
1. Constructs a unified multigraph using NetworkX
2. Computes intersection bridges via graph analysis
3. Uses similarity search to detect latent/implicit K-ρ connections
4. Documents results with context management for traceability

---

## 2. Architecture — Three-Graph Unified Model

### 2.1 Graph Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                    VVV-QMRF-EX Unified Multigraph               │
│                                                                 │
│  ┌──────────────┐    Bridge 1          ┌──────────────────────┐ │
│  │   BE System   │ ──BR_EX_BE_XXXXX──▶ │     VVV-QMRF         │ │
│  │  (263 nodes)  │    (K-side source)   │  (52 N_QM_VVV nodes) │ │
│  │  N_BE_00001-  │                      │  (115 internal edges)│ │
│  │  N_BE_00263   │                      │                      │ │
│  └──────────────┘                      └──────────────────────┘ │
│                                              │                   │
│                                     Bridge 2 │                   │
│                                  BR_EX_QM_XXXXX                 │
│                                   (ρ-side link)                 │
│                                              ▼                   │
│                                       ┌──────────────┐          │
│                                       │  QM Standard  │          │
│                                       │ (105 nodes)   │          │
│                                       │ N_QM_00001-   │          │
│                                       │ N_QM_00105    │          │
│                                       └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Node Inventory

| Layer | Node range | Count | Role in VVV-QMRF-EX |
|---|---|---|---|
| BE System | `N_BE_00001` – `N_BE_00263` | 263 | K-side source-analogue nodes (epistemological origin) |
| VVV-QMRF | `N_QM_VVV_00001` – `N_QM_VVV_00055` | 52 (3 codes unassigned: 00017, 00019, 00026) | Central mediating layer (K-side registration concepts) |
| QM Standard | `N_QM_00001` – `N_QM_00105` | 105 | ρ-side physical substrate nodes |

### 2.3 Edge Inventory

| Edge type | Code family | Count (current) | Direction | Source |
|---|---|---|---|---|
| VVV internal | `ED_QM_VVV_00001`–`ED_QM_VVV_00040` | 40 | VVV ↔ VVV | Phase 1, `edge_QM_VVV.md` |
| VVV → QM substrate | `ED_QM_VVV_00041`–`ED_QM_VVV_00100` | 60 | VVV → QM | Phase 2, `edge_QM_VVV.md` |
| VVV → BE source-analogue | `ED_QM_VVV_00101`–`ED_QM_VVV_00115` | 15 | VVV → BE | Phase 3, `edge_QM_VVV.md` |
| QM → VVV bridge (v0.1) | `BR_00001`–`BR_00015` | 13 graphable + 2 boundary guards = 15 registered | QM → VVV | `bridge_QM_standard_to_VVV_QMRF.md` |
| BE → VVV draft bridge | `BR_DRAFT_X_XXX` | 21 directed edges (from 19 unique proposals) | BE → VVV | 263-node audit cycle |

> **F8/F9/F10 Note:** `BR_00002` (Born Rule boundary guard) and `BR_00015` (non-replacement guard) use abstract K-side anchors, not specific `N_QM_VVV_XXXXX` node codes — Phase 1 graph loader correctly skips them as non-graphable. Draft bridge count uses all 21 directed edges including multi-BIAN duplicates. Total graph edge count = 40 + 60 + 15 + 13 + 21 = **149**. The per-type decomposition is now consistent with `phase1_validation_report.json`.

---

## 3. Bridge Expansion Direction 1: BR_EX_BE_XXXXX

### 3.1 Definition

**Bridge 1** creates formal edges from the full 263 BE nodes to VVV-QMRF nodes. This is the **K-side expansion** — it traces how each VVV registration concept draws from Buddhist epistemological source material.

### 3.2 Input Sources

| Source | Content | Status |
|---|---|---|
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Full 263-node BE SOT | Active, RCA-verified |
| 263-node audit cycle (Batches A–F) | Triage results: 177 evidence-only, 24 no-map, 32 candidate, 19 gate-passed | Complete |
| `edge_QM_VVV.md` Phase 3 | 15 existing VVV → BE source-analogue edges | Complete |
| Draft bridge registries (Batches B–F) | 19 unique draft bridge rows / 21 BIAN-support links | Draft only |

### 3.3 Expansion Scope

| Category | Count | Action in VVV-QMRF-EX |
|---|---|---|
| **Core 30 BE nodes** (`N_BE_00001`–`N_BE_00030`) | 30 | Map all 30 to VVV-QMRF nodes via existing Phase 3 edges + new BR_EX_BE edges |
| **Gate-passed candidates** (19 nodes) | 19 | Formalize 19 draft bridges into BR_EX_BE_XXXXX edges |
| **Evidence-layer nodes** (177 nodes) | 177 | Evaluate for secondary/indirect K-side support edges via similarity search |
| **No-map nodes** (24 nodes) | 24 | Exclude from bridge creation; retain as BE-internal only |
| **Remaining candidates** (13 not passed) | 13 | Re-evaluate with expanded VVV-QMRF-EX scope |

### 3.4 BR_EX_BE Schema

| Field | Definition |
|---|---|
| `Bridge ID` | `BR_EX_BE_XXXXX` (five digits) |
| `Direction` | `BE → VVV` |
| `BE Anchor` | `N_BE_XXXXX` (five-digit BE node) |
| `VVV-QMRF Anchor` | `N_QM_VVV_XXXXX` (five-digit VVV node) |
| `Bridge Relation` | One of: `source_analogue`, `structural_support`, `gap_source`, `conceptual_parallel`, `indirect_support` |
| `K-side Function` | How the BE concept contributes to K-side registration semantics |
| `Claim Type` | `source_analogue`, `evidence_support`, `interpretive_mapping` |
| `Boundary Guard` | What the bridge does NOT claim |
| `BIAN Target` | Which BIAN(s) this bridge supports, if any |
| `Source Evidence` | File path + line range |
| `NetworkX Weight` | Confidence score [0.0–1.0] from similarity analysis |
| `Status` | `proposed`, `checked`, `verified` |

### 3.5 Expected Output

- **Tier 1:** ~19 formalized BR_EX_BE edges (from gate-passed draft bridges)
- **Tier 2:** ~15 derived-copy source-analogue edges (referencing existing Phase 3 edges; originals remain frozen in `edge_QM_VVV.md`)
- **Tier 3:** ~30-50 secondary support edges (from evidence-layer similarity analysis)
- **Total estimated:** 64–84 BR_EX_BE edges

> **F2 — Direction Non-Reversal Note:** Phase 3 edges in `edge_QM_VVV.md` are stored as `VVV → BE source-analogue` (VVV node draws from BE source). BR_EX_BE_XXXXX schema uses field names `BE Anchor` and `VVV-QMRF Anchor` — these are **role labels, not direction indicators**. The semantic relation `source_analogue_of` is bidirectional in meaning but registered as `BE → VVV` in BR_EX_BE for K-side expansion clarity. **Derived-copy MUST NOT silently reverse direction without recording the rationale in the `Bridge Relation` field** (e.g., `source_analogue_of` preserves Phase 3 semantics regardless of registry-level direction notation).

---

## 4. Bridge Expansion Direction 2: BR_EX_QM_XXXXX

### 4.1 Definition

**Bridge 2** creates formal edges from VVV-QMRF nodes to QM Standard nodes. This is the **ρ-side expansion** — it traces how each VVV registration concept anchors to physical quantum measurement substrates.

### 4.2 Input Sources

| Source | Content | Status |
|---|---|---|
| `SYSTEM_Quantum_Measurement/system_qm_full.md` | Full 105-node QM SOT | Active, RCA-verified |
| `edge_QM_VVV.md` Phase 2 | 60 existing VVV → QM substrate edges | Complete |
| `bridge_QM_standard_to_VVV_QMRF.md` | 15 BR_XXXXX bridge edges (v0.1) | Checked |
| `node_QM_VVV.md` Section 2 "Existing QM nearest node" | QM anchors for all 52 VVV nodes | Complete |

### 4.3 Expansion Scope

| Category | Count | Action in VVV-QMRF-EX |
|---|---|---|
| **Existing BR_XXXXX bridges** | 15 | Reference-copy into unified BR_EX_QM registry (originals remain frozen in `bridge_QM_standard_to_VVV_QMRF.md`) |
| **Existing Phase 2 edges with bridge potential** | 60 | Evaluate which qualify for BR_EX_QM derived-copy (originals remain frozen in `edge_QM_VVV.md`) |
| **Unconnected VVV → QM paths** | ~10-15 | Discover via NetworkX shortest-path / similarity analysis |
| **QM nodes not yet bridged** | ~60-70 | Evaluate for indirect ρ-side substrate connections |

### 4.4 BR_EX_QM Schema

| Field | Definition |
|---|---|
| `Bridge ID` | `BR_EX_QM_XXXXX` (five digits) |
| `Direction` | `VVV → QM` or `QM → VVV` or `Boundary guard` |
| `VVV-QMRF Anchor` | `N_QM_VVV_XXXXX` or `ED_QM_VVV_XXXXX` |
| `QM Standard Anchor` | `N_QM_XXXXX` or `ED_QM_XXXXX` |
| `Bridge Relation` | From controlled whitelist: `physical_substrate_for`, `formal_substrate_for`, `probability_rule_preserved_by`, `boundary_input_to`, `registration_layer_extension_of`, `distinguishes_from`, `non_replacement_guard` |
| `ρ-side Function` | How the QM concept provides physical/formal grounding |
| `Claim Type` | `derived`, `interpretive_mapping`, `formal_model`, `boundary_guard` |
| `Boundary Guard` | What the bridge does NOT claim |
| `Source Evidence` | File path + line range |
| `NetworkX Weight` | Confidence score [0.0–1.0] from analysis |
| `Status` | `proposed`, `checked`, `verified` |

### 4.5 Expected Output

- **Tier 1:** 15 referenced BR_XXXXX edges (reference-copy from v0.1 bridge registry; originals remain frozen in `bridge_QM_standard_to_VVV_QMRF.md`)
- **Tier 2:** ~20-30 derived-copy Phase 2 edges (meeting bridge-level boundary/verification standards; originals remain frozen in `edge_QM_VVV.md`)
- **Tier 3:** ~10-15 newly discovered ρ-side connections (from graph analysis)
- **Total estimated:** 45–60 BR_EX_QM edges

---

## 5. Intersection Analysis — The Core of VVV-QMRF-EX

### 5.1 Intersection Definition

The **intersection** of Bridge 1 and Bridge 2 is the set of VVV-QMRF nodes that have:
- At least one **BR_EX_BE edge** (K-side source from BE), AND
- At least one **BR_EX_QM edge** (ρ-side anchor to QM Standard)

These intersection nodes are the **genuine K-ρ mediators** — VVV-QMRF concepts that simultaneously:
- Draw epistemological structure from Buddhist source-analogues (K-side)
- Anchor to Standard QM physical substrates (ρ-side)

### 5.2 NetworkX Implementation Plan

#### Phase A — Graph Construction

```python
import networkx as nx

# Create unified directed multigraph
G = nx.MultiDiGraph()

# Layer 1: Add BE nodes (263)
for node_id in range(1, 264):
    G.add_node(f"N_BE_{node_id:05d}", layer="BE", side="K")

# Layer 2: Add VVV-QMRF nodes (52 actual; codes span 00001-00055, gaps at 00017/00019/00026)
for node_id in VVV_NODE_LIST:
    G.add_node(f"N_QM_VVV_{node_id:05d}", layer="VVV", side="K-rho_mediator")

# Layer 3: Add QM Standard nodes (105)
for node_id in range(1, 106):
    G.add_node(f"N_QM_{node_id:05d}", layer="QM", side="rho")

# Add all edge types with attributes
# Phase 1: VVV internal (40 edges)
# Phase 2: VVV → QM (60 edges)
# Phase 3: VVV → BE source-analogue (15 edges)
# BR v0.1: QM → VVV bridges (15 edges)
# BR_DRAFT: BE → VVV draft bridges (19 edges)
```

#### Phase B — Intersection Discovery

```python
# Find VVV nodes with both K-side and ρ-side connections
intersection_nodes = []
for node in G.nodes():
    if G.nodes[node].get('layer') != 'VVV':
        continue
    
    # Check K-side: has incoming/outgoing edge to BE layer
    has_k_side = any(
        G.nodes[neighbor].get('layer') == 'BE'
        for neighbor in set(G.predecessors(node)) | set(G.successors(node))
    )
    
    # Check ρ-side: has incoming/outgoing edge to QM layer
    has_rho_side = any(
        G.nodes[neighbor].get('layer') == 'QM'
        for neighbor in set(G.predecessors(node)) | set(G.successors(node))
    )
    
    if has_k_side and has_rho_side:
        intersection_nodes.append(node)
```

#### Phase C — Centrality & Community Analysis

```python
# Betweenness centrality — which VVV nodes are strongest mediators?
bc = nx.betweenness_centrality(G)
top_mediators = sorted(
    [(n, bc[n]) for n in intersection_nodes],
    key=lambda x: x[1], reverse=True
)

# Community detection — are there natural clusters?
from networkx.algorithms import community
communities = sorted(
    community.greedy_modularity_communities(G.to_undirected()),
    key=lambda c: (-len(c), sorted(c))
)

# Shortest paths BE → VVV → QM — what are the most direct K-ρ chains?
for be_node in BE_BRIDGE_SOURCES:
    for qm_node in QM_BRIDGE_TARGETS:
        try:
            path = nx.shortest_path(G, be_node, qm_node)
            # Record paths passing through VVV layer
        except nx.NetworkXNoPath:
            pass
```

#### Phase D — Similarity Search (Latent Connection Discovery)

Using **Similarity Search Patterns**:

1. **Embedding Generation:** Generate semantic embeddings for:
   - All BE node definitions (from `system_be_full.md`)
   - All VVV-QMRF node definitions (from `node_QM_VVV.md`)
   - All QM Standard node definitions (from `system_qm_full.md`)

2. **Cross-layer Similarity:** Compute cosine similarity between:
   - Each BE node embedding ↔ each VVV-QMRF node embedding
   - Each VVV-QMRF node embedding ↔ each QM Standard node embedding
   - Each BE node embedding ↔ each QM Standard node embedding (control — should be weak for most pairs)

3. **Threshold-based Bridge Candidates:**
   - Similarity ≥ 0.75: Strong bridge candidate → propose as Tier 1 BR_EX edge
   - Similarity 0.50–0.74: Moderate candidate → propose as Tier 2 evidence support
   - Similarity 0.30–0.49: Weak candidate → flag for manual review
   - Similarity < 0.30: No bridge → exclude

4. **Latent Gap Detection:**
   - Find VVV-QMRF nodes with high QM similarity but NO existing BE analogue → K-side gap
   - Find VVV-QMRF nodes with high BE similarity but NO existing QM anchor → ρ-side gap
   - These gaps are **expansion targets** for VVV-QMRF-EX

### 5.3 Expected Intersection Results

Based on the existing Phase 3 edges (15 VVV → BE source-analogue) and Phase 2 edges (60 VVV → QM), the current intersection includes at least these VVV-QMRF nodes:

| VVV Node | K-side (BE source-analogue) | ρ-side (QM substrate) | K-ρ Mediator Role |
|---|---|---|---|
| `N_QM_VVV_00001` | Apoha (N_BE_00015) | No-Result Measurement (N_QM_00033) | Contrapositive evidence: exclusion-based (K) ↔ null-measurement (ρ) |
| `N_QM_VVV_00004` | Apoha (N_BE_00015) | No-Result Measurement (N_QM_00033) | Informative silence: valid absence (K) ↔ null detection (ρ) |
| `N_QM_VVV_00006` | Apoha (N_BE_00015) | Post-Measurement Update (N_QM_00022) | Exclusion-based selection: meaning-by-exclusion (K) ↔ state update (ρ) |
| `N_QM_VVV_00020` | Apoha/Anupalabdhi (N_BE_00015) | No-Result Measurement (N_QM_00033) | Validated absence: non-perception (K) ↔ null measurement (ρ) |
| `N_QM_VVV_00025` | Svabhāvapratibandha (N_BE_00021) | Entanglement (N_QM_00047) | Intrinsic relational binding: essential relation (K) ↔ non-separability (ρ) |
| `N_QM_VVV_00027` | Arthakriyā (N_BE_00022) | Measurement (N_QM_00019) | Self-completion matrix: causal efficacy (K) ↔ physical measurement (ρ) |
| `N_QM_VVV_00029` | Pramāṇa/Bādhaka (N_BE_00001) | Measurement Reversal (N_QM_00102) | Retroactive override: sublating cognition (K) ↔ physical reversal (ρ) |
| `N_QM_VVV_00032` | Bhrānti (N_BE_00006) | Decoherence (N_QM_00095) | Registration error: erroneous cognition (K) ↔ noise/decoherence (ρ) |
| `N_QM_VVV_00033` | Svasaṃvedana (N_BE_00011) | von Neumann Model (N_QM_00020) | Self-certifying registration: reflexive awareness (K) ↔ measurement chain (ρ) |
| `N_QM_VVV_00039` | Kṣaṇabhaṅgavāda (N_BE_00029) | Heisenberg Cut (N_QM_00094) | Process framework: momentariness (K) ↔ quantum-classical boundary (ρ) |
| `N_QM_VVV_00042` | Trairūpya (N_BE_00018) | System-Meter Coupling (N_QM_00021) | Tripartite validity: triple-condition syllogism (K) ↔ physical coupling (ρ) |
| `N_QM_VVV_00044` | Nirvikalpaka Pratyakṣa (N_BE_00009) | System-Meter Coupling (N_QM_00021) | Pre-symbolic stratum: non-conceptual perception (K) ↔ physical interaction (ρ) |
| `N_QM_VVV_00048` | Yogipratyakṣa (N_BE_00012) | Weak Measurement (N_QM_00028) | Limit-faculty registration: yogic perception (K) ↔ weak measurement (ρ) |
| `N_QM_VVV_00051` | Kṣaṇabhaṅgavāda (N_BE_00029) | Quantum Jump Operator (N_QM_00042) | Temporal discontinuity: momentariness (K) ↔ quantum jumps (ρ) |
| `N_QM_VVV_00054` | Saṃśaya (N_BE_00007) | Superposition (N_QM_00005) | Pre-measurement indeterminacy: doubt (K) ↔ superposition (ρ) |

**Predicted intersection:** 15 nodes with explicit K-ρ dual anchoring. VVV-QMRF-EX expansion targets the remaining ~40 VVV nodes that currently lack one or both anchors.

---

## 6. Context Management Strategy

### 6.1 Context Extraction

Using the **Context Management** skill, VVV-QMRF-EX will maintain:

| Context artifact | Content | Storage |
|---|---|---|
| `vvv_qmrf_ex_graph.json` | NetworkX graph serialized as node-link JSON | `vvv-qmrf-ex/data/` |
| `vvv_qmrf_ex_intersection.md` | Intersection analysis results | `vvv-qmrf-ex/` |
| `br_ex_be_registry.md` | Bridge 1 full registry | `vvv-qmrf-ex/` |
| `br_ex_qm_registry.md` | Bridge 2 full registry | `vvv-qmrf-ex/` |
| `vvv_qmrf_ex_similarity_matrix.csv` | Cross-layer similarity scores | `vvv-qmrf-ex/data/` |
| `vvv_qmrf_ex_centrality.csv` | Betweenness centrality scores | `vvv-qmrf-ex/data/` |
| `vvv_qmrf_ex_gaps.md` | K-side and ρ-side gap analysis | `vvv-qmrf-ex/` |

### 6.2 Context Fingerprint

```json
{
  "project_name": "VVV-QMRF-EX",
  "version": "0.1-plan",
  "context_fingerprint": "qmrf-ex-2026-05-20",
  "captured_at": "2026-05-20T13:41:00+07:00",
  "architectural_decisions": [
    {
      "decision_type": "graph_model",
      "rationale": "MultiDiGraph allows multiple edges between same node pair (e.g., a VVV node can have both grounded_by and extends edges to the same QM node)",
      "impact_score": 5.0
    },
    {
      "decision_type": "intersection_first",
      "rationale": "Identify K-ρ intersection nodes before expanding bridges — ensures expansion is grounded, not speculative",
      "impact_score": 4.5
    },
    {
      "decision_type": "similarity_threshold",
      "rationale": "0.75 threshold for auto-bridge proposal prevents false positives while capturing strong structural parallels",
      "impact_score": 4.0
    }
  ]
}
```

---

## 7. Execution Phases

### Phase 0 — Environment Setup (Estimated: 0.5 session) — Added by F6 RCA fix

> **Purpose:** Verify all execution dependencies BEFORE Phase 1 to prevent mid-flight import failures.

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 0.1 | Verify Python version | `python --version` | Version string | `Python ≥ 3.10` |
| 0.2 | Install core dependencies | `pip install "networkx>=3.0" "sentence-transformers>=2.2" "numpy>=1.24" "pandas>=2.0" "matplotlib>=3.7"` | Installed packages | `pip list` shows all targets |
| 0.3 | Smoke test NetworkX | `python -c "import networkx as nx; G = nx.MultiDiGraph(); G.add_node('test'); print(len(G.nodes()))"` | Output `1` | Exit code 0 |
| 0.4 | Smoke test sentence-transformers | `python -c "from sentence_transformers import SentenceTransformer; m = SentenceTransformer('all-mpnet-base-v2'); print(m.get_sentence_embedding_dimension())"` | Output `768` | Exit code 0 (first run downloads model — internet required) |
| 0.5 | Record environment manifest | `pip freeze > vvv-qmrf-ex/data/env_manifest.txt` | `env_manifest.txt` with all package versions | File exists, non-empty |
| 0.6 | Initialize data directory | `mkdir vvv-qmrf-ex/data` (if not exists) | Directory ready | `data/` directory exists |

**Phase 0 blocking condition:** If any step 0.1–0.4 fails → STOP. Resolve env issue before Phase 1. Do **NOT** proceed to Phase 1 with partial env.

---

### Phase 1 — Graph Construction (Estimated: 1 session)

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 1.1 | Parse BE SOT into NetworkX nodes | `system_be_full.md` | 263 BE nodes with attributes | Node count = 263 |
| 1.2 | Parse VVV-QMRF nodes | `node_QM_VVV.md` | 52 VVV nodes with attributes | Node count = 52 (codes span 00001–00055; 3 folded: 00017, 00019, 00026) |
| 1.3 | Parse QM Standard nodes | `system_qm_full.md` | 105 QM nodes with attributes | Node count = 105 |
| 1.4 | Parse all existing edges | `edge_QM_VVV.md`, `bridge_QM_standard_to_VVV_QMRF.md`, draft bridges | 115 + 15 + 19 = 149 edges | Edge count = 149 |
| 1.5 | Construct unified MultiDiGraph | All parsed data | `vvv_qmrf_ex_graph.json` | Graph connected components check |
| 1.6 | Validate graph integrity | Cross-reference with SOT files | Validation report | **Zero dangling edge references** (every edge endpoint resolves to an existing node). Orphan nodes are **permitted at this phase** — they are gap-fill targets for Phase 4, not Phase 1 failures (per F3 RCA fix). |

### Phase 2 — Intersection Analysis (Estimated: 1 session)

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 2.1 | Compute intersection nodes | Unified graph | List of VVV nodes with dual K-ρ anchoring | ≥15 intersection nodes expected |
| 2.2 | Compute betweenness centrality | Unified graph | Ranked mediator list | Top mediators align with E1-E16 core postulates |
| 2.3 | Detect community structure | Unified graph (undirected) | BIAN-cluster alignment | Top-N non-singleton communities should roughly map to BIAN groups; total community count is dominated by orphan BE nodes and is not a quality metric |
| 2.4 | Compute shortest paths BE→QM | Unified graph | Path catalog through VVV layer | All paths route through VVV (no direct BE→QM) |
| 2.5 | Identify K-side gaps | Intersection analysis | VVV nodes without BE anchoring | Gap list for Bridge 1 expansion |
| 2.6 | Identify ρ-side gaps | Intersection analysis | VVV nodes without QM anchoring | Gap list for Bridge 2 expansion |

### Phase 3 — Similarity Search (Estimated: 1-2 sessions)

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 3.1 | Generate node definition embeddings using **`sentence-transformers/all-mpnet-base-v2`** (768-dim, English-optimized, local, free). Alternative: `text-embedding-3-large` (3072-dim, OpenAI, multilingual) for Sanskrit/Pāli-origin terms if needed. Model name + version + dim **MUST** be recorded into `vvv_qmrf_ex_context.json` for reproducibility (F4 RCA fix). | All SOT node definitions (English text only) | Embedding vectors for 420 nodes (dim = 768 or 3072) | Embedding dimension consistency + model version recorded |
| 3.2 | Compute BE ↔ VVV similarity matrix | BE embeddings, VVV embeddings | 263 × 52 similarity matrix | Matrix shape = (263, 52) |
| 3.3 | Compute VVV ↔ QM similarity matrix | VVV embeddings, QM embeddings | 52 × 105 similarity matrix | Matrix shape = (52, 105) |
| 3.4 | Apply threshold filter | Similarity matrices | Candidate bridge lists (Tier 1/2/3) | Tier 1 candidates ≤ 50% of total |
| 3.5 | Cross-reference with existing edges | Candidate lists vs existing edges | New candidate edges not yet in graph | No duplicates with existing edges |
| 3.6 | Manual review of top candidates | Candidate lists with confidence scores | Approved new BR_EX edges | Each edge passes boundary check |

### Phase 4 — Bridge Registry Construction (Estimated: 1-2 sessions)

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 4.1 | Formalize BR_EX_BE edges | Phase 2-3 results | `br_ex_be_registry.md` | Schema compliance check |
| 4.2 | Formalize BR_EX_QM edges | Phase 2-3 results | `br_ex_qm_registry.md` | Schema compliance check |
| 4.3 | Update unified graph | New BR_EX edges | Updated `vvv_qmrf_ex_graph.json` | Re-run intersection analysis |
| 4.4 | Generate K-ρ relationship report | Intersection + centrality | `vvv_qmrf_ex_intersection.md` | All intersection nodes documented |
| 4.5 | Gap analysis report | Missing anchors | `vvv_qmrf_ex_gaps.md` | Gaps classified as K-gap vs ρ-gap |

### Phase 5 — Visualization & Validation (Estimated: 1 session)

| Step | Action | Input | Output | Verification |
|---|---|---|---|---|
| 5.1 | Generate graph visualization | Unified graph | Publication-quality network diagram | All three layers visually distinct |
| 5.2 | K-ρ heatmap | Intersection analysis | BIAN-grouped K-ρ strength heatmap | Heatmap covers all 19+ BIANs |
| 5.3 | Bridge coverage report | Both registries | Coverage statistics per VVV node | ≥80% VVV nodes have dual anchoring |
| 5.4 | Boundary compliance audit | All new bridges | Boundary check results | Zero overclaim violations |
| 5.5 | Context save | All VVV-QMRF-EX artifacts | Final context snapshot | Reproducible from saved context |

---

### Phase Report Immutability Rule (F-RCA-01 — added v1.5)

> **Rule:** Once a phase completes and writes `data/phase{N}_*.json`, that file is **immutable**. Later phases that re-compute the same metrics MUST write to a new filename (e.g., `data/phase{N}_*_post_phase{M}.json` where M > N).
>
> **Why:** Phase 2's `phase2_intersection_report.json` was overwritten with post-Phase 6 metrics (RCA Audit F-RCA-01), destroying the Phase 4-era baseline (16 intersection nodes) and replacing it with post-Phase 6 state (25 nodes). The baseline was only recoverable via git history (commit `2bffc3f`).
>
> **Enforcement:**
> 1. Every phase JSON MUST include a `"snapshot_phase"` field declaring which phase the data reflects (e.g., `"phase2_baseline"`, `"post_phase6"`, `"phase5_frozen"`).
> 2. Re-runs of an earlier phase script after a later phase has executed MUST write to a new file, not overwrite.
> 3. If a script needs to update post-hoc, it MUST include a `"snapshot_note"` explaining what changed and why.

---

## 8. Isolation Protocol — VVV-QMRF Core Protection

> **Purpose:** Ensure VVV-QMRF-EX expansion cannot corrupt or modify the existing VVV-QMRF core.

### Rule I-1: READ-ONLY Contract

VVV-QMRF-EX **MUST NOT** modify any file outside of `documents/research_documents/vvv-qmrf-ex/`.

| Protected file / directory | Protection level |
|---|---|
| `vvv-qmrf/node_QM_VVV.md` | 🔒 FROZEN — no add/delete/modify nodes |
| `vvv-qmrf/edge_QM_VVV.md` | 🔒 FROZEN — no add/delete/modify edges |
| `vvv-qmrf/bridge_QM_standard_to_VVV_QMRF.md` | 🔒 FROZEN — no migrate, reference-copy only |
| `vvv-qmrf/schema_guide.md` | 🔒 FROZEN |
| `vvv-qmrf/dictionary.md` | 🔒 FROZEN |
| `SYSTEM_Buddhist_Epistemology/*` | 🔒 FROZEN |
| `SYSTEM_Quantum_Measurement/*` | 🔒 FROZEN |
| `category/*` | 🔒 FROZEN |
| `framework/*` | 🔒 FROZEN |

### Rule I-2: Copy-Not-Move

- **"Reference-copy"** replaces "migrate": BR_EX_QM registry **references** BR_XXXXX edges by ID; originals remain in `bridge_QM_standard_to_VVV_QMRF.md`.
- **"Derived-copy"** replaces "promote": BR_EX registries **derive-copy** Phase 2/3 edges with added boundary fields; originals remain in `edge_QM_VVV.md`.

### Rule I-3: Namespace Isolation

VVV-QMRF-EX uses exclusively:
- `BR_EX_BE_XXXXX` (Bridge 1 edges)
- `BR_EX_QM_XXXXX` (Bridge 2 edges)

VVV-QMRF-EX **MUST NOT** create:
- `N_QM_VVV_XXXXX` (VVV nodes — only VVV-QMRF core can)
- `ED_QM_VVV_XXXXX` (VVV edges — only VVV-QMRF core can)
- `BR_XXXXX` (v0.1 bridges — only VVV-QMRF core can)
- `N_BE_XXXXX` (BE nodes — only BE System can)
- `N_QM_XXXXX` (QM nodes — only QM System can)

### Rule I-4: Rollback = Delete Directory

If VVV-QMRF-EX is abandoned or fails:
- **Action:** `DELETE documents/research_documents/vvv-qmrf-ex/`
- **Result:** No other file is affected. VVV-QMRF remains fully intact.

### Rule I-5: Promotion Gate (EX → Core)

If VVV-QMRF-EX results prove valuable and user approves:
1. New BR_EX edges may be **selectively copied** into `bridge_QM_standard_to_VVV_QMRF.md` as new `BR_XXXXX` entries.
2. This requires **separate RCA approval** — not automatic.
3. VVV-QMRF-EX does **NOT** auto-merge into VVV-QMRF.

---

## 9. Boundary Controls

| Control | Rule | Enforcement |
|---|---|---|
| No BE-QM identity | All bridges are structural analogies, not identity claims | Every BR_EX edge requires `Boundary Guard` field |
| No new QM law | No bridge creates new physical formalism | QM Standard nodes are read-only anchors |
| No automatic E17+ | No bridge automatically creates new VVV-QMRF postulates | Postulate creation requires separate RCA gate |
| No replacement claim | VVV-QMRF-EX does not replace Standard QM | Global `non_replacement_guard` applies to all BR_EX_QM edges |
| Born Rule preserved | No bridge modifies `p_QM(o)` | `BR_EX_QM_00002` (referenced from BR_00002) enforces this |
| Source traceability | Every bridge edge traces to a specific SOT line | `Source Evidence` field is mandatory |
| Reproducibility | All analysis is reproducible from saved NetworkX graph | `vvv_qmrf_ex_graph.json` is the serialized source |

---

## 10. Success Criteria

### 10.1 Dual-Criterion Success Framework (F-RCA-02 — adopted v1.5)

> **Root cause of revision:** Plan v1.4 had two metrics in tension — raw dual-anchored % (§10.1 stage table) vs. effective coverage with exceptions (§10.2 F15 row). After Phase 6, the raw metric reached 48.1% (25/52) — 1.9pt below the ≥50% Phase 5 stretch target — while effective coverage reached 100%. Plan v1.4 silently marked Phase 5/6 ✅ without picking which metric was authoritative. RCA Audit F-RCA-02 (3-round decision, scoring 5.0/5) selected the **dual-criterion framework**: raw measures *quality of automated discovery*; effective measures *completeness of expansion scope*. Both have legitimate roles and must coexist with explicit pass thresholds.
>
> **Authoritative success criterion (v1.5):** Phase 5/6 PASS = **Primary MET AND Secondary MET**.

#### 10.1.1 Primary Criterion — Completeness (Effective Coverage)

| Stage | Target | Method | Status |
|---|---|---|---|
| **Phase 5 — Completeness** | K-effective ≥80% AND ρ-effective ≥80% | Cover via BR_EX_BE/BR_EX_QM edges OR formal structural exception (KE-QI / KE-OF / KE-SC for K-side; RE-BI for ρ-side per F15) | ✅ K-effective **100%** (25 covered + 27 excepted), ρ-effective **100%** (51 covered + 1 excepted) |

#### 10.1.2 Secondary Criterion — Discovery Quality (Raw Dual-Anchored)

| Stage | Target | Method | Status |
|---|---|---|---|
| **Phase 4 (baseline)** | Measurement only | Automated graph + Phase 3 similarity (cosine ≥0.50) | ✅ 30.8% (16/52) — establishes achievable floor |
| **Phase 5 — Discovery quality** | Raw dual-anchored ≥30% | Phase 4 baseline + Phase 3 Tier2 promotion + targeted Phase 6 expert mapping | ✅ **48.1% (25/52)** — exceeds floor; closes 9 KE-PM exceptions |
| **Stretch — Raw ≥50%** | ≥26 nodes raw dual-anchored | Continued expert mapping of KE-OF operator decomposition + KE-SC parent inheritance | ⏳ Future work (not a gate) |
| **Stretch — Raw ≥80%** | ≥42 nodes raw dual-anchored | Full domain expert mapping campaign | ⏳ Future work (not a gate) |

#### 10.1.3 Anti-Gaming Guards

The dual-criterion framework is guarded against metric abuse by:
1. **F15 structural exception requirement** — every K-gap exception MUST be classified as KE-QI (QM-intrinsic), KE-OF (operator formalism), or KE-SC (sub-concept of a covered parent). Adding "KE-misc" or "KE-pending" without structural rationale violates the framework.
2. **Per-node coverage criteria (§10.2 F5/F15)** — every VVV node must have ≥1 BR_EX_BE OR be on approved K-gap exception list; same for ρ-side. Prevents bulk-marking nodes as "excepted" to hit primary criterion.
3. **Raw ≥30% floor** — secondary criterion cannot drop below the Phase 4 automated baseline. Prevents regression by manual node removal.

### 10.2 Other Success Criteria

| Criterion | Target | Measurement |
|---|---|---|
| **Bridge 1 coverage** | ≥30 BR_EX_BE edges (K-side) | Count of formalized BR_EX_BE edges — **actual: 46** ✅ (37 from Phase 4 + 9 from Phase 6 expert mapping BR_EX_BE_00038–00046) |
| **Bridge 2 coverage** | ≥30 BR_EX_QM edges (ρ-side) | Count of formalized BR_EX_QM edges — **actual: 74** ✅ |
| **Per-node K-side coverage (F5/F15)** | Every VVV node has ≥1 BR_EX_BE edge OR is on the approved K-gap exception list (`vvv-qmrf-ex/k_gap_exception_list.md`) | For each VVV node: `count(BR_EX_BE incident) ≥ 1` OR `node_id ∈ approved_K_gap_list` |
| **Per-node ρ-side coverage (F5/F15)** | Every VVV node has ≥1 BR_EX_QM edge OR is on the approved ρ-gap exception list (`vvv-qmrf-ex/rho_gap_exception_list.md`) | For each VVV node: `count(BR_EX_QM incident) ≥ 1` OR `node_id ∈ approved_rho_gap_list` |
| **Boundary compliance** | 100% pass rate | Zero overclaim violations in audit |
| **Graph integrity** | Zero orphan VVV nodes after Phase 4 (orphans permitted during Phase 1; see Step 1.6) | All VVV nodes reachable from at least one other layer post-expansion |
| **Context saved** | All artifacts serialized and recoverable | Context restore test |
| **Embedding reproducibility (F4)** | Model name + version + dim recorded in context.json | Inspect `vvv_qmrf_ex_context.json["embedding_model"]` |
| **Ghost entry prevention (F11/F12)** | Zero registry entries with empty mandatory fields | Validate all BR_EX entries have non-empty BE/VVV/QM Node + Direction + Confidence |

---

## 11. File Structure

```
documents/research_documents/vvv-qmrf-ex/
├── vvv-qmrf-ex-plan.md                     ← This document
├── ex_schema_addendum.md                     ← BR_EX_* namespace declaration (F1, EX-local)
├── br_ex_be_registry.md                      ← Bridge 1 registry (K-side) — 46 entries
├── br_ex_qm_registry.md                      ← Bridge 2 registry (ρ-side) — 74 entries
├── vvv_qmrf_ex_intersection.md               ← Intersection analysis report
├── vvv_qmrf_ex_gaps.md                       ← K-side and ρ-side gap report
├── vvv_qmrf_ex_boundary_audit.md             ← Boundary compliance audit (Phase 6 Final)
├── k_gap_exception_list.md                    ← F15: Approved K-gap exceptions (Phase 6 Final)
├── rho_gap_exception_list.md                  ← F15: Approved ρ-gap exceptions (Phase 6 Final)
└── data/
    ├── env_manifest.txt                       ← pip freeze output (F6)
    ├── vvv_qmrf_ex_graph.json                ← Serialized NetworkX multigraph (420 nodes, 160 edges)
    ├── vvv_qmrf_ex_similarity_be_vvv.csv     ← BE ↔ VVV similarity matrix (263×52)
    ├── vvv_qmrf_ex_similarity_vvv_qm.csv     ← VVV ↔ QM similarity matrix (52×105)
    ├── vvv_qmrf_ex_centrality.csv            ← Betweenness centrality scores
    └── vvv_qmrf_ex_context.json              ← Context management snapshot (incl. embedding model name + version per F4; edge_count=160 per Phase 6)
```

### 11.1 Namespace Declaration — F1 RCA Fix (EX-local, schema_guide.md remains frozen)

> **Problem solved:** `schema_guide.md` is frozen (Rule I-1) and does NOT declare `BR_EX_BE_XXXXX` / `BR_EX_QM_XXXXX` namespaces. Per Rule Zero, modifying `schema_guide.md` would treat the symptom (need to declare namespace) by violating isolation. Instead, declare namespace **inside VVV-QMRF-EX** scope only.

**Implementation:** Create new file `vvv-qmrf-ex/ex_schema_addendum.md` containing:

1. **Namespace declaration:**
   - `BR_EX_BE_XXXXX` — five-digit, BE → VVV bridge edge, EX-only
   - `BR_EX_QM_XXXXX` — five-digit, VVV ↔ QM bridge edge, EX-only
2. **Full field schemas** (mirroring Section 3.4 and Section 4.4 of this plan — self-contained, no `schema_guide.md` reference)
3. **Controlled vocabulary** for `Bridge Relation` field (whitelist from Sections 3.4 and 4.4)
4. **Cross-reference declaration:** `ex_schema_addendum.md` is the authoritative schema for `br_ex_be_registry.md` and `br_ex_qm_registry.md`. `schema_guide.md` remains the authoritative schema for VVV-QMRF core artifacts and is **not modified**.
5. **Promotion gate clause:** If EX results are promoted to core (Rule I-5), the corresponding new `BR_XXXXX` entries in `bridge_QM_standard_to_VVV_QMRF.md` require a **separate** RCA gate that may extend `schema_guide.md` — but this is downstream of VVV-QMRF-EX scope.

---

## 12. Dependencies and Prerequisites

| Prerequisite | Status | Blocking? |
|---|---|---|
| 263-node audit cycle complete | ✅ Complete | No |
| BR v0.1 bridge registry complete | ✅ Complete (15 edges) | No |
| VVV-QMRF edge registry complete | ✅ Complete (115 edges) | No |
| VVV-QMRF node registry complete | ✅ Complete (52 nodes; codes span 00001–00055, 3 folded: 00017, 00019, 00026) | No |
| BIAN-14 structural review | ⏳ Pending (open item #1) | Non-blocking — proceed with conditional retention |
| Final BR_XXXXX ID assignment | ⏳ Deferred (open item #2) | Non-blocking — use draft IDs until finalized |
| Python + NetworkX + sentence-transformers env | ✅ Verified during Phase 0 (F6 RCA fix) | No longer blocking |
| EX schema addendum (`ex_schema_addendum.md`) | ✅ Created during Phase 4 (F1 RCA fix) | No longer blocking |
| F8–F15 RCA fixes applied | ✅ Applied in v1.3 | No longer blocking |
| Gap exception lists (`k_gap_exception_list.md`, `rho_gap_exception_list.md`) | ✅ Created during Phase 5 (F15 RCA fix) | No longer blocking |

---

## 13. Recommended Next RCA Step

1. ~~**User approves Plan v1.1** — proceed to Phase 0~~ ✅ Done
2. ~~**Execute Phase 0** — verify Python ≥3.10, install dependencies~~ ✅ Done
3. ~~**Execute Phase 1** — construct unified multigraph~~ ✅ Done (420 nodes, 149 edges)
4. ~~**Execute Phase 2** — run intersection analysis~~ ✅ Done (16 intersection nodes)
5. ~~**Execute Phase 3** — generate embeddings and similarity search~~ ✅ Done (0 Tier1, 15 Tier2)
6. ~~**Execute Phase 4** — formalize BR_EX_BE / BR_EX_QM registries~~ ✅ Done (Phase-4-baseline: 37 BE + 74 QM = 111 registry entries; 151 graph edges. Post-Phase 6: 46 + 74 = 120 entries; post-Phase 7: 69 + 74 = 143 entries)
7. ~~**Apply F8–F15 RCA fixes** — ghost entries, edge accounting, success criteria, context.json~~ ✅ Done (plan v1.3)
8. ~~**Execute Phase 5** — visualization + validation~~ ✅ Done — at time of Phase 5 (pre-Phase 6): boundary audit PASS 0/111 violations; K-effective 82.7% (43/52 = 16 covered + 27 structural exceptions; 9 KE-PM still pending); ρ-effective 100% (51 covered + 1 RE-BI); raw dual-anchored 30.8% (16/52); network diagram + heatmap + coverage report generated. *Note: numbers later updated to post-Phase 6 state in `phase5_coverage_report.json` — see RCA Audit F-RCA-05 / F-RCA-08; historical baseline preserved here.*
9. ~~**Execute Phase 6** — domain expert mapping of 9 KE-PM nodes~~ ✅ Done (9/9 KE-PM resolved → KE-RESOLVED; raw dual-anchored rose to 25/52 = **48.1%**; K-effective 100% (25 covered + 27 structural exceptions); BR_EX_BE_00038–00046 created; 160 graph edges)
10. ~~**EXPANSION COMPLETE** — all phases executed; all KE-PM nodes resolved; 0 pending items~~ ✅ Done under dual-criterion framework (§10.1): **Primary (Completeness): K-effective 100%, ρ-effective 100% ≥80% ✅**; **Secondary (Discovery quality): Raw 48.1% ≥30% floor ✅**. Stretch targets raw ≥50% / ≥80% are future work, not gates.
11. ~~**Apply F-RCA-01/02 BLOCKING fixes**~~ ✅ Done (plan v1.5) — Phase 2 baseline restored from git; dual-criterion framework adopted in §10.1; `snapshot_phase` field added to all 7 phase JSONs; §7 immutability rule added.

---

## 14. v1.6 Stretch Expansion Plan — Phases 7–10 (PHASES 7–8 COMPLETED; PHASES 9–10 PENDING)

> **Document type:** Forward-looking RCA expansion (not yet executed).
> **Status gate:** Phases 7–8 are COMPLETED as of 2026-05-20. Phase 7 evidence: `phase7_candidate_pool.md`, `phase7_ke_of_rca_log.md`, `phase7_ke_sc_rca_log.md`, `br_ex_be_registry.md` entries `BR_EX_BE_00047`–`BR_EX_BE_00069`, `k_gap_exception_list.md` `KE-RESOLVED-STRETCH` updates, and `ex_schema_addendum.md` v1.1 vocabulary update. Phase 8 evidence: `reviews/phase8_audit_closure_report.md` and `data/phase8_boundary_audit_report.json` (`entries_audited: 143`, `violations: 0`, `overall: PASS`). Phases 9–10 remain pending because no `_v1.6` immutable re-run snapshots or final completion audit are present yet.
> **Authority:** This section EXTENDS Plan v1.5 — it does not overwrite §7, §10, or §13. Phase 7 execution evidence is recorded in-place per "extend, not overwrite" rule.

### 14.1 RCA Purpose (v1.6)

**Symptom:** Plan v1.5 closed "EXPANSION COMPLETE" at raw dual-anchored 48.1% (25/52), 1.9pt below the §10.1.2 Stretch Tier 1 target (≥50%) and 31.9pt below Stretch Tier 2 (≥80%). 23 nodes remain structurally excepted (13 KE-OF + 10 KE-SC), retaining 100% effective coverage but without direct BR_EX_BE anchors.

**Cause:** Phase 6 prioritized 9 KE-PM nodes (highest blocker — no parent inheritance, no structural rationale). KE-OF (operator-formalism) and KE-SC (sub-concept-of-parent) were deferred to "Future work" because Primary Completeness was already 100%.

**5 Whys:**
1. Raw dual-anchored stuck at 48.1% → 23 nodes never got direct BR_EX_BE
2. Why not direct? → Phase 6 scope was KE-PM only (`KE-PM` was the labelled blocker)
3. Why was KE-OF/KE-SC labelled "Future work"? → §10.1.2 defined them as stretch, not gate
4. Why is stretch needed now? → User requested update based on expansion results + audit findings; publication readiness benefits from raw discovery quality lift
5. **Root cause:** v1.5 lacks a Phase 7+ execution loop for KE-OF/KE-SC promotion; lacks an audit-closure Phase 8 for the 5 unresolved findings (F-RCA-05/07/08/09/10/11).

**Fix:** Define Phase 7 (Stretch mapping), Phase 8 (Audit closure), Phase 9 (Full re-run), Phase 10 (Doc sync). All re-runs write to NEW filenames with `_v1.6` suffix per §7 v1.5 immutability rule.

### 14.2 Decision Parameters (User-confirmed 2026-05-20)

| Q | Question | Answer | Rationale |
|---|---|---|---|
| Q1 | Approval granularity | **Batch per category** | Reduces user interaction overhead; 2 batches (KE-OF, KE-SC) instead of 23 |
| Q2 | RCA threshold | **Split: KE-OF=4.5/5, KE-SC=3.5/5** | KE-OF requires strict semantic fidelity (operator → BE concept is non-trivial); KE-SC has parent K-coverage as fallback so lower bar acceptable |
| Q3 | Output files | **Split into 2 logs** | `phase7_ke_of_rca_log.md` + `phase7_ke_sc_rca_log.md` — separate audit trails per category |

**3-round rejection protocol (applied to BOTH categories):**
- Round 1 → Round 2 → Round 3, each round proposes a distinct BE candidate from BE SOT
- Accept if score ≥ threshold (4.5 for KE-OF, 3.5 for KE-SC) at any round
- After 3 unsuccessful rounds → node tagged `KE-{OF,SC}-RCA-REJECTED-3R`, remains in exception list with full 3-round log appended

### 14.3 Phase 7 — Stretch Expert Mapping (KE-OF + KE-SC promotion) ✅ COMPLETED

**Completion date:** 2026-05-20

**Execution result:** 23/23 target nodes accepted and registered. KE-OF accepted 13/13 at threshold 4.5/5; KE-SC accepted 10/10 at threshold 3.5/5. No `REJECTED-NO-POOL`, `KE-OF-RCA-REJECTED-3R`, or `KE-SC-RCA-REJECTED-3R` nodes were created.
| Step | Description | Output artifact |
|---|---|---|
| 7.0 | ✅ DONE — Built candidate pool ≥3 per node from `SYSTEM_Buddhist_Epistemology/system_be_full.md` (BE SOT). No node tagged `REJECTED-NO-POOL` | `phase7_candidate_pool.md` |
| 7.1 | ✅ DONE — RCA gate per KE-OF node (13 nodes, threshold 4.5/5, 3-round protocol). Result: 13/13 accepted, all Round 1 | `phase7_ke_of_rca_log.md` |
| 7.2 | ✅ DONE — RCA gate per KE-SC node (10 nodes, threshold 3.5/5, 3-round protocol). Result: 10/10 accepted; 6 Round 1, 4 Round 2 | `phase7_ke_sc_rca_log.md` |
| 7.3 | ✅ DONE — Boundary-guard pre-check applied to every accepted entry. Claim class remains `interpretive_mapping`; no identity claim accepted | inline in 7.1/7.2 logs |
| 7.4 | ✅ DONE — Applied F1/F4/F11/F12 schemas and appended `BR_EX_BE_00047`–`BR_EX_BE_00069`; added `stretch_expert_mapping` overview row | edited `br_ex_be_registry.md` |
| 7.5 | ✅ DONE — Batch approval completed per category: KE-OF and KE-SC approved as category batches | user batch approval |
| 7.6 | ✅ DONE — Updated `k_gap_exception_list.md`: accepted KE-OF/KE-SC nodes moved to `KE-RESOLVED-STRETCH`; coverage updated to 48/52 = 92.3% direct K-side bridge coverage | edited `k_gap_exception_list.md` |

### 14.4 Phase 8 — Audit Closure (F-RCA-05/07/08/09/10/11) ✅ COMPLETED

**Completion date:** 2026-05-20

**Decision protocol:** Each finding was evaluated with 3 rounds max using RCA × 5-Why × scoring threshold 4/5. All six findings reached closure threshold; no finding required Round 3.

| Step | Finding | Fix | Output |
|---|---|---|---|
| 8.1 | F-RCA-11 | ✅ DONE — NetworkX 3.3 has no supported `random_state` parameter for `greedy_modularity_communities`; fixed reproducibility by deterministic post-detection community ordering and recorded API boundary in context | edited `phase2_intersection_analysis.py` + `vvv_qmrf_ex_context.json` |
| 8.2 | F-RCA-05 + F-RCA-07 | ✅ DONE — Full boundary audit report created for 143 entries (69 BR_EX_BE + 74 BR_EX_QM); result `entries_audited: 143`, `violations: 0`, `overall: PASS` | `data/phase8_boundary_audit_report.json` |
| 8.3 | F-RCA-08 | ✅ DONE — Historical Phase 5 qualifier preserved in §13: K-effective 82.7% (43/52) at time of Phase 5; later JSON reflects post-Phase 6 state | edited §13 |
| 8.4 | F-RCA-10 | ✅ DONE — Added baseline/current qualifier: Phase-4 baseline 111 entries; post-Phase 6 120 entries; post-Phase 7 143 entries | edited §13 |
| 8.5 | F-RCA-09 | ✅ DONE — Updated §5.2 expectation: Top-N non-singleton communities map to BIAN; total count dominated by orphan BE nodes is not a quality metric | edited §5.2 |

### 14.5 Phase 9 — Full Re-run (immutable `_v1.6` snapshots) ✅ EXECUTED

**Completion date:** 2026-05-21 (commit `d8ec025`)

**Execution result:** All 6 phase scripts patched with `SUFFIX` env var (Option D-refined); 6 immutable `*_v1.6.json` reports + 2 `*_v1.6.png` images produced; raw dual-anchored intersection **48/52 (92.3%)** — Stretch Tier 1 (≥50%) AND Tier 2 (≥80%) both PASS. Three new RCA findings discovered + closed: **F-RCA-12** (phase4 unsafe re-run → A.1+ workaround via new `phase4_graph_sync.py`), **F-RCA-13** (NetworkX `links`/`edges` key inconsistency), **F-RCA-14** (`K_SIDE_TYPES` missing `BR_EX_BE_STRETCH`).

| Step | Script | Output (immutable, NEW filename) | Status |
|---|---|---|---|
| 9.1 | `phase1_graph_construction.py` | `data/phase1_validation_report_v1.6.json` (`snapshot_phase: "v1.6-stretch"`) | ✅ DONE |
| 9.1.5 | `phase4_graph_sync.py` (new helper, A.1+ fix for F-RCA-12) | Injected 34 missing edges (33 BE + 1 QM) into `vvv_qmrf_ex_graph.json` (149 → 183) | ✅ DONE |
| 9.2 | `phase2_intersection_analysis.py` (with deterministic post-detection community ordering; NetworkX 3.3 does not support `random_state` for `greedy_modularity_communities`) | `data/phase2_intersection_report_v1.6.json` — intersection **48/52 = 92.3%**, exceeds both Tier 1 (≥26) and Tier 2 (≥42) | ✅ DONE |
| 9.3 | `phase3_similarity_search.py` | `data/phase3_similarity_report_v1.6.json` — Tier2 BE=2 / QM=13 | ✅ DONE |
| 9.4 | ~~`phase4_bridge_registry.py`~~ — **SKIPPED per F-RCA-12 A.1+ fix.** Manual generation from registry MDs + Phase 8 audit data. | `data/phase4_registry_report_v1.6.json` — ghost count = 0; total BR_EX_BE = 69 (= 46 + 23 accepted); total BR_EX_QM = 74 | ✅ DONE |
| 9.5 | `phase5_visualize.py` | `data/phase5_coverage_report_v1.6.json` + `phase5_output/step5_1_network_diagram_v1.6.png` + `step5_2_kp_heatmap_v1.6.png` | ✅ DONE |
| 9.6 | `phase6_expert_mapping.py` | `data/phase6_expert_mapping_report_v1.6.json` — 9 KE-PM resolutions intact | ✅ DONE |
| 9.7 | Numerical consistency sanity check | [`reviews/rca_plan_v1.6_completion_audit.md`](reviews/rca_plan_v1.6_completion_audit.md) | ✅ DONE |

**Immutability invariant:** `git diff HEAD -- data/phase{1,2,3,4,5,6}*_report.json` (excluding `_v1.6` and `_post_phase6` suffixes) shows **ZERO modifications** ✅ PASSED.

### 14.6 Phase 10 — Documentation Synchronization

| Step | File | Update | Status |
|---|---|---|---|
| 10.1 | `vvv-qmrf-ex-plan.md` | Bump status v1.6 PROPOSED → v1.6 EXECUTED; mark Section 14 phases ✅ Done; append new changelog row to header | ✅ DONE (this edit) |
| 10.2 | `vvv_qmrf_ex_intersection.md` | Header → "Phase 9 final — post-stretch (v1.6)"; add changelog row: Phase 6 (25) → Phase 9 stretch (48 final raw count) | ✅ DONE (Phase 9.2 auto-regen + header bump) |
| 10.3 | `vvv_qmrf_ex_boundary_audit.md` | Update line 9 / 65 / 81 / 116 to final entry count (143); add Phase 7–9 changelog block | ✅ DONE |
| 10.4 | `vvv_qmrf_ex_gaps.md` | Recompute K-gap to retain only `KE-QI` (4 nodes) + `KE-{OF,SC}-RCA-REJECTED-3R` as true gaps | ✅ DONE (Phase 9.2 auto-regen reflects 4 K-gaps) |
| 10.5 | `reviews/rca_checkpoint.md` | Bump v1.5 → v1.6; findings count 22 → 22 + new Phase 7–9 findings (F-RCA-12/13/14); add Section 3e | ✅ DONE |
| 10.6 | `reviews/rca_inventory.md` + `reviews/vvv_qmrf_ex_effectiveness.md` | Re-validate effectiveness metrics with new raw 92.3% and total 143 entries | ✅ DONE |
| 10.7 | `reviews/rca_plan_v1.6_completion_audit.md` | New file — read-only audit verifying Phase 7–9 outputs match Section 14 claims; cross-check JSON ↔ MD ↔ git | ✅ DONE (committed `d8ec025`) |
| 10.8 | `data/vvv_qmrf_ex_context.json` | Bump version 0.4 → 0.7; update `edge_count: 183`, `node_count: 420`, add `greedy_modularity_random_state_supported: false`, `replacement_control: "stable_post_detection_sort"`, `snapshot_phase: "post-stretch-v1.6"` | ✅ DONE |
| 10.9 | `ex_schema_addendum.md` | Document Phase 7 stretch Bridge Relation additions: `operator_decomposition` + `sub_concept_direct_anchor` | ✅ DONE |

### 14.7 Risks

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| R1 | Strict 4.5/5 KE-OF threshold → high REJECT rate; Stretch Tier 2 (≥80%) may not be achievable | 🔴 VERY HIGH | Graceful degradation accepted by user (Q2=c); final raw % reported honestly; REJECTED-3R nodes retain `KE-OF` status |
| R2 | KE-SC relaxed 3.5/5 may accept weak parent-inheritance-based mappings | 🟡 MEDIUM | Boundary-guard pre-check (Step 7.3) catches `identity` violations; relaxed bar justified by parent K-coverage already exists |
| R3 | Phase 9 re-run overwrites v1.5 immutables | 🔴 CRITICAL | Step 9.x uses `_v1.6` suffix EXCLUSIVELY; immutability invariant verified via `git diff` (Step 9.7) |
| R4 | `random_state=42` produces different community count than v1.5 (320/323) | 🟡 LOW | Documented as expected change; new value recorded in context.json |
| R5 | BE SOT lacks sufficient candidate pool for some KE-OF nodes | 🟡 MEDIUM | Step 7.0 `REJECTED-NO-POOL` graceful fallback; does not block other nodes |
| R6 | New Bridge Relations needed in whitelist (`operator_decomposition`, `sub_concept_direct_anchor`) | 🟢 LOW | Step 10.9 updates `ex_schema_addendum.md` |
| R7 | Author metadata missing on new files | 🟡 LOW | Template from CLAUDE.md author block applied to every new file outside `public_documents/` and `published_documents/` |

### 14.8 Success Criteria (v1.6 gates)

| # | Criterion | Target | Method |
|---|---|---|---|
| 1 | **Stretch Tier 1** | Raw ≥50% (≥26 dual-anchored) | `data/phase2_intersection_report_v1.6.json` → `intersection_count` |
| 2 | **Stretch Tier 2 (aspirational)** | Raw ≥80% (≥42 dual-anchored) | Same source — pass-or-graceful-degradation |
| 3 | **Audit closure** | F-RCA-05/07/08/09/10/11 all ✅ Resolved | `reviews/rca_plan_v1.6_completion_audit.md` |
| 4 | **Boundary integrity** | C1–C7 100% pass on final entries (≤143) | `data/phase8_boundary_audit_report.json` |
| 5 | **Immutability** | Zero git modification to v1.5 phase JSONs (original 7 files) | `git diff HEAD -- data/phase{1..6}_*.json` (exclude `_v1.6` / `_post_phase6`) |
| 6 | **Reproducibility** | `random_state=42` recorded; re-run reproduces identical results | `vvv_qmrf_ex_context.json["random_state"]` |
| 7 | **RCA rigor** | 100% ACCEPTED entries pass their category threshold (4.5 or 3.5); 100% REJECTED entries have full 3-round audit trail | `phase7_ke_of_rca_log.md` + `phase7_ke_sc_rca_log.md` |
| 8 | **Doc synchronization** | All MD numerical claims match JSON sources | Audit Section 4 of `rca_plan_v1.6_completion_audit.md` |

### 14.9 Sequence and Dependencies

```
Step 8.1 (F-RCA-11 random_state) ─┐
                                  ├─→ Phase 7 (RCA gates, batch approval)
Step 7.0 (candidate pool)         ─┘                  │
                                                      ▼
                                  Phase 8 (Audit closure 8.2–8.5)
                                                      │
                                                      ▼
                                  Phase 9 (Full re-run, _v1.6 outputs)
                                                      │
                                                      ▼
                                  Phase 10 (Doc sync)
```

- **Critical path:** Phase 7 ⇒ Phase 9 (re-run needs new bridges)
- **Parallel:** Step 8.1 (random_state edit) independent — can run before Phase 7
- **Audit closure (Steps 8.2–8.5):** runs after Phase 7 completes but before Phase 9 so re-run picks up F-RCA-08/10 plan edits

### 14.10 Open Items / Deferrals

- BIAN-14 structural review (still ⏳ Pending from v1.5 §12) — not in v1.6 scope
- Final BR_XXXXX ID assignment (still ⏳ Deferred from v1.5 §12) — not in v1.6 scope
- Promotion gate from EX → core (Rule I-5) — explicitly out-of-scope for v1.6

---

## 15. v1.7 KE-SC Threshold Tightening — Phase 11 ✅ EXECUTED

**Completion date:** 2026-05-21
**Authority:** Extends Plan v1.6 — does not overwrite §14. Phase 11 results recorded in-place per "extend, not overwrite" rule.

### 15.1 RCA Purpose (v1.7)

**Symptom:** Plan v1.6 §14.2 Q2 set KE-SC threshold at 3.5/5 vs KE-OF at 4.5/5 — asymmetric rigor. Publication-ready audit defensibility requires near-symmetric thresholds.

**Cause:** §14.2 Q2 justification ("KE-SC has parent K-coverage as fallback so lower bar acceptable") was a pragmatic v1.6 floor, but did not anticipate post-execution academic review pressure on threshold parity.

**5 Whys:**
1. Why raise KE-SC to 4.0? → Reduce asymmetry with KE-OF (4.5/5).
2. Why not full 4.5 symmetry? → KE-SC retains parent K-coverage fallback, so slightly lower (4.0) is defensible.
3. Why allow 1 carve-out at 3.8? → `BR_EX_BE_00060` (N_QM_VVV_00007) has structurally sharp boundary guard (Vyatireka = discrete logical operation, well-bounded from QM counterfactual physics) + raw cosine 4.35 (highest in 3.8-band).
4. Why downgrade 3 specific entries? → They share thin structural boundaries (semantic-only distinction or generic concept mapped to QM-specific experiment) AND score ≤3.8.
5. **Root cause F-RCA-15:** v1.6 KE-SC=3.5 was a stretch floor; v1.7 retrofits stricter 4.0+carve-out to harmonize with KE-OF for publication readiness, accepting -3 entries (48→45 intersection, 92.3%→86.5%; Tier 2 still passes with 6.5pt margin).

### 15.2 Threshold Specification (v1.7)

| Threshold | v1.6 | **v1.7** | Rationale |
|---|---|---|---|
| KE-OF | 4.5/5 | 4.5/5 (unchanged) | Strictest — no parent inheritance fallback |
| **KE-SC** | **3.5/5** | **4.0/5 + 1 carve-out at 3.8** | Near-symmetric with KE-OF; carve-out requires (i) score ≥3.8, (ii) structurally sharp boundary guard, (iii) raw cosine ≥4.3 |

### 15.3 Tier Action Plan (3-tier, applied to 10 KE-SC entries)

| Tier | Action | Entries (verified) | Total |
|---|---|---|---|
| A | **KEEP (score ≥4.0)** | `BR_EX_BE_00062` (00012, 4.0), `00063` (00013, 4.0), `00064` (00016, 4.1), `00067` (00035, 4.0), `00068` (00040, 4.0), `00069` (00053, 4.1) | 6 |
| B | **KEEP (score 3.8, carve-out)** | `BR_EX_BE_00060` (00007, 3.8, raw 4.35) — boundary "absence-side evidence ≠ quantum counterfactual physics" structurally sharp | 1 |
| C | **RECLASSIFY → KE-SC exception** | `BR_EX_BE_00061` (00008, 3.7), `BR_EX_BE_00065` (00022, 3.8), `BR_EX_BE_00066` (00024, 3.7) — boundary guards too thin | 3 |

**Total:** 7 accepted + 3 reclassified = 10 (math checks).

### 15.4 Phase 11 — Re-execution Scope

| Step | Action | Output |
|---|---|---|
| 11.1 | Annotate 3 reclassified entries in `br_ex_be_registry.md` with `v1.7 Status: RECLASSIFIED-v1.7-KE-SC-THRESHOLD-RAISE` (NO renumber — namespace gaps preserved) | edited registry |
| 11.2 | Re-add 3 VVV nodes to `k_gap_exception_list.md` under KE-SC (with note on v1.7 reclassification) | edited exception list |
| 11.3 | Annotate `phase7_ke_sc_rca_log.md` for 3 reclassified entries | edited log |
| 11.4 | Update `ex_schema_addendum.md` threshold spec to KE-SC v1.6=3.5, v1.7=4.0+carve-out | edited schema |
| 11.5 | Patch `phase4_graph_sync.py` with reclassified-entry filter list | edited helper |
| 11.6 | Re-run Phase 9 chain with `VVV_QMRF_EX_SUFFIX="_v1.7"` — produces `_v1.7.json` immutable snapshots without overwriting `_v1.6` baselines | 6 new JSONs + 2 PNGs |
| 11.7 | Generate `phase4_registry_report_v1.7.json` manually (per F-RCA-12 A.1+ workaround) | manual JSON |
| 11.8 | Re-audit boundary on 140 entries → `phase8_boundary_audit_report_v1.7.json` | new audit JSON |
| 11.9 | Write `reviews/rca_plan_v1.7_completion_audit.md` | new audit doc |
| 11.10 | Doc sync (header bumps, changelog appends) across plan/intersection/gaps/boundary_audit/rca_checkpoint/inventory/effectiveness/context | edited 8 files |

### 15.5 Immutability Invariant (v1.7)

**Hard rule:** `_v1.7` snapshots MUST NOT overwrite `_v1.6` or v1.5-baseline phase JSONs. Verify with:
```
git diff HEAD -- data/phase{1..6}*_report.json data/phase{1..6}*_report_v1.6.json
```
Must show ZERO modifications to both v1.5 and v1.6 immutables.

### 15.6 Expected Results

| Metric | v1.6 | **v1.7 target** |
|---|---|---|
| BR_EX_BE active | 69 | 66 |
| BR_EX_BE reclassified (in registry, marked) | 0 | 3 |
| BR_EX_QM | 74 | 74 (unchanged) |
| Total registry rows | 143 | 143 (3 marked inactive) |
| Graph edges (active) | 183 | 180 |
| Raw dual-anchored | 48/52 (92.3%) | 45/52 (86.5%) |
| Stretch Tier 1 (≥50%) | ✅ | ✅ |
| Stretch Tier 2 (≥80%) | ✅ | ✅ (6.5pt margin) |
| Boundary violations | 0/143 | 0/140 (active set) |

### 15.7 Risks

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| R1 | Removing 3 entries from active set breaks v1.5/v1.6 hash invariants | 🟡 Medium | Use "annotate-don't-delete" pattern: rows stay in registry MD with RECLASSIFIED status; namespace gaps preserved |
| R2 | F-RCA-12 (phase4 unsafe re-run) carries forward | 🟢 Low | Continue A.1+ workaround via `phase4_graph_sync.py` (now with filter) |
| R3 | Carve-out criterion (3.8 + sharp boundary) is subjective | 🟡 Medium | Document explicit criteria in §15.2; only 1 carve-out, well-justified by raw 4.35 cosine + structural distinction |
| R4 | Reviewers may argue "still asymmetric" (4.5 vs 4.0) | 🟢 Low | KE-SC retains parent fallback; 0.5-band difference is defensible; alternative 4.5 symmetry would cost more entries |

### 15.8 Success Criteria (v1.7 gates)

| # | Criterion | Target | Method |
|---|---|---|---|
| 1 | **Stretch Tier 1** | Raw ≥50% (≥26) | `data/phase2_intersection_report_v1.7.json` |
| 2 | **Stretch Tier 2** | Raw ≥80% (≥42) | Same source |
| 3 | **Threshold spec applied** | 6 KEEP + 1 carve-out + 3 RECLASSIFIED | Registry annotations + log audit |
| 4 | **Boundary integrity** | 0 violations on 140 active entries | `phase8_boundary_audit_report_v1.7.json` |
| 5 | **Immutability v1.5 + v1.6** | git diff zero on phase JSONs (both suffixes) | git diff verification |
| 6 | **Doc consistency** | All MD claims match JSON | Section 4 of v1.7 completion audit |

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
