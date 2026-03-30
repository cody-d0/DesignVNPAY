# UX Review Report — Chuyển tiền nhanh 24/7 qua thẻ

## Tổng quan
- Folder: `coopbank/final/Chuyển tiền nhanh 24/7 qua thẻ`
- Số màn hình: 3 | Tổng check: 44
- Pass: 33 | Gap: 9 | Unverifiable: 2
- UX Score (Simple): 75% (33/44)
- UX Score (Weighted): 100%
- Proposals: 🔴 Critical: 2 | 🟡 Major: 3 | ⚪ Minor: 2 | Total: 7

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Màn OTP overlay (CTNST_5) hiển thị 6 ô nhập OTP nhưng thiếu hoàn toàn: (1) nút "Gửi lại mã OTP" với countdown timer, ... |
| **Gap ref** | Check #10 |
| **DDL** | UXG-235 · COMP:otp-input-1 · Law:doherty |
| **Giải pháp** | Thêm text link "Gửi lại mã OTP" với countdown "Gửi lại sau 60s"; Hiển thị "Mã OTP hết hạn sau: 02:00" realtime; Spinner + "Đang xác thực..." khi ta... |

---


**Total checks:** 44  
**Pass:** 33 | **Gap:** 9 | **Unverifiable:** 2  
**Simple Score:** 75%  
**Weighted Score:** 75%#### UXP-002 · Critical
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Không có trạng thái error/validation visible trên form nhập |
| **Gap ref** | Check #11, Check #12, Check #13 |
| **DDL** | UXG-180 · COMP:text-input-1 |
| **Giải pháp** | Viền đỏ (#dc2626) + icon cảnh báo + helper text lỗi dưới mỗi field; Validate real-time: số thẻ 16 digits, số tiền > 0 và ≤ hạn mức; Banner tổng hợp... |

---

#### UXP-003 · Major
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Hai variant xác nhận (CTNST_4: qua thẻ, CTNST_5: qua số điện thoại) hiển thị thông tin khác nhau về label: CTNST_4 dù... |
| **Gap ref** | Check #14 |
| **DDL** | UXG-183 |
| **Giải pháp** | Thêm subtitle phân biệt: "Chuyển tiền qua thẻ" vs "Chuyển tiền qua số điện thoại"; Giữ nguyên label "Số thẻ thụ hưởng" cho flow qua thẻ, không mix ... |

---

#### UXP-004 · Major
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Biên nhận chỉ hiển thị "Mã giao dịch: 0982312" (7 ký tự) — format không chuẩn, thiếu prefix bank |
| **Gap ref** | Check #10, Check #9 |
| **DDL** | COMP:receipt-preview-1 · Law:peak-end |
| **Giải pháp** | Format chuẩn: "COOP-2020021522-0982312" (prefix + date + code); Format: "22:00 — 15/02/2020 (GMT+7)" |

---

#### UXP-005 · Major
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Overlay "Danh bạ thụ hưởng" (CTNST_2) hiển thị danh sách dài nhưng không có trạng thái empty state khi search không c... |
| **Gap ref** | Check #14 |
| **DDL** | UXG-184 · Law:hick |
| **Giải pháp** | "Không tìm thấy người hưởng. Bạn có thể nhập trực tiếp số thẻ." + CTA "Nhập thủ công"; Thêm shadow/fade ở bottom khi list dài hơn viewport |

---

#### UXP-006 · Minor
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Nội dung giao dịch mặc định hiển thị "NGUYEN HOANG KHAI chuyen tien" (CTNST_1) — toàn chữ hoa không dấu, style bankin... |
| **Gap ref** | Check #8 |
| **DDL** | UXG-181 |
| **Giải pháp** | Auto-generate nội dung mặc định: "{Tên} chuyển tiền" (có dấu, sentence case) |

---

#### UXP-007 · Minor
| **Màn hình** | Chuyển tiền nhanh 24/7 qua thẻ › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Biên nhận hiển thị "nguyen tung" (chữ thường) trong khi CTNST_4 confirm screen hiển thị "NGUYEN TUNG" (chữ hoa) |
| **Gap ref** | Check #9, Check #10 |
| **DDL** | COMP:receipt-preview-1 · Law:peak-end |
| **Giải pháp** | Normalize tên thụ hưởng: luôn uppercase cả receipt lẫn confirm; Viết tắt trên receipt: "BIDV" (đã rõ bên confirm). Hoặc tăng width card |

---

## Chi tiết theo màn hình

### 1. Chuyển tiền nhanh 24/7 qua thẻ › Form nhập thông tin
> `SCR-THE-001` · form · 3 artboards
>
> **Score: 82% | Pass: 14 | Gap: 2 | Unverifiable: 1 | Images: chuyen-tien-nhanh-247-qua-the.png, chuyen-tien-nhanh-247-qua-the-2.png, chuyen-tien-nhanh-247-qua-the-3.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + back button | Skill C | COMP:app-header-1 | Pass | Từ ảnh CTNST_1: header xanh navy "Chuyển tiền nhanh 24/7 qua thẻ" + back_white icon trái |
| 2 | Card tài khoản nguồn hiển thị đủ: số TK, số dư, đơn vị | Skill B | UXG-235 | Pass | Từ ảnh: card hiển thị "9099798712313123", "Số dư khả dụng", "20,000,000 VND" |
| 3 | Dropdown chọn tài khoản nguồn | Skill C | COMP:text-input-1 | Pass | Từ ảnh: drop_blue icon bên phải card TK nguồn |
| 4 | Input "Số thẻ thụ hưởng" có icon danh bạ | Skill A | UXG-184 | Pass | Từ ảnh CTNST_1: input field + ic_contact icon bên phải |
| 5 | Resolve tên + ngân hàng sau nhập thẻ | Skill B | UXG-183 | Pass | Từ ảnh CTNST_3: "NGUYEN HOANG HIEU", "Vietcombank" resolved dưới input |
| 6 | Toggle "Lưu danh bạ thụ hưởng" | Skill C | — | Pass | Từ ảnh CTNST_1: switch component visible |
| 7 | Input số tiền hiển thị cả số + bằng chữ | Skill A | UXG-235 | Pass | Từ ảnh CTNST_3: "20,000,000" + "Hai mươi triệu đồng" |
| 8 | Dropdown đối tượng chịu phí | Skill C | — | Pass | Từ ảnh: "Người chuyển trả" + drop_blue |
| 9 | Nội dung giao dịch có character counter | Skill A | COMP:text-input-1 | Pass | Từ ảnh CTNST_1: "30/160" counter visible |
| 10 | CTA "Tiếp tục" full-width và rõ ràng | Skill C | UXG-235 | Pass | Từ ảnh: nút xanh navy "Tiếp tục" full-width ở footer |
| 11 | Error state cho input fields (viền đỏ, helper text) | Skill A | COMP:text-input-1 | Gap | DDL `text-input-1` yêu cầu states: error, errorMessage. Không có variant nào hiển thị error state |
| 12 | Overlay danh bạ có search + list | Skill C | — | Pass | Từ ảnh CTNST_2: "Danh bạ thụ hưởng", search bar + 8 contacts |
| 13 | Overlay danh bạ có close affordance | Skill C | UXG-184 | Pass | Từ ảnh CTNST_2: icon X (close) góc phải trên |
| 14 | Empty state cho search danh bạ không kết quả | Skill B | COMP:empty-state-1 | Gap | Không có variant hiển thị empty state khi search không tìm thấy |
| 15 | Fitts's Law: CTA size ≥ 44px touch target | Skill C | UXG-235 | Pass | Từ ảnh + metadata: btn_main 343×44px, đủ touch target |
| 16 | Hick's Law: số lượng choices hợp lý | Skill A | — | Pass | Form layout 3 field chính, clear hierarchy |
| 17 | Label "Số tài khoản/Số thẻ/Số điện thoại" placeholder quá dài | Skill C | UXG-181 | Unverifiable | Chỉ thấy trong CTNST_2 (overlay), có thể bị truncate trên device nhỏ hơn 375px |

### 2. Chuyển tiền nhanh 24/7 qua thẻ › Xác nhận giao dịch
> `SCR-THE-002` · confirm · 2 artboards
>
> **Score: 79% | Pass: 11 | Gap: 3 | Unverifiable: 0 | Images: chuyen-tien-nhanh-247-qua-the-4.png, chuyen-tien-nhanh-247-qua-the-5.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Xác nhận giao dịch" + back button | Skill C | COMP:app-header-1 | Pass | Từ ảnh CTNST_4: header xanh navy + back_white |
| 2 | Banner instruction text | Skill C | UXG-183 | Pass | Từ ảnh CTNST_4: "Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo" |
| 3 | Hiển thị đầy đủ 7 rows thông tin readonly | Skill B | UXG-235 | Pass | Từ ảnh CTNST_4: TK nguồn, thẻ, tên, NH, số tiền, phí, nội dung — all 7 rows visible |
| 4 | Số tiền hiển thị cả số + chữ (confirmation) | Skill A | UXG-235 | Pass | Từ ảnh CTNST_4: "20,000,000 VND" + "Hai mươi triệu đồng" (chữ đỏ) |
| 5 | Dropdown chọn phương thức xác thực | Skill C | — | Pass | Từ ảnh CTNST_4: "Chọn phương thức xác thực" + "SMS OTP" + drop_blue |
| 6 | CTA "Xác nhận" rõ ràng | Skill C | UXG-235 | Pass | Từ ảnh: nút xanh navy "Xác nhận" full-width |
| 7 | OTP overlay có instruction text rõ ràng | Skill C | COMP:otp-input-1 | Pass | Từ ảnh CTNST_5: "Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098****123" |
| 8 | OTP 6 ô nhập riêng biệt | Skill C | COMP:otp-input-1 | Pass | Từ ảnh CTNST_5: 6 ô 44×44px visible |
| 9 | OTP che số điện thoại (privacy) | Skill A | UXG-235 | Pass | Từ ảnh CTNST_5: "098****123" — masked properly |
| 10 | OTP resend button + countdown timer | Skill A | COMP:otp-input-1 | Gap | DDL spec: canResend, timeLeft states + resend button. Từ ảnh: KHÔNG thấy nút gửi lại hay timer |
| 11 | OTP close affordance (dismiss overlay) | Skill C | UXG-184 | Pass | Từ ảnh CTNST_5: clear_login icon (X) top-right |
| 12 | Loading/processing state khi xác nhận | Skill A | UXG-180 | Gap | Không có variant hiển thị loading spinner hoặc processing state |
| 13 | Fitts's Law: CTA size ≥ 44px | Skill C | UXG-235 | Pass | Từ metadata + ảnh: btn_main 343×44px |
| 14 | Label consistency giữa 2 variants | Skill C | UXG-183 | Gap | CTNST_4: "Số thẻ thụ hưởng" vs CTNST_5: "Số tài khoản thụ hưởng" + thêm "Số điện thoại" — inconsistent |

### 3. Chuyển tiền nhanh 24/7 qua thẻ › Kết quả giao dịch
> `SCR-THE-003` · result · 1 artboard
>
> **Score: 62% | Pass: 8 | Gap: 4 | Unverifiable: 1 | Images: chuyen-tien-nhanh-247-qua-the-6.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Kết quả giao dịch" + home button | Skill C | COMP:app-header-1 | Pass | Từ ảnh CTNST_6: ic_backhome + "Kết quả giao dịch" |
| 2 | Status "Chuyển tiền thành công" rõ ràng + icon | Skill C | COMP:receipt-preview-1 | Pass | Từ ảnh: checkmark icon xanh + "Chuyển tiền thành công" |
| 3 | Số tiền hiển thị nổi bật | Skill A | UXG-235 | Pass | Từ ảnh: "20,000,000 VND" text lớn, màu xanh, bold |
| 4 | Đầy đủ chi tiết receipt: thời gian, tên, thẻ, NH, mã GD, nội dung | Skill B | COMP:receipt-preview-1 | Pass | Từ ảnh: 6 rows detail visible (thời gian, tên, thẻ, NH, mã GD, nội dung) |
| 5 | Actions: Chia sẻ + Lưu ảnh | Skill C | COMP:receipt-preview-1 | Pass | Từ ảnh: 2 icon actions "Chia sẻ" và "Lưu ảnh" dưới receipt |
| 6 | CTA "Tạo giao dịch mới" | Skill C | — | Pass | Từ ảnh: nút xanh navy full-width ở footer |
| 7 | Logo Co-opBank trên receipt | Skill C | — | Pass | Từ ảnh: logo Co-opBank đỏ ở top receipt card |
| 8 | Name casing consistency (uppercase) | Skill C | UXG-181 | Gap | Từ ảnh CTNST_6: "nguyen tung" lowercase vs CTNST_4: "NGUYEN TUNG" uppercase |
| 9 | Bank name text wrapping | Skill C | COMP:receipt-preview-1 | Gap | Từ ảnh: "BIDV - Ngân hàng đầu tư và phát triển Việt Nam" wraps 3 lines trên receipt |
| 10 | Mã giao dịch format chuẩn | Skill B | COMP:receipt-preview-1 | Gap | "0982312" — 7 chars, thiếu prefix, format không chuẩn banking |
| 11 | Timestamp format rõ ràng | Skill C | — | Unverifiable | "22:00 15/02/2020" — không rõ timezone, nhưng có thể server-side logic |
| 12 | Peak-End Rule: positive ending experience | Skill A | — | Pass | Từ ảnh: checkmark xanh, text "thành công", card design đẹp, share/save options |
| 13 | Error/failure state variant | Skill B | UXG-180 | Gap | Không có variant hiển thị giao dịch thất bại |

---

## DDL References sử dụng
| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| COMP:otp-input-1 | OTP/PIN input with auto-focus, paste support, resend timer | doherty | SCR-THE-002: OTP overlay |
| COMP:text-input-1 | Enhanced text input with error state, validation | — | SCR-THE-001: Form fields |
| COMP:app-header-1 | Mobile app header with back button, title | — | SCR-THE-001, 002, 003: Headers |
| COMP:receipt-preview-1 | Receipt preview with paper-style layout, share/print | peak-end | SCR-THE-003: Receipt card |
| COMP:empty-state-1 | Empty state with icon, title, description, CTA | — | SCR-THE-001: Beneficiary search |
| UXG-235 | Form field completeness and CTA clarity | — | All screens |
| UXG-180 | Error handling and validation feedback | — | SCR-THE-001, 002 |
| UXG-181 | Text formatting consistency | — | SCR-THE-001, 003 |
| UXG-183 | Confirmation screen consistency | — | SCR-THE-002 |
| UXG-184 | Empty state and search guidance | hick | SCR-THE-001 |
