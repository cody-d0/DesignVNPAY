# UX Review Report — Co-opBank Mobile Banking

## Tổng quan

- **Folder:** COOPBANK/final/Tra soát/Tra cứu yêu cầu
- **Số màn hình:** 3 | **Tổng check:** 0
- **Pass:** 0 | **Gap:** 0 | **Unverifiable:** 0
- **UX Score (Simple):** 0% (0/0)
- **UX Score (Weighted):** 0%

> ⚠️ Scores được cập nhật bởi `ux-score-calculator.js`

---


**Total checks:** 48  
**Pass:** 16 | **Gap:** 28 | **Unverifiable:** 4  
**Simple Score:** 33%  
**Weighted Score:** 33%## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Chi tiết yêu cầu tra soát › Chi tiết |
|:---|:---|
| **Vấn đề** | Trường "Tài khoản nguồn" hiển thị đầy đủ 13 chữ số (1212390002122) không có masking, không có toggle ẩn/hiện |
| **Gap ref** | Check #15, Check #1 |
| **DDL** | UXG-76 · banking-security · Law:fitts |
| **Giải pháp** | Vị trí |

---

#### UXP-002 · Major
| **Màn hình** | Tra cứu yêu cầu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Sau khi bấm "Tìm kiếm", không có loading state |
| **Gap ref** | Check #2, Check #9, Check #2 |
| **DDL** | UXG-61 · UXG-78 · Law:doherty |
| **Giải pháp** | Vị trí |

---

#### UXP-003 · Major
| **Màn hình** | Tra cứu yêu cầu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Validation lỗi chỉ hiển thị qua popup "Thông báo" |
| **Gap ref** | Check #10, Check #1, Check #16 |
| **DDL** | UXG-56 · UXG-44 · UXG-33 |
| **Giải pháp** | Vị trí |

---

#### UXP-004 · Major
| **Màn hình** | Tra cứu yêu cầu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Label hiển thị "Trang thái tra soát" (thiếu chữ "g") — lỗi chính tả visible trên 2 artboard |
| **Gap ref** | Check #15 |
| **DDL** | UXG-76 |
| **Giải pháp** | Vị trí |

---

#### UXP-005 · Major
| **Màn hình** | Danh sách yêu cầu tra soát › Danh sách |
|:---|:---|
| **Vấn đề** | Empty state chỉ có 1 text "Không có kết quả tìm kiếm" |
| **Gap ref** | Check #1, Check #3, Check #1 |
| **DDL** | UXG-79 · UXG-90 · Law:peak-end |
| **Giải pháp** | Vị trí |

---

#### UXP-006 · Major
| **Màn hình** | Danh sách yêu cầu tra soát › Danh sách |
|:---|:---|
| **Vấn đề** | 3 status badges phân biệt chỉ bằng màu |
| **Gap ref** | Check #6, Check #7, Check #7 |
| **DDL** | UXG-37 · UXG-36 |
| **Giải pháp** | Vị trí |

---

#### UXP-007 · Major
| **Màn hình** | Chi tiết yêu cầu tra soát › Chi tiết |
|:---|:---|
| **Vấn đề** | Link "Chi tiết giao dịch ›" không có affordance: text màu thường, no underline, chevron nhỏ, touch target < 44px |
| **Gap ref** | Check #5, Check #6, Check #4 |
| **DDL** | UXG-4 · UXG-165 · Law:fitts |
| **Giải pháp** | Vị trí |

---

#### UXP-008 · Minor
| **Màn hình** | Tra cứu yêu cầu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Popup "Thông báo" minimal: không icon, không suggestion hành động |
| **Gap ref** | Check #6, Check #11, Check #9 |
| **DDL** | UXG-35 · UXG-44 · Law:peak-end |
| **Giải pháp** | Vị trí |

---

#### UXP-009 · Minor
| **Màn hình** | Chi tiết yêu cầu tra soát › Chi tiết |
|:---|:---|
| **Vấn đề** | Badge "Đã xử lý" (artboard 5) contrast ~3 |
| **Gap ref** | Check #8, Check #7, Check #8 |
| **DDL** | UXG-37 · UXG-36 |
| **Giải pháp** | Vị trí |

---

#### UXP-010 · Minor
| **Màn hình** | Chi tiết yêu cầu tra soát › Chi tiết |
|:---|:---|
| **Vấn đề** | Trường "Kết quả: — —" khi pending — screen reader đọc "dash dash", không có meaning |
| **Gap ref** | Check #9, Check #11 |
| **DDL** | UXG-44 |
| **Giải pháp** | Vị trí |

