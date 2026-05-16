Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Research Terminology and Symbol Registry / Bảng Thuật ngữ và Ký hiệu Nghiên cứu VVV-QMRF

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)  
**Document ID:** VVV-QMRF-REGISTRY-TERMINOLOGY-001  
**Document type:** index  
**Date:** 2026-05-16  
**Status:** derived research registry  
**Purpose:** Provide the technical registry for VVV-QMRF terminology, symbols, claim classes, source traces, and boundary rules.  
**Scope:** Registration-layer terminology and notation used in active VVV-QMRF research documents.  
**Out of scope:** This registry does not define new Standard Quantum Mechanics laws, does not replace canonical QM notation, and does not upgrade VVV-QMRF proposals into peer-reviewed physics.  
**Schema contract:** `documents/research_documents/vvv-qmrf/schema_guide.md`

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.
>
> VVV-QMRF là nghiên cứu cá nhân độc lập ở Class D, không phải "Standard Quantum Mechanics", chưa "peer-reviewed" hoặc kiểm chứng thực nghiệm, và không dùng cho ứng dụng kỹ thuật ngoài thực tế. Giao thức giới hạn đầy đủ: `DISCLAIMER.md`.

---

## 1. Source Corpus / Tập nguồn

| Source | Role | Required trace |
|---|---|---|
| `documents/research_documents/vvv-qmrf/schema_guide.md` | Schema contract | Document type, symbol registry rule, formula boundary rule, index-document requirements. |
| `documents/research_documents/meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` | Primary VVV-QMRF symbol registry source | Symbol class, layer, owner, status, and boundary for the research-level registry. |
| `documents/research_documents/vvv-qmrf/VVV_QMRF_vs_Standard_QM_system_diagram.md` | Layer-boundary support | Separation between physical state `ρ` and registration state `K`; `U_K` does not modify Born-rule probability. |
| `documents/research_documents/framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | E1 source | `σ(M)`, `R̂_svasa`, `M′`, and K-side self-certification boundary. |
| `documents/research_documents/synthesis/vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | S1-Λ source | `Λ`, `ε(M)`, and symbolization-interface status as lemma/interface. |
| `documents/research_documents/category/vvv_qmrf_category_13_e14_validated_absence_registration.md` | E14 / VAR source | `Π̂_absent^(ℋ_M)`, null result boundary, and validity-gated absence registration. |
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | BE SOT when BE node or edge definitions are used | Use only for BE node/edge meanings; BE source terms remain structural lineage, not QM operators. |

---

## 2. RCA Summary / Tóm tắt RCA

### 2.1 Define

**Symptom:** The old file presented VVV-QMRF symbols as a high-school lesson, while the file name and location now require a research-facing technical registry.

**Triệu chứng:** File cũ trình bày ký hiệu như bài học phổ thông, nhưng tên và vị trí mới yêu cầu nó là bảng kỹ thuật nghiên cứu.

### 2.2 Trace — 5 Whys

1. **Why can the registry drift?** Because educational prose can simplify notation without preserving claim class and source trace.  
   **Vì sao bảng có thể lệch?** Vì văn phong giáo dục có thể làm dễ ký hiệu nhưng không giữ đầy đủ loại claim và nguồn.
2. **Why is that risky?** Because VVV-QMRF notation can look like canonical QM notation if the layer is not stated.  
   **Vì sao rủi ro?** Vì ký hiệu VVV-QMRF có thể trông giống ký hiệu QM chuẩn nếu không ghi tầng.
3. **Why does the layer matter?** Because `ρ` belongs to the physical QM side, while `K` belongs to the registration layer.  
   **Vì sao tầng quan trọng?** Vì `ρ` thuộc tầng vật lý QM, còn `K` thuộc tầng ghi nhận.
4. **Why must formula status be declared?** Because symbolic notation can look stronger than the evidence supporting it.  
   **Vì sao phải khai báo trạng thái công thức?** Vì ký hiệu toán học có thể làm claim trông mạnh hơn bằng chứng.
