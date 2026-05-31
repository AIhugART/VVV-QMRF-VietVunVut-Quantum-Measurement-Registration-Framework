# Cơ chế Collapse Hàm Sóng và VVV-QMRF Scope

**Author:** VietVunVut (Viet — Nguyen Xuan)
**Framework:** VVV-QMRF (VietVunVut Quantum Measurement Registration Framework)
**Date:** 2026-05-31
**Source paper:** *Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?* (Draft v95)

---

## 1. Câu hỏi gốc: Cơ chế gây collapse hàm sóng khi đo là gì?

Đây là câu hỏi trung tâm của cơ học lượng tử kể từ thế kỷ 20. Trước khi đo, hệ lượng tử ở trạng thái **chồng chất** (superposition):

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

Sau khi đo, ta chỉ thấy **một** kết quả. Điều gì khiến $|\psi\rangle$ "sập" thành một trạng thái duy nhất?

### Các lý thuyết chính hiện có

| Lý thuyết | Cơ chế | Vấn đề còn lại |
|---|---|---|
| **Copenhagen** | Thiết bị đo cổ điển gây collapse | Không có cơ chế vật lý; ranh giới lượng tử/cổ điển ở đâu? |
| **Decoherence** (Zurek) | Hệ rò thông tin ra môi trường → off-diagonal terms → 0 | Không giải thích tại sao ta thấy *một* kết quả cụ thể |
| **Many-Worlds** (Everett) | Không có collapse — tất cả nhánh tồn tại | Không thể falsify; vấn đề Born rule |
| **Chuỗi von Neumann** | Collapse bị trì hoãn vô tận dọc chuỗi $S \to M_1 \to M_2 \to \cdots$ | Không có điểm dừng tự nhiên |

---

## 2. VVV-QMRF Scope: Phân tách 2 tầng

VVV-QMRF **không** đưa ra lý thuyết mới về cơ chế collapse vật lý. Thay vào đó, framework đề xuất phân tách Quantum Measurement thành **hai tầng độc lập**:

```
┌──────────────────────────────────────────────────────────────┐
│                    CÂU HỎI: Collapse là gì?                  │
└──────────────────────┬───────────────────────────────────────┘
                       │
          ┌────────────┴────────────┐
          ▼                        ▼
   P-layer (vật lý)         K-layer (registration)
          │                        │
   "Tại sao |ψ⟩ → |o⟩?"    "Sau khi |o⟩ đã xảy ra,
          │                  K-space ghi nhận như thế nào?"
          │                        │
   ❌ Ngoài scope VVV-QMRF   ✅ VVV-QMRF hoạt động ở đây
   (QM chuẩn không thay đổi)
```

### Tầng P-layer (Physical layer)

- Hilbert space $\mathcal{H}$, density matrix $\rho$, Born rule
- Decoherence, entanglement, unitary evolution
- **VVV-QMRF không sửa đổi và không tuyên bố giải thích phần này**

> *"This document does not modify Standard Quantum Mechanics, does not change any VVV-QMRF postulate (E1–E16), and does not claim K-space is a canonical QM object."*
> — K_Space_Axiomatization.md §0, Line 20

### Tầng K-layer (Registration layer)

- K-state tuple: $k = \langle M, o, \text{cert}, t, V \rangle \in K_R$
- Khi nào một outcome được "đăng ký" (cert = 1)?
- Registration event có hợp lệ không? (V = 1 hay V = 0?)
- Contradiction giữa hai registrations: $k_2 \perp k_1$?
- **Overlap geometry có ảnh hưởng đến thống kê đo lường không?**

---

## 3. Câu trả lời của VVV-QMRF ở tầng K-layer

> **Sau khi P-layer interaction đã xảy ra và outcome đã được đăng ký (cert = 1), cấu trúc geometric của registration — cụ thể là overlap $|\langle b|d\rangle|^2$ giữa basis đo của Superobserver và outcome đã ghi nhận của Friend — có thể để lại dấu vết thống kê đo được.**

