# RCA — Báo cáo Toàn diện về TV1 / TV2 / TV3
## VVV-QMRF · E10 Tripartite Validity · VietVunVut (2026)

**Ngày lập báo cáo:** 2026-05-29T16:09:27+07:00  
**Nguồn chính:** Plan v2.3 · Framework §3a-d · AHP trace · Category 09  
**Phạm vi:** Registration-layer supplement — không thay thế Standard QM P1-P4

---

## PHẦN I — BỐI CẢNH VÀ NGUỒN GỐC

### 1.1. Vấn đề gốc rễ — BIAN-14

| Mục | Nội dung |
|---|---|
| **BIAN** | BIAN-14 |
| **Tên khoảng trống** | Tripartite Measurement Validity Conditions |
| **Mô tả** | Standard QM P1-P4 không quy định tập điều kiện tầng ghi nhận (registration-layer) để phân biệt một phép đo-ghi nhận hợp lệ với một tín hiệu nhiễu vật lý hoặc sự kiện decoherence. Một detector có thể trải qua decoherence mà không tạo ra sự kiện ghi nhận hợp lệ theo ngữ nghĩa VVV-QMRF. |
| **Nguồn BE** | Trairūpya (N_BE_00018) — Dignāga–Dharmakīrti |
| **Giải pháp** | E10 cung cấp tập điều kiện TV1/TV2/TV3 |
| **Trạng thái** | ✅ Resolved — Category 09 + E10 |

### 1.2. Nguồn gốc Phật giáo — Trairūpya (Tam tướng)

Trairūpya (त्रैरूप्य) là cấu trúc ba điều kiện của suy luận hợp lệ trong triết học Dignāga–Dharmakīrti. Ba **rūpa** (tướng / mark) mà một **hetu** (lý do) hợp lệ phải thỏa:

| Mark | Sanskrit | Pali tương ứng | Tên VN | Nội dung logic |
|---|---|---|---|---|
| Mark 1 | Pakṣadharmatva (पक्षधर्मत्व) | Pakṣadharmatā | Sự hiện diện ở chủ thể | Hetu H phải là thuộc tính của chủ thể S |
| Mark 2 | Anvaya (अन्वय) = Sapakṣasattva (सपक्षसत्त्व) | — | Tương quan dương tính | Ở mọi nơi H có mặt, kết luận C có mặt — đánh giá trên *sapakṣa* (tập trường hợp dương) |
| Mark 3 | Vyatireka (व्यतिरेक) = Vipakṣāsattva (विपक्षासत्त्व) | — | Tương quan âm tính | Ở mọi nơi C vắng, H vắng — đánh giá trên *vipakṣa* (tập trường hợp âm / counter-cases) |

> **Lưu ý quan trọng (RCA v1.0 → v2.0):** Trong logic vị từ Boolean, Anvaya (P→Q) và Vyatireka (¬Q→¬P) là **logically equivalent** (contrapositives). Chúng chỉ thực sự độc lập khi được đánh giá trên **hai tập mẫu khác nhau**:
> - Anvaya → TV2 → Sensitivity: kiểm tra trên *sapakṣa* (detector khi nên bắn)
> - Vyatireka → TV3 → Specificity: kiểm tra trên *vipakṣa* (detector khi không nên bắn)

---

## PHẦN II — ĐỊNH NGHĨA HÌNH THỨC

### 2.0. Formal Objects (Các đối tượng hình thức)

```
rho   ∈ S(H)        = quantum state (density operator trên Hilbert space H)
d     ∈ D           = detector response event (sự kiện tương tác vật lý)
R_sys               = registering system (hệ ghi nhận — được xem như process per E6)
M ∈ {active, inactive} = registration mode của R_sys
                     (active iff R_sys ở trong cấu hình đo được hiệu chuẩn và
                     hướng vào quantum system — do experimental configuration quyết định,
                     KHÔNG phải do quantum state được đo quyết định)
r   ∈ R             = registered result (tập kết quả rời rạc)
r_null              = null registration status (từ E9)
V̂(rho, d)          = registration operator → (r, rho_certified) hoặc (r_null, rho_unchanged)
Phi(rho, d)         = physical decoherence event (không có registration label)
epsilon_det ∈ [0,1) = missed-detection threshold (sensitivity calibration parameter)
epsilon_fp  ∈ [0,1) = false-positive threshold (specificity calibration parameter)
```

---

### 2.1. TV1 — Pakṣadharmatva — Subject Property Condition

#### Loại predicate: **BOOLEAN**

