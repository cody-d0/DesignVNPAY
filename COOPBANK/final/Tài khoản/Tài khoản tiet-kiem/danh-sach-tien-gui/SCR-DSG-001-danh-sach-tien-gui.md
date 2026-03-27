# SCR-DSG-001 — Danh sách tiền gửi › Danh sách

**Screen ID:** SCR-DSG-001  
**Section:** Tiết kiệm › Danh sách tiền gửi  
**Screen Type:** list  
**Figma Artboards:** 1601, 1602, 1603 (3 state variants)  
**Wireframe Images:** `ui/1601-danh-sach-tien-gui.png`, `ui/1602-danh-sach-tien-gui.png`, `ui/1603-danh-sach-tien-gui.png`

---

## 1. Overview

Màn hình danh sách toàn bộ tài khoản tiền gửi (tiền gửi thường + tiền gửi tích lũy) của khách hàng trong ứng dụng Co-opBank Mobile Banking. Hiển thị tổng số dư gốc, bộ lọc theo loại, danh sách thẻ tài khoản với thông tin chi tiết, và trạng thái đặc biệt (tạm dừng tích lũy). Hỗ trợ empty state với CTA onboarding.

**Product:** Co-opBank Mobile Banking  
**Domain:** Banking / Tiết kiệm  
**Entry Point:** Tiền gửi tiết kiệm hub menu → "Danh sách tiền gửi"  

---

## 2. User Story

**Tiêu đề:** Xem danh sách tài khoản tiền gửi

**Vai trò:** Khách hàng ngân hàng Co-opBank

**Kịch bản:**
- **Loaded state:** "Là khách hàng, tôi muốn xem toàn bộ tài khoản tiền gửi của mình, bao gồm số dư, ngày đáo hạn, kỳ hạn và trạng thái, để theo dõi tình hình tiết kiệm."
- **Filter state:** "Là khách hàng, tôi muốn lọc theo loại tiền gửi (thường hoặc tích lũy) để tìm nhanh tài khoản cần thiết."
- **Empty state:** "Là khách hàng mới, tôi muốn được hướng dẫn mở tài khoản tiền gửi khi chưa có tài khoản nào."

**Acceptance Criteria:**
- Hiển thị tổng số dư gốc của tất cả tài khoản
- Bộ lọc chip: Tất cả / Tiền gửi thường / Tiền gửi tích lũy với số lượng tương ứng
- Mỗi card hiển thị: số tài khoản, ngày đến hạn/tích lũy, kỳ hạn, số dư gốc hiện tại
- Hiển thị badge trạng thái "Tạm dừng tích lũy" khi tài khoản tích lũy bị tạm dừng
- FAB (+) luôn hiển thị để mở tài khoản tiền gửi mới
- Empty state: thông báo + tooltip CTA khi không có tài khoản

---

## 3. Screen Text (OCR)

| # | Text | Location | Type |
|---|------|----------|------|
| 1 | Danh sách tiền gửi | Header center | Title |
| 2 | [filter icon] | Header right | Icon-action |
| 3 | Tổng số dư gốc | Summary row label | Label |
| 4 | 10,000,000 VND | Summary value (1601) | Value-currency |
| 5 | 5,000,000 VND | Summary value (1602/1603) | Value-currency |
| 6 | Tất cả (2) | Filter chip [active, 1601] | Chip-active |
| 7 | Tiền gửi thường (10) | Filter chip [1601] | Chip |
| 8 | Tiền gửi tích lũy (1) | Filter chip [1601] | Chip |
| 9 | Tất cả (1) | Filter chip [active, 1602] | Chip-active |
| 10 | Tiền gửi thường (1) | Filter chip [1602] | Chip |
| 11 | Tiền gửi tích lũy (0) | Filter chip [1602/1603] | Chip-zero |
| 12 | Tất cả (0) | Filter chip [active, 1603] | Chip-active |
| 13 | Tiền gửi thường (0) | Filter chip [1603] | Chip-zero |
| 14 | 12300123123000 | Card — account number | Account-number |
| 15 | Ngày tích lũy tiếp theo: 20/09/2021 | Card date row (tích lũy) | Date-label |
| 16 | Ngày đáo hạn: 21/09/2025 | Card date row | Date-label |
| 17 | Tạm dừng tích lũy | Card — status badge | Status-warning |
| 18 | Kỳ hạn: 2 tháng | Card metadata | Metadata |
| 19 | Số số: 1231233213 | Card serial (1602) | Metadata |
| 20 | Ngày đến hạn: 20/09/2021 | Card date (1602) | Date-label |
| 21 | Số dư gốc hiện tại | Card balance label | Label |
| 22 | 5,000,000 VND | Card balance value | Value-currency |
| 23 | Quý khách chưa có tài khoản tiền gửi. Vui lòng bấm vào mở mới để mở tiền gửi trực tuyến | Empty state message | Empty-state-text |
| 24 | Nhấn vào đây để mở mới tiền gửi trực tuyến | Tooltip CTA (1603) | CTA-tooltip |
| 25 | + | FAB bottom-right | FAB |

**Icon Inventory:**
- `filter-funnel` — header right, action (mở bộ lọc nâng cao)
- `red-badge-account` — card icon, status indicator (tich lũy type)
- `fab-plus-blue` — bottom right, trigger (mở mới tiền gửi)
- `chip-toggle` — filter row (chọn loại xem)

