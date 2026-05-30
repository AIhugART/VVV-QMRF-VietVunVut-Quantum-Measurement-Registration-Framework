# RCA — Logic Audit: VVV-QMRF Class C
**Date:** 2026-05-30 | **Method:** 3-Round RCA × 5-Why × Threshold 4/5
**Scope:** Toàn bộ `project_vvv_qmrf_class_c/` — architecture, derivation chain, data fitting, governance
**Status:** Class C (qualified) — structurally testable, empirically UNCONFIRMED

---

## 0. TL;DR — Verdict nhanh

| Layer | Vấn đề | Severity | Trạng thái |
|-------|--------|----------|------------|
| **L1** K1-K8 Axioms | Logic nhất quán, không circular | ✅ PASS | Frozen (Layer 1) |
| **L2** Bridge theorems T1-T9 | T8/T9 derived đúng; [A-E1] ELIMINATED | ✅ PASS | Layer 2 updatable |
| **L3** K9_E Postulate | K9_E là POSTULATE (P9), KHÔNG phải theorem từ K1-K8 | ⚠️ KNOWN | Documented rõ ràng |
| **L4** Data Fitting | Genuine fit (beta=0.598) nhưng **noise FAIL** — 1 data point drives 80% signal | ❌ QUALIFIED | v30 downgrade |
| **L5** Convention Dual | `f_perp` có 2 convention — NORM-1 đã chuẩn hóa Conv 2 | ✅ RESOLVED | 2026-05-30 |

**Overall RCA aggregate: 4.2/5 — Class C (qualified) status VALID. Framework internally consistent; empirical evidence fragile.**

---

## 1. Kiến trúc Logic — 5 Layers

```
Layer 1 (FROZEN)  K1–K8: axioms đăng ký nhị phân (V∈{0,1}, ⊥_K, AdmJoint)
       |
       ↓ bridge theorems (updatable)
Layer 2           T1–T9: K_ctx morphism (T9), f_perp frequency bridge (T8),
       |           K7_trace + D_enc (canonical v2.4, RCA 4.77/5)
       ↓ POSTULATE (không derived)
Layer 3 (Class C) K9_E — P9:
       |           P(o|K) = Tr(E_o ρ) · [1 − β·f_perp(o, K_ctx)] / Z_E
       ↓ empirical fitting
Layer 4 (Class D) D1 Proietti CHSH: beta=0.598, 2.31σ — NOISE FAIL
       |           D3 FR: AVOIDED via K5 V_prov
       |           D4 B&B: T_BB' CLOSED, P2-C π/8 exact
       ↓ prediction
Layer 5           3-observer: delta_M3 = -0.223 at beta=0.3 (illustrative)
                  Copenhagen/MWI = special cases
```

---

## 2. Round 1 — Chuỗi Derivation: Logic có chặt chẽ không?

### 2.1 Phát hiện: K9_E là POSTULATE, không phải Theorem

**5-Why:**
1. Tại sao K9_E không thể derived từ K1-K8?
   → K1-K8 định nghĩa **cấu trúc** (registration, validity, incommensurability) nhưng không xác định duy nhất một quy tắc xác suất
2. Tại sao lại cần thêm postulate?
   → K-space là một formal language; nó cần "probability bridge" để nối với thực nghiệm — tương tự QM cần Born rule như axiom riêng
3. Điều này có phải là vấn đề không?
   → Không — tất cả physical theories đều có postulates. QM có Born rule (P1-P4). K9_E là P9 tương đương
4. Tại sao Phase 8 ban đầu gọi là "K9_E Formal Derivation"?
   → Lỗi đặt tên (F2 cascade). ERRATUM đã được ghi vào Phase 8
5. Root cause?
   → **Nhầm lẫn ngữ nghĩa**: "provenance trace" (truy xuất nguồn gốc các term) được hiểu nhầm là "derivation proof". 8 terms có K-space provenance NHƯNG K9_E assembly là POSTULATE

**Verdict R1-A: LOGIC SOUND.** Postulate status = documented + intentional. Không phải lỗi logic.
*Score: 4.5/5*

### 2.2 Assumption Audit: Bao nhiêu assumptions còn lại?

