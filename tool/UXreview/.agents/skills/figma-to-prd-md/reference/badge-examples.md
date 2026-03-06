# Ví dụ badge "🤖 by AI" theo từng section XPOS

Dùng khi chạy Phase 4 Augment. Nội dung trong badge **PHẢI dùng đúng format của section tương ứng**. Không tự chế format riêng.

---

## Section 1 — Chân dung khách hàng (Overview, follow xpos-app-overview.md)

```markdown
## 1. Chân dung khách hàng

> **`🤖 by AI`** | Nguồn: search.py --domain product "fintech mobile banking" | Độ tin cậy: Medium
>
> - **Đối tượng:** Người dùng cá nhân 25-45 tuổi, sử dụng smartphone, có tài khoản ngân hàng.
> - **Quy mô:** Cá nhân, 1 tài khoản chính.
> - **Lĩnh vực:** Ngân hàng bán lẻ, chuyển tiền, thanh toán.
> - **Nhu cầu:**
>     - Chuyển tiền nhanh, an toàn mà không cần đến quầy giao dịch.
>     - Theo dõi lịch sử giao dịch và số dư tài khoản theo thời gian thực.
```

---

## Section 1 — User Flow (Feature, follow home.md / order-payment.md)

```markdown
> **`🤖 by AI`** | Nguồn: ux-guidelines.csv#10 + case-study:{competitor} | Độ tin cậy: Medium
>
> ### 1.3. Luồng xử lý lỗi giao dịch
> | Bước | Tên màn hình | Tên hành động | Kết quả |
> |:---:|---|---|---|
> | 1 | Kết quả | Hệ thống nhận lỗi từ API | Hiển thị thông báo "Giao dịch thất bại" kèm mã lỗi |
> | 2 | Kết quả | Chạm "Thử lại" | Quay về màn hình Xác nhận, giữ nguyên thông tin đã nhập |
```

---

## Section 4 — Thiết kế Database (follow register.md, backtick field names)

```markdown
> **`🤖 by AI`** | Nguồn: figma_inferred:{nodeId} | Độ tin cậy: High
>
> ### Entity: Transfer (Giao dịch chuyển tiền)
> | Field | Data Type | Constraint | Description |
> |---|---|---|---|
> | `transfer_id` | UUID | Primary Key | |
> | `from_account` | String(20) | Not Null | Tài khoản nguồn |
> | `to_account` | String(20) | Not Null | Tài khoản đích |
> | `amount` | Decimal | Not Null | Số tiền chuyển |
```

---

## Section 5 — Non-functional requirement (follow order-payment.md, nested 4-space indent)

```markdown
> **`🤖 by AI`** | Nguồn: ux-guidelines.csv#22 + frontend-design#touch_target | Độ tin cậy: High
>
> - **Trải nghiệm:**
>     - Touch target >= 44pt cho mọi interactive element (nút, link, input).
>     - Hiệu ứng chuyển màn hình 150-300ms, tôn trọng `prefers-reduced-motion`.
>     - Focus ring 2px solid cho keyboard navigation.
```

---

## Section 3 — Wireframe (Mô tả màn hình, bảng 4 cột)

```markdown
> **`🤖 by AI`** | Nguồn: ux-guidelines.csv#10: Loading states | Độ tin cậy: High
>
> | STT | Tên màn hình | Loại thành phần | Mô tả |
> |:---:|---|---|---|
> | {N+1} | {Tên màn hình} | Loading State | Hiển thị khi đang xử lý: "Đang xử lý giao dịch..." với spinner. Timeout sau 30s hiển thị "Vui lòng thử lại." |
> | {N+2} | {Tên màn hình} | Success State | Hiển thị: "Chuyển tiền thành công!" với icon ✓ và chi tiết giao dịch. |
> | {N+3} | {Tên màn hình} | Error State | Hiển thị: "Giao dịch thất bại. Vui lòng thử lại." với nút "Thử lại" và nút "Quay về trang chủ". |
> | {N+4} | {Tên màn hình} | Empty State | Hiển thị: "Chưa có giao dịch nào." với illustration và nút CTA. |
```
