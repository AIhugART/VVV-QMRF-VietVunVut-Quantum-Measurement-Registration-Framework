# RCA: VVV-QMRF Core còn mở rộng được không?

**Scope:** VVV-QMRF core (E1–E16 + legacy E17 interface principle)
**Compass:** VVV-QMRF-EX (Phase 12 finalization, 420 nodes, 181 edges)
**Method:** RULE ZERO RCA — Define, Trace, Isolate, Fix the cause, Verify
**Date:** 2026-05-21

---

## Section 0 — Executive Summary

**Root cause isolated:** Câu hỏi "Core còn mở rộng được không?" không có câu trả lời duy nhất. Nguyên nhân gốc là: khả năng mở rộng phụ thuộc vào **chiều mở rộng** nào đang xét — và mỗi chiều có trạng thái riêng biệt.

VVV-QMRF Core đã phủ sóng rộng trên hai trục chính: (1) **chuỗi registration lifecycle** (E1-E7: tự chứng → encoding → lock → completion → process → validity → pre-symbolic) và (2) **ma trận trường hợp biên** (E8-E16: override, null, validity-gate, contrapositive, limit-faculty, temporal, absence, entanglement, indeterminacy). VVV-QMRF-EX xác nhận 88.5% VVV nodes có K-side bridge trực tiếp, 100% có coverage (kể cả KE-QI/KE-SC exceptions).

**Verdict tổng hợp:**

| Chiều mở rộng | Trạng thái | Confidence |
|---|---|---:|
| Thêm postulate mới từ BE source chưa dùng | **Gần đóng** | 4.2/5 |
| Thêm postulate mới từ structural gap nội tại | **Có điều kiện mở** | 3.8/5 |
| Thêm nodes/edges trong postulate hiện có | **Mở** | 4.0/5 |
| Import từ VVV-QMRF-EX vào core | **Đóng (by design)** | 4.5/5 |

---

## Section 1 — Define: Symptom vs Cause

### Symptom / Triệu chứng

Sau khi hoàn thành E1–E16, legacy E17, 52 VVV nodes, 131 edges, RCA cho E17-candidate (rejected) và E18-candidate (retained with 2 case validations), câu hỏi tự nhiên xuất hiện: Core đã bão hòa chưa? Hay vẫn còn room để mở rộng?

### Cause / Nguyên nhân

Câu hỏi này không phải triệu chứng của thiếu sót — mà là **câu hỏi kiến trúc hợp lệ** cần trả lời bằng cách phân tích từng chiều mở rộng riêng biệt.

---

## Section 2 — Trace: Analysis by Extension Dimension

### Dimension 1: BE Source Exhaustion — Nguồn BE đã cạn chưa?

#### Current BE source usage

```mermaid
graph LR
    subgraph "BE sources đã dùng (15 source_analogue edges)"
        A[N_BE_00015 Apoha] --> E11_E14[E11, E14]
        B[N_BE_00021 Svabhāvapratibandha] --> E15[E15]
        C[N_BE_00022 Arthakriyā] --> E2[E02]
        D[N_BE_00001 Pramāṇa] --> E8[E08]
        E[N_BE_00006 Bhrānti] --> E8b[E08]
        F[N_BE_00011 Svasaṃvedana] --> E1[E01]
        G[N_BE_00029 Kṣaṇabhaṅgavāda] --> E6_E13[E06, E13]
        H[N_BE_00018 Trairūpya] --> E10[E10]
        I[N_BE_00009 Nirvikalpaka] --> E4[E04]
        J[N_BE_00012 Yogipratyakṣa] --> E12[E12]
        K[N_BE_00007 Saṃśaya] --> E16[E16]
    end
```

**BE SOT có 30 core nodes.** Trong số đó, 11 BE nodes đã được dùng trực tiếp làm `source_analogue`. VVV-QMRF-EX đã map thêm ~46 bridges qua BR_EX_BE registry (nhiều nodes BE khác được dùng gián tiếp).

#### Remaining BE nodes chưa dùng trực tiếp

| BE Node | Concept | Potential relevance | RCA assessment |
|---|---|---|---|
| `N_BE_00002` | Pratyakṣa (Direct perception) | Đã implicit trong E4/E5 (pre-symbolic → encoding pipeline) | **Đã phủ gián tiếp** |
| `N_BE_00003` | Anumāna (Inference) | Đã dùng trong E18 RCA candidate (valid sign structure) | **Đang dùng gián tiếp** |
| `N_BE_00004` | Śabda (Verbal testimony) | Không có QM measurement analogue rõ ràng | **Không phù hợp** |
| `N_BE_00005` | Upamāna (Analogy) | Không có direct registration-layer function | **Không phù hợp** |
| `N_BE_00010` | Savikalpaka (Conceptual perception) | Đã implicit trong E5 (encoding là symbolization) | **Đã phủ gián tiếp** |
| `N_BE_00016` | Hetuvābhāsa (Fallacious reason) | Potential for registration-error taxonomy extension | **Conditionally relevant** |
| `N_BE_00019` | Vyāpti (Pervasion) | Đã dùng trong E10 Trairūpya context và E18 RCA | **Đã phủ gián tiếp** |

