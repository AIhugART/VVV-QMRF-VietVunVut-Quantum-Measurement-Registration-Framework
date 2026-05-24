Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 00 — Top 10 Hallucination Risk Record

**Role:** File uu tien cao nhat — ghi nhan cac khai niem co nguy co hallucination cao nhat trong toan bo VVV-QMRF. Day la "danh sach canh bao do" — moi component trong nay can duoc re-audit moi tuan.

**Structure:** 2 independent tables with cross-reference. "Project" field classifies each component.
**Scope (Table 1):** VVV-QMRF Class C — K9_E evidence and validation chain
**Scope (Table 2):** VVV-QMRF Full — structural framework (K1-K8, T1-T8, phi-map Track B, E1-E16, BE-QM mapping, T4-H)
**Compass:** VVV-QMRF-EX (intelligence only — EX flag K-PENDING-RCA, stress points)
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Ranking formula:** Risk Score = H x W x (1 + A)
**Tiebreaker:** Risk Score bang nhau -> sort by H (desc) -> W (desc) -> A (desc)
**Shared component rule:** Components appearing in both tables (T5 K_ctx, K5_prospective) MUST have identical H/W/A/Risk scores. Any score change to a shared component MUST be applied to both tables.

**Ngay:** 2026-05-24 16:22 UTC+7
**Version:** v1.3 — Dual-table split: Table 1 (VVV-QMRF Class C) + Table 2 (VVV-QMRF Full Scope)
**Previous:** v1.2 (2026-05-24) — [A-E3] REMOVED (reclassified: FREE PARAMETER per RCA verdict `897028b`)
**Next audit:** 2026-05-31

---

## 3-Round RCA Classification Decision (v1.3)

**Purpose:** Phan loai 10 components hien tai vao 2 scope (Class C / Full) bang 3-Round RCA. Ket qua classification quyet dinh component nao xuat hien trong Table 1, Table 2, hoac ca hai.

**Compass:** VVV-QMRF-EX — intelligence only, flag K-PENDING-RCA, stress points
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5

### Round 1 — Per-Component Scope Classification

