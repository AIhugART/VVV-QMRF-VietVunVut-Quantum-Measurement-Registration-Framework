# E14 — Epistemic Absence Cognition Postulate / Tiên đề Nhận thức Vắng mặt

**Framework:** VietVunVut Epistemic Quantum Measurement (VVV-EQM)  
**Author:** VietVunVut (Viet - Nguyen Xuan)  
**GitHub:** https://github.com/AIhugART/  
**Date:** 2026-05-12  
**Status:** Proposal — Epistemic class D  
**Lineage:** gap/ (BIAN-9) → category/ (Category 13) → framework/ (E14)

---

## 1. Postulate Statement

**English:**
> The null result of a quantum measurement — when the measurement setup satisfies E10's Trairūpya conditions — constitutes a distinct, formally valid epistemic act: the positive cognition of the *absence* of the measured property. This act (Epistemic Absence Cognition, EAC) is epistemically equivalent in authority to a positive detection event. It is categorically distinct from measurement failure (E8 domain) and from the Null Observer Event (E9 domain).

**Vietnamese:**
> Kết quả rỗng của phép đo lượng tử — khi thiết lập đo thỏa điều kiện Trairūpya của E10 — tạo thành một hành vi nhận thức riêng biệt, chính thức hợp lệ: nhận thức dương tính về *sự vắng mặt* của thuộc tính đo. Hành vi này (EAC) có thẩm quyền nhận thức tương đương với sự kiện phát hiện dương tính. Khác biệt hoàn toàn với lỗi đo (E8) và Sự kiện Quan sát viên Rỗng (E9).

---

## 2. Prose Statement

QM handles null results implicitly: they appear as residual probability (1 − Σ P(λᵢ)). There is no formal category treating "no detection" as a first-class epistemic act. *Anupalabdhi* (Non-perception) in Buddhist Epistemology establishes this: under the right conditions, NOT perceiving an object that WOULD be perceived if present is a valid means of knowledge (*pramāṇa*) establishing absence.

E14 maps this directly. When E10's three conditions hold (the detector is properly coupled, calibrated, and dark-count-free), a null result is not a failure — it is a positive cognition of the property's absence. The Absence Projector $\hat{\Pi}_{absent}$ yields a definite post-measurement state that encodes positive knowledge.

Key distinction from E9 and E11:
- **E9**: Physical interaction occurred, no epistemic output (decoherence escape — NOT knowledge)
- **E11**: No physical interaction, positive knowledge via contrapositive (IFSI — interaction-free)
- **E14**: Physical interaction offered, null result = positive knowledge of *absence* (Anupalabdhi)

---

## 3. Formal Sketch

```
Absence Projector: Π̂_absent = Î − Σᵢ |λᵢ⟩⟨λᵢ|

Null measurement event (under E10 conditions):
  Pre-state:   |ψ⟩ (arbitrary superposition)
  Null click:  Π̂_absent triggers
  Post-state:  ρ → Π̂_absent ρ Π̂_absent / Tr(Π̂_absent ρ)

Epistemic content:
  "System does NOT have any property in {λ₁, λ₂, ...λₙ}"
  This IS positive knowledge — not "we don't know"

Anupalabdhi conditions check:
  1. Object perceivable IF present:  E10 C2 (Sapakṣasattva) ✅
  2. Object not perceived:           null click ✅
  3. Therefore absent:               valid cognition ✅
```

---

## 4. Three-way Distinction (E8 / E9 / E14)

| Scenario | Physical interaction | Epistemic output | Domain |
|----------|:-------------------:|:----------------:|--------|
| Bhrānti (false positive) | NO | YES (error) | E8 override |
| NOE | YES | NONE (decoherence) | E9 |
| IFSI | NO | YES (contrapositive) | E11 |
| **EAC (null = absence)** | **YES** | **YES (absence)** | **E14** |
| Standard PVM | YES | YES (presence) | PVM |

---

## 5. Architectural Position

```
E10 (Validity gate) — conditions for valid measurement
E9  (NOE) — interaction without epistemic output
E11 (IFSI) — no interaction, positive output via contrapositive
 └→ E14 (EAC) ← THIS POSTULATE
       E14: interaction + null output → positive absence knowledge
```

| Layer | Document | Role |
|-------|----------|------|
| Gap | BIAN-9 (SOT L38, N_BE_00253) | Diagnosis |
| Category | vvv_qmrf_category_13_e14_validated_absence_registration.md (Category 13) | Prescription |
| Framework | **This document (E14)** | Architecture |

---

## 6. Assertion Level

| Component | Class |
|---|---|
| "Anupalabdhi is valid pramāṇa" | **M** (Buddhist logic) |
| "Null result under E10 = positive absence knowledge" | **D** |
| "Π̂_absent operator definition" | **D** |
| "EAC ≠ NOE ≠ IFSI" | **M** (structural analysis) |

---

*Source: category/vvv_qmrf_category_13_e14_validated_absence_registration.md, framework/E10_tripartite_validity_postulate.md, framework/E9_null_observer_postulate.md, BIAN_index_SOT.md*
