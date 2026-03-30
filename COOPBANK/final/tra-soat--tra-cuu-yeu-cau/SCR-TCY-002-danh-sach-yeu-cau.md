# SCR-TCY-002 — Danh sách yêu cầu tra soát › Danh sách

**Product:** Co-opBank Mobile Banking  
**Section:** Tra soát khiếu nại › Tra cứu yêu cầu  
**Screen Type:** Danh sách  
**Figma Node:** `142:29347` (có kết quả), `142:29341` (empty state search)  

---

## 1. Overview

Màn hình hiển thị danh sách kết quả tra cứu yêu cầu tra soát. Mỗi item hiển thị: ngày giờ giao dịch, số tiền, lý do tra soát, mã yêu cầu và trạng thái (badge màu). Có thanh tìm kiếm nhanh để lọc trong danh sách. Khi tìm kiếm không có kết quả → empty state.

**Artboards:**
- `tra-cuu-yeu-cau-3.png` — Danh sách có 3 kết quả (Đã xử lý, Đã tiếp nhận, Nghi vấn)
- `tra-cuu-yeu-cau-6.png` — Empty state: "Không có kết quả tìm kiếm" + keyboard

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** xem danh sách yêu cầu tra soát đã gửi,  
> **Để** nhanh chóng biết trạng thái từng yêu cầu và chọn xem chi tiết.

**Acceptance Criteria:**
- [ ] List item hiển thị đầy đủ: ngày giờ, số tiền, lý do tra soát, mã #, status badge
- [ ] Status badge có màu sắc phân biệt: Đã xử lý / Đã tiếp nhận / Nghi vấn
- [ ] Search bar để lọc trong danh sách hiện tại
- [ ] Empty state rõ ràng khi search không có kết quả

---

## 3. Content & Text Nodes

| Element | Label | Role |
|---------|-------|------|
| Header title | Danh sách yêu cầu tra soát | page_title |
| Search placeholder | Tìm kiếm | search_placeholder |
| List item — timestamp | 29/09/2025 18:00 | transaction_datetime |
| List item — amount | -5,000,000 VND | transaction_amount |
| List item — label | Lý do tra soát | dispute_reason_label |
| List item — value | Thay đổi tên người nhận | dispute_reason_value |
| List item — id | #123123 | dispute_id |
| Status badge | Đã xử lý | status_resolved |
| Status badge | Đã tiếp nhận | status_received |
| Status badge | Nghi vấn | status_suspect |
| Empty state | Không có kết quả tìm kiếm | empty_state_message |

---

## 4. Functional Requirements

| # | Requirement | Priority |
|---|-------------|----------|
| F1 | Hiển thị danh sách sorted by date desc | Must |
| F2 | Mỗi item: timestamp + amount + lý do + mã + badge | Must |
| F3 | Status badge có màu: Đã xử lý (xanh/green) / Đã tiếp nhận (xanh navy) / Nghi vấn (xám/neutral) | Must |
| F4 | Search bar lọc nhanh trong danh sách | Should |
| F5 | Empty state khi search không match | Must |
| F6 | Tap list item → navigate sang Chi tiết yêu cầu tra soát | Must |
| F7 | Pull-to-refresh danh sách | Should |

---

## 5. Non-Functional Requirements

- Pagination / infinite scroll nếu list > 20 items
- Negative amount (-5,000,000 VND) phải hiển thị rõ dấu âm
- Mã tra soát (#123123) phải selectable (copy)

---

## 6. UX Signal Inference (Phase 4e)

**Signals detected từ text-signals-banking.json:**

| Signal | Text | Category | Implication |
|--------|------|----------|-------------|
| list-transaction | "-5,000,000 VND", "29/09/2025" | data-display | Financial list item — amount formatting critical |
| status-badge-multi | "Đã xử lý", "Đã tiếp nhận", "Nghi vấn" | status | 3 distinct statuses — color differentiation required |
| search-within-list | "Tìm kiếm" | search | In-list search with keyboard trigger |
| empty-state-search | "Không có kết quả tìm kiếm" | feedback | Search empty state needed |
| dispute-id | "#123123" | data-display | Reference ID format |

**DDL UX Law matches:**
- **Recognition over Recall:** Status badges thay vì text code
- **Fitts' Law:** List item touch target — kiểm tra ≥44px height
- **von Restorff Effect:** Status badge cần visually distinct từng loại