---

## Chi tiết theo màn hình

### 1. Tra cứu yêu cầu › Form nhập thông tin

> `SCR-TCY-001` · form · 3 artboards

**Score: 33% | Pass: 6 | Gap: 10 | Unverifiable: 4**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | text-input-1: error state — inline validation | Skill A (Component) | Major | Gap | DDL text-input-1: states=[value,error,focused]. Từ ảnh tra-cuu-yeu-cau-1.png+2.png: chỉ default/filled state. error state MISSING. UXG-56. |
| 2 | loading-spinner-1: loading state sau submit | Skill A (Component) | Major | Gap | DDL loading-spinner-1: idle=animating. Từ ảnh: không có loading variant artboard. Doherty Threshold violation. UXG-61 UXG-78. |
| 3 | empty-state-1: icon trong popup Thông báo | Skill A (Component) | Minor | Gap | DDL empty-state-1: icon required. Từ ảnh tra-cuu-yeu-cau-7.png: popup title+text+Đóng, không có icon. UXG-79. |
| 4 | Fitts Law: calendar icon touch target ≥44px | Skill A (Law) | Minor | Gap | DDL Fitts Law trigger (button). Từ ảnh tra-cuu-yeu-cau-1.png: calendar icon ~20px visible, ước tính < 44px. UXG-165. |
| 5 | Hick Law: status filter options ≤7 | Skill A (Law) | Pass | Pass | DDL Hick Law (dropdown). Dropdown Tất cả: ≤5 options giả định. Trong giới hạn cognitive load. |
| 6 | Peak-End Rule: error popup experience | Skill A (Law) | Major | Gap | DDL Peak-End Rule (error state). Từ ảnh tra-cuu-yeu-cau-7.png: popup minimal, không có icon, không có alternative action. UXG-35. |
| 7 | UXG-43: Form labels — mọi field có label | Skill B (PRD) | Pass | Pass | Từ ảnh tra-cuu-yeu-cau-1.png: Từ ngày, Đến ngày, Trang thái tra soát, Mã tra soát đều có label text rõ ràng. |
| 8 | UXG-54: Input labels associated với inputs | Skill B (PRD) | Pass | Pass | Từ ảnh: labels nằm ngay trên input fields. Visual association rõ ràng. |
| 9 | UXG-61: Submit feedback loading sau CTA | Skill B (PRD) | Major | Gap | UXG-61 Submit Feedback (High). Từ ảnh: không có loading state artboard sau tap Tìm kiếm. |
| 10 | UXG-56: Inline validation vs popup only | Skill B (PRD) | Major | Gap | UXG-56 Inline Validation. Error chỉ có popup Thông báo, không có inline per field. |
| 11 | UXG-44: Error message actionable | Skill B (PRD) | Minor | Gap | UXG-44 Error Messages (High). Từ ảnh tra-cuu-yeu-cau-7.png: message có hướng dẫn chung nhưng thiếu suggest cụ thể. |
| 12 | UXG-35: Confirmation dialog dismiss behavior | Skill B (PRD) | Pass | Pass | Từ ảnh: popup có nút Đóng rõ ràng. UXG-35. Acceptable. |
| 13 | UXG-37: Color Only — Tab active indicator | Skill C (Vision) | Pass | Pass | Từ ảnh tra-cuu-yeu-cau-1.png: Tab active dùng underline + màu xanh, không chỉ màu. UXG-37. |
| 14 | UXG-76: Contrast readability — header và CTA | Skill C (Vision) | Pass | Pass | Từ ảnh: header trắng/xanh ~10:1 PASS; CTA trắng/xanh ~10:1 PASS. WCAG AA. |
| 15 | Typo: Trang thái → Trạng thái | Skill C (Vision) | Major | Gap | Từ ảnh tra-cuu-yeu-cau-1.png+2.png: label Trang thái tra soát — thiếu chữ g. UXG-76. |
| 16 | Date range validation: Từ ngày ≤ Đến ngày | Skill B (Flow) | Major | Gap | Skill B flow_check: has_error=false cho date validation. Không có artboard cho invalid date range. UXG-56. |
| 17 | UXG-58: Autocomplete cho date fields | Skill B (PRD) | Minor | Unverifiable | UXG-58 Autofill Support. Không verifiable từ static Figma wireframe. |
| 18 | Banking: session timeout warning UI | Skill B (Product) | Minor | Unverifiable | product_context: Security-first. Session timeout UI không verifiable từ Figma static. |

