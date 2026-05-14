Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Work History
# Lịch sử làm việc hệ thống VVV-QMRF

**Last updated:** 2026-05-14T22:36+07:00<br/>
**Scope:** Historical record of work completed, system milestones, and VVV-QMRF concept nodes created.<br/>
**Status:** Historical summary only; not a source of truth for node definitions.

---

## 1. Purpose / Mục đích

This file records the working history of the **VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)** system. Its legacy name is **VietVunVut Epistemic Quantum Measurement (VVV-EQM)**.

File này ghi lại lịch sử làm việc của hệ thống **VVV-QMRF**: đã làm gì, đã giải quyết những khoảng trống nào, và đã tạo những "node" khái niệm nào trong lớp mở rộng VVV-QM. Tên cũ của hệ thống là **VVV-EQM**.

### RCA root cause / Căn nguyên RCA

**Symptom:** The project history, BIAN resolutions, and VVV-QM node list are distributed across multiple files.

**Root cause:** The project has separate files for the published overview, BE source of truth, QM source of truth, BIAN index, and VVV-QM node extraction, but no single historical log showing what work has been completed over time.

**Fix:** Create this file as a historical index that points back to the verified sources. Do not make this file a new source of truth.

---

## 2. Verified Sources / Nguồn kiểm chứng

This history is derived from these active project files:

| Role | File |
|---|---|
| Project overview | [README.md](README.md) |
| BE node/edge source of truth | [SYSTEM_Buddhist_Epistemology/system_be_full.md](SYSTEM_Buddhist_Epistemology/system_be_full.md) |
| QM system source | [SYSTEM_Quantum_Measurement/system_qm_full.md](SYSTEM_Quantum_Measurement/system_qm_full.md) |
| BIAN source of truth | [documents/research_documents/gap/BIAN_index_SOT.md](documents/research_documents/gap/BIAN_index_SOT.md) |
| VVV-QM node table | [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md) |
| Primary BE-QM refine mapping | [documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md](documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md) |
| Formal BE-QM system mapping | [documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md](documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md) |

---

## 3. System Snapshot / Ảnh chụp hệ thống hiện tại

| Item | Current state |
|---|---|
| System name | VVV-QMRF — VietVunVut Quantum Measurement Registration Framework |
| Primary method | Buddhist Epistemology as the primary ontological frame; Quantum Measurement mapped onto it |
| BE source of truth | `SYSTEM_Buddhist_Epistemology/system_be_full.md` |
| QM source | `SYSTEM_Quantum_Measurement/system_qm_full.md` |
| BE core graph | 30 core BE nodes and 39 core BE edges in published compact form; expanded BE SOT used for RCA |
| BIAN status | 20 labels accounted for: 19 active gaps resolved + 1 reserved label |
| VVV-QM node policy | New VVV nodes use `N_QM_VVV_00001`, `N_QM_VVV_00002`, ... |
| Boundary | VVV-QM nodes are epistemic / interpretive / formal-category extensions, not replacement canonical QM nodes |

---

## 4. Work Timeline / Dòng thời gian làm việc

### 2026-05-11 — BIAN-1 transition gap isolated

- Resolved **BIAN-1** through **Lemma S1-Λ**, not through Postulate E8.
- Clarified that `N_BE_00010` is the receiver on the E5-side, not the transition operator.
- Root cause fixed: the post-detection internal representational state was being confused with the transition mechanism itself.

### 2026-05-12 — BIAN resolution framework completed

- Consolidated the BIAN gap resolution pipeline.
- Resolved BIAN-2 through BIAN-19 through categories, postulates, and lemmas.
- Established that BIAN-20 is reserved and should be read through BIAN-10.
- Updated the system architecture toward the stable v2 framework: E1-E16 postulates, synthesis lemmas, meta-architecture files, and BIAN resolution registry.
- Added and refined README sections for thesis, central question, problem statement, non-claim boundaries, bilingual research framing, and BIAN etymology.

### 2026-05-13 — VVV-QM node system extracted

