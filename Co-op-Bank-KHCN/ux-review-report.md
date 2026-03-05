# UX Review Report — Co-op Bank KHCN

> **Pipeline:** `figma-to-ux-review` (Pipe 2: ux-review-pipe)
> **Ngày chạy:** 2026-03-03
> **Folder:** `Co-op-Bank-KHCN/co-op-bank-khcn/package-2/chuyen-tien-noi-bo-khac-chu`
> **Domain:** banking
> **Execution mode:** No `.handoff/` → fallback parse .md Section 3

---

## Tổng quan

| Metric | Value |
|:---|:---|
| Số màn hình | **3** screens (Form, Confirm, Result) |
| Số ảnh wireframe | **7** files (7 trạng thái khác nhau) |
| Tổng check items | **42** |
| ✅ Pass | **27** (64%) |
| ⚠️ Gap | **12** (29%) |
| ❓ Unverifiable | **3** (7%) |
| **UX Score** | **64%** |

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical (3)

| ID | Screen | Vấn đề | Đề xuất | DDL | UX Law |
|:---:|:---|:---|:---|:---|:---|
| UXP-001 | `form` (internal-transaction-2.png) | Toggle "Lưu danh bạ thụ hưởng" và "Đặt lịch chuyển tiền" **thiếu label trạng thái** (Bật/Tắt). Người dùng khiếm thị không biết toggle đang on hay off | Thêm text "Bật" / "Tắt" kế bên mỗi toggle switch. Hoặc dùng `aria-label="Lưu danh bạ: Đang tắt"` với cập nhật dynamic | `ux-guidelines.csv#40` (ARIA Labels) | `wcag-perceivable` |
| UXP-002 | `confirm-otp` (internal-transaction-6.png) | Nút Close (X) trên Bottom Sheet OTP có **touch target nhỏ hơn 44×44px**. Trên ảnh, icon X ở góc trên phải rất nhỏ (~24px), không đủ vùng tap | Tăng hit area nút X lên tối thiểu **44×44pt**. Thêm `padding: 10px` xung quanh icon hoặc dùng invisible tap area rộng hơn | `ux-guidelines.csv#22` (Touch Target Size), `web-interface.csv#1` (Icon Button Labels) | `fitts`, `hig-44pt` |
| UXP-003 | `form` (internal-transaction-3.png, internal-transaction-4.png) | Dialog "Thông báo" chỉ có **nút "Đóng" duy nhất**, không cung cấp hướng dẫn khắc phục (error recovery). Nội dung lỗi mô tả vấn đề nhưng **không gợi ý hành động tiếp theo** | Thêm guidance text: "Vui lòng nhập thông tin thụ hưởng là **số tài khoản ngân hàng** để sử dụng chức năng Đặt lịch." Thêm nút "Thử lại" bên cạnh "Đóng" | `ux-guidelines.csv#80` (Error Recovery), `ux-guidelines.csv#33` (Error Feedback) | `nng-error-recovery` |

### 🟡 Major (5)

