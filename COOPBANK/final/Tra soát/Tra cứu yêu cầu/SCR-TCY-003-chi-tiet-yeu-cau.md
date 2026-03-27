# SCR-TCY-003 — Chi tiết yêu cầu tra soát › Chi tiết

**Product:** Co-opBank Mobile Banking  
**Section:** Tra soát khiếu nại › Tra cứu yêu cầu  
**Screen Type:** Chi tiết  
**Figma Node:** `142:29471` (Đã tiếp nhận), `142:29490` (Đã xử lý)  

---

## 1. Overview

Màn hình chi tiết một yêu cầu tra soát cụ thể. Gồm 2 section:
1. **Thông tin giao dịch**: thời gian, mã giao dịch, tài khoản nguồn, link "Chi tiết giao dịch"
2. **Thông tin tra soát**: lý do, nội dung, trạng thái (badge), kết quả

2 variants theo trạng thái: "Đã tiếp nhận" (kết quả rỗng "— —") và "Đã xử lý" (có nội dung kết quả).

**Artboards:**
- `tra-cuu-yeu-cau-4.png` — Variant: Trạng thái "Đã tiếp nhận", Kết quả "— —"
- `tra-cuu-yeu-cau-5.png` — Variant: Trạng thái "Đã xử lý", Kết quả "Đã kiểm tra và xử lý"

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** xem chi tiết một yêu cầu tra soát,  
> **Để** biết thông tin đầy đủ về giao dịch liên quan và kết quả xử lý.

**Acceptance Criteria:**
- [ ] Hiển thị đầy đủ thông tin giao dịch: thời gian, mã GD, TK nguồn
- [ ] Link "Chi tiết giao dịch" dẫn sang màn hình giao dịch gốc
- [ ] Trạng thái tra soát hiển thị badge màu sắc tương ứng
- [ ] Kết quả hiển thị "— —" khi chưa có, hoặc nội dung thực khi đã xử lý

---

## 3. Content & Text Nodes

| Element | Label | Role |
|---------|-------|------|
| Header title | Chi tiết yêu cầu tra soát | page_title |
| Section label | Thông tin giao dịch | section_label |
| Field label | Thời gian giao dịch | detail_label |
| Field value | 20/02/2025 18:00 | datetime_value |
| Field label | Mã giao dịch | detail_label |
| Field value | 12312329 | transaction_id |
| Field label | Tài khoản nguồn | detail_label |
| Field value | 1212390002122 | account_number |
| Link | Chi tiết giao dịch → | navigation_link |
| Section label | Thông tin tra soát | section_label |
| Field label | Lý do tra soát | detail_label |
| Field value | Chưa nhận được tiền | dispute_reason |
| Field label | Nội dung tra soát | detail_label |
| Field value | ab123 | dispute_note |
| Field label | Trạng thái tra soát | status_label |
| Status badge | Đã tiếp nhận | status_received |
| Status badge | Đã xử lý | status_resolved |
| Field label | Kết quả | result_label |
| Field value | — — | result_empty |
| Field value | Đã kiểm tra và xử lý | result_value |

---

## 4. Functional Requirements

| # | Requirement | Priority |
|---|-------------|----------|
| F1 | Section "Thông tin giao dịch" với 3 fields + link | Must |
| F2 | Link "Chi tiết giao dịch" navigate sang transaction detail | Must |
| F3 | Section "Thông tin tra soát" với lý do, nội dung, trạng thái, kết quả | Must |
| F4 | Status badge — variant theo trạng thái | Must |
| F5 | Kết quả field — "— —" khi pending, text khi completed | Must |
| F6 | Account number masking nếu cần (PII) | Should |

---

## 5. Non-Functional Requirements

- Account number (1212390002122) cần xét masking (****0122)
- Long text truncation cho "Nội dung tra soát"
- Deep link: có thể navigate trực tiếp vào chi tiết từ notification

---

## 6. UX Signal Inference (Phase 4e)

**Signals detected từ text-signals-banking.json:**

| Signal | Text | Category | Implication |
|--------|------|----------|-------------|
| transaction-detail | "Thời gian giao dịch", "Mã giao dịch", "Tài khoản nguồn" | data-display | Financial detail — PII consideration |
| navigation-link | "Chi tiết giao dịch" | navigation | Cross-screen link to transaction |
| status-badge | "Đã tiếp nhận", "Đã xử lý" | status | Conditional badge display |
| empty-result | "— —" | feedback | Pending state indicator |
| dispute-result | "Đã kiểm tra và xử lý" | feedback | Resolution message |
| pii-sensitive | "1212390002122" | security | Account number — consider masking |

**DDL UX Law matches:**
- **Information Scent:** Link "Chi tiết giao dịch" phải rõ ràng là clickable
- **Consistency:** Status badge phải dùng cùng màu với màn hình danh sách
- **Aesthetic-Usability Effect:** 2 sections cần visual separation rõ ràng