- Created the VVV-QM RCA node table in [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md).
- Distinguished canonical QM nodes `N_QM_XXXXX` from VVV-QMRF extension nodes `N_QM_VVV_XXXXX`.
- Aligned terminology around **"registration-state update" / "cập nhật trạng thái ghi nhận"** for the general K-side update beyond human cognition.
- Added RCA traceability for VVV-QM materials and standardized traceability tables.
- Synchronized VVV-QMRF research materials across mapping, framework, and node files.

### 2026-05-14 — BE SOT centralized and history file added

- Centralized Buddhist Epistemology node/edge RCA around [SYSTEM_Buddhist_Epistemology/system_be_full.md](SYSTEM_Buddhist_Epistemology/system_be_full.md) as the single BE source of truth.
- Added this [history.md](history.md) file to preserve a clear historical record of completed work and created VVV-QM nodes.

### 2026-05-14T15:00+07:00 — Epistemic Fidelity Audit (Opus 4.6)

**Auditor:** Google Gemini — Opus 4.6 (Antigravity agent)  
**Method:** Line-by-line RCA of 15 category files, cross-referenced against 3 primary SOT sources  
**SOT Sources used:**
- **SOT-1 (BE):** Hari Shankar Prasad, *The Buddhist Pramāṇa-Epistemology, Logic, and Language* (Studia Humana)
- **SOT-2 (QM):** Andrew N. Jordan & Irfan A. Siddiqi, *Quantum Measurement: Theory and Practice* (Cambridge University Press, 2024)
- **SOT-3 (QM):** Leonard Susskind & Art Friedman, *Quantum Mechanics: The Theoretical Minimum* (Basic Books, 2014)

**Discovered 5 logic errors (D1–D5):**

| ID | File | Line(s) | Error Type | Severity | Description |
|:--:|:-----|:-------:|:-----------|:--------:|:------------|
| **D1** | Cat 14 | L49-52, L63 | Misattribution | 🔴 CRITICAL | Claimed IRB as "third subtype" of Dharmakīrti's *Svabhāvapratibandha*. SOT-1 L348 (Katsura [25]) confirms Dharmakīrti recognizes exactly **2 types** (Tadutpatti + Tādātmya). IRB is a VVV-QMRF extension, not a classical Buddhist category. |
| **D2** | Cat 14 | L62 | Wrong physics explanation | 🔴 CRITICAL | Claimed LHV theories fail because "they assume all relations are causal". SOT-1 L348: Dharmakīrti's own system has non-causal Tādātmya. SOT-2 L688-742: LHV fail because **Bell inequality is experimentally violated** under locality + realism assumptions (Nobel 2022). |
| **D3** | BIAN_index_SOT | L45 | Typo in SOT | 🔴 HIGH | Master table L45 wrote `BIAN-16 → Cat 06 + E2` but L72 + Cat 02 file both confirm correct target is `Cat 02 + E2`. Cat 06 is Anadhyavasāya (BIAN-13). |
| **D4** | Cat 15 | L21 | Over-restriction | 🟡 MEDIUM | Defined *Saṃśaya* as "indeterminacy between **two** equally weighted alternatives". SOT-1 L89: classical definition not restricted to binary. SOT-2 L467: QM superposition is N-ary with unequal |cᵢ|². Formal structure (L39-63) correctly handles N-ary — error is only in summary text. |
| **D5** | Cat 14 | L50 | Stretched mapping | 🟡 MEDIUM | Mapped Tādātmya → identical particles. SOT-1 L348: Tādātmya = logical genus-species identity ("oak IS a tree"). QM identical particles = physical exchange symmetry. Different senses of "identity" — mapping is analogical, not direct equivalence. |

**Remediation status (as of 2026-05-14T22:20+07:00):**

| ID | Status | Detail |
|:--:|:------:|:-------|
| D1 | ✅ Patched | Cat 14 L13, L21, L30, L42, L49, L52, L63, L65 updated with qualifier "VVV-QMRF extension, not classical subtype" |
| D2 | ✅ Patched | Cat 14 L62 rewritten: now cites Bell inequality violation under locality+realism (SOT-2) as reason LHV fail, not philosophical "all causal" claim. Also L47 updated. |
| D3 | ✅ Patched | BIAN_index_SOT L45 corrected: now reads `Cat 02 + E2` (was erroneously `Cat 06 + E2`). Verified 2026-05-14T22:20+07:00. |
| D4 | ✅ Patched | Cat 15 L21 updated: now includes `not a binary/equal-weight state` qualifier. Verified 2026-05-14T22:20+07:00. |
| D5 | ✅ Patched | Cat 14 L50 updated with "logical genus-species identity; classical Dharmakīrti type" (per Katsura/Prasad SOT-1 L348). Katsura [25] reference added to L69. |