5. **Why is the registry needed?** Because every formula-using document needs a single place to check symbol meaning, claim class, domain, and boundary.  
   **Vì sao cần registry?** Vì mọi tài liệu dùng công thức cần một nơi kiểm tra nghĩa ký hiệu, loại claim, domain, và ranh giới.

### 2.3 Isolate

**Root cause:** The document was classified as `highschool_lesson`, but the actual research need is an `index`-style symbol registry that enforces source trace, claim class, formula boundary, and update rules before symbols are reused.

**Nguyên nhân gốc:** Doc bị đặt ở lớp `highschool_lesson`, trong khi nhu cầu thật là registry dạng `index`, bắt buộc có nguồn, loại claim, ranh giới công thức, và rule cập nhật trước khi dùng lại ký hiệu.

### 2.4 Fix

This file is now normalized as the research-facing VVV-QMRF terminology and symbol registry. Educational documents may simplify the language, but they must not override the status, source trace, layer, or boundary in this registry.

### 2.5 Verify

The root cause is removed only if every retained symbol answers these fields: meaning, domain, claim class, source trace, and boundary.

---

## 3. Registry Admission Rule / Quy tắc đưa ký hiệu vào bảng

Each symbol must score at least **3.5/5** before it is kept in the canonical registry.

| Criterion | Pass condition |
|---|---|
| Meaning EN | The English technical meaning is explicit. |
| Nghĩa VN | The Vietnamese explanation is clear enough for reuse. |
| Domain | The symbol is assigned to `standard QM`, `registration-layer`, `bridge`, `BE-source lineage`, or `proposal`. |
| Claim class | The symbol has a status such as Class A, B, C, D, M, or BE-source. |
| Boundary | The registry states what the symbol must not imply. |

Symbols below 3.5/5 must be moved to a provisional list, sourced more strongly, or removed from formula use.

---

## 4. Claim Class System / Hệ phân loại claim

| Class | Meaning | Usage rule |
|---|---|---|
| Class A | Canonical Standard QM notation | Use as standard QM notation; do not rename as VVV-QMRF notation. |
| Class B | Standard mathematical or conventional label | Safe when context defines it. |
| Class C | Conjectural VVV-QMRF formal definition | Formal inside VVV-QMRF only; not canonical QM. |
| Class D | Proposed VVV-QMRF operator, map, category, or notation | Registration-layer proposal; not source-system physics by itself. |
| Class M | External model, experiment, or exemplar | Evidence/example only; not a VVV-QMRF axiom. |
| BE-source | Buddhist Epistemology source term | Structural lineage or analogy; not a physical operator. |

---

## 5. Claim Traceability / Truy vết claim

| Claim ID | Claim | Type | Source | Boundary |
|---|---|---|---|---|
| C-001 | VVV-QMRF is a registration-layer research framework. | derived | `schema_guide.md`; `registration_layer_formalization.md` | Not Standard Quantum Mechanics and not an empirically validated physical theory. |
| C-002 | `ρ`, `ψ`, `ℋ`, `E_o`, and `p_QM(o)=Tr(E_oρ)` remain physical-side QM notation. | source / external standard | `VVV_QMRF_vs_Standard_QM_system_diagram.md`; standard QM convention | Not replaced by `K`, `𝒦`, or `U_K`. |
| C-003 | `K`, `K_before`, `K_after`, `𝒦`, and `U_K` are VVV-QMRF registration-layer notation. | formal_notation | `registration_layer_formalization.md` | Not physical quantum states or Schrödinger evolution. |
| C-004 | `σ(M)` and `R̂_svasa` are K-side self-certification formalisms. | formal_notation | `vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Not consciousness-collapse claims and not Hamiltonian modification. |
| C-005 | `Λ` is a symbolization interface between pre-symbolic and symbolic registration stages. | formal_notation | `vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | Lemma/interface status; not a separate postulate unless future RCA upgrades it. |
| C-006 | `Π̂_absent^(ℋ_M)` is bounded absence-projection notation for validated absence registration. | formal_notation | `vvv_qmrf_category_13_e14_validated_absence_registration.md` | Valid only inside measurement-accessible subspace `ℋ_M`; not proof of absence outside the tested domain. |

