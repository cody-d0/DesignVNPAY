# UX Review Report — Co-opBank KHCN · Xem nhanh mã QR

## Tổng quan
- Folder: coopbank/final/Xem nhanh mã QR
- Số màn hình: 5 | Tổng check: 40
- Pass: 30 | Gap: 10 | Unverifiable: 0
- UX Score (Simple): 75% (30/40)
- UX Score (Weighted): 100%
- Proposals: 🔴 Critical: 1 | 🟡 Major: 3 | ⚪ Minor: 6 | Total: 10

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-3 |
| **Gap ref** | Check #4 |
| **DDL** | UXG-165 · Law:fitts |
| **Giải pháp** | Thêm loading spinner, disable button khi đang xử lý; Hiển thị progress indicator trước khi chuyển sang popup kết quả |

---


**Total checks:** 39  
**Pass:** 30 | **Gap:** 9 | **Unverifiable:** 0  
**Simple Score:** 77%  
**Weighted Score:** 77%#### UXP-002 · Major
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-3 |
| **Gap ref** | Check #5 |
| **DDL** | UXG-243 · Law:peak-end |
| **Giải pháp** | Thêm icon shield/security phía trên title; Đổi "Thông báo" → "Xác nhận bảo mật"; Highlight từ "không cần đăng nhập" bằng màu warning |

---

#### UXP-003 · Major
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-2 |
| **Gap ref** | Check #6 |
| **DDL** | UXG-78 |
| **Giải pháp** | Tách thành warning card với icon ⚠️ + 2 bullet points ngắn; Collapse mô tả chi tiết, chỉ hiện warning icon + text ngắn |

---

#### UXP-004 · Major
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-10 |
| **Gap ref** | Check #5 |
| **DDL** | UXG-52 · Law:hicks |
| **Giải pháp** | Đổi "Cài đặt ngay" → "Đăng nhập để cài đặt"; Sau đăng nhập tự động redirect đến màn Cài đặt QR; Thêm "Bạn sẽ được hướng dẫn sau khi đăng nhập" |

---

#### UXP-005 · Minor
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-4 |
| **Gap ref** | Check #4, Check #5, Check #6 |
| **DDL** | UXG-10 · Law:doherty |
| **Giải pháp** | Auto-dismiss sau 2-3 giây, giữ "Đóng" cho dismiss sớm |

---

#### UXP-006 · Minor
| **Màn hình** | Xem nhanh mã QR › Chi tiết |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-16 |
| **Gap ref** | Check #5 |
| **DDL** | UXG-32 · Law:fitts |
| **Giải pháp** | Thêm dots indicator (●○○) dưới QR code; Hoặc hiển thị "1/3" bên cạnh tên TK |

---

#### UXP-007 · Minor
| **Màn hình** | Xem nhanh mã QR › Tính năng |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-12 |
| **Gap ref** | Check #3 |
| **DDL** | UXG-78 · Law:hicks |
| **Giải pháp** | Chỉ hiển thị badge trên tabs có thông tin mới thực sự; Ẩn khi camera active, chỉ hiện khi user tap vùng dưới |

---

#### UXP-008 · Minor
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh xem-nhanh-ma-qr-9 |
| **Gap ref** | Check #8 |
| **DDL** | UXG-32 |
| **Giải pháp** | Đảm bảo nội dung trong safe area, CTA padding ≥16px từ edge |

---

#### UXP-009 · Minor
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Màn hình hiển thị 2 tài khoản với toggle |
| **Gap ref** | Check #7 |
| **DDL** | COMP:empty-state-1 |
| **Giải pháp** | Thiết kế empty state theo DDL spec: icon 48px + title + CTA |

---

#### UXP-010 · Minor
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh popup-touch-id |
| **Gap ref** | Check #7 |
| **DDL** | UXG-88 |
| **Giải pháp** | Thống nhất dùng "Đóng" hoặc "Hủy xác thực" cho rõ ý |

---

## Chi tiết theo màn hình