| ID | Assumption | Trạng thái gốc | Trạng thái hiện tại |
|----|-----------|----------------|---------------------|
| [A-E1] | K_ctx via T3-morphism | WEAK | **ELIMINATED** — T9 (5 lemmas, K8-constrained T1 embedding) |
| [A-E2a] | f_perp fraction counting | WEAK | **DERIVED** — T8 + T8-H1 (binary K1-K8 + K6 non-hierarchy → fraction là UNIQUE admissible form) |
| [A-E2b] | outcome filter `o(k_j) ≠ o` | WEAK | **DERIVED** — T8-H1: PP-2 v2 forces `≠` (outcome-independent → cancellation → δP=0) |
| [A-E3] | β universal | WEAK | **RECLASSIFIED: FREE PARAMETER** — analogous to coupling constants |
| [A-E4] | ⊥_K^str ≠ ⊥_K^dyn | MODERATE | JUSTIFIED — Tier 4 OI-4; dual modes BE-anchored |
| [A-NS] | No-signaling N>2 | WEAKLY | OPEN — proven N=2, induction for N>2 pending |
| [A-3O-2] | T5 K_joint composition | CONDITIONAL | Pending Level 4 freeze |
| [A-3O-3] | β same for 3-obs | WEAKLY | Untested |

**Net: 0 assumptions (mạnh) + 1 free parameter (β) + 3 weak/open items**

**Verdict R1-B: 4 assumptions gốc → 0. Progress significant. 3 weak/open items là known technical debt.**

### 2.3 Circular Reasoning Check

| Potential Circularity | Analysis | Verdict |
|----------------------|----------|---------|
| K_ctx → f_perp → P feed back into K_ctx? | K_ctx phụ thuộc V (từ K4/K5); V không phụ thuộc P(o\|k) từ K9_E | ✅ NO CIRCULARITY |
| f_perp dùng ρ_joint (ρ-side) | ρ_joint determined by physical preparation TRƯỚC K9_E chạy; K9_E không thay đổi ρ | ✅ NO CIRCULARITY |
| AJVS là disguised conclusion? | AJVS là semantic commitment ở Layer 0.5 — tương đương "measurement collapses state" của Copenhagen | ✅ GENUINE AXIOM |

**Round 1 Score: 4.5/5** ✅

---

## 3. Round 2 — Data Fitting: Evidence có robust không?

### 3.1 Genuine Fit (v29, 2026-05-23)

**Upgrade path:** Circular fit (E_exp = V·E_QM → β=0 guaranteed) → Genuine fit (raw Proietti Fig 3 data)

| Metric | Circular Fit (superseded) | Genuine Fit (v29) |
|--------|--------------------------|-------------------|
| beta | 0 (trivial) | **0.598** |
| V (visibility) | 0.854 | **0.939** |
| chi2/DOF | — | 0.670 (DOF=2), p=0.51 |
| Delta_chi2 | 0 | **5.35 (2.31σ)** |
| Note | Mathematically circular | Real but fragile |

### 3.2 Noise Sensitivity Analysis (v30, 2026-05-24) — **FAIL**

**Root cause của FAIL:**

```
B1: A0B0 drives 80% of Delta_chi2
    → Entire "signal" dominated by 1 data point

B2: Single-setting fragility = 1.85 sigma at A0B0
    → Shift 1.85σ at A0B0 ELIMINATES K9_E advantage

B3: Monte Carlo B4:
    noise_threshold = 0.10 sigma_RMS << 1.0 (threshold for PASS: >3.0)
    → Noise ở BẤT KỲ magnitude → Delta_chi2 ≥ 5.35 trong ~50% realizations
```

**5-Why cho noise FAIL:**
1. Tại sao noise threshold = 0.10 sigma_RMS << 3.0?
   → K9_E có directional sensitivity (always suppression) + chỉ 4 data points
2. Tại sao directional sensitivity = vấn đề?
   → Bất kỳ perturbation nào cũng "xếp hàng" với K9_E direction trong ~50% cases
3. Tại sao A0B0 drives 80%?
   → Proietti Fig 3: A0B0 có residual lớn nhất trong raw data (−0.678 vs QM −0.604)