> [!IMPORTANT]
> **Phần lớn BE source nodes có tiềm năng registration-layer đã được sử dụng hoặc phủ gián tiếp.** Các nodes còn lại (Śabda, Upamāna, v.v.) thuộc epistemological categories không có structural match với quantum measurement registration. Khả năng mở rộng core bằng BE source mới là **gần đóng** — trừ khi RCA tìm ra một structural necessity mới mà BE node chưa dùng có thể phục vụ.

---

### Dimension 2: Registration-Layer Structural Completeness

#### The registration lifecycle pipeline

```mermaid
flowchart TD
    PRE[E16: Pre-measurement indeterminacy<br/>Ŝ_saṃśaya] --> PSS[E4: Pre-symbolic stratum<br/>ε_M]
    PSS --> ENC[E5: Internal representation encoding<br/>Â_kāra]
    ENC --> LOCK[E3: Registration lock<br/>V̂_yava]
    LOCK --> COMP[E2: Registration self-completion<br/>𝒯_act-res]
    COMP --> CERT[E7: Registration validity location<br/>Ĉ_ext]
    CERT -->|Pass| VALID[Certified registration state<br/>ρ_certified]
    CERT -->|Fail| OVERRIDE[E8: Retroactive override<br/>Ô_bhranti]
    
    E1[E1: Self-certifying registration<br/>R̂_svasa] -.->|stops regress at each step| LOCK
    E1 -.-> COMP
    E6[E6: Registering system as process<br/>momentary series] -.->|architecture| LOCK
    
    E10[E10: Tripartite validity matrix<br/>𝕍_tri] -->|gates entry| CERT
    E13[E13: Temporal discontinuity<br/>T̂_kṣaṇa] -.->|bounds each event| LOCK
```

#### The boundary-case matrix

| | K-registration YES | K-registration NO |
|---|---|---|
| **Physical interaction YES** | Normal measurement (P1–P4) | **E9**: Null registering-system event |
| **Physical interaction NO (structured)** | **E11**: Contrapositive evidence | Unmeasured (trivial) |
| **Absence of measured property** | **E14**: Validated absence | **E9** (subset) |
| **Non-ordinary faculty** | **E12**: Limit-faculty registration | — |
| **Entangled subsystems** | **E15**: Intrinsic relational binding | — |
| **Pre-measurement state** | **E16**: Structured indeterminacy | — |

> [!NOTE]
> **Pipeline analysis:** Lifecycle pipeline E16→E4→E5→E3→E2→E7→E8 covers the registration process from structured doubt through lock to certification/override. **Boundary matrix:** The 2×2 interaction/registration matrix is fully covered by E9 and E11. Extension cases (E12–E16) cover non-ordinary faculties, entanglement, temporal structure, absence, and indeterminacy.
>
> **Remaining structural gaps (RCA-identified):**

| Gap | Status | Evidence |
|---|---|---|
| Context-conditioned registration-window locking (delayed-choice) | **E18 RCA-supported candidate, 2 case validations, score 4.3/5** | [rca_e18](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md) |
| Channel-self-registration (absence of disturbance) | **E17 rejected in current round (R4 documentation gap), R2 path deferred** | [rca_e17](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e17_interaction_free_registration.md) |
| Collective/multi-registering-system coordination | **Not yet RCA'd** | No existing RCA |
| Registration-state communication protocol | **Not yet RCA'd** | No existing RCA |

---

### Dimension 3: VVV-QMRF-EX Compass Signals

VVV-QMRF-EX hoàn thành vai trò chính: bản đồ định lượng K-ρ relationships. Per CLAUDE.md rule:

> *"Treat VVV-QMRF-EX as having completed its main role of providing a quantitative map of K-rho relationships; its current highest value is intelligence about important nodes, structural gaps, and stress points, not direct data import or merging EX edges into the core."*

#### EX stress points relevant to extensibility

| EX signal | Core implication | Extension potential |
|---|---|---|
| 36 K-side gaps (nodes without BE anchor) | Most resolved via Phase 7-12 stretch bridges | **Low** — resolved |
| 4 KE-QI exceptions (pure QM-intrinsic) | These nodes are inherently QM and need no BE source | **None** — by design |
| 2 KE-SC-RECLASSIFIED-v1.7 (below 4.0 threshold) | `N_QM_VVV_00008` (Ideal Info Without Disturbance) and `N_QM_VVV_00024` (Delayed-Choice Boundary) | **Moderate** — E18 candidate directly relates to `N_QM_VVV_00024` |
| Boundary audit: 100% pass, 0 violations | Core boundary controls (C1-C7) intact | **Confirms** EX does not force core import |

