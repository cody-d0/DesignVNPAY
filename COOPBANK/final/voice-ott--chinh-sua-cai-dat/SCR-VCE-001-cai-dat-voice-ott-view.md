# SCR-VCE-001 · Cài đặt Voice OTT › Form nhập thông tin

**Screen ID:** SCR-VCE-001  
**Display Name:** Cài đặt Voice OTT › Form nhập thông tin  
**Section:** Chỉnh sửa cài đặt Voice  
**Product:** Co-opBank Mobile Banking  
**Domain:** Banking  
**Artboards:** 7201 Chỉnh Sửa Voice (main) + 7204 Chỉnh Sửa Voice (overlay: success popup)  
**Wireframe Images:** ui/7201-chinh-sua-voice.png, ui/7204-chinh-sua-voice.png

---

## 1. Screen Overview

Màn hình xem thông tin cài đặt hiện tại của tính năng **Voice OTT** (Voice Over The Top). Đây là read-only view hiển thị cấu hình đã đăng ký, cho phép người dùng nghe thử giọng đọc, bật/tắt thông báo, và xem danh sách tài khoản + khung giờ đã đăng ký. Overlay 7204 hiển thị popup success sau khi lưu thay đổi.

**User Goal:** Xem lại cài đặt Voice OTT hiện tại và điều hướng sang chỉnh sửa nếu cần.

**Screen Type:** Settings view (read-only) with sticky bottom CTA

---

## 2. User Story

> **Là** khách hàng Co-opBank đã đăng ký Voice OTT,  
> **Tôi muốn** xem lại cấu hình Voice OTT hiện tại (danh sách tài khoản, khung giờ, trạng thái bật/tắt),  
> **Để** kiểm tra và quyết định có cần chỉnh sửa không.

**Acceptance Criteria:**
- AC1: Hiển thị đầy đủ nội dung giới thiệu tính năng Voice OTT
- AC2: Nút "Nghe thử" cho phép nghe preview giọng đọc OTT
- AC3: Toggle "Nhận thông báo BĐSD bằng giọng nói" hiển thị trạng thái hiện tại (ON/OFF)
- AC4: Danh sách tài khoản đăng ký hiển thị đầy đủ số tài khoản
- AC5: Khung giờ thông báo hiển thị chính xác khoảng thời gian đã cài đặt
- AC6: CTA "Chỉnh sửa" điều hướng sang màn hình edit (SCR-VCE-002)
- AC7: Popup success xuất hiện sau khi save từ 7202, với nội dung xác nhận rõ ràng và nút "Đóng"

---

## 3. UI Text Inventory (OCR)

| # | Text | Component | Zone |
|---|------|-----------|------|
| 1 | 9:41 | status-bar | top |
| 2 | Cài đặt Voice OTT | header-title | top |
| 3 | Nội dung giới thiệu | section-header | middle |
| 4 | Voice OTT là tính năng phát loa đọc thông báo BĐSD bằng giọng nói trên thiết bị di động khi tài khoản đã đăng ký của Quý khách được cộng tiền hoặc tài khoản chia sẻ của Quý khách được cộng tiền. | body-text | middle |
| 5 | Lưu ý: KHÔNG để thiết bị ở chế độ im lặng | warning-text | middle |
| 6 | Nghe thử | secondary-action | middle |
| 7 | Nhận thông báo BĐSD bằng giọng nói | toggle-label | middle |
| 8 | Thông tin cài đặt | section-header | middle |
| 9 | Danh sách tài khoản đăng ký | sub-section-header | middle |
| 10 | 212312312313 | account-number | middle |
| 11 | 312312312313 | account-number | middle |
| 12 | Thời gian thông báo | sub-section-header | middle |
| 13 | Từ 10:00 đến 23:15 | time-range-display | middle |
| 14 | Chỉnh sửa | primary-cta | bottom |
| 15 | [OVERLAY] Thông báo | popup-title | overlay |
| 16 | [OVERLAY] Quý khách đã cập nhật cài đặt nhận thông báo BĐSD bằng giọng nói thành công. | popup-body | overlay |
| 17 | [OVERLAY] Đóng | popup-cta | overlay |

**Icon Inventory:**
- `back-arrow` (top-left, nav)
- `home-icon` (top-right, nav)
- `play-circle-blue` (middle-left, trigger — beside "Nghe thử")
- `toggle-switch-ON-blue` (middle-right, trigger — beside toggle label)
- `s-red-badge-circle` (middle-left, decoration — before section header)
- `logo-coopbank-faded` (background, decoration)

---

## 4. Flow & Navigation

**Đến màn hình này từ:** Settings menu / Voice OTT entry point  
**Từ màn hình này đến:** SCR-VCE-002 (via "Chỉnh sửa" CTA)  
**Overlay:** 7204 success popup (from SCR-VCE-002 save action → back to this view)

**Non-functional Requirements (NFR):**
- Toggle state phải persist sau khi user rời màn hình
- Success popup phải auto-dismiss sau X giây hoặc qua nút "Đóng"
- Nếu không có tài khoản đăng ký → hiển thị empty state cho danh sách tài khoản

---

## 5. UX Signal Inference (Phase 4e)

**UX Signals detected:**
- `LONG_BODY_TEXT`: Đoạn giới thiệu Voice OTT dài (4 dòng) — rủi ro truncation trên màn hình nhỏ
- `WARNING_TEXT_CAPS`: "Lưu ý: KHÔNG để thiết bị ở chế độ im lặng" — dùng all-caps KHÔNG → cần đánh giá accessibility
- `READ_ONLY_VIEW`: Chỉ có 1 CTA "Chỉnh sửa" → clear action hierarchy
- `OVERLAY_SUCCESS_PATTERN`: Popup "Thông báo" → tuỳ chỉnh nút từ text sang button rõ ràng hơn
- `ACCOUNT_LIST_DISPLAY`: 2 account numbers hiển thị → cần xem xét masking PII (số tài khoản)
- `TIME_RANGE_COMPACT`: "Từ 10:00 đến 23:15" — compact display tốt cho read-only

**DDL Signals matched:**
- `banking.notification_settings` → confirm read-only pattern
- `banking.security` → account number display → PII masking check needed
