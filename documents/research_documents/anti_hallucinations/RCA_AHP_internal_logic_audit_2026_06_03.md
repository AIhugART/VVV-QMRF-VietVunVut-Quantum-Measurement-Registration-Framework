Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — AHP Internal-Logic Audit (Self-Audit of the Anti-Hallucination Pipeline)

**Date:** 2026-06-03 UTC+7
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5 (CLAUDE.md Rule Zero)
**Scope:** VVV-QMRF — folder `documents/research_documents/anti_hallucinations/` (AHP itself)
**Compass:** VVV-QMRF-EX (intelligence only, no structure import)
**Status:** FINDINGS + PROPOSALS — **propose only, no core-file edits applied**
**Constraint:** This report documents internal-logic issues of the AHP and proposes fixes. It does **not** modify `00_top_10`, `01`–`06`, `index.md`, or `label_system.md`.

> **Purpose:** Áp dụng chính pipeline chống-ảo-giác (AHP) lên CHÍNH NÓ — kiểm tra logic nội tại của folder `anti_hallucinations`. Đây là bước "self-audit" mà workflow hiện tại chưa có (xem F5).

---

## 1. Define — Triệu chứng trung tâm (tách symptom / cause)

Folder chứa **27 file** (CLAUDE.md chỉ mô tả 8 file pipeline lõi). Đối chiếu version giữa các file:

| File | Version khai báo | Ngày | Vai trò |
|------|------------------|------|---------|
| `00_top_10_hallucinations_record.md` | **v2.3** | 2026-06-01 | Record lõi (đang "sống") |
| `index.md` | **v1.6** | 2026-05-24 | Điều hướng / File Map |
| `label_system.md` | **v1.0** | 2026-05-24 | Registry + Dashboard |
| `01`–`06_*.md` | **v1.0** | 2026-05-24 | Pipeline layers |
| `AHP_Gate1_Phase1_Audit_2026_06_01.md` | (mới) | 2026-06-01 | Output audit gate |
| `AHP_E04/E06/E13/E15/E16_*` | (mới) | 2026-05-29/31 | Output postulate plans |

- **Symptom:** file điều hướng/quản trị (`index`, `label_system`) đứng ở v1.0–v1.6, trong khi record lõi đã v2.3.
- **Cause (giả thuyết, sẽ cô lập ở §3–§4):** thiếu cơ chế đồng bộ (sync gate) buộc file phái sinh cập nhật theo `00`.

---

## 2. Findings — đã Trace + Isolate

Mỗi finding gắn signal-ID của chính AHP (`01_early_warning.md`) để chứng minh pipeline đang vi phạm luật của chính nó.

### 🟠 F1 — Version drift: file điều hướng vs file record — Signal **Y4**
- **Symptom:** `index.md` v1.6 mô tả "9-file pipeline" + "Top 10 v1.3 Dual-Table"; record thực đã qua v2.0 → v2.1 → v2.2 (Node Relevant columns) → v2.3 (Gate 1).
- **Trace:** `index.md` §6 Version History dừng ở v1.6 (2026-05-24); `00` Changelog có v2.0–v2.3 (2026-06-01).
- **Isolate:** không có bước cập nhật `index`/`label_system` khi `00` đổi version.

### 🟠 F2 — File Map trỏ sai vị trí 3 file ngoài-folder — Signal **O2 (broken trace / source gap)**
- **Symptom:** `index.md` File Map (L94–100) liệt kê chung bảng với 00–06:
  - `RCA_P10_NOISE_methodology_decision_2026_05_24.md`
  - `noise_sensitivity_analysis_spec.md`
  - `noise_sensitivity_analysis.py`
- **Trace (đã xác minh bằng `find` toàn repo):** 3 file này thực nằm tại
  - `project_vvv_qmrf_class_c/04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md`
  - `project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis_spec.md`
  - `project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis.py`
- **Isolate:** File Map không path-qualify → người đọc tìm trong folder `anti_hallucinations` sẽ không thấy (reference gãy về định vị). Đúng loại lỗi O2 mà AHP định nghĩa để bắt.