```
TV1(d, R_sys) : D × R_sys → {true, false}

TV1(d, R_sys) := d is causally produced by R_sys in response to the quantum system
                 AND
                 d is NOT a spurious event (dark count, thermal noise, background)

TV1 = TRUE  iff  d là phản hồi causal của R_sys đối với quantum system
TV1 = FALSE iff  d là nhiễu nền, dao động nhiệt, hoặc tín hiệu spurious
                 không có kết nối causal với quantum system
```

#### Định nghĩa tác vụ của "causally produced":
```
d được tạo ra trong interaction window xác định bởi H_int (coupling Hamiltonian),
KHÔNG phải từ thermal bath nội bộ của detector độc lập với quantum system.
Operationalized qua: timing gates + dark-count characterization.
```

#### Kết nối với E4 (Pre-Symbolic Layer):
```
TV1 = TRUE yêu cầu d đã đi qua Pre-Symbolic Layer (E4).
Dao động nhiệt thuần túy trong vật liệu detector KHÔNG BAO GIỜ vào E4 processing.
TV1 là cổng (gate) giữa physical events và registration pipeline.
```

#### K-Axiom Anchors:
| K-Axiom | Lý do anchor |
|---|---|
| **K1** (act-result co-instantiation) | TV1=true yêu cầu d và rho được co-instantiated qua cùng một interaction event coupling với rho |
| **K7** (closure) | TV1=true nghĩa là d nằm trong registration closure của R_sys |

#### Failure consequence:
```
TV1 = FALSE → V̂(rho, d) = (r_null, rho_unchanged) [E9 null registration]
Tất cả sự kiện TV1=FALSE được gán là null registration (r_null) per E9,
bất kể TV2/TV3 có giá trị gì.
```

---

### 2.2. TV2 — Anvaya / Sapakṣasattva — Positive Concomitance — Sensitivity

#### Loại predicate: **PROBABILISTIC** (Sensitivity)
#### Tập kiểm tra: *sapakṣa* = positive cases (những trường hợp detector NÊN bắn)

```
TV2(R_sys, epsilon_det) := P(r ≠ r_null | TV1(d, R_sys) = true, M = active) ≥ 1 − ε_det

Meaning:
  Trong tập hiệu chuẩn dương (sapakṣa), khi:
    - d causally được tạo bởi quantum system (TV1=true)
    - R_sys ở active registration mode (M=active)
  xác suất tạo ra kết quả ghi nhận hợp lệ (r ≠ r_null) ≥ 1 − ε_det

TV2 = TRUE  iff  hệ thống ghi nhận đáp ứng sensitivity threshold ε_det
TV2 = FALSE iff  hệ thống bỏ sót các sự kiện hợp lệ với tỷ lệ vượt ε_det
                 (inefficient detector, low quantum efficiency)

ε_det = 0  (giới hạn lý tưởng): mọi causal event với M=active đều cho r ≠ r_null
ε_det = 1 − η (thực tế): η là quantum detection efficiency
```

#### Kết nối với E3 (Registration Lock):
```
TV2 là hướng sensitivity của điều kiện Registration Lock.
TV2 = FALSE chỉ ra V̂ không hiệu quả (E3 condition I hoặc SC có thể fail).
```

#### Kết nối với Standard QM:
```
P3 (Standard QM) ngầm giả thiết TV2 ở ε_det=0 — measurement LUÔN cho một kết quả.
E10 làm TV2 TƯỜNG MINH, có tham số, và có thể tách biệt khỏi TV1 và TV3.
```

#### K-Axiom Anchors:
| K-Axiom | Lý do anchor |
|---|---|
| **K2** (temporal injectivity) | Các causal event riêng biệt tạo ra các kết quả riêng biệt theo thời gian; TV2 bounds the false-negative rate of this injectivity |
| **K4** (registration validity) | V̂ phải tạo ra chứng chỉ hợp lệ r; TV2 đảm bảo điều này với calibrated sensitivity |

---

### 2.3. TV3 — Vyatireka / Vipakṣāsattva — Negative Concomitance — Specificity

#### Loại predicate: **PROBABILISTIC** (Specificity) — INDEPENDENT với TV2
#### Tập kiểm tra: *vipakṣa* = counter-cases (những trường hợp detector KHÔNG NÊN bắn)

```
TV3(R_sys, epsilon_fp) := P(r ≠ r_null | TV1(d, R_sys) = false OR M = inactive) ≤ ε_fp

Meaning:
  Trong tập hiệu chuẩn âm (vipakṣa), khi:
    - d KHÔNG phải causal từ quantum system (TV1=false)
      HOẶC R_sys không ở active mode (M=inactive)
  xác suất tạo ra kết quả spurious non-null (false registration) ≤ ε_fp

TV3 = TRUE  iff  hệ thống đáp ứng specificity threshold ε_fp (low dark count rate)
TV3 = FALSE iff  hệ thống tạo ra spurious registration vượt ε_fp

ε_fp = 0  (giới hạn lý tưởng): spurious events KHÔNG BAO GIỜ tạo r ≠ r_null
ε_fp thực tế = dark count rate / total spurious event rate
```

