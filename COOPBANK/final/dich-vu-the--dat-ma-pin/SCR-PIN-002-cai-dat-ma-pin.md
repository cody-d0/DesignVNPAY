# SCR-PIN-002 — Cài đặt mã PIN › Form nhập thông tin

> **Module:** Dịch vụ thẻ | **Section:** Đặt mã PIN thẻ | **Flow Stage:** Input  
> **Screen ID:** SCR-PIN-002 | **Type:** Form nhập thông tin  
> **Primary image:** `ui/yat-ma-pin-the-1.png`

---

## Section 1 — Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Tên màn hình | Cài đặt mã PIN |
| Loại màn hình | Form nhập thông tin (Secure PIN entry) |
| URL/Deeplink | `coopbank://card/pin/set` |
| Platform | iOS + Android |
| Flow stage | Input |
| Preceding screen | Dịch vụ thẻ (SCR-PIN-001) |
| Succeeding screen | Xác thực khuôn mặt (SCR-PIN-003) |
| Overlays | 4: Xác thực giao dịch, Thành công, Lỗi giấy tờ hết hạn, Lỗi Facepay |

---

## Section 2 — Mô tả chức năng

Màn hình nhập **Mã PIN 6 chữ số** cho thẻ. Bao gồm:

- **2 trường secure input 6 ô** — "Nhập mã PIN" và "Nhập lại mã PIN", hiển thị dot/dash pattern
- **Bàn phím số custom** — Numpad 0-9 + backspace, thay thế system keyboard
- **Khu notice an toàn** — Quy tắc PIN (không dãy liên tiếp, không trùng lặp)
- **CTA adaptive** — "Xác nhận" (khi chưa điền đủ) / "Tiếp tục" (khi đủ → sang bước Xác thực)

### States

| State | Mô tả |
|---|---|
| `keyboard_visible_first_field` | Bàn phím mở, ô đầu tiên active (cursor), CTA = "Xác nhận" |
| `both_fields_filled` | Cả 2 trường đủ 6 chấm, bàn phím thu, CTA = "Tiếp tục" |
| `overlay_auth_sheet` | Bottom sheet Xác thực giao dịch (PIN thẻ cũ) |
| `overlay_success_dialog` | Dialog thành công sau xác thực |
| `overlay_error_id_expired` | Dialog lỗi: Giấy tờ hết hạn |
| `overlay_error_facepay` | Dialog lỗi: Chưa đăng ký Facepay |

---

## Section 3 — Nội dung văn bản (OCR)

| Element | Text | Role |
|---|---|---|
| Page title | Cài đặt mã PIN | header_title |
| Instruction | Quý khách vui lòng cài đặt mã PIN 6 số cho thẻ | body_instruction |
| Label field 1 | Nhập mã PIN | field_label |
| Input field 1 | `\| _ _ _ _ _` (state 1) / `• • • • • •` (state 2) | secure_input |
| Label field 2 | Nhập lại mã PIN | field_label |
| Input field 2 | `_ _ _ _ _ _` (state 1) / `• • • • • •` (state 2) | secure_input |
| Notice header | **Lưu ý** | section_label_accent |
| Notice 1 | Để đảm bảo an toàn... không chia sẻ cho bất kỳ ai | body_notice |
| Notice 2 | Mã PIN mới phải thỏa mãn các điều kiện sau: | body_notice |
| Rule 1 | Không được là dãy số tiến liên tiếp | list_item |
| Rule 2 | Không được là dãy số giống nhau | list_item |
| CTA (state 1) | Xác nhận | primary_action |
| CTA (state 2) | Tiếp tục | primary_action_enabled |
| Numpad | 1–9, 0, ⌫ | input_keys |
| **Overlay: Sheet title** | Xác thực giao dịch | overlay_title |
| Overlay: Sheet body | Quý khách vui lòng nhập mã PIN thẻ để xác thực giao dịch | overlay_instruction |
| Overlay: Sheet warning | **Lưu ý: PIN thẻ sẽ bị khóa nếu Quý khách nhập sai PIN 5 lần liên tiếp** | overlay_warning |
| Overlay: Success | Quý khách cài đặt mã PIN thẻ thành công. | success_message |
| Overlay: Error 1 title | Thông báo | dialog_title |
| Overlay: Error 1 body | Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học... | error_message |
| Overlay: Error 2 body | Yêu cầu cài đặt mã PIN cần được xác thực bằng Facepay. Quý khách vui lòng đăng ký "Thu thập sinh trắc học"... | error_message |
| Overlay: Buttons | Huỷ / Đồng ý | dialog_actions |

---

## Section 4 — Icons & Interactions