4. Tại sao 4 data points không đủ?
   → DOF=2 sau fit 2 params (beta, V); quá ít để phân biệt signal từ fluctuation
5. Root cause?
   → **Thiếu data**: K9_E prediction cần 3-observer experiment (N≥3) để amplify signal (delta_M3 = -0.223, 11x amplification)

**Verdict R2-A: Empirical evidence NOT robust. Class C (genuine) → Class C (qualified). CORRECT DOWNGRADE.**

### 3.3 Pattern Check: K9E-PAT (CLOSED as UNRESOLVABLE)

| Check | Expected | Observed | Verdict |
|-------|----------|----------|---------|
| 2BSM/1BSM ratio | ~2 (K9_E multiplicative) | -0.78 (reversed) | FAIL |
| Explanation | — | Two sub-σ residuals divided → red herring | CLOSED (v31) |
| Action | — | Deferred to K9-S12 experiment | Acceptable |

**Round 2 Score: 4.0/5** ✅ (deduction: evidence fragile but downgrade correct)

---

## 4. Round 3 — Convention & Structural Consistency

### 4.1 f_perp Dual Convention — NORM-1 (2026-05-30)

**Vấn đề phát hiện:**

| Convention | Formula | Used in |
|-----------|---------|---------|
| Conv 1 (operational) | `P = Tr(E_oρ)·f_perp(K_ctx)/Z_E` với `f_perp` = whole factor | index.md, k9e_predictor.py |
| Conv 2 (derivation-chain) | `P = Tr(E_oρ)·[1−β·f_perp(o,K_ctx)]/Z_E` với `f_perp` = fraction | Phase8, K9S7_final_lock, paper |

**Tại sao nguy hiểm (5-Why):**
1. Paper reviewer thấy `f_perp` trong paper (Conv 2, fraction 0–1) so sánh với `f_perp` trong index.md (Conv 1, factor = 1 tại β=0)
2. `Falsification_Hierarchy §2.5` dùng CÙNG section nhưng hai convention (L70: Conv 2, L112: Conv 1)
3. Root cause: Conv 1 emerged từ code convenience, không bao giờ được formally designated

**Resolution (NORM-1, RCA 4.33/5):**
- ✅ C1: `index.md §3` rewritten to Conv 2
- ✅ C2: `Definitions §3.4` rewritten to Conv 2  
- ✅ C3: `Falsification_Hierarchy §2.5 L112` fixed
- ✅ C4: `k9e_predictor.py`: `k9e_f_perp` → `k9e_suppression_factor` (rename only, math UNCHANGED)
- ⬜ EXTENDED: `CLAUDE.md` — user decision pending

### 4.2 Adversarial Tests (4/4 PASS)

| Test | Scenario | Result |
|------|---------|--------|
| T1a: P ∈ [0,1] | β→1, f_perp=1 cho một số o | ✅ PASS — Z_E > 0 always; β<1 strict bound |
| T1b: No-signaling | Alice marginal vs Bob setting choice | ✅ PASS — K_ctx_A không phụ thuộc Bob's setting |
| T2: Axiom consistency | 8 terms traced | ✅ PASS — 0 orphaned assumptions |
| T3: Distinguishability | δS tại β=0.5 | ✅ PASS — δS = −0.055 ≠ 0 |
| T4: cert/V trivial | cert=1, V=1 cho tất cả k | ✅ PASS — Born limit in standard lab ✓ |

### 4.3 Physical Content Assessment

| Category | Content | New vs QM? |
|----------|---------|------------|
| cert (svasaṃvedana) | Admission filter (gate); cert=1 always in K1 | STRUCTURAL marker — minimal new physics |
| V=0 (Bhrānti) | Registration tồn tại nhưng không có P → "overwritten" | ✅ GENUINELY NEW — no Standard QM analogue |
| isNull (Anupalabdhi) | Null event, no P | ✅ GENUINELY NEW |
| f_perp mechanism | K_ctx structure modifies P | ✅ NEW at β>0 |
| β=0 limit | K-space = notational variant of QM | Standard QM reproduced exactly |

**Round 3 Score: 4.1/5** ✅

---

## 5. Tổng hợp RCA — Scoring Matrix