#### TV3 trong giới hạn lý tưởng (ε_fp→0) — Self-Completion:
```
TV3 (ε_fp→0) phát biểu: trong giới hạn lý tưởng, V̂ tạo r≠r_null CHỈ KHI TV1=true
và M=active. Đây là điều kiện CLOSED — không cần meta-certifier.
r_null là self-certified absence of registration.
KHÔNG có regress vì điều kiện được phát biểu như probability bound hiệu chuẩn,
KHÔNG phải thuộc tính cần đánh giá runtime bởi một certifier riêng.
→ TV3 cung cấp nội dung cấu trúc của E3-SC (Self-Completion).
```

#### Kết nối với E9 (Null Registration Event):
```
TV3 cung cấp calibration structure cho E9.
E9: physical interaction + zero information = distinct registration status.
TV3: distinct status đó (r_null) phải xảy ra với rate ≥ 1−ε_fp cho spurious events.
```

#### Kết nối với E11 (Contrapositive Evidence):
```
TV3 cung cấp calibration basis cho E11.
Khi TV3 holds với ε_fp→0, r_null là valid registration of absence —
cầu nối logic giữa E10 và E11.
```

#### K-Axiom Anchors:
| K-Axiom | Lý do anchor |
|---|---|
| **K3** (self-certification) | Null output r_null của V̂ phải self-certify absence of valid registration; TV3 bounds the false-certificate rate |
| **K4** (registration validity) | TV3 đảm bảo V̂ không tạo spurious r≠r_null outputs vượt ε_fp |

---

## PHẦN III — TV1/TV2/TV3 LÀ ĐỘC LẬP — TẠI SAO VÀ BẰNG CHỨNG

### 3.1. Lý do cần tính độc lập

| So sánh | TV2 (Sensitivity) | TV3 (Specificity) |
|---|---|---|
| **Câu hỏi** | Detector có bắn khi NÊN bắn không? | Detector có IM LẶNG khi KHÔNG NÊN bắn không? |
| **Tập đánh giá** | sapakṣa (positive cases) | vipakṣa (counter-cases / negative cases) |
| **Metric** | P(register \| should register) ≥ 1−ε_det | P(no-register \| should not register) ≥ 1−ε_fp |
| **Cơ chế vật lý** | Quantum efficiency η — absorption, conversion | Dark count suppression — shielding, cooling |
| **Engineering handle** | Cải thiện absorption (↑η) | Cải thiện thermal isolation (↓dark count) |

### 3.2. Ví dụ độc lập thực tế

```
Detector A: Sensitive nhưng không Specific (TV2=true, TV3=false)
  → Bắn tin cậy trên real events (η cao)
  → NHƯNG cũng bắn spuriously (dark count rate cao, shielding kém)
  → TV2=true, TV3=false: logically possible và physically realizable

Detector B: Specific nhưng không Sensitive (TV2=false, TV3=true)
  → Hiếm khi bắn spuriously (dark count rate thấp, shielding tốt)
  → NHƯNG bỏ sót nhiều real events (η thấp)
  → TV2=false, TV3=true: logically possible và physically realizable

→ Hai trường hợp này BỊ LOẠI TRỪ trong v1.0 (Boolean TV2≡TV3)
→ ĐƯỢC PHỤC HỒI trong v2.0 (probabilistic TV2/TV3 độc lập)
```

### 3.3. Ví dụ SNSPD (Superconducting Nanowire Single-Photon Detector)

```
Cooling (↓ nhiệt độ):
  → Giảm dark count rate = ε_fp ↓ = TV3 ↑ (specificity cải thiện)
  → NHƯNG KHÔNG tự động thay đổi detection efficiency = ε_det, TV2

→ TV2 và TV3 có engineering handles riêng biệt
→ Nhất quán với dự đoán E10 rằng TV2 và TV3 độc lập
```

---

## PHẦN IV — CONJUNCTION TV VÀ TRUTH TABLE

### 4.1. Định nghĩa TV Conjunction

```
DEFINITION — Tripartite Validity (TV):

TV(rho, d, R_sys) := TV1(d, R_sys)
                     AND TV2(R_sys, ε_det)
                     AND TV3(R_sys, ε_fp)

Khi TV = TRUE:
  V̂(rho, d) = (r, rho_certified)  với r ≠ r_null  [valid registration]

Khi TV = FALSE (bất kỳ điều kiện nào fail):
  V̂(rho, d) = (r_null, rho_unchanged)              [null registration, E9]
```

