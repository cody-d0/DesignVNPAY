# SCR-PIN-003 — Xác thực khuôn mặt › Xác minh sinh trắc học

> **Module:** Dịch vụ thẻ | **Section:** Đặt mã PIN thẻ | **Flow Stage:** Verify  
> **Screen ID:** SCR-PIN-003 | **Type:** Xác minh sinh trắc học  
> **Primary image:** `ui/02a.png`

---

## Section 1 — Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Tên màn hình | Xác thực khuôn mặt |
| Loại màn hình | Biometric verification |
| URL/Deeplink | `coopbank://card/pin/face-auth` |
| Platform | iOS + Android |
| Flow stage | Verify (biometric step) |
| Preceding screen | Cài đặt mã PIN — CTA "Tiếp tục" (SCR-PIN-002) |
| Succeeding screen | Trở về SCR-PIN-002 (overlay Thành công) |

---

## Section 2 — Mô tả chức năng

Màn hình **Xác thực khuôn mặt** là bước xác minh sinh trắc học trước khi hoàn tất cài đặt PIN. Cung cấp:

- **Camera viewfinder dạng oval** — Khung hình nhận diện khuôn mặt
- **Instruction banner** — "Đưa mặt vào giữa khung hình" — nổi bật trên nền tối
- **Minimal UI** — Camera chiếm phần lớn màn hình, tối giản tối đa distraction

Sau khi nhận diện thành công → tự động trở về SCR-PIN-002 → hiển thị overlay **Thành công**.

---

## Section 3 — Nội dung văn bản (OCR)

| Element | Text | Role |
|---|---|---|
| Page title | Xác thực khuôn mặt | header_title |
| Instruction banner | **Đưa mặt vào giữa khung hình** | instruction_prominent |
| Camera region | (camera preview / demo face) | camera_viewfinder |

---

## Section 4 — Icons & Interactions

| Icon | Vị trí | Category | Action |
|---|---|---|:---|
| ic_back | Top-left | nav | Quay lại Cài đặt mã PIN |
| ic_face_frame_oval | Center screen | decoration | Khung nhận diện khuôn mặt |

---

## Section 5 — UX Gaps (Preliminary)

1. **No loading/progress indicator** — Sau khi camera phát hiện khuôn mặt, không rõ có loading state nào hiển thị trong khi processing không
2. **No retry CTA** — Nếu nhận diện thất bại, không thấy CTA "Thử lại" hay hướng dẫn fallback trong design
3. **No permission denied state** — Không có artboard cho trường hợp user từ chối camera permission
4. **Instruction contrast** — Banner instruction dùng màu nền tối + text trắng — cần kiểm tra WCAG AA contrast ratio
5. **Biometric flow context gap** — Người dùng không được thông báo *tại sao* cần xác thực khuôn mặt trong flow đặt PIN thẻ (jump từ PIN entry sang face auth đột ngột, không có bridge explanation)

---

## Section 6 — UX Signal Inference (Phase 4e)

> **Scope:** `screen` | **scope_id:** `SCR-PIN-003` | **Domain:** `banking`  
> **Patterns matched:** `biometric_instruction` (manual — không có matching pattern trong registry)  
> **Note:** minimal text signals (2 strings) — inference chủ yếu từ context + icon

### Flows inferred

| Signal | Flow | DDL Ref |
|---|---|---|
| `biometric_auth_flow` — Camera oval + instruction text | Camera idle → face detect → process → result; processing step MISSING loading feedback | `ux-guidelines.csv#153` |
| `single_step_terminal` — Minimal UI, no CTA visible | Terminal screen: auto-advance sau recognition | — |

### Components inferred

| Component | Pattern ID | State inferred | DDL Ref |
|---|---|---|---|
| `camera_viewfinder_oval` | biometric_frame | idle (current) — missing: **processing state**, **error state** | `ux-guidelines.csv#221` |
| `instruction_banner` | contextual_instruction | "Đưa mặt vào giữa khung hình" — dark bg, white text | `ux-guidelines.csv#153` |

### UX Improvements (prd_extension)

1. **Thêm processing indicator khi face detected** — Vòng quay animation trong/quanh oval frame; thay đổi màu viền (navy → xanh lá)  
   `ddl_ref: ux-guidelines.csv#221 (Loading Indicators)`, `ux-guidelines.csv#153`
2. **Thêm trạng thái lỗi + retry** — Sau 10s hoặc 3 lần fail: hiển thị overlay "Không nhận diện được, thử lại?"  
   `ddl_ref: ux-guidelines.csv#176 (Error Feedback)`
3. **Bridge explanation** — Thêm 1 dòng text nhỏ bên dưới instruction: "Để xác nhận danh tính trước khi lưu mã PIN"  
   `ddl_ref: ux-guidelines.csv#153`
4. **WCAG AA verify** — Kiểm tra contrast ratio instruction banner: white #FFFFFF trên dark overlay — cần ≥4.5:1  
   `ddl_ref: ux-guidelines.csv#180 (Color Only)`
