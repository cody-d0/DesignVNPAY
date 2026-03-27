# SCR-VCE-002 · Chỉnh sửa cài đặt Voice › Form nhập thông tin

**Screen ID:** SCR-VCE-002  
**Display Name:** Chỉnh sửa cài đặt Voice › Form nhập thông tin  
**Section:** Chỉnh sửa cài đặt Voice  
**Product:** Co-opBank Mobile Banking  
**Domain:** Banking  
**Artboards:** 7202 Chỉnh Sửa Voice (main edit) + 7203 Chỉnh Sửa Voice (overlay: OTP bottom sheet)  
**Wireframe Images:** ui/7202-chinh-sua-voice.png, ui/7203-chinh-sua-voice.png

---

## 1. Screen Overview

Màn hình **chỉnh sửa** cài đặt Voice OTT. Cho phép người dùng:
1. Thêm / Xóa tài khoản đăng ký nhận thông báo giọng nói
2. Cài đặt khung giờ đọc loa (time-picker từ-đến)

Sau khi nhấn "Lưu chỉnh sửa" → hệ thống yêu cầu xác thực OTP qua bottom sheet (7203 overlay). Sau OTP thành công → popup success xuất hiện ở màn hình 7201 (view).

**Screen Type:** Edit form với dual CTA (Huỷ / Lưu) + auth overlay (OTP bottom sheet)

---

## 2. User Story

> **Là** khách hàng Co-opBank đã đăng ký Voice OTT,  
> **Tôi muốn** chỉnh sửa danh sách tài khoản và khung giờ nhận thông báo giọng nói,  
> **Để** tuỳ chỉnh Voice OTT phù hợp với nhu cầu của mình và xác nhận an toàn qua OTP.

**Acceptance Criteria:**
- AC1: Hiển thị đầy đủ danh sách tài khoản hiện tại với icon xóa (−) tại mỗi dòng
- AC2: Nút "Thêm tài khoản" (+) mở picker/form thêm tài khoản mới
- AC3: Khi nhấn (−) tại 1 tài khoản → xóa tài khoản đó khỏi danh sách (hoặc confirm dialog)
- AC4: Time picker "Từ" và "Đến" cho phép chọn giờ:phút theo format HH:mm
- AC5: Helper text giải thích hành vi khi bỏ trống khung giờ
- AC6: "Huỷ" → điều hướng về SCR-VCE-001 (no change)
- AC7: "Lưu chỉnh sửa" → trigger OTP bottom sheet overlay (7203)
- AC8: OTP overlay hiển thị số điện thoại đã che (masked: 098****123)
- AC9: 6 ô nhập OTP rõ ràng, hỗ trợ paste/auto-tab
- AC10: "Xác nhận" trong OTP overlay → submit, chuyển về view + hiện success popup

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
| 7 | Tài khoản đọc loa thông báo | section-header | middle |
| 8 | Thêm tài khoản | add-action-trigger | middle |
| 9 | 12312312313123 | account-number-row-1 | middle |
| 10 | 12312312313123 | account-number-row-2 | middle |
| 11 | Khung giờ đọc loa thông báo | section-header | middle |
| 12 | Ngoài khung giờ này, loa sẽ không phát thông báo BĐSD | helper-text | middle |
| 13 | Từ | time-picker-label-start | middle |
| 14 | Đến | time-picker-label-end | middle |
| 15 | 10:00 | time-picker-value-start | middle |
| 16 | 23:15 | time-picker-value-end | middle |
| 17 | Nếu bỏ trống khung giờ đọc loa, Quý khách sẽ được phát loa thông báo BĐSD không bị giới hạn thời gian. | helper-text-extended | middle |
| 18 | Huỷ | secondary-cta | bottom |
| 19 | Lưu chỉnh sửa | primary-cta | bottom |
| 20 | [OVERLAY] Xác thực giao dịch | bottomsheet-title | overlay |
| 21 | [OVERLAY] Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098****123 | bottomsheet-instruction | overlay |
| 22 | [OVERLAY] Xác nhận | bottomsheet-cta | overlay |

**Icon Inventory:**
- `back-arrow` (top-left, nav)
- `home-icon` (top-right, nav)
- `play-circle-blue` (middle-left, trigger — beside "Nghe thử")
- `plus-circle-blue` (middle-left, trigger — beside "Thêm tài khoản")
- `minus-circle-blue` ×2 (middle-right per row, trigger — remove account)
- `calendar-icon` ×2 (right of time-picker fields — ⚠️ should be clock icon)
- `person-red-badge` (section badge, decoration)
- `clock-red-badge` (section badge, decoration)
- `coopbank-logo-small` (per account row, decoration)
- `[OTP-OVERLAY] x-close-button` (top-right of sheet)
- `[OTP-OVERLAY] 6-digit-input-cells` ×6 (44×44px each, OTP input)

---

## 4. Flow & Navigation

**Đến màn hình này từ:** SCR-VCE-001 (via "Chỉnh sửa" CTA)  
**Từ màn hình này đến:**
- SCR-VCE-001 (via "Huỷ")
- SCR-VCE-001 + popup success (via "Lưu chỉnh sửa" → OTP → confirm)

**Overlay flow:**  
`Lưu chỉnh sửa` → [OTP bottom-sheet 7203] → `Xác nhận` → SCR-VCE-001 + success popup 7204

**Non-functional Requirements (NFR):**
- Validation: Phải có ít nhất 1 tài khoản trong danh sách trước khi lưu
- Validation: Time picker không cho phép "Từ" > "Đến" (invalid range)
- OTP: Timeout 2 phút, resend option nếu OTP hết hạn
- OTP: Paste support + auto-submit khi điền đủ 6 chữ số

---

## 5. UX Signal Inference (Phase 4e)

**UX Signals detected:**
- `CALENDAR_ICON_MISMATCH`: Time picker dùng icon calendar (📅) thay vì clock (🕐) — semantic mismatch với time selection
- `INLINE_ADD_REMOVE_PATTERN`: Thêm/xóa tài khoản trực tiếp trong list — effective nhưng cần confirm trước khi xóa
- `DUAL_CTA_ASYMMETRY`: "Huỷ" vs "Lưu chỉnh sửa" — label pair tốt, nhưng check weight parity (secondary vs primary)
- `OTP_MASKED_PHONE`: "098****123" → good security practice, đúng chuẩn banking
- `OTP_6_DIGIT_CELLS`: 6 cells × 44px — đúng touch target (≥44px), good
- `HELPER_TEXT_CONDITION`: 2 helper texts giải thích điều kiện khung giờ — valuable nhưng text dài
- `DUPLICATE_ACCOUNT_NUMBERS`: 2 account rows hiển thị cùng số "12312312313123" → likely placeholder data, cần xem xét account masking trong production
- `NO_EMPTY_STATE`: Không thấy empty state khi tất cả tài khoản bị xóa

**DDL Signals matched:**
- `banking.otp_authentication` → OTP overlay pattern → check state coverage (loading, error, resend)
- `banking.form_validation` → time picker range → check validation feedback
- `banking.security` → OTP masking, account list masking