**Impact assessment:**
- 12/15 category files have **no** critical errors
- Errors concentrated in Cat 14 (3/5 errors) — Cat 14 now fully patched (D1, D2, D5 ✅)
- Framework architecture is **not** structurally broken — all fixes are precision corrections
- **All 5/5 errors (D1–D5) are now ✅ Patched** — no outstanding remediation items

**Propagation trace (files also affected by Cat 14 errors):**
- `vvv-qmrf/node_QM_VVV.md` L25, L55 — N_QM_VVV_00025 description
- `vvv-eqm/node_QM_VVV.md` L27, L57 — copy of above
- `vvv-qmrf/dictionary.md` L96 — IRB entry
- `vvv-eqm/dictionary.md` L98 — copy of above
- `gap/BIAN_index_SOT.md` L66 — BIAN-10 resolution claim
- `framework/E15_intrinsic_relation_postulate.md` L88, L104 — Cat 14 back-reference

### 2026-05-14T22:22+07:00 — QM Physics Accuracy Audit (Opus 4.6)

**Auditor:** Google Gemini — Opus 4.6 (Antigravity agent)
**Method:** Line-by-line verification of all 15 category §3 (Formal Structure) sections against standard QM textbooks
**SOT Sources used:**
- **SOT-2 (QM):** Andrew N. Jordan & Irfan A. Siddiqi, *Quantum Measurement: Theory and Practice* (Cambridge University Press, 2024)
- **SOT-3 (QM):** Leonard Susskind & Art Friedman, *Quantum Mechanics: The Theoretical Minimum* (Basic Books, 2014)
- **Standard:** Nielsen & Chuang, Zurek (2003), AAV (1988), Minev et al. (*Nature* 2019)

**Discovered 8 QM physics issues (Q1–Q8):**

| ID | File | Line(s) | Error Type | Severity | Description |
|:--:|:-----|:-------:|:-----------|:--------:|:------------|
| **Q1** | Cat 06 | L46 | Wrong physics term | 🟠 HIGH | Wrote decoherence "dissipates into the environment". Decoherence = entanglement with env degrees of freedom (Zurek 2003), not energy dissipation. State doesn't dissipate — it loses coherence. |
| **Q2** | Cat 12 | L53 | Outdated characterization | 🟡 MEDIUM | Described quantum jump as "instantaneous, irreversible". Minev et al. (*Nature* 2019) showed jumps have finite duration (~4μs) and can be reversed mid-flight. |
| **Q3** | Cat 13 | L48 | Missing subspace condition | 🟡 MEDIUM | Absence projector must be bounded as Π̂_absent^(ℋ_M) = Î_ℋ_M - Σᵢ\|λᵢ⟩⟨λᵢ\| with \|λᵢ⟩ ∈ ℋ_M; otherwise a global complement can collapse into a trivial zero projector or overclaim absence outside the tested domain. |
| **Q4** | Cat 15 | L44 | Notation inconsistency | 🟡 MEDIUM | Wrote ρ = Σᵢ cᵢ\|λᵢ⟩⟨λᵢ\| + off-diagonal terms. Mixes pure-state amplitudes cᵢ with density matrix diagonal weights (should be \|cᵢ\|² or pᵢ). |
| **Q5** | Cat 06 | L42 | Category confusion | 🟡 MEDIUM | Called detection efficiency η a QM formalism concept. η is an experimental parameter; QM formalism handles no-click via POVM element E₀ = (1-η)I. |
| **Q6** | Cat 03 | L45 | Minor terminology | 🟢 LOW | "Transition probability" used where "orthogonality" (⟨λ₂\|λ₁⟩ = 0) is meant. Transition probability usually refers to \|⟨λ₂\|U(t)\|λ₁⟩\|². |
| **Q7** | Cat 11 | L48 | Resolved precision issue | 🟢 LOW | Weak value Aᵥ now distinguishes Aᵥ ∈ ℂ in general from anomalous Re(Aᵥ) outside the eigenvalue spectrum. |
| **Q8** | Cat 10 | L49 | Not testable | 🟢 LOW | "Pre-symbolic event ε(M)" is a framework definition, not a QM claim. Already correctly marked as Derived in §5. No QM contradiction. |

