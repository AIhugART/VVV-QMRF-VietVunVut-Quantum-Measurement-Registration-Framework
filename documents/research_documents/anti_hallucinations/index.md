Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Anti-Hallucination System â€” VVV-QMRF

**System name:** VVV-QMRF Anti-Hallucination Pipeline (AHP)
**Version:** v1.4 (2026-05-24)
**Scope:** VVV-QMRF (toan bo cac layer: K1-K8 axioms, T1-T8 bridge theorems, K9_E postulate, E1-E16 postulates, BE-QM mapping, Class C/D data analysis)
**Compass:** VVV-QMRF-EX (intelligence only, no structure import)
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Status:** ACTIVE

> **Purpose:** Phat hien, phan tich, cham diem, va loai bo hallucination trong toan bo du an VVV-QMRF. He thong nay la cong cu van hanh (operational tool) cua CLAUDE.md Rule Zero â€” no chuan hoa RCA process thanh pipeline co the audit duoc.

---

## 1. Pipeline Overview

```
                      +-----------------------------------+
                      | 00_top_10_hallucinations_record   |  <- Uu tien cao nhat
                      | Top 10 nguy co hallucination      |     Re-audit moi tuan
                      | Risk Score = H x W x (1+A)        |     CRITICAL/HIGH/MEDIUM/LOW
                      +-----------------------------------+
                                        |
                                        v (lam moi khi co component moi)
Claim / Component / Term moi            |
        |                               |
        v                               v
+-------------------------------+  (doi chieu voi Top 10)
| 01_early_warning.md           |  <- Canh bao som
| Quet symptom patterns         |     Co khop signal RED/ORANGE/YELLOW?
| 15 signals, 3 muc severity    |     YES -> trigger pipeline
+--------------+----------------+
               | TRIGGER
               v
+-------------------------------+
| 02_detection.md               |  <- Phat hien
| Component inventory + tracing |     Lap bang dieu tra thanh phan
| 4 nhom nguon goc              |     Classify: std QM / pre-Class C / new-flagged / orphaned
+--------------+----------------+
               |
               v
+-------------------------------+
| 03_sot_traceability.md        |  <- Truy vet SOT
| Cross-reference matrix        |     Tra cuu: component nay duoc SOT nao anchor?
| 6 SOT sources, trace score    |     Trace score = so SOT anchor / tong SOT lien quan
+--------------+----------------+
               |
               v
+-------------------------------+
| 04_analysis.md                |  <- Phan tich RCA
| 5-Whys + root cause taxonomy  |     W1->W5: truy nguoc den root cause
| 6 loai root cause             |     Isolate: diem bat dau cua failure
+--------------+----------------+
               |
               v
+-------------------------------+
| 05_scoring.md                 |  <- Cham diem
| Rubric 0-10 (5 band)          |     Moi component -> score 0-10
| Aggregate formula             |     TB toan he thong, phan phoi %
+--------------+----------------+
               |
               v
+-------------------------------+
| label_system.md               |  <- Dan nhan canh bao
| 5 primary + 9 secondary       |     [AH-OK] [AH-LOW] [AH-WARN] [AH-HIGH] [AH-CRIT]
| + 4 risk score labels         |     [RS-CRIT] [RS-HIGH] [RS-MED] [RS-LOW]
| Decision tree + registry      |
+--------------+----------------+
               |
               v
+-------------------------------+
| 06_solution.md                |  <- Giai phap
| Priority matrix P0-P4         |     P0 (BLOCKING, 9-10) -> fix ngay
| 5 solution types              |     P4 (ONGOING, 0-2) -> duy tri practice
| Resolution tracking           |     Track den RESOLVED
+-------------------------------+
```

---

## 2. File Map

