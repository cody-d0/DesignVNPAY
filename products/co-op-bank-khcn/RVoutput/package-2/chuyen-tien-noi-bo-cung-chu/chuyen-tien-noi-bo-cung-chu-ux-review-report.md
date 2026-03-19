# UX Review Report — Chuyển tiền nội bộ cùng chủ (Co-op Bank KHCN)

## Tổng quan
- **Folder:** `co-op-bank-khcn/co-op-bank-khcn/package-2/chuyen-tien-noi-bo-cung-chu`
- **Số màn hình:** 3 (Form nhập thông tin, Xác nhận giao dịch, Kết quả giao dịch)
- **Tổng check:** 38 | **Pass:** 22 | **Gap:** 16 | **Unverifiable:** 8 (ảnh wireframe không có trên disk)
- **UX Score: 58%** (verifiable only: 22/38)

> **Ghi chú:** Các ảnh `ui/internal-transaction*.png` được tham chiếu trong PRD nhưng không tồn tại trên disk. Skill C (vision review) sử dụng dữ liệu OCR từ Section 3 thay thế; các kiểm tra cần ảnh thực tế được đánh dấu **unverifiable**.

---

## Đề xuất cải tiến (Priority)

### Critical

- **[UXP-001]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Thiếu loading state khi tải danh sách tài khoản & validate** | Hiện tại flow không mô tả trạng thái chờ khi load danh sách TK hoặc khi form đang validate. Đề xuất: thêm **skeleton loading gồm 2 dòng placeholder** cho block TK nguồn khi đang tải; thêm **spinner overlay** trên CTA "Tiếp tục" khi đang validate trước chuyển màn. | DDL: `ux-guidelines.csv#10` (Loading States), `ux-guidelines.csv#78` (Loading Indicators) | UX Law: `doherty` (< 400ms feedback)

- **[UXP-002]** Screen: `xac-nhan-giao-dich` | **Thiếu flow xử lý khi API Xác nhận thất bại** | Flow 1.1 chỉ mô tả Xác nhận → Kết quả thành công; không có luồng khi API trả lỗi (timeout, server error). Đề xuất: thêm **luồng 1.3 — Lỗi API**: hiển thị modal "Giao dịch không thành công. Vui lòng thử lại sau." với 2 nút: "Thử lại" (retry API) và "Quay lại" (về form). | DDL: `ux-guidelines.csv#33` (Error Feedback), `ux-guidelines.csv#80` (Error Recovery) | UX Law: `nng-error-recovery`

- **[UXP-003]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Thiếu xử lý lỗi Số tiền > Số dư khả dụng** | BR nêu "Số tiền ≤ số dư khả dụng" nhưng không có flow, AC, hoặc wireframe mô tả khi vi phạm. Đề xuất: thêm **inline error** dưới ô "Số tiền": text "Số tiền vượt quá số dư khả dụng" (màu đỏ), đồng thời **disable CTA "Tiếp tục"** cho đến khi sửa. | DDL: `ux-guidelines.csv#33` (Error Feedback), `web-interface.csv#15` (Inline Errors) | UX Law: `nng-error-prevention`

### Major

- **[UXP-004]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Thiếu empty state cho danh sách tài khoản** | Nếu khách hàng chưa có tài khoản cùng chủ hoặc danh sách trống, không có mô tả gì hiển thị. Đề xuất: trong dropdown TK nguồn/thụ hưởng, hiển thị text "Chưa có tài khoản phù hợp" kèm icon info. | DDL: `ux-guidelines.csv#79` (Empty States) | UX Law: `nng-visibility`

- **[UXP-005]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Thiếu mô tả trạng thái error & focused cho các input field** | Wireframe chỉ mô tả state mặc định và đặt lịch bật/tắt. Không có spec cho border đỏ khi lỗi, focus ring khi active. Đề xuất: thêm vào bảng "Mô tả màn hình" — mỗi input field bổ sung: state **focused** (border xanh `#2px solid primary`), state **error** (border đỏ + error message bên dưới, font 12px, màu `#E53935`). | DDL: `web-interface.csv#7` (Focus States), `web-interface.csv#15` (Inline Errors), `ux-guidelines.csv#56` (Inline Validation) | UX Law: `nng-visibility`