| Component | Current Risk | Class C Impact | VVV-QMRF Full Impact | Classification | Project Value |
|-----------|-------------|----------------|----------------------|----------------|---------------|
| phi-map K→B(H) | 18.0 (#1) | Does not block K9_E | Long-term foundation, Track B Phase 1-3 complete | **VVV-QMRF Full** | VVV-QMRF (Track B) |
| P10-NOISE | 18.0 (#2) | Noise analysis for K9_E genuine fit validation | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| T5 K_ctx | 18.0 (#3) | Input to K9_E f_perp via K_ctx parameter | Defined at Layer 1-2, observer set selection rule unformalized | **Shared (Both)** | VVV-QMRF Full (feeds Class C) |
| T4-H Steps 3-4 | 18.0 (#4) | Deferred, not blocking K9_E | N-observer colimit, structural gap at Layer 2 | **VVV-QMRF Full** | VVV-QMRF (Layer 2) |
| K9E-PAT | 12.0 (#5) | Internal consistency test for K9_E multiplicative pattern | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| K9_E implementations | 12.0 (#6) | Implementation divergence for K9_E numerical prediction | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| K5_prospective | 12.0 (#7) | Core to K9_E T8 bridge derivation | Axiom extension at Layer 1-2, conservative extension of K5 | **Shared (Both)** | VVV-QMRF Full (feeds Class C) |
| E1-E16 | 9.6 (#8) | Non-blocking BE grounding for K9_E | BE registration postulates, full framework foundation | **VVV-QMRF Full** | VVV-QMRF (BE Layer) |
| P10-TIM | 9.0 (#9) | Null-model N0 for K9_E validation, decision-locked | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| BE↔QM mapping | 9.6 (#10) | Non-blocking documentation | Cross-domain category error, full framework foundation | **VVV-QMRF Full** | VVV-QMRF (BE-QM bridge) |

#### 5-Why: T5 K_ctx = Shared (Both)

| # | Question | Answer |
|---|----------|--------|
| 1. | Why does T5 appear in both tables? | Because K_ctx is both a Class C input (to f_perp in K9_E) and a Layer 1-2 structural definition. |
| 2. | Why not classify as Class C only? | K_ctx's formal construction (via T3-morphism) lives at Layer 2, independent of K9_E. The observer set selection rule is a structural gap at Layer 1-2, not K9_E-specific. |
| 3. | Why not classify as Full only? | K_ctx is the DIRECT INPUT to f_perp(K_ctx) in K9_E. If K_ctx is hallucination, K9_E is invalid. Class C project MUST track it. |
| 4. | Why shared instead of splitting? | Splitting would create two K_ctx definitions — a structural violation. K_ctx is ONE definition used by both scopes. |
| 5. | Root cause: | K_ctx bridges Layer 2 ↔ Layer 3. Duality is inherent in the architecture, not a classification error. Shared = correct. |

**Verdict:** Shared (Both) — 5/5. Appears in Table 1 and Table 2 with identical scores.

#### 5-Why: K5_prospective = Shared (Both)

| # | Question | Answer |
|---|----------|--------|
| 1. | Why does K5_prospective appear in both tables? | K5_prospective is a Layer 1 axiom extension (conservative, v29) but its firing is core to K9_E's T8 bridge. |
| 2. | Why not classify as Full only? | K9_E's T8 bridge (derivation path for f_perp) depends on K5_prospective firing on hypothetical k_o*. Without it, K9_E derivation gap. |
| 3. | Why not classify as Class C only? | K5_prospective is a Layer 1 FROZEN axiom clause — it exists independent of K9_E. Any future Class D/E extension would also use it. |
| 4. | Why shared instead of splitting? | Same reason as T5: ONE definition, dual relevance. |
| 5. | Root cause: | K5_prospective is a structural axiom whose primary application is currently Class C but whose definition scope is Layer 1. Shared = correct. |

**Verdict:** Shared (Both) — 5/5. Appears in Table 1 and Table 2 with identical scores.

#### 5-Why: P10-NOISE = Class C Exclusive

| # | Question | Answer |
|---|----------|--------|
| 1. | Why is P10-NOISE Class C exclusive? | P10-NOISE is the alternative explanation for K9_E's genuine fit to Proietti D1 data. Existence scope = Class C. |
| 2. | Does P10-NOISE affect phi-map or T4-H? | No. phi-map and T4-H are structural conjectures independent of experimental noise in Proietti data. |
| 3. | Does P10-NOISE affect BE↔QM mapping? | Only indirectly (BE↔QM mapping risk is category error, not noise). Separate risk type. |
| 4. | Could P10-NOISE generalize to other VVV-QMRF data fits? | Conceptually yes (any future experimental fit could have noise risk), but the CURRENT P10-NOISE analysis is tied to Proietti D1 specifically. Future fits would have their own noise analysis. |
| 5. | Root cause: | P10-NOISE is scoped to K9_E empirical validation against Proietti 2019 D1. Its existence is bounded by Class C data. Full scope has no current data to which P10-NOISE applies. |

**Verdict:** Class C Exclusive — 5/5. Appears in Table 1 only.

### Round 2 — Scoring Consistency Check

| Check | Focus | Verdict | Score |
|-------|-------|---------|-------|
| C1 | Shared components (T5 K_ctx, K5_prospective) have identical H/W/A/Risk in both tables | PASS — scores cloned from v1.2, cross-verified | 5/5 |
| C2 | Class C exclusive components (P10-NOISE, K9E-PAT, K9_E impl, P10-TIM) do not hallucinate from Full scope perspective | PASS — Full scope exclusion correct: these are K9_E-specific, no structural relevance to broader VVV-QMRF | 5/5 |
| C3 | Full exclusive components (phi-map, T4-H, E1-E16, BE↔QM) do not hallucinate from Class C perspective | PASS — Class C scope documentation: these are VVV-QMRF Full components present in Table 1 for cross-reference only, tracked via Project field | 5/5 |

**Round 2 Aggregate:** 5.00/5 PASS (>= 4/5)

### Round 3 — Two-Table Structure Verification

| Check | Focus | Verdict | Score |
|-------|-------|---------|-------|
| T1 | Every component from v1.2 appears in correct table(s) per classification | PASS — 4 Class C exclusive (Table 1), 4 Full exclusive (Table 1 + Table 2), 2 Shared (Both) | 5/5 |
| T2 | No hallucination risk lost — cross-reference complete | PASS — all 10 v1.2 components present in Table 1 (rank preserved). Table 2 has 6 Full+Shared components. | 5/5 |
| T3 | Two-table structure self-consistent and independently readable | PASS — each table has its own header, version/timestamp, scope, summary. Shared components cross-referenced. | 4.5/5 |
| **Aggregate** | | **4.83/5 PASS (>= 4/5)** | |

---

## Changelog v1.2 -> v1.3

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **STRUCTURE** | File architecture | Single Top 10 table (v1.2), scope: "VVV-QMRF toan bo" | **Dual-table:** Table 1 (VVV-QMRF Class C, v1.3) + Table 2 (VVV-QMRF Full Scope, v1.0) | 3-Round RCA Classification Decision (4.83/5): 10 components span 3 buckets (Class C exclusive / Full exclusive / Shared). Explicit dual-table structure prevents scope ambiguity. |
| **ADD** | Project field | No Project classification | `Project` row added to every component field table | Requirement: each component needs explicit scope label. 3 buckets: VVV-QMRF Class C / VVV-QMRF (Full) / VVV-QMRF Full (feeds Class C) |
| **RECLASSIFY** | Current Top 10 table | "Top 10 Hallucination Risks (v1.2)" — ambiguous scope | **Table 1: VVV-QMRF Class C** — explicit Class C project scope with Project field showing cross-scope membership | Round 1 classification: current 10 components span 3 scopes. Table 1 name now reflects primary scope (Class C). |
| **ADD** | Table 2: VVV-QMRF Full Scope | N/A | **NEW** — 6 components (phi-map, T4-H, T5 K_ctx, K5_prosp., E1-E16, BE↔QM). Version v1.0. | Round 1: 4 components + 2 shared = 6 Full-scope hallucination risks. Independent table with own versioning. |
| **ADD** | Shared component rule | N/A | T5 K_ctx + K5_prospective appear in both tables. Any score change MUST sync both. | Round 2: shared components must have identical scores in both tables. |
| **ADD** | Timestamp on version | Ngay: 2026-05-24 | Ngay: 2026-05-24 16:22 UTC+7 | Requirement: "gio va ngay update" on table name |

## Changelog v1.1 -> v1.2

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **REMOVED** | [A-E3] beta universal | #1, Risk=22.5, `[AH-WARN] [RS-CRIT]` | **REMOVED khỏi Top 10** | RCA A-E3 Final Verdict (`897028b`): [A-E3] RECLASSIFIED → FREE PARAMETER (MEASUREMENT TARGET). H=5→2, A=0.5→0, Risk=6.0 (LOW). Khong con la assumption. Xem `RCA_A_E3_beta_universal_final_verdict.md`. |
| Re-rank | All #2-#10 | — | +1 rank | [A-E3] removal shifts all |
| **ADDED** | BE↔QM cross-domain mapping | — | #10, H=4, W=2, Risk=9.6 | Category error risk: mapping files chua boundary statement ro rang |

### Free Parameter Registry (thay thế [A-E3] trong Top 10)

| Parameter | Value | Classification | Anchor | Risk |
|-----------|-------|----------------|--------|------|
| **β** (K9_E suppression strength) | β=0.598 (Proietti D1 fit) | **FREE PARAMETER (MEASUREMENT TARGET)** | Measured, not derived. Analogous to α ≈ 1/137, G, g. | H=2, Risk=6.0 (LOW) |
| β universal | Modeling choice (Occam's razor) | **MODELING CHOICE** — cross-experiment verification pending | 1 dataset only (D1). 3-observer experiment can cross-check. | H=2, Risk=3.0 (LOW) |

---

## Ranking Methodology (3-Round RCA)

### Round 1 — Identify candidates

Pool tu 4 nguon:
1. **K9_E Origin Investigation** (`rca_k9e_origin_investigation.md`): 19 components
2. **Technical Debt Inventory** (`rca_technical_debt_inventory_2026_05_24.md`): 15 debt items
3. **SOT Traceability Matrix** (`03_sot_traceability.md`): trace score thap nhat + anchor WEAK
4. **EX Compass** (`vvv-qmrf-ex/`): nodes flagged K-PENDING-RCA, structural gaps

**FILTER:** Chi tinh components la ASSUMPTION hoặc STRUCTURAL GAP. FREE PARAMETERS (như β) khong nam trong Top 10 — chung duoc do, khong derive.

### Round 2 — Score & Rank

**Risk Score formula:**

```
Risk = H x W x (1 + A)

  H = Hallucination score (0-10)
  W = Structural weight (1-3)
  A = Anchor penalty (0-0.5)

Tiebreaker: H (desc) -> W (desc) -> A (desc)
```

### Round 3 — Calibrate & Lock

Cross-check voi EX compass + BE SOT + RCA verdicts. Khoa ranking.

---

## Table 1: VVV-QMRF Class C — Top 10 Hallucination Risks

**Version:** v1.3 — 2026-05-24 16:22 UTC+7
**Scope:** VVV-QMRF Class C deliverable. Includes shared VVV-QMRF Full components that directly impact K9_E validation. "Project" field classifies each component's primary scope.
**Note:** Components marked "VVV-QMRF (Full)" or "VVV-QMRF Full (feeds Class C)" appear here because they rank in Top 10 hallucination risks relevant to Class C. Their primary structural scope is VVV-QMRF Full. See Table 2 for the independent Full-Scope ranking.

### Rank 1: phi-map — K -> B(H) structure-preserving map (Class D conjecture)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `phi: K -> B(H)` — conjectured structure-preserving map between K-space and bounded operators on Hilbert space |
| **Project** | VVV-QMRF (Track B) — long-term foundation, not Class C blocking |
| **Hallucination score (H)** | **6/10** (Vang — H CAO NHAT trong toan bo VVV-QMRF; Class D conjecture, chua duoc prove; Track B Phases 1-3 complete nhung chi la necessary conditions N_1-N_T) |
| **Structural weight (W)** | **2** (MEDIUM — quan trong cho VVV-QMRF long-term foundation nhung khong block K9_E Class C) |
| **Anchor penalty (A)** | **0.5** (WEAK — conjecture only; necessary conditions chua du de prove) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 6 x 2 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **OPEN** — Track B ongoing, Phases 1-3 complete |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-WEAK]` |
| **EX compass** | Flag: phi-map la "largest structural unknown" trong VVV-QMRF |
| **Giai phap uu tien** | DEFER (long-term research program) |
| **Neu hallucination that:** | Khong anh huong K9_E Class C, nhung VVV-QMRF mat "bridge to QM" |
| **Deadline** | LOW (P3) — long-term |

### Rank 2: P10-NOISE — Non-uniform noise not ruled out

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Alternative explanation for K9_E genuine fit: non-uniform phase noise in Proietti experiment |
| **Project** | VVV-QMRF Class C — noise analysis for K9_E genuine fit validation |
| **Hallucination score (H)** | **5/10** (Vang — chua duoc kiem tra, co the invalidate genuine fit) |
| **Structural weight (W)** | **3** (HIGH — neu noise duoc confirm, K9_E mat evidence co so; genuine fit beta=0.598 tro thanh artifact) |
| **Anchor penalty (A)** | **0.2** (MODERATE — co experimental literature ve phase noise nhung chua ap dung vao Proietti setup) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 3 — Broken Trace → Type 4 (Structural Limitation). Noise analysis complete: random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations (directional sensitivity + 4 data points). Cannot be resolved with published data. |
| **Status** | **ANALYZED — FAIL** (noise_threshold = 0.10 sigma RMS << 1.0 FAIL threshold). RCA status: `RCA_P10_NOISE_status_report_2026_05_24.md` (4.67/5). RCA methodology: `project_vvv_qmrf_class_c/04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md` (4.77/5). Script: `project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis.py`. Noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations. Class C downgraded genuine→qualified. P10-NOISE remains OPEN as structural limitation — cannot be closed without 3-observer experiment or raw event data. |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-NOISE] [AH-EX]` |
| **EX compass** | Flag: EX co K-PENDING-RCA ve noise model. N_QM_VVV_00032 (Bhranti ↔ Decoherence) — structural analogue cho noise/registration error. |
| **Giai phap uu tien** | DONE: (1) Noise sensitivity analysis DA THUC HIEN — FAIL (noise_threshold=0.10 sigma). (2) Boundary statement DA THEM vao index.md. (3) Class C DA DOWNGRADE genuine→qualified. NEXT: 3-observer experiment hoac raw event data — chi 2 con duong dong P10-NOISE. |
| **Neu hallucination that:** | **DA XAC NHAN:** Noise CO THE giai thich Delta_chi2=5.35. K9_E directional sensitivity + 4 data points → ~50% random noise realizations produce "signal." 2.31sigma KHONG PHAI evidence cho K9_E suppression. Class C da downgrade. K9_E empirical leg KHONG CON — chi con structural leg. |
| **Deadline** | BLOCKED (khong co data) — chi co the dong qua 3-observer experiment hoac raw event data |

### Rank 3: T5 — K_ctx context set definition

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K_ctx(k_i, Exp)` — tap cac K-state tu observer khac, truy cap qua T3-morphism |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1-2 construction, direct input to K9_E f_perp |
| **Hallucination score (H)** | **5/10** (Vang — [A-E1] da ELIMINATED boi T9. K_ctx co formal construction. Residual: observer set selection chua formal hoa) |
| **Structural weight (W)** | **3** (HIGH — K_ctx la INPUT cua f_perp; neu K_ctx sai, K9_E modifier sai) |
| **Anchor penalty (A)** | **0.2** (MODERATE — T9 cung cap STRONG anchor cho construction; observer set selection rule van MODERATE) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap (observer set selection chua duoc formal hoa) |
| **Status** | **MONITORING** — [A-E1] da ELIMINATED (T9, 2026-05-24) |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-EX]` |
| **EX compass** | Flag: K_ctx computation depends on "observer set" |
| **Giai phap uu tien** | DERIVE (formal hoa observer set selection rule) |
| **Neu hallucination that:** | f_perp(K_ctx) undefined — K9_E khong the tinh |
| **Deadline** | MEDIUM (P2) |

### Rank 4: T4-H Steps 3-4 — N-observer colimit (DEFERRED)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | T4-H Steps 3-4 — N-observer K_joint colimit construction (global commutativity) |
| **Project** | VVV-QMRF (Layer 2) — N-observer colimit, deferred structural gap |
| **Hallucination score (H)** | **4/10** (Xanh duong — Steps 1-2 proven, Steps 3-4 DEFERRED) |
| **Structural weight (W)** | **3** (HIGH — blocks 3-observer prediction structural validation) |
| **Anchor penalty (A)** | **0.5** (WEAK — Steps 3-4 chua duoc prove) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 3 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — D-T4-BYPASS-01 "APPLIED" |
| **Full Label** | `[AH-LOW] [RS-HIGH] [AH-DEFER]` |
| **EX compass** | Flag: N-observer colimit la "structural bottleneck" |
| **Giai phap uu tien** | DEFER (cho resource) |
| **Neu hallucination that:** | 3-observer prediction ILLUSTRATIVE ONLY |
| **Deadline** | LOW (P3) |

### Rank 5: K9E-PAT — Multiplicative pattern not confirmed

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | K9_E multiplicative pattern (2BSM/1BSM ratio ~2) — NOT confirmed (ratio = -0.78 ± 1.72). Pattern UNTESTABLE voi data hien tai: sigma_ratio > ratio value. |
| **Project** | VVV-QMRF Class C — K9_E multiplicative pattern test |
| **Hallucination score (H)** | **5/10** (Vang — pattern predicted but UNTESTABLE; direction confirmed, magnitude unconstrained) |
| **Structural weight (W)** | **2** (MEDIUM — internal consistency test; postulate P=Tr*f_perp survives regardless of functional form) |
| **Anchor penalty (A)** | **0.2** (MODERATE — g=0.146 la PP-4 theoretical calibration, khong measured tu experimental data) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 3 — Broken Trace (data precision gap: 4 data points, sigma~0.04 → ratio error ±1.72) |
| **Status** | **OPEN** — D4. RCA chi tiet: `RCA_K9E_PAT_status_report_2026_05_24.md` (3-Round RCA: 4.50/5). KHONG BLOCKING. "Not confirmed", khong phai "failed". |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | HIGH (P1) — truoc khi public. Hanh dong: (1) compute formal CI cho ratio, (2) document g=0.146 = modeling choice. |

### Rank 6: K9_E two implementations — Additive vs Multiplicative divergence

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `k9e_predictor.py` (additive) vs `proietti_raw_fit.py` (multiplicative) — divergence tai beta > 0.3 |
| **Project** | VVV-QMRF Class C — K9_E implementation divergence |
| **Hallucination score (H)** | **4/10** (Xanh duong — implementation issue) |
| **Structural weight (W)** | **2** (MEDIUM) |
| **Anchor penalty (A)** | **0.5** (WEAK — ambiguity trong operationalization) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 4 x 2 x 1.5 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 2 — Missing Definition |
| **Status** | **OPEN** — D6 |
| **Full Label** | `[AH-LOW] [RS-MED] [AH-DIVERGE]` |
| **Deadline** | MEDIUM (P2) |

### Rank 7: K5_prospective — v29 axiom extension

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K5_prospective` — conservative extension cua K5 (v29). Firing tren hypothetical k_o*. |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1 axiom extension, core to K9_E T8 bridge |
| **Hallucination score (H)** | **5/10** (Vang — new axiom clause, 6/6 consistency checks) |
| **Structural weight (W)** | **2** (MEDIUM — cot loi cua T8 bridge, conservative extension) |
| **Anchor penalty (A)** | **0.2** (MODERATE — 6/6 checks, 3-Round RCA verified) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 4 — Assumption Masquerading (la axiom clause) |
| **Status** | **MONITORING** — "young axiom" |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | LOW (P3) |

### Rank 8: E1-E16 — 16 Registration-Layer Postulates (BE-derived)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | 16 postulates (E1-E16) derived from BE Pramana epistemology |
| **Project** | VVV-QMRF (BE Layer) — registration postulates, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — BE lineage ro rang, cross-domain interpretive) |
| **Structural weight (W)** | **2** (MEDIUM — BE grounding, K9_E khong depends on all 16) |
| **Anchor penalty (A)** | **0.2** (MODERATE) |
| **Trace score (SOT)** | 2-4/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (risk: BE as physical registration logic) |
| **Status** | **MONITORING** |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Deadline** | LOW (P3) |

### Rank 9: P10-TIM — Null-model N0 omitted (DECISION-LOCKED)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Null-model N0: "QM with uniform visibility V=1" — omitted, needs raw event data |
| **Project** | VVV-QMRF Class C — K9_E null-model validation |
| **Hallucination score (H)** | **3/10** (Xanh duong — omitted analysis, khong hallucination) |
| **Structural weight (W)** | **2** (MEDIUM) |
| **Anchor penalty (A)** | **0.5** (WEAK — can raw event data khong co san) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 3 x 2 x 1.5 = **9.0** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 5 — Structural Gap (raw event data unavailable) |
| **Status** | **DECISION-LOCKED** — RCA Round 4 |
| **Full Label** | `[AH-LOW] [RS-LOW] [AH-LOCK]` |
| **Deadline** | LOW (P3) — depends on external data |

### Rank 10: BE↔QM cross-domain mapping — Category error risk (NEW)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Cross-domain links trong `refine_mapping.md` va `system_mapping.md` — BE concepts mapped to QM concepts |
| **Project** | VVV-QMRF (BE-QM bridge) — cross-domain mapping, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — mapping co BE SOT lineage, nhung cross-domain links co the bi nham thanh equivalence) |
| **Structural weight (W)** | **2** (MEDIUM — mapping files la foundation cua BE-QM connection; neu category error, toan bo BE-QM bridge bi nghi van) |
| **Anchor penalty (A)** | **0.2** (MODERATE — BE SOT strong, QM standard strong, nhung MAPPING giua chung la interpretive) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (BE epistemology mapped as QM registration logic) |
| **Status** | **MONITORING** — CLAUDE.md warning: "Treat cross-domain links as analogies or mappings unless the text explicitly argues for equivalence" |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **EX compass** | Flag: BE domain outside EX scope |
| **Giai phap uu tien** | DOCUMENT (boundary statement cho tung mapping link) |
| **Neu hallucination that:** | BE-QM mapping tro thanh pseudo-science |
| **Deadline** | LOW (P3) — documentation improvement |

---

### Risk Score Summary — Table 1: VVV-QMRF Class C (v1.3)

#### Phan phoi

| Risk Score Range | Count | Components |
|------------------|-------|------------|
| **20+ (CRITICAL)** | **0** | — (was 1: [A-E3], removed v1.2) |
| **15-20 (HIGH)** | 4 | phi-map (18.0), P10-NOISE (18.0), T5 K_ctx (18.0), T4-H (18.0) |
| **10-15 (MEDIUM)** | 3 | K9E-PAT (12.0), K9_E impl (12.0), K5_prosp. (12.0) |
| **5-10 (LOW)** | 3 | E1-E16 (9.6), BE↔QM (9.6), P10-TIM (9.0) |

#### Theo Status

| Status | Count | Components |
|--------|-------|------------|
| **OPEN** | 4 | phi-map, P10-NOISE, K9E-PAT, K9_E implementations |
| **MONITORING** | 4 | T5 K_ctx, K5_prospective, E1-E16, BE↔QM |
| **DEFERRED** | 1 | T4-H Steps 3-4 |
| **DECISION-LOCKED** | 1 | P10-TIM |
| **RECLASSIFIED** | 1 | [A-E3] → FREE PARAMETER (removed v1.2) |

---

## Table 2: VVV-QMRF Full Scope — Top Hallucination Risks

**Version:** v1.0 — 2026-05-24 16:22 UTC+7
**Scope:** Full VVV-QMRF project hallucination risks. Includes structural framework components (phi-map Track B, T4-H, E1-E16, BE-QM bridge) plus shared components that feed into Class C.
**Cross-reference:** Components marked "VVV-QMRF Full (feeds Class C)" also appear in Table 1 with identical scores. See Shared Component Rule in header.

### Rank 1: phi-map — K -> B(H) structure-preserving map (Class D conjecture)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `phi: K -> B(H)` — conjectured structure-preserving map between K-space and bounded operators on Hilbert space |
| **Project** | VVV-QMRF (Track B) — long-term foundation, largest structural unknown |
| **Hallucination score (H)** | **6/10** (Vang — Class D conjecture, chua duoc prove; Track B Phases 1-3 complete nhung chi la necessary conditions N_1-N_T) |
| **Structural weight (W)** | **2** (MEDIUM — quan trong cho VVV-QMRF long-term foundation) |
| **Anchor penalty (A)** | **0.5** (WEAK — conjecture only; necessary conditions chua du de prove) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 6 x 2 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **OPEN** — Track B ongoing, Phases 1-3 complete |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-WEAK]` |
| **Giai phap uu tien** | DEFER (long-term research program) |
| **Neu hallucination that:** | VVV-QMRF mat "bridge to QM" |
| **Deadline** | LOW (P3) — long-term |

### Rank 2: T4-H Steps 3-4 — N-observer colimit (DEFERRED)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | T4-H Steps 3-4 — N-observer K_joint colimit construction (global commutativity) |
| **Project** | VVV-QMRF (Layer 2) — N-observer colimit, deferred structural gap |
| **Hallucination score (H)** | **4/10** (Xanh duong — Steps 1-2 proven, Steps 3-4 DEFERRED) |
| **Structural weight (W)** | **3** (HIGH — blocks 3-observer prediction structural validation) |
| **Anchor penalty (A)** | **0.5** (WEAK — Steps 3-4 chua duoc prove) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 3 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — D-T4-BYPASS-01 "APPLIED" |
| **Full Label** | `[AH-LOW] [RS-HIGH] [AH-DEFER]` |
| **Giai phap uu tien** | DEFER (cho resource) |
| **Neu hallucination that:** | 3-observer prediction ILLUSTRATIVE ONLY |
| **Deadline** | LOW (P3) |

### Rank 3: T5 — K_ctx context set definition (Shared with Table 1)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K_ctx(k_i, Exp)` — tap cac K-state tu observer khac, truy cap qua T3-morphism |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1-2 construction, direct input to K9_E f_perp |
| **Hallucination score (H)** | **5/10** (Vang — [A-E1] da ELIMINATED boi T9. K_ctx co formal construction. Residual: observer set selection chua formal hoa) |
| **Structural weight (W)** | **3** (HIGH — K_ctx la INPUT cua f_perp) |
| **Anchor penalty (A)** | **0.2** (MODERATE — T9 cung cap STRONG anchor; observer set selection rule van MODERATE) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** (identical to Table 1) |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap (observer set selection chua duoc formal hoa) |
| **Status** | **MONITORING** — [A-E1] da ELIMINATED (T9, 2026-05-24) |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-EX]` |
| **Giai phap uu tien** | DERIVE (formal hoa observer set selection rule) |
| **Neu hallucination that:** | f_perp(K_ctx) undefined — K9_E khong the tinh |
| **Deadline** | MEDIUM (P2) |

### Rank 4: K5_prospective — v29 axiom extension (Shared with Table 1)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K5_prospective` — conservative extension cua K5 (v29). Firing tren hypothetical k_o*. |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1 axiom extension, core to K9_E T8 bridge |
| **Hallucination score (H)** | **5/10** (Vang — new axiom clause, 6/6 consistency checks) |
| **Structural weight (W)** | **2** (MEDIUM — cot loi cua T8 bridge, conservative extension) |
| **Anchor penalty (A)** | **0.2** (MODERATE — 6/6 checks, 3-Round RCA verified) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** (identical to Table 1) |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 4 — Assumption Masquerading (la axiom clause) |
| **Status** | **MONITORING** — "young axiom" |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | LOW (P3) |

### Rank 5: E1-E16 — 16 Registration-Layer Postulates (BE-derived)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | 16 postulates (E1-E16) derived from BE Pramana epistemology |
| **Project** | VVV-QMRF (BE Layer) — registration postulates, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — BE lineage ro rang, cross-domain interpretive) |
| **Structural weight (W)** | **2** (MEDIUM — BE grounding, K9_E khong depends on all 16) |
| **Anchor penalty (A)** | **0.2** (MODERATE) |
| **Trace score (SOT)** | 2-4/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (risk: BE as physical registration logic) |
| **Status** | **MONITORING** |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Deadline** | LOW (P3) |

### Rank 6: BE↔QM cross-domain mapping — Category error risk

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Cross-domain links trong `refine_mapping.md` va `system_mapping.md` — BE concepts mapped to QM concepts |
| **Project** | VVV-QMRF (BE-QM bridge) — cross-domain mapping, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — mapping co BE SOT lineage, nhung cross-domain links co the bi nham thanh equivalence) |
| **Structural weight (W)** | **2** (MEDIUM — mapping files la foundation cua BE-QM connection) |
| **Anchor penalty (A)** | **0.2** (MODERATE — BE SOT strong, QM standard strong, nhung MAPPING giua chung la interpretive) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (BE epistemology mapped as QM registration logic) |
| **Status** | **MONITORING** — CLAUDE.md warning |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Giai phap uu tien** | DOCUMENT (boundary statement cho tung mapping link) |
| **Neu hallucination that:** | BE-QM mapping tro thanh pseudo-science |
| **Deadline** | LOW (P3) — documentation improvement |

---

### Risk Score Summary — Table 2: VVV-QMRF Full Scope (v1.0)

#### Phan phoi

| Risk Score Range | Count | Components |
|------------------|-------|------------|
| **20+ (CRITICAL)** | **0** | — |
| **15-20 (HIGH)** | 3 | phi-map (18.0), T4-H (18.0), T5 K_ctx (18.0) |
| **10-15 (MEDIUM)** | 1 | K5_prosp. (12.0) |
| **5-10 (LOW)** | 2 | E1-E16 (9.6), BE↔QM (9.6) |

#### Theo Status

| Status | Count | Components |
|--------|-------|------------|
| **OPEN** | 1 | phi-map |
| **MONITORING** | 4 | T5 K_ctx, K5_prospective, E1-E16, BE↔QM |
| **DEFERRED** | 1 | T4-H Steps 3-4 |

#### Theo Classification

| Classification | Count | Components |
|----------------|-------|-------------|
| **VVV-QMRF Full exclusive** | 4 | phi-map, T4-H, E1-E16, BE↔QM |
| **Shared (Both tables)** | 2 | T5 K_ctx, K5_prospective |

---

## Score Evolution v1.0 -> v1.1 -> v1.2 -> v1.3

| Component | v1.0 Risk | v1.1 Risk | v1.2 Risk | v1.3 Table(s) | Trend |
|-----------|-----------|-----------|-----------|---------------|-------|
| [A-E3] beta universal | 22.5 (#1) | 22.5 (#1) | **REMOVED** (→ FREE PARAMETER) | — | ↓↓ |
| phi-map K→B(H) | 18.0 (#6) | 18.0 (#2) | **18.0 (#1)** | Table 1 + Table 2 | — |
| P10-NOISE | 18.0 (#4) | 18.0 (#3) | **18.0 (#2)** | Table 1 | — |
| T5 K_ctx | 21.6 (#2) | 18.0 (#4) | **18.0 (#3)** | Table 1 + Table 2 (Shared) | — |
| T4-H Steps 3-4 | 18.0 (#3) | 18.0 (#5) | **18.0 (#4)** | Table 1 + Table 2 | — |
| K9E-PAT | 12.0 (#5) | 12.0 (#6) | **12.0 (#5)** | Table 1 | — |
| K9_E implementations | 12.0 (#8) | 12.0 (#7) | **12.0 (#6)** | Table 1 | — |
| K5_prospective | 12.0 (#9) | 12.0 (#8) | **12.0 (#7)** | Table 1 + Table 2 (Shared) | — |
| E1-E16 | 9.6 (#7) | 9.6 (#9) | **9.6 (#8)** | Table 1 + Table 2 | — |
| P10-TIM | 9.0 (#10) | 9.0 (#10) | **9.0 (#9)** | Table 1 | — |
| BE↔QM mapping | — | — | **9.6 (#10)** | Table 1 + Table 2 | NEW |

---

## Free Parameter Registry

Khong nam trong Top 10 (khong phai assumption), nhung can duoc track:

| # | Parameter | Value | Unit | Classification | Caveat |
|---|-----------|-------|------|----------------|--------|
| FP-1 | **β** (suppression strength) | 0.598 (Proietti D1) | [0, 1) dimensionless | FREE PARAMETER — measured, not derived | 1 dataset only. Cross-experiment pending. |
| FP-2 | β_universal | Modeling choice | — | MODELING CHOICE (Occam's razor) | Will be tested by 3-observer experiment |

---

## Audit Schedule (v1.3)

| Component | Table(s) | Next Audit | Frequency | Trigger |
|-----------|----------|-----------|-----------|---------|
| phi-map K→B(H) | Both | 2026-06-30 | Monthly | Moi Track B milestone |
| P10-NOISE | Table 1 | 2026-05-31 | Weekly | Truoc khi public "genuine" claim |
| T5 K_ctx | Both | 2026-05-31 | Weekly | Moi khi T3/T9 duoc update. Sync both tables. |
| T4-H Steps 3-4 | Both | 2026-06-30 | Monthly | Khi co resource |
| K9E-PAT | Table 1 | 2026-05-31 | Weekly | Moi khi re-analyze raw data |
| K9_E implementations | Table 1 | 2026-05-31 | Weekly | Moi numerical prediction |
| K5_prospective | Both | 2026-05-31 | Weekly | Moi khi K5/K9_E thay doi. Sync both tables. |
| E1-E16 | Both | 2026-06-30 | Monthly | Moi khi BE SOT thay doi |
| P10-TIM | Table 1 | N/A | On trigger | Khi raw event data available |
| BE↔QM mapping | Both | 2026-06-30 | Monthly | Moi khi mapping files thay doi |
| **β (Free Param)** | Table 1 | 2026-05-31 | Weekly | Moi experimental data moi |

---

## 3-Round RCA Design Verification (v1.3)

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Classification RCA — per-component scope split via 5-Why for borderline cases (T5, K5_prospective shared; P10-NOISE exclusive). 10/10 components classified correctly. | 5/5 | 4 Class C exclusive + 4 Full exclusive + 2 Shared. All classifications backed by 5-Why analysis. No misclassifications. |
| R2 | Scoring consistency — shared components (T5 K_ctx, K5_prospective) have identical H/W/A/Risk in both tables. | 5/5 | T5: 5/3/0.2/18.0 in both. K5_prosp: 5/2/0.2/12.0 in both. 0 divergence. |
| R3 | Two-table completeness — all v1.2 risks covered, no risks lost. Table 2 self-contained and independently readable. | 4.5/5 | All 10 v1.2 components present in Table 1. Table 2 has 6 Full+Shared. Minor: Table 2 may need expansion as new Full-scope risks are identified from EX compass or technical debt inventory. |
| **Aggregate** | | **4.83/5 PASS (>= 4/5)** | |

---

*Top 10 Hallucination Risk Record v1.3 — Dual-table architecture: Table 1 (VVV-QMRF Class C, 10 components) + Table 2 (VVV-QMRF Full Scope, 6 components). 2 shared components (T5 K_ctx, K5_prospective) with identical scores in both tables. 0 CRITICAL + 4 HIGH + 3 MEDIUM + 3 LOW. 0 hallucination that su (9-10). 3-Round RCA Classification Decision: 4.83/5. Next audit: 2026-05-31.*