### 4.2. Truth Table đầy đủ (8 hàng)

| TV1 | TV2 | TV3 | TV | Trạng thái Ghi nhận | Lý do vật lý |
|---|---|---|---|---|---|
| TRUE | TRUE (sens.) | TRUE (spec.) | **TRUE** | ✅ Valid registered measurement | Tất cả điều kiện thỏa |
| TRUE | TRUE (sens.) | **FALSE** | FALSE | ❌ Null — spurious events exceed ε_fp | TV3=false: dark count cao, specificity thấp |
| TRUE | **FALSE** | TRUE (spec.) | FALSE | ❌ Null — missed detections exceed ε_det | TV2=false: quantum efficiency thấp |
| TRUE | **FALSE** | **FALSE** | FALSE | ❌ Null — cả sensitivity VÀ specificity fail | Detector kém cả hai hướng |
| **FALSE** | * | TRUE (spec.) | FALSE | ❌ Null — TV1=false: spurious signal | d không phải từ quantum system, dù TV2/TV3 thế nào |
| **FALSE** | * | **FALSE** | FALSE | ❌ Null — spurious và non-specific | TV1=false + specificity thấp |
| **FALSE** | **FALSE** | * | FALSE | ❌ Null | TV1=false |
| **FALSE** | **FALSE** | **FALSE** | FALSE | ❌ Null — pure decoherence, no registration | Decoherence thuần, không có registration layer |

> **QUAN TRỌNG:** Các hàng `TV2=TRUE, TV3=FALSE` và `TV2=FALSE, TV3=TRUE` là LOGICALLY POSSIBLE với v2.0.  
> Trong v1.0 (Boolean), những hàng này BỊ LOẠI TRỪ vì TV2≡TV3 (contrapositive equivalent) → lỗi nghiêm trọng.

### 4.3. Born-limit Compatibility

```
Khi ε_det → 0 AND ε_fp → 0:
  E10 tương thích với giả thiết P3 của Standard QM (measurement luôn cho kết quả)
  trong bối cảnh đo lý tưởng.

ĐÂY LÀ tuyên bố tương thích registration-layer,
KHÔNG PHẢI là chứng minh E10 suy ra hoặc thay thế P3 đầy đủ của Standard QM.
```

---

## PHẦN V — PHÂN BIỆT VỚI DECOHERENCE (Proof Sketch)

### 5.1. Luận điểm chính

```
Decoherence là ĐIỀU KIỆN CẦN nhưng KHÔNG ĐỦ cho valid registration.
Phi(rho, d) does NOT imply TV(rho, d, R_sys).
```

### 5.2. Ba-phần chứng minh

```
(1) Decoherence có thể xảy ra mà KHÔNG có TV1:
    Ví dụ: Dao động nhiệt trong vật liệu detector gây ra pointer-basis selection
    trong một sub-component của R_sys mà KHÔNG phải do quantum system tạo ra.
    TV1 = false, decoherence occurred.
    → Decoherence does NOT imply TV1.

(2) Decoherence có thể xảy ra mà KHÔNG có TV2:
    Ví dụ: R_sys trải qua decoherence nhưng KHÔNG ở active registration mode
    (e.g., detector đang calibration, không đang đo).
    TV2 = false, decoherence occurred.
    → Decoherence does NOT imply TV2.

(3) Decoherence có thể xảy ra mà KHÔNG có TV3:
    Ví dụ: Detector có dark count rate vượt ε_fp (shielding kém).
    Decoherence xảy ra trong detector nhưng hệ thống cũng bắn spuriously
    trên thermal events — TV3 = false (specificity threshold vi phạm).
    → Decoherence does NOT imply TV3.

→ Kết luận scope-safe:
  TV là STRICTER hơn decoherence ở tầng registration.
  Đây là sự phân biệt hình thức mà BIAN-14 xác định là không được quy định bởi P1-P4.
```

### 5.3. Ghi chú về Quantum Eraser (lỗi đã sửa)

```
Quantum Eraser KHÔNG phải là ví dụ cho TV3.
Quantum Eraser là sự kiện E8 (Retroactive Override):
  → Nó hoạt động RETROACTIVELY trên một registration đã xảy ra trước đó.
  → E8 retroactively sets TV=false cho một prior registration.
  → Đây là hành động E8 trên một TV record trước, KHÔNG PHẢI TV3 failing
    trong initial registration attempt.

Sử dụng quantum eraser như TV3 example = CATEGORY ERROR (E8 ≠ TV3 failure).
```

