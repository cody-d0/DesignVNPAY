# SCR-TCY-001 — Tra cứu yêu cầu › Form nhập thông tin

**Product:** Co-opBank Mobile Banking  
**Section:** Tra soát khiếu nại › Tra cứu yêu cầu  
**Screen Type:** Form nhập thông tin  
**Figma Node:** `142:29634`, `142:29646`, `142:29658` (overlay)  

---

## 1. Overview

Màn hình tra cứu yêu cầu tra soát cho phép khách hàng tìm kiếm các yêu cầu tra soát đã tạo trước đó theo bộ lọc: khoảng thời gian (Từ ngày – Đến ngày), trạng thái tra soát, và mã tra soát. Nằm trong tab "Tra cứu yêu cầu" của trang Tra soát khiếu nại.

**Artboards:**
- `tra-cuu-yeu-cau-1.png` — Form rỗng (chỉ có date range + status = Tất cả)
- `tra-cuu-yeu-cau-2.png` — Form có mã tra soát "12312323"
- `tra-cuu-yeu-cau-7.png` — Form + overlay "Thông báo" không tìm thấy kết quả

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** tra cứu các yêu cầu tra soát đã gửi,  
> **Để** kiểm tra tình trạng xử lý và theo dõi tiến độ.

**Acceptance Criteria:**
- [ ] Khách hàng có thể lọc theo khoảng thời gian (Từ ngày / Đến ngày) bằng date picker
- [ ] Khách hàng có thể lọc theo trạng thái (Tất cả / Đã tiếp nhận / Đã xử lý / Nghi vấn)
- [ ] Khách hàng có thể nhập mã tra soát tự do để tìm kiếm
- [ ] Khi không tìm thấy kết quả → popup thông báo với nút "Đóng" để dismiss

---

## 3. Content & Text Nodes

| Element | Label | Role |
|---------|-------|------|
| Header title | Tra soát khiếu nại | page_title |
| Tab (inactive) | Tạo yêu cầu | tab_inactive |
| Tab (active) | Tra cứu yêu cầu | tab_active |
| Section label | Thông tin tra soát | section_label |
| Field label | Từ ngày | date_start_label |
| Field value | 12/09/2025 | date_start_placeholder |
| Field label | Đến ngày | date_end_label |
| Field value | 12/10/2025 | date_end_placeholder |
| Field label | Trang thái tra soát | status_filter_label |
| Default value | Tất cả | status_default |
| Field label | Mã tra soát | id_search_label |
| CTA | Tìm kiếm | primary_button |
| Modal title | Thông báo | dialog_title |
| Modal body | Không có thông tin tra soát trong khoảng thời gian tìm kiếm. Quý khách vui lòng thử lại. | dialog_error_body |
| Modal action | Đóng | dialog_dismiss |

---

## 4. Functional Requirements

| # | Requirement | Priority |
|---|-------------|----------|
| F1 | Date picker cho Từ ngày và Đến ngày (calendar icon trigger) | Must |
| F2 | Dropdown chọn trạng thái: Tất cả / Đã tiếp nhận / Đã xử lý / Nghi vấn | Must |
| F3 | Text field nhập Mã tra soát (optional) | Should |
| F4 | Button "Tìm kiếm" submit form → navigate sang màn hình danh sách | Must |
| F5 | Khi không có kết quả → popup modal với nút Đóng | Must |
| F6 | Tab navigation: Tạo yêu cầu / Tra cứu yêu cầu | Must |

---

## 5. Non-Functional Requirements

- Validation: Từ ngày ≤ Đến ngày
- Date range tối đa: 3 tháng (banking standard)
- Loading state khi submit search
- Popup dismiss: tap "Đóng" hoặc tap ngoài overlay

---

## 6. UX Signal Inference (Phase 4e)

**Signals detected từ text-signals-banking.json:**

| Signal | Text | Category | Implication |
|--------|------|----------|-------------|
| date-range-filter | "Từ ngày", "Đến ngày" | filter | Date range selection needed — validate order |
| status-filter | "Trang thái tra soát", "Tất cả" | filter | Multi-value filter with default "All" |
| search-by-id | "Mã tra soát" | search | Free-text ID search — optional field |
| error-no-results | "Không có thông tin tra soát" | feedback | Error state for empty results |
| tab-navigation | "Tạo yêu cầu", "Tra cứu yêu cầu" | navigation | 2-tab structure |
| cta-primary | "Tìm kiếm" | action | Primary search trigger |

**DDL UX Law matches:**
- **Fitts' Law:** CTA "Tìm kiếm" ở bottom → kiểm tra touch target ≥44px
- **Miller's Law:** 3 filter fields — trong giới hạn cognitive load
- **Doherty Threshold:** Loading state khi tìm kiếm cần <400ms feedback