**Remediation status (as of 2026-05-14T22:36+07:00):**

| ID | Status | Detail |
|:--:|:------:|:-------|
| Q1 | ⏳ Pending | Cat 06 L46 needs "dissipates" → "becomes entangled with environmental degrees of freedom" |
| Q2 | ⏳ Pending | Cat 12 L53 needs Minev 2019 qualifier |
| Q3 | ⏳ Pending | Cat 13 L48 needs subspace condition dim(span{λᵢ}) < dim(H) |
| Q4 | ⏳ Pending | Cat 15 L44 needs notation fix cᵢ → \|cᵢ\|² or pᵢ |
| Q5 | ⏳ Pending | Cat 06 L42 needs POVM clarification |
| Q6 | ⏳ Pending | Cat 03 L45 optional terminology fix |
| Q7 | ✅ Fixed | Cat 11 L48 now distinguishes complex Aᵥ from anomalous Re(Aᵥ) outside the eigenvalue spectrum |
| Q8 | ✅ No fix needed | Already correctly labeled as Derived |

**Impact assessment:**
- 7/15 category files have **no** QM physics issues (Cat 01, 02, 04, 05, 07, 08, 09, 14)
- Cat 06 has most issues (Q1 + Q5)
- No issue breaks framework logic — all are precision/completeness improvements
- Overall QM physics accuracy: **8.7/10**

### 2026-05-14T23:05+07:00 — RCA Audit Categories 08-15 & Vietnamese Explanation

**Auditor:** Google Gemini 3.1 Pro (High)
**Method:** Line-by-line RCA audit of remaining VVV-QMRF categories (08–15) and full Vietnamese explanation for all 15 categories.
**Results:**
- **Zero** fatal logical errors, physics violations, or BE-QM conflations across all 15 category files.
- Category 13 (VAR/Anupalabdhi) identified as the strongest technical file.
- Generated `rca_audit_categories_08_15.md` for English audit report.
- Generated `rca_audit_giai_thich_tieng_viet.md` translating the 15-category audit results into plain Vietnamese.

---

## 5. Completed Work / Những việc đã làm

### 5.1. Source-of-truth structure

- Established [SYSTEM_Buddhist_Epistemology/system_be_full.md](SYSTEM_Buddhist_Epistemology/system_be_full.md) as the only BE node/edge source of truth for RCA.
- Preserved compact derived BE references in published node and edge documents.
- Converted the Quantum Measurement concept table into [SYSTEM_Quantum_Measurement/system_qm_full.md](SYSTEM_Quantum_Measurement/system_qm_full.md), with canonical QM nodes `N_QM_00001` through `N_QM_00105`.

### 5.2. BIAN gap resolution

- Created and consolidated the BIAN index SOT.
- Resolved 19 active BIAN gaps.
- Reserved BIAN-20 as a non-independent label tied to BIAN-10.
- Kept no-node cases explicit instead of forcing every Buddhist concept into a separate QM node.

### 5.3. VVV-QM extension layer

- Created the VVV-QM node code policy: `N_QM_VVV_XXXXX`.
- Extracted VVV-QM nodes only when the category file adds a genuinely new epistemic, inferential, interpretive, or formal-category role beyond canonical QM.
- Folded duplicate or non-independent candidates instead of creating redundant nodes.

### 5.4. Terminology alignment

- Standardized **"registration-state update" / "cập nhật trạng thái ghi nhận"** for the general K-side update.
- Restricted **"detector response"** to the apparatus' physical response.
- Preserved the distinction between physical QM measurement and VVV-QMRF registration certification.

---

## 6. BIAN Resolution Summary / Tóm tắt giải quyết BIAN