### 🟡 F3 — File Map bỏ sót ~11 file thực có trong folder — navigation gap
- **Symptom:** Các file sau KHÔNG xuất hiện trong `index.md` File Map:
  `AHP_E04`, `AHP_E06`, `AHP_E13`, `AHP_E15`, `AHP_E16`, `AHP_Gate1_Phase1_Audit`, `RCA_FINAL_VERDICT`, `RCA_K9E_PAT_status_report`, `RCA_phi_map_detailed_status`, `RCA_session_top10_v1_1`, `RCA_session_top10_v1_2`, `RCA_why_A_E3_is_top1`.
- **Isolate:** 5 file kế hoạch postulate `AHP_E*` và bản audit Gate 1 — output thật của pipeline — đang **orphaned khỏi navigation**.

### 🟡 F4 — Registry + Dashboard của `label_system.md` đóng băng ở v1.0 — Signal **O5 (stale reference)**
- **Symptom:** §4 "Component Label Registry (2026-05-24)" và §4.2 vẫn ghi "Top 10 **v1.3**"; §5 Dashboard đếm `[AH-OK]=9, [AH-LOW]=10...` theo trạng thái cũ.
- **Isolate:** không phản ánh v2.3 — cột Node Relevant, nội dung mới I.1/III.1, status note phi-map/T4-H.

### 🔴 F5 — Meta-inconsistency: pipeline không tự áp dụng luật của chính nó — **ROOT CAUSE**
- **Symptom:** AHP định nghĩa O2 (broken trace), Y3 (inconsistent terminology), Y4 (version metadata) để bắt lỗi cho phần còn lại của VVV-QMRF; nhưng chính folder AHP đang vi phạm O2 (F2) và Y4 (F1, F4), thêm navigation gap (F3).
- **Isolate:** không tồn tại bước "self-audit / sync-check cho chính folder AHP" trong workflow. `00` được audit kỹ; `index`/`label_system` thì không ai audit. Đây cùng đúng lớp lỗi **PEER-SYNC DRIFT** (D1) mà dự án từng gặp với `K_Space_Axiomatization.md` (đã có rule riêng), nhưng chưa có rule tương đương cho folder AHP.

### 🟡 F6 — Integration Map chưa path-qualify reference — biến thể của F2
- **Symptom:** `index.md` Integration Map (L122–137) tham chiếu `rca_k9e_origin_investigation.md`, `rca_technical_debt_inventory_2026_05_24.md` không kèm đường dẫn.
- **Trace:** cả hai tồn tại tại `project_vvv_qmrf_class_c/04_governance/` (không nằm trong folder AHP). Đây là nguồn calibration load-bearing cho `03`/`04`/`05`, nên cần path-qualify để truy vết được.

---

## 3. 5-Why → Root Cause

```
Triệu chứng: index v1.6 / label_system v1.0 trong khi record đã v2.3, và index có reference gãy.
  W1: Vì sao index/label_system lệch version?
      → Khi audit 00 (v2.0→v2.3), chỉ cập nhật 00, không đụng index/label_system.
  W2: Vì sao chỉ cập nhật 00?
      → Workflow định nghĩa "re-audit Top 10", không định nghĩa "re-sync navigation/label".
  W3: Vì sao workflow không có bước đó?
      → AHP coi 01–06 + label_system + index là "thiết kế tĩnh" (design-frozen v1.0), chỉ 00 là "sống".
  W4: Vì sao giả định đó sai?
      → Vì index/label_system CHỨA dữ liệu phái sinh từ 00 (File Map, Registry, Dashboard) → chúng KHÔNG tĩnh.
  W5: Đây có phải "bịa đặt" (fabrication) không?
      → KHÔNG. Đây là drift do thiếu sync-rule; cùng lớp lỗi PEER-SYNC DRIFT (D1) đã từng xảy ra với K_Space_Axiomatization.

Root Cause (1 câu):
AHP thiếu một "self-audit / sync gate" buộc index.md và label_system.md đồng bộ với 00_top_10
mỗi khi 00 đổi version — y hệt lớp lỗi PEER-SYNC mà dự án đã có rule cho K_Space nhưng chưa có
cho chính folder anti_hallucinations.
```

**Root cause type (theo `04_analysis.md` taxonomy):** Type 5 — Structural Gap (thiếu machinery sync), biểu hiện ra dưới dạng Type 3-like broken trace (F2) và stale metadata (F1/F4).

---

## 4. 3-Round Scoring (ngưỡng 4/5)

