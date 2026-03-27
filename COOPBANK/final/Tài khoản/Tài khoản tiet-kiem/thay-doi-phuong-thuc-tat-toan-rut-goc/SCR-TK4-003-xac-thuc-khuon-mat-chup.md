# SCR-TK4-003 — Xác thực khuôn mặt — Chụp › Form nhập thông tin

**Screen ID:** SCR-TK4-003  
**Flow:** Thay đổi phương thức tất toán/ rút gốc  
**Product:** CoopBank Mobile Banking  
**Domain:** Banking  
**Screen Type:** form  
**Artboards:** 1503  
**Wireframes:** `ui/1503-yoi-phuong-thuc-tat-toan.png`

---

## 1. Overview

Màn hình xác thực sinh trắc học bằng khuôn mặt (Facepay/eKYC). Camera live của thiết bị chiếu khuôn mặt người dùng trong khung hình oval. Hỗ trợ voice guide để hỗ trợ người dùng khiếm thị điều chỉnh khuôn mặt.

**Mục tiêu người dùng:**
- Xác thực danh tính bằng khuôn mặt để hoàn tất giao dịch thay đổi phương thức tất toán

**Màn hình liên quan:**
- ← SCR-TK4-002 (trigger: popup "Giao dịch yêu cầu xác thực bằng Facepay")
- → SCR-TK4-004 (sau khi chụp xong)

---

## 2. User Story

> Là **khách hàng Co-opBank**, tôi muốn **xác thực danh tính bằng khuôn mặt** để **hoàn tất thay đổi phương thức tất toán một cách bảo mật**.

**Acceptance Criteria:**
- Camera live stream hiển thị trong khung oval
- Hướng dẫn điều chỉnh khuôn mặt vào đúng vị trí
- Voice guide hỗ trợ người dùng khiếm thị
- Auto-capture khi khuôn mặt đạt tiêu chuẩn

---

## 3. Screen Content (OCR)

| Element | Text |
|:--------|:-----|
| Header | Xác thực khuôn mặt |
| Main instruction | Hãy điều chỉnh sao cho khuôn mặt nằm trong khung hình |
| Secondary instruction | Vui lòng nhìn thẳng |

---

## 4. Flow & Navigation

```
[SCR-TK4-002 popup → Đồng ý]
  ↓
[Camera live — oval frame]
  ↓ auto-capture
  → SCR-TK4-004 (result)
```

---

## 5. Non-Functional Requirements

- **Camera performance:** 30fps minimum; khung oval không bị giật
- **Auto-capture latency:** < 500ms sau khi nhận diện khuôn mặt hợp lệ
- **Voice guidance:** TTS phát hướng dẫn khi user kích hoạt voice icon
- **Privacy:** Camera stream không lưu/ghi ngoài mục đích xác thực
- **Lighting tolerance:** Hoạt động trong điều kiện ánh sáng thấp
- **Accessibility:** Voice over support — mô tả vị trí khung hình

---

## 6. UX Signal Analysis (Phase 4e)

**Signals detected:**
- `"Hãy điều chỉnh sao cho khuôn mặt nằm trong khung hình"` → real-time guidance needed → visual feedback required
- `"Vui lòng nhìn thẳng"` → liveness detection requirement → anti-spoofing
- `"Voice on"` icon → accessibility tool → voice guide active state
- Không có CTA button → auto-capture flow → user anxiety management critical

**UX Laws triggered:**
- **Doherty Threshold:** No visible progress indicator → user uncertainty high → need feedback
- **Fitts' Law:** Voice icon 48×48px at top-right → accessible position ✅
- **Aesthetic-Usability Effect:** Camera UI needs to feel premium/trustworthy for security context