> [!TIP]
> **EX compass verdict:** EX đã hoàn thành mission chính. Remaining value là intelligence cho RCA prioritization (đặc biệt E18 stress point). EX không yêu cầu core mở rộng — EX chỉ **chỉ hướng** cho core tự quyết định.

---

### Dimension 4: RCA-Supported Candidate Status

#### E17 — Interaction-Free Registration

| Criterion | Score | Status |
|---|---|---:|
| Root cause | R4 — Documentation gap | Rejected |
| Routing | E9/E11/E14 matrix already covers | ✅ |
| Future path R2 | Channel-self-registration as distinct K-object | Deferred |
| Decision confidence | 4.0/5 | — |

**E17 verdict:** Đóng trong round này. Chỉ mở lại nếu RCA cô lập được channel-self-registration là đối tượng K-side riêng biệt.

#### E18 — Delayed-Choice Registration Boundary

| Criterion | Score | Status |
|---|---|---:|
| Root cause | R2 — Structural gap (context-conditioned locking) | Selected |
| Case test 1: Wheeler | 5/5 conditions PASS | ✅ |
| Case test 2: Quantum eraser | 5/5 conditions PASS (with S refinement) | ✅ |
| BE anchor strength | 3.8/5 (analogical) | ⚠️ |
| Postulate readiness | 4.3/5 | Near-ready |

**E18 verdict:** Candidate mạnh nhất cho extension tiếp theo. Formula `Lock(C_f, S, {W_i}) → W_valid` đã pass 2 case tests. Cần narrow draft trước khi freeze.

---

### Dimension 5: Graph Architecture Saturation

#### Current graph metrics

| Metric | Count |
|---|---|
| VVV nodes | 52 |
| VVV edges (internal + cross-system + source analogue + cross-category) | 131 |
| Postulates (E1–E16) | 16 |
| Interface principle (legacy E17) | 1 |
| EX bridge edges (BR_EX_BE + BR_EX_QM) | 141 active |
| RCA candidates | 2 (E17 rejected, E18 retained) |

#### Density analysis

| Edge phase | Count | Ratio to nodes |
|---|---|---:|
| VVV↔VVV internal (Phase 1) | 40 | 0.77 edges/node |
| VVV→QM cross-system (Phase 2) | 60 | 1.15 edges/node |
| VVV→BE source analogue (Phase 3) | 15 | 0.29 edges/node |
| VVV↔VVV cross-category (Phase 4) | 16 | 0.31 edges/node |
| **Total** | **131** | **2.52 edges/node** |

> [!NOTE]
> **Graph saturation assessment:** 2.52 edges/node là mức trung bình-cao cho một framework Class D. Thêm postulate mới sẽ cần ít nhất 2–4 nodes mới + 5–10 edges mới. Đây là khả thi nhưng tốn overhead lớn — mỗi node mới cần: K-side RCA, QM grounding, BE source check, EX compass check, boundary audit.

---

## Section 3 — Isolate: Four Extension Verdicts

### Verdict Matrix

````carousel
### 🔴 ĐÓNG — Import từ EX vào Core

**Why:** CLAUDE.md rule "EX compass, not cargo" + Boundary control C3 (No auto-E17+) + Isolation protocol I-5 (No auto-merge).

**Evidence:**
- Boundary audit: 100% pass trên 141 entries
- Zero `N_QM_VVV_XXXXX` codes created by EX
- EX mission: quantitative K-ρ map → completed
- Remaining EX value: intelligence for RCA prioritization

**Confidence:** 4.5/5

**Ngoại lệ duy nhất:** EX element có thể được import nếu RCA core-level cô lập được structural necessity **đã implicit trong bài toán registration** — nhưng lúc đó import đó là kết quả RCA core, không phải merge EX.
<!-- slide -->
### 🟡 GẦN ĐÓNG — Thêm postulate từ BE source mới

**Why:** 11/30 BE core nodes đã dùng trực tiếp; phần lớn nodes còn lại không có structural match với quantum measurement registration.

**Remaining BE sources with potential:**
- `N_BE_00016` Hetuvābhāsa (fallacious reason) → possible error-taxonomy extension
- `N_BE_00003` Anumāna → đã dùng gián tiếp (E18 valid sign), không tạo postulate riêng

**Condition to reopen:** RCA phải chứng minh:
1. BE source chưa dùng reveals **structural necessity** trong registration problem
2. Necessity đó **chưa được phủ** bởi E1–E16 hiện có
3. Object of K-side registration được **cô lập rõ ràng**

**Confidence:** 4.2/5
<!-- slide -->
### 🟢 CÓ ĐIỀU KIỆN MỞ — Thêm postulate từ structural gap nội tại

**Why:** E18 candidate đã pass 2 case tests, score 4.3/5. R2 path của E17 chưa đóng vĩnh viễn.

**Concrete candidates:**