---

## PHẦN VI — ÁNH XẠ TV → E3 REGISTRATION LOCK

### 6.1. Bảng cross-reference

| E3 Condition | TV Condition | Buddhist Mark | Nội dung hình thức |
|---|---|---|---|
| **I** (Irreversibility — Tính bất khả nghịch) | TV2 + TV1 | Anvaya + Pakṣadharmatva | Causal + sensitivity grounding |
| **D** (Distinctness from projection — Phân biệt với phép chiếu) | TV1 | Pakṣadharmatva | Subject-property check vắng mặt trong PVM |
| **SC** (Self-Completion — Tự hoàn chỉnh) | TV3 (ε_fp→0) | Vyatireka | Specificity closure → no regress |

### 6.2. Giải thích chi tiết

```
E3-D (Distinctness):
  TV1 thêm kiểm tra "d có phải causally produced bởi quantum system không?"
  Projection operators (PVM) trong Standard QM KHÔNG kiểm tra điều này.
  → TV1 là nội dung hình thức của E3-D.

E3-I (Irreversibility):
  Nếu V̂ tạo ra r, TV2 đảm bảo các precondition đã được thỏa.
  Reversing r sẽ yêu cầu un-satisfying các precondition đó retroactively.
  Vì TV1 là điều kiện causal (d was produced by quantum system),
  và causal events cannot be un-caused, TV2+TV1 jointly ground irreversibility.

E3-SC (Self-Completion):
  TV3 KHÔNG phát biểu Boolean absolute: "r_null ⇒ preconditions failed"
  Thay vào đó, TV3 bounds the false-positive certification rate:
    P(r ≠ r_null | TV1=false OR M=inactive) ≤ ε_fp
  Trong giới hạn lý tưởng ε_fp→0, r_null trở thành self-certified absence
  of valid registration. Không cần meta-certifier riêng.
  → TV3 là nội dung cấu trúc của E3-SC.
```

---

## PHẦN VII — K-AXIOM ANCHOR TABLE (Đầy đủ)

| TV Component | K-Axiom | Lý do Anchor |
|---|---|---|
| TV1 (Boolean) | **K1** | Act-result co-instantiation: TV1=true yêu cầu d và rho được co-instantiated qua cùng interaction event coupling với rho. K1 formalizes co-occurrence condition này. |
| TV1 (Boolean) | **K7** | Closure: TV1=true nghĩa là d nằm trong registration closure defined by R_sys's coupling với quantum system. |
| TV2 (Sensitivity) | **K2** | Temporal injectivity: distinct causal events tạo distinct results theo thời gian; TV2 bounds the false-negative rate của injectivity này. |
| TV2 (Sensitivity) | **K4** | Registration validity: V̂ phải tạo valid certificate r; TV2 đảm bảo điều này ở calibrated rate. |
| TV3 (Specificity) | **K3** | Self-certification: null output r_null của V̂ phải self-certify absence of valid registration; TV3 bounds the false-certificate rate (dark count). |
| TV3 (Specificity) | **K4** | Registration validity: TV3 đảm bảo V̂ không tạo spurious r≠r_null outputs vượt ε_fp. |
| TV (conjunction) | **K5** | Incommensurability boundary: TV conjunction phân tách local registration validity khỏi cross-registration incommensurability. TV=true là local validity precondition cho K_joint work sau này; KHÔNG phải proof of full K_joint validity. |

---

## PHẦN VIII — AHP TRACEABILITY (SOT Anchors)

### 8.1. Component Inventory và Trace Scores