- **[UXP-006]** Screen: `xac-nhan-giao-dich` | **Thiếu trạng thái loading & chống double-submit cho CTA "Xác nhận"** | NFR có đề cập "disable sau khi chạm" nhưng wireframe và AC không mô tả. Đề xuất: sau khi tap "Xác nhận" → CTA chuyển sang state **loading** (spinner thay text, background mờ, touch disabled) cho đến khi API trả về. Copy trên button: spinner icon + "Đang xử lý...". | DDL: `ux-guidelines.csv#32` (Loading Buttons), `web-interface.csv#14` (Submit Button) | UX Law: `doherty`

- **[UXP-007]** Screen: `xac-nhan-giao-dich` | **NFR yêu cầu mask số TK nhưng wireframe hiển thị đầy đủ** | NFR viết "chính sách ẩn một phần số tài khoản" nhưng wireframe spec hiện: 98712313123, 13237899903. Gap giữa NFR và wireframe. Đề xuất: hiển thị dạng mask `****3123` và `****9903`; hoặc explicit ghi rõ "hiển thị đầy đủ" nếu đó là thiết kế chủ đích. | DDL: — | UX Law: —

- **[UXP-008]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Thiếu chỉ dấu required cho các trường bắt buộc** | Form có nhiều trường (Số tiền, TK thụ hưởng, Nội dung) nhưng không spec trường nào required, asterisk hay label "bắt buộc". Đề xuất: thêm ký hiệu `*` sau label của các trường bắt buộc: "Số tiền *", "Tài khoản thụ hưởng *". | DDL: `ux-guidelines.csv#59` (Required Indicators) | UX Law: `nng-error-prevention`

- **[UXP-009]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Switch "Đặt lịch chuyển tiền" thiếu accessible label** | Switch chỉ có visual label "Đặt lịch chuyển tiền" nhưng không spec aria-label hoặc accessibility cho screen reader. Đề xuất: thêm `aria-label="Bật đặt lịch chuyển tiền"` cho switch; đảm bảo touch target ≥ 44pt bao gồm cả label (click on label toggles switch). | DDL: `web-interface.csv#1` (Icon Button Labels), `ux-guidelines.csv#40` (ARIA Labels) | UX Law: `wcag-operable`

### Minor

- **[UXP-010]** Screen: `ket-qua-giao-dich` | **Thời gian đặt lịch mâu thuẫn với ngày bắt đầu** | Wireframe spec: "Thời gian đặt lịch: 15/02/2020 22:00" nhưng "Ngày bắt đầu: 15/05/2023" — chênh 3 năm, dữ liệu mẫu không hợp lý. Đề xuất: sửa thành cùng năm (vd. "15/05/2023 22:00"). | DDL: `ux-guidelines.csv#85` (Date Formatting) | UX Law: —

- **[UXP-011]** Screen: Cross-screen | **Số tài khoản không nhất quán giữa các màn** | Form: 9099798712313123; Xác nhận: 98712313123 / 13237899903; Kết quả: 9704000012345678 / 1231236788923211. Dữ liệu mẫu khác nhau gây nhầm lẫn khi review. Đề xuất: thống nhất dữ liệu mẫu xuyên suốt 3 màn. | DDL: — | UX Law: `nng-consistency-standards`

- **[UXP-012]** Screen: `ket-qua-giao-dich` | **Thiếu xử lý lỗi khi Chia sẻ/Lưu ảnh thất bại** | Không có flow hoặc AC cho trường hợp native share hoặc save thất bại (permission denied, disk full). Đề xuất: hiển thị **toast notification** "Không thể lưu ảnh. Vui lòng kiểm tra quyền truy cập." (auto-dismiss 4s). | DDL: `ux-guidelines.csv#33` (Error Feedback), `ux-guidelines.csv#82` (Toast Notifications) | UX Law: `nng-error-recovery`

- **[UXP-013]** Screen: `chuyen-tien-noi-bo-cung-chu` | **Không đề cập prefers-reduced-motion** | Switch toggle, modal animation, transition giữa các state không có spec cho motion sensitivity. Đề xuất: thêm vào NFR: "Tôn trọng prefers-reduced-motion: giảm hoặc tắt animation cho switch, modal fade, transitions." | DDL: `ux-guidelines.csv#9` (Reduced Motion) | UX Law: —