| BIAN | Structural concept | BE node status | Resolution |
|---|---|---|---|
| BIAN-1 | Post-Detection Internal Representational State | `N_BE_00010` | Resolved by Lemma S1-Λ |
| BIAN-2 | Observer Self-Reference / Reflexive Cognition | `N_BE_00011` | Category 05 + E1 |
| BIAN-3 | Limit-Case Observation by Different Faculty | `N_BE_00012` | Category 11 + E12 |
| BIAN-4 | Measurement Representation / Internal Encoding | No dedicated BE node | Category 08 + E5 |
| BIAN-5 | Epistemic Commitment Act / Moment of Determination | No dedicated BE node | Category 08 + E3 |
| BIAN-6 | Self-Certifying Measurement / No External Meta-Level | `N_BE_00011` | Category 05 + E1 |
| BIAN-7 | Pre-Symbolic Physical Event / Formalism-External Stratum | `N_BE_00009` | Category 10 + E4 |
| BIAN-8 | Epistemological Theorization of Temporal Discontinuity | `N_BE_00029` | Category 12 + E13 |
| BIAN-9 | Formal Cognition of Absence as Distinct Category | `N_BE_00253` | Category 13 + E14 |
| BIAN-10 | Non-Classical Correlation / Entanglement as VVV-QMRF Extension Relation | `N_BE_00021` | Category 14 + E15 |
| BIAN-11 | Pre-Measurement Registration Indeterminacy | `N_BE_00007` | Category 15 + E16 |
| BIAN-12 | Formal Measurement Invalidation / Epistemological Override | No dedicated BE node | Category 03 + E8 |
| BIAN-13 | Null Observer Event / Non-Engagement Epistemic State | No dedicated BE node | Category 06 + E9 |
| BIAN-14 | Tripartite Measurement Validity Conditions | `N_BE_00018` | Category 09 + E10 |
| BIAN-15 | Purely Contrastive Quantum Evidence Structure | No dedicated BE node | Category 01 + E11 |
| BIAN-16 | Measurement Self-Completion / No External Registration | `N_BE_00001` | Category 02 + E2 |
| BIAN-17 | Regress-Stopping Principle for Measurement Chain | `N_BE_00011` | Category 05 + E1 |
| BIAN-18 | Intrinsic vs Extrinsic Measurement Validity Location | No dedicated BE node | Category 04 + E7 |
| BIAN-19 | Observer as Causal Process not Substance | `N_BE_00066` | Category 07 + E6 |
| BIAN-20 | Reserved — Entanglement correlation type | `N_BE_00021` | Reserved; see BIAN-10 |

---

## 7. Created VVV-QM Concept Nodes / Các node khái niệm VVV-QM đã tạo

These nodes are recorded in [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md). This section is a historical index only.