---

## 6. Canonical Symbol Registry / Bảng ký hiệu chuẩn

### 6.1 Standard QM reference symbols / Ký hiệu tham chiếu QM chuẩn

| Symbol | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `ρ` | Physical quantum state description, often a density operator. | Mô tả trạng thái lượng tử vật lý. | standard QM | Class A | `registration_layer_formalization.md`; `VVV_QMRF_vs_Standard_QM_system_diagram.md` | Not a K-side registration state. |
| `ψ` | Wave function or state vector notation where context allows. | Ký hiệu hàm sóng hoặc vector trạng thái khi ngữ cảnh cho phép. | standard QM | Class A | Standard QM convention; registry support docs | Not VVV-QMRF registration state. |
| `ℋ` | Hilbert space for physical quantum states. | Không gian Hilbert của trạng thái vật lý. | standard QM | Class A | `registration_layer_formalization.md` | Not the registration-state space `𝒦`. |
| `Ĥ` | Hamiltonian operator for physical dynamics. | Toán tử Hamiltonian cho động lực học vật lý. | standard QM | Class A | Standard QM convention; E1 boundary | Not modified by `σ(M)` or `R̂_svasa`. |
| `E_o` | Measurement effect associated with outcome `o`. | Hiệu ứng đo gắn với outcome `o`. | standard QM | Class A | `registration_layer_formalization.md`; system diagram | Not a VVV-QMRF operator. |
| `M = {E_o}` | QM measurement represented as effects/outcomes. | Phép đo QM dưới dạng tập hiệu ứng/outcome. | standard QM | Class A | `registration_layer_formalization.md`; system diagram | Distinguish from K-side `M` as measurement-registration act. |
| `p_QM(o)=Tr(E_oρ)` | Born-rule probability for outcome `o`. | Xác suất Born-rule cho outcome `o`. | standard QM | Class A | `registration_layer_formalization.md`; system diagram | Not replaced by `U_K`. |
| `ρ_after` | Post-measurement physical state. | Trạng thái vật lý sau phép đo. | standard QM | Class A | `registration_layer_formalization.md`; system diagram | Not the same as `K_after`. |

### 6.2 Registration-state symbols / Ký hiệu trạng thái ghi nhận