---

## 4. PRD (Augmented)

### 4.1 Feature Specification

**Feature name:** Danh sách tài khoản tiền gửi

**Components:**
- **Summary Bar:** Label "Tổng số dư gốc" + tổng số VND (aggregated across all accounts)
- **Filter Chips:** Horizontal scrollable chip group (Tất cả / Tiền gửi thường / Tiền gửi tích lũy), mỗi chip có count badge
- **Deposit Card (balance-card):** 
  - Icon loại tài khoản (có badge đỏ badge)
  - Số tài khoản (bold, primary)
  - Ngày tích lũy tiếp theo / Ngày đáo hạn / Ngày đến hạn
  - Kỳ hạn
  - Trạng thái badge (Tạm dừng tích lũy — màu đỏ)
  - "Số dư gốc hiện tại" + số VND (right-aligned, bold)
- **FAB (+):** Floating Action Button, fixed bottom-right, mở mới tiền gửi
- **Empty State:** Text message + tooltip CTA + FAB
- **Filter Icon Header:** Top-right, mở advanced filter panel

### 4.2 Information Architecture

```
Danh sách tiền gửi
├── Summary Bar
│   ├── Label: "Tổng số dư gốc"
│   └── Value: {totalBalance} VND
├── Filter Chips (horizontal scroll)
│   ├── Tất cả ({total})  [default active]
│   ├── Tiền gửi thường ({count})
│   └── Tiền gửi tích lũy ({count})
├── Deposit Card List [repeat per account]
│   ├── Account Icon + status badge
│   ├── Account Number (primary)
│   ├── Date info (contextual per type)
│   ├── Status badge (conditional: "Tạm dừng tích lũy")
│   ├── Term (Kỳ hạn)
│   └── Balance (Số dư gốc hiện tại + value)
├── Empty State [conditional]
│   ├── Empty message
│   └── Tooltip CTA
└── FAB (+) [persistent]
```

### 4.3 States

| State | Trigger | UI |
|-------|---------|-----|
| Loaded (many) | ≥2 active accounts | Summary + chips + card list |
| Loaded (few) | 1 account | Summary + chips + 1 card |
| Empty | 0 accounts | Summary (0 VND) + chips (0) + empty message + tooltip |
| Filter: Thường | Chip "Tiền gửi thường" | Shows only standard deposits |
| Filter: Tích lũy | Chip "Tiền gửi tích lũy" | Shows only accumulation deposits |

### 4.4 Business Logic

- Tổng số dư gốc = sum(các tài khoản tiền gửi đang hoạt động)
- Chip count thay đổi real-time theo filter state
- "Tạm dừng tích lũy" badge = trạng thái đặc biệt của tiền gửi tích lũy, color đỏ
- FAB luôn visible (z-index cao nhất) kể cả empty state
- Tooltip CTA chỉ hiển thị trong empty state, dismiss khi tap ngoài
- Tap vào card → navigate sang Chi tiết tiền gửi
- Tap FAB → navigate sang Mở tiền gửi mới

### 4.5 NFR (Non-Functional Requirements)

| # | Requirement | Target |
|---|------------|--------|
| NFR-1 | Load time danh sách | < 2s |
| NFR-2 | Skeleton loading | PHẢI hiển thị khi đang load |
| NFR-3 | Pagination | Infinite scroll nếu > 10 items |
| NFR-4 | Accessibility | WCAG AA, touch targets ≥44px |
| NFR-5 | Security | Số tài khoản không masking (full display) |

---

## 5. UX Signal Extensions (Phase 4e)

**UX Signals detected:**
- `danh-sách` → List pattern → Áp dụng: pagination, empty state, skeleton loading
- `tiền-gửi` + `số-dư` → Finance list → Áp dụng: precision formatting, currency display
- `Tạm dừng` → Status signal → Áp dụng: clear status communication, color coding
- `Nhấn vào đây` → Onboarding CTA → Áp dụng: tooltip dismiss, CTA prominence
- `mở mới` → Primary action → Áp dụng: FAB pattern, high discoverability

**DDL Context Hints:**
- Component match: `balance-card` → DDL component spec cho card danh sách tài khoản
- Component match: `chip` → DDL filter chip spec
- UX Law match: `Miller's Law` → giới hạn chip filter (3 options = good), cognitive load
- UX Law match: `Fitts's Law` → FAB size ≥ 44px, touch target card toàn width
- Guideline: `UXG-165` → Empty state phải có clear action
- Guideline: `UXG-243` → Currency display chuẩn hóa (VND)

---

## 6. Flow (Navigation)

| Trigger | Action | Destination |
|---------|--------|-------------|
| Back chevron | Navigate back | Tiền gửi tiết kiệm hub |
| Tap balance-card | Navigate (drill-down) | Chi tiết tiền gửi (EXT) |
| Tap FAB (+) | Navigate | Mở tiền gửi mới (EXT) |
| Tap chip filter | Filter intra-screen | SCR-DSG-001 (state change) |
| Tap filter icon header | Navigate (panel) | Bộ lọc nâng cao (EXT) |
| Tap tooltip CTA | Navigate | Mở tiền gửi mới (EXT) |