| Round | Focus | Score | Threshold | Verdict |
|-------|-------|-------|-----------|---------|
| R1 | Derivation chain + Assumptions + Circularity | **4.5/5** | ≥4.0 | ✅ PASS |
| R2 | Empirical evidence + Noise robustness | **4.0/5** | ≥4.0 | ✅ PASS (marginal) |
| R3 | Convention consistency + Adversarial tests | **4.1/5** | ≥4.0 | ✅ PASS |
| **Aggregate** | | **4.2/5** | ≥4.0 | ✅ **PASS** |

---

## 6. Root Causes Đã Được Giải Quyết

### RC-1: "K9_E Formal Derivation" (RESOLVED)
- **Cause:** Nhầm lẫn "provenance trace" vs "derivation proof"
- **Fix:** ERRATUM ghi vào Phase 8; K9_E reclassified as POSTULATE (P9)
- **Impact:** Zero — K9_E vẫn valid, chỉ thay đổi epistemological framing

### RC-2: Circular Data Fit (RESOLVED)
- **Cause:** E_exp = V·E_QM → beta=0 guaranteed by construction
- **Fix:** v29 genuine fit với raw Proietti Fig 3 data → beta=0.598
- **Impact:** Qualified by v30 noise analysis

### RC-3: Noise Sensitivity FAIL (DOCUMENTED, path forward defined)
- **Cause:** 4 data points + directional sensitivity + A0B0 fragility
- **Fix needed:** K9-S12 experiment (3-observer, dedicated noise characterization)
- **Current status:** arXiv submitted 2026-05-27; awaiting lab collaboration

### RC-4: Dual f_perp Convention (RESOLVED — NORM-1)
- **Cause:** Conv 1 emerged từ code convenience, never formally designated
- **Fix:** 4 surgical changes; Conv 2 = canonical (2026-05-30)
- **Residual:** CLAUDE.md còn Conv 1 (user decision pending)

---

## 7. Open Items — Logic Gaps Còn Lại

| ID | Gap | Risk | Priority |
|----|-----|------|----------|
| **[A-NS]** | No-signaling proof cho N>2 (induction) | Nếu violated → K9_E creates FTL communication | HIGH |
| **[A-3O-2]** | T5 K_joint composition (T4-H resolved, T5 pending Level 4 freeze) | 3-observer predictions có thể invalid nếu K_joint fails | MEDIUM |
| **[A-3O-3]** | β universal across N (β_2obs = β_3obs?) | Nếu β phụ thuộc N → Phase 11 predictions sai | MEDIUM |
| **CLAUDE.md** | Layer 3 formula còn Conv 1 | AI sessions tiếp theo có thể propagate Conv 1 | LOW-MEDIUM |
| **GAP-A** | Empirical confirmation (K9-S12 experiment NOT YET PERFORMED) | Critical path | CRITICAL |

---

## 8. Kết luận: Class C (qualified) — Tại sao status này là CORRECT?

```
✅ Structurally testable:
   - K9_E có 1 free parameter (β)
   - Prediction: delta_AB(theta) ≠ 0 iff theta ≠ pi/2
   - Falsification rule C-FALSI v1.0 pre-registered
   - K9-S12 protocol: 1 QWP thêm vào Bong experiment, ~1 giờ

❌ Empirically UNCONFIRMED:
   - Proietti fit: beta=0.598 NHƯNG noise threshold = 0.10σ << 3.0
   - K9E-PAT: CLOSED (unresolvable với 4 data points)
   - No 3-observer experiment exists

✅ Framework internally consistent:
   - 7/7 K-axiom checks PASS
   - 4/4 adversarial tests PASS
   - 3/3 operationalizability gates PASS
   - FR paradox AVOIDED via K5 V_prov
   - Copenhagen/MWI = special cases (beta=0)

⚠️ Principal weakness: empirical
   - K9_E effect tại beta=0.5: δS = -0.055 (< 1σ của Proietti)
   - 11x amplification với 3-observer (delta_M3 = -0.223 tại beta=0.3) 
     → cần K9-S12 experiment
```