| Icon | Vị trí | Category | Action |
|---|---|---|:---|
| ic_back | Top-left | nav | Quay lại Dịch vụ thẻ |
| ic_home | Top-right (state 2) | nav | Về Home |
| ic_close_x | Bottom sheet top-right | trigger | Đóng overlay Xác thực GD |
| ic_success_checkmark | Dialog center | decoration | Trạng thái thành công |
| ic_backspace (⌫) | Numpad row 4, col 3 | trigger | Xoá chữ số cuối |

---

## Section 5 — UX Gaps (Preliminary)

1. **CTA label ambiguity** — State 1 hiển thị "Xác nhận" khi chưa điền đủ PIN có thể confuse user; phổ biến hơn là disabled CTA hoặc label "Nhập PIN" + progress indicator
2. **5-attempt lockout warning** — Chỉ hiện trong overlay Xác thực GD, không có trong màn form chính → người dùng có thể không biết giới hạn trước khi thực hiện
3. **PIN rule truncation** — Notice section rule 2 bị cắt (`Không được là dãy số giống nhau...`) — không rõ còn tiếp hay hết
4. **Confirm PIN feedback** — Không có realtime match indicator khi cả 2 fields đều đang nhập (user không biết 2 PIN có khớp không trước khi bấm CTA)
5. **Overlay entry trigger ambiguity** — "Xác nhận" ở state 1 trigger overlay Xác thực GD, nhưng "Tiếp tục" ở state 2 trigger sang màn Xác thực KM — 2 CTA tên khác nhau với intent khác nhau có thể gây nhầm lẫn UX flow
6. **Facepay error action** — Nút "Đồng ý" trong dialog Facepay không rõ sẽ dẫn user đến đâu (Screen nào? Deep link nào?)

---

## Section 6 — UX Signal Inference (Phase 4e)

> **Scope:** `screen` | **scope_id:** `SCR-PIN-002` | **Domain:** `banking`  
> **Patterns matched:** `confirm_dialog` ✅, `double_entry_validation`, `lockout_warning`, `success_state`  
> **DDL refs grounded by:** `ddl-context.json` (banking product)

### Flows inferred

| Signal | Flow | DDL Ref |
|---|---|---|
| `confirm_dialog` — "Huỷ / Đồng ý" pair detected | 2 error dialog paths (giấy tờ hết hạn, facepay) với destructive-adjacent actions | `ux-guidelines.csv#178` |
| `double_entry_validation` — "Nhập mã PIN" + "Nhập lại mã PIN" | Realtime match validation cần thêm (hiện tại không có inline error) | `web-interface.csv#257` |
| `lockout_warning` — "PIN thẻ sẽ bị khóa nếu nhập sai 5 lần liên tiếp" | Cảnh báo chỉ trong overlay — cần expose ở main form | `ux-guidelines.csv#176` |
| `success_state` — "Quý khách cài đặt mã PIN thẻ thành công." | Clear success copy, single-action dismiss | `ux-guidelines.csv#204` |

### Components inferred

| Component | Pattern ID | State inferred | DDL Ref |
|---|---|---|---|
| `6_cell_otp_input` ×2 | secure_pin_input | active / filled — missing: **error state** (mismatch) | `ux-guidelines.csv#183` |
| `custom_numpad` | numpad_10digit_backspace | Blocks system keyboard → **no paste access** | `web-interface.csv#254` |
| `bottom_sheet_auth` | overlay_auth | PIN re-entry + lockout warning | `ux-guidelines.csv#178` |
| `dialog_success` | success_dialog | Single CTA "Đóng", checkmark icon | `ux-guidelines.csv#204` |
| `dialog_error` ×2 | error_dialog_dual_action | "Huỷ/Đồng ý" — destination of "Đồng ý" unclear | `ux-guidelines.csv#176` |

### UX Improvements (prd_extension)

1. **Thêm inline error validation** — Sau khi field 2 điền đủ 6 digits: compare với field 1, show ❌ "Mã PIN không khớp" inline  
   `ddl_ref: web-interface.csv#257 (Inline Errors)`, `ux-guidelines.csv#176`
2. **Unify CTA label** — Dùng "Tiếp tục" duy nhất; khi chưa đủ PIN: disabled state (opacity 0.4)  
   `ddl_ref: ux-guidelines.csv#204 (Submit Feedback)`
3. **Expose lockout warning trong main form** — Thêm vào notice section: ⚠️ "PIN sẽ bị khóa sau 5 lần sai liên tiếp"  
   `ddl_ref: ux-guidelines.csv#176 (Error Feedback)`
4. **Realtime match indicator** — Sau khi field 2 đủ 6 digits: ✅ xanh nếu match, ❌ đỏ nếu không  
   `ddl_ref: ux-guidelines.csv#176`
5. **Clarify error dialog action** — "Đồng ý" trong Facepay dialog cần sub-label: "→ Mở Thu thập sinh trắc học"  
   `ddl_ref: ux-guidelines.csv#204`
