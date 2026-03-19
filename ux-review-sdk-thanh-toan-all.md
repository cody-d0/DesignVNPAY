# 🏦 UX Review Report — SDK Thanh Toán All

> **Pipeline:** figma-to-ux-review · **Generated:** 2026-03-17
> **Figma File:** [`aYeSAVi94QlI4i4rL3xtmR`](https://www.figma.com/design/aYeSAVi94QlI4i4rL3xtmR/Untitled?node-id=24-10736)

---

## 📊 Score Dashboard

| Metric | Value |
|--------|-------|
| **Screens** | 13 |
| **Total Checks** | 89 |
| **Pass** | 54 (61%) |
| **Gap** | 28 (31%) |
| **Unverifiable** | 7 (8%) |
| **UX Score (Simple)** | **61%** |
| **UX Score (Weighted)** | **100%** |
| **Proposals** | 🔴 3 Critical · 🟡 6 Major · 🔵 5 Minor |

> [!NOTE]
> Weighted score = 100% vì tool không parse được proposal-to-screen mapping (proposal format trong report dùng multi-screen references). Simple score 61% là metric chính xác hơn.

✅ **Tool-verified** by `ux-score-calculator v1.0.0` — zero discrepancies

---

## 📁 Output Files

### PRD .md Pack (13 files)

| Section | Files |
|---------|-------|
| **Thanh Toán Vietlott** (4 screens) | [scr-vl-001](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-vietlott/scr-vl-001-thanh-toan-vietlott-summary.md), [scr-vl-002](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-vietlott/scr-vl-002-xac-nhan-giao-dich.md), [scr-vl-003](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-vietlott/scr-vl-003-otp-vietlott.md), [scr-vl-004](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-vietlott/scr-vl-004-ket-qua-giao-dich.md) |
| **Thanh toán vé xem phim** (4 screens) | [scr-vp-001](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-xem-phim/scr-vp-001-thanh-toan-ve-xem-phim-summary.md), [scr-vp-002](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-xem-phim/scr-vp-002-xac-nhan-giao-dich.md), [scr-vp-003](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-xem-phim/scr-vp-003-otp-ve-xem-phim.md), [scr-vp-004](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-xem-phim/scr-vp-004-ket-qua-giao-dich.md) |
| **Thanh toán vé tàu** (5 screens) | [scr-vt-001](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-tau/scr-vt-001-thanh-toan-ve-tau-summary-1.md), [scr-vt-002](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-tau/scr-vt-002-thanh-toan-ve-tau-summary-2.md), [scr-vt-003](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-tau/scr-vt-003-xac-nhan-giao-dich.md), [scr-vt-004](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-tau/scr-vt-004-otp-ve-tau.md), [scr-vt-005](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/thanh-toan-ve-tau/scr-vt-005-ket-qua-giao-dich.md) |

### Handoff + Review

| File | Link |
|------|------|
| **Overview** | [sdk-thanh-toan-all-overview.md](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/sdk-thanh-toan-all-overview.md) |
| **Screen Inventory** | [screen_inventory.json](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/.handoff/screen_inventory.json) |
| **Handoff Manifest** | [handoff-manifest.json](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/.handoff/handoff-manifest.json) |
| **UX Review Report** | [ux-review-report.md](file:///Users/dataism/Documents/UXtool/sdk-thanh-toan-all/ux-review-report.md) |

---

## 🔴 Critical Proposals (3)

### UXP-001 · Long Scroll CTA Hidden
**Screens:** SCR-VT-001 (1071px), SCR-VT-002 (1407px) — vượt viewport 812px

Màn hình summary vé tàu quá dài, button "Tiếp tục" bị ẩn khỏi viewport ban đầu. User có thể nhấn mà chưa review hết thông tin.

**Đề xuất:**
1. Gom thông tin chuyến đi thành **collapsible sections** (mặc định collapse, hiện summary 1 dòng)
2. **Sticky button** "Tiếp tục" ở bottom viewport
3. Thêm scroll indicator nếu content > viewport

> DDL: `ux-guidelines.csv#19` (Content Jumping), `ux-laws.csv#cognitive-load`

### UXP-002 · Instruction Text Mismatch
**Screens:** Tất cả Confirm screens (SCR-VL-002, SCR-VP-002, SCR-VT-003)

Text "đặt lịch" chỉ đúng cho booking service, không phù hợp mua xổ số hay vé tàu.

**Đề xuất:** Dùng text generic: *"Quý khách vui lòng kiểm tra lại thông tin giao dịch"*

> DDL: `ux-laws.csv#nng-match-world` (Match System and Real World)

### UXP-003 · Hotline Placeholder
**Screens:** SCR-VP-004, SCR-VT-005

"Tổng đài XXXXX" — placeholder chưa thay bằng số thật. Deploy sẽ khiến user không có kênh liên hệ.

**Đề xuất:** Thay `XXXXX` → số tổng đài thật + format `tel:` link

> DDL: `ux-guidelines.csv#80` (Error Recovery)

---

## 🟡 Major Proposals (6)

| ID | Vấn đề | Screens | Đề xuất |
|----|--------|---------|---------|
| **UXP-004** | Thiếu failure variant | All Result screens | Thêm "Giao dịch không thành công" + Thử lại |
| **UXP-005** | OTP thiếu states | All OTP screens | Countdown + Error + Expired states |
| **UXP-006** | Info inconsistent ở Result | SCR-VT-005 | 4 rows vs 6 rows so với vé phim |
| **UXP-007** | Masking mã TT inconsistent | SCR-VL-001 vs VL-002 | 123*** vs 123123 |
| **UXP-008** | Thiếu loading transition | All Summary | Skeleton loading SDK → Payment |
| **UXP-009** | Số tiền chữ đỏ = error color | All Confirm | Đổi sang primary dark |

---

## 🔵 Minor Proposals (5)

| ID | Vấn đề | Đề xuất |
|----|--------|---------|
| **UXP-010** | Font size title inconsistent | Thống nhất 16/18px |
| **UXP-011** | "Tổng tiền" text wrapping | Flexible layout |
| **UXP-012** | SĐT masking inconsistent | Thống nhất policy |
| **UXP-013** | "Tạo giao dịch mới" vague | Context-specific CTA |
| **UXP-014** | Bottom sheet thiếu grabber | Thêm pill-shape grabber |

---

## 📈 Per-Screen Score Heatmap

| Screen | Checks | Pass | Gap | Unv | Score |
|--------|--------|------|-----|-----|-------|
| scr-vl-001 · Summary Vietlott | 7 | 5 | 1 | 1 | 🟢 71% |
| scr-vl-002 · Confirm Vietlott | 7 | 5 | 2 | 0 | 🟢 71% |
| scr-vl-003 · OTP Vietlott | 7 | 3 | 3 | 1 | 🔴 43% |
| scr-vl-004 · Result Vietlott | 6 | 4 | 2 | 0 | 🟡 67% |
| scr-vp-001 · Summary Vé phim | 7 | 5 | 1 | 1 | 🟢 71% |
| scr-vp-002 · Confirm Vé phim | 7 | 5 | 2 | 0 | 🟢 71% |
| scr-vp-003 · OTP Vé phim | 7 | 3 | 3 | 1 | 🔴 43% |
| scr-vp-004 · Result Vé phim | 7 | 5 | 2 | 0 | 🟢 71% |
| scr-vt-001 · Summary Vé tàu 1 | 7 | 4 | 2 | 1 | 🟡 57% |
| scr-vt-002 · Summary Vé tàu 2 | 6 | 3 | 2 | 1 | 🟡 50% |
| scr-vt-003 · Confirm Vé tàu | 7 | 5 | 2 | 0 | 🟢 71% |
| scr-vt-004 · OTP Vé tàu | 7 | 3 | 3 | 1 | 🔴 43% |
| scr-vt-005 · Result Vé tàu | 7 | 4 | 3 | 0 | 🟡 57% |

> [!IMPORTANT]
> **Pattern rõ ràng:** Màn OTP luôn là điểm yếu nhất (43%) do thiếu error/resend/expired states. Đây là gap dễ fix nhất với ROI cao nhất.

---

## 🎯 Key UX Patterns Detected

### ✅ Strengths
1. **Consistent flow 4-bước** chuẩn (Summary → Confirm → OTP → Result) trên tất cả SDK
2. **Balance card** với dropdown chọn TK — pattern tốt cho banking
3. **Số tiền bằng chữ** ở bước xác nhận — giảm risk nhập sai
4. **Touch target** đạt chuẩn 44×44px trên tất cả CTA
5. **Header navigation** Back + Home consistent

### ⚠️ Weaknesses  
1. **OTP screen** thiếu nhiều states quan trọng (error, resend, expired)
2. **Long scroll** vé tàu (1.7x viewport) — CTA bị ẩn
3. **Text instruction** dùng chung "đặt lịch" cho mọi service
4. **Masking** inconsistent giữa các screens

---

## 🔗 DDL References Used

19 DDL rules referenced from:
- `ux-guidelines.csv`: #4, #10, #19, #22, #33, #37, #74, #80, #81, #84
- `ux-laws.csv`: cognitive-load, nng-match-world, nng-consistency-standards, nng-error-recovery, nng-visibility, jakob, doherty, gestalt-similarity, fitts
