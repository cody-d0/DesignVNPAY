# Term Equivalents (Tương đương nghĩa)

Dùng trong Phase 2 **2b-pre**: chuẩn hóa chuỗi từ Figma (layer name, label) về ngôn ngữ canonical trước khi so khớp với component-mapping. Giảm gap khi Figma dùng ngôn ngữ khác (vd. English) so với pattern trong component-mapping (vd. Vietnamese).

**Load:** Phase 2 load file này trước 2b (Component recognition). Khi layer name từ Figma nằm trong **aliases** của một canonical_term → dùng **canonical_term** để match pattern.

---

## Format

- **canonical_term**: Chuỗi ở ngôn ngữ chuẩn (mặc định `vi`), dùng để match với Figma Layer Pattern trong component-mapping.
- **aliases**: Các chuỗi cùng nghĩa (en, vi, viết tắt). So khớp case-insensitive; có thể normalize (lowercase, trim) trước khi tra bảng.

---

## Bảng tương đương

| canonical_term | aliases (cách nhau bằng `;` hoặc dòng) |
|----------------|----------------------------------------|
| số điện thoại | phone; phone number; sdt; tel; số ĐT; mobile; số di động |
| mật khẩu | password; pass; pwd; passwd |
| gửi | submit; send |
| tiếp tục | continue; next |
| quay lại | back; previous; cancel |
| xác nhận | confirm; confirmation; verify |
| đăng nhập | login; sign in; signin |
| đăng ký | register; sign up; signup |
| đăng xuất | logout; sign out; signout |
| quên mật khẩu | forgot password; reset password |
| tìm kiếm | search; find |
| lọc | filter |
| ngày | date; calendar |
| số tiền | amount; money; balance; số dư |
| nội dung | content; description; note; ghi chú |
| tài khoản | account |
| người nhận | recipient; beneficiary |
| chuyển tiền | transfer |
| nút | button; btn; cta |
| ô nhập | input; text field; textfield |
| chọn | select; dropdown; picker |
| bật tắt | switch; toggle |
| hộp kiểm | checkbox; check box |
| radio | radio button; option |
| tiêu đề | header; title |
| chân trang | footer |
| thanh điều hướng | navbar; navigation bar; bottom bar; tab bar |
| modal | dialog; popup |
| thông báo | alert; notice; message; infobox |
| lỗi | error |
| thành công | success |
| đang tải | loading; spinner |
| trống | empty; no data |
| minh họa | illustration; image; icon |
| phân cách | separator; divider |

---

## Ghi chú

- BA/PM có thể bổ sung dòng mới (domain term, ngôn ngữ khác). Giữ format bảng để script/agent parse được.
- Alias quá rộng (vd. "button" cho mọi nút) có thể gây match nhầm — ưu tiên alias theo ngữ cảnh (vd. CTA: submit, send, gửi, tiếp tục).
- Khi không có term equivalent cho chuỗi Figma: chỉ match pattern có sẵn trong component-mapping (hành vi cũ).