---

## Chi tiết theo màn hình

### 1. Chuyển tiền nội bộ cùng chủ (Form nhập thông tin)
**Score: 50% | Pass: 9 | Gap: 9 | Unverifiable: 4 | Images: `ui/internal-transaction.png` → `ui/internal-transaction-4.png`**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Happy path flow (Form → Tiếp tục → Xác nhận) | Skill B §1.1 | — | **pass** | Flow 1.1 mô tả đầy đủ 3 bước |
| 2 | Validation error flow (số lần > 10 → modal) | Skill B §1.2 | ux-guidelines#33 | **pass** | Flow 1.2 + modal "Thông báo" |
| 3 | Back navigation + giữ data | Skill B §1.3 | ux-guidelines#4 | **pass** | Flow 1.3: "giữ data đã nhập" |
| 4 | Loading state khi load TK / validate | Skill B §1+§5 | ux-guidelines#10,#78 | **gap** | Không có mô tả loading trong flow hoặc wireframe |
| 5 | Empty state cho danh sách TK | Skill B §3 | ux-guidelines#79 | **gap** | Không có mô tả khi 0 TK |
| 6 | Lỗi Số tiền > Số dư | Skill B §2 (US-003 BR) | ux-guidelines#33; nng-error-prevention | **gap** | BR nêu ràng buộc nhưng không có error flow/AC |
| 7 | Form labels đầy đủ | Skill A (OCR) | web-interface#2 | **pass** | OCR xác nhận: tất cả field có label visible |
| 8 | Character counter (30/160) | Skill A (OCR) | — | **pass** | OCR: "30/160" hiển thị |
| 9 | Input inline error states (border, message) | Skill B §3 | web-interface#15; ux-guidelines#56 | **gap** | Wireframe chỉ mô tả state mặc định |
| 10 | Input focused states (focus ring) | Skill B §3 | web-interface#7 | **gap** | Không có spec focused state |
| 11 | CTA "Tiếp tục" loading/disabled state | Skill B §3 | ux-guidelines#32; web-interface#14 | **gap** | Wireframe chỉ mô tả "CTA gradient xanh" |
| 12 | Switch accessible label | Skill B §3 | web-interface#1; ux-guidelines#40 | **gap** | Không có aria-label spec |
| 13 | Modal "Thông báo" — dismiss + error recovery | Skill B §3 (row 8) | ux-guidelines#80 | **pass** | Có nút "Đóng", quay lại form chỉnh sửa |
| 14 | Touch target ≥ 44pt | Skill B §5 NFR | ux-guidelines#22 | **pass** | NFR ghi: "Touch target tối thiểu 44pt" |
| 15 | Focus ring cho điều hướng bàn phím | Skill B §5 NFR | ux-guidelines#28 | **pass** | NFR ghi: "focus ring cho điều hướng bàn phím" |
| 16 | Inline validation on blur/change | Skill B §5 NFR | ux-guidelines#56 | **pass** | NFR ghi: "validate form ngay khi blur/change" |
| 17 | Required field indicators | Skill B §3 | ux-guidelines#59 | **gap** | Không có dấu * hoặc "bắt buộc" |
| 18 | Reduced motion support | Skill B §5 | ux-guidelines#9 | **gap** | Không đề cập |
| 19 | Layout alignment & spacing | Skill C (cần ảnh) | gestalt-proximity | **unverifiable** | Ảnh không tồn tại trên disk |
| 20 | Color contrast đủ 4.5:1 | Skill C (cần ảnh) | ux-guidelines#36 | **unverifiable** | Ảnh không tồn tại |
| 21 | Icon visibility & clarity | Skill C (cần ảnh) | ux-guidelines#40 | **unverifiable** | OCR ghi nhận icon: back, chevron, calendar, switch |
| 22 | Text truncation check | Skill C (cần ảnh) | ux-guidelines#84 | **unverifiable** | Không thể kiểm tra từ OCR text |

---