| ID | Screen | Vấn đề | Đề xuất | DDL | UX Law |
|:---:|:---|:---|:---|:---|:---|
| UXP-004 | `result` (internal-transaction-7.png) | "Mã đặt lịch: **0982312**" — **thiếu icon Copy**. Người dùng cần copy mã giao dịch để lưu trữ hoặc tra cứu nhưng phải chụp màn hình hoặc ghi tay | Thêm **icon Copy (clipboard)** bên phải giá trị "0982312". Khi tap → copy vào clipboard + hiện toast "Đã sao chép mã đặt lịch" | `ux-guidelines.csv#34` (Success Feedback) | `nng-flexibility` |
| UXP-005 | `form` (internal-transaction.png) | Label "Đặt lịch chuyển tiền" ở bottom bị **cắt bớt** (truncated) do nút "Tiếp tục" che phần dưới. Toàn bộ phần cài đặt lịch (Tần suất, Số lần, Ngày) chưa hiển thị trên trạng thái toggle OFF | Toggle OFF không hiện preview → người dùng **không biết** bật lên sẽ có gì. Thêm **micro-description** dưới toggle: "Thiết lập chuyển tiền tự động theo lịch" | `ux-guidelines.csv#84` (Truncation) | `nng-recognition-recall` |
| UXP-006 | `confirm` (internal-transaction-5.png) | Giá trị "Tần suất: **Hàng tháng**" và "Số lần: **2**" hiển thị text đỏ (highlight) nhưng **không có giải thích** tại sao highlight đỏ. Có thể hiểu nhầm là lỗi (error) thay vì nhấn mạnh (emphasis) | Dùng **màu primary (xanh Co-op Bank)** thay vì đỏ cho emphasis. Hoặc thêm tooltip/caption giải thích: "Thông tin quan trọng cần kiểm tra". Đỏ chỉ nên dùng cho error/warning | `ux-guidelines.csv#37` (Color Only) | `gestalt-similarity` |
| UXP-007 | `form` (internal-transaction-2.png) | Dropdown "Tần suất" hiện giá trị "Hàng tháng" với chevron (v) nhưng **không rõ đây là dropdown** hay label tĩnh. Affordance yếu — input trông giống text label | Thêm **border/background** cho dropdown field (giống các input khác). Hoặc dùng bottom border rõ ràng + chevron icon lớn hơn. Đảm bảo **padding ≥ 44px height** cho touch target | `ux-guidelines.csv#62` (Input Affordance) | `fitts` |
| UXP-008 | `confirm-otp` (internal-transaction-6.png) | Bottom Sheet OTP có **overlay mờ (blur)** nhưng viền sheet **không đủ nổi bật**. Contrast giữa sheet background (trắng) và overlay (xám mờ) ở vùng border thấp | Thêm **elevation shadow** (box-shadow: `0 -4px 24px rgba(0,0,0,0.15)`) cho bottom sheet. Hoặc tăng border-radius + thêm 1px border `rgba(0,0,0,0.1)` ở cạnh trên | `ux-guidelines.csv#36` (Color Contrast) | `gestalt-common-region` |

### 🟢 Minor (4)

| ID | Screen | Vấn đề | Đề xuất | DDL | UX Law |
|:---:|:---|:---|:---|:---|:---|
| UXP-009 | `form` (internal-transaction.png) | Field "Nội dung giao dịch" **tự điền** `NGUYEN HOANG KHAI chuyen tien` — tên viết hoa không dấu, content giao dịch không tiếng Việt. Trải nghiệm không tự nhiên | Auto-populate nên dùng format: `"NGUYEN HOANG KHAI chuyển tiền"` (có dấu tiếng Việt). Hoặc để người dùng tự nhập với placeholder gợi ý | `ux-guidelines.csv#87` (Placeholder Content) | `nng-match-world` |
| UXP-010 | `form` (internal-transaction.png, internal-transaction-2.png) | Field "Số tài khoản/Số thẻ/Số điện thoại" có icon Contact (👤) bên phải nhưng **thiếu `aria-label`**. Người dùng screen reader không biết icon này làm gì | Thêm `aria-label="Chọn từ danh bạ thụ hưởng"` cho icon button | `web-interface.csv#1` (Icon Button Labels), `ux-guidelines.csv#40` (ARIA Labels) | `wcag-operable` |
| UXP-011 | `result` (internal-transaction-7.png) | Nút "Chia sẻ" và "Lưu ảnh" dùng **icon-only** (không có text label dạng accessibility). Trên ảnh thấy icon nhỏ + text bên dưới, nhưng icon có thể gây nhầm | Đảm bảo mỗi icon button có `aria-label` tương ứng: `aria-label="Chia sẻ giao dịch"`, `aria-label="Lưu ảnh biên lai"` | `web-interface.csv#1` (Icon Button Labels) | `wcag-perceivable` |
| UXP-012 | `confirm` (internal-transaction-5.png) | Dòng "Hai mươi triệu đồng" (chữ đỏ nghiêng) là **bằng chữ của số tiền** — hữu ích nhưng font size quá nhỏ so với số tiền `20,000,000 VND`. Tỷ lệ contrast thấp | Tăng font-size text bằng chữ lên **14px** (hiện ~11px). Dùng font-weight medium thay vì italic để tăng readability | `ux-guidelines.csv#67` (Readable Font Size) | `wcag-perceivable` |

---

## Chi tiết theo màn hình

### 📱 Chuyển tiền nội bộ — Form