| Component | Định nghĩa | Claim Class | BE SOT | K-Space SOT | Framework SOT | Trace Score | Label |
|---|---|---|---|---|---|---|---|
| **TV1** | Boolean: d causally produced by R_sys, not by noise | Formalized core predicate | N_BE_00018 Trairupya / Paksadharmatva | K1, K7 | E10 §3a | **4/5** | [AH-OK] |
| **TV2** | Probabilistic sensitivity: P(r≠r_null \| TV1=T, M=active) ≥ 1−ε_det | Formalized core predicate | N_BE_00018 Trairupya / Anvaya-Sapaksasattva | K2, K4 | E10 §3a | **4/5** | [AH-OK] |
| **TV3** | Probabilistic specificity: P(r≠r_null \| TV1=F OR M=inactive) ≤ ε_fp | Formalized core predicate | N_BE_00018 Trairupya / Vyatireka-Vipaksasattva | K3, K4 | E10 §3a | **4/5** | [AH-OK] |
| **epsilon_det** | Missed-detection threshold cho TV2 | Calibration parameter | Indirect via TV2 | K2, K4 | E10 §3a | 3/5 | [AH-WATCH] |
| **epsilon_fp** | False-positive threshold cho TV3 | Calibration parameter | Indirect via TV3 | K3, K4 | E10 §3a | 3/5 | [AH-WATCH] |
| **M** | Active/inactive process-state của R_sys | Minimal process variable | Indirect via registration process | E6; K7 closure | E10 §3a | 3/5 | [AH-WATCH] |
| **r_null** | Null registration status khi TV fails | Core registration status | Indirect via absence/null status | K3, K4 | E9; E10 §3b | **4/5** | [AH-OK] |
| **V̂** | Registration operator: certified result hoặc r_null | Formal operator | Indirect via registration lock | K1-K4 | E3; E10 §3a-§3b | **4/5** | [AH-OK] |
| **Phi** | Physical decoherence không có registration label | Scope-boundary symbol | Not a BE claim | Boundary only | E10 §3b | 3/5 | [AH-WATCH] |

> **Không có component nào là [AH-CRIT].** AHP Composite Score: 4.5/5 — ABOVE threshold.

---

## PHẦN IX — LỊCH SỬ RCA VÀ CÁC LỖI ĐÃ SỬA

### 9.1. Timeline phiên bản

| Version | RCA Score | Trạng thái | Vấn đề chính |
|---|---|---|---|
| **v1.0** | 2.9/5 | ❌ BELOW threshold — phải sửa | TV2≡TV3 (Boolean contrapositives); thiếu §0; M undefined; quantum eraser dùng sai |
| **v2.0** | 4.0/5 | ✅ AT threshold | TV2/TV3 → probabilistic; §0 thêm; M defined; quantum eraser → E8 |
| **v2.1** | 4.2/5 | ✅ ABOVE threshold | Xóa residual Boolean-TV3 wording ở Step 4; M reclassified; E8 reframed |
| **v2.2** | 4.3/5 | ✅ ABOVE threshold | Thêm scope boundary; Born-limit reframed; "cannot say" → "do not specify" |
| **v2.3** | **4.5/5** | ✅ ABOVE threshold — READY | §0.5 execution targets; K_joint wording; verification checklist |

### 9.2. Chi tiết các lỗi đã sửa

#### ❌ LỖI CRITICAL v1.0 — TV2 ≡ TV3 (Boolean)

```
Lỗi: TV2 (Anvaya: P→Q) và TV3 (Vyatireka: ¬Q→¬P) là LOGICALLY EQUIVALENT
      trong Boolean predicate logic → không thể là điều kiện độc lập.
      → Truth table có các hàng IMPOSSIBLE (TV2=true, TV3=false không tồn tại)

Sửa (v2.0): TV2 và TV3 là PROBABILISTIC predicates độc lập:
  TV2 = Sensitivity (sapakṣa set)
  TV3 = Specificity (vipakṣa set)
  → Sensitivity và specificity do các cơ chế vật lý KHÁC NHAU điều khiển
  → Độc lập thực sự
```

#### ❌ LỖI HIGH v1.0 — M undefined

```
Lỗi: M (registration mode) không được định nghĩa hình thức trước TV2.
Sửa (v2.0): M ∈ {active, inactive} — state của E6 process, KHÔNG phải
            thuộc tính của quantum state được đo.
```

#### ❌ LỖI MEDIUM v1.0/v2.0 — Quantum Eraser là TV3 example

```
Lỗi: Quantum eraser được dùng như ví dụ TV3 failure.
Sửa (v2.1): Quantum eraser thuộc E8 (Retroactive Override).
            E8 hoạt động RETROACTIVELY trên prior registration record.
            Đây là E8 action, KHÔNG phải TV3 failing trong initial registration.
```

#### ❌ LỖI MEDIUM v2.1 — Scope overclaim

```
Lỗi: E10 có thể bị đọc như "sửa" hoặc "thay thế" Standard QM.
Sửa (v2.2): VVV-QMRF scope boundary: "P1-P4 do not specify the VVV-QMRF
            registration-layer distinction" — không phải "P1-P4 cannot say".
```

---

## PHẦN X — VỊ TRÍ KIẾN TRÚC

### 10.1. E-Postulate Architecture

```
E10 được reference bởi: E3 (Registration Lock — condition D)
                         E7 (Validity Locus)
                         E12 (Beyond-Projection Registration / POVM)

E10 references:          E4 (Pre-Symbolic Layer)
                         E6 (Registering System as Process)
                         E9 (Null Registration Event)

E10 kết nối với:         E8 (Retroactive Override) qua timestamped TV records
                         E11 (Contrapositive Evidence) qua TV3 calibration
                         E13 (Temporal Discontinuity) qua E8 retroactive interface
```