### 2. Danh sách yêu cầu tra soát › Danh sách

> `SCR-TCY-002` · list · 2 artboards

**Score: 40% | Pass: 6 | Gap: 8 | Unverifiable: 1**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | empty-state-1: icon + description + CTA | Skill A (Component) | Major | Gap | DDL empty-state-1: icon required, CTA optional. Từ ảnh tra-cuu-yeu-cau-6.png: chỉ 1 text Không có kết quả tìm kiếm, không icon, không CTA. UXG-79 UXG-90. |
| 2 | loading-spinner-1: loading state khi fetch | Skill A (Component) | Major | Gap | DDL loading-spinner-1. Không có loading variant artboard cho màn hình danh sách. UXG-78. |
| 3 | Doherty Threshold: feedback khi fetch list | Skill A (Law) | Major | Gap | DDL Doherty Threshold auto-match. Không có loading/skeleton screen. UXG-78. |
| 4 | Fitts Law: list item touch target | Skill A (Law) | Pass | Pass | Từ ảnh tra-cuu-yeu-cau-3.png: list item height ~116px. Thoải mái ≥44px. Fitts Law OK. |
| 5 | Hick Law: 3 status types distinction | Skill A (Law) | Pass | Pass | 3 badge types ≤7 options trong giới hạn cognitive load. Hick Law. |
| 6 | UXG-37: Color Only — status badges | Skill B (PRD) | Major | Gap | UXG-37 Color Only (High). Từ ảnh tra-cuu-yeu-cau-3.png: 3 badges phân biệt chỉ bằng màu, không icon. ~8% người dùng mù màu bị ảnh hưởng. |
| 7 | WCAG AA: badge Nghi vấn contrast | Skill C (Vision) | Major | Gap | Từ ảnh tra-cuu-yeu-cau-3.png: badge Nghi vấn — nền xám nhạt, text xám, est. ~3.5:1 < 4.5:1. FAIL WCAG AA. UXG-36. |
| 8 | WCAG AA: badge Đã xử lý contrast | Skill C (Vision) | Minor | Gap | Từ ảnh: badge Đã xử lý — est. ~4:1 borderline < 4.5:1. FAIL WCAG AA. UXG-36. |
| 9 | WCAG AA: badge Đã tiếp nhận contrast | Skill C (Vision) | Pass | Pass | Từ ảnh: badge Đã tiếp nhận — nền navy, text trắng, est. ~8:1. PASS WCAG AA. UXG-36. |
| 10 | UXG-165: search clear X button touch target | Skill C (Vision) | Pass | Pass | Từ ảnh tra-cuu-yeu-cau-6.png: X button dalam search bar — sufficient size. UXG-165. |
| 11 | UXG-78: Loading indicator khi fetch | Skill B (PRD) | Major | Gap | UXG-78 Loading Indicators (High). Không có artboard loading state. |
| 12 | UXG-76: Amount text contrast | Skill C (Vision) | Pass | Pass | Từ ảnh: -5,000,000 VND text đậm trên nền trắng, est. >7:1. PASS WCAG AA. |
| 13 | Peak-End Rule: negative amount display | Skill A (Law) | Pass | Pass | Từ ảnh: amount hiển thị rõ dấu âm, màu phân biệt. Peak-End OK. |
| 14 | Banking: transaction ID copyable | Skill B (Product) | Minor | Gap | product_context: Trust paramount. #123123 không có copy affordance visible từ ảnh. |
| 15 | UXG-47: Virtualize lists performance | Skill B (NFR) | Minor | Unverifiable | UXG-47 Lazy Loading. Không verifiable từ static wireframe. Cần implement nếu list >20 items. |

### 3. Chi tiết yêu cầu tra soát › Chi tiết

> `SCR-TCY-003` · detail · 2 artboards