### 2. Xác nhận giao dịch
**Score: 50% | Pass: 5 | Gap: 5 | Unverifiable: 2 | Images: `ui/internal-transaction-5.png`**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Happy path flow (Review → Xác nhận → Kết quả) | Skill B §1.1 | — | **pass** | Flow 1.1 đầy đủ |
| 2 | Error flow khi API thất bại | Skill B §1 | ux-guidelines#33,#80; nng-error-recovery | **gap** | Không có luồng error handling |
| 3 | Back + giữ data | Skill B §1.2 | ux-guidelines#4 | **pass** | Flow 1.2: "giữ nguyên thông tin" |
| 4 | CTA "Xác nhận" loading state | Skill B §3 | ux-guidelines#32,#78 | **gap** | Wireframe chỉ ghi "CTA full width, màu xanh" |
| 5 | Double-submit prevention | Skill B §5 NFR | web-interface#14 | **gap** | NFR đề cập "disable sau khi chạm" nhưng wireframe/AC không spec |
| 6 | Account masking (NFR vs wireframe) | Skill B §5 vs §3 | — | **gap** | NFR ghi mask nhưng wireframe hiển thị đầy đủ: 98712313123 |
| 7 | Label-value display đầy đủ các trường | Skill A+B §3 | — | **pass** | OCR xác nhận 9 cặp label-value |
| 8 | Số tiền hiển thị số + chữ | Skill A (OCR) | ux-guidelines#86 | **pass** | "20,000,000 VND" + "Hai mươi triệu đồng" |
| 9 | Touch target ≥ 44pt | Skill B §5 NFR | ux-guidelines#22 | **pass** | NFR ghi: "touch target ≥ 44pt" |
| 10 | API timeout handling (< 5s + loading) | Skill B §5 NFR | ux-guidelines#78 | **gap** | NFR ghi hiển thị loading nhưng flow/wireframe không spec |
| 11 | Layout & spacing | Skill C (cần ảnh) | gestalt-proximity | **unverifiable** | Ảnh không tồn tại |
| 12 | Color contrast | Skill C (cần ảnh) | ux-guidelines#36 | **unverifiable** | Ảnh không tồn tại |

---