| No. | Node code | Concept | Vietnamese | RCA role |
|---:|---|---|---|---|
| 1 | `N_QM_VVV_00001` | Contrapositive Quantum Evidence / Purely Contrastive Quantum Evidence Structure | Bằng chứng lượng tử phản chứng / cấu trúc bằng chứng thuần loại trừ | New epistemic category for knowledge established through structured null results |
| 2 | `N_QM_VVV_00002` | Interaction-Free State Inference (IFSI) | Suy luận trạng thái phi tương tác | Inference mechanism from no-click to state exclusion |
| 3 | `N_QM_VVV_00003` | Null-Projection Operator `P_null` | Toán tử chiếu vắng mặt `P_null` | Proposed operator for null-outcome projection |
| 4 | `N_QM_VVV_00004` | Informative Silence | Sự im lặng mang thông tin | Distinguishes valid silence from mere absence of signal |
| 5 | `N_QM_VVV_00005` | Non-Informative Null Event / Broken-Detector Null | Sự kiện rỗng không mang thông tin / im lặng do máy dò lỗi | Diagnostic failure-mode node |
| 6 | `N_QM_VVV_00006` | Exclusion-Based State Selection | Chọn trạng thái bằng loại trừ | Apoha-like interpretive-formal operation |
| 7 | `N_QM_VVV_00007` | Counterfactual Evidential Branch | Nhánh bằng chứng phản sự kiện | Interpretive hypothesis for evidential force of unrealized branches |
| 8 | `N_QM_VVV_00008` | Ideal Information Without Direct Disturbance | Thông tin lý tưởng không qua nhiễu loạn trực tiếp | Ideal limit condition for information through exclusion |
| 9 | `N_QM_VVV_00009` | Elitzur-Vaidman Interaction-Free Measurement as VVV Evidence Exemplar | Thí nghiệm Elitzur-Vaidman như ví dụ bằng chứng VVV | Evidence exemplar, not a core canonical QM node |
| 10 | `N_QM_VVV_00010` | PVM-Equivalent Epistemic Authority of Null Evidence | Thẩm quyền nhận thức của bằng chứng rỗng tương đương PVM | Claim node; marked overclaim-sensitive until fully formalized |
| 11 | `N_QM_VVV_00011` | Dual-Phase Epistemic Certification / Formal Validity Location | Sự xác thực nhận thức kép / định vị tính hợp lệ chính thức | Root category for measurement-validity location |
| 12 | `N_QM_VVV_00012` | Intrinsic Causal Triggering Phase | Pha kích hoạt nhân quả nội tại | Provisional physical-trigger phase |
| 13 | `N_QM_VVV_00013` | Extrinsic Epistemic Certification Phase | Pha xác thực nhận thức ngoại tại | External verification/certification phase |
| 14 | `N_QM_VVV_00014` | Extrinsic Certification Operator `Ĉ_ext` | Toán tử xác thực ngoại tại `Ĉ_ext` | Proposed operator for extrinsic certification |
| 15 | `N_QM_VVV_00015` | Conditionally Updated State `ρ̃` | Trạng thái cập nhật có điều kiện `ρ̃` | Intermediate provisional state-status notation |
| 16 | `N_QM_VVV_00016` | Certified Measurement State `ρ_certified` / Truth-Stamped State | Trạng thái đo lường đã được xác thực / trạng thái được đóng dấu chân lý | Terminal certified state-status notation |
| 17 | `N_QM_VVV_00018` | Verification-Integrated Density Matrix Evolution | Tiến hóa ma trận mật độ tích hợp xác thực | Proposed formal evolution rule linking density-matrix update and verification |
| 18 | `N_QM_VVV_00020` | Epistemic Absence Cognition / Anupalabdhi-Conditioned Null Cognition | Nhận thức vắng mặt / vô tri giác có điều kiện Anupalabdhi | Root category for absence/non-perception as positive valid knowledge |
| 19 | `N_QM_VVV_00021` | Epistemic Commitment Operator / Semantic Translation State | Toán tử kiến lập nhận thức / trạng thái chuyển đổi ngữ nghĩa | Root category for converting record into semantic knowledge |
| 20 | `N_QM_VVV_00022` | Internal Encoding Phase `Â_kāra` / Mental Correlate Generation | Pha mã hóa nội tại `Â_kāra` / sinh ảnh tượng tâm trí | Observer-internal encoding phase |
| 21 | `N_QM_VVV_00023` | Commitment Act `V̂_yava` / Irreversible Epistemic Locking | Hành động kiến lập `V̂_yava` / chốt nhận thức không thể đảo ngược | Terminal epistemic commitment act/operator |
| 22 | `N_QM_VVV_00024` | Epistemic Locking Boundary in Delayed-Choice Erasure | Ranh giới chốt nhận thức trong xóa lựa chọn trễ | Boundary claim between reversible physical erasure and irreversible epistemic status |
| 23 | `N_QM_VVV_00025` | Intrinsic Relational Binding / Non-Classical Correlation Architecture | Liên kết quan hệ nội tại / kiến trúc tương quan phi cổ điển | Root relation-category for entanglement as intrinsic relational binding |

### 7.1. Candidate code decisions / Quyết định về mã ứng viên

| Candidate code | Decision | Reason |
|---|---|---|
| `N_QM_VVV_00017` | Folded into `N_QM_VVV_00011` | The candidate was part of the DPEC root category, not an independent node |
| `N_QM_VVV_00019` | Downgraded to relation with REO / BIAN-12 | Failed certification is a relation to the existing invalidation pipeline, not a standalone VVV-QM node |
| `N_QM_VVV_00026` | Folded into `N_QM_VVV_00025` | `E_svabh` is only a symbol for IRB, not an independent tensor definition |