### 10.2. Layer Architecture (Gap → Category → Framework)

```
gap/BIAN-14
  ↓ diagnoses missing registration structure
category/Category 09 — Tripartite Registration Validity Matrix / Strict Apparatus Axiom
  ↓ specifies detailed category and boundary conditions
framework/E10 — Tripartite Validity Postulate
  ↓ installs rule into VVV-QMRF postulate architecture
VVV-QMRF registration-state update layer
  ↓ applies category without replacing canonical QM physics

Document sizes:
  Category 09:     24.9 KB  (vvv_qmrf_category_09_e10_tripartite_registration_validity_matrix.md)
  Framework E10:   12.6 KB  (vvv_qmrf_framework_e10_tripartite_registration_validity_matrix_postulate.md)
  AHP Trace:        6.7 KB  (AHP_E10_Tripartite_Validity_Formalization_2026_05_29.md)
  Plan v2.3:       42.4 KB  (E10_Tripartite_Validity_Formalization_Plan.md)
```

### 10.3. Node IDs trong VVV-QMRF-EX

| Node | ID | Mô tả |
|---|---|---|
| Tripartite Registration Validity Matrix | N_QM_VVV_00042 | Root node của E10 trong EX graph |
| Validity Tensor 𝕍_tri | N_QM_VVV_00043 | Compact Trairūpya criteria set |
| Buddhist source Trairūpya | N_BE_00018 | BE SOT anchor |

---

## PHẦN XI — HẬU QUẢ KIỂM CHỨNG (Testable Consequences)

### 11.1. Consequence 1 — Dark Count Rate = TV3 Failure Rate

```
CLAIM:
  Hệ ghi nhận không thể phân biệt causally-produced detector responses (TV1=true)
  khỏi thermal noise (TV1=false) sẽ hệ thống gán r≠r_null cho spurious events.

PREDICTION (VVV-QMRF):
  Dark count rate = P(r ≠ r_null | TV1=false, M=active) = TV3 failure rate.
  Hai detector với quantum efficiency GIỐNG NHAU (same TV2 / ε_det) nhưng
  dark count suppression KHÁC NHAU sẽ có TV3 scores KHÁC NHAU.
  Cải thiện shielding → ε_fp ↓ (TV3 ↑) ĐỘCLẬP khỏi cải thiện η (TV2 ↑).

VỚI P1-P4: Standard QM không phân tách thành TV1/TV2/TV3 registration-layer roles.

EXPERIMENTAL ACCESS:
  SNSPD: cooling → dark count rate ↓ (ε_fp ↓, TV3 ↑)
  mà không tự động thay đổi detection efficiency (ε_det, TV2).
```

### 11.2. Consequence 2 — TV2/TV3 Engineering Independence

```
CLAIM:
  E10 dự đoán optimal detector design yêu cầu ĐỘCLẬP tối ưu hóa TV2
  (sensitivity ε_det ↓) và TV3 (specificity ε_fp ↓), governed by different
  physical mechanisms.

PREDICTION (VVV-QMRF):
  Detector optimization cải thiện TV2 (higher absorption → higher η)
  KHÔNG tự động cải thiện TV3 (dark count suppression cần thermal isolation engineering riêng).
  Hai điều kiện registration-layer RIÊNG BIỆT với engineering handles RIÊNG BIỆT.

EXPERIMENTAL ACCESS:
  So sánh 2 detectors:
  - Detector A: optimized for sensitivity (high η, high dark count)
  - Detector B: optimized for specificity (low dark count, lower η)
  E10 predicts: 2 điểm trên TV2-dominant vs TV3-dominant paths, KHÔNG phải
  2 điểm trên một single efficiency curve.
```

---

## PHẦN XII — NHỮNG GÌ E10 KHÔNG TUYÊN BỐ

| Claim | Trạng thái |
|---|---|
| E10 thay thế Standard QM P1-P4 | ❌ SAI — E10 là registration-layer supplement |
| E10 sửa một lỗi trong Standard QM | ❌ SAI — P1-P4 do not specify TV decomposition; không phải P1-P4 sai |
| TV=true là bằng chứng đầy đủ của K_joint validity | ❌ SAI — TV=true là local validity precondition cho K_joint work, không phải proof |
| Quantum eraser là ví dụ TV3 failure | ❌ SAI — Quantum eraser thuộc E8 (Retroactive Override) |
| Trairūpya là doctrine về apparatus vật lý | ❌ SAI — Trairūpya trong Dignāga evaluate *hetu* trong suy luận, KHÔNG phải apparatus |
| E10 là engineering guarantee mọi detector đều perfect | ❌ SAI — E10 là registration-layer category, không phải engineering specification |