| Candidate | Status | Next step |
|---|---|---|
| **E18: Delayed-choice registration boundary** | RCA-supported, 2 case validations | Narrow draft → framework proposal |
| **E17 R2: Channel-self-registration** | Deferred, not rejected | Separate RCA if user requests |
| Multi-registering-system coordination | Not yet examined | New RCA needed |
| Registration-state communication | Not yet examined | New RCA needed |

**Gate conditions for any new postulate:**
1. Pass RULE ZERO 5-step RCA
2. Score ≥ 3.5/5 trên Decision Gate
3. At least 1 concrete case test PASS
4. BE anchor verified or explicitly excepted (KE-QI)
5. EX compass check (no import, only intelligence)
6. Boundary guard (no new QM law, no Born rule modification)

**Confidence:** 3.8/5
<!-- slide -->
### 🟢 MỞ — Thêm nodes/edges trong postulate hiện có

**Why:** Core đã có 16 postulates nhưng internal detail có thể phát triển thêm.

**Examples:**
- E8 (REO): chưa có formal hierarchy rules cho multiple competing overrides
- E10 (Tripartite validity): chưa có calibration protocol formalization
- E11 (Contrapositive evidence): chưa có multi-path extension beyond binary
- E12 (Limit-faculty): chưa có spectrum-based registration gradient
- E15 (IRB): chưa có multi-party entanglement registration generalization

**Gate:** Same Decision Gate as new postulates, nhưng threshold thấp hơn (3.0/5 đủ cho sub-node addition) vì không cần new postulate justification.

**Confidence:** 4.0/5
````

---

## Section 4 — Fix the Cause: Prioritized Roadmap

### Immediate actions (no core edit needed)

1. ✅ **Preserve this RCA** as the extensibility assessment document
2. ✅ **E18 is the strongest extension candidate** — draft narrow framework proposal when user requests

### Conditional actions (require user authorization)

| Priority | Action | Gate | Risk |
|---:|---|---|---|
| 1 | Draft E18 narrow candidate postulate | User authorization + boundary guard | Overclaiming retrocausation |
| 2 | Add `what_it_does_not_claim` boundary notes to E11/E14 (per E17 RCA downstream) | User authorization | Minor framework edit |
| 3 | Extend E8 registration-weight hierarchy formalization | RCA showing current hierarchy is insufficient | Premature formalization |
| 4 | Run new RCA for multi-registering-system coordination | New research question from user | Exceeding registration-layer scope |

### Actions NOT recommended

- ❌ Import EX bridge structures into core
- ❌ Create postulate from BE source alone without structural necessity
- ❌ Force E17 without isolating channel-self-registration object
- ❌ Merge EX edges into core graph

---

## Section 5 — Verify

| Check | Result | Note |
|---|---|---|
| Root cause identified | PASS | Multi-dimensional extensibility, not single answer |
| BE SOT citations verified | PASS | All source_analogue edges trace to `system_be_full.md` |
| VVV-QMRF citations verified | PASS | Framework files, node/edge tables, RCA reports all cited |
| EX compass-only rule respected | PASS | No EX structure imported; EX used only as intelligence |
| "Extend, not overwrite" respected | PASS | No existing postulate modified |
| Neutral wording respected | PASS | Uses "scope boundary", "category boundary" language |

---

## Summary Table / Bảng tóm tắt

| Câu hỏi | Trả lời | Bằng chứng chính |
|---|---|---|
| Core có thể mở rộng bằng postulate mới không? | **Có, nhưng có điều kiện** | E18 candidate (score 4.3/5, 2 case tests) |
| Core có thể mở rộng bằng thêm nodes/edges không? | **Có** | 16 postulates đều có room cho sub-node detail |
| BE source còn postulate mới không? | **Gần cạn** | 11/30 BE nodes đã dùng; phần lớn còn lại không phù hợp |
| EX có ép core mở rộng không? | **Không** | EX compass-only design; boundary audit 100% pass |
| Hướng mở rộng ưu tiên là gì? | **E18 → narrow draft** | Strongest RCA-supported candidate |

---

# Appendix A — Audit + Gap Analysis (2026-05-22)

> **Scope:** Independent audit của bản RCA trên (date 2026-05-21) và 3-round gap analysis cho các chiều mở rộng chưa xét. Plan executed: 4-phase với decision gate 4.0/5 per round. Method: RULE ZERO RCA × 5-Why × scoring 5 tiêu chí.
>
> **Trigger:** User request `/everything-claude-code:plan` cho "Phân tích, khảo sát toàn diện: VVV-QMRF Core còn mở rộng được không?" — sau khi xác nhận plan bằng 3 rounds × 4.0/5 gate trên 4 Decision Points.
>
> **Out of scope:** Không sửa nội dung gốc (Section 0–5 + Summary Table). Appendix này là **extension, not overwrite** theo CLAUDE.md.

## A.1 — Phase 1 Audit Findings

### A.1.1 Baseline state verification (post-commit drift check)