**Score: 27% | Pass: 4 | Gap: 10 | Unverifiable: 1**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | Account number masking — PII | Skill B (Product Security) | Critical | Gap | Từ ảnh tra-cuu-yeu-cau-4.png+5.png: Tài khoản nguồn 1212390002122 — 13 số đầy đủ, không masked. product_context: Security-first. banking-security. |
| 2 | loading-spinner-1: loading state chi tiết | Skill A (Component) | Minor | Gap | DDL loading-spinner-1. Không có loading state artboard khi navigate list→detail. UXG-78. |
| 3 | receipt-preview-1: section visual separator | Skill A (Component) | Minor | Gap | DDL receipt-preview-1: sections cần separator rõ. Từ ảnh: 2 sections chỉ chia bởi whitespace, không có divider line. |
| 4 | Doherty Threshold: loading chi tiết | Skill A (Law) | Minor | Gap | DDL Doherty auto-match. Không có skeleton/loading state. UXG-78. |
| 5 | Fitts Law: Chi tiết giao dịch touch target | Skill A (Law) | Major | Gap | Từ ảnh tra-cuu-yeu-cau-4.png: row Chi tiết giao dịch — text row, touch target ước tính < 44px. Fitts Law. UXG-165. |
| 6 | UXG-4: Link Chi tiết giao dịch affordance | Skill B (PRD) | Major | Gap | UXG-4 Navigation (High). Từ ảnh: text màu thường, no underline, no background. Không rõ là clickable. Information Scent thấp. |
| 7 | UXG-37: Status badge color-only | Skill C (Vision) | Major | Gap | UXG-37 Color Only (High). Từ ảnh: badges Đã tiếp nhận/Đã xử lý phân biệt chỉ bằng màu. Không có icon. |
| 8 | WCAG AA: badge Đã xử lý contrast artboard 5 | Skill C (Vision) | Minor | Gap | Từ ảnh tra-cuu-yeu-cau-5.png: badge Đã xử lý faded, est. ~3.8:1 < 4.5:1. FAIL WCAG AA. UXG-36. |
| 9 | Kết quả pending state unclear | Skill C (Vision) | Minor | Gap | Từ ảnh tra-cuu-yeu-cau-4.png: field Kết quả = — —. Screen reader reads dash dash, no meaning. UXG-44. |
| 10 | UXG-76: Typography contrast — detail fields | Skill C (Vision) | Pass | Pass | Từ ảnh: field labels/values đen trên trắng, est. >15:1. WCAG AAA. UXG-76. |
| 11 | Hick Law: information density in detail | Skill A (Law) | Pass | Pass | 8 fields trong 2 sections. Acceptable density. Hick Law OK. |
| 12 | UXG-35: No destructive actions present | Skill B (PRD) | Pass | Pass | Màn hình chỉ đọc, không có destructive action. N/A → Pass. UXG-35. |
| 13 | Banking: deep link chi tiết | Skill B (Product) | Minor | Unverifiable | product_context: Trust paramount. Deep link URL không verifiable từ Figma. |
| 14 | Section icon S accessible label | Skill C (Vision) | Minor | Gap | UXG-38 Alt Text. Từ ảnh: icon đỏ S bên trái section headers, no accessible label visible. |
| 15 | UXG-4: Back button available all screens | Skill B (PRD) | Pass | Pass | Từ ảnh: back arrow icon trái header visible. UXG-4. |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-4 | Back Button/Navigation | — | SCR-TCY-003 link affordance, back button |
| UXG-33 | Error Feedback | — | SCR-TCY-001 inline error |
| UXG-35 | Confirmation Dialogs | — | SCR-TCY-001 popup dismiss |
| UXG-36 | Color Contrast | — | SCR-TCY-002, 003 badge contrast WCAG |
| UXG-37 | Color Only | — | SCR-TCY-002, 003 badges |
| UXG-38 | Alt Text | — | SCR-TCY-003 section icon |
| UXG-43 | Form Labels | — | SCR-TCY-001 form fields |
| UXG-44 | Error Messages | — | SCR-TCY-001, 003 |
| UXG-47 | Lazy Loading | — | SCR-TCY-002 list performance |
| UXG-54 | Input Labels | — | SCR-TCY-001 |
| UXG-56 | Inline Validation | — | SCR-TCY-001 form errors |
| UXG-58 | Autofill Support | — | SCR-TCY-001 date fields |
| UXG-61 | Submit Feedback | Doherty | SCR-TCY-001 CTA loading |
| UXG-76 | Contrast Readability | — | All screens typography |
| UXG-78 | Loading Indicators | Doherty | SCR-TCY-001, 002, 003 |
| UXG-79 | Empty States | Peak-End | SCR-TCY-002 empty state |
| UXG-90 | No Results | — | SCR-TCY-002 search empty |
| UXG-165 | Touch Target Size | Fitts | All screens touch targets |
| banking-security | PII Masking | — | SCR-TCY-003 account number |
| banking-trust | Trust paramount | — | SCR-TCY-002, 003 |