### 3. Kết quả giao dịch
**Score: 80% | Pass: 8 | Gap: 2 | Unverifiable: 2 | Images: `ui/internal-transaction-6.png`**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success display (icon + text) | Skill A+B §3 | ux-guidelines#34 | **pass** | OCR: "Đặt lịch chuyển tiền thành công" + checkmark icon |
| 2 | Chi tiết giao dịch đầy đủ (10 fields) | Skill B §3 | — | **pass** | OCR xác nhận 10 cặp label-value |
| 3 | Hành động Chia sẻ & Lưu ảnh | Skill A+B §3 | — | **pass** | OCR: "Chia sẻ", "Lưu ảnh" với icon |
| 4 | CTA "Tạo giao dịch mới" | Skill B §3 | — | **pass** | Wireframe spec row 5 |
| 5 | Home navigation (header) | Skill B §1.2 | — | **pass** | Flow 1.2 + OCR: Home icon |
| 6 | Success branding (logo Co-opBank) | Skill A (OCR) | — | **pass** | OCR: "Co-opBank" logo |
| 7 | Error handling Chia sẻ/Lưu ảnh | Skill B §1+§2 | ux-guidelines#33,#82 | **gap** | Không có flow/AC cho trường hợp lỗi |
| 8 | Dữ liệu mẫu nhất quán (date, TK) | Skill B cross-screen | nng-consistency-standards | **gap** | "15/02/2020" mâu thuẫn "15/05/2023"; TK khác form |
| 9 | Account masking on share/save | Skill B §5 NFR | — | **pass** | NFR ghi: "cân nhắc che/mask" |
| 10 | Touch target ≥ 44pt | Skill B §5 NFR | ux-guidelines#22 | **pass** | NFR ghi rõ |
| 11 | Icon clarity (Share, Save) | Skill C (cần ảnh) | ux-guidelines#40 | **unverifiable** | OCR ghi nhận icon: share, save image |
| 12 | Layout & contrast | Skill C (cần ảnh) | ux-guidelines#36 | **unverifiable** | Ảnh không tồn tại |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| `ux-guidelines.csv#4` | Back Button — preserve history | `jakob` | Screen 1 (pass), Screen 2 (pass) |
| `ux-guidelines.csv#9` | Reduced Motion — prefers-reduced-motion | — | Screen 1 (gap: UXP-013) |
| `ux-guidelines.csv#10` | Loading States — skeleton/spinner | `doherty` | Screen 1 (gap: UXP-001) |
| `ux-guidelines.csv#22` | Touch Target Size — min 44×44px | `fitts` | All screens (pass via NFR) |
| `ux-guidelines.csv#28` | Focus States — visible focus ring | — | Screen 1 (pass via NFR) |
| `ux-guidelines.csv#32` | Loading Buttons — disable + spinner | `doherty` | Screen 1 (gap: UXP-001), Screen 2 (gap: UXP-006) |
| `ux-guidelines.csv#33` | Error Feedback — clear messages | — | Screen 1 (gap: UXP-003), Screen 2 (gap: UXP-002), Screen 3 (gap: UXP-012) |
| `ux-guidelines.csv#34` | Success Feedback — confirm action | — | Screen 3 (pass) |
| `ux-guidelines.csv#36` | Color Contrast — 4.5:1 minimum | — | All screens (unverifiable) |
| `ux-guidelines.csv#40` | ARIA Labels — accessible names | — | Screen 1 (gap: UXP-009) |
| `ux-guidelines.csv#56` | Inline Validation — validate on blur | — | Screen 1 (pass via NFR) |
| `ux-guidelines.csv#59` | Required Indicators — asterisk or text | — | Screen 1 (gap: UXP-008) |
| `ux-guidelines.csv#78` | Loading Indicators — spinner/skeleton | `doherty` | Screen 1 (gap: UXP-001), Screen 2 (gap: UXP-006) |
| `ux-guidelines.csv#79` | Empty States — helpful message + action | — | Screen 1 (gap: UXP-004) |
| `ux-guidelines.csv#80` | Error Recovery — clear next steps | — | Screen 2 (gap: UXP-002) |
| `ux-guidelines.csv#82` | Toast Notifications — auto-dismiss 3-5s | — | Screen 3 (gap: UXP-012) |
| `ux-guidelines.csv#84` | Truncation — ellipsis + expand | — | All screens (unverifiable) |
| `ux-guidelines.csv#85` | Date Formatting — locale-appropriate | — | Screen 3 (gap: UXP-010) |
| `ux-guidelines.csv#86` | Number Formatting — thousand separators | — | Screen 2 (pass), Screen 3 (pass) |
| `web-interface.csv#1` | Icon Button Labels — aria-label required | — | Screen 1 (gap: UXP-009) |
| `web-interface.csv#2` | Form Control Labels — label/aria required | — | Screen 1 (pass) |
| `web-interface.csv#7` | Visible Focus States — ring/outline | `von-restorff` | Screen 1 (gap: UXP-005) |
| `web-interface.csv#14` | Submit Button — spinner during request | `doherty` | Screen 2 (gap: UXP-006) |
| `web-interface.csv#15` | Inline Errors — near problem field | — | Screen 1 (gap: UXP-003, UXP-005) |

### UX Laws referenced

| law_id | Law | Áp dụng |
|--------|-----|---------|
| `doherty` | Doherty Threshold (< 400ms feedback) | UXP-001, UXP-006 |
| `fitts` | Fitts's Law (target size) | All screens — touch target NFR |
| `jakob` | Jakob's Law (familiarity) | Back button behavior |
| `nng-error-prevention` | Error Prevention (Nielsen) | UXP-003, UXP-008 |
| `nng-error-recovery` | Error Recovery (Nielsen) | UXP-002, UXP-012 |
| `nng-visibility` | Visibility of System Status | UXP-004, UXP-005 |
| `nng-consistency-standards` | Consistency and Standards | UXP-011 |
| `von-restorff` | Von Restorff Effect | Focus states |
| `gestalt-proximity` | Law of Proximity | Layout checks (unverifiable) |
| `wcag-operable` | Operable (WCAG POUR) | UXP-009 |

---

*Generated by UX Review Pipe — Skill A (Signal Inference + DDL) ∥ Skill B (PRD Context + DDL) → Skill C (Vision Review + Proposals)*