| Symbol | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `K` | Registration state. | Trạng thái ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md` | Not the physical state `ρ`. |
| `k` | One element of `𝒦`. | Một phần tử của không gian trạng thái ghi nhận `𝒦`. | registration-layer | Class C | `registration_layer_formalization.md` | Formal registration state, not a vector in `ℋ`. |
| `𝒦` | K-side registration-state space. | Không gian trạng thái ghi nhận phía K. | registration-layer | Class C | `registration_layer_formalization.md` | Not `ℋ` and not canonical QM state space. |
| `𝒦_pre` | Pre-symbolic registration stratum. | Tầng ghi nhận tiền biểu tượng. | registration-layer | Class C/D | `registration_layer_formalization.md`; S1-Λ source | Not raw consciousness. |
| `𝒦_sym` | Symbolic registration stratum. | Tầng ghi nhận đã có biểu tượng/ký hiệu. | registration-layer | Class C/D | `registration_layer_formalization.md`; S1-Λ source | Not Born-rule probability space. |
| `K_before` | Prior registration state before registered outcome update. | Trạng thái ghi nhận trước khi outcome được ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; system diagram | Not a pre-measurement wavefunction. |
| `K_after` | Posterior registration state after registered outcome update. | Trạng thái ghi nhận sau khi outcome được ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; system diagram | Not a new density matrix. |
| `cert` | Self-certification marker. | Dấu chứng nhận rằng sự kiện ghi nhận đã xảy ra. | registration-layer | Class C | `registration_layer_formalization.md`; E1 source | Formal marker only; not consciousness. |
| `t(M)` | Registration time of `M`. | Thời điểm ghi nhận của `M`. | registration-layer | Class B/D | `registration_layer_formalization.md` | Not a claim that physical time itself is discrete. |
| `t` | Registration-time component inside a K-state tuple. | Thành phần thời điểm ghi nhận trong tuple trạng thái K. | registration-layer | Class B/D | `registration_layer_formalization.md` | Not proof that physical time is discrete. |
| `V` | Validity status component inside a K-state tuple. | Thành phần trạng thái hợp lệ trong tuple trạng thái K. | registration-layer | Class D | `registration_layer_formalization.md` | Not absolute metaphysical truth and not a physical observable. |

### 6.3 Registration update and event symbols / Ký hiệu cập nhật và sự kiện ghi nhận

| Symbol | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `U_K` | Registration update rule. | Quy tắc cập nhật trạng thái ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; system diagram | Not Schrödinger evolution and not physical collapse. |
| `o` | Registered outcome supplied by the physical measurement side. | Outcome được phía vật lý cung cấp để tầng K ghi nhận. | bridge | Class B/D | `registration_layer_formalization.md`; system diagram | Outcome probabilities remain governed by QM. |
| `I` | Physical interaction entering possible registration. | Tương tác vật lý có thể đi vào ghi nhận. | bridge | Class B | `registration_layer_formalization.md` | Not every `I` becomes a valid `M`. |
| `M` | Measurement-registration act. | Hành vi đo-ghi nhận ở tầng K. | registration-layer | Class D | `registration_layer_formalization.md`; E1 source | Not identical to a bare physical interaction `I` or to `M={E_o}`. |
| `M′` | Second-order or meta-registration act. | Ghi nhận bậc hai hoặc meta-registration. | registration-layer | Class D | E1 source | E1 says `M′` is not required for primary certification. |
| `σ(M)` | Self-certification function. | Hàm tự chứng nhận sự kiện `M`. | registration-layer | Class D | E1 source; `registration_layer_formalization.md` | Certifies occurrence of `M` without `M′`; not a detector Hamiltonian. |
| `R̂_svasa` | Reflexive registration operator. | Toán tử ghi nhận phản thân. | registration-layer / BE-source lineage | Class D | E1 source; Category 05 source pointer inside E1 | Not a consciousness-collapse operator. |
| `≡^K` | K-side act-result inseparability. | Tính không tách rời giữa hành vi và kết quả ở tầng K. | registration-layer | Class D | `registration_layer_formalization.md` | Not physical identity in `ℋ`. |

### 6.4 Core registration operators, maps, and relations / Toán tử, ánh xạ, và quan hệ ghi nhận lõi

| Symbol | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `C` / `C_R` | Registration lock. | Khóa interaction thành trạng thái đã được ghi nhận. | bridge / registration-layer | Class D | `registration_layer_formalization.md`; E3 source | Does not by itself collapse `ρ`. |
| `ε(M)` | Pre-symbolic registration event. | Sự kiện ghi nhận tiền biểu tượng. | registration-layer | Class D | `registration_layer_formalization.md`; E4 source; S1-Λ source | Not a mystical perception event. |
| `Λ` | Symbolization operator. | Toán tử biểu tượng hóa. | registration-layer | Class D | `registration_layer_formalization.md`; S1-Λ source | Maps pre-symbolic registration to symbolic result; not the Born rule. |
| `r` | Symbolic registered result. | Kết quả ghi nhận đã được biểu tượng hóa. | registration-layer | Class D | `registration_layer_formalization.md`; S1-Λ source | Not the physical outcome probability itself. |
| `f_enc` | Internal encoding map. | Ánh xạ mã hóa nội tại. | registration-layer | Class D | `registration_layer_formalization.md`; E5 source | Not a second apparatus. |
| `V(M,t)` / `V(M)` | Validity status function. | Hàm trạng thái hợp lệ của ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; E7 source | K-side validity, not absolute metaphysical truth. |
| `⊥` | Registration contradiction relation. | Quan hệ mâu thuẫn ở tầng ghi nhận. | registration-layer | Class B/D | `registration_layer_formalization.md` | Not physical orthogonality unless separately specified. |
| `R=<M_1,M_2,...,M_n>` | Registering system as process. | Hệ ghi nhận như một chuỗi sự kiện. | registration-layer | Class D | `registration_layer_formalization.md`; E6 source | Not a fixed substantial observer. |
| `Δ(M_i,M_{i+1})` | Temporal registration gap. | Khoảng gián đoạn giữa hai lần ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; E13/S2 support | Not proof that physical time is discrete. |
| `Sym(ε(M))=∅` | No symbolic value at the pre-symbolic stage. | Chưa có giá trị biểu tượng ở tầng tiền biểu tượng. | registration-layer | Class D | `registration_layer_formalization.md`; E4 source | Not absence of physical interaction. |

### 6.5 Extended proposed category symbols / Ký hiệu đề xuất mở rộng theo category

| Symbol | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `P_null` / `P̂_null` | Null-projection registration operator. | Toán tử ghi nhận chiếu-rỗng. | bridge / registration-layer | Class D | `registration_layer_formalization.md`; Category 01 | Built on projection support; not canonical PVM by itself. |
| `Π̂_absent^(ℋ_M)` | Bounded absence projection. | Phép chiếu vắng mặt có giới hạn bởi không gian đo được `ℋ_M`. | bridge / registration-layer | Class D support | E14 / VAR source | Valid only inside measurement-accessible subspace `ℋ_M`. |
| `ℋ_M` | Measurement-accessible subspace used by VAR. | Không gian con mà thiết lập đo có thể kiểm tra. | bridge | Class B/D | E14 / VAR source | Does not cover what the setup cannot validly test. |
| `I_(ℋ_M)` | Identity operator on `ℋ_M`. | Toán tử đơn vị trên không gian con `ℋ_M`. | bridge | Class B | E14 / VAR source | Only scoped to the declared measurement-accessible subspace. |
| `λ_i` | Tested property/eigenvalue label inside `ℋ_M`. | Nhãn thuộc tính/eigenvalue được kiểm tra trong `ℋ_M`. | bridge | Class B | E14 / VAR source | Absence claim applies only to the tested set. |
| `Ĉ_ext` | Extrinsic registration-certification operator. | Toán tử chứng nhận ghi nhận từ ngoài. | registration-layer | Class D | `registration_layer_formalization.md`; Category 04 | Certification layer, not environmental decoherence itself. |
| `ρ̃` | Conditionally updated physical state. | Trạng thái vật lý được cập nhật có điều kiện. | bridge | Class D | `registration_layer_formalization.md`; Category 04 | Provisional notation; not a new density-matrix law. |
| `ρ_certified` | Certified registration-status label. | Nhãn trạng thái ghi nhận đã được chứng nhận. | bridge / registration-layer | Class D | `registration_layer_formalization.md`; Category 04 | Status label, not a canonical physical state. |
| `Â_kara` | Internal representation encoding operator. | Toán tử mã hóa biểu tượng nội tại. | registration-layer / BE-source lineage | Class D | `registration_layer_formalization.md`; Category 08 | Source lineage only; not mystical cognition. |
| `V̂_yava` | Irreversible registration lock. | Khóa ghi nhận không đảo ngược ở tầng K. | registration-layer / BE-source lineage | Class D | `registration_layer_formalization.md`; Category 08 | Registration lock, not proof of physical irreversibility. |
| `𝒯_act-res` | Act-result tensor. | Tensor nối hành vi-kết quả ở tầng ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; Category 02 | Not a Born-rule tensor. |
| `Ô_bhranti` | Invalidation / registration override operator. | Toán tử phủ quyết hoặc ghi đè ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; Category 03 | Reclassifies registration status; does not alter physical history. |
| `Ê_empty` | Null registration operator. | Toán tử ghi nhận rỗng. | registration-layer | Class D | `registration_layer_formalization.md`; Category 06 | Marks non-engagement after interaction; not every no-result measurement. |
| `Π̂_causal` | Causal memory projection. | Phép chiếu ký ức nhân quả ở tầng ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; Category 07 | Continuity without identity; not hidden-variable memory. |
| `𝕍_tri` | Tripartite apparatus validity tensor / criteria set. | Bộ tiêu chí/tensor hợp lệ ba phần. | registration-layer | Class D | `registration_layer_formalization.md`; Category 09 / E10 | Validity gate, not detector physics itself. |
| `M̂_trans` | Limit-faculty registration operator. | Toán tử ghi nhận của năng lực giới hạn. | registration-layer | Class D | `registration_layer_formalization.md`; Category 11 / E12 | Validity-gated non-ordinary registration; not new eigenvalue physics. |
| `T̂_kṣaṇa` | Discrete transition operator. | Toán tử chuyển đoạn rời rạc của ghi nhận. | registration-layer | Class D | `registration_layer_formalization.md`; Category 12 / E13 | Registration transition marker; not replacement for quantum jump operators. |
| `Ŝ_saṃśaya` | Structured registration-doubt operator. | Toán tử nghi vấn ghi nhận có cấu trúc. | registration-layer | Class D | `registration_layer_formalization.md`; Category 15 / E16 | K-side suspension, not hidden-variable ignorance. |
| `ℰ_svabh` | Intrinsic relational binding symbol. | Ký hiệu liên kết quan hệ nội tại. | registration-layer relation category | Class D folded symbol | `registration_layer_formalization.md`; Category 14 / E15 | Not a new physical force. |

### 6.6 BE-source lineage labels / Nhãn dòng nguồn Phật học

| Label | Meaning EN | Nghĩa VN | Domain | Claim class | Source trace | Boundary |
|---|---|---|---|---|---|---|
| `Svasaṃvedana` | Self-awareness as BE source lineage for self-certification. | Tự tri như dòng nguồn BE cho tự chứng nhận. | BE-source lineage | BE-source | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E1 source | Not a consciousness-collapse mechanism. |
| `Pramāṇa-phala` | Act-result relation as BE source lineage. | Quan hệ phương tiện-kết quả nhận thức. | BE-source lineage | BE-source | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E2/Category 02 sources | Structural lineage only, not QM identity. |
| `Apoha` | Exclusion as BE source lineage. | Loại trừ như dòng nguồn BE. | BE-source lineage | BE-source | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; mapping sources | Not identical to quantum complementarity. |
| `Anupalabdhi` | Non-perception / absence cognition as BE source lineage. | Vắng mặt được nhận biết hợp lệ. | BE-source lineage | BE-source | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E14 / VAR source | Not a physical substance or a canonical QM operator. |
| `Trairūpya` | Three-condition validity criterion as source lineage. | Tiêu chuẩn ba điều kiện cho tính hợp lệ. | BE-source lineage | BE-source | `SYSTEM_Buddhist_Epistemology/system_be_full.md`; E10/E14 sources | Validity gate analogue, not native QM formalism. |

---

## 7. Formula Inventory / Danh sách công thức

| Formula ID | Formal expression | Formula class | Domain of validity | Source trace | Interpretation boundary |
|---|---|---|---|---|---|
| F-K-001 | `k ∈ 𝒦; k=<M,o,cert,t,V>` | definition | Minimal K-side registration-state tuple. | `registration_layer_formalization.md` | Defines registration state only; not a physical state vector or density matrix. |
| F-K-002 | `K_after = U_K(K_before,o)` | heuristic_formalization | K-side registration-state update after a physical outcome is available. | `registration_layer_formalization.md`; system diagram | Not Schrödinger evolution, Born-rule probability, or physical collapse. |
| F-E1-001 | `σ(M)=1 iff M occurred as K-side registration` | definition | K-side self-certification marker for E1. | E1 framework source | Does not require `M′`; not consciousness-caused collapse. |
| F-E2-001 | `M ≡^K r` | heuristic_formalization | K-side registration self-completion. | `registration_layer_formalization.md`; E2 source | Act-result inseparability inside `𝒦`; not physical identity in `ℋ`. |
| F-E7-001 | `V(M)=1; V(M)->0 iff later contradictory M′ invalidates M` | constraint | K-side validity and invalidation. | `registration_layer_formalization.md`; E7/E8 sources | K-side validity rule; not universal metaphysical truth. |
| F-S1-001 | `I -> ε(M) -> Λ(ε(M))=r` | lemma_expression | Registration flow from interaction to symbolic result. | `registration_layer_formalization.md`; S1-Λ source | Not a replacement for detector physics. |
| F-E3-001 | `C: ℋ -> 𝒦; C(I)=k_locked` | mapping_function | Bridge from available interaction to locked registration status. | `registration_layer_formalization.md`; E3 source | Does not by itself collapse `ρ`. |
| F-E4-001 | `ε(M) ∈ 𝒦_pre; Sym(ε(M))=∅` | definition | Pre-symbolic registration stage. | `registration_layer_formalization.md`; E4 source | No symbolic value yet; not absence of physical interaction. |
| F-S1-002 | `Λ: 𝒦_pre -> 𝒦_sym; r=Λ(ε(M))` | lemma_expression | Symbolization interface between E4 and E5. | S1-Λ source | Interface/lemma status; not a separate postulate by default. |
| F-E14-001 | `Π̂_absent^(ℋ_M)=I_(ℋ_M)-Σ_i |λ_i><λ_i|` | heuristic_formalization | Validated absence registration inside accessible subspace `ℋ_M`. | E14 / VAR source | Does not assert absence outside the tested subspace. |

---

## 8. Concept Traceability / Truy vết concept

| Concept | Canonical name | Source | Role | Boundary |
|---|---|---|---|---|
| E1 | Self-certifying registration | `framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Blocks K-side regress by making primary registration self-certifying. | Not a consciousness claim and not `ρ`-side collapse. |
| E2 | Registration self-completion | `framework/vvv_qmrf_framework_e02_registration_self_completion_postulate.md` | Treats act/result completion as K-side registration structure. | Not physical identity in `ℋ`. |
| E3 | Registration lock | `framework/vvv_qmrf_framework_e03_registration_lock_postulate.md` | Locks an available interaction into registered status. | Not by itself physical collapse. |
| E4 | Pre-symbolic registration stratum | `framework/vvv_qmrf_framework_e04_pre_symbolic_registration_stratum_postulate.md` | Defines raw registration before symbolic value. | Not mystical perception and not absence of physical interaction. |
| E5 | Internal representation encoding | `framework/vvv_qmrf_framework_e05_internal_representation_encoding_postulate.md` | Encodes registered outcome internally. | Not a second apparatus measurement. |
| E6 | Registering system as process | `framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md` | Treats registering system as ordered events. | Not a fixed substantial observer. |
| E7 | Registration validity location | `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` | Places validity at K-side registration status. | Not absolute metaphysical truth. |
| E8 | Retroactive registration override | `framework/vvv_qmrf_framework_e08_retroactive_registration_override_postulate.md` | Reclassifies prior registration status when contradicted. | Does not alter physical history. |
| E14 | Validated absence registration | `category/vvv_qmrf_category_13_e14_validated_absence_registration.md`; E14 framework source | Makes controlled absence a positive registration category when validity conditions hold. | Not ordinary detector silence or failed measurement. |
| S1-Λ | Registration natural interface lemma | `synthesis/vvv_qmrf_synthesis_s1_lambda_registration_natural_interface_lemma.md` | Connects pre-symbolic event to symbolic registration. | Lemma/interface, not postulate unless future RCA upgrades it. |