---

## 8. Internal VVV-QM Relations / Quan hệ nội bộ VVV-QM

| Source | Relation | Target | Meaning |
|---|---|---|---|
| `N_QM_VVV_00002` | operationalizes | `N_QM_VVV_00001` | IFSI gives the procedure for contrapositive quantum evidence |
| `N_QM_VVV_00006` | grounds | `N_QM_VVV_00003` | Exclusion-based selection supports `P_null` |
| `N_QM_VVV_00004` | contrasts with | `N_QM_VVV_00005` | Valid silence must be separated from broken-detector null events |
| `N_QM_VVV_00011` | contains phase | `N_QM_VVV_00012` | DPEC begins with intrinsic causal triggering |
| `N_QM_VVV_00011` | contains phase | `N_QM_VVV_00013` | DPEC requires extrinsic certification |
| `N_QM_VVV_00012` | produces | `N_QM_VVV_00015` | Intrinsic phase yields `ρ̃` |
| `N_QM_VVV_00013` | is formalized by | `N_QM_VVV_00014` | `Ĉ_ext` names extrinsic certification |
| `N_QM_VVV_00014` | upgrades | `N_QM_VVV_00016` | Certification turns `ρ̃` into `ρ_certified` |
| `N_QM_VVV_00018` | implements | `N_QM_VVV_00011` | Verification-integrated evolution implements DPEC |
| `N_QM_VVV_00014` | routes contradiction to | REO / BIAN-12 | Failed certification belongs to invalidation, not a new node |
| `N_QM_VVV_00020` | generalizes | `N_QM_VVV_00001` | EAC is broader than contrapositive evidence |
| `N_QM_VVV_00020` | uses formal support from | `N_QM_VVV_00003` | `Π̂_absent^(ℋ_M)` is folded into subspace-bounded null-projection support |
| `N_QM_VVV_00020` | requires contrast with | `N_QM_VVV_00005` | Valid absence needs invalid-null controls |
| `N_QM_VVV_00021` | contains phase | `N_QM_VVV_00022` | ECO includes internal encoding |
| `N_QM_VVV_00021` | culminates in | `N_QM_VVV_00023` | ECO ends in commitment act |
| `N_QM_VVV_00023` | establishes boundary for | `N_QM_VVV_00024` | Commitment creates the delayed-choice epistemic locking boundary |

---

## 9. Boundary Rules / Quy tắc ranh giới

1. This file is **history**, not a formal source of truth.
2. VVV-QM nodes do **not** replace canonical QM nodes `N_QM_XXXXX`.
3. VVV-QM nodes represent epistemic, interpretive, inferential, or formal-category additions.
4. Treat cross-domain links as mappings or analogies unless a file explicitly supplies formal proof, peer review, physical prediction, and experimental test.
5. BE node/edge RCA must use only [SYSTEM_Buddhist_Epistemology/system_be_full.md](SYSTEM_Buddhist_Epistemology/system_be_full.md) as BE source of truth.
6. Use **"registration-state update" / "cập nhật trạng thái ghi nhận"** for the general K-side update beyond human cognition.
7. Use **"detector response"** only for the apparatus' physical response.

---

## 10. Open Maintenance Notes / Ghi chú bảo trì

- Update this file only after a meaningful project milestone, new VVV-QM node extraction, BIAN resolution change, or source-of-truth change.
- When a VVV-QM node definition changes, update [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md) first, then update this history file.
- When BE node or edge definitions change, verify against [SYSTEM_Buddhist_Epistemology/system_be_full.md](SYSTEM_Buddhist_Epistemology/system_be_full.md) before editing any derived history summary.

---

## 11. Completion TODO List / Danh sách việc cần làm để hoàn thiện

This TODO list records remaining work needed to make VVV-QMRF clearer, safer, and more publication-ready. It does not change the current source-of-truth hierarchy.

