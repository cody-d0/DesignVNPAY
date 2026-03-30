# SCR-TK4-004 — Xác thực khuôn mặt — Kết quả › Kết quả giao dịch

**Screen ID:** SCR-TK4-004  
**Flow:** Thay đổi phương thức tất toán/ rút gốc  
**Product:** CoopBank Mobile Banking  
**Domain:** Banking  
**Screen Type:** result  
**Artboards:** 1504  
**Wireframes:** `ui/1504-yoi-phuong-thuc-tat-toan.png`

---

## 1. Overview

Màn hình báo kết quả xác thực khuôn mặt thất bại. Ảnh khuôn mặt được chụp không đạt tiêu chuẩn. Hệ thống hiển thị viền đỏ oval trên ảnh khuôn mặt. Người dùng có thể chọn **Thử lại** để quay về màn hình chụp hoặc **Thoát** để kết thúc flow.

**Mục tiêu người dùng:**
- Nhận phản hồi về lỗi xác thực và quyết định thử lại hoặc thoát

**Màn hình liên quan:**
- ← SCR-TK4-003 (từ auto-capture)
- → SCR-TK4-003 (khi "Thử lại")
- → Thoát khỏi flow (khi "Thoát")

---

## 2. User Story

> Là **khách hàng Co-opBank**, tôi muốn **nhận phản hồi rõ ràng khi xác thực khuôn mặt thất bại** để **có thể thử lại hoặc thoát ra an toàn**.

**Acceptance Criteria:**
- Hiển thị ảnh khuôn mặt đã chụp với viền đỏ báo lỗi
- Thông báo lỗi rõ ràng: "Ảnh xác thực khuôn mặt không hợp lệ. Quý khách vui lòng thử lại"
- 2 CTA: Thoát (kết thúc) và Thử lại (retry)
- Guidance về lý do thất bại (ánh sáng, góc mặt, v.v.)

---

## 3. Screen Content (OCR)

| Element | Text |
|:--------|:-----|
| Header | Xác thực khuôn mặt |
| Error message | Ảnh xác thực khuôn mặt không hợp lệ. Quý khách vui lòng thử lại |
| Exit CTA | Thoát |
| Retry CTA | Thử lại |

---

## 4. Flow & Navigation

```
[SCR-TK4-003 — auto-capture]
  ↓ capture failed
  → [Error result: viền đỏ + thông báo lỗi]
      ├─ "Thử lại" → SCR-TK4-003
      └─ "Thoát" → exit flow (về màn hình trước)
```

---

## 5. Non-Functional Requirements

- **Error specificity:** Lý do lỗi cụ thể (ánh sáng, góc, che khuất) giúp user sửa
- **Max retry attempts:** Cần xác định giới hạn retry để tránh brute force
- **Session timeout:** Xử lý session hết hạn trong quá trình retry
- **Image privacy:** Ảnh chụp không được lưu lại sau khi verify thất bại

---

## 6. UX Signal Analysis (Phase 4e)

**Signals detected:**
- `"Ảnh xác thực khuôn mặt không hợp lệ"` → generic error → lacks specific reason → UX gap
- `"Thoát"` + `"Thử lại"` → binary choice → primary action (Thử lại) should be more prominent
- Viền đỏ oval → error visual feedback → good signal but may be anxiety-inducing
- Không có guidance về cách sửa lỗi → user may retry with same failure

**UX Laws triggered:**
- **Error Recovery (Nielsen Heuristic 9):** Error message không có hướng dẫn cụ thể → gap
- **Fitts' Law:** 2 buttons side-by-side (Thoát | Thử lại) — verify touch target size ≥ 44px
- **Psychology of Progress:** Không có retry count → user không biết còn bao nhiêu lần thử