---

## 9. Relationship Rules / Quy tắc quan hệ

| Relation | Meaning | Required boundary |
|---|---|---|
| `ρ-side -> K-side input` | Physical outcome can enter registration update. | Physical probability remains governed by Standard QM. |
| `source_of` | A BE concept provides source lineage for a VVV-QMRF registration concept. | Source lineage is not identity. |
| `structural_analogy` | A BE relation and a QM/VVV-QMRF relation share a useful structure. | Analogy is not proof. |
| `derives_from` | A VVV-QMRF symbol follows from an active framework/category/synthesis document. | Show source trace and claim class. |
| `depends_on` | A formula requires previously defined symbols. | No formula may use an undefined symbol. |
| `contrast_with` | A valid category is separated from similar-looking non-cases. | Define the negative control, especially for null/absence registration. |

---

## 10. Failure Modes / Các cách hiểu lệch cần chặn

| Failure mode | Prevention |
|---|---|
| Reading `K` as `ρ`. | Always state `K` is registration state and `ρ` is physical quantum state. |
| Reading `𝒦` as `ℋ`. | Mark `𝒦` as Class C VVV-QMRF registration-state space, not Hilbert space. |
| Reading `U_K` as a new physical evolution law. | State that `U_K` updates registration status only. |
| Reading `σ(M)` or `R̂_svasa` as consciousness-caused collapse. | State that E1 is structural self-certification at K-side. |
| Reading `Π̂_absent^(ℋ_M)` as proof of absence everywhere. | Restrict it to measurement-accessible subspace `ℋ_M`. |
| Reading `detector response` as identical to `registration-state update`. | Use `detector response` only for apparatus physical response; use `registration-state update` for K-side update. |
| Reading BE-source terms as QM operators. | Keep them in BE-source lineage unless a VVV-QMRF source explicitly defines a derived operator. |