### 1. Xem nhanh mã QR › Danh sách
> `SCR-QR-001` · list · 1 artboard
>
> **Score: 86% | Pass: 6 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-1.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Contrast đủ cho menu text | Skill C | UXG-165 | Pass | Từ ảnh: Text đen trên nền trắng, đủ contrast |
| 2 | Touch target ≥44px cho menu items | Skill C | UXG-32 | Pass | Từ ảnh: Mỗi row menu cao ~56px |
| 3 | Tab bar icons có label | Skill C | COMP:bottom-tab-bar-1 | Pass | Từ ảnh: 5 tabs đều có icon + text label |
| 4 | Dropdown chevron cho expandable items | Skill C | — | Pass | Từ ảnh: Soft OTP và Quản lý danh bạ có chevron |
| 5 | Active tab state rõ ràng | Skill C | COMP:bottom-tab-bar-1 | Pass | Từ ảnh: Tab "Cài đặt" có highlight khác biệt |
| 6 | Hick's Law — số lượng menu items hợp lý | Skill A | hicks | ⚠️ Gap | Từ ảnh: 9 menu items + 5 tabs = 14 choices. Trigger: ≥5 interactive |
| 7 | Fitts's Law — menu items dễ tap | Skill A | fitts | Pass | Từ ảnh: rows 56px, full-width, dễ tap |

### 2. Xem nhanh mã QR › Form nhập thông tin
> `SCR-QR-002` · form · 7 artboards
>
> **Score: 60% | Pass: 6 | Gap: 4 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-2.png, xem-nhanh-ma-qr-3.png, xem-nhanh-ma-qr-4.png, xem-nhanh-ma-qr-5.png, xem-nhanh-ma-qr-6.png, xem-nhanh-ma-qr-7.png, xem-nhanh-ma-qr-8.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header có back + home buttons | Skill C | COMP:app-header-1 | Pass | Từ ảnh: ic_back trái, ic_home phải |
| 2 | Toggle switch có ON/OFF state rõ ràng | Skill C | — | Pass | Từ ảnh: Toggle OFF xám, ON xanh dương có check |
| 3 | Popup confirm có nút primary + secondary | Skill C | — | Pass | Từ ảnh: "Đóng" (secondary) + "Đồng ý" (primary bold) |
| 4 | Loading state khi toggle action | Skill C | UXG-165 | Gap | Từ ảnh xem-nhanh-ma-qr-3.png: Không loading giữa confirm và success → UXP-001 |
| 5 | Popup title phù hợp context bảo mật | Skill C | UXG-243 | Gap | Từ ảnh xem-nhanh-ma-qr-3.png: Title "Thông báo" generic → UXP-002 |
| 6 | Mô tả bảo mật scannable | Skill C | UXG-78 | Gap | Từ ảnh xem-nhanh-ma-qr-2.png: Wall of text → UXP-003 |
| 7 | Empty state coverage | Skill A | COMP:empty-state-1 | Gap | Không có artboard cho TK rỗng → UXP-009 |
| 8 | Fitts's Law — toggle size đủ lớn | Skill A | fitts | Pass | Từ ảnh: Toggle ~48px width, đủ target |
| 9 | Peak-End Rule — kết thúc tích cực | Skill A | peak-end | Pass | Từ ảnh xem-nhanh-ma-qr-4.png: Check icon + success message |
| 10 | Hick's Law — limited choices | Skill A | hicks | Pass | Từ ảnh: 2 TK, mỗi TK 1 toggle = clear decision |

### 3. Xem nhanh mã QR › Form nhập thông tin
> `SCR-QR-003` · form · 5 artboards
>
> **Score: 75% | Pass: 9 | Gap: 3 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-9.png, xem-nhanh-ma-qr-10.png, xem-nhanh-ma-qr-14.png, xem-nhanh-ma-qr-15.png, popup-touch-id.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Login form có label cho input fields | Skill C | COMP:text-input-1 | Pass | Từ ảnh xem-nhanh-ma-qr-14.png: "Số điện thoại" + "Mật khẩu" labels |
| 2 | Password eye toggle | Skill C | COMP:text-input-1 | Pass | Từ ảnh: ic_eye_toggle bên phải field Mật khẩu |
| 3 | Biometric option visible | Skill C | — | Pass | Từ ảnh xem-nhanh-ma-qr-9.png: Fingerprint icon cạnh Đăng nhập |
| 4 | QR shortcuts visible và accessible | Skill C | UXG-32 | Pass | Từ ảnh: "Quét QR" + "QR của tôi" icon + label, đủ size |
| 5 | Popup "Cài đặt ngay" flow clarity | Skill C | UXG-52 | Gap | Từ ảnh xem-nhanh-ma-qr-10.png: Nút chưa rõ flow → UXP-004 |
| 6 | Popup kích hoạt ứng dụng actionable | Skill C | — | Pass | Từ ảnh xem-nhanh-ma-qr-15.png: Message rõ "cần kích hoạt trước" |
| 7 | Touch ID popup wording consistency | Skill C | UXG-88 | Gap | Từ ảnh popup-touch-id.png: "Hủy" vs "Đóng" → UXP-010 |
| 8 | Banner CTA touch target | Skill C | UXG-32 | Gap | Từ ảnh xem-nhanh-ma-qr-9.png: "Chi tiết" gần edge → UXP-008 |
| 9 | Fitts's Law — CTA size đủ lớn | Skill A | fitts | Pass | Từ ảnh: Nút "Đăng nhập" full-width, đủ height |
| 10 | Hick's Law — decision complexity | Skill A | hicks | Pass | Từ ảnh: Login có ít choices, clear primary action |
| 11 | Auto-dismiss success popup | Skill C | UXG-10 | Pass | Popup kích hoạt chỉ có 1 nút "Đóng", phù hợp cho error-type |
| 12 | Forgot password accessible | Skill C | — | Pass | Từ ảnh: "Quên mật khẩu?" link visible dưới CTA |