### 3.1 Deformation class (Overlap-only)

Nếu K-layer có cấu trúc phụ thuộc overlap, xác suất đo bị biến dạng:

$$\boxed{P'(a,b \mid x,y) = \frac{P_{\rm QM}(a,b \mid x,y) \cdot g\!\left(|\langle b|d\rangle|^2\right)}{Z}}$$

trong đó:
- $b \in \{+1,-1\}$: outcome của Superobserver
- $d \in \{H,V\}$: outcome đã đăng ký của Friend
- $g: [0,1] \to \mathbb{R}$: **hàm bất kỳ** — theorem đúng với mọi $g$
- $Z$: chuẩn hóa

**Đại diện tối giản** (thỏa 3 ràng buộc vật lý: bất biến quay, căn chỉnh hoàn hảo, đơn điệu):

$$f_\perp(b,d) = 1 - |\langle b|d\rangle|^2$$

### 3.2 Equatorial Cancellation Theorem (Proposition 1)

Basis đo của Superobserver tại góc Bloch sphere $(\theta, \phi)$:

$$|b=+1\rangle = \cos(\theta/2)|H\rangle + e^{i\phi}\sin(\theta/2)|V\rangle$$
$$|b=-1\rangle = \sin(\theta/2)|H\rangle - e^{i\phi}\cos(\theta/2)|V\rangle$$

Squared overlaps ($\phi$ triệt tiêu vì $|e^{i\phi}|^2 = 1$):

$$|\langle b{=}+1|H\rangle|^2 = \cos^2(\theta/2), \qquad |\langle b{=}-1|H\rangle|^2 = \sin^2(\theta/2)$$

Sự khác biệt giữa hai nhánh — chính là **observable signal**:

$$\boxed{f_\perp(+1,H) - f_\perp(-1,H) = -\cos\theta}$$

**Triệt tiêu khi và chỉ khi $\theta = \pi/2$:**

$$\theta = \frac{\pi}{2} \implies \cos\theta = 0 \implies f_\perp = \frac{1}{2} = \text{const} \implies P' \equiv P_{\rm QM} \quad \forall g \quad \blacksquare$$

### 3.3 Observable và chữ ký thực nghiệm

Signal đo được — bất biến dưới mọi basis redefinition (Lemma 1):

$$\delta\langle AB\rangle_\theta = \langle AB\rangle_\theta - \langle AB\rangle_{\pi/2}$$

| Điều kiện | QM chuẩn | VVV-QMRF (nếu K-layer có cấu trúc) |
|---|---|---|
| $\theta = \pi/2$ | $\delta\langle AB\rangle = 0$ | $\delta\langle AB\rangle = 0$ (bắt buộc — Proposition 1) |
| $\theta \neq \pi/2$ | $\delta\langle AB\rangle = 0$ | $\delta\langle AB\rangle \approx 0.115\beta \neq 0$ |
| $\theta$-sweep đầy đủ | $\delta = 0 \ \forall\theta$ | $\delta = 0$ iff $\theta = \pi/2$ |

### 3.4 Root Cause: Tại sao mọi thí nghiệm EWF đều bỏ qua điều này?

**Phát hiện gốc:** Cả hai thí nghiệm EWF đã được công bố (Proietti 2019, Bong 2020) đều đo tại $\theta = \pi/2$ — không phải vì thiết kế, mà vì **convention tối ưu hóa LF violation**.

```
Tại θ = π/2:  |⟨b|H⟩|² = |⟨b|V⟩|² = 1/2  (cho cả b = ±1)
→ g(1/2) = const → P' ≡ P_QM → δ⟨AB⟩ ≡ 0
```

Đây là **điểm mù hình học** (geometric blind spot) — mọi deformation phụ thuộc overlap đều **triệt tiêu hoàn toàn** tại xích đạo Bloch sphere.

---

## 4. Ngưỡng phát hiện thực nghiệm

Tại $\theta = 31°$, $N = 91{,}000$ coincidences, $\mu = 0.95$:

| $\beta$ | $|\delta\langle AB\rangle|$ | $n_\sigma$ (1 setting) | $n_\sigma$ (4 kết hợp) |
|---|---|---|---|
| $0.05$ | $0.0057$ | $3.3\sigma$ | $6.7\sigma$ |
| **0.07** | **0.0080** | **4.7σ** | **9.4σ** |
| $0.10$ | $0.0115$ | $6.7\sigma$ | $13.5\sigma$ |
| $0.30$ | $0.0355$ | $20.8\sigma$ | $41.6\sigma$ |

**Ngưỡng $5\sigma$:** $\beta_{\min} \approx 0.038$ (4 settings kết hợp).
**Một quarter-wave plate** tái-chèn vào apparatus Bong (2020) → $\theta = 31°$ → phá vỡ điểm mù.

---

## 5. Bảng phân tách scope

| Câu hỏi | Layer | VVV-QMRF scope? |
|---|---|---|
| Tại sao $\|\psi\rangle \to \|o\rangle$ khi đo? | P-layer | ❌ Ngoài scope |
| Decoherence xảy ra nhanh bao nhiêu? | P-layer | ❌ Ngoài scope |
| GRW/CSL collapse parameter $\lambda$? | P-layer | ❌ Ngoài scope |
| Khi Friend đo xong, Superobserver có thống kê khác không? | P/K boundary | ✅ Câu hỏi VVV-QMRF |
| $\delta\langle AB\rangle(\theta) \neq 0$ tại $\theta \neq \pi/2$? | K → P signal | ✅ Trong scope |
| $P'(a,b\|x,y) = P_{\rm QM} \cdot g(\|\langle b\|d\rangle\|^2)/Z$? | K-layer deformation | ✅ Trong scope |
| Registration event: cert=1, V=1? | K-layer | ✅ Trong scope |

---

## 6. Câu trả lời cô đọng nhất

**VVV-QMRF không giải thích *tại sao* collapse xảy ra ở P-layer.**

VVV-QMRF hỏi và kiểm tra:

> *"Nếu K-layer có cấu trúc registration phụ thuộc overlap, liệu $\delta\langle AB\rangle(\theta) = 0$ iff $\theta = \pi/2$? — một dự đoán mà tất cả thí nghiệm EWF hiện có, do convention cố định $\theta = \pi/2$, về mặt cấu trúc không thể kiểm tra."*

**Null test:** $\beta \sim 0.07$ tại $5\sigma$, $\theta = 31°$, một waveplate, apparatus Bong (2020).

---

## 7. Luồng logic hoàn chỉnh

```
P-layer collapse xảy ra (QM chuẩn, không thay đổi)
         │
         ▼
Outcome lan đến K-layer → registration event (cert=1, V=1)
         │
         ▼  ← VVV-QMRF bắt đầu từ đây
K-layer: registration geometry có phụ thuộc vào θ không?
         │
    ┌────┴────┐
    ▼         ▼
  β = 0     β ≠ 0
    │         │
  QM chuẩn  P'(a,b|x,y) ≠ P_QM
  đúng hoàn  δ⟨AB⟩(θ) ≠ 0 tại θ ≠ π/2
  toàn       δ⟨AB⟩(π/2) = 0 (luôn luôn)
                   │
                   ▼
             Kiểm tra: θ = 31°, 1 QWP
             Falsify class nếu δ = 0 ∀θ
             Discover nếu δ ≠ 0 tại θ ≠ π/2
```

---

*Tài liệu này được tổng hợp từ VVV-QMRF Working Paper v95 và K_Space_Axiomatization.md v2.5.*
*Xem paper đầy đủ: `papers/paper_002/arxiv/blind_equator_ArxivR/main.tex`*
*Xem axiom hóa K-space: `documents/research_documents/meta_architecture/K_Space_Axiomatization.md`*