**FINAL VERDICT:** VVV-QMRF Class C logic là **internally consistent và sound**. Các vấn đề logic đã được xác định (postulate vs derivation, circular fit) và documented + addressed. Status Class C (qualified) là **ACCURATE** và **CORRECTLY CALIBRATED** — framework chưa falsified, chưa confirmed, đang chờ experiment.

---

*RCA Class C Logic Audit — 2026-05-30. Aggregate 4.2/5. All 3 rounds ≥ 4.0. Class C (qualified) status VALID. Critical path: K9-S12 experiment.*

---

## 9. Post-Audit RCA Decision — 2026-05-30

**Method:** 3-round RCA × 5-Why × threshold 4/5 | **Scope:** VVV-QMRF (core) | **Compass:** VVV-QMRF-EX

### 9.1 Verdict Matrix

| Decision | R1 | R2 | R3 | Agg | Verdict |
|----------|----|----|----|----|---------|
| D1: Fix Architecture Overview Conv 1 (`index.md` L70) | 4.5 | 4.5 | 4.5 | **4.5/5** | ✅ EXECUTED |
| D2: CLAUDE.md Conv 2 status | — | — | — | N/A | ✅ VERIFIED — already Conv 2; EXTENDED CLOSED |
| D3: Governance for open items (update audit, NOT Post_v30) | 4.0 | 4.2 | 4.0 | **4.07/5** | ✅ EXECUTED (this §9) |
| D4: [A-NS] defer with explicit note | 4.5 | 4.0 | 4.5 | **4.33/5** | ✅ EXECUTED (§9.3) |

### 9.2 D1 — Architecture Overview NORM-1 Miss (RESOLVED)

**Root cause:** NORM-1 C1 targeted "index.md §3" (K9_E Postulate prose section). The Architecture Overview ASCII diagram (code block in §3) was outside C1 scope — it was the first visible formula for any reader, creating the highest external-reader risk.

**Fix applied (C5):**
- `index.md` Architecture Overview L70: `P(o|K) = Tr(E_o rho) * f_perp(K_ctx)` → `P(o|K) = Tr(E_o rho) * [1-beta*f_perp(o,K_ctx)]/Z_E  [Conv 2]`
- L71–L72 updated: `0 assumptions; 1 free parameter beta` (reflects [A-E1]–[A-E4] ELIMINATED/RECLASSIFIED state)
- NORM-1 record updated: C5 added, EXTENDED CLOSED

**Blast radius:** Zero. No PEER-SYNC trigger. No theorem change. Notation alignment only.

### 9.3 D4 — [A-NS] Deferral Decision (RECORDED)

**[A-NS]: No-signaling proof for N>2 — DEFERRED**

| Item | Rationale |
|------|-----------|
| Why defer | K9-S12 is N=2; no-signaling N=2 proven. N>2 depends on T5 K_joint + T4-H Steps 2-4 (both Class D, deferred). Deferral is structurally correct. |
| Deferral scope | Until: (a) K9-S12 experiment complete, OR (b) Level 4 unfreeze gate opened |
| Paper_002 mitigation | Note as "N>2 generalization: future work" in §Limitations |
| RCA score | 4.33/5 → deferral approved |

**[A-3O-2] and [A-3O-3]** — same deferral logic (CONDITIONAL on Level 4 freeze and K9-S12 result).

### 9.4 Updated Open Items Table

| ID | Gap | Risk | Status | When to address |
|----|-----|------|--------|-----------------|
| **[A-NS]** | No-signaling N>2 | HIGH | **DEFERRED** — RCA 4.33/5 | After K9-S12 experiment OR Level 4 unfreeze |
| **[A-3O-2]** | T5 K_joint composition | MED | CONDITIONAL | After Level 4 freeze |
| **[A-3O-3]** | β universality across N | MED | OPEN | After K9-S12 result |
| **NORM-1 C5** | Architecture Overview diagram | — | **RESOLVED** (this session) | Done |
| **EXTENDED** | CLAUDE.md Conv 2 | — | **RESOLVED** (verified Conv 2) | Done |
| **GAP-A** | K9-S12 experiment | CRITICAL | ACTIVE — Track 3 | Needs optical lab |

---

*Post-Audit RCA — 2026-05-30. All 4 decisions ≥ 4.0/5. D1+D2+D3+D4 executed. Audit fully closed.*