---

## 11. Update Rule / Quy tắc cập nhật

1. Add a new symbol only after it has meaning, domain, claim class, source trace, and boundary.
2. Add or update formulas only after every symbol in the formula appears in this registry.
3. If an active framework, category, synthesis, or meta-architecture document changes a symbol status, update this registry in the same change set.
4. If a source uses legacy terminology, preserve it only as trace and use the current normalized label.
5. If a formula looks stronger than its source evidence, downgrade the claim class before publication-facing reuse.
6. Course-level documents may simplify wording, but they must not weaken the claim boundary in this registry.

---

## 12. What This Registry Does NOT Claim / Những gì registry này KHÔNG tuyên bố

- It does not claim that VVV-QMRF replaces Standard Quantum Mechanics.
- It does not modify the Born rule, Schrödinger equation, Hamiltonian dynamics, or canonical QM state-update rules.
- It does not claim that Buddhist Epistemology proves Quantum Mechanics.
- It does not identify `detector response` with `registration-state update`.
- It does not treat derived VVV-QMRF notation as canonical QM notation.
- It does not treat BE-source terms as physical operators.
- It does not make Class C or Class D symbols peer-reviewed or experimentally validated.

---

## 13. Validation Checklist / Checklist kiểm chứng

| Check | Pass condition |
|---|---|
| Metadata | Author metadata exists and `document_type` is `index`. |
| Source corpus | Schema guide and active research sources are listed. |
| Claim types | Major claims are classified by type or class. |
| Symbol registry | Every retained symbol has meaning, domain, claim class, source trace, and boundary. |
| Formula registry | Every formula has formula class, domain of validity, source trace, and interpretation boundary. |
| K-side vs ρ-side | Registration-layer claims do not modify physical QM. |
| Terminology | `registration-state update` is used for K-side update; `detector response` is reserved for apparatus response. |
| BE boundary | BE-source labels are structural lineage, not QM identity claims. |
| Overclaim check | No claim says BE proves, solves, or replaces QM. |
| Update rule | New symbols and formulas must be added here before reuse. |