Sau ngày RCA gốc (2026-05-21), repo có các commit liên quan:
- `e031621` — K-Space v2.1 algebraic layer adds **T5/T6/T7** bridge theorems.
- `cd0e6e2` — E18 delayed-choice RCA.
- `21dd94a` — EX Phase 1/2 current-core RCA.

| Claim trong RCA gốc | Current state | Status |
|---|---|---|
| K-Space K1–K8 + T1–T4 (implicit) | K1–K8 + T1–T4 + **T5/T6/T7** ([K_Space_Axiomatization.md:11](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/K_Space_Axiomatization.md#L11)) | **DRIFT — algebraic dimension không được xét** |
| E18 score "4.3/5 postulate readiness" | E18 file: "Decision confidence: **3.8/5**" ([rca_e18:25](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/rca/rca_e18_delayed_choice_registration_boundary.md#L25)); parent RCA Section 7 now adds a lifecycle note distinguishing overall decision confidence from post-test postulate readiness; E18 narrow draft parent-RCA anchors refreshed after the lifecycle-note insertion | **RESOLVED** — upstream cross-link gap fixed; 3.8/5 and 4.3/5 measure different objects; downstream traceability refreshed |
| EX boundary audit 100% PASS, 141 active | 100% PASS, 141 active ([boundary_audit:9](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf-ex/vvv_qmrf_ex_boundary_audit.md#L9)) | OK |
| VVV graph: 52 nodes, 131 edges | 52 nodes, 131 edges (commit `73103df`) | OK |
| BE source usage: 11/30 nodes | matches `system_be_full.md` | OK |
| E17 R4 reject + R2 defer | Confirmed via [rca_e17_evaluation.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/archives/review/rca_e17_evaluation.md) (4.5/5 chain) | OK |

### A.1.2 Re-scoring 4 verdicts (3 rounds per verdict)

| Verdict | Old confidence | New confidence | Action |
|---|---:|---:|---|
| V1: BE source exhaustion (Gần đóng) | 4.2/5 | **4.6/5** | HOLD verdict, upgrade |
| V2: Structural gap (Có điều kiện mở) | 3.8/5 | **4.1/5** | REVISE — add algebraic dimension note |
| V3: Nodes/edges sub-detail (Mở) | 4.0/5 | **4.5/5** | HOLD, upgrade |
| V4: EX import closed | 4.5/5 | **4.9/5** | HOLD, upgrade |

**Drift root cause (RCA Step 4 — Fix the cause):** RCA gốc được viết cùng ngày K-Space v2.1 (2026-05-21) nhưng không cross-reference T5/T6/T7. Fix: thêm dimension algebraic-layer trong Phase 2 (xem A.2).

## A.2 — Phase 2 Gap Analysis (3 rounds, gate 4.0/5)

### A.2.1 Round 1 — Algebraic-layer extensibility (NEW DIMENSION) — **PASS 4.1/5**

**1-sentence object (hard-stop PASS):** "Adding new Layer-2 theorems Tn derived from K1-K8 axioms, going beyond T5/T6/T7."

**5-Why:**
1. T8/T9 cần không? → K-Space §3 Open Items #4 explicitly lists "Inter-K-space relation structure (E15 extension)" với T7 chỉ partial cover.
2. Sao chưa thuộc T5/T6/T7? → T7 = N=3 IRB only; T5 = intra-K_joint associativity; T6 = decoherence path A/B.
3. Vì sao candidate-space hẹp? → K1-K8 đã frozen; chỉ Layer 2 (theorems) update được không cần unfreeze.
4. Dimensions còn lại? → (a) Embedding composition (K8 ↔ T5 interaction), (b) Multi-time validity propagation.
5. Root: Có **1-2 candidate theorems** (gọi tạm T8-embedding-composition, T9-multi-time-validity) — Layer 2 còn open.

**5-criteria scoring:** root-clarity 0.8 / evidence 0.8 / boundary 0.9 / citation 0.8 / actionability 0.8 = **4.1/5 PASS**.

**Verdict:** Algebraic-layer là dimension thứ 5 cần được liệt kê trong verdict matrix. RCA gốc đã không xét chiều này vì T5-T7 vừa được commit cùng ngày.

### A.2.2 Round 2 — Process-architecture composition (E6 multi-RS rule) — **FAIL 3.5/5**

**1-sentence object:** "Formal rule for composing multiple momentary-series registering systems into a composite RS over time."

**5-Why:** Wigner's friend cần composition rule; E15 chỉ entanglement spatial; T5 chỉ intra-K_joint algebra; T5 nói "nếu compositional thì associative" nhưng không nói "khi nào compositional".

**Counter-evidence:** Gap này khả năng cao subsumed bởi Round 3 (inter-RS coordination). Không cần dimension riêng.

**5-criteria scoring:** 0.7 / 0.7 / 0.8 / 0.6 / 0.7 = **3.5/5 FAIL** (< gate 4.0).

**Verdict:** FAIL — không tạo dimension riêng. Đưa vào Round 3 scope.

### A.2.3 Round 3 — Inter-RS coordination (NEW DIMENSION) — **PASS 4.1/5**

**1-sentence object (hard-stop PASS):** "How multiple K_R spaces relate, communicate validity, and resolve conflict across distinct registering systems."

**5-Why:**
1. Multi-RS coordination cần không? → Wigner's friend, EPR distributed, multi-observer.
2. Không phải E15 IRB? → E15 = entangled subsystems trong cùng quantum state; không phải RS-RS communication.
3. Không phải T7 scope propagation? → T7 propagates trong shared C_K (cùng IRB); không phải arbitrary RS-RS.
4. Gap thật sao? → Chưa postulate nào define K_R1 ↔ K_R2 sharing/conflict/merge protocol.
5. Root: Inter-RS coordination là **open frontier**; RCA gốc tự liệt kê "Not yet RCA'd" tại Section 2 Dimension 2 gap table.

**5-criteria scoring:** 0.9 / 0.8 / 0.9 / 0.7 / 0.8 = **4.1/5 PASS**.

**Verdict:** Inter-RS coordination là dimension thứ 6. Phase 2 Round 2 (E6 composition) được subsume vào đây.

## A.3 — Updated Verdict Matrix (6 dimensions)

| # | Dimension | Status | Confidence | Source |
|---|---|---|---:|---|
| 1 | Thêm postulate từ BE source mới | Gần đóng | **4.6/5** | Section 2 Dim 1 + A.1.2 |
| 2 | Thêm postulate từ structural gap nội tại | Có điều kiện mở | **4.1/5** | Section 2 Dim 2 + A.1.2 |
| 3 | Thêm nodes/edges trong postulate hiện có | Mở | **4.5/5** | Section 2 Dim 5 + A.1.2 |
| 4 | Import từ VVV-QMRF-EX vào core | Đóng (by design) | **4.9/5** | Section 2 Dim 3 + A.1.2 |
| **5 (NEW)** | **Algebraic-layer theorems (T8/T9)** | **Có điều kiện mở** | **4.1/5** | A.2.1 |
| **6 (NEW)** | **Inter-RS coordination (K_R1↔K_R2 protocol)** | **Open frontier** | **4.1/5** | A.2.3 |

## A.4 — Updated Prioritized Roadmap

### Tier 1 — Pre-existing recommendations (vẫn current)

1. Draft E18 narrow framework proposal — RCA-supported candidate, 2 case PASS.
2. Boundary notes cho E11/E14 (downstream từ E17 RCA-1).

### Tier 2 — Mới phát hiện từ Phase 2

3. **Enumerate T8/T9 algebraic-layer candidates.** Cụ thể:
   - T8 candidate: K8 (cross-space embedding) ∘ T5 (K_joint composition) — interaction theorem.
   - T9 candidate: Multi-time validity propagation across embeddings.
   - Gate: Mỗi candidate cần (a) 1-sentence statement, (b) Level 4 freeze status check, (c) case validation.
4. **Open RCA cho inter-RS coordination dimension.** Object: protocol cho K_R1 và K_R2 sharing/conflict resolution. Use cases: Wigner's friend (paper v2.0), EPR multi-RS.

### Tier 3 — Not recommended (giữ nguyên từ Section 4)

- Không import EX vào core.
- Không tạo postulate từ BE source alone không có structural necessity.
- Không force E17 (R2 path) without isolating channel-self-registration object.

## A.5 — Phase 3 Verify

| Check | Result | Note |
|---|---|---|
| Drift được phát hiện và document | PASS | T5/T6/T7 và E18 confidence ambiguity flagged |
| Re-scoring uses 3 rounds × 5-Why × gate 4.0/5 | PASS | Per user decision rule |
| Round 1 + 3 PASS, Round 2 FAIL — đầy đủ document | PASS | Mỗi round có scoring + verdict |
| "Extend, not overwrite" | PASS | Original Section 0-5 + Summary Table untouched |
| EX compass-only | PASS | EX dùng để verify boundary audit, không import |
| RCA Rule Zero Step 5 (Verify root cause removed) | PASS | Drift cause (cùng-ngày commit + algebraic-layer chưa public) đã được fix bằng appendix này |

## A.6 — Open question (chuyển giao)

**Câu hỏi gốc của user:** "VVV-QMRF Core còn mở rộng được không?"

**Trả lời cập nhật (6-dimension matrix):**
- **3 chiều OPEN/Có điều kiện mở** (V2, V3, V5) với confidence 4.1–4.5.
- **1 chiều Open frontier** (V6) cần RCA mới.
- **1 chiều Gần đóng** (V1) với 1 candidate hé cửa (Hetuvābhāsa error-taxonomy).
- **1 chiều Đóng by design** (V4) confidence 4.9/5.

**Khuyến nghị tiếp theo (theo thứ tự):**
1. E18 narrow draft (đã có RCA, đã có 2 case PASS).
2. Enumerate T8/T9 candidate theorems trong K-Space Layer 2.
3. RCA mới cho inter-RS coordination dimension.
4. Hetuvābhāsa-based error-taxonomy nếu BE source dimension cần reopen.

---

**Appendix end. Original Section 0-5 + Summary Table above remain authoritative for the 4-dimension verdict; Appendix A extends to 6 dimensions per Phase 2 findings.**

---

# Appendix B — E18 Promotion Progress: G6 EX Recoverability Check (2026-05-22)

> **Scope:** VVV-QMRF core (E18 promotion path); VVV-QMRF-EX as compass only.
>
> **Trigger:** Appendix A.4 Tier 1 listed "Draft E18 narrow framework proposal — RCA-supported candidate, 2 case PASS" as the top priority action. This appendix records the downstream progress through G6 and its impact on the extensibility verdict. **Extend, not overwrite:** Sections 0-5, Summary Table, and Appendix A remain authoritative and are not modified.

## B.0 — Context / Bối cảnh

Appendix A (commit `b779117`, 2026-05-22) was written when E18 had two case validations (Wheeler + Scully-Drühl) and the narrow draft had just been recommended. Since then, E18 has advanced through G4 (Kim 1999 third case), G5 (analogical-only BE anchor), and G6 (EX recoverability check + EX registry sync), bringing the gate progress to **6/7 DONE**. Only G7 (user-authorized index insertion) remains pending.

This appendix documents the G6 chain specifically, as it directly interacts with the extensibility verdict: G6 was the gate where VVV-QMRF-EX (used as compass) informed whether the EX-side `N_QM_VVV_00024` node recovers above the 4.0 threshold after the refined E18 structure was established.

## B.1 — E18 Promotion Gate Progress (state at 2026-05-22)

| Gate | Condition | Status | Evidence |
|---|---|---|---|
| G1 | Two case validations PASS | **DONE** | Wheeler + Scully-Drühl (`rca_e18.md` Sections 10-11) |
| G2 | Formal locking rule with explicit `S` | **DONE** | `Lock(C_f, S, {W_i}) -> W_valid` (`rca_e18.md` Section 11.8) |
| G3 | Boundary safety ≥ 4.0/5 | **DONE** | 4.3/5 per `rca_e18.md:756` |
| G4 | Third independent case validation | **DONE** | Kim et al. 1999 — 4-branch lock, 20/20 condition cells PASS (`rca/cases/e18_case_kim_1999.md`) |
| G5 | BE anchor decision | **DONE** | Analogical-only permanent boundary accepted (`rca_e18.md` Section 13) |
| **G6** | **EX recoverability check** | **DONE** | EX registry sync via Path C — `BR_EX_BE_00070`–`BR_EX_BE_00072` active (see B.2 below) |
| G7 | User-authorized index insertion | **PENDING** | Explicit user authorization required before `framework/index.md` is touched |

**Gate progress: 6/7 DONE (86%).** E18 remains in `framework/drafts/` until G7.

## B.2 — G6 Key RCA Chain / Chuỗi RCA G6

G6 asked: does EX `N_QM_VVV_00024` recover above the 4.0 threshold after E18 gained three case validations and a closed G5 boundary?

**Step 1 — G6 HOLD** (`rca_e18_g6_ex_recoverability_check.md`, 2026-05-22):

Root cause isolated: old `BR_EX_BE_00066` anchors delayed-choice erasure to `N_BE_00029` Momentariness only, while the refined E18 object depends on valid-sign locking (`C_f + S → W_valid`). The old bridge object and the refined E18 object are not the same object. Therefore G6 was marked **HOLD — EX vNext re-audit required**, not a direct PASS or FAIL.

**Step 2 — Bridge audit: three paths** (`rca_e18_ex_vnext_bridge_audit.md`, 2026-05-22):

3 RCA rounds × 5-Why × gate 4.0/5:

| Path | Candidate | Score | Decision |
|---|---|---:|---|
| A | Old `BR_EX_BE_00066` reactivated as-is | 3.4/5 | FAIL — temporal anchor too broad for valid-sign structure |
| B | Narrowed temporal-boundary-only revision | 3.8/5 full-node; 4.1/5 component-only | HOLD — useful secondary support, not full-node recovery |
| **C** | **New valid-sign package: `N_BE_00003` + `N_BE_00019` + `N_BE_00021` (primary); `N_BE_00029` (secondary boundary support)** | **4.2/5** | **PASS-CANDIDATE** |

Root cause fixed by Path C: the old bridge failed because it mapped generic momentariness to a more specific valid-sign locking structure; the Anumāna–Vyāpti–Svabhāvapratibandha chain directly addresses the `I(C_f, S, W_j)` inferential validity condition.

**Step 3 — EX registry sync (2026-05-22):**

EX vNext registry sync added three new active bridges under the valid-sign package:

| Bridge ID | BE Anchor | VVV Node | Status |
|---|---|---|---|
| `BR_EX_BE_00070` | `N_BE_00003` Anumāna | `N_QM_VVV_00024` | Active |
| `BR_EX_BE_00071` | `N_BE_00019` Vyāpti | `N_QM_VVV_00024` | Active |
| `BR_EX_BE_00072` | `N_BE_00021` Svabhāvapratibandha | `N_QM_VVV_00024` | Active |

`BR_EX_BE_00066` (old) remains `RECLASSIFIED-v1.7`, inactive, with a supersession note. `N_BE_00029` is retained as secondary temporal-boundary support. Row 24 in `k_gap_exception_list.md` updated to `KE-RESOLVED-STRETCH-vNext-PATH-C` at 4.2/5. EX active registry: 144 entries. Graph: 184 edges.

**Step 4 — G6 DONE:**

With EX registry sync completed and `vvv_qmrf_ex_boundary_audit.md` "E18 Path C EX vNext sync" entry confirming 0 violations, G6 moves to **DONE**. E18 narrow draft Section 8 records G6 DONE, G7 PENDING.

## B.3 — Impact on 6-Dimension Verdict / Tác động lên Verdict Matrix

The 6-dimension verdict from Appendix A.3 is not changed by G6 completion:

| Dimension | A.3 Verdict | After G6 | Confidence | Reason |
|---|---|---|---:|---|
| 1 — BE source exhaustion | Gần đóng | **Unchanged** | 4.6/5 | G6 reuses BE nodes already in core (N_BE_00003/00019/00021); no new BE source opened |
| **2 — Structural gap (nội tại)** | Có điều kiện mở | **Unchanged** | 4.1/5 | G6 DONE advances gate progress to 6/7 but E18 stays in `drafts/` until G7; Dimension 2 remains conditionally open |
| 3 — Nodes/edges trong postulate hiện có | Mở | **Unchanged** | 4.5/5 | G6 is a promotion-path step, not a node/edge addition |
| **4 — Import EX vào core** | Đóng (by design) | **Unchanged** | 4.9/5 | Path C bridges are EX-local; zero core edges added; boundary audit 0 violations |
| 5 — Algebraic-layer theorems | Có điều kiện mở | **Unchanged** | 4.1/5 | Outside G6 scope |
| 6 — Inter-RS coordination | Open frontier | **Unchanged** | 4.1/5 | Outside G6 scope |

**EX coverage delta (Dimension 4 note):** Section 2 (original, 2026-05-21) cited 88.5% K-side direct bridge. EX vNext sync brings this to **47/52 = 90.4%** direct coverage (+ 4 KE-QI + 1 KE-SC-RECLASSIFIED-v1.7 = 52/52 = 100% effective coverage). This is an EX-internal metric improvement, not a change to the core extensibility verdict.

> [!NOTE]
> **Why Dimension 2 remains "Có điều kiện mở" (not upgraded):** G6 DONE closes a promotion gate for E18, but does not add a new structural gap or open a new extension dimension. The verdict label reflects how many extension candidates exist and their readiness level, not whether a given candidate has passed all gates. E18 becomes a frozen postulate only when G7 is satisfied.

## B.4 — Roadmap Impact / Tác động Roadmap

**Appendix A.4 Tier 1** — "Draft E18 narrow framework proposal — RCA-supported candidate, 2 case PASS": **DONE.** E18 narrow draft exists at `framework/drafts/vvv_qmrf_framework_e18_delayed_choice_registration_boundary_narrow_draft.md` with refined `Lock(C_f, S, {W_i}) → W_valid`, 3 case validations, G1-G6 DONE.

**Remaining Dimension 2 action:** G7 — explicit user authorization to insert E18 into `framework/index.md`. Until then, E18 must remain in `framework/drafts/`.

**Appendix A.4 Tier 2 items** (T8/T9 algebraic, inter-RS coordination) and **Tier 3** (not recommended) are unchanged by G6.

## B.5 — Verify / Kiểm chứng

| Check | Result | Evidence |
|---|---|---|
| G6 root cause isolated (not symptom patched) | PASS | Old bridge object vs refined E18 object mismatch identified; Path C fixes the object |
| EX compass-only rule respected | PASS | `BR_EX_BE_00070-00072` are EX-local; zero core edges added; boundary audit 0 violations |
| "Extend, not overwrite" respected | PASS | Sections 0-5, Summary Table, Appendix A untouched |
| 6-Dimension verdict accuracy | PASS | All 6 verdicts unchanged; EX coverage delta documented as EX-internal metric |
| G7 separation preserved | PASS | No index insertion authorized or performed; E18 stays in `framework/drafts/` |
| Neutral wording respected | PASS | No "error/wrong/fallacy" about Standard QM; uses "scope boundary", "registration-layer distinction" language |

---

**Appendix B end. Appendices A and B together cover: (A) 6-dimension extensibility audit + roadmap, and (B) E18 G6 EX recoverability chain and promotion gate progress. Both are extensions of the original Sections 0-5 + Summary Table, which remain authoritative.**