---

## PHẦN XIII — TÓM TẮT QUICK REFERENCE

```
┌─────────────────────────────────────────────────────────────────────────┐
│              TV1 / TV2 / TV3 — QUICK REFERENCE                         │
├─────────────────┬───────────────────────────────────────────────────────┤
│ TV1             │ Boolean: d causally produced by R_sys, not noise      │
│ Buddhist mark   │ Pakṣadharmatva (Mark 1 — Property of Subject)         │
│ K-axioms        │ K1 (co-instantiation), K7 (closure)                  │
│ E-postulate     │ E4 (gate), E3-D (grounding)                          │
│ Failure         │ → r_null regardless of TV2/TV3                        │
├─────────────────┼───────────────────────────────────────────────────────┤
│ TV2             │ Probabilistic Sensitivity: P(r≠r_null|TV1=T,M=act)   │
│                 │ ≥ 1 − ε_det                                          │
│ Buddhist mark   │ Anvaya / Sapakṣasattva (Mark 2 — Positive Concom.)   │
│ Test set        │ sapakṣa = positive cases                              │
│ K-axioms        │ K2 (temporal injectivity), K4 (registration validity) │
│ E-postulate     │ E3-I (grounding), E3 condition (sensitivity dir.)     │
│ Failure         │ → missed detections exceed ε_det (low η)             │
├─────────────────┼───────────────────────────────────────────────────────┤
│ TV3             │ Probabilistic Specificity: P(r≠r_null|TV1=F OR M=in) │
│                 │ ≤ ε_fp                                               │
│ Buddhist mark   │ Vyatireka / Vipakṣāsattva (Mark 3 — Negative Conc.) │
│ Test set        │ vipakṣa = counter-cases (negative cases)              │
│ K-axioms        │ K3 (self-certification), K4 (registration validity)   │
│ E-postulate     │ E3-SC (grounding), E9 (calibration), E11 (bridge)    │
│ Failure         │ → spurious registrations exceed ε_fp (high dark cnt) │
├─────────────────┼───────────────────────────────────────────────────────┤
│ TV conjunction  │ TV = TV1 AND TV2 AND TV3                             │
│ K-axiom         │ K5 (local validity precondition for K_joint)          │
│ TV=TRUE         │ V̂(rho,d) = (r, rho_certified) — Valid registration   │
│ TV=FALSE        │ V̂(rho,d) = (r_null, rho_unchanged) — E9 null        │
│ Born-limit      │ ε_det→0, ε_fp→0 compatible with P3 (ideal context)   │
└─────────────────┴───────────────────────────────────────────────────────┘
```

---

## PHẦN XIV — CÁC FILE LIÊN QUAN

| File | Vai trò | Trạng thái |
|---|---|---|
| [`framework/vvv_qmrf_framework_e10_...postulate.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e10_tripartite_registration_validity_matrix_postulate.md) | Framework chính (§3a-d) | ✅ TV1/TV2/TV3 tích hợp đầy đủ |
| [`plan/E10_Tripartite_Validity_Formalization_Plan.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/plan/E10_Tripartite_Validity_Formalization_Plan.md) | Plan v2.3 (858 dòng) | ✅ READY TO EXECUTE — 4.5/5 |
| [`anti_hallucinations/AHP_E10_Tripartite_Validity_Formalization_2026_05_29.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/anti_hallucinations/AHP_E10_Tripartite_Validity_Formalization_2026_05_29.md) | AHP trace (9 components) | ✅ Composite 4.5/5 — PASS |
| [`category/vvv_qmrf_category_09_e10_tripartite_registration_validity_matrix.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/category/vvv_qmrf_category_09_e10_tripartite_registration_validity_matrix.md) | Category 09 (307 dòng) | ✅ Full RCA + Mermaid diagram |
| [`framework/vvv_qmrf_framework_e03_registration_lock_postulate.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e03_registration_lock_postulate.md) | E3 (được grounded bởi TV) | Reference |
| [`framework/vvv_qmrf_framework_e09_null_registering_system_event_postulate.md`](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/framework/vvv_qmrf_framework_e09_null_registering_system_event_postulate.md) | E9 (r_null — TV3 calibration) | Reference |

---

*Báo cáo lập bởi: Antigravity (Google DeepMind) — 2026-05-29T16:09:27+07:00*  
*Dữ liệu tổng hợp từ: Plan v2.3, Framework §3a-d, AHP trace, Category 09, EX graph*
