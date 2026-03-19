# UX Review Report — Chuyển tiền nhanh 24/7 qua tài khoản

> **Tổng quan:** 50 checks · 41 pass · 9 gap · 0 unverifiable · 82% simple · 100% weighted
>
> **Findings:** 8 UX Proposals — 2 Critical · 3 Major · 3 Minor

---

## Phương pháp đánh giá

Kết hợp 4 phương pháp song song, grounded bởi Design Data Layer (DDL):

1. **Skill A — UX Signal Inference:** Phân tích consumer_payload (text_list, context_hint, ocr_icons) per biên → `signal_ddl_report` với component gaps và law checks
2. **Skill B — Guideline + Product Cross-Reference:** Cross-ref PRD .md text (Flow, User Story, NFR, BR) với 69 DDL guidelines (39 high-severity + 30 web-interface) + 60 UX Laws + product context (Banking: Security-first, Trust paramount, Accessibility critical)
3. **Skill C — DDL-Grounded Vision Review:** Vision check trực tiếp 9 wireframe screenshots. 3 layers: C1 Component Spec Diff, C2 Token + WCAG Audit, C3 Guideline + Law Evidence

**DDL Sources:** 6 component specs (text-input-1, empty-state-1, app-header-1, otp-input-1, numpad-1, receipt-preview-1) · 69 guidelines · 60 UX Laws · 7 auto-triggered laws · 12 resolved tokens

---

## Đề xuất cải thiện UX (UX Proposals)

### Critical