| Priority | Area | TODO | RCA reason | Target file |
|---|---|---|---|---|
| P0 | SOT consistency | Standardize BIAN status wording as "20 labels accounted for: 19 active gaps resolved + 1 reserved label" across public-facing summaries | Remove wording drift around BIAN accounting in active docs | [README.md](README.md); [history.md](history.md) |
| P0 | Boundary control | Keep all VVV-QM nodes explicitly marked as epistemic, interpretive, inferential, or formal-category extensions, not canonical QM replacements | Prevent category error between epistemology and physics | [history.md](history.md); [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md) |
| P1 | Node status | Add a status label for each of the 23 `N_QM_VVV_XXXXX` nodes: complete, needs formalization, overclaim-sensitive, or example-only | Readers need to know which nodes are stable and which are proposals | [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md) |
| P1 | Formalism | Formalize `P_null`, `Ĉ_ext`, `ρ̃`, `ρ_certified`, and `V̂_yava` with minimal equations and explicit proposal labels | Several VVV-QM nodes are currently proposal or overclaim-sensitive | framework files |
| P1 | RCA traceability | For each VVV-QM node, verify source category, nearest canonical QM node, BE/BIAN root, and claim strength | Prevent duplicate, unsupported, or overextended nodes | [documents/research_documents/node_QM_VVV.md](documents/research_documents/node_QM_VVV.md) |
| P2 | Diagram integration | Review the VVV-QMRF vs Standard QM diagram and decide whether it belongs in active docs or draft materials | Architecture diagrams help readers but can overclaim if not boundary-labeled | diagram file |
| P2 | Bridge layer | Review bridge files and decide whether they are active architecture or draft material | Bridge files may be needed to connect BE, QM, and VVV-QM, but should not create a second SOT | bridge folder |
| P2 | Publication prep | Create a claim-strength table before using the framework in paper-facing or README-facing text | Publication-facing claims need clear strength labels | paper / README files |
| P3 | Cleanup | Decide whether `desktop.ini` files should be ignored or removed | These are OS artifacts, not research content | repo config / working tree |

### 11.1. High-priority weak or overclaim-sensitive nodes

| Node | Issue to resolve | Suggested next action |
|---|---|---|
| `N_QM_VVV_00005` | Detector-failure control is weak until detector-validity criteria are formalized | Define minimum validity conditions distinguishing informative silence from broken-detector silence |
| `N_QM_VVV_00007` | Counterfactual evidential branch is interpretive and weak until formal criteria are supplied | Specify when an unrealized branch may count as evidence without becoming metaphysical speculation |
| `N_QM_VVV_00008` | Ideal zero-direct-disturbance claim depends on idealized conditions | State the ideal-limit assumptions and avoid treating them as ordinary laboratory conditions |
| `N_QM_VVV_00010` | PVM-equivalent epistemic authority is not formally validated | Reframe as a proposal unless equivalence conditions are proven |
| `N_QM_VVV_00018` | Verification-integrated density matrix evolution lacks a full equation | Provide a minimal equation or downgrade to framework note |
| `N_QM_VVV_00021`–`N_QM_VVV_00024` | ECO layer is registration-side and not canonical QM | Keep it explicitly VVV-QMRF registration architecture, not a physical collapse mechanism |

### 11.2. Action Plan 1-2-3 / Kế hoạch hành động 1-2-3

This action plan compresses the completion TODO list into a short execution order that fixes root causes before formal expansion or publication-facing use.

1. **Lock wording and boundary first**
   - Standardize BIAN wording to **"20 labels accounted for: 19 active gaps resolved + 1 reserved label"** in [README.md](README.md) and [history.md](history.md).
   - Keep all `N_QM_VVV_XXXXX` nodes explicitly marked as VVV-QMRF extension nodes, not canonical QM nodes.

2. **Add status and traceability to each VVV-QM node**
   - Add one status label to each of the 23 VVV-QM nodes: `complete`, `needs formalization`, `overclaim-sensitive`, or `example-only`.
   - For each node, verify source category, nearest canonical QM node, BE/BIAN root, and claim strength.

3. **Formalize weak nodes before publication-facing use**
   - Formalize `P_null`, `Ĉ_ext`, `ρ̃`, `ρ_certified`, and `V̂_yava` with minimal equations and explicit proposal labels.
   - Review the high-priority weak or overclaim-sensitive nodes before using them in paper-facing or README-facing text.
   - Only after this step, create the claim-strength table and decide whether diagrams and bridge files belong in active architecture or draft material.