| File | Role | Khi nao dung | Input | Output |
|------|------|-------------|-------|--------|
| `00_top_10_hallucinations_record.md` | Danh sach uu tien cao nhat | Moi tuan (re-audit) + khi co component moi | Toan bo VVV-QMRF components | Top 10 risk ranking (Risk Score) |
| `01_early_warning.md` | Canh bao som | Moi khi co claim/term moi, hoac review dinh ky | Claim text, component description | Signal match (Y/N) + severity |
| `02_detection.md` | Phat hien & truy vet | Khi co trigger tu early warning | Component list | Inventory table + phan loai nguon goc |
| `03_sot_traceability.md` | Truy vet SOT | Sau khi inventory (tra cuu anchor) | Component ID | Trace score + SOT links |
| `04_analysis.md` | Phan tich RCA | Khi component co dau hieu dang ngo | Component + trace score | Root cause (1 cau) + verdict |
| `05_scoring.md` | Cham diem | Moi component moi hoac khi SOT thay doi | Component + RCA result | Hallucination score 0-10 |
| `label_system.md` | Co che dan nhan canh bao | Sau khi cham diem + xac dinh Risk Score | H score + Risk Score + Trace + Anchor | Label chinh + label phu + label registry |
| `06_solution.md` | Giai phap | Khi co score >= 5 | Score + root cause | Solution type + priority + action |

---

## 3. Quick Reference â€” "Toi thay mot claim la, bat dau tu dau?"

| Tinh huong | Bat dau tu |
|------------|-----------|
| "Top 10 nguy co cao nhat hien tai la gi?" | `00_top_10_hallucinations_record.md` -> xem ranking |
| "Claim nay co ve khong co can cu" | `01_early_warning.md` -> tra signal registry |
| "Toi muon kiem tra toan bo 1 file/document" | `02_detection.md` -> component inventory |
| "Component nay duoc anchor boi cai gi?" | `03_sot_traceability.md` -> cross-reference matrix |
| "Tai sao claim nay sai?" | `04_analysis.md` -> 5-Whys template |
| "Claim nay dang bao nhieu diem hallucination?" | `05_scoring.md` -> rubric |
| "Label [AH-WARN] [AH-WEAK] nghia la gi?" | `label_system.md` -> label taxonomy |
| "Component nay nen gan nhan gi?" | `label_system.md` -> decision tree |
| "Lam sao de sua?" | `06_solution.md` -> priority matrix |

---

## 4. Integration Map

```
CLAUDE.md (Rule Zero)
  +-- RCA 5-step process (Define -> Trace -> Isolate -> Fix -> Verify)
       +-- Anti-Hallucination Pipeline (he thong nay)
            +-- 00_top_10_record  <- rca_k9e_origin_investigation.md section 3
            |                      + rca_technical_debt_inventory_2026_05_24.md
            |                      + EX compass (K-PENDING-RCA flags)
            +-- 01_early_warning  <- CLAUDE.md Warnings section
            +-- 02_detection      <- rca_k9e_origin_investigation.md section 2
            +-- 03_sot_traceability <- SYSTEM_Buddhist_Epistemology/system_be_full.md
            |                        + meta_architecture/K_Space_Axiomatization.md
            +-- 04_analysis       <- CLAUDE.md Rule Zero steps 1-3
            +-- 05_scoring        <- rca_k9e_origin_investigation.md section 3
            +-- label_system      <- 05_scoring.md + 00_top_10_hallucinations_record.md
            +-- 06_solution       <- rca_k9e_origin_investigation.md section 8-9
```

---

## 5. Design Principles (3-Round RCA Verified)

| Principle | Rationale | RCA Round |
|-----------|-----------|-----------|
| **Extend, not overwrite** | Ke thua CLAUDE.md Rule Zero, khong thay the | R1: 5/5 |
| **SOT-first** | Moi claim phai trace duoc ve it nhat 1 SOT | R1: 5/5 |
| **Score before solve** | Cham diem truoc khi de xuat giai phap â€” tranh over-engineering | R2: 4.5/5 |
| **Proportionality** | Component don gian -> detection + scoring; phuc tap -> full pipeline | R2: 5/5 |
| **Track resolution** | Moi issue phai duoc track den RESOLVED, khong bo sot | R3: 5/5 |
| **Compass, not cargo** | VVV-QMRF-EX dung de guide prioritization, khong import structure | R3: 4.5/5 |

---

## 6. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-05-24 | Initial release â€” 9-file pipeline, 3-round RCA verified |

---

*Anti-Hallucination Pipeline v1.0 â€” VVV-QMRF scope, VVV-QMRF-EX as compass. 3-Round RCA aggregate: 4.83/5 PASS (>= 4/5).*