| Round | Trọng tâm | Điểm | Findings |
|-------|-----------|------|----------|
| R1 | Phát hiện có thật & trace được? | 5/5 | F1–F6 verify bằng đọc file + `find` toàn repo. 3 file ở folder khác đã xác nhận tồn tại. |
| R2 | Cô lập đúng root cause (không vá triệu chứng)? | 4.5/5 | Root = thiếu sync gate (F5); F1–F4 là hệ quả; F6 là biến thể của F2. |
| R3 | Đề xuất sửa đúng gốc + an toàn (extend, not overwrite)? | 4.5/5 | Thêm sync-rule + cập nhật metadata; không xóa nội dung lịch sử. |
| **Aggregate** | | **4.67/5 PASS (≥ 4/5)** | |

---

## 5. Proposed Fixes (PROPOSE ONLY — chưa thực thi)

Phân loại theo Priority Matrix của `06_solution.md`. **Tất cả đề xuất tuân thủ "extend, not overwrite": chỉ thêm/chú thích/đồng bộ metadata, giữ nguyên nội dung & bảng RCA lịch sử.**

| # | Finding | Priority | Solution Type | Đề xuất |
|---|---------|----------|---------------|---------|
| 1 | F5 (root) | **P1** | DOCUMENT + Prevention | Thêm vào CLAUDE.md một rule **"AHP-SYNC"** song song với "PEER-SYNC K_Space": mỗi khi `00_top_10` đổi version, BẮT BUỘC sync `index.md` (File Map + Version History) và `label_system.md` (Registry §4 + Dashboard §5); verify bằng bước self-audit. |
| 2 | F2 | **P1** | ANCHOR | Trong `index.md` File Map, tách 3 file ngoài-folder thành mục riêng ghi rõ đường dẫn `../project_vvv_qmrf_class_c/...`. Không xóa dòng — chỉ chú thích đúng vị trí. |
| 3 | F1 + F3 | **P2** | DOCUMENT | Cập nhật `index.md` lên v2.x: bổ sung ~11 file đang thiếu vào File Map (đặc biệt nhóm `AHP_E*` và `Gate1`); thêm Version History v1.6 → v2.3; vẽ lại sơ đồ nếu luồng gate thay đổi. |
| 4 | F4 | **P2** | DOCUMENT | Cập nhật `label_system.md` Registry §4 + Dashboard §5 về v2.3 (Node Relevant, status note phi-map/T4-H, I.1/III.1); sửa "Top 10 v1.3" → "v2.3". |
| 5 | F6 | **P3** | ANCHOR | Path-qualify các reference trong Integration Map (L122–137) của `index.md`. |

---

## 6. Resolution Tracking

| # | Issue | Component | Severity | Root Cause Type | Solution Type | Status | Open Date | Resolve Date |
|---|-------|-----------|----------|-----------------|---------------|--------|-----------|--------------|
| 1 | Thiếu AHP-SYNC self-audit gate | workflow | 🔴 ROOT | Type 5 | DOCUMENT+Prevention | **OPEN** | 2026-06-03 | — |
| 2 | File Map trỏ sai vị trí 3 file | index.md L94–100 | 🟠 | Type 3-like | ANCHOR | **OPEN** | 2026-06-03 | — |
| 3 | index version drift v1.6 vs v2.3 | index.md | 🟠 | Type 5 | DOCUMENT | **OPEN** | 2026-06-03 | — |
| 4 | File Map bỏ sót ~11 file | index.md | 🟡 | navigation gap | DOCUMENT | **OPEN** | 2026-06-03 | — |
| 5 | Registry/Dashboard stale | label_system.md §4–5 | 🟡 | Type 5 | DOCUMENT | **OPEN** | 2026-06-03 | — |
| 6 | Integration Map chưa path-qualify | index.md L122–137 | 🟡 | Type 3-like | ANCHOR | **OPEN** | 2026-06-03 | — |

---

## 7. Lưu ý meta

> Bản thân file báo cáo này, nếu không được đăng ký vào `index.md` File Map, sẽ **tái lập đúng F3**. Việc đăng ký nó là một phần của fix #4 (P2) — **đang chờ duyệt**, chưa thực hiện trong phiên này để giữ ràng buộc "propose only, no core-file edits".

---

*AHP Internal-Logic Audit — 2026-06-03. 3-Round RCA 4.67/5 PASS (≥ 4/5). 6 findings, root = missing AHP-SYNC self-audit gate. Propose only; 0 core-file edits applied.*