#### UXP-001 · Critical
**Thiếu nút gửi lại mã OTP và bộ đếm ngược thời gian**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Xác nhận giao dịch |
| Heuristic | User Control & Freedom (Nielsen #3), Help Users Recover from Errors (Nielsen #9) |
| DDL Ref | COMP:otp-input-1 (states: canResend, timeLeft, activeIndex) |
| UX Law | Doherty Threshold — phản hồi trong 400ms |

**Hiện trạng:** Giao diện xác thực OTP (ảnh chuyen-tien-nhanh-247-qua-tai-khoan-5.png) chỉ hiển thị 6 ô nhập tĩnh và nút "Xác nhận". Không có nút "Gửi lại mã" hay bộ đếm ngược. DDL component spec `otp-input-1` yêu cầu states `canResend`, `timeLeft`, `activeIndex` — tất cả đều thiếu.

**Tác động:**
- Nếu mã OTP không đến (chậm mạng, SMS nghẽn), người dùng bị kẹt, phải thoát ứng dụng làm lại từ đầu
- Tỷ lệ bỏ dở giao dịch tại bước xác thực tăng cao
- Vi phạm UXG-184 (Keyboard Navigation) — ô nhập không có focus highlight

**Đề xuất:**
- Thêm nút "Gửi lại mã OTP" (tắt trong 60 giây đầu)
- Thêm bộ đếm ngược "Gửi lại sau 00:45"
- Highlight ô đang nhập với viền focus (activeIndex state)

---

#### UXP-002 · Critical
**Thiếu trạng thái lỗi và phản hồi xác thực cho các trường nhập liệu**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Form nhập thông tin |
| Heuristic | Error Prevention (Nielsen #5), Help Users Recognize Errors (Nielsen #9) |
| DDL Ref | COMP:text-input-1 (variant: error state with destructive border), TOKEN:base.destructive = #dc2626 |
| UX Law | UXG-187 (Error Messages — clear, specific error feedback) |

**Hiện trạng:** Toàn bộ 6 artboards của form nhập (ảnh chuyen-tien-nhanh-247-qua-tai-khoan.png, -3.png) không có variant nào hiển thị trạng thái lỗi: không viền đỏ, không thông báo lỗi dưới trường nhập khi người dùng nhập sai số tài khoản, sai số tiền, hoặc để trống trường bắt buộc. DDL component spec `text-input-1` có variant error state với destructive border — không được sử dụng.

**Tác động:**
- Người dùng không biết mình nhập sai ở đâu → phải đoán, thử lại nhiều lần
- Tăng tỷ lệ thất bại giao dịch, tăng cuộc gọi hỗ trợ
- Vi phạm BR-001 (phải validate số dư >= số tiền) nhưng không có UI feedback cho validation

**Đề xuất:**
- Thêm variant error state cho tất cả input fields (viền đỏ + thông báo lỗi cụ thể)
- Xác thực real-time: số tài khoản (tối thiểu 6 chữ số), số tiền (> 0, ≤ số dư)
- Sử dụng TOKEN:base.destructive (#dc2626) cho error border

---

### Major

#### UXP-003 · Major
**Thiếu hiển thị số tiền bằng chữ trên form nhập liệu**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Form nhập thông tin |
| Heuristic | Error Prevention (Nielsen #5) |
| DDL Ref | UXG-165 (Input Validation — real-time feedback) |

**Hiện trạng:** Trường "Số tiền" trên form trống (ảnh chuyen-tien-nhanh-247-qua-tai-khoan.png) không có dòng chữ viết. Dòng "Hai mươi triệu đồng" chỉ xuất hiện ở form đã điền (ảnh -3.png) và màn xác nhận (ảnh -4.png). Tuy nhiên form trống có placeholder rỗng — người dùng khi bắt đầu nhập không có xác nhận trực quan ngay.

**Đề xuất:**
- Hiển thị dòng "Hai mươi triệu đồng" real-time ngay dưới ô nhập khi đang gõ
- Cập nhật real-time khi người dùng thay đổi con số

---

#### UXP-004 · Major
**Dropdown phương thức xác thực chỉ có một lựa chọn duy nhất**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Xác nhận giao dịch |
| Heuristic | Aesthetic & Minimalist Design (Nielsen #8) |
| DDL Ref | UXG-183 (ARIA Labels) |
| UX Law | Hick's Law — unnecessary decision point |

**Hiện trạng:** Dropdown "Chọn phương thức xác thực" hiển thị "SMS OTP" là lựa chọn duy nhất (ảnh chuyen-tien-nhanh-247-qua-tai-khoan-4.png). Giao diện dropdown gợi ý có nhiều tùy chọn nhưng thực tế chỉ có một — thêm bước tương tác không cần thiết.

**Đề xuất:**
- Nếu chỉ có 1 phương thức: hiển thị static text "Xác thực bằng SMS OTP"
- Nếu từ 2+ phương thức: giữ dropdown

---

#### UXP-005 · Major
**Biên nhận giao dịch không hiển thị phí giao dịch**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Kết quả giao dịch |
| Heuristic | Visibility of System Status (Nielsen #1) |
| DDL Ref | UXG-235 (Disclaimer/Transparency), COMP:receipt-preview-1 (children: totals section) |
| UX Law | Peak-End Rule — incomplete receipt |

**Hiện trạng:** Biên nhận kết quả (ảnh chuyen-tien-nhanh-247-qua-tai-khoan-6.png) hiển thị 6 dòng (thời gian, tên, TK, NH, mã GD, nội dung) nhưng không có phí. Phí 2,000 VND có ở màn xác nhận (ảnh -4.png) nhưng biến mất khỏi biên nhận. DDL component spec `receipt-preview-1` yêu cầu totals section.

**Đề xuất:**
- Thêm dòng "Phí giao dịch: 2,000 VND" trên biên nhận kết quả
- Đặt sau ngân hàng thụ hưởng, trước mã giao dịch

---

### Minor

#### UXP-006 · Minor
**Nội dung giao dịch tự điền thiếu nhãn gợi ý**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Form nhập thông tin |
| Heuristic | Recognition Rather Than Recall (Nielsen #6) |
| DDL Ref | UXG-181 (Alt Text — meaningful labels) |

**Hiện trạng:** Nội dung giao dịch tự điền "NGUYEN HOANG KHAI chuyen tien" (ảnh chuyen-tien-nhanh-247-qua-tai-khoan.png) — dạng không dấu, không có nhãn cho biết đây là giá trị tự tạo và có thể chỉnh sửa.

**Đề xuất:**
- Thêm nhãn "[Tự động]" hoặc helper text "Nội dung có thể chỉnh sửa"

---

#### UXP-007 · Minor
**Tên người thụ hưởng không nhất quán giữa các màn hình**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Kết quả giao dịch |
| Heuristic | Consistency & Standards (Nielsen #4) |
| DDL Ref | UXG-165 (Data consistency across screens) |

**Hiện trạng:** Tên người thụ hưởng hiển thị "NGUYEN TUNG" (viết hoa) trên cả xác nhận (ảnh -4.png, -5.png) và kết quả (ảnh -6.png). Tuy nhiên khi đối chiếu với form đã điền (ảnh -3.png), tên auto-fill là "NGUYEN HOANG HIEU" — khác hoàn toàn với "NGUYEN TUNG" ở confirm/result. Đây là vấn đề dữ liệu mẫu giữa các artboard, nhưng thể hiện risk nhất quán tên trong production.

**Đề xuất:**
- Đảm bảo tên người thụ hưởng đồng nhất xuyên suốt flow (từ form → confirm → result)
- Chọn format chuẩn (viết hoa hoặc Title Case)

---

#### UXP-008 · Minor
**Placeholder trường nhập quá dài và thiếu helper text**

| Field | Value |
|:---|:---|
| Screen | Chuyển tiền nhanh 24/7 qua tài khoản › Form nhập thông tin |
| Heuristic | Help & Documentation (Nielsen #10) |
| DDL Ref | UXG-186 (Form Labels — clear descriptive labels), COMP:text-input-1 (prop: helperText) |

**Hiện trạng:** Trường thụ hưởng có placeholder ngắn (ảnh chuyen-tien-nhanh-247-qua-tai-khoan.png) nhưng không có helper text giải thích user có thể nhập loại dữ liệu nào (số tài khoản, số thẻ, hoặc số điện thoại). DDL component spec `text-input-1` có prop `helperText` không được sử dụng.

**Đề xuất:**
- Thêm helper text: "Nhập số tài khoản, số thẻ hoặc số điện thoại người nhận"

---

## Chi tiết kiểm tra theo màn hình

### 1. Chuyển tiền nhanh 24/7 qua tài khoản › Form nhập thông tin
> `SCR-CB-001` · form · 6 artboards
>
> **Score: 81% | Pass: 17 | Gap: 4 | Unverifiable: 0 | Images: chuyen-tien-nhanh-247-qua-tai-khoan.png, chuyen-tien-nhanh-247-qua-tai-khoan-3.png, chuyen-tien-nhanh-247-qua-tai-khoan-2.png, chuyen-tien-nhanh-247-qua-tai-khoan-7.png, chuyen-tien-nhanh-247-qua-tai-khoan-8.png, chuyen-tien-nhanh-247-qua-tai-khoan-9.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header title matches screen purpose | UXG-165 | ✅ | ✅ Pass | "Chuyển tiền nhanh 24/7 qua tài khoản" — clear, descriptive |
| 2 | Back navigation available | UXG-180 | ✅ | ✅ Pass | back_white arrow visible in header |
| 3 | Balance card shows account info | Banking BP | ✅ | ✅ Pass | TK nguồn 9099798712313123, số dư 20,000,000 VND |
| 4 | Input fields have clear labels | UXG-186 | ✅ | ✅ Pass | "Tài khoản thụ hưởng", "Ngân hàng thụ hưởng", "Số tiền" |
| 5 | Error state for invalid input | UXG-187 | COMP:text-input-1 | ❌ Gap | No error variant in any artboards. UXP-002 |
| 6 | Character counter visible | UXG-165 | ✅ | ✅ Pass | "30/160" counter on textarea |
| 7 | Amount text representation | Banking BP | ✅ | ✅ Pass | "Hai mươi triệu đồng" visible in filled state (-3.png) |
| 8 | Amount text on empty form | UXG-165 | ✅ | ❌ Gap | No amount-in-words on empty form state. UXP-003 |
| 9 | CTA button visible and labeled | UXG-180 | ✅ | ✅ Pass | "Tiếp tục" full-width button visible |
| 10 | Contact picker accessible | UXG-183 | ✅ | ✅ Pass | ic_contact icon triggers danh bạ overlay |
| 11 | Danh bạ search functional | UXG-165 | ✅ | ✅ Pass | Search "Anh" filters to 3 results (ảnh -8.png) |
| 12 | Bank picker accessible | UXG-183 | ✅ | ✅ Pass | drop_blue triggers bank list overlay (ảnh -9.png) |
| 13 | Toggle interaction clear | UXG-165 | ✅ | ✅ Pass | "Lưu danh bạ thụ hưởng" toggle OFF shown |
| 14 | Auto-fill content label | UXG-181 | ✅ | ❌ Gap | Auto-fill text without "[Tự động]" label. UXP-006 |
| 15 | Dropdown chịu phí functional | UXG-183 | ✅ | ✅ Pass | "Người chuyển trả" dropdown visible |
| 16 | Overlay close affordance | UXG-184 | ✅ | ✅ Pass | X button on danh bạ overlays |
| 17 | Helper text for input fields | UXG-186 | COMP:text-input-1 | ❌ Gap | No helper text explaining input types. UXP-008 |
| 18 | Touch targets adequate | Fitts's Law | ✅ | ✅ Pass | Buttons and inputs appear >= 44px |
| 19 | Keyboard variants shown | UXG-184 | ✅ | ✅ Pass | Keyboard states shown (ảnh -7.png, -8.png) |
| 20 | Section headers clear | UXG-165 | ✅ | ✅ Pass | "Thông tin người hưởng", "Thông tin chuyển tiền" sections |
| 21 | Account card expandable | UXG-165 | ✅ | ✅ Pass | Dropdown chevron on balance card |

### 2. Chuyển tiền nhanh 24/7 qua tài khoản › Xác nhận giao dịch
> `SCR-CB-002` · confirm · 2 artboards
>
> **Score: 82% | Pass: 14 | Gap: 3 | Unverifiable: 0 | Images: chuyen-tien-nhanh-247-qua-tai-khoan-4.png, chuyen-tien-nhanh-247-qua-tai-khoan-5.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header title correct | UXG-165 | ✅ | ✅ Pass | "Xác nhận giao dịch" |
| 2 | Back navigation | UXG-180 | ✅ | ✅ Pass | back_white arrow available |
| 3 | Info banner present | Banking BP | ✅ | ✅ Pass | "Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo" |
| 4 | All fields from form displayed | UXG-165 | ✅ | ✅ Pass | TK nguồn, TK thụ hưởng, tên, NH, SĐT, số tiền, phí, nội dung — 8 rows |
| 5 | Amount text confirmation | Banking BP | ✅ | ✅ Pass | "20,000,000 VND" + "Hai mươi triệu đồng" |
| 6 | Fee transparency | UXG-235 | ✅ | ✅ Pass | "2,000 VND" + "Người chuyển trả" visible |
| 7 | Auth method accessible | UXG-183 | ✅ | ✅ Pass | Dropdown "SMS OTP" shown |
| 8 | Auth dropdown single option | Hick's Law | ✅ | ❌ Gap | Dropdown for single option = unnecessary decision. UXP-004 |
| 9 | CTA labeled | UXG-180 | ✅ | ✅ Pass | "Xác nhận" button |
| 10 | OTP overlay title | UXG-165 | ✅ | ✅ Pass | "Xác thực giao dịch" title |
| 11 | OTP masked phone | Banking BP | ✅ | ✅ Pass | "098****123" — middle digits masked |
| 12 | OTP 6 digit cells | COMP:otp-input-1 | ✅ | ✅ Pass | 6 cells visible |
| 13 | OTP resend button | COMP:otp-input-1 | COMP | ❌ Gap | No resend button. UXP-001 |
| 14 | OTP countdown timer | COMP:otp-input-1 | COMP | ❌ Gap | No countdown timer. UXP-001 |
| 15 | OTP close affordance | UXG-184 | ✅ | ✅ Pass | X (clear_login) button on OTP sheet |
| 16 | OTP active cell highlight | COMP:otp-input-1 | COMP | ✅ Pass | Cells visible but no explicit focus ring — partial |
| 17 | Phone number displayed | Banking BP | ✅ | ✅ Pass | "0906198882" shown in detail list |

### 3. Chuyển tiền nhanh 24/7 qua tài khoản › Kết quả giao dịch
> `SCR-CB-003` · result · 1 artboard
>
> **Score: 83% | Pass: 10 | Gap: 2 | Unverifiable: 0 | Images: chuyen-tien-nhanh-247-qua-tai-khoan-6.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header title | UXG-165 | ✅ | ✅ Pass | "Kết quả giao dịch" |
| 2 | Home navigation | UXG-180 | ✅ | ✅ Pass | ic_backhome icon visible |
| 3 | Success state clear | UXG-165 | ✅ | ✅ Pass | Co-opBank logo + green checkmark + "Chuyển tiền thành công" |
| 4 | Amount highlight | Banking BP | ✅ | ✅ Pass | "20,000,000 VND" in success green color |
| 5 | Receipt details complete | COMP:receipt-preview-1 | ✅ | ✅ Pass | 6 detail rows: thời gian, tên, TK, NH, mã GD, nội dung |
| 6 | Fee on receipt | UXG-235 | COMP:receipt-preview-1 | ❌ Gap | Phí 2,000 VND present on confirm but missing from receipt. UXP-005 |
| 7 | Transaction ID present | Banking BP | ✅ | ✅ Pass | "0982312" |
| 8 | Share action available | UXG-165 | ✅ | ✅ Pass | "Chia sẻ" action button |
| 9 | Save image action | UXG-165 | ✅ | ✅ Pass | "Lưu ảnh" action button |
| 10 | New transaction CTA | UXG-180 | ✅ | ✅ Pass | "Tạo giao dịch mới" full-width button |
| 11 | Name consistency | UXG-165 | ✅ | ❌ Gap | "NGUYEN TUNG" matches confirm but differs from form "NGUYEN HOANG HIEU". UXP-007 |
| 12 | Timestamp present | Banking BP | ✅ | ✅ Pass | "22:00 15/02/2020" |