### 4. Xem nhanh mã QR › Tính năng
> `SCR-QR-004` · feature · 1 artboard
>
> **Score: 80% | Pass: 4 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-12.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Camera guideline text rõ ràng | Skill C | UXG-165 | Pass | Từ ảnh: Mô tả rõ ràng cách quét |
| 2 | Partner logos visible | Skill C | — | Pass | Từ ảnh: napas 247, VNPAY QR hiển thị đầy đủ |
| 3 | Tab bar badges visual noise | Skill C | UXG-78 | Gap | Từ ảnh: 5/5 tabs có badge đỏ → UXP-007 |
| 4 | Back navigation accessible | Skill C | COMP:app-header-1 | Pass | Từ ảnh: ic_back góc trái trên |
| 5 | Camera action buttons accessible | Skill C | UXG-32 | Pass | Từ ảnh: gallery + flashlight icons giữa screen, đủ size |

### 5. Xem nhanh mã QR › Chi tiết
> `SCR-QR-005` · detail · 2 artboards
>
> **Score: 83% | Pass: 5 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-16.png, xem-nhanh-ma-qr-17.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Close X button visible | Skill C | — | Pass | Từ ảnh xem-nhanh-ma-qr-16.png: X button góc phải trên |
| 2 | QR code hiển thị đủ lớn | Skill C | — | Pass | Từ ảnh: QR code ~60% width, đủ để scan |
| 3 | Account info đầy đủ | Skill C | — | Pass | Từ ảnh: Tên, STK, Alias hiển thị rõ |
| 4 | Share + Save actions accessible | Skill C | UXG-32 | Pass | Từ ảnh: "Chia sẻ" + "Lưu ảnh" buttons với icons |
| 5 | Pagination indicator cho multi-account | Skill C | UXG-32 | Gap | Từ ảnh: Arrows trái/phải nhưng thiếu dots → UXP-006 |
| 6 | Fitts's Law — action buttons size | Skill A | fitts | Pass | Từ ảnh: Buttons icon + text, đủ touch target |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-10 | Auto-dismiss Notifications | doherty | SCR-QR-002 success popup không auto-dismiss |
| UXG-32 | Touch Target Spacing | fitts | SCR-QR-003 banner CTA, SCR-QR-005 pagination |
| UXG-52 | Navigation Clarity | hicks | SCR-QR-003 popup flow unclear |
| UXG-78 | Content Scannability | — | SCR-QR-002 wall of text, SCR-QR-004 badge noise |
| UXG-88 | Consistent Microcopy | — | SCR-QR-003 "Hủy" vs "Đóng" |
| UXG-165 | System Feedback / Text Legibility | fitts | SCR-QR-002 loading state missing |
| UXG-243 | Error/Warning Feedback | peak-end | SCR-QR-002 popup title generic |
| COMP:app-header-1 | App header spec | — | All screens header check |
| COMP:bottom-tab-bar-1 | Bottom tab bar spec | — | SCR-QR-001, SCR-QR-004 tab bars |
| COMP:empty-state-1 | Empty state spec | — | SCR-QR-002 missing empty state |
| COMP:text-input-1 | Text input spec | — | SCR-QR-003 login fields |
