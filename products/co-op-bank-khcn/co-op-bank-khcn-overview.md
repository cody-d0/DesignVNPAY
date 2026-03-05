# Co-op Bank KHCN — Tổng quan sản phẩm

Tài liệu này cung cấp cái nhìn tổng thể về ứng dụng ngân hàng hợp tác (Co-op Bank) KHCN, tập trung vào tính năng Danh bạ thụ hưởng.

---

## Mục lục
1. [Chân dung khách hàng](#1-chân-dung-khách-hàng)
2. [Tổng quan sản phẩm](#2-tổng-quan-sản-phẩm)
3. [Tính năng chính](#3-tính-năng-chính)
4. [Phạm vi sản phẩm](#4-phạm-vi-sản-phẩm)
5. [Hệ thống cần tích hợp](#5-hệ-thống-cần-tích-hợp)
6. [Success Metrics](#6-success-metrics)
7. [User Flow chính](#7-user-flow-chính)
8. [Cấu trúc tài liệu PRD](#8-cấu-trúc-tài-liệu-prd)

---

## 1. Chân dung khách hàng
- **Đối tượng:** Khách hàng cá nhân sử dụng dịch vụ chuyển tiền của Co-op Bank.
- **Quy mô:** Người dùng di động (mobile-first).
- **Lĩnh vực:** Ngân hàng bán lẻ, chuyển tiền nội bộ và chuyển tiền nhanh 24/7.
- **Nhu cầu:** Quản lý danh bạ thụ hưởng, tìm kiếm và chọn người nhận nhanh, thêm/xóa/cập nhật thông tin danh bạ, thực hiện giao dịch từ danh bạ.

---

## 2. Tổng quan sản phẩm
**Co-op Bank KHCN** là ứng dụng ngân hàng di động cho phép khách hàng quản lý danh bạ thụ hưởng và thực hiện chuyển tiền (nội bộ, chuyển nhanh 24/7 qua tài khoản, qua thẻ).

- **Đơn vị tham khảo:** Ứng dụng ngân hàng số (MB Bank, BIDV, Vietcombank…).
- **Giá trị cốt lõi:** Tiện lợi — An toàn — Quản lý danh bạ rõ ràng.

---

## 3. Tính năng chính
| STT | Tên tính năng | Mô tả |
|:---:|---|---|
| 1 | Danh sách thụ hưởng | Xem danh sách danh bạ theo nhóm (nội bộ, 24/7 tài khoản, 24/7 thẻ); chế độ chọn xóa; FAB thêm mới. |
| 2 | Tìm kiếm danh bạ | Ô tìm kiếm placeholder "Tìm kiếm"; lọc danh sách theo tên hoặc số tài khoản. |
| 3 | Chi tiết danh bạ | Xem thông tin read-only (loại chuyển tiền, tên, số TK, ngân hàng); sửa Tên gợi nhớ; nút Cập nhật và Thực hiện giao dịch. |
| 4 | Thêm mới danh bạ | Form: Loại chuyển tiền (dropdown), Số tài khoản/Số thẻ, Tên gợi nhớ; nút "Thêm mới". |
| 5 | Popup xác nhận xóa | Dialog "Thông báo" xác nhận xóa 02 danh bạ; nút "Không" và "Đồng ý". |

---

## 4. Phạm vi sản phẩm

### 4.1. In Scope (MVP)
- Danh bạ thụ hưởng: danh sách theo nhóm, tìm kiếm, thêm/sửa/xóa, chi tiết danh bạ, xác nhận xóa (dialog).
- Chuyển tiền nội bộ và chuyển tiền nhanh 24/7 (qua tài khoản, qua thẻ) — tham chiếu từ màn hình.

### 4.2. Out of Scope & Roadmap
- **Tích hợp backend:** Chi tiết API lưu/xóa/cập nhật danh bạ sẽ bổ sung trong giai đoạn kỹ thuật.
- **Đa ngân hàng:** Danh sách ngân hàng thụ hưởng (vd. BIDV) có thể mở rộng theo API ngân hàng.

---

## 5. Hệ thống cần tích hợp
- **Core Banking / Chuyển tiền:** API tra cứu tài khoản, xác thực và thực hiện giao dịch chuyển tiền (nội bộ, 24/7).
- **Danh bạ:** Lưu trữ và đồng bộ danh bạ thụ hưởng (create, read, update, delete).

---

## 6. Success Metrics
- **Số lượng danh bạ:** Số danh bạ thụ hưởng được thêm mới và sử dụng lại.
- **Tỷ lệ giao dịch từ danh bạ:** Phần trăm giao dịch bắt nguồn từ màn Danh bạ thụ hưởng.
- **Trải nghiệm:** Thời gian hoàn thành thao tác thêm/xóa/cập nhật danh bạ.

---

## 7. User Flow chính
1. **Danh bạ:** Mở Danh bạ thụ hưởng → Tìm kiếm / Mở rộng thu gọn nhóm → Chọn một danh bạ → Xem Chi tiết danh bạ.
2. **Thêm mới:** Từ Danh bạ → Chạm FAB "Thêm" → Nhập Loại chuyển tiền, Số tài khoản/Số thẻ, Tên gợi nhớ → Chạm "Thêm mới".
3. **Chỉnh sửa / Giao dịch:** Từ Chi tiết danh bạ → Cập nhật "Tên gợi nhớ" hoặc "Thực hiện giao dịch".
4. **Xóa:** Từ Danh bạ → Chạm icon Xóa → Chọn danh bạ cần xóa → Xác nhận trong dialog "Thông báo" (Không / Đồng ý).

---

## 8. Cấu trúc tài liệu PRD

Dưới đây là danh sách các tài liệu PRD chi tiết cho tính năng Danh bạ thụ hưởng (mỗi màn hình một tài liệu):

| STT | Tài liệu | Mô tả chức năng |
|:---:|---|---|
| 1 | [Danh sách thụ hưởng](./co-op-bank-khcn/package-2/danh-ba-thu-huong/danh-sach-thu-huong.md) | Danh sách theo nhóm, chế độ chọn xóa, FAB thêm mới. |
| 2 | [Tìm kiếm](./co-op-bank-khcn/package-2/danh-ba-thu-huong/tim-kiem.md) | Ô tìm kiếm và lọc danh bạ theo từ khóa. |
| 3 | [Chi tiết danh bạ](./co-op-bank-khcn/package-2/danh-ba-thu-huong/chi-tiet-danh-bach.md) | Thông tin read-only, sửa Tên gợi nhớ, Cập nhật và Thực hiện giao dịch. |
| 4 | [Thêm mới danh bạ](./co-op-bank-khcn/package-2/danh-ba-thu-huong/them-moi-danh-bach.md) | Form thêm danh bạ: Loại chuyển tiền, Số TK/Số thẻ, Tên gợi nhớ. |
| 5 | [Popup xác nhận xóa](./co-op-bank-khcn/package-2/danh-ba-thu-huong/popup-xac-nhan-xoa.md) | Dialog xác nhận xóa danh bạ đã chọn. |

---

## Kết quả chạy pipeline (Phase Report)

| Phase | Kết quả |
|-------|---------|
| **Phase 0** | Bỏ qua (node_id trỏ section "Danh bạ thụ hưởng", không phải page). 0b-bis: mockup capability check passed. |
| **Phase 1** | file_key: kPft93N2A3gYOC3YwuXpQR, node_id: 5199:5932; 1 section, 15 artboards; 15 ảnh lưu vào `co-op-bank-khcn/co-op-bank-khcn/package-2/danh-ba-thu-huong/ui/`. |
| **Phase 2** | 5 screens (screen_boundaries: danh-sach-thu-huong, tim-kiem, chi-tiet-danh-bach, them-moi-danh-bach, popup-xac-nhan-xoa); OCR đã chạy 2 round vision (text, icon+vị trí) cho 5 màn có ảnh; ocr_screen_context / ocr_ux_improvements đã sinh; `.handoff/.ocr_done` đã ghi. |
| **Phase 3** | feature_file_plan: 5; 1 overview + 5 feature files. |
| **Phase 4** | Augment (ui-ux-pro-max) trong từng feature file. **Mockup 1 (trước cải thiện):** đã tạo → `.mockups/before/mockup-before-ux-improve.png`. |
| **Phase 5** | 6 file .md đã ghi (1 overview + 5 feature); output_dir: co-op-bank-khcn. **Mockup 2 (sau cải thiện):** đã tạo → `.mockups/after/mockup-after-ux-improve.png`. |

**Comparison mockups:** Màn hình đại diện: Danh sách thụ hưởng (danh-sach-thu-huong).
- Mockup 1 (trước cải thiện UX): `co-op-bank-khcn/.mockups/before/mockup-before-ux-improve.png`
- Mockup 2 (sau cải thiện UX): `co-op-bank-khcn/.mockups/after/mockup-after-ux-improve.png`

---

*Generated by VNPAY Agentic Framework*