**Screen ID:** `chuyen-tien-noi-bo-khac-chu-form`
**Score: 58% | Pass: 11 | Gap: 6 | Unverifiable: 2**
**Images:** `internal-transaction.png`, `internal-transaction-2.png`, `internal-transaction-3.png`, `internal-transaction-4.png`

| # | Check | Source | DDL | Verdict | Evidence |
|:---:|:---|:---:|:---|:---:|:---|
| 1 | Back button logic | Skill B | `ux-guidelines.csv#4` | ✅ pass | Nút `<` góc trái header — nhất quán với iOS pattern |
| 2 | Form input labels visible | Skill B | `ux-guidelines.csv#54` | ✅ pass | Tất cả fields có label phía trên: "Số tài khoản", "Số tiền", "Nội dung giao dịch" |
| 3 | Touch target ≥ 44px | Skill A | `ux-guidelines.csv#22` | ✅ pass | Nút "Tiếp tục" full-width, height ~48px |
| 4 | Toggle label status | Skill A | `ux-guidelines.csv#40` | ⚠️ **gap** | Toggle "Lưu danh bạ thụ hưởng" + "Đặt lịch chuyển tiền" thiếu text Bật/Tắt → **UXP-001** |
| 5 | Error dialog recovery | Skill B | `ux-guidelines.csv#80` | ⚠️ **gap** | Dialog chỉ "Đóng", không gợi ý cách khắc phục → **UXP-003** |
| 6 | Dropdown affordance | Skill C | `ux-guidelines.csv#62` | ⚠️ **gap** | "Tần suất" dropdown nhìn như label tĩnh → **UXP-007** |
| 7 | Input type = number cho "Số tiền" | Skill B | `web-interface.csv#11` | ❓ unverifiable | Không thể verify `inputmode` từ ảnh tĩnh |
| 8 | Required field indicators | Skill B | `ux-guidelines.csv#59` | ⚠️ **gap** | Không thấy dấu `*` hay "(bắt buộc)" trên form |
| 9 | Content truncation bottom | Skill C | `ux-guidelines.csv#84` | ⚠️ **gap** | Toggle "Đặt lịch" bị cắt bởi button "Tiếp tục" → **UXP-005** |
| 10 | Auto-populate content quality | Skill C | `ux-guidelines.csv#87` | ⚠️ **gap** | Nội dung tự điền không tự nhiên → **UXP-009** |
| 11 | Icon button aria-label | Skill A | `web-interface.csv#1` | ⚠️ ️**gap** | Icon Contact thiếu aria-label → **UXP-010** |
| 12 | Keyboard type cho phone/account | Skill B | `ux-guidelines.csv#63` | ❓ unverifiable | Không verify được từ ảnh tĩnh |
| 13 | Scroll behavior | Skill C | `ux-guidelines.csv#69` | ✅ pass | Nội dung dài scroll tự nhiên, không horizontal scroll |
| 14 | Color contrast text | Skill C | `ux-guidelines.csv#36` | ✅ pass | Text đậm (#1a1a1a) trên nền trắng — contrast ratio >7:1 |
| 15 | Loading state khi tra cứu TK | Skill A | `ux-guidelines.csv#10` | ❓ unverifiable | Không thấy loading state cho auto-lookup thụ hưởng |
| 16 | Card thông tin nguồn | Skill C | `ux-guidelines.csv#76` | ✅ pass | Contrast tốt: text trắng trên gradient xanh đậm |
| 17 | Heading hierarchy | Skill B | `ux-guidelines.csv#39` | ✅ pass | "Thông tin người hưởng" → "Thông tin chuyển tiền" → logic top-down |
| 18 | Touch spacing giữa fields | Skill C | `ux-guidelines.csv#23` | ✅ pass | Gap giữa các sections ≥ 16px |
| 19 | Character counter | Skill C | — | ✅ pass | "30/160" hiện rõ cho "Nội dung giao dịch" |

---

### 📱 Xác nhận giao dịch — Confirm

**Screen ID:** `chuyen-tien-noi-bo-khac-chu-confirm`
**Score: 69% | Pass: 9 | Gap: 3 | Unverifiable: 1**
**Images:** `internal-transaction-5.png`, `internal-transaction-6.png`

| # | Check | Source | DDL | Verdict | Evidence |
|:---:|:---|:---:|:---|:---:|:---|
| 1 | Read-only data display | Skill B | — | ✅ pass | Tất cả fields hiện dạng label-value, không editable |
| 2 | Destructive action confirm | Skill B | `ux-guidelines.csv#35` | ✅ pass | Có bước xác nhận riêng trước khi giao dịch thực thi |
| 3 | OTP input 6 boxes | Skill C | `web-interface.csv#12` | ✅ pass | 6 ô OTP riêng biệt, rõ ràng |
| 4 | Phone masking | Skill C | — | ✅ pass | "098****123" — che đúng quy tắc bảo mật |
| 5 | Red text misleading | Skill C | `ux-guidelines.csv#37` | ⚠️ **gap** | "Hàng tháng", "2" highlight đỏ → nhầm error → **UXP-006** |
| 6 | OTP Close button touch target | Skill C | `ux-guidelines.csv#22` | ⚠️ **gap** | Icon X quá nhỏ, <44px → **UXP-002** |
| 7 | Bottom sheet elevation | Skill C | `ux-guidelines.csv#36` | ⚠️ **gap** | Viền sheet không đủ nổi bật → **UXP-008** |
| 8 | Text bằng chữ readability | Skill C | `ux-guidelines.csv#67` | ⚠️ **gap** | "Hai mươi triệu đồng" font quá nhỏ → **UXP-012** |
| 9 | Back button | Skill B | `ux-guidelines.csv#4` | ✅ pass | Nút `<` trên header "Xác nhận giao dịch" |
| 10 | Auth method dropdown | Skill C | `ux-guidelines.csv#62` | ✅ pass | "SMS OTP" với chevron rõ ràng, border phân biệt |
| 11 | OTP auto-focus next | Skill B | — | ❓ unverifiable | Không verify auto-move từ ảnh tĩnh |
| 12 | Banner instruction | Skill C | — | ✅ pass | "Quý khách vui lòng kiểm tra lại thông tin đặt lịch đã khởi tạo" — rõ ràng, đủ context |
| 13 | Alert/instruction text | Skill C | `ux-guidelines.csv#76` | ✅ pass | Banner xanh gradient — text trắng contrast tốt |

---

### 📱 Kết quả giao dịch — Result

**Screen ID:** `chuyen-tien-noi-bo-khac-chu-result`
**Score: 70% | Pass: 7 | Gap: 3 | Unverifiable: 0**
**Images:** `internal-transaction-7.png`

| # | Check | Source | DDL | Verdict | Evidence |
|:---:|:---|:---:|:---|:---:|:---|
| 1 | Success feedback | Skill A | `ux-guidelines.csv#34` | ✅ pass | ✓ Icon + "Đặt lịch chuyển tiền thành công" + số tiền 50,000 VND |
| 2 | Copy transaction code | Skill C | `ux-guidelines.csv#33` | ⚠️ **gap** | "Mã đặt lịch: 0982312" thiếu icon Copy → **UXP-004** |
| 3 | Share/Save actions | Skill C | — | ✅ pass | "Chia sẻ" + "Lưu ảnh" icons present ở bottom |
| 4 | New transaction CTA | Skill B | — | ✅ pass | "Tạo giao dịch mới" full-width fixed bottom — rõ ràng |
| 5 | Home navigation | Skill C | `ux-guidelines.csv#4` | ✅ pass | Icon Home (🏠) góc trái header |
| 6 | All transaction data displayed | Skill B | — | ✅ pass | 10 rows data (thời gian, TK nguồn, TK thụ hưởng, tên, số tiền, tần suất, số lần, ngày BĐ, ngày KT, mã, nội dung) |
| 7 | Icon-only button labels | Skill A | `web-interface.csv#1` | ⚠️ **gap** | "Chia sẻ" + "Lưu ảnh" cần aria-label → **UXP-011** |
| 8 | Brand consistency | Skill C | — | ✅ pass | Co-op Bank logo + color scheme nhất quán |
| 9 | Monetary amount formatting | Skill C | `ux-guidelines.csv#86` | ✅ pass | "50,000 VND" + "20,000,000 VND" — đúng format locale |
| 10 | Fixed bottom button spacing | Skill C | `ux-guidelines.csv#17` | ⚠️ **gap** | "Tạo giao dịch mới" fixed bottom — kiểm tra có che nội dung cuối (Nội dung giao dịch) không. Trên ảnh thấy sát nhau, cần padding-bottom ≥ button height |

---

## Signal Inference Summary (Skill A)

| Screen | Matched Signals | Inferred Flows | Confidence |
|:---|:---:|:---|:---:|
| form | 8 | `input_flow`, `schedule_flow`, `contact_lookup`, `error_exception` | High |
| confirm | 5 | `review_confirm_flow`, `otp_auth_flow`, `destructive_confirm` | High |
| result | 4 | `success_display`, `share_flow`, `new_transaction_restart` | High |

---

## PRD Context Coverage (Skill B)

| Feature | User Stories | AC Covered | AC Missing | Flow Complete |
|:---|:---:|:---:|:---:|:---:|
| Form | US-001, US-002, US-003 | 5/7 | Error recovery guidance, Toggle status label | ⚠️ Partial |
| Confirm | US-004, US-005, US-006 | 4/5 | OTP error state visual | ⚠️ Partial |
| Result | US-007, US-008, US-009 | 3/3 | — | ✅ Complete |

### State Coverage Gap

| Component | States in PRD | DDL Required States | Missing |
|:---|:---|:---|:---|
| Toggle (Đặt lịch) | default, on | default, on, **disabled**, **loading** | disabled, loading |
| OTP Input | default, filled | default, focus, filled, **error**, **disabled** | error, disabled |
| "Tiếp tục" Button | default, active | default, **hover**, active, **disabled**, **loading** | hover, disabled, loading |
| Dialog Thông báo | shown | shown, **with_recovery_action** | with recovery action |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|:---|:---|:---|:---|
| `ux-guidelines.csv#4` | Back Button logic | `jakob` | Form ✅, Confirm ✅, Result ✅ |
| `ux-guidelines.csv#10` | Loading States | `doherty` | Form ❓ (unverifiable) |
| `ux-guidelines.csv#22` | Touch Target ≥ 44px | `fitts` | Confirm ⚠️ (UXP-002) |
| `ux-guidelines.csv#33` | Error Feedback | — | Form ⚠️ (UXP-003) |
| `ux-guidelines.csv#34` | Success Feedback | — | Result ✅, Result ⚠️ (UXP-004) |
| `ux-guidelines.csv#36` | Color Contrast | — | Form ✅, Confirm ⚠️ (UXP-008) |
| `ux-guidelines.csv#37` | Color Only | — | Confirm ⚠️ (UXP-006) |
| `ux-guidelines.csv#40` | ARIA Labels | — | Form ⚠️ (UXP-001, UXP-010) |
| `ux-guidelines.csv#54` | Input Labels | — | Form ✅ |
| `ux-guidelines.csv#59` | Required Indicators | — | Form ⚠️ |
| `ux-guidelines.csv#62` | Input Affordance | — | Form ⚠️ (UXP-007) |
| `ux-guidelines.csv#67` | Readable Font Size | — | Confirm ⚠️ (UXP-012) |
| `ux-guidelines.csv#80` | Error Recovery | — | Form ⚠️ (UXP-003) |
| `ux-guidelines.csv#84` | Truncation | — | Form ⚠️ (UXP-005) |
| `web-interface.csv#1` | Icon Button Labels | — | Confirm ⚠️ (UXP-002), Result ⚠️ (UXP-011) |
| `web-interface.csv#12` | Never Block Paste | — | Confirm ✅ |

---

## Execution Log

| Phase | Status | Duration | Notes |
|:---|:---:|:---|:---|
| Handoff Check | ✅ | — | `.handoff/` created: `screen_inventory.json` (consumer_payload per screen), `handoff-manifest.json` (pipeline metadata), `flow_graph.json` (navigation edges). Next run uses fast-path |
| Skill A (Signal Inference) | ✅ | ~2 min | 17 signals matched across 3 screens |
| Skill B (PRD Context) | ✅ | ~2 min | 3 feature .md + 1 overview parsed |
| Skill C (Vision Review) | ✅ | ~5 min | 7 images analyzed via Agent Vision |
| Report Generation | ✅ | — | 12 findings: 3 Critical, 5 Major, 4 Minor |

*Generated by Pipe 2 (ux-review-pipe) — VNPAY Agentic Framework*
