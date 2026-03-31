# 📋 Chuyển tiền

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `core/`
> **Trích xuất:** 2026-03-28

---

## 16. URD_MB_COOPBANK_CHUYỂN TIỀN

> **Page ID:** `29895952` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29895952

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*8 trang con:*

### 16.1. Màn hình chuyển tiền

> **Page ID:** `29898131` · **Version:** 26
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29898131

#### 1/ Luồng màn hình

##### MH1: Màn hình chuyển tiền

##### MH2: Danh bạ thụ hưởng

#### Mô tả:

#####  MH1: Màn hình chuyển tiền
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Chuyển tiền

 | 2 | 
Nút Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút này, hiển thị màn hình đang thao tác trước đó.

 | 4 | Nút chuyển tiền nội bộ cùng chủ | Icon | Click | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

 | 5 | Nút chuyển tiền nội bộ khác chủ | Icon | Click | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

 | 6 | Nút chuyển tiền nhanh 24/7 qua thẻ | Icon | Click | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

 | 7 | Nút chuyển tiền nhanh 24/7 qua tài khoản | Icon | Click | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

 | 8 | Quản lý danh bạ | Icon | Click | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

##### MH2: Danh bạ thụ hưởng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: DANH BẠ THỤ HƯỞNG

 | 2 | Icon Back | Icon | Click | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Ô tìm kiếm danh bạ
 | 
Textbox
 | 
Input
 | -- | 200 | 
• Cho nhập Freetext
• Tìm kiếm tương đối theo:  tên thụ hưởng (tên gợi nhớ và tên chủ tài khoản đã lưu), tài khoản/ số thẻ thụ hưởng, Ngân hàng thụ hưởng
• Trường hợp không có danh bạ sẽ không hiển thị chức năng này
• Hiển thị dấu "x" cho phép xóa toàn ký tự đã nhập
 | 4 | 
Danh sách danh bạ
 | 
View
 | 
Click
 | -- | -- | 
• Nếu danh sách trống: Hiển thị thông báo: Quý khách chưa có danh bạ thụ hưởng.
• Nếu có, danh bạ sẽ hiển thị theo phân loại theo nhóm, và sắp xếp theo thứ tự: (Chuyển tiền nội bộ → Chuyển tiền nhanh 24/7 qua tài khoản → Chuyển tiền nhanh 24/7 qua thẻ). Các danh bạ trong mỗi nhóm sẽ được sắp theo mức độ thường xuyên sử dụng của danh bạ, khi thực hiện (từ cao tới thấp)
• Các nhóm danh bạ khi chạm vào cho phép thu gọn và mở rộng để xem các danh bạ chi tiết.
• Danh bạ hiển thị gồm các thông tin:
• Logo bank 
• Tên người thụ hưởng (hiển thị tên gợi nhớ, khi có tên gợi nhớ được lưu; nếu không, hiển thị tên được lưu tại bank)
• Số tài khoản thụ hưởng/ Số thẻ thụ hưởng
• Ngân hàng thụ hưởng 
• Nhấn chọn thông tin thụ hưởng trong danh bạ (xử lý chọn theo row), fill dữ liệu gồm:  Tài khoản/ Số thẻ thụ hưởng, Tên thụ hưởng, Ngân hàng thụ hưởng (tùy theo dịch vụ) vào màn hình khởi tạo giao dịch theo loại chuyển tiền tương ứng.
 | 5 | 
Thêm mới danh bạ
 | 
Button
 | 
Click
 | -- | -- | 
Click vào hiển thị màn hình thêm mới danh bạ

#### 2/ Logic xử lý
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn icon chuyển tiền | Client MB | Focus vào màn hình chức năng chuyển tiền
 | 2

 | Nhấn icon chuyển tiền nội bộ cùng chủ

 | Client MB | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Gửi yêu cầu lấy danh sách tài khoản thanh toán cho server
• Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng, thông báo: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ." Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thống báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"
• Có tài khoản thanh toán → Chuyển màn hình khởi tạo giao dịch chuyển tiền nội bộ cùng chủ
 | 3 | Nhấn icon chuyển tiền nội bộ khác chủ | Client MB | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Gửi yêu cầu lấy danh sách tài khoản thanh toán cho server
• Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng, thông báo: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ." Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thống báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"
• Có tài khoản thanh toán → Chuyển màn hình khởi tạo giao dịch chuyển tiền nội bộ khác chủ
 | 4 | Nhấn iocn chuyển tiền nhanh 24/7 qua tài khoản | Client MB | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Gửi yêu cầu lấy danh sách tài khoản thanh toán cho server
• Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng, thông báo: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ." Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thống báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"
• Có tài khoản thanh toán → Chuyển màn hình khởi tạo giao dịch chuyển tiền nhanh 24/7 qua tài khoản
 | 5 | Nhấn icon chuyển tiền nhanh 24/7 qua thẻ | Client MB | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Gửi yêu cầu lấy danh sách tài khoản thanh toán cho server
• Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng, thông báo: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ." Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thống báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"
• Có tài khoản thanh toán → Chuyển màn hình khởi tạo giao dịch chuyển tiền nhanh 24/7 qua thẻ
 | 6 | Nhấn icon quản lý danh bạ | Client MB | Chuyển sang màn hình

---

### 16.2. Chuyển tiền nhanh 24/7 qua thẻ

> **Page ID:** `29895961` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29895961

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia:  KH, Client MB, MB Server, Bank Server, HT Napas
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• KH có gói dịch vụ được phép sử dụng chức năng này
• KH có tài khoản hợp lệ để thực hiện chức năng này
• Kết quả mong muốn:
• KH thực hiện giao dịch thành công
• Tài khoản nguồn được ghi nợ đúng bằng số tiền giao dịch
• Tài khoản đích được ghi có đúng bằng số tiền giao dịch
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Màn hình khởi tạo

##### MH2: Màn hình nhập thông tin số thẻ

##### MH3: Màn hình kết quả kiểm tra số thẻ thụ hưởng thành công

##### MH4: Màn hình pop danh sách số thẻ đã lưu

##### MH5: Màn hình nhập số tiền

##### MH6: Màn hình xác nhận giao dịch

##### MH7: Màn hình kết quả giao dịch

#### Mô tả:

##### a) Màn hình khởi tạo
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền qua thẻ

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
x
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ. 
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
8
 | 
Số thẻ thụ hưởng
 | 
Textbox
 | 
Text
 | 
x
 | 
30
 | 
Mặc định trống 

Placeholder: Số thẻ thụ hưởng

Cho phép nhập/chọn:

• Nếu nhập:
• Cho phép nhập tối đa 30 ký tự số
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý
 | 
10
 | 
Icon danh bạ thụ hưởng
 | 
icon
 | 
click
 | 

 | 

 | 
Nhấn icon danh bạ thụ hưởng → focus màn hình danh sách số thẻ thụ hưởng

 | 
11
 | 
Tên người thụ hưởng
 | 
label
 | 
Read only
 | 

 | 

 | 
Tên người thụ hưởng chỉ hiện lên khi thông tin nhập vào là số thẻ được hệ thống trả kết quả về đúng

 | 
12
 | 
Lưu danh bạ thụ hưởng
 | 
Switch Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi nhập thông tin "Số thẻ thụ hưởng" và có kết quả truy vấn thụ hưởng thành công.

Mặc định: OFF

Cho phép thực hiện switch ON/OFF

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

 | 13 | Tên gợi nhớ | Textbox | Input | 
 | 20 | 
Chỉ hiển thị khi nhập thông tin "Số thẻ thụ hưởng" và có kết quả truy vấn thụ hưởng thành công và nút Lưu danh bạ ở trạng thái ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu
 | 
13
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
X
 | 
13
 | 
Nhập vào ô số tiền::

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 
14
 | 
Đối tượng chịu phí
 | 
Listbox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
15
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về.

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
16
 | 
Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable

##### b) Màn hình danh bạ thụ hưởng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Title | Label | Read only | 
 | 
 | Danh bạ thụ hưởng
 | 2 | Nút "X" | Icon | Click | 
 | 
 | Đóng màn hình popup → Giữ nguyên màn hình khởi tạo giao dịch trước đó
 | 3 | Tìm kiếm | Textbox | Text | 
 | 
 | 
Cho phép tìm kiếm tương đối theo số tài khoản trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại )

 | 4 | Danh sách số thẻ thụ hưởng  | List | Click | 
 | 
 | 
Là danh sách số thẻ lưu tại Danh bạ thụ hưởng, mục Chuyển tiền nhanh 24/7 qua thẻ

Thông tin hiển thị gồm:

• Logo bank
• Tên chủ tài khoản/tên gợi nhớ đã lưu
• Số thẻ thụ hưởng
Nhấn chọn 1 số thẻ → Tham khảo logic xử lý

##### c) Màn hình xác nhận
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read Only | 
 | 
 | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 
5
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin tài khoản nguồn; 

 | 
6
 | 
Số thẻ thụ hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Số thẻ thụ hưởng (bôi đỏ)

 | 
7
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên người thụ hưởng

 | 
9
 | 
Số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ; Số tiền viết bằng chữ tương ứng (bôi đỏ)

 | 
10
 | 
Phí giao dịch và thuế
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ. Dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)

Người chịu phí

 | 
11
 | 
Nội dung giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị nội dung chuyển tiền

 | 
12
 | 
Chọn phương thức xác thực
 | 
Label
 | 
Read

Only
 | 

 | 

 | 

 | 
13
 | 
Phương thức xác thực
 | 
Listbox
 | 
Select
 | 

 | 

 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 
14
 | 
Xác nhận
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mặc định Enable

##### d) Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT 

##### e) Màn hình kết quả
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
2
 | 
icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Quay về màn hình home

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin giao dịch thành công bao gồm các thông tin

• Logo ngân hàng Co-opBank
• Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Chuyển tiền thành công
• Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tên người thụ hưởng
• Số thẻ thụ hưởng
• Ngân hàng thụ hưởng
• Mã giao dịch
• Nội dung
 | 4 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

 | 5 | Lưu ảnh | icon | click | 
 | 
 | Nhấn icon → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

#### 4/ Luồng xử lý

##### a) Màn hình khởi tạo
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Bấm chọn chức năng chuyển tiền nhanh 24/7 qua thẻ
 | 
Client MB
 | 
 Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server

 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | 
1/ Nhận yêu cầu và lấy danh sách tài khoản thanh toán

2/ Kiểm tra và xác định rule được phép thực hiện các loại giao dịch của mỗi tài khoản đến MB server

 | MB server | 
Nhận kết quả lấy danh sách tài khoản thanh toán và phản hồi lại Client

 | 
Client MB
 | 
1/ Nhận kết quả:

• Không thành công:Hiển thị thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau.",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình chuyển tiền
• Thành công: Chuyển bước 2
 2/  Kết quả trả về:

Nếu có tài khoản thanh toán: Hiển thị màn hình popup danh sách tài khoản nguồn, bao gồm các thông tin:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ
Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"

 | 2

 | 
Chọn 1 tài khoản nguồn khác
 | 
Client MB
 | 
Hiển thị danh sách tài khoản nguồn

Hiển thị dấu tích và sẽ hiển thị lên đầu danh sách bản ghi đang được chọn hiện tại.

Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 3

 | 
Nhập số thẻ thụ hưởng 

 | 
Client MB

 | 
Nhập số thẻ thụ hưởng → Thoát focus, validate thông tin:

• Không hợp lệ: Nếu chuỗi ký tự số nhập vào khác điều kiện sau: 
• Có độ dài nhỏ hơn 13 ký tự, thông báo:Số thẻ thụ hưởng không đúng định dạng. Quý khách vui lòng kiểm tra lại.
• Có độ dài trong đoạn [16,25] và bắt đầu bằng dãy số 970446, hiển thị thông báo: Số thẻ là số thẻ nội bộ của Co-opbank. Quý khách vui lòng chọn loại chuyển tiền nội bộ.
• Hợp lệ: Gửi yêu cầu kiểm tra thông tin số thẻ thụ hưởng
 | MB server | Nhận và gửi yêu cầu kiểm tra thông tin người thụ hưởng sang bank server
 | Bank server | Nhận và gửi yêu cầu sang hệ thống Napas
 | HT Napas | Xử lý yêu cầu và phản hồi lại Bank server
 | Bank server | Nhận và gửi lại kết quả cho MB server
 | MB server | 
Nhận kết quả và gửi kết quả lại cho client

 | Client MB | 
Nhận kết quả:

• Không thành công, thông báo lỗi tương ứng với yêu cầu gửi đi (danh sách lỗi do hệ thống Napas trả về): | Case | Tác nhân | Thông báo | Ghi chú
 | Số thẻ thụ hưởng không hợp lệ | Client | Số thẻ thụ hưởng không hợp lệ. Quý khách vui lòng kiểm tra lại! | 

 | Số thẻ thụ hưởng không tồn tại | 
 | Số thẻ thụ hưởng không tồn tại trên hệ thống. Quý khách vui lòng kiểm tra lại! | 

 | Các lỗi khác | Client | Hệ thống tạm thời gian đoạn. Quý khách vui lòng thử lại sau.  | 

• Thành công:
• Hiển thị tên tài khoản thụ hưởng
• Ô nhập tên gợi nhớ
• Nút Lưu thụ hưởng, cho phép khách hàng lưu thông tin người thụ hưởng theo tên gợi nhớ
 | 
5
 | Nhấn icon danh bạ | Client MB | 
Chuyển sang màn hình danh sách số tài khoản thụ hưởng: Kiểm tra danh bạ số tài khoản thụ hưởng đã lấy được trước đó chưa (Chức năng danh bạ chuyển tiền)?

• Nếu chưa lấy trước đó → Gửi lại yêu cầu lấy danh bạ thụ hưởng theo user sang server.
• Nếu đã gọi lấy trước đó → Hiển thị theo kết quả đã lấy được trước đó:
• Có dữ liệu hiển thị danh sách số tài khoản thụ hưởng (màn hình danh bạ thụ hưởng)
• Không có dữ liệu thông báo "Quý khách chưa có danh bạ thụ hưởng."
 | MB server | 
1/ Xử lý yêu cầu:

• Truy vấn danh sách số thẻ đã lưu theo user
• Sắp xếp danh sách số thẻ truy vấn được theo thời gian giao dịch gần nhất
2/ Trả kết quả về cho client

 | Client MB | 
Nhận kết quả

• Không thành công, hiển thị danh sách trống và thông báo lỗi: "Không lấy được danh sách danh bạ. Quý khách vui lòng thử lại sau."
• Thành công:Hiển thị danh sách số tài khoản truy vấn được (màn hình danh bạ thụ hưởng), không có dữ liệu hiển thị thông báo "Quý khách chưa có danh bạ thụ hưởng"
 | 6 | 
Chọn số thẻ thụ hưởng từ danh sách
 | 
Client MB
 | 
Tham khảo logic màn hình danh bạ thụ hưởng

 | 
7
 | 
Nhập số tiền
 | 
Client MB
 | 
Hiển thị dấu “x” trên ô số tiền cho phép xóa toàn bộ ký tự nhập

Gợi ý số tiền chuyển theo quy tắc: <Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG>

 | 8

 | 
Nhấn "Tiếp tục"

 | 
Client MB
 | 
Kiểm tra thông tin validate tại màn hình khởi tạo:

1/ Nếu không hợp lệ, hiển thị thông báo lỗi tương ứng:
 | | 
Case
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Ghi chú

 | Số thẻ thụ hưởng trống | Client | Số thẻ thụ hưởng không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Bỏ trống số tiền | Client | Số tiền không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Bỏ trống nội dung giao dịch | Client | Nội dung giao dịch không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

2/  Nếu hợp lệ: Gửi yêu cầu khời tạo giao dịch sang MB server

 | 
Server MB
 | 
Nhân yêu cầu và kiểm tra:

1/ Kiểm tra Nội dung giao dịch với giá trị tham số TEXT_BLACKLIST:

• Nếu nội dung giao dịch có chưa các chuỗi text được cấu hình tại tham số TEXT_BLACKLIST ->  Trả mã lỗi cho ứng dụng theo thông báo cấu hình là "Giao dịch không thành công do nội dung giao dịch có chứa các đoạn mã không phù hợp. Quý khách vui lòng kiểm tra lại."
• Nếu nội dung GD không bao gồm các chuỗi text trong TEXT_BLACKLIST -> Chuyển bước 2
2/ Kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch. → Tham khảo logic xử lý tại Logic kiểm tra PTXT

• Không hợp lệ: Trả về lỗi như logic validate của PTXT
• Hợp lệ: Kiểm tra nếu Nút lưu danh bạ ở trạng thái ON, thực hiện lưu danh bạ và phản hồi lại client: Gửi kết quả lại cho client bao gồm mã dịch vụ khách hàng đang sử dụng
 | Client MB | 
Nhân kết quả phản hồi từ server:

Hợp lệ: Chuyển sang màn hình Xác nhận giao dịch (MH2)

Không hợp lệ: Hiển thị thông báo lỗi tương ứng. Đóng thông báo, giữ nguyên màn hình hiện tại. <Tham khảo >

##### b) Màn hình danh bạ thụ hưởng
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn icon "X" | Client | Đóng màn hình popup → Giữ nguyên màn hình khởi tạo giao dịch trước đó
 | 2 | Nhập dữ liệu tìm kiếm | Client | 
 Cho tìm kiếm tương đối số thẻ có trong danh sách

Nếu không có kết quả, hiển thị: Không có kết quả tìm kiếm.

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 3 | Nhấn chọn row tương ứng trong danh sách (logo/tên/số thẻ) | Client | 
Quay về màn hình khởi tạo giao dịch trước đó:

• Fill số thẻ thụ hưởng vào ô số thẻ thụ hưởng
• Hiển thị thông tin tên tài khoản thụ hưởng, ngân hàng thụ hưởng
• Nút Lưu thụ hưởng, mặc định switch ON
• Fill tên gợi nhớ vào ô Tên gợi nhớ nếu có. Cho phép chỉnh sửa lại tên gợi nhớ.

##### c) Màn hình xác nhận giao dịch 
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Xác nhận"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại )
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại )
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại )

##### d) Xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Nhập thông tin xác thực và nhấn "Tiếp tục"

 | Client MB | Validate thông tin  (xem tại logic màn hình xác thực giao dịch theo PTXT ) và gửi yêu cầu xác thực sang server
 | MB server | 
Xử lý:

1/ Kiểm tra hiệu lực của giao dịch:

• Không hợp lệ: Trả mã lỗi tương ứng theo PTXT cho client
• Hợp lệ: Chuyển bước tiếp
2/ Gửi yêu cầu hạch toán giao dịch chuyển tiền 247 qua số thẻ NAPAS sang Bank  (API : createNapasFTToCard)

(Bổ sung truyền request tên người nhận (desCardName) -  do tiêu chuẩn kỹ thuật bên bank có sự thay đổi nên cần phải truyền thêm mới đáp ứng đc)

 | Bank server | Thực hiện hạch toán và trả kết quả về cho MB server
 | MB server | 
Nhận, kiểm tra kết quả:

Th

> ⚠️ *Nội dung đã cắt ngắn (16343 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 16.3. Chuyển tiền nhanh 24/7 qua tài khoản

> **Page ID:** `29895959` · **Version:** 20
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29895959

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia:  KH, Client MB, MB Server, Bank Server, HT Napas
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• KH có gói dịch vụ được phép sử dụng chức năng này
• KH có tài khoản hợp lệ để thực hiện chức năng này
• Kết quả mong muốn:
• KH thực hiện giao dịch thành công
• Tài khoản nguồn được ghi nợ đúng bằng số tiền giao dịch
• Tài khoản đích được ghi có đúng bằng số tiền giao dịch
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Màn hình khởi tạo

##### MH2: Màn hình nhập số tài khoản thụ hưởng

##### MH3: Màn hình kết quả kiểm tra thông tin tài khoản thụ hưởng

##### MH4: Màn hình popup danh sách số tài khoản thụ hưởng

##### MH5: Màn hình nhập số tiền

##### MH6: Màn hình xác nhận

##### MH7: Màn hình kết quả

##### MH8: Thay đổi bàn phím

#### Mô tả:

##### a) Màn hình khởi tạo
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền qua tài khoản

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
x
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách bank server trả về
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ. 
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
8
 | 
Tài khoản thụ hưởng
 | 
Textbox
 | 
Text
 | 
x
 | 
30
 | 
Mặc định trống 

Placeholder: Tài khoản thụ hưởng

Cho phép nhập/chọn:

• Nếu nhập:
• Cho phép nhập tối đa 30 ký tự số và chữ
• Nếu dán vào ô tài khoản/số thẻ/số điện thoại mà có khoảng trống ở đầu hoặc/và cuối thì hệ thống tự xóa khoảng trống ở đầu hoặc/và cuối
• Khi focus vào ô tài khoản thụ hưởng, hệ thống hiển thị bàn phím dạng số có icon bàn phím chữ ở phía trên góc trái, cho phép chuyển đổi giữa bàn phím số sang bàn phím chữ và ngược lại. Khi hiển thị bàn phím chữ thì có icon bàn phím số ở phía trên góc trái (MH8)
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý
 | 9 | 
Tên người thụ hưởng
 | 
label
 | 
Read only
 | 

 | 

 | 
Tên người thụ hưởng chỉ hiện lên khi thông tin nhập vào là số tài khoản và ngân hàng thụ hưởng được hệ thống trả kết quả về đúng

 | 10 | Ngân hàng thụ hưởng | Listbox | Select | x | 
 | 
Hiển thị danh sách các ngân hàng mà Co-opBank đã kết nối.

Danh sách ngân hàng thụ hưởng được cấu hình trên Backend do Server trả về.

Yêu cầu hiển thị:

• Thứ tự hiển thị theo back-end trả về
• Hiển thị những thông tin: (<tên viết tắt ngân hàng>) Tên ngân hàng
• Khi dữ liệu trống, hiển thị thông báo: Không có dữ liệu hiển thị.
 | 
11
 | 
Icon danh bạ thụ hưởng
 | 
icon
 | 
click
 | 

 | 

 | 
Nhấn icon danh bạ thụ hưởng → focus màn hình danh sách số tài khoản thụ hưởng(MH4)

 | 
12
 | 
Lưu danh bạ thụ hưởng
 | 
Switch Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi nhập thông tin "Tài khoản thụ hưởng" và có kết quả truy vấn thụ hưởng thành công.

Mặc định: OFF

Cho phép thực hiện switch ON/OFF

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

 | 
 | Tên gợi nhớ | Textbox | Input | 
 | 20 | 
Chỉ hiển thị khi nhập thông tin "Tài khoản thụ hưởng" và có kết quả truy vấn thụ hưởng thành công và nút Lưu danh bạ ở trạng thái ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu
 | 
13
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
X
 | 
13
 | 
Nhập vào ô số tiền::

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 
14
 | 
Đối tượng chịu phí
 | 
Listbox
 | 
Select
 | 
--
 | 
--
 | 
 Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
15
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
16
 | 
Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable

##### b) Màn hình Danh bạ thụ hưởng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Title | Label | Read only | 
 | 
 | Danh bạ thụ hưởng
 | 2 | Nút back | Icon | Click | 
 | 
 | 

 | 3 | Tìm kiếm | Textbox | Text | 
 | 
 | 
Cho phép tìm kiếm tương đối theo số tài khoản trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại )

 | 4 | Danh sách tài khoản thụ hưởng  | List | Click | 
 | 
 | 
Là danh sách tài khoản lưu tại Danh bạ thụ hưởng, mục Chuyển tiền danh 24/7 qua tài khoản

Thông tin hiển thị gồm:

• Logo bank
• Tên chủ tài khoản/tên gợi nhớ đã lưu
• Số tài khoản thụ hưởng
Nhấn chọn 1 số tài khoản → Tham khảo logic xử lý

##### c) Màn hình xác nhận
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read Only | 
 | 
 | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo:
 | 
5
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin tài khoản nguồn; 

 | 
6
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Số tài khoản thụ hưởng (bôi đỏ)

 | 
7
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên người thụ hưởng

 | 
8
 | 
Ngân hàng thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên ngân hàng thụ hưởng (bôi đỏ)

 | 
9
 | 
Số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ; Số tiền viết bằng chữ tương ứng(bôi đỏ)

 | 
10
 | 
Phí giao dịch và thuế
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ

Người chịu phí

Dữ liệu do Server trả về (chỉ hiển thị nếu khác 0 và rỗng)

 | 
11
 | 
Nội dung giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị nội dung chuyển tiền

 | 
12
 | 
Chọn phương thức xác thực
 | 
Label
 | 
Read

Only
 | 

 | 

 | 

 | 
13
 | 
Phương thức xác thực
 | 
Listbox
 | 
Select
 | 

 | 

 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 
14
 | 
Xác nhận
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mặc định Enable

##### d) Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### e) Màn hình kết quả
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
2
 | 
icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin giao dịch thành công bao gồm các thông tin

• Logo ngân hàng Co-opBank
• Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Chuyển tiền thành công
• Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tên người thụ hưởng
• Tài khoản thụ hưởng
• Ngân hàng thụ hưởng
• Mã giao dịch
• Nội dung
 | 4 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

 | 5 | Lưu ảnh | icon | click | 
 | 
 | Nhấn icon → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

#### 4/ Luồng xử lý

##### a) Màn hình khởi tạo
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Bấm chọn chức năng chuyển tiền 24/7 qua tài khoản
 | 
Client MB
 | 
Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server

 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | 
1/ Nhận yêu cầu và lấy danh sách tài khoản thanh toán

2/ Kiểm tra và xác định rule được phép thực hiện các loại giao dịch của mỗi tài khoản đến MB server

 | MB server | 
Nhận kết quả lấy danh sách tài khoản thanh toán và phản hồi lại Client

 | 
Client MB
 | 
1/ Nhận kết quả:

• Không thành công:Hiển thị thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau.",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình chuyển tiền
• Thành công: Chuyển bước 2
 2/  Kết quả trả về:

Nếu có tài khoản thanh toán: Hiển thị màn hình popup danh sách tài khoản nguồn, bao gồm các thông tin:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ
Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"

 | 2 | Lấy danh sách ngân hàng thụ hưởng khi chọn chức năng chuyển tiền 24/7 qua tài khoản | Client MB | Gửi yêu cầu lấy danh ngân hàng thụ hưởng sang server
 | MB server | Xử lý và trả lại kết quả cho client
 | Client MB | 
Nhận kết quả:

• Không thành công, hiển thị thống báo: Không có dữ liệu
• Thành công hiển thị danh sách ngân hàng thụ hưởng theo yêu cầu mô tả trên màn hình
 | 3 | 
Chọn 1 tài khoản nguồn khác
 | 
Client MB
 | 
Hiển thị danh sách tài khoản nguồn

Hiển thị dấu tích và sẽ hiển thị lên đầu danh sách bản ghi đang được chọn hiện tại.

Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 4

 | 
Nhập tài khoản thụ hưởng và chọn ngân hàng thụ hưởng

 | 
Client MB
 | 
1/Nhập tài khoản thụ hưởng và chọn ngân hàng thụ hưởng hoặc chọn ngân hàng thụ hưởng và nhập tài khoản thụ hưởng

Lưu ý: Chọn ngân hàng thụ hưởng

• Hiển thị danh sách ngân hàng mà Co-opBank đã kết nối
• Cho phép tìm kiếm gần đúng theo tên viết tắt và tên đầy đủ của ngân hàng.
2/ Kiểm tra thông tin thụ hưởng: Ngân hàng thụ hưởng và tài khoản thụ hưởng, kiểm tra thông tin tài khoản thụ hưởng và ngân hàng thụ hưởng

• Hợp lệ: Gửi yêu cầu kiểm tra thông tin tài khoản thụ hưởng gồm thông tin: số tài khoản thụ hưởng và ngân hàng thụ hưởng
• Không hợp lệ, thông báo: | Case | Tác nhân | Thông báo  | Ghi chú
 | Tài khoản thụ hưởng trống | Client | Tài khoản thụ hưởng không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Ngân hàng thụ hưởng trống | Client | Ngân hàng thụ hưởng không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | MB server | Nhận và gửi yêu cầu kiểm tra thông tin người thụ hưởng sang bank server
 | Bank server | Gửi yêu yêu cầu kiểm tra thông tin người thụ hưởng sang hệ thống Napas
 | HT Napas | Xử lý yêu cầu và phản hồi lại cho Bank server
 | Bank server | Nhận kết quả và phản hồi lại MB server
 | MB server | 
Nhận kết quả và gửi kết quả lại cho client

 | Client MB | 
Nhận kết quả:

• Không thành công, thông báo lỗi tương ứng nhận được (danh sách lỗi do hệ thống Napas trả về) | | 
Case
 | 
Tác nhân
 | 
Thông báo
 | 
Ghi chú

 | Số tài khoản thụ hưởng không hợp lệ | Client | Số tài khoản thụ hưởng không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

 | Số tài khoản thụ hưởng không tồn tại | Client | Số tài khoản thụ hưởng không tồn tại trên hệ thống. Quý khách vui lòng kiểm tra lại. | 

 | Các lỗi khác | Client | Hệ thống tạm thời gian đoạn. Quý khách vui lòng thử lại sau.  | 

• Thành công:
• Hiển thị tên tài khoản thụ hưởng
• Ô nhập tên gợi nhớ
• Nút Lưu thụ hưởng, cho phép khách hàng lưu thông tin người thụ hưởng theo tên gợi nhớ
 | 
5
 | Nhấn icon danh bạ | Client MB | 
Chuyển sang màn hình danh sách số tài khoản thụ hưởng: Kiểm tra danh bạ số tài khoản thụ hưởng đã lấy được trước đó chưa (Chức năng danh bạ chuyển tiền)?

• Nếu chưa lấy trước đó → Gửi lại yêu cầu lấy danh bạ thụ hưởng theo user sang server.
• Nếu đã gọi lấy trước đó → Hiển thị theo kết quả đã lấy được trước đó:
• Có dữ liệu hiển thị danh sách số tài khoản thụ hưởng (màn hình danh bạ thụ hưởng)
• Không có dữ liệu thông báo "Quý khách chưa có danh bạ thụ hưởng."
 | MB server | 
1/ Xử lý yêu cầu:

• Truy vấn danh sách số tài khoản đã lưu theo user
• Sắp xếp danh sách số tài khoản truy vấn được theo thời gian giao dịch gần nhất
2/ Trả kết quả về cho Client

 | Client MB | 
Nhận kết quả

• Không thành công, hiển thị danh sách trống và thông báo lỗi: "Không lấy được danh sách danh bạ. Quý khách vui lòng thử lại sau."
• Thành công:Hiển thị danh sách số tài khoản truy vấn được (màn hình danh bạ thụ hưởng), không có dữ liệu hiển thị thông báo "Quý khách chưa có danh bạ thụ hưởng"
 | 6 | 
Chọn số tài khoản thụ hưởng từ danh sách
 | 
Client MB
 | 
Tham khảo logic xử lý màn hình Danh bạ thụ hưởng

 | 
7
 | 
Nhập số tiền
 | 
Client MB
 | 
Hiển thị dấu “x” trên ô số tiền cho phép xóa toàn bộ ký tự nhập

Gợi ý số tiền chuyển theo quy tắc: <Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG>

 | 8

 | 
Nhấn "Tiếp tục"

 | 
Client MB
 | 
Kiểm tra thông tin validate tại màn hình khởi tạo:

1/ Nếu không hợp lệ, hiển thị thông báo lỗi tương ứng:
 | | 
Case
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Ghi chú

 | Bỏ trống số tiền | Client | Số tiền không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Bỏ trống nội dung giao dịch | Client | Nội dung giao dịch không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

2/  Nếu hợp lệ: Gửi yêu cầu khời tạo giao dịch sang MB server

 | 
Server MB
 | 
Nhân yêu cầu:

1/ Kiểm tra Nội dung giao dịch với giá trị tham số TEXT_BLACKLIST:

• Nếu nội dung giao dịch có chưa các chuỗi text được cấu hình tại tham số TEXT_BLACKLIST ->  Trả mã lỗi cho ứng dụng theo thông báo cấu hình là "Giao dịch không thành công do nội dung giao dịch có chứa các đoạn mã không phù hợp. Quý khách vui lòng kiểm tra lại."
• Nếu nội dung GD không bao gồm các chuỗi text trong TEXT_BLACKLIST -> Chuyển bước 2
2/ Kiểm tra tài khoản hưởng từ thiện theo tham số CHARITY_ACCOUNT_247 (lưu ý: các giá trị cách nhau bởi dấu phẩy và không chứ khoảng trắng):

• Nếu số tài khoản thụ hưởng trùng với 1 trong các list giá trị cấu hình: Chuyển sang bước 2, kiểm tra hạn mức theo loại giao dịch với số tiền phí = 0 (Giao dịch không mất phí)
• Nếu số tài khoản thụ hưởng không thuộc list giá trị cấu hình: Chuyển sang bước 2
3/ Kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch(nếu có). → Tham khảo logic xử lý tại Logic kiểm tra PTXT

• Không hợp lệ: Trả về lỗi như logic validate của PTXT
• Hợp lệ: Kiểm tra nếu Nút lưu danh bạ ở trạng thái ON, thực hiện lưu danh bạ và phản hồi lại client: Gửi kết quả lại cho client bao gồm mã dịch vụ khách hàng đang sử dụng
 | Client MB | 
Nhận kết quả phản hồi từ server:

Hợp lệ: Chuyển sang màn hình Xác nhận giao dịch

Không hợp lệ: Hiển thị thông báo lỗi

> ⚠️ *Nội dung đã cắt ngắn (18530 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 16.4. Chuyển tiền nội bộ khác chủ

> **Page ID:** `29895957` · **Version:** 27
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29895957

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | Trang VT | 
 | 
Tạo mới
 | V1.0
 | 19/04/2023 | M | HongLT | 
 | 
Cập nhật

• Cập nhật maxlength = 21 ký tự tại trường STK/Số thẻ/ SĐT 
• Cập nhật cho phép dùng bàn phím chữ
• Cập nhật bổ sung logic kiểm tra tài khoản Alias | V2.0

1/ Tác nhân, điều kiện trước, kết quả mong muốn

• 
Tác nhân tham gia:  KH, Client MB, MB Server, Bank Server

• 
Điều kiện trước: 

• 
KH đăng nhập ứng dụng thành công

• 
KH có gói dịch vụ được phép sử dụng chức năng này

• KH có tài khoản hợp lệ để thực hiện chức năng này
• 
Kết quả mong muốn:

• 
KH thực hiện giao dịch thành công

• 
Tài khoản nguồn được ghi nợ đúng bằng số tiền giao dịch

• 
Tài khoản đích được ghi có đúng bằng số tiền giao dịch

2/ Luồng validate STK/Số thẻ/ SĐT/Alias

3/ Luồng màn hình

a) Nhóm màn hình chính

MH1: Màn hình khởi tạo

MH2: Màn hình nhập thông tin tài khoản/số thẻ/số điện thoại thụ hưởng

MH3: Màn hình kết quả kiểm tra thông tin số tài khoản khoản thụ hưởng thành công

MH4: Màn hình kết qủa kiểm tra thông tin số thẻ/số điện thoại thụ hưởng thành công

MH5: Màn hình nhập số tiền

MH6: Màn hình xác nhận khi nhập số tài khoản thụ hưởng

MH7: Màn hình xác nhận khi nhập số thẻ thụ hưởng (nếu nhập số điện thoại sẽ hiển thị số điện thoại thay số thẻ)

MH8: Màn hình kết quả khi nhập số tài khoản thụ hưởng

MH9: Màn hình kết quả khi nhập số thẻ thụ hưởng (nếu nhập số điện thoại sẽ hiển thị số điện thoại thay số thẻ)

b) Nhóm màn hình phụ

MH10: Màn hình danh bạ thụ hưởng (Số tài khoản/số thẻ đã lưu danh bạ)

MH11: Màn hình danh bạ điện thoại 

Màn hình bổ sung

MH12: Thay đổi bàn phím

Mô tả:

a) Màn hình khởi tạo
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nội bộ khác chủ

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
5
 | 
Hạn mức(Đã chốt để phase sau)
 | 
Textlink
 | 
Click
 | 
X
 | 
--
 | 
Nhấn textlink → Điều hướng sang màn hình Thông tin hạn mức, do ngân hàng cũng cấp link và được tích hợp trên app

 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
x
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
8
 | 
Tài khoản thụ hưởng
 | 
Textbox
 | 
Text
 | 
x
 | 
2-21
 | 
Mặc định trống

Placeholder: Số tài khoản/số thẻ/số điện thoại

Cho phép nhập/chọn:

• 
Nếu nhập:

• 
Cho phép nhập tối thiểu 2 và tối đa 21 ký tự số và chữ cái, không bao gồm ký tự đặc biệt (Hiển thị bàn phím số và chữ cái IN HOA) (Cho phép nhập số tài khoản Alias)

• Nếu dán vào ô tài khoản/số thẻ/số điện thoại mà có khoảng trống ở đầu hoặc/và cuối thì hệ thống tự xóa khoảng trống ở đầu hoặc/và cuối
• Nếu điền số điện thoại mà:
• Số điện thoại là alias đã gán với 1TK: Chỉ hiển thị tên khách hàng
• Số điện thoại của khách hàng đang sử dung mobile banking nhưng không là alias: Hiển thị như cũ (tên KH + số TK mặc định)
• Khi focus vào ô tài khoản thụ hưởng, hệ thống hiển thị bàn phím dạng số có icon bàn phím chữ ở phía trên góc trái, cho phép chuyển đổi giữa bàn phím số sang bàn phím chữ và ngược lại. Khi hiển thị bàn phím chữ thì có icon bàn phím số ở phía trên góc trái (MH12)
• 
Thoát focus kiểm tra thông tin thụ hưởng  → Tham khảo logic xử lý

• 
Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý

 | 
9
 | 
Icon danh bạ thụ hưởng
 | 
icon
 | 
click
 | 

 | 

 | 
Nhấn icon danh bạ thụ hưởng → focus màn hình danh bạ số tài khoản/số thẻ thụ hưởng (MH10)

 | 
10
 | 
Tên người thụ hưởng/ Số tài khoản
 | 
label
 | 
Read only
 | 

 | 

 | 
Nếu nhập/chọn số tài khoản thụ hưởng và có kết quả truy vấn thành công: Hiển thị thông tin tên tài khoản

Nếu nhập/chọn số điện thoại/số thẻ thụ hưởng và có kết quả truy vấn thành công: Hiển thị thông tin số tài khoản, tên tài khoản thụ hưởng (Kiểm tra số điện thoại tại hệ thống MB)

 | 
11
 | 
Lưu danh bạ thụ hưởng
 | 
Switch button
 | 
click
 | 
-
 | 
-
 | 
Chỉ hiển thị khi nhập thông tin "Số tài khoản/số thẻ/số điện thoại" và có kết quả truy vấn thụ hưởng thành công.

Mặc định: OFF

Cho phép thực hiện switch ON/OFF

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

 | 
12
 | 
Tên gợi nhớ
 | 
Textbox
 | 
Text
 | 
 | 
20
 | 
Chỉ hiển thị khi nhập thông tin "Số tài khoản/số thẻ/số điện thoại" có kết quả truy vấn thụ hưởng thành công và nút Lưu người thụ hưởng switch ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• 
Nhập ký tự tiếng Việt có dấu

 | 
13
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
X
 | 
13
 | 
Nhập vào ô số tiền::

• 
Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0

• 
Hiển thị ngăn cách hàng nghìn bằng dấu “,”

• 
Hiển thị đơn vị tiền tệ mặc định “VND”

• 
Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 
14
 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
15
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển do Bank server trả về theo danh sách tài khoản nguồn

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Focus ô Nội dung giao dịch → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
16
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable

b) Màn hình danh bạ 
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Title
 | 
Label
 | 
Read only
 | 
 | 
 | 
Danh bạ thụ hưởng

 | 
2
 | 
Nút đóng
 | 
Icon
 | 
Click
 | 
 | 
 | 
Nhấn dấu "X" → Đóng màn hình popup danh bạ

 | 
 | 
Danh bạ
 | 
List
 | 
 | 
 | 
 | 
Gồm 2 tab: Danh bạ thụ hưởng và Danh bạ điện thoại

Mặc định focus màn hình Danh bạ thụ hưởng

 | 
Tab Danh bạ thụ hưởng

 | 
3
 | 
Tìm kiếm
 | 
Textbox
 | 
Text
 | 
 | 
 | 
Cho phép tìm kiếm tương đối theo tên chủ tài khoản/tên gợi nhớ/số tài khoản/số thẻ lưu trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại )

 | 
4
 | 
Danh sách tài khoản thụ hưởng 
 | 
List
 | 
Click
 | 
 | 
 | 
Là danh sách số tài khoản/số thẻ lưu tại Danh bạ thụ hưởng, mục Chuyển tiền nội bộ khác chủ

Thông tin hiển thị gồm:

• 
Logo bank

• 
Tên chủ tài khoản/tên gợi nhớ đã lưu

• 
Số tài khoản thụ hưởng/số thẻ thụ hưởng

Nhấn chọn 1 số tài khoản/số thẻ → Tham khảo logic xử lý

 | 
Tab Danh bạ điện thoại

 | 
5
 | 
Tìm kiếm
 | 
Textbox
 | 
Text
 | 
 | 
 | 
Cho phép tìm kiếm tương đối theo tên/số điện thoại lưu trong danh dạ

Chỉ hiển thị khi có trên n bản ghi (xem tại )

 | 
6
 | 
Danh sách số điện thoại 
 | 
List
 | 
Click
 | 
 | 
 | 
Là danh sách số điện thoại lưu trên danh bạ thiết bị.

Thông tin hiển thị gồm:

• 
icon avatar

• 
Tên tương ứng tên lưu số điện thoại trong danh bạ (Danh bạ không có tên không hiển thị)

• 
Số điện thoại

Nhấn chọn 1 số tài khoản/số thẻ → Tham khảo logic xử lý

c) Màn hình xác nhận giao dịch
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 
3
 | 
Ghi chú
 | 
Label
 | 
Read Only
 | 
 | 
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo:

 | 
5
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản nguồn

 | 
6
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản thụ hưởng (bôi đỏ tài khoản)

 | 
7
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên người thụ hưởng

 | 
9
 | 
Số thẻ/số điện thoại
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số thẻ/số điện thoại người thụ hưởng (bôi đỏ) nếu người chuyển nhập số thẻ/số điện thoại vào ô Tài khoản thụ hưởng  trong màn hình khởi tạo

 | 
10
 | 
Số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ; Số tiền viết bằng chữ tương ứng(bôi đỏ)

 | 
11
 | 
Phí giao dịch và thuế
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền, dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)

Hiển thị thông tin đối tượng chịu phí

 | 
12
 | 
Nội dung giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị nội dung chuyển tiền

 | 
13
 | 
Chọn phương thức xác thực
 | 
Label
 | 
Read

Only
 | 

 | 

 | 

 | 
14
 | 
Phương thức xác thực
 | 
Listbox
 | 
Select
 | 
Yes
 | 

 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 
15
 | 
Xác nhận
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mặc định Enable

d) Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT 

e) Màn hình kết quả
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
2
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Nếu nhập/chọn số tài khoản thụ hưởng, hiển thị thông tin giao dịch thành công bao gồm các thông tin:

• 
Logo Co-opbank

• 
 Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)

• 
Chuyển tiền thành công

• 
 Số tiền bằng số + đơn vị tiền tệ

• 
Thời gian giao dịch

• 
Tên người thụ hưởng

• 
Tài khoản thụ hưởng

• 
 Chi nhánh/PGD thụ hưởng

• 
Nội dung

• 
Mã giao dịch

Nếu nhập/chọn số thẻ/số điện thoại thụ hưởng, hiển thị thông tin giao dịch thành công bao gồm các thông tin:

• 
Logo Co-opbank

• 
 Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)

• 
Chuyển tiền thành công

• 
 Số tiền bằng số + đơn vị tiền tệ

• 
Thời gian giao dịch

• 
Tên người thụ hưởng

• 
Tài khoản thụ hưởng

• 
Số thẻ thụ hưởng

• 
 Chi nhánh/PGD thụ hưởng

• 
Nội dung

• 
Mã giao dịch

 | 
4
 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 
5
 | 
Lưu ảnh
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý

 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

4/ Luồng xử lý

a) Màn hình khởi tạo
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
1
 | 
Bấm chọn chức năng chuyển tiền nội bộ khác chủ
 | 
Client MB
 | 
Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server

 | 
MB server
 | 
Nhận và gửi yêu cầu sang Bank server

 | 
Bank server
 | 
1/ Nhận yêu cầu và trả danh sách tài khoản thanh toán

2/ Kiểm tra và xác định rule được phép thực hiện các loại giao dịch của mỗi tài khoản đến MB server

 | 
MB server
 | 
 Nhận kết quả lấy danh sách tài khoản thanh toán và phản hồi lại Client

 | 
Client MB
 | 
1/ Nhận kết quả:

• 
Không thành công:Hiển thị thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau.",  button "Đóng".

• 
Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình chuyển tiền

• 
Thành công: Chuyển bước 2

2/  Kết quả trả về:

Nếu có tài khoản thanh toán: Hiển thị màn hình popup danh sách tài khoản nguồn, bao gồm các thông tin:

• 
Số tài khoản

• 
Số dư khả dụng + đơn vị tiền tệ

Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!". Đóng thông báo, giữ nguyên màn hình hiện tại.

 | 
2
 | 
Chọn 1 tài khoản nguồn khác
 | 
Client MB
 | Hiển thị danh sách tài khoản nguồn
Hiển thị dấu tích và sẽ hiển thị lên đầu danh sách bản ghi đang được chọn hiện tại.

Fill thông tin vào ô tài khoản nguồn bao gồm:

• 
 Số tài khoản

• 
 Số dư khả dụng + đơn vị tiền tệ VND

 | 
3
 | 
Nhập số tài khoản/số thẻ/số điện thoại thụ hưởng
 | 
Client MB

 | 
Focus ô Số tài khoản/số thẻ/số điện thoại → Gợi ý số điện thoại lưu trong danh bạ thiết bị có chứa chuỗi ký tự số nhập vào

Thoát focus → Validate

• Không hợp lệ | STT | Trường hợp | Mô tả | Xử lý
 | 1 | 
Chuỗi ký tự nhập vào là số khác các trường hợp sau:

• Có độ dài =16 ký tự và 6 số đầu khác 970446
• Có độ dài nằm trong đoạn: [16,21] và 6 số đầu = 970446
• Bắt đầu bằng số 0 và có độ dài 10 ký tự
• Có độ dài trong đoạn [2,17], số bắt đầu khác 0, khác 970446 | Thông báo "Số tài khoản/Số thẻ/Số điện thoại không đúng định dạng. Quý khách vui lòng kiểm tra lại!" | 

 | 2 | 
Chuỗi ký tự nhập vào gồm cả chữ và số khác các trường hợp sau:

• Có độ dài trong đoạn [2,15], các ký tự đầu khác  970446, 0, và 90 | 

 | 3 | 
Chuỗi ký tự nhập vào chỉ bao gồm chữ, có độ dài <2 và > 15 ký tự
 | 

 | 4 | 
Chuỗi ký tự số nhập vào có độ dài 16 ký tự số và bắt đầu khác chuỗi số 970446 nhưng trùng với STK trong danh sách Tài khoản nguồn do MB server đã trả ở bước trước
 | Thông báo Quý khách vui lòng chọn loại "Chuyển tiền nội bộ cùng chủ" | 

 | 5 | 
Chuỗi ký tự bắt đầu bằng số 0 và có độ dài 10 ký tự nhưng trùng với số điện thoại Login
 | Thông báo Quý khách vui lòng chọn loại "Chuyển tiền nội bộ cùng chủ" | 

• Hợp lệ
- Chuỗi ký tự là số có độ dài =16 ký tự và 6 số đầu khác 970446, không trùng với DS tài khoản nguồn → Gửi yêu cầu truy vấn thông tin thụ hưởng nội bộ tới MB server ( Truyền accountNo)

- Chuỗi ký tự là số có độ dài trong đoạn [2,17] và 6 số đầu khác 0, khác 970446 → Gửi yêu cầu truy vấn thông tin tài khoản nội bộ tới MB server ( Truyền accountNo)

- Chuỗi ký tự là số có độ dài nằm trong đoạn: [16,21] và 6 ký tự đầu = 970446 → Gửi yêu cầu truy vấn thông tin tài khoản nội bộ tới MB server ( Truyền cardNo)

- Chuỗi ký tự là chữ có độ dài [2,15] ký tự → Gửi yêu cầu truy vấn thông tin thụ hưởng nội bộ tới MB server ( Truyền accountNo)

- Chuỗi ký tự bao gồm cả chữ và số có độ dài trong đoạn [2,15], các ký tự đầu khác  970446, 0, và 90 → Gửi yêu cầu truy vấn thông tin thụ hưởng nội bộ tới MB server ( Truyền accountNo)

- Chuỗi ký tự bắt đầu bằng số 0 và có độ dài 10 ký tự không trùng với số điện thoại Login → Gửi yêu cầu truy vấn thông tin thụ hưởng nội bộ tới MB server ( Truyền mobileNo)

 | 
MB server
 | 
Gửi yêu cầu truy vấn thông tin tài khoản tới Bank

• 
Chuyển khoản đến số điện thoại + Chuyển khoản đến số tài khoản → Gọi API queryCustomerByAcc  (Truy vấn thông tin tài khoản thụ hưởng nội bộ theo số tài khoản)

• 
Chuyển khoản đến số thẻ → Gọi API 

> ⚠️ *Nội dung đã cắt ngắn (26222 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 16.5. Chuyển tiền nội bộ cùng chủ

> **Page ID:** `29895954` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29895954

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia:  KH, Client MB, MB Server, Bank Server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• KH có gói dịch vụ được phép sử dụng chức năng này
• KH có tài khoản hợp lệ để thực hiện chức năng này
• Kết quả mong muốn:
• KH thực hiện giao dịch thành công
• Tài khoản nguồn được ghi nợ đúng bằng số tiền giao dịch
• Tài khoản đích được ghi có đúng bằng số tiền giao dịch
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### a) Màn hình khởi tạo

##### b) Màn hình xác nhận

##### 

##### c) Màn hình kết quả

##### d) Màn hình nhập số tiền

##### 

#### Mô tả:

##### a) Màn hình khởi tạo
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nội bộ cùng chủ

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 5 | Hạn mức (Đã chốt để phase sau) | Textlink | Click | X | -- | Nhấn textlink → Điều hướng sang màn hình Thông tin hạn mức, do ngân hàng cũng cấp link và được tích hợp trên app (Để phase sau)
 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
X
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả về
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ. 
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
8
 | 
Tài khoản thụ hưởng
 | 
Combobox
 | 
List
 | 
X
 | 
--
 | 
Danh sách tài khoản thụ hưởng: Là tài khoản nguồn nhưng không bao gồm tài khoản nguồn đã chọn.

• Số tài khoản
Không có tài khoản: Hiển thị thông báo: Không có tài khoản hợp lệ để thực hiện giao dịch.

 | 
9
 | 
Thông tin chuyển tiền
 | 
label
 | 
Read only
 | 

 | 

 | 

 | 
10
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
X
 | 
13
 | 
Hiển thị ngăn cách hàng nghìn bằng dấu “,”

Độ dài 13 ký tự bao gồm cả dấu “,  “

Hiển thị đơn vị tiền tệ mặc định “VND”

Không nhập số bắt đầu bằng số 0

Focus ô Số tiền → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 11 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
X
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
12
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
X
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Focus ô Nội dung giao dịch → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
13
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable

##### b) Màn hình xác nhận
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
 Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read only | 
 | 
 | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo:
 | 
5
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản nguồn

 | 
6
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản thụ hưởng (bôi đỏ tài khoản)

 | 
7
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên người thụ hưởng

 | 
8
 | 
Số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ; Số tiền viết bằng chữ tương ứng(bôi đỏ)

 | 
10
 | 
Nội dung giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị nội dung chuyển tiền

 | 11 | Phí giao dịch và thuế | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ

Dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)

Người chịu phí

 | 
12
 | 
Xác nhận
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mặc định Enable

##### c) Màn hình kết quả
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
2
 | 
icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin giao dịch thành công bao gồm các thông tin:

• Logo Co-opbank
• Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Chuyển tiền thành công
• Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản thụ hưởng
• Chi nhánh/PGD
• Mã giao dịch
• Nội dung
 | 4 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon chia sẻ → Tham khảo logic xử lý

 | 5 | 
Lưu ảnh
 | 
Icon
 | 
Click
 | 

 | 

 | 
Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý

 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 4/ Luồng xử lý

##### a) Màn hình khởi tạo
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Bấm chọn chức năng chuyển tiền nội bộ cùng chủ
 | 
Client MB
 | 
Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server

 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | 
1/ Nhân yêu cầu và lấy danh sách tài khoản thanh toán

2/ Kiểm tra và xác định rule được phép thực hiện các loại giao dịch của mỗi tài khoản đến MB server

 | MB server | 
 Nhận kết quả lấy danh sách tài khoản thanh toán từ Bank server và phản hồi lại Client

 | 
Client MB
 | 
1/ Nhận kết quả:

• Không thành công:Hiển thị thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau.",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình chuyển tiền
• Thành công: Chuyển bước 2
 2/  Kết quả trả về:

• Nếu có tài khoản thanh toán: Hiển thị danh sách tài khoản nguồn, bao gồm các thông tin:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ
• Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" Đóng câu thông báo quay lại màn hình home.
 | 2

 | 
Chọn lại  tài khoản nguồn
 | 
Client MB
 | 
Hiển thị danh sách tài khoản nguồn

Hiển thị dấu tích và sẽ hiển thị lên đầu danh sách bản ghi đang được chọn hiện tại.

Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 3 | 
Chọn "Tài khoản thụ hưởng”  
 | 
Client MB

 | 
Hiển thị màn hình popup danh sách tài khoản thụ hưởng: Là danh sách tài khoản nguồn nhưng không bao gồm tài khoản nguồn đã chọn.

• Số tài khoản
Hiển thị dấu tích và sẽ hiển thị lên đầu danh sách bản ghi đang được chọn hiện tại.

Nếu không có tài khoản thụ hưởng, hiển thị thông báo "Quý khách không có tài khoản thụ hưởng cùng chủ để thực hiện giao dịch. Vui lòng kiểm tra lại.". Đóng thông báo, giữ nguyên màn hình hiện tại

 | Chọn 1 tài khoản trong danh bạ thụ hưởng | 
Client MB
 | 
Hiển thị màn hình khởi tạo giao dịch với thông tin tài khoản thụ hưởng được fill vào ô “Tài khoản thụ hưởng".

 | 
4
 | 
Nhập số tiền
 | 
Client MB
 | 
Hiển thị dấu "x" cho phép bỏ tất cả các ký tự đã nhập

Gợi ý số tiền chuyển theo quy tắc: <Tham khảo quy tắc gợi ý chung trong >

 | 5

 | 
Nhấn "Tiếp tục"

 | 
Client MB
 | 
Kiểm tra thông tin validate tại màn hình khởi tạo:

1/ Nếu không hợp lệ, hiển thị thông báo lỗi tương ứng:
 | Case | Tác nhân | Nội dung thông báo | Ghi chú
 | Tài khoản thụ hưởng trống | Client | Tài khoản thụ hưởng không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Bỏ trống số tiền | Client | Số tiền không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Bỏ trống nội dung giao dịch | Client | Nội dung giao dịch không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

2/  Nếu hợp lệ: Gửi yêu cầu khời tạo giao dịch sang MB server

 | 
Server MB
 | 
Nhận yêu cầu và kiểm tra: 

1/ Kiểm tra Nội dung giao dịch với giá trị tham số TEXT_BLACKLIST:

• Nếu nội dung giao dịch có chưa các chuỗi text được cấu hình tại tham số TEXT_BLACKLIST ->  Trả mã lỗi cho ứng dụng theo thông báo cấu hình là "Giao dịch không thành công do nội dung giao dịch có chứa các đoạn mã không phù hợp. Quý khách vui lòng kiểm tra lại."
• Nếu nội dung GD không bao gồm các chuỗi text trong TEXT_BLACKLIST -> Chuyển bước 2
2/ Nếu mã dịch vụ (serviceCode) là  chuyển tiền nội bộ cùng chủ, thực hiện kiểm tra hạn mức gói dịch vụ của khách hàng và tính phí giao dịch. → Tham khảo logic xử lý tại Logic kiểm tra PTXT 

Lưu ý: Đối quy tắc kiểm tra hạn mức với dịch vụ Chuyển tiền nội bộ cùng chủ, 

- Có check Hạn mức gói dịch vụ
- Có check Hạn mức chuyển tiền ( cài đặt trên app)
- Có check Hạn mức/ GD
- Có check Phí

- Không check hạn mức của nhóm dịch vụ 630/ ngày

Gửi kết quả lại cho client bao gồm cả serviceCode

 | Client MB | 
Nhân kết quả phản hồi từ server:

Hợp lệ: Chuyển sang màn hình Xác nhận giao dịch

Không hợp lệ: Hiển thị thông báo lỗi tương ứng. Đóng câu thông báo, giữ nguyên màn hình hiện tại. <Tham khảo >

##### b) Màn hình xác nhận giao dịch và xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Nhấn "Xác nhận"

 | Client MB | 
Gửi yêu cầu hạch toán sang server

 | MB server | 
Nhận và gọi bank server hạch toán

 | Bank server | Thực hiện hạch toán và trả kết quả về cho MB server
 | MB server | 
Nhận, kiểm tra kết quả:

Thành công: Cập nhật trạng thái giao dịch thành công

Không thành công: Cập nhật trạng thái giao dịch thất bại và phản hồi mã lỗi về cho client

 | Client MB | 
Nhận kết quả:

Thành công: Chuyển sang màn hình kết quả giao dịch

Không thành công: Hiển thị thông báo lỗi (mã lỗi do bank trả về, hiển thị theo thông báo lỗi của bank)
 | STT | Case | Tác nhân | Thông báo | Ghi chú
 | 1 | Bank server hạch toán Time out | Server | Xem tại  | Đóng câu thông báo và xử lý quay lại màn hình home
 | 2 | Chuyển tiền thất bại (bank server hạch toán thất bại) | Server | Hiển thị theo thông báo bank trare về (có thể cấu hình lại tại QUản lý mã lỗi trên BE) | Đóng câu thông báo: Quay lại màn hình khởi tạo, xử lý reset các giá trị khởi tạo trước đó.
 | 3 | Time out tại đầu MB server | Server | Xem tại  | Đóng câu thông báo: Quay lại màn hình thao tác trước đó, giữ nguyên giá trị khởi tạo trước đó

##### c) Màn hình kết quả
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình home

 | 2

 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại 

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại 

 | 4 | 
Nhấn nút Tạo giao dịch mới
 | 
Client MB
 | 
Gọi danh sách tài khoản vừa thực hiện giao dịch để cập nhật lại danh sách giao dịch chuyển tiền

Trở lại màn hình khởi tạo giao dịch chuyển tiền nội bộ cùng chủ

---

### 16.6. Chuyển tiền qua GTTT - Gói 4

> **Page ID:** `37682335` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37682335

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia:  KH, Client MB, MB Server, Bank Server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• KH có gói dịch vụ được phép sử dụng chức năng này
• KH có tài khoản hợp lệ để thực hiện chức năng này
• Kết quả mong muốn:
• Tài khoản nguồn được ghi nợ đúng bằng số tiền giao dịch
• Bank Server ghi nhận lệnh chuyển tiền qua GTTT cho KH thành công
• KH có thể sử dụng GTTT ra quầy giao dịch của ngân hàng để nhận tiền mặt trong vòng [n] ngày kể từ ngày thực hiện giao dịch thành công (giá trị n tùy nghiệp vụ của bank).
#### 2/ Luồng màn hình

#### MB:

##### MH1: Màn hình khởi tạo - khi truy cập chức năng

##### MH2: Màn hình khởi tạo - chọn Loại GTTT là CCCD

##### MH3: Màn hình khởi tạo - Lưu danh bạ thụ hưởng

##### MH4: Màn hình khởi tạo - Nhập số tiền giao dịch

##### MH5: Màn hình xác nhận giao dịch

##### M7: Màn hình kết quả giao dịch

##### M8: Màn hình danh bạ thụ hưởng

#### Mô tả màn hình:

##### MH1/2/3/4: Màn hình khởi tạo
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Back | 
Icon
 | 
Click
 | 

 | -- | Nhấn Back, quay về màn hình thao tác trước đó
 | 2 | Tiêu đề | 
Label
 | 
Read Only
 | 

 | 
--
 | Hiển thị title "Chuyển tiền qua GTTT"
 | Thông tin giao dịch
 | 1 | Thông tin người chuyển | 
Label
 | 
Read Only
 | 

 | -- | 

 | 2 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
X
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách bank server trả về
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 3 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
 | 
 | 

 | 4 | 
Tên người thụ hưởng
 | 
Textbox
 | 
Text
 | 
X
 | 
70
 | 
Placeholder: Tên người thụ hưởng

Mặc định trống

Chỉ cho nhập ký tự chữ không dấu và số. Không cho nhập ký tự đặc biệt

Khi nhập, hiển thị dấu x cho phép xóa bỏ toàn bộ kỹ tự đã nhập

 | 5 | 
Loại GTTT
 | 
Combobox
 | 
Select
 | 
X
 | 
--
 | 
Placeholder: Loại GTTT

Mặc định trống

Giá trị hiển thị cho chọn, fix tại client gồm:

• Chứng minh nhân dân
• Hộ chiếu
• CMT quân đội
• Thẻ căn cước công dân
Chỉ cho chọn 1 giá trị

 | 6 | 
Số GTTT
 | 
Textbox
 | 
Text
 | 
X
 | 
20
 | 
Placeholder: Số GTTT

Mặc định trống

Chỉ cho phép nhập ký tự số và chữ không dấu

Khi nhập, hiển thị dấu x cho phép xóa bỏ toàn bộ kỹ tự đã nhập

Trường hợp nhập số  CMND (Giấy tờ tùy thân chọn CMND), kiểm tra nếu khác 9 hoặc 12 ký tự -> thông báo "Số CMND không hợp lệ. Quý khách vui lòng kiểm tra lại."

 | 7 | 
Ngày cấp
 | 
Calendar
 | 
Select
 | 
x
 | 

 | 
Chỉ hiển thị khi chọn Loại giấy tờ

Placeholder: Ngày cấp

Mặc định trống

Định dạng: dd/mm/yyyy

Không cho chọn những ngày tương lai

 | 8 | 
Nơi cấp
 | Textbox/Combobx | Input/Select | X | 50 | 
Chỉ hiển thị khi chọn Loại giấy tờ

Chỉ cho phép KH nhập ký tự chữ tiếng Việt có dấu, có khoảng trắng và số. Hệ thống tự động bỏ dấu khi truyền sang server.

Hiển thị theo Loại GTTT:

• Nếu KH chon CMT quân đội, hiển thị dạng textbox cho KH tự nhập
• Nếu KH chọn Hộ chiếu, hiển thị giá trị "Cục Quản lý Xuất nhập cảnh" và có dấu "x" cho phép xóa toàn bộ ký tự để nhập lại.
• Nếu chọn CMND thị mặc định: "Cục CSĐKQL cư trú và DLQG về dân cư". KH có thể xóa đi nhâp lại nếu muốn nhập công an tỉnh/thành phố khác.
• Nếu chọn CCCD thi ra 2 lựa chọn: "Cục CSQLHC về TTXH" và "Cục CSĐKQL cư trú và DLQG về dân cư". Chỉ được chọn 1 trong 2 giá trị và không cho nhập sửa lại giá trị.
Lưu ý: Tại trường này sẽ có dấu "x" cho phép xóa toàn bộ ký tự hiện có nhé
 | 9 | 
Số điện thoại
 | 
Textbox
 | 
Number
 | 

 | 
10
 | 
Chỉ cho phép nhập số

Bắt đầu bằng số 0

Nếu chuỗi số nhập vào có độ dài khác 10 và không bắt đầu bằng số 0, hiển thị thông báo "Số điện thoại không đúng định dạng. Quý khách vui lòng kiểm tra lại."

 | 10 | 
Icon danh bạ thụ hưởng
 | 
Icon
 | 
Click
 | 

 | 

 | 
Nhấn icon danh bạ thụ hưởng → focus màn hình danh bạ thụ hưởng theo loại chuyển tiền qua GTTT

 | 11 | 

Lưu danh bạ thụ hưởng

 | 
Switch button
 | 
Click
 | 

 | 

 | 
Chỉ hiển thị khi nhập đủ thông tin thụ hưởng: Tên người thụ hưởng, Loại GTTT, Số GTTT, Ngày cấp, Nơi cấp.

Mặc định: OFF

Cho phép thực hiện switch ON/OFF

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

 | 12 | Tên gợi nhớ | Textbox | Input | 
 | 20 | 
Chỉ hiển thị khi Lưu danh bạ thụ hưởng ở trạng thái ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu
 | 13 | Thông tin chuyển tiền | Label | Read Only | 
 | 
 | 

 | 14 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
X
 | 
13
 | 
Ngăn cách đơn vị hàng nghìn bằng dấu ","
Độ dài 13 ký tự bao gồm cả dấu “,”. Không cho nhập sô 0 đầu tiên.

Có gợi ý số tiền chuyển, quy tắc gợi ý số tiền xem tại quy tắc xử lý chung.

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 15 | 
Đối tượng chịu phí
 | 
Listbox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

• Nếu là "Người chuyển trả" -> Trừ trực tiếp tại tài khoản nguồn
• Nếu là "Người nhận trả" -> Trừ phí vào số tiền chuyển của KH nhận tại quầy GD
Mặc định hiển thị “Người chuyển trả”

 | 16 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”.

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

Hiển thị số kí tự đã nhập/số kí tự tối đa

 | Nút thao tác
 | 1 | Tiếp tục | 
Button
 | 
Click
 | 

 | -- | Nhấn nút, tham khảo logic xử lý

##### MH5: Màn hình xác nhận giao dịch
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Nhấn nút, xử lý quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tiêu đề: Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read Only | 
 | 
 | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 
4
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin tài khoản nguồn đã chọn tại màn hình trước

 | 
5
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên người thụ hưởng đã nhập tại màn hình trước

 | 
6
 | 
Số CCCD/CMND/ CMT quân đội/hộ chiếu
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị giá trị theo giá trị đã nhập ở màn hình trước (bôi đỏ)

Label hiển thị động theo loại giấy tờ đã chọn:

• Nếu loại giấy tờ là "Thẻ căn cước công dân" -> Hiển thị label: Số CCCD
• Nếu loại giấy tờ là "Chứng minh nhân dân" -> Hiển thị label: Số CMND
• Nếu loại giấy tờ là "CMT quân đội" -> Hiển thị label: Số CMT quân đội
• Nếu loại giấy tờ là "Hộ chiếu" -> Hiển thị label: Số hộ chiếu
 | 7 | Ngày cấp | 
Label
 | 
Read Only
 | 
 | 
 | Hiển thị theo giá trị đã chọn tại màn hình trước
 | 8 | Nơi cấp | 
Label
 | 
Read Only
 | 
 | 50 | Hiển thị theo giá trị đã chọn tại màn hình trước
 | 9 | Số điện thoại | 
Label
 | 
Read Only
 | 
 | 
 | 
Hiển thị theo giá trị đã chọn tại màn hình trước

Chỉ hiển thị khi có nhập số điện thoại tại màn hình trước

 | 
10
 | 
Số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ;

Số tiền viết bằng chữ tương ứng(bôi đỏ)

 | 
11
 | 
Phí giao dịch và thuế
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ

Người chịu phí

Dữ liệu do Server trả về (chỉ hiển thị nếu khác 0 và rỗng)

 | 
12
 | 
Nội dung giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị nội dung chuyển tiền

 | 
13
 | 
Chọn phương thức xác thực
 | 
Label
 | 
Read

Only
 | 

 | 

 | 

 | 
14
 | 
Phương thức xác thực
 | 
Combobox
 | 
Select
 | 

 | 

 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 
15
 | 
Xác nhận
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mặc định Enable

##### MH6: Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH7: Màn hình kết quả giao dịch
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
2
 | 
icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút, hiển thị màn hình home

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin giao dịch thành công bao gồm các thông tin

• Tên ứng dụng ngân hàng điện tử (logo+ co-opbank)
• Icon thành công (nút tích trog nền tròn xanh)
• Chuyển tiền thành công
• Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch (định dạng dd/mm/yyyy hh:mm)
• Tên người thụ hưởng
• Số CCCD/CMND/ CMT quân đội/hộ chiếu (Hiển thị label động theo màn hình xác nhận)
• Ngày cấp
• Nơi cấp
• Mã giao dịch
• Nội dung
• Lưu ý: Người thụ hưởng vui lòng mang GTTT ra quầy giao dịch của Ngân hàng Hợp tác để nhận tiền mặt trong vòng [n] ngày kể từ ngày thực hiện giao dịch thành công. (text lưu ý cấu hình dưới back-end, do server trả về)
 | 4 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

 | 5 | Lưu ảnh | icon | click | 
 | 
 | Nhấn icon → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

##### MH7: Màn hình danh bạ thụ hưởng

 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Title | Label | Read only | 
 | 
 | Danh bạ thụ hưởng
 | 2 | Nút đóng | Icon | Click | 
 | 
 | Nhấn dấu "X" → Đóng màn hình popup danh bạ
 | 3 | Tìm kiếm | Textbox | Text | 
 | 
 | 
Cho phép tìm kiếm tương đối theo tên thụ hưởng/số cmnd/ số cccd/số cmt quân đội/hộ chiếu/loại giấy tờ lưu trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại )

 | 4 | Danh sách tài khoản thụ hưởng  | List | Click | 
 | 
 | 
Là danh sách thụ hưởng bằng GTTT lưu tại mục Chuyển tiền qua GTTT tại Danh bạ thụ hưởng.

Thông tin hiển thị gồm:

• Logo = in hoa ký tự đầu tiên của từ đầu tiên và từ cuối cùng trong tên hiển thị. Nếu tên chỉ có 1 từ sẽ in hoa 2 ký tự đầu tiên trong tên hiển thị
• Tên người thụ hưởng/tên gợi nhớ đã lưu
• Số CMND/Số CCCD/Số CMT quân đội/Hộ chiếu
• Loại giấy tờ
Nhấn chọn 1 bản ghi → Fill các giá trị tương ứng vào màn hình khởi tạo giao dịch:

• Tên người thụ hưởng
• Loại giấy tờ
• Số GTTT
• Ngày cấp
• Nơi cấp

#### 4/ Luồng xử lý

##### Truy cập chức năng:
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
1
 | 
Tại màn hình home, chọn chức năng "Chuyển tiền", sau đó chọn loại chuyển tiền "Chuyển tiền qua GTTT"
 | 
Client MB
 | 
Kiểm tra thông tin: 

• Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Gửi yêu cầu lấy danh sách tài khoản thanh toán theo số CIF cho server
• Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng, thông báo: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ." Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại."
• Có tài khoản thanh toán → Chuyển màn hình khởi tạo giao dịch chuyển tiền qua GTTT

##### MH1/2/3/4: Màn hình khởi tạo
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn tài khoản nguồn | 
Client MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 
2
  | 
Nhấn icon danh bạ

 | 
Client MB
 | 
 Kiểm tra danh bạ thụ hưởng của chuyển tiền qua GTTT đã lấy được trước đó chưa (gọi truy vấn tại màn hình chuyển tiền khi nhấn icon danh bạ)? Nếu chưa lấy được → Gửi lại yêu cầu lấy danh bạ thụ hưởng của chuyển tiền qua GTTT theo user sang server. Nếu có rồi: Hiển thị màn hình popup danh bạ thụ hưởng

 | MB server | 
1/ Xử lý yêu cầu:

• Truy vấn danh sách danh bạ thụ hưởng của chuyển tiền qua GTTT đã lưu theo user.
• Thông tin trả về bao gồm: Tên người hưởng, Loại giấy tờ, Số GTTT, Ngày cấp, Nơi cấp, Tên gợi nhớ (nếu có)
• Sắp xếp danh sách truy vấn được theo bản ghi sử dụng chuyển tiền gần nhất
2/ Trả kết quả về cho Client

 | Client MB | 
Nhận kết quả

• Không thành công, hiển thị danh sách trống và thông báo lỗi: "Không lấy được danh sách danh bạ. Quý khách vui lòng thử lại sau."
• Thành công:Hiển thị màn hình danh bạ thụ hưởng, không có dữ liệu hiển thị thông báo "Quý khách chưa có danh bạ thụ hưởng."
 | 2 | Nhấn chọn 1 bản ghi từ danh bạ | Client MB | 
Fill các giá trị vào ô tương ứng:

• Tên người thụ hưởng
• Loại GTTT
• Số GTTT
• Ngày cấp
• Nơi cấp
 | 3

 | Nhấn "Tiếp tục"

 | 
Client MB
 | 
Kiểm tra thông tin validate tại màn hình khởi tạo:

1/ Nếu không hợp lệ, hiển thị thông báo lỗi tương ứng. Đóng thông báo, giữ nguyên màn hình hiện tại:
 | | 
Case
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Ghi chú

 | Tên người thụ hưởng trống | Client | Tên người thụ hưởng không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Loại GTTT trống | Client | Loại GTTT không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Số GTTT trống | Client | Số GTTT không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Ngày cấp trống | Client | Ngày cấp không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Nơi cấp trống | Client | Nơi cấp không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | Số tiền trống | Client | Số tiền không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

 | Nội dung giao dịch trống | Client | Nội dung giao dịch không được bỏ trống. Quý khách vui lòng kiểm tra lại! | 

2/  Nếu hợp lệ: Gửi yêu cầu khời tạo giao dịch sang MB server

 | 
Server MB
 | 
1/ Kiểm tra Nội dung giao dịch với giá trị tham số TEXT_BLACKLIST:

• Nếu nội dung giao dịch có chưa các chuỗi text được cấu hình tại tham số TEXT_BLACKLIST ->  Trả mã lỗi cho ứng dụng theo thông báo cấu hình là "Giao dịch không thành công do nội dung giao dịch có chứa các đoạn mã không phù hợp. Quý khách vui lòng kiểm tra lại."
• Nếu nội dung GD không bao gồm các chuỗi text trong TEXT_BLACKLIST -> Chuyển bước 2
2/ Validate thông tin: Trường hợp chọn Giấy tờ tùy thân là CMND hoặc Hộ chiếu, kiểm tra lại thời hạn của các loại giấy tờ này:

• Đối với loại giấy tờ là CMND: ngày hiển tại – ngày cấp>15 năm => Giấy tờ hết hạn, trả về thông báo cho client "Giấy tờ tùy thân của người thụ hưởng quá hạn sử dụng. Quý khách vui lòng kiểm tra lại."
• Đối với loại giấy tờ là Hộ chiếu: ngày hiện tại – ngày cấp > 10 năm =>Giấy tờ hết hạn, trả

> ⚠️ *Nội dung đã cắt ngắn (18484 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 16.7. Chuyển tiền theo lô

> **Page ID:** `110855072` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/110855072

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

#### 16.7.1. SOW chức năng chuyển tiền theo lô

> **Page ID:** `108003497` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/108003497

### 1/ Nguyên tắc
falseGhi rõ các nguyên tắc về CHÍNH SÁCH mà Bank/Đối tác áp dụng cho chức năng thuộc phạm vi phân tích

### 2/ Phạm vi

#### 2.1/ Phạm vi FrontEnd
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | API Bank cấp
 | Chuyển tiền | 
• Chuyển tiền nhanh 247 theo lô qua tài khoản
• Chuyển tiền nhanh 247 theo lô qua thẻ
• Chuyển tiền nội bộ | 

RedThêm mới
 | MB | 
Cho phép người dùng CK tới nhiều người nhận cùng 1 lúc trên ứng dụng MB

Các bước thực hiện:

Bước 1: Chọn chức năng:

• CK nội bộ 
• Hoặc CK nhanh 247 qua tài khoản
• Hoặc CK nhanh 247 qua thẻ
Bước 2: Khởi tạo → chọn người nhận và các thông tin giao dịch

• Nếu Số lượng người nhận = 1 → Giữ nguyên luồng hiện tại của các loại chuyển tiền tương ứng
• Nếu Số lượng người nhận > 1 → Theo luồng chuyển tiền theo lô của các loại chuyển tiền tương ứng
( Số lượng người nhận tối đa:

- CK Nội bộ: 10 người

- CK nhanh 247: 03 người)

Bước 3: Xác nhận

• Nếu Số lượng người nhận = 1 → Giữ nguyên luồng hiện tại của các loại chuyển tiền tương ứng
• Nếu Số lượng người nhận > 1 →  Quy tắc hạn mức/ phí giao dịch/ PTXT như sau | STT | Loại hạn mức/ phí giao dịch | Yêu cầu
 | 1 | Hạn mức tối thiểu/ Giao dịch | Tính theo giao dịch đơn lẻ
 | 2 | Hạn mức tối đa/Giao dịch | Tính theo giao dịch đơn lẻ
 | 3 | Hạn mức theo nhóm chuyển tiền/ ngày (Cài đặt trên App) | Tính theo tổng giao dịch lô
 | 3 | Phương thức xác thực | Tính theo tổng giao dịch lô
 | 4 | Hạn mức theo nhóm dịch vụ 630/ngày/ PTXT | Tính theo tổng giao dịch lô
 | 5 | Hạn mức về số lần giao dịch/ ngày | Đếm số lần theo giao dịch đơn lẻ
 | 6 | 
Phí giao dịch tương ứng với Người chuyển trả và người nhận trả
 | Tính theo từng giao dịch đơn lẻ

Bước 4: Xác thực

Theo luồng xác thực chung

Bước 4: Kết quả giao dịch

• Nếu Số lượng người nhận = 1 → Giữ nguyên luồng hiện tại của các loại chuyển tiền tương ứng
• Nếu Số lượng người nhận > 1 →  Hạch toán giao dịch sang bank theo tuần tự từng giao dịch đơn lẻ. Mỗi giao dịch lô sẽ có 2 loại mã: Mã lô  và mã giao dịch đơn lẻ | 
RedKhó
 | Client, Server, Bank | 

 | Danh bạ | 
• Chọn danh bạ chuyển tiền nội bộ
• Chọn danh bạ chuyển tiền 247 qua tài khoản
• Chọn danh bạ chuyển tiền 247 qua thẻ | 
GreenCập nhật
 | MB | 
• Bổ sung label tại MH Chọn danh bạ "Quý khách có thể chọn tối đa {n} người thụ hưởng cho 1 lần giao dịch (n được cấu hình cho từng loại chuyển tiền)"
• Cho phép chọn nhiều người thụ hưởng từ danh bạ đã lưu. Số lượng người thụ hưởng cho phép cấu hình theo từng loại giao dịch chuyển tiền | 
BlueTRUNG BÌNH
 | Client, Server | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 

#### 2.2/ Phạm vi Backend
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | API Bank cấp
 | Báo cáo BE | Báo cáo chi tiết giao dịch chuyển tiền | 
GreenCập nhật
 | MB | 
• Bổ sung cột Chuyển tiền lô (Hiển thị mã giao dịch lô hoặc thứ tự của các gd chuyểnn tiền trong lô) | 
BlueTRUNG BÌNH
 | BE

#### 2.3/ Phạm vi Server

Xác định hạn mức/ phí/ ptxt của GD chuyển tiền theo lô như đã mô tả

#### 2.4/ Đánh giá ảnh hưởng

Cần test lại các chức năng:

App: Các chức năng chuyển tiền tới 1 người thụ hưởng

• CK nội bộ khác chủ
• CK nhanh 247 qua thẻ
• CK nhanh 247 qua tài khoản
• Danh bạ
• Báo cáo giao dịch
Backend

• Báo cáo tổng hợp giao dịch
• Báo cáo chi tiết giao dịch
• Báo cáo chi tiết giao dịch chuyển tiền
#### 2.4/ Phạm vi API kênh cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Kênh sử dụng | Input | Output | Ghi chú
 | 1 | Khởi tạo giao dịch theo lô | 
 | MB | 
Client truyền vào các loại chuyển tiền:

• CK Nội bộ khác chủ
• CK nhanh 247 qua thẻ
• CK nhanh 247 qua tài khoản | 
• Mã giao dịch lô
• Mã giao dịch đơn lẻ | Server cấp API mới cho App
 | 
 | 
 | 
 | 
 | 

 | 
 | 

### 3/ Q&A

#### 3.1/ Phạm vi Frontend
 | Nhóm chức năng | Chức năng | Màn hình | TT | Câu hỏi | Trả lời | Cần xử lý tiếp
 | Chuyển tiền | CK theo lô | Kết quả giao dịch | 1 | 
Giả sử trong 1 lô có 3 người nhận.

• Khi hạch toán, server sẽ đưa các giao dịch đơn lẻ trong lô vào queue và gọi hạch toán sang bank lần lượt từng giao dịch hay đẩy hết cả lô sang bank và bank hạch toán lần lượt từng giao dịch một và trả kết quả cho server?
• Nếu kết quả hạch toán cho người nhận 1 bị lỗi thì có gọi hạch toán tiếp người 2 và người 3 không hay dừng luôn và thông báo kết quả giao dịch không thành công? | 

 | 

 | Kết quả giao dịch | 2 | 
• Trường hợp người nhận 1 và người nhận 2 thành công thì có hiển thị màn hình KQGD 2/3 thành công, và đánh dấu người thứ 3 không thành công? Hay chỉ cần 1 người nhận không thành công → Không hiển thị MH KQGD ? | 
 | 

 | Khởi tạo | 3 | 
Nếu bật chức năng Thông tin chuyển tiền giống nhau

• Thì lấy theo thông tin chuyển tiền của người thứ tự thứ mấy ?
• Giả sử lấy theo thông tin chuyển tiền của người đầu tiên, nếu người đầu tiên chưa nhập thông tin chuyển tiền thì sẽ lấy theo thông tin chuyển tiền của người nào ? | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

#### 3.2/ Phạm vi Backend

3.3/ Phạm vi API kênh cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Câu hỏi | Trả lời | Cần xử lý tiếp | Ghi chú
 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 |

---

#### 16.7.2. Chuyển tiền nội bộ khác chủ tài khoản theo lô

> **Page ID:** `108004085` · **Version:** 50
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/108004085

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Tuan VN1 | 
 | 
Tạo mới tài liệu
 | V1.0.0

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Chuyển tiền nội bộ khác chủ tài khoản theo lô
 | Use Case ID | UC-CL-01
 | Use Case Description | 
Là người dùng, tôi mong muốn chuyển tiền tới nhiều người nhận cùng 1 lúc

 | Actor | 
KH, MB Client, MB Server, Bank Server

 | Priority | High
 | Trigger | 
KH thực hiện lệnh chuyển tiền nội bộ, KH nhập nhiều người nhận tiền (tối đa 10 người)

 | 
Pre-Condition
 | 
1. KH đăng nhập thành công ứng dụng; 
2. KH có tài khoản nguồn hợp lệ để thực hiện giao dịch; 
3. Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch
4. Người hưởng đúng Số tài khoản/Số thẻ/Số điện thoại

 | Post-Condition | 
1. KH thực hiện lệnh chuyển tiền nội bộ thành công cho nhiều người thụ hưởng 
2. Tài khoản nguồn của KH bị trừ tổng số tiền GD + phí vs TH người chuyển chịu phí
3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng và trừ phí khi người nhận là người chịu phí
4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]
5. Hệ thống MB ghi nhận giao dịch chuyển tiền nội bộ vào [Transaction History]
6. MB Client hiển thị chi tiết các giao dịch thành công, thất bại (nếu có)
7. MB Client hiển thị chi tiết lỗi đối với các giao dịch thất bại (nếu có)

 | Basic Flow | 
1. KH đăng nhập ứng dụng
2. KH chọn chức năng "Chuyển tiền nội bộ khác chủ tài khoản"
3. KH nhấn thêm người hưởng để chuyển được cho nhiều người (số lượng người hưởng tối đa được cấu hình trong BE và trả về trong API mid409)
4. KH nhập Số tài khoản/Số thẻ/Số điện thoại của người hưởng
5. KH nhập số tiền, người trả phí, nội dung chuyển tiền cho từng người hưởng
6. KH thực hiện xác thực giao dịch
7. Hệ thống MB server xác thực giao dịch,
8. Hệ thống Bank server hạch toán và trả kết quả lệnh chuyển tiền thành công
9. Hệ thống MB ghi nhận log theo từng GD đơn lẻ của lô vào [Activity Log]
10. Hệ thống MB ghi nhận giao dịch chuyển tiền nội bộ  theo từng GD đơn lẻ của lô vào [Transaction History]

 | Alternative Flow | 
1. KH đăng nhập ứng dụng; 
2. KH chọn chức năng "Chuyển tiền nội bộ khác chủ tài khoản"; 
3. KH thêm người thụ hưởng
4. KH nhập Số tài khoản/Số thẻ/Số điện thoại
5. KH nhập số tiền, đối tượng chịu phí, nội dung chuyển tiền; 
Tiếp theo mục 6 của Basic Flow.

 | Exception Flow | 
1. KH thực hiện khởi tạo giao dịch không thành công 
2. KH thực hiện xác thực giao dịch không thành công
3. KH chọn hủy lệnh giao dịch

 | Bussiness Rules | 
Số lượng người hưởng tối đa 

 | Non-Funtional Requiremnt | 
NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây

NFR-2: Thời gian hiệu lực của 1 GD chuyển tiền đơn lẻ của lô là 10 giây

### 2/ Luồng sơ đồ

#### 2.1/ Sơ đồ

#### 2.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
Đăng nhập hệ thống
 | 
Lấy giá trị config cho client

mid409
 | MB Client - MB Server - Bank Server | {api_base_url}/mid409 | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"List[String] configCode": configCode cần lấy value 

 | 

Xem chi tiết
"configList": [
             {
                 "configCode": maxCus
                 "configValue": 10
             },

             {
                 "configCode": max247toAcc
                 "configValue": 3
             },

             {
                 "configCode": max247toCard
                 "configValue": 3
             }

          ]     

 | 
maxCus: số lượng người nhận tối đa chuyển tiền nội bộ khác chủ theo lô

max247toAcc: số lượng người nhận tối đa chuyển nhanh 24/7 qua TK theo lô

max247toCard: số lượng người nhận tối đa chuyển nhanh 24/7 qua thẻ theo lô

 | 
Tại MH Chuyển tiền, nhấn chọn chức năng Chuyển tiền nội bộ khác chủ
 | 
Lấy danh sách tài khoản thanh toán

queryCurrentAcc
 | MB Client - MB Server - Bank Server | {api_base_url}/queryCurrentAcc | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"accountType": Loại tài khoản

 | 

Xem chi tiết
"accountType": Loại tài khoản
"accountNo": Số tài khoản
"accountName": Tên chủ tài khoản
"availBalance": Số dư khả dụng tài khoản
"currency": Loại tiền tệ
"accountStatus": Trạng thái tài khoản
"branchCode": Mã chi nhánh mở tài khoản
"branchName": Tên chi nhánh mở tài khoản

 | 

 | 
Tại MH khởi tạo, thoát Focus
 | 
Truy vấn thông tin chủ tài khoản nội bộ theo tài khoản thanh toán.

queryCustomerByAcc
 | 

 | {api_base_url}/queryCustomerByAcc | 

Xem chi tiết
"accountNo": Số tài khoản

 | 

Xem chi tiết
"accountNo": Số tài khoản
"accountName": Tên chủ tài khoản

 | 

 | 
Tại MH khởi tạo, thoát Focus
 | 
Truy vấn thông tin chủ tài khoản nội bộ theo số thẻ

queryCustomerByCard
 | 

 | {api_base_url}/queryCustomerByCard | 

Xem chi tiết
"cardNo": Số thẻ

 | 

Xem chi tiết
"accountNo": Số tài khoản
"cardHolder": Tên chủ thẻ

 | 

 | 
Tại MH khởi tạo, thoát Focus
 | 
Truy vấn thông tin khách hàng theo SDT

queryCustomerByPhone
 | 

 | {api_base_url}/queryCustomerByPhone | 

Xem chi tiết
"mobile": Số điện thoại khách hàng

 | 

Xem chi tiết
"mobile": Số điện thoại khách hàng
"fullname": Tên khách hàng

 | 

 | 
Tại MH khởi tạo, nhấn Tiếp tục
 | 
Khởi tạo giao dịch theo lô
 | 

 | 
 | 
Các tham số cần có

• Loại chuyển tiền
• Thông tin các GD đơn trong lô | 
Các tham số cần có

• Mã lô chuyển tiền
• Mã các GD đơn
• STT trong queue của lô | tạo mới API
 | 
Tại MH Xác thực giao dịch, nhập OTP và nhấn Xác nhận
 | 
Chuyển khoản nội bộ NHHT qua tài khoản thanh toán

createInternalFTToAcc
 | 

 | {api_base_url}/createInternalFTToAcc | 

Xem chi tiết
"accountNo": Số tài khoản
"desAccountNo": Tài khoản người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

Xem chi tiết
"desAccountNo": Tài khoản người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

 | 
Tại MH Xác thực giao dịch, nhập OTP và nhấn Xác nhận
 | 
Chuyển khoản nội bộ NHHT qua số thẻ

createInternalFTToCard
 | 

 | {api_base_url}/createInternalFTToCard | 

Xem chi tiết
"accountNo": Số tài khoản
"desCardNo": Số thẻ nhận tiền
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

Xem chi tiết
"desCardNo": Số thẻ nhận tiền
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

### 3/ Luồng màn hình

#### 3.1/ Danh sách màn hình

a. Nhóm màn hình khởi tạo

##### MH1: Chuyển tiền nội bộ khác chủ đơn lẻ

##### MH2: Chuyển tiền nội bộ khác chủ cho nhiều người

##### MH3: Chuyển tiền nội bộ khác chủ cho 10 người

##### MH4: Nhập Số điện thoại người hưởng gợi ý danh bạ

##### MH5: Nhập Số tài khoản người hưởng

##### MH6: Lưu danh bạ thụ hưởng

##### MH7: Nhập số tiền gợi ý số tiền chuyển

##### MH8: Nhập thông tin chuyển tiền hiển thị tổng số tiền

##### MH9: Thông báo lỗi người hưởng, thông tin chuyển tiền

##### MH10: Hightlight hiển thị người hưởng bị lỗi và thông tin lỗi

b. Nhóm màn hình Danh bạ

##### MH11: Tab Danh bạ thụ hưởng - hiển thị switch chọn nhiều người

##### MH12: Tab Danh bạ thụ hưởng - ON switch và chọn nhiều người hưởng

##### MH13: Tab Danh bạ thụ hưởng - chọn nhiều người hưởng TH MH khởi tạo đã có nhiều người hưởng

c. Nhóm màn hình Phương thức xác thực

##### MH14: Phương thức xác thực TH 1 người nhận (giữ nguyên)

##### MH15: Phương thức xác thực TH 3 người nhận

##### MH16: Phương thức xác thực TH 10 người nhận

##### MH17: Xem tất cả - TH thông tin chuyển tiền giống nhau

##### MH18: Xem tất cả - TH thông tin chuyển tiền khác nhau

d. Nhóm màn hình Xác thực giao dịch

##### MH19: Xác thực giao dịch

e. Nhóm màn hình Kết quả giao dịch

##### MH20: Kết quả giao dịch

##### MH21: Kết quả giao dịch - Chi tiết chuyển tiền thành công

##### MH22: Kết quả giao dịch - Chi tiết chuyển tiền không thành công do lỗi

##### MH23: Kết quả giao dịch - Chi tiết chuyển tiền nghi vấn do Time Out

##### 

#### 3.2/ Mô tả màn hình

Đối với chuyển tiền nội bộ khác chủ theo GD đơn lẻ tham khảo ()

##### MH A: Nhóm màn hình Khởi tạo

 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả | 

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước
 | 

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nội bộ khác chủ
 | 

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
--
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị Số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 

 | 4 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Tiêu đề: Thông tin người hưởng + (n/m) 

n là số lượng người hưởng hiện tại

m là số lượng người hưởng tối đa
 | 

 | 6 | Thêm người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định enable

Nhấn Thêm người hưởng sẽ hiển thị icon người hưởng và các trường thông tin người hưởng

Nếu số lượng người hưởng đạt tối đa thì sẽ disable và không cho thêm người hưởng
 | 

 | 7 | Người hưởng | 
List
 | 

 | 
--
 | 
--
 | 
Hiển thị danh sách người hưởng

• Icon avatar cho từng người hưởng, có highlight khi nhấn chọn người hưởng
• Nhấn icon người hưởng sẽ hiển thị thông tin chuyển tiền của người hưởng đó | 

 | 8 | Xóa người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi số lượng người hưởng > 1

Hiển thị text Xóa người hưởng + số thứ tự người hưởng đang được chọn
 | 

 | 9 | 
Tài khoản thụ hưởng
 | 
Textbox
 | 
number
 | 
--
 | 
--
 | 
Mặc định trống

Placeholder: Số tài khoản/số thẻ/số điện thoại

Cho phép nhập/chọn:

• Nếu nhập:
• Cho phép nhập tối đa 25 ký tự số (bàn phím số)
• Thoát Focus kiểm tra thông tin thụ hưởng  → Tham khảo logic xử lý
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý | 

 | 10 | 
Icon danh bạ thụ hưởng
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon danh bạ thụ hưởng → vào màn hình Danh bạ thụ hưởng và focus tab thụ hưởng
 | 

 | 11 | 
Tên người thụ hưởng/ Số tài khoản
 | 
label
 | 
Read only
 | 
--
 | 
--
 | 
Nếu nhập/chọn số tài khoản thụ hưởng và có kết quả truy vấn thành công: Hiển thị thông tin tên tài khoản

Nếu nhập/chọn số điện thoại/số thẻ thụ hưởng và có kết quả truy vấn thành công: Hiển thị thông tin số tài khoản, tên tài khoản thụ hưởng (Kiểm tra số điện thoại tại hệ thống MB)
 | 

 | 12 | 
Lưu danh bạ thụ hưởng
 | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi nhập thông tin "Số tài khoản/số thẻ/số điện thoại" và có kết quả truy vấn thụ hưởng thành công.

Mặc định là tắt (OFF)

Cho phép thực hiện switch ON/OFF

Nếu bật (ON) sẽ hiển thị nhập tên gợi nhớ

Không hiển thị khi chọn thông tin thụ hưởng từ danh bạ thụ hưởng
 | 

 | 13 | Tên gợi nhớ | Textbox | Text | -- | 20 | 
Chỉ hiển thị khi nhập thông tin "Số tài khoản/số thẻ/số điện thoại" có kết quả truy vấn thụ hưởng thành công và nút Lưu người thụ hưởng switch ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu | 

 | 14 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Tiêu đề: Thông tin chuyển tiền | 

 | 15 | Thông tin chuyển tiền giống nhau | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Với những dòng máy MH nhỏ thì text hiển thị sẽ được xuống dòng

Mặc định là tắt (OFF)

Cho phép thực hiện switch ON/OFF

Nếu bật (ON) sẽ sao chép thông tin chuyển tiền tất cả người thụ giống nhau. 
 | 

 | 17 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
--
 | 
13
 | 
Nhập vào ô số tiền::

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý
 | 

 | 18 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”
 | 

 | 19 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển do Bank server trả về theo danh sách tài khoản nguồn

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Focus ô Nội dung giao dịch → Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
 | 

 | 20 | 
Tổng số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền được chuyển cho tất cả người hưởng + đơn vị tiền tệ VND
 | 

 | 21 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

 | 22 | 
Kiểm tra lại thông tin
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

##### MH B: Nhóm màn hình Danh bạ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Nút đóng | Icon | Click | 
--
 | 
--
 | Nhấn dấu "X" → Đóng màn hình popup Danh bạ
 | 2 | Danh bạ | List | 
 | 
--
 | 
--
 | 
Gồm 2 tab: Danh bạ thụ hưởng và Danh bạ điện thoại

Mặc định focus màn hình Danh bạ thụ hưởng

 | 
Tab Danh bạ thụ hưởng

 | 3 | Tiêu đề | Label | Read only | 
--
 | 
--
 | Tiêu đề: Danh bạ thụ hưởng
 | 4 | Tìm kiếm | Textbox | Text | 
--
 | 
--
 | 
Cho phép tìm kiếm tương đối theo tên chủ tài khoản/tên gợi nhớ/số tài khoản/số thẻ lưu trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại quy tắc chung)

 | 5 | Chọn nhiều người thụ hưởng | Swicth Button | Click | 
--
 | 
--
 | 
• Nếu ở màn hình khởi tạo chỉ có 1 người hưởng (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ, ẩn nút Xác nhận, hiện switch button Chọn nhiều người thụ hưởng và mặc định OFF.
      + Nếu OFF thì khi chọn 1 người thụ hưởng trong danh bạ, hệ thống thoát khỏi danh bạ và fill thông tin vào màn hình khởi tạo (như luồng cũ trước đây)
      + Nếu ON thì cho phép chọn nhiều người thụ hưởng.  
      + Nếu ON và chọn người hưởng rồi lại OFF thì bỏ tích tất cả các KH đã tích chọn.

• Nếu ở màn hình khởi tạo đã có từ 2 người hưởng trở lên (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ sẽ không hiển thị switch button Chọn nhiều người thụ hưởng, mặc định luôn là cho chọn nhiều người hưởng
 | 6 | Tiêu đề | Label | Read only | 
--
 | 
--
 | 
Chỉ hiện thị khi số lượng người hưởng > 1

Tiêu đề: Số lượng đã chọn (n người/ tối đa m người)

n là số lượng người hưởng đã chọn ở MH khởi tạo + số lượng người đã chọn ở MH danh bạ

m là tham số cấu hình từ MB Server trả về

Khi tích chọn thêm người thụ hưởng trong MH danh bạ sẽ cộng thêm vào n

 | 7 | Danh sác

> ⚠️ *Nội dung đã cắt ngắn (44231 ký tự gốc). Xem đầy đủ trên Confluence.*


---

#### 16.7.3. Chuyển tiền nhanh 24/7 qua tài khoản theo lô

> **Page ID:** `113771419` · **Version:** 47
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/113771419

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Tuan VN1 | 
 | 
Tạo mới tài liệu
 | V1.0.0

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Chuyển tiền nhanh 24/7 qua tài khoản theo lô
 | Use Case ID | UC-CLTK-01
 | Use Case Description | 
Là người dùng, tôi mong muốn chuyển tiền tới nhiều người nhận cùng 1 lúc

 | Actor | 
KH, MB Client, MB Server, Bank Server

 | Priority | High
 | Trigger | 
KH thực hiện lệnh chuyển tiền nhanh 24/7 qua tài khoản, KH nhập nhiều người nhận tiền (tối đa 3 người)

 | 
Pre-Condition
 | 
1. KH đăng nhập thành công ứng dụng; 
2. KH có tài khoản nguồn hợp lệ để thực hiện giao dịch; 
3. Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch
4. Người hưởng đúng Số tài khoản và Ngân hàng thụ hưởng

 | Post-Condition | 
1. KH thực hiện lệnh chuyển tiền nhanh 24/7 qua tài khoản thành công cho nhiều người thụ hưởng 
2. Tài khoản nguồn của KH bị trừ tổng số tiền GD + phí vs TH người chuyển chịu phí
3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng và trừ phí khi người nhận là người chịu phí
4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]
5. MB Client hiển thị chi tiết các giao dịch thành công, thất bại (nếu có)
6. MB Client hiển thị chi tiết lỗi đối với các giao dịch thất bại (nếu có)

 | Basic Flow | 
1. KH đăng nhập ứng dụng
2. KH chọn chức năng "Chuyển tiền nhanh 24/7 qua tài khoản"
3. KH nhấn thêm người hưởng để chuyển được cho nhiều người (số lượng người hưởng tối đa được cấu hình trong BE và trả về trong API mid409)
4. KH nhập Số tài khoản và ngân hàng của người hưởng
5. KH nhập số tiền, người trả phí, nội dung chuyển tiền cho từng người hưởng
6. KH thực hiện xác thực giao dịch
7. Hệ thống MB server xác thực giao dịch,
8. Hệ thống Bank server hạch toán và trả kết quả lệnh chuyển tiền thành công
9. Hệ thống MB ghi nhận log theo từng GD đơn lẻ của lô vào [Activity Log]
10. Hệ thống MB ghi nhận giao dịch chuyển tiền nhanh 24/7 qua tài khoản  theo từng GD đơn lẻ của lô vào [Transaction History]

 | Alternative Flow | 
1. KH đăng nhập ứng dụng; 
2. KH chọn chức năng "Chuyển tiền nhanh 24/7 qua tài khoản"; 
3. KH thêm người thụ hưởng
4. KH nhập Số tài khoản
5. KH nhập số tiền, đối tượng chịu phí, nội dung chuyển tiền; 
Tiếp theo mục 6 của Basic Flow.

 | Exception Flow | 
1. KH thực hiện khởi tạo giao dịch không thành công 
2. KH thực hiện xác thực giao dịch không thành công
3. KH chọn hủy lệnh giao dịch

 | Bussiness Rules | 
Số lượng người hưởng tối đa 3 người

 | Non-Funtional Requiremnt | 
NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây

NFR-2: Thời gian hiệu lực của 1 GD chuyển tiền đơn lẻ của lô là 20 giây

### 2/ Luồng sơ đồ

#### 2.1/ Sơ đồ

#### 2.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
Đăng nhập hệ thống
 | 
Lấy giá trị config cho client

mid409
 | MB Client - MB Server - Bank Server | {api_base_url}/mid409 | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"List[String] configCode": configCode cần lấy value 

 | 

Xem chi tiết
"configList": [
             {
                 "configCode": maxCus
                 "configValue": 10
             },

             {
                 "configCode": max247toAcc
                 "configValue": 3
             },

             {
                 "configCode": max247toCard
                 "configValue": 3
             }

          ]     

 | 
maxCus: số lượng người nhận tối đa chuyển tiền nội bộ khác chủ theo lô

max247toAcc: số lượng người nhận tối đa chuyển nhanh 24/7 qua TK theo lô

max247toCard: số lượng người nhận tối đa chuyển nhanh 24/7 qua thẻ theo lô

 | 
Tại MH Chuyển tiền, nhấn chọn chức năng Chuyển tiền nhanh 24/7 qua tài khoản
 | 
Lấy danh sách tài khoản thanh toán

queryCurrentAcc
 | MB Client - MB Server - Bank Server | {api_base_url}/queryCurrentAcc | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"accountType": Loại tài khoản

 | 

Xem chi tiết
"accountType": Loại tài khoản
"accountNo": Số tài khoản
"accountName": Tên chủ tài khoản
"availBalance": Số dư khả dụng tài khoản
"currency": Loại tiền tệ
"accountStatus": Trạng thái tài khoản
"branchCode": Mã chi nhánh mở tài khoản
"branchName": Tên chi nhánh mở tài khoản

 | 

 | 
Tại MH khởi tạo, thoát Focus
 | 
Truy vấn thông tin khách hàng theo stk của NAPAS

napasNameInqByAcc
 | 

 | {api_base_url}/napasNameInqByAcc | 

Xem chi tiết
"fromAccount": Số tài khoản gửi tiền
"accountNo": Số tài khoản
"bankCode": Mã ngân hàng

 | 

Xem chi tiết
"accountName": Tên chủ tài khoản

 | 

 | 
Tại MH khởi tạo, nhấn Tiếp tục
 | 
Khởi tạo giao dịch theo lô
 | 

 | 
 | 
Các tham số cần có

• Loại chuyển tiền
• Thông tin các GD đơn trong lô | 
Các tham số cần có

• Mã lô chuyển tiền
• Mã các GD đơn
• STT trong queue của lô | tạo mới API
 | 
Tại MH Xác thực giao dịch, KH nhập OTP và nhấn Xác nhận
 | 
Chuyển khoản liên ngân hàng 247 qua số tài khoản

createNapasFTToAcc
 | 

 | {api_base_url}/createNapasFTToAcc | 

Xem chi tiết
"accountNo": Số tài khoản
"bankCode": Mã ngân hàng thụ hưởng
"desAccountNo": Tài khoản người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

Xem chi tiết
"desAccountNo": Tài khoản người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

### 3/ Luồng màn hình

#### 3.1/ Danh sách màn hình

a. Nhóm màn hình khởi tạo

##### MH1: Chuyển tiền nhanh 24/7 qua tài khoản đơn lẻ

##### MH2: Chuyển tiền nhanh 24/7 qua tài khoản cho nhiều người (TH 3 người hưởng)

##### MH3: Chuyển tiền nhanh 24/7 qua tài khoản cho nhiều người (TH 10 người hưởng)

##### MH4: Nhập thông tin người hưởng

##### MH5: Lưu danh bạ thụ hưởng

##### MH6: Nhập thông tin chuyển tiền

##### MH7: Tổng số tiền chuyển khoản

##### MH8: Thông báo lỗi người hưởng, thông tin chuyển tiền

##### MH9: Highlight hiển thị người hưởng bị lỗi và thông tin lỗi

b. Nhóm màn hình Danh bạ thụ hưởng

##### MH10: Tab Danh bạ thụ hưởng - hiển thị switch chọn nhiều người

##### MH11: Tab Danh bạ thụ hưởng - ON switch và chọn nhiều người hưởng

##### MH12: Tab Danh bạ thụ hưởng - chọn nhiều người hưởng TH MH khởi tạo đã có nhiều người hưởng

c. Nhóm màn hình Phương thức xác thực

##### MH13: Phương thức xác thực TH 1 người nhận

##### MH14: Phương thức xác thực TH 3 người nhận

##### MH15: Phương thức xác thực TH 10 người nhận

##### MH16: Thông tin chuyển tiền giống nhau

##### MH17: Thông tin chuyển tiền khác nhau

d. Nhóm màn hình Xác thực giao dịch

##### MH18: Xác thực giao dịch

e. Nhóm màn hình Kết quả giao dịch

##### MH19: Kết quả giao dịch

##### MH20: Kết quả giao dịch - Chi tiết chuyển tiền thành công

##### MH21: Kết quả giao dịch - Chi tiết chuyển tiền không thành công do lỗi

##### MH22: Kết quả giao dịch - Chi tiết chuyển tiền nghi vấn do Time Out

##### 

#### 3.2/ Mô tả màn hình

Đối với chuyển tiền nhanh 24/7 qua tài khoản theo GD đơn lẻ tham khảo ()

##### MH A: Nhóm màn hình Khởi tạo

 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả | 

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước
 | 

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nhanh 24/7 qua tài khoản
 | 

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
--
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị Số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 

 | 4 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Tiêu đề: Thông tin người hưởng + (n/m) 

n là số lượng người hưởng hiện tại

m là số lượng người hưởng tối đa
 | 

 | 6 | Thêm người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định enable

Nhấn Thêm người hưởng sẽ hiển thị icon người hưởng và các trường thông tin người hưởng

Nếu số lượng người hưởng đạt tối đa thì sẽ disable và không cho thêm người hưởng
 | 

 | 7 | Người hưởng | 
List
 | 

 | 
--
 | 
--
 | 
Hiển thị danh sách người hưởng

• Icon avatar cho từng người hưởng, có highlight khi nhấn chọn người hưởng
• Nhấn icon người hưởng sẽ hiển thị thông tin chuyển tiền của người hưởng đó | 

 | 8 | Xóa người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi số lượng người hưởng > 1

Hiển thị text Xóa người hưởng + số thứ tự người hưởng đang được chọn
 | 

 | 9 | 
Tài khoản thụ hưởng
 | 
Textbox
 | 
number
 | 
--
 | 
--
 | 
Mặc định trống 

Placeholder: Tài khoản thụ hưởng

Cho phép nhập/chọn:

• Nếu nhập: cho phép nhập tối đa 30 ký tự số và chữ
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý | 

 | 10 | 
Tên người thụ hưởng
 | 
Label
 | 
Read only
 | 
--
 | 
--
 | 
Tên người thụ hưởng chỉ hiện lên khi thông tin nhập vào là số tài khoản và ngân hàng thụ hưởng được hệ thống trả kết quả về đúng
 | 

 | 11 | 
Ngân hàng thụ hưởng
 | Listbox | Select | x | -- | 
Hiển thị danh sách các ngân hàng mà Co-opBank đã kết nối.

Danh sách ngân hàng thụ hưởng được cấu hình trên BO Client do MB Server trả về.

Yêu cầu hiển thị:

• Thứ tự hiển thị theo MB server trả về
• Hiển thị những thông tin: (<tên viết tắt ngân hàng>) Tên ngân hàng
• Khi dữ liệu trống, hiển thị thông báo: Không có dữ liệu hiển thị. | 

 | 12 | 
Icon danh bạ thụ hưởng
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon danh bạ thụ hưởng → vào màn hình Danh bạ thụ hưởng
 | 

 | 13 | 
Lưu danh bạ thụ hưởng
 | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi nhập thông tin Số tài khoản và có kết quả truy vấn thụ hưởng thành công.

Mặc định là tắt (OFF)

Cho phép thực hiện switch ON/OFF

Nếu bật (ON) sẽ hiển thị nhập tên gợi nhớ

Không hiển thị khi chọn thông tin thụ hưởng từ danh bạ thụ hưởng
 | 

 | 14 | Tên gợi nhớ | Textbox | Text | -- | 20 | 
Chỉ hiển thị khi nhập thông tin Số tài khoản và có kết quả truy vấn thụ hưởng thành công và nút Lưu người thụ hưởng switch ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu | 

 | 15 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Tiêu đề: Thông tin chuyển tiền | 

 | 16 | Thông tin chuyển tiền giống nhau | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Với những dòng máy MH nhỏ thì text hiển thị sẽ được xuống dòng

Mặc định là tắt (OFF)

Cho phép thực hiện switch ON/OFF

Nếu bật (ON) sẽ sao chép thông tin chuyển tiền tất cả người thụ giống nhau. 
 | 

 | 17 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
--
 | 
13
 | 
Nhập vào ô số tiền:

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý
 | 

 | 18 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”
 | 

 | 19 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển do Bank server trả về theo danh sách tài khoản nguồn

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Focus ô Nội dung giao dịch → Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
 | 

 | 20 | 
Tổng số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền được chuyển cho tất cả người hưởng + đơn vị tiền tệ VND
 | 

 | 21 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

 | 22 | 
Kiểm tra lại thông tin
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

##### MH B: Nhóm màn hình Danh bạ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | Read only | 
--
 | 
--
 | Tiêu đề: Danh bạ thụ hưởng
 | 2 | Nút "X" | Icon | Click | 
--
 | 
--
 | Đóng màn hình popup → Giữ nguyên màn hình khởi tạo giao dịch trước đó
 | 3 | Tìm kiếm | Textbox | Text | 
--
 | 
--
 | 
Cho phép tìm kiếm tương đối theo tên chủ tài khoản/tên gợi nhớ/số tài khoản trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại quy tắc chung)

 | 4 | Chọn nhiều người thụ hưởng | Swicth Button | Click | 
--
 | 
--
 | 
• Nếu ở màn hình khởi tạo chỉ có 1 người hưởng (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ, ẩn nút Xác nhận, hiện switch button Chọn nhiều người thụ hưởng và mặc định OFF.
      + Nếu OFF thì khi chọn 1 người thụ hưởng trong danh bạ, hệ thống thoát khỏi danh bạ và fill thông tin vào màn hình khởi tạo (như luồng cũ trước đây)
      + Nếu ON thì cho phép chọn nhiều người thụ hưởng.  
      + Nếu ON và chọn người hưởng rồi lại OFF thì bỏ tích tất cả các KH đã tích chọn.

• Nếu ở màn hình khởi tạo đã có từ 2 người hưởng trở lên (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ sẽ không hiển thị switch button Chọn nhiều người thụ hưởng, mặc định luôn là cho chọn nhiều người hưởng
 | 5 | Tiêu đề | Label | Read only | 
--
 | 
--
 | 
Chỉ hiện thị khi số lượng người hưởng > 1

Tiêu đề: Số lượng đã chọn (n người/ tối đa m người)

n là số lượng người hưởng đã chọn ở MH khởi tạo + số lượng người đã chọn ở MH danh bạ

m là tham số cấu hình từ MB Server trả về

Khi tích chọn thêm người thụ hưởng trong MH danh bạ sẽ cộng thêm vào n

 | 6 | Danh sách tài khoản thụ hưởng  | List | Click | 
--
 | 
--
 | 
Là danh sách tài khoản lưu tại Danh bạ thụ hưởng, mục Chuyển tiền danh 24/7 qua tài khoản

Thông tin hiển thị gồm:

• Logo bank
• Tên chủ tài khoản/tên gợi nhớ đã lưu
• Số tài khoản thụ hưởng
Nhấn chọn 1 số tài khoản → Tham khảo logic xử lý

 | 7 | Xác nhận | Button | Click | 
--
 | 
--
 | 
Mặc định Disable

Chọn ít nhất 1 người hưởng sẽ Enable

##### MH C: Nhóm màn hình Phương thức xác thực
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read Only | 
--
 | 
--
 | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo:
 | 
4
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản nguồn

 | 
5
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tiêu đề: Thông tin người hưởng + số lượng người hưởng

 | 
6
 | 
Xem tất cả
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi số lượng người hưởng > 1

 | 
7
 | 
Người hưởng
 | 
List
 | 

 | 
--
 | 
--
 | 
Hiển thị danh sá

> ⚠️ *Nội dung đã cắt ngắn (37960 ký tự gốc). Xem đầy đủ trên Confluence.*


---

#### 16.7.4. Chuyển tiền nhanh 24/7 qua thẻ theo lô

> **Page ID:** `118556037` · **Version:** 38
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/118556037

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Tuan VN1 | 
 | 
Tạo mới tài liệu
 | V1.0.0

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Chuyển tiền nhanh 24/7 qua thẻ theo lô
 | Use Case ID | UC-CLTK-01
 | Use Case Description | 
Là người dùng, tôi mong muốn chuyển tiền tới nhiều người nhận cùng 1 lúc

 | Actor | 
KH, MB Client, MB Server, Bank Server

 | Priority | High
 | Trigger | 
KH thực hiện lệnh chuyển tiền nhanh 24/7 qua thẻ, KH nhập nhiều người nhận tiền (tối đa 3 người)

 | 
Pre-Condition
 | 
1. KH đăng nhập thành công ứng dụng; 
2. KH có tài khoản nguồn hợp lệ để thực hiện giao dịch; 
3. Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch
4. Người hưởng đúng Số thẻ

 | Post-Condition | 
1. KH thực hiện lệnh chuyển tiền nhanh 24/7 qua thẻ thành công cho nhiều người thụ hưởng 
2. Tài khoản nguồn của KH bị trừ trừ tổng số tiền GD + phí vs TH người chuyển chịu phí
3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng và trừ phí khi người nhận là người chịu phí
4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]
5. MB Client hiển thị chi tiết các giao dịch thành công, thất bại (nếu có)
6. MB Client hiển thị chi tiết lỗi đối với các giao dịch thất bại (nếu có)

 | Basic Flow | 
1. KH đăng nhập ứng dụng
2. KH chọn chức năng "Chuyển tiền nhanh 24/7 qua thẻ"
3. KH nhấn thêm người hưởng để chuyển được cho nhiều người (số lượng người hưởng tối đa được cấu hình trong BE và trả về trong API mid409)
4. KH nhập Số thẻ của người hưởng
5. KH nhập số tiền, người trả phí, nội dung chuyển tiền cho từng người hưởng
6. KH thực hiện xác thực giao dịch
7. Hệ thống MB server xác thực giao dịch,
8. Hệ thống Bank server hạch toán và trả kết quả lệnh chuyển tiền thành công
9. Hệ thống MB ghi nhận log theo từng GD đơn lẻ của lô vào [Activity Log]
10. Hệ thống MB ghi nhận giao dịch chuyển tiền nhanh 24/7 qua thẻ theo từng GD đơn lẻ của lô vào [Transaction History]

 | Alternative Flow | 
1. KH đăng nhập ứng dụng; 
2. KH chọn chức năng "Chuyển tiền nhanh 24/7 qua thẻ"; 
3. KH thêm người thụ hưởng
4. KH nhập Số thẻ
5. KH nhập số tiền, đối tượng chịu phí, nội dung chuyển tiền; 
Tiếp theo mục 6 của Basic Flow.

 | Exception Flow | 
1. KH thực hiện khởi tạo giao dịch không thành công 
2. KH thực hiện xác thực giao dịch không thành công
3. KH chọn hủy lệnh giao dịch

 | Bussiness Rules | 
Số lượng người hưởng tối đa 3 người

 | Non-Funtional Requiremnt | 
NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây

NFR-2: Thời gian hiệu lực của 1 GD chuyển tiền đơn lẻ của lô là 20 giây

### 2/ Luồng sơ đồ

#### 2.1/ Sơ đồ

#### 2.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
Đăng nhập hệ thống
 | 
Lấy giá trị config cho client

mid409
 | MB Client - MB Server - Bank Server | {api_base_url}/mid409 | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"List[String] configCode": configCode cần lấy value 

 | 

Xem chi tiết
"configList": [
             {
                 "configCode": maxCus
                 "configValue": 10
             },

             {
                 "configCode": max247toAcc
                 "configValue": 3
             },

             {
                 "configCode": max247toCard
                 "configValue": 3
             }

          ]     

 | 
maxCus: số lượng người nhận tối đa chuyển tiền nội bộ khác chủ theo lô

max247toAcc: số lượng người nhận tối đa chuyển nhanh 24/7 qua TK theo lô

max247toCard: số lượng người nhận tối đa chuyển nhanh 24/7 qua thẻ theo lô

 | 
Tại MH Chuyển tiền, nhấn chọn chức năng Chuyển tiền nhanh 24/7 qua thẻ
 | 
Lấy danh sách tài khoản thanh toán

queryCurrentAcc
 | MB Client - MB Server - Bank Server | {api_base_url}/queryCurrentAcc | 

Xem chi tiết
"username": tài khoản đăng nhập MB Client
"accountType": Loại tài khoản

 | 

Xem chi tiết
"accountType": Loại tài khoản
"accountNo": Số tài khoản
"accountName": Tên chủ tài khoản
"availBalance": Số dư khả dụng tài khoản
"currency": Loại tiền tệ
"accountStatus": Trạng thái tài khoản
"branchCode": Mã chi nhánh mở tài khoản
"branchName": Tên chi nhánh mở tài khoản

 | 

 | 
Tại MH khởi tạo, thoát Focus
 | 
Truy vấn thông tin khách hàng theo stk của NAPAS

napasNameInqByAcc
 | 

 | {api_base_url}/napasNameInqByAcc | 

Xem chi tiết
"fromAccount": Số tài khoản gửi tiền
"accountNo": Số tài khoản
"bankCode": Mã ngân hàng

 | 

Xem chi tiết
"accountName": Tên chủ tài khoản

 | 

 | 
Tại MH khởi tạo, nhấn Tiếp tục
 | 
Khởi tạo giao dịch theo lô
 | 

 | 
 | 
Các tham số cần có

• Loại chuyển tiền
• Thông tin các GD đơn trong lô | 
Các tham số cần có

• Mã lô chuyển tiền
• Mã các GD đơn
• STT trong queue của lô | tạo mới API
 | 
Tại MH Xác thực giao dịch, KH nhập OTP và nhấn Xác nhận
 | 
Chuyển khoản liên ngân hàng 247 qua số thẻ

createNapasFTToCard
 | 

 | {api_base_url}/createNapasFTToCard | 

Xem chi tiết
"accountNo": Số tài khoản
"desCardNo": Số thẻ người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

Xem chi tiết
"desCardNo": Số thẻ người thụ hưởng
"transAmount": Số tiền giao dịch
"transRemark": Nội dung giao dịch
"transFee": Phí giao dịch
"transVAT": VAT
"feeType": Người chịu phí

 | 

### 3/ Luồng màn hình

#### 3.1/ Danh sách màn hình

a. Nhóm màn hình khởi tạo

##### MH1: Chuyển tiền nhanh 24/7 qua thẻ đơn lẻ

##### MH2: Chuyển tiền nhanh 24/7 qua thẻ cho nhiều người (TH 3 người hưởng)

##### MH3: Chuyển tiền nhanh 24/7 qua thẻ cho nhiều người (TH 10 người hưởng)

##### MH4: Nhập thông tin người hưởng

##### MH5: Lưu danh bạ thụ hưởng

##### MH6: Nhập thông tin chuyển tiền

##### MH7: Tổng số tiền chuyển khoản

##### MH8: Thông báo lỗi người hưởng, thông tin chuyển tiền

##### MH9: Highlight người hưởng bị lỗi

b. Nhóm màn hình Danh bạ thụ hưởng

##### MH10: Tab Danh bạ thụ hưởng - hiển thị switch chọn nhiều người

##### MH11: Tab Danh bạ thụ hưởng - ON switch và chọn nhiều người hưởng

##### MH12: Tab Danh bạ thụ hưởng - chọn nhiều người hưởng TH MH khởi tạo đã có nhiều người hưởng

c. Nhóm màn hình Phương thức xác thực

##### MH13: Phương thức xác thực TH 1 người nhận

##### MH14: Phương thức xác thực TH 3 người nhận

##### MH15: Phương thức xác thực TH 10 người nhận

##### MH16: Thông tin chuyển tiền giống nhau

##### MH17: Thông tin chuyển tiền khác nhau

d. Nhóm màn hình Xác thực giao dịch

##### MH18: Xác thực giao dịch

e. Nhóm màn hình Kết quả giao dịch

##### MH19: Kết quả giao dịch

##### MH20: Kết quả giao dịch - Chi tiết chuyển tiền thành công

##### MH21: Kết quả giao dịch - Chi tiết chuyển tiền không thành công do lỗi

##### MH22: Kết quả giao dịch - Chi tiết chuyển tiền nghi vấn do Time Out

##### 

#### 3.2/ Mô tả màn hình

Chuyển tiền nhanh 24/7 qua thẻ đối với 1 GD đơn lẻ tham khảo ( )

##### MH A: Nhóm màn hình Khởi tạo
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả | 

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước
 | 

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nhanh 24/7 qua thẻ
 | 

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
--
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị Số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 

 | 4 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Tiêu đề: Thông tin người hưởng + (n/m) 

n là số lượng người hưởng hiện tại

m là số lượng người hưởng tối đa
 | 

 | 6 | Thêm người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định enable

Nhấn Thêm người hưởng sẽ hiển thị icon người hưởng và các trường thông tin người hưởng

Nếu số lượng người hưởng đạt tối đa thì sẽ disable và không cho thêm người hưởng
 | 

 | 7 | Người hưởng | 
List
 | 

 | 
--
 | 
--
 | 
Hiển thị danh sách người hưởng

• Icon avatar cho từng người hưởng, có highlight khi nhấn chọn người hưởng
• Nhấn icon người hưởng sẽ hiển thị thông tin chuyển tiền của người hưởng đó | 

 | 8 | Xóa người hưởng | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi số lượng người hưởng > 1

Hiển thị text Xóa người hưởng + số thứ tự người hưởng đang được chọn
 | 

 | 9 | 
Số thẻ thụ hưởng
 | 
Textbox
 | 
number
 | 
--
 | 
--
 | 
Mặc định trống 

Placeholder: Số thẻ thụ hưởng

Cho phép nhập/chọn:

• Nếu nhập:
• Cho phép nhập tối đa 30 ký tự số
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý | 

 | 10 | 
Tên người thụ hưởng
 | 
Label
 | 
Read only
 | 
--
 | 
--
 | 
Tên người thụ hưởng chỉ hiện lên khi thông tin nhập vào là số thẻ được hệ thống trả kết quả về đúng
 | 

 | 11 | 
Icon danh bạ thụ hưởng
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon danh bạ thụ hưởng → vào màn hình Danh bạ thụ hưởng
 | 

 | 12 | 
Lưu danh bạ thụ hưởng
 | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi nhập thông tin "Số thẻ thụ hưởng" và có kết quả truy vấn thụ hưởng thành công.

Mặc định: OFF

Cho phép thực hiện switch ON/OFF

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng
 | 

 | 13 | Tên gợi nhớ | Textbox | Text | -- | 20 | 
Chỉ hiển thị khi nhập thông tin "Số thẻ thụ hưởng" và có kết quả truy vấn thụ hưởng thành công và nút Lưu người thụ hưởng switch ON

Không hiển thị khi chọn thông tịn thụ hưởng từ danh bạ thụ hưởng

• Nhập ký tự tiếng Việt có dấu | 

 | 14 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Tiêu đề: Thông tin chuyển tiền | 

 | 15 | Thông tin chuyển tiền giống nhau | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
Với những dòng máy MH nhỏ thì text hiển thị sẽ được xuống dòng

Mặc định là tắt (OFF)

Cho phép thực hiện switch ON/OFF

Nếu bật (ON) sẽ sao chép thông tin chuyển tiền tất cả người thụ giống nhau. 
 | 

 | 16 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
--
 | 
13
 | 
Nhập vào ô số tiền:

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý
 | 

 | 17 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”
 | 

 | 18 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
Mặc định: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển do Bank server trả về theo danh sách tài khoản nguồn

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

Focus ô Nội dung giao dịch → Hiển thị nút "X" cho phép xóa toàn bộ ký tự đã nhập
 | 

 | 19 | 
Tổng số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền được chuyển cho tất cả người hưởng + đơn vị tiền tệ VND
 | 

 | 20 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

 | 21 | 
Kiểm tra lại thông tin
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
 | 

##### MH B: Nhóm màn hình Danh bạ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | Read only | 
--
 | 
--
 | Tiêu đề: Danh bạ thụ hưởng
 | 2 | Nút "X" | Icon | Click | 
--
 | 
--
 | Đóng màn hình popup → Giữ nguyên màn hình khởi tạo giao dịch trước đó
 | 3 | Tìm kiếm | Textbox | Text | 
--
 | 
--
 | 
Cho phép tìm kiếm tương đối theo tên chủ tài khoản/tên gợi nhớ/số thẻ lưu trong danh sách

Chỉ hiển thị khi có trên n bản ghi (xem tại quy tắc chung)

 | 4 | Chọn nhiều người thụ hưởng | Swicth Button | Click | 
--
 | 
--
 | 
• Nếu ở màn hình khởi tạo chỉ có 1 người hưởng (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ, ẩn nút Xác nhận, hiện switch button Chọn nhiều người thụ hưởng và mặc định OFF.
      + Nếu OFF thì khi chọn 1 người thụ hưởng trong danh bạ, hệ thống thoát khỏi danh bạ và fill thông tin vào màn hình khởi tạo (như luồng cũ trước đây)
      + Nếu ON thì cho phép chọn nhiều người thụ hưởng.  
      + Nếu ON và chọn người hưởng rồi lại OFF thì bỏ tích tất cả các KH đã tích chọn.

• Nếu ở màn hình khởi tạo đã có từ 2 người hưởng trở lên (có thể đã điền thông tin thụ hưởng hoặc chưa) thì khi bấm vào icon danh bạ sẽ không hiển thị switch button Chọn nhiều người thụ hưởng, mặc định luôn là cho chọn nhiều người hưởng
 | 5 | Tiêu đề | Label | Read only | 
--
 | 
--
 | 
Chỉ hiện thị khi số lượng người hưởng > 1

Tiêu đề: Số lượng đã chọn (n người/ tối đa m người)

n là số lượng người hưởng đã chọn ở MH khởi tạo + số lượng người đã chọn ở MH danh bạ

m là tham số cấu hình từ MB Server trả về

Khi tích chọn thêm người thụ hưởng trong MH danh bạ sẽ cộng thêm vào n

 | 6 | Danh sách tài khoản thụ hưởng  | List | Click | 
--
 | 
--
 | 
Là danh sách số thẻ lưu tại Danh bạ thụ hưởng, mục Chuyển tiền nhanh 24/7 qua thẻ

Thông tin hiển thị gồm:

• Logo bank
• Tên chủ tài khoản/tên gợi nhớ đã lưu
• Số thẻ thụ hưởng
Nhấn chọn 1 số thẻ → Tham khảo logic xử lý

 | 7 | Xác nhận | Button | Click | 
--
 | 
--
 | 
Mặc định Disable

Chọn ít nhất 1 người hưởng sẽ Enable

##### MH C: Nhóm màn hình Phương thức xác thực
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | Ghi chú | Label | Read Only | 
--
 | 
--
 | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo:
 | 
4
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản nguồn

 | 
5
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tiêu đề: Thông tin người hưởng + số lượng người hưởng

 | 
6
 | 
Xem tất cả
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiển thị khi số lượng người hưởng > 1

 | 
7
 | 
Người hưởng
 | 
List
 | 

 | 
--
 | 
--
 | 
Hiển thị danh sách người hưởng gồm các thông tin:

• Icon avatar cho từng người hưởng
• Họ và tên người hưởng: chỉ hiển thị 4 ký tự đầu
• Số tiền chuyển, hiển thị ngăn cách hàng nghìn bằng dấu “,”
 | 
8
 | 
Tổng số tiền
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền (chưa bao gồm phí và thuế) và đơn vị tiền tệ; Số tiền viết bằng chữ tương ứng(bôi đỏ)

 | 
9
 | 
Tổng số tiền phí và thuế
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền phí và thuế nếu khác 0 và rỗng

 | 
10
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Tiêu đề: Phương thức xác thực

 | 
11
 | 
Phương thức xác thực
 | 
Listbox
 | 
Select
 | 
Yes
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

M

> ⚠️ *Nội dung đã cắt ngắn (36157 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 16.8. Chuyển tiền định kỳ

> **Page ID:** `196348275` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/196348275

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

#### 16.8.1. SOW chức năng chuyển tiền định kỳ

> **Page ID:** `196348100` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/196348100

###  1/ Mục đích & ý nghĩa chức năng

• Giúp KH chủ động khi có các khoản tiền phải chi cố định, thường xuyên
• Giúp KH tiết kiệm thời gian
• Giúp Ngân hàng hoàn thiện thêm các tính năng của App, và nâng cao trải nghiệm người dùng

### 2/ Phạm vi

#### 2.1/ Phạm vi FrontEnd
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Chuyển tiền | 
• Đặt lịch chuyển tiền nội bộ cùng chủ
• Đặt lịch chuyển tiền khác chủ (Chỉ cho phép đặt lịch chuyển tiền tới số tài khoản, không cho phép đặt lịch chuyển tiền tới số điện thoại, số thẻ, số tài khoản alias) | 
RedThêm mới
 | MB | 
Cho phép KH tạo lệnh chuyển tiền (Chỉ là tạo lệnh vì lúc này giao dịch chuyển tiền chưa được thực hiện)

• Bước 1: KH chọn chức năng Đặt lịch chuyển tiền
• Bước 2: KH nhập thông tin để đặt lịch : Chọn ngày bắt đầu thực hiện lệnh chuyển tiền, tần suất... Có 2 kiểu tần suất:
     - Không lặp lại: Lệnh chỉ được thực hiện 1 lần

     - Lặp lại: Lệnh được thực hiện nhiều lần, theo số lần KH chọn

• Bước 3: KH xác nhận đặt lịch
• Bước 4: Hệ thống kiểm tra hạn mức tối thiểu/ tối đa theo giao dịch (Không kiểm tra hạn mức ngày, hạn mức gói dịch vụ)
• Bước 5: Xác thực giao dịch thành công--> Hệ thống MB gửi yêu cầu tạo lệnh chuyển tiền sang hệ thống Bank
• Bước 6: Đến ngày hiệu lực của lệnh chuyển tiền đã đặt. Hệ thống Bank thực hiện trích/ chuyển tiền cho KH theo thông tin đã đặt lịch | 
BlueTrung Bình
 | Client, Server, Bank | 

 | Chuyển tiền | Danh sách đặt lịch chuyển tiền | 
RedThêm mới
 | MB | 
Cho phép KH tra cứu trạng thái lệnh chuyển tiền đã đặt tính đến hiện tại
 | 
BlueTrung Bình
 | 
Client, Server, Bank
 | 

#### 2.2/ Phạm vi Server
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Số dư khả dụng/ Hạn mức/ Phí | Kiểm tra số dư khả dụng | 
BlueCập nhật

(Chỉ áp dụng riêng cho các chức năng được nhắc đến trong SOW này)
 | MB | 
• Không kiểm tra số dư khả dụng
• Không kiểm tra hạn mức gói dịch vụ, hạn mức ngày (Vẫn áp dụng hạn mức tối thiểu/ tối đa/ giao dịch)
• Không tính phí giao dịch | 
RedKhó
 | Server | 

#### 2.2/ Phạm vi Backend
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Link tài liệu
 | Cấu hình | 
Quản lý tần suất đặt lịch chuyển tiền
 | 
RedThêm mới
 | BE | 
Chức năng cho phép Bank khai báo các loại tần suất đặt lịch được phép chọn trên App Client.

Ví dụ:

• 1 tuần/ lần (1 tuần = 7 ngày)
• 2 ngày/ lần
• 1 tháng/ lần 
• 1 quý/ lần (1 quý = 3 tháng)
• 1 năm/ lần | 
BlueTRUNG BÌNH
 | 
 | Báo cáo | 
Báo cáo chi tiết giao dịch đặt lịch chuyển tiền
 | 
RedThêm mới
 | BE | 
Chức năng cho phép thống kê lại các giao dịch đặt lệnh đã được thực hiện trên App.
 | 
BlueTRUNG BÌNH
 | 
 | Quản lý khách hàng | 
Hủy dịch vụ mobile banking
 | 
BlueCập nhật
 | BE | 
Sau khi duyệt hủy dịch vụ MB gọi API Hủy trạng thái đặt lệnh chuyển tiền sang Bank.
 | 
BlueTRUNG BÌNH
 | 

2.4/ Đánh giá ảnh hưởng

App/ Server

• Test lại Hạn mức gói dịch vụ và hạn mức theo ngày của các dịch vụ khác
• Test lại logic tính phí, kiểm tra số dư khả dụng của các dịch vụ khác
• Test lại toàn bộ chức năng Chuyển tiền nội bộ cùng chủ và Chuyển tiền nội bộ khác chủ (Chú ý test UX, bao gồm cả chức năng chuyển tiền nội bộ khác chủ theo lô)
#### 2.4/ Phạm vi API Bank cung cấp cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Kênh sử dụng | Input | Output | Ghi chú
 | 1 | createScheduleFundsTransfer  | Gửi yêu cầu tạo lệnh chuyển tiền sang Bank | 
 | 

 | 

 | 

 | 2 | queryScheduleAccount | Gửi yêu cầy lấy danh sách lệnh chuyển tiền sang Bank | 
 | 

 | 

 | Tên API hơi ngược so với các API lấy danh sách khác (Do Bank cấp API này sau nên không đổi được tên)
 | 
 | queryScheduleAccountSum | Gửi yêu cầu lấy chi tiết lệnh chuyển tiền | 
 | 

 | 

 | 

 | 3 | updateScheduleAccount |  Cập nhật trạng thái lệnh chuyển tiền | 
 | 

 | 

 | 

### 3/ Q&A

#### 3.1/ Phạm vi Frontend

#### 3.2/ Phạm vi Backend

3.3/ Phạm vi API kênh cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Câu hỏi | Trả lời | Cần xử lý tiếp | Ghi chú
 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 |

---

#### 16.8.2. Đặt lịch chuyển tiền

> **Page ID:** `206178717` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/206178717

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

##### 16.8.2.1. Flow & Action screen_Nội bộ cùng chủ

> **Page ID:** `205456611` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/205456611

Mục lục
none

### 1/ Danh sách màn hình

##### <MH1.1: Khởi tạo mặc định>

##### <MH1.2: Khởi tạo đặt lịch- Có tần suất>

##### <MH1.3: Khởi tạo đặt lịch- Tần suất Không lặp lại>

##### MH thông báo lỗi

##### <MH2: Xác nhận giao dịch>

##### <MH3: Kết quả giao dịch>

### 3/ Mô tả màn hình

##### <MH1: Khởi tạo mặc định>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Khối thông tin Tài khoản nguồn + Số dư khả dụng | 
--
 | 
--
 | 
--
 | 
--
 | 
Giống luồng hiện tại:

• CK nội bộ cùng chủ: 
 | 2 | Khối thông tin người hưởng | 
--
 | 
--
 | 
--
 | 
-
 | 
Giống luồng hiện tại 

• CK nội bộ cùng chủ: 
 | 3 | Khối thông tin chuyển tiền | 
--
 | 
--
 | 
--
 | 
--
 | 
• Trường số tiền và Nội dung giao dịch: Giữ nguyên theo quy tắc hiện tại
• Trường Đối tượng chịu phí 
         - Ẩn trường đối tượng chịu phí nếu chọn ON Đặt lịch chuyển tiền (Do Bank tự tính phí và hạch toán)

         - Hiển thị lại trường đối tượng chịu phí nếu chọn OFF Đặt lịch chuyển tiền

 | 4 | Khối thông tin Đặt lịch chuyển tiền | 
Icon
 | 
Toggle ON/OFF
 | 
--
 | 
--
 | 
• Mặc định OFF
• Cho phép chọn ON/OFF. Khi chọn ON mở ra các trường thông tin sau:
 | 5 | Tần suất | 
Droplist
 | 
Select
 | 
--
 | 
--
 | 
Bao gồm giá trị "Không lặp lại" và các giá trị tần suất được cấu hình tại BE:

• Không lặp lại <Mặc định> <Fix giá trị này tại Client>
• Hàng ngày <cấu hình tại BE>
• 2 ngày/ lần  <cấu hình tại BE>
• 3 ngày/ lần <cấu hình tại BE>
• Hàng tháng <cấu hình tại BE>
• 2 tháng/ lần <cấu hình tại BE>
• Hàng quý <cấu hình tại BE>
• 3 quý/ lần <cấu hình tại BE>
• Hàng năm <cấu hình tại BE>
• ...
 | 6 | Số lần giao dịch | 
Textbox
 | 
Number
 | 
--
 | 
10
 | 
• Nếu chọn tần suất = Không lặp lại  → Ẩn trường số lần giao dịch
• Nếu chọn tần suất khác Không lặp lại → Mặc định = 2
• Cho phép KH sửa giá trị >= 2 (Không cho sửa giá trị < 2)
• Cho phép hiển thị bàn phím số
• Số lần giao dịch được nhập tối đa <Tham khảo Logic xử lý>
 | 7 | Ngày bắt đầu | 
Datetime
 | 
Select
 | 
--
 | 
--
 | 
• Mặc định ngày T+1
• Chỉ cho phép chọn Ngày tương lai (Không cho chọn ngày quá khứ và ngày hiện tại)
 | 8 | Ngày kết thúc | 
Label
 | 
ReadOnly
 | 

 | 

 | 
• Nếu chọn tần suất = Không lặp lại  → Không hiển thị label Ngày kết thúc
• Nếu chọn tần suất khác Không lặp lại → Hiển thị theo quy tắc sau: Ngày kết thúc = Ngày bắt đầu + (Số lần giao dịch-1) * tần suất
• Nếu tần suất có loại = Tháng/ Quý/ Năm, nếu theo công thức tính Ngày kết thúc, rơi vào tháng không có ngày đó thì lấy luôn ngày cuối tháng của tháng đó (Các loại tần suất Ngày/ Tuần nếu tháng không có ngày đó thì lấy sang ngày của tháng tiếp theo)
Mô tả các trường hợp:
 | 
 | Trường hợp | Cách tính ngày kết thúc | Ghi chú
 | 
1
 | 
• Tần suất : Hàng tháng
• Số lần giao dịch : 4
• Ngày bắt đầu: 10/05/2023 | 
Ngày kết thúc = 10/05/2023 + (4-1) * 1 tháng

  = 10/05/2023 + 3*1 tháng

 Ngày kết thúc = 10/08/2023
 | 
Các lệnh sẽ được thực hiện vào các ngày:

• 10/05/2023
• 10/06/2023
• 10/07/2023
• 10/08/2023
 | 
2
 | 
• Tần suất : 3 ngày/ lần
• Số lần giao dịch : 4
• Ngày bắt đầu: 10/05/2023 | 
Ngày kết thúc = 10/05/2023 + (4-1) * 3 ngày/ lần

   = 10/05/2023 + (4-1) * 3 ngày

   = 10/05/2023 + 3*3 ngày

   = 10/05/2023 + 9 ngày

  Ngày kết thúc = 19/05/2023
 | Các lệnh sẽ được thực hiện vào các ngày:
• 10/05/2023
• 13/05/2023
• 16/05/2023
• 19/05/2023
 | 
3
 | 
• Tần suất : Hàng tháng
• Số lần giao dịch : 2
• Ngày bắt đầu: 31/05/2023 | 
Ngày kết thúc = 31/05/2023 + (2-1) * 1 tháng

= 31/05/2023 + 1 tháng

Ngày kết thúc = 31/06/2023 (Theo công thức)

→ Nhưng do tháng 6 chỉ có 30 ngày

→ Vậy ngày kết thúc = 30/06/2023
 | Các lệnh sẽ được thực hiện vào các ngày:
• 31/05/2023
• 30/06/2023

 | 9 | Lưu ý | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Phí và VAT của từng giao dịch chuyển tiền theo lịch áp dụng theo quy định của Co-opBank trong từng thời kỳ.

 | 10 | Tiếp  tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến MH Xác nhận <Tham khảo logic xử lý>

##### <MH2: Xác nhận giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 2 | Tài khoản nguồn | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 3 | Tài khoản thụ hưởng | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 5 | Tần suất | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ đậm tần suất KH đã chọn.

Nếu Tần suất = Không lặp lại → Hiển thị "Không lặp lại"

 | 6 | Số lần giao dịch | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ đậm số lần giao dịch KH đã chọn

Nếu Tần suất = Không lặp lại → Ẩn trường Số lần giao dịch

 | 7 | Ngày bắt đầu | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 8 | Ngày kết thúc | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nếu Tần suất = Không lặp lại → Ẩn trường Ngày kết thúc

 | 9 | Số tiền | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền bằng số + số tiền bằng chữ

Bôi đỏ đậm số tiền bằng số

 | 10 | Nội dung giao dịch | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 11 | PTXT | 
--
 | 
--
 | 
--
 | 
--
 | 
Không cần phải chọn PTXT

 | 12 | Tiếp  tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến MH Kết quả <Tham khảo logic xử lý>

##### MH3: <Kết quả giao dịch>
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Kết quả giao dịch

 | 
3
 | 
Logo Bank
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Đã đặt lịch thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền bằng số VND

Bôi đỏ số tiền bằng số

 | 
7
 | 
Thời gian đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
9
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
11
 | 
Tần suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ

Nếu Tần suất = Không lặp lại → Hiển thị "Không lặp lại"

 | 
12
 | 
Số lần giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ

Nếu Tần suất = Không lặp lại → Ẩn trường Số lần giao dịch

 | 
13
 | 
Ngày bắt đầu
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
14
 | 
Ngày kết thúc
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nếu Tần suất = Không lặp lại → Ẩn trường Ngày kết thúc

 | 
15
 | 
Mã đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
16
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 
17
 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở lại màn hình khởi tạo CK nội bộ cùng chủ và Clear hết các thông tin của giao dịch trước

 | 
18
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
19
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý

---

##### 16.8.2.2. Flow & Action screen_Nội bộ khác chủ

> **Page ID:** `204702368` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/204702368

Mục lục
none

### 1/ Danh sách màn hình

##### <MH1.1: Khởi tạo mặc định>

##### <MH1.2: Khởi tạo ON Đặt lịch- Ẩn Thêm người thụ hưởng>

##### <MH1.3: Khởi tạo Số người thụ hưởng > 1- Ẩn Đặt lịch>

##### <MH1.4: Khởi tạo đặt lịch- Có tần suất>

##### <MH1.5: Khởi tạo đặt lịch- Tần suất Không lặp lại>

##### <MH2: Xác nhận giao dịch>

##### <MH3: Xác thực giao dịch>

##### <MH4: Kết quả giao dịch>

##### <Các thông báo lỗi>

### 3/ Mô tả màn hình

##### <MH1: Khởi tạo mặc định>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Khối thông tin Tài khoản nguồn + Số dư khả dụng | 
--
 | 
--
 | 
--
 | 
--
 | 
Giống luồng hiện tại:

• CK nội bộ khác chủ : 
 | 2 | Khối thông tin người hưởng | 
--
 | 
--
 | 
--
 | 
-
 | 
Giống luồng hiện tại:

• CK nội bộ khác chủ : 
Lưu ý đối với chuyển tiền theo lô:

• Nếu Số lượng người thụ hưởng > 1 → Ẩn toàn bộ khối thông tin Đặt lịch chuyển tiền. Nếu xóa hết người thụ hưởng → Hiển thị lại khối thông tin Đặt lịch chuyển tiền
• Nếu chọn ON Đặt lịch chuyển tiền → Ẩn nút Thêm người hưởng+ Khi bấm vào danh bạ ẩn nút ON chọn nhiều người thụ hưởng, chỉ cho phép chọn 1 danh bạ. Nếu chọn OFF đặt lịch chuyển tiền → Hiển thị lại nút Thêm người thụ hưởng
 | 3 | Khối thông tin chuyển tiền | 
--
 | 
--
 | 
--
 | 
--
 | 
• Trường số tiền và Nội dung giao dịch: Giữ nguyên theo quy tắc hiện tại
• Trường Đối tượng chịu phí 
         - Ẩn trường đối tượng chịu phí nếu chọn ON Đặt lịch chuyển tiền(Do Bank tự tính phí và hạch toán)

         - Hiển thị lại trường đối tượng chịu phí nếu chọn OFF Đặt lịch chuyển tiền

 | 4 | Khối thông tin Đặt lịch chuyển tiền | 
Icon
 | 
Toggle ON/OFF
 | 
--
 | 
--
 | 
• Mặc định OFF
• Cho phép chọn ON/OFF. Khi chọn ON đặt lịch <Tham khảo logic xử lý>
Bật ON thành công, mở ra các trường thông tin sau:

 | 5 | Tần suất | 
Droplist
 | 
Select
 | 
Y
 | 
--
 | 
Bao gồm giá trị "Không lặp lại" và các giá trị tần suất được cấu hình tại BE:

• Không lặp lại <Mặc định> <Fix giá trị này tại Client>
• Hàng ngày <cấu hình tại BE>
• 2 ngày/ lần  <cấu hình tại BE>
• Hàng tuần<cấu hình tại BE>
• Hàng tháng <cấu hình tại BE>
• 2 tháng/ lần <cấu hình tại BE>
• Hàng quý <cấu hình tại BE>
• 3 quý/ lần <cấu hình tại BE>
• Hàng năm <cấu hình tại BE>
• ...
 | 6 | Số lần giao dịch | 
Textbox
 | 
Number
 | 
Y
 | 
10
 | 
• Nếu chọn tần suất = Không lặp lại  → Ẩn trường số lần giao dịch
• Nếu chọn tần suất khác Không lặp lại → Mặc định = 2
• Cho phép KH sửa giá trị >= 2 (Không cho sửa giá trị < 2)
• Cho phép hiển thị bàn phím số
• Số lần giao dịch được nhập tối đa <Tham khảo Logic xử lý>
 | 7 | Ngày bắt đầu | 
Datetime
 | 
Select
 | 
Y
 | 
--
 | 
• Mặc định ngày T+1
• Chỉ cho phép chọn Ngày tương lai (Không cho chọn ngày quá khứ và ngày hiện tại)
 | 8 | Ngày kết thúc | 
Label
 | 
ReadOnly
 | 

 | 

 | 
• Nếu chọn tần suất = Không lặp lại  → Không hiển thị label Ngày kết thúc
• Nếu chọn tần suất khác Không lặp lại → Hiển thị theo quy tắc sau: Ngày kết thúc = Ngày bắt đầu + (Số lần giao dịch-1) * tần suất
• Nếu tần suất có loại = Tháng/ Quý/ Năm, nếu theo công thức tính Ngày kết thúc, rơi vào tháng không có ngày đó thì lấy luôn ngày cuối tháng của tháng đó (Các loại tần suất Ngày/ Tuần nếu tháng không có ngày đó thì lấy sang ngày của tháng tiếp theo)
Mô tả các trường hợp:
 | 
 | Trường hợp | Cách tính ngày kết thúc | Ghi chú
 | 
1
 | 
• Tần suất : Hàng tháng
• Số lần giao dịch : 4
• Ngày bắt đầu: 10/05/2023 | 
Ngày kết thúc = 10/05/2023 + (4-1) * 1 tháng

  = 10/05/2023 + 3*1 tháng

 Ngày kết thúc = 10/08/2023
 | 
Các lệnh sẽ được thực hiện vào các ngày:

• 10/05/2023
• 10/06/2023
• 10/07/2023
• 10/08/2023
 | 
2
 | 
• Tần suất : 3 ngày/ lần
• Số lần giao dịch : 4
• Ngày bắt đầu: 10/05/2023 | 
Ngày kết thúc = 10/05/2023 + (4-1) * 3 ngày/ lần

   = 10/05/2023 + (4-1) * 3 ngày

   = 10/05/2023 + 3*3 ngày

   = 10/05/2023 + 9 ngày

  Ngày kết thúc = 19/05/2023
 | Các lệnh sẽ được thực hiện vào các ngày:
• 10/05/2023
• 13/05/2023
• 16/05/2023
• 19/05/2023
 | 
3
 | 
• Tần suất : Hàng tháng
• Số lần giao dịch : 2
• Ngày bắt đầu: 31/05/2023 | 
Ngày kết thúc = 31/05/2023 + (2-1) * 1 tháng

= 31/05/2023 + 1 tháng

Ngày kết thúc = 31/06/2023 (Theo công thức)

→ Nhưng do tháng 6 chỉ có 30 ngày

→ Vậy ngày kết thúc = 30/06/2023
 | Các lệnh sẽ được thực hiện vào các ngày:
• 31/05/2023
• 30/06/2023

 | 9 | Lưu ý | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Phí và VAT của từng giao dịch chuyển tiền theo lịch áp dụng theo quy định của Co-opBank trong từng thời kỳ.

 | 10 | Tiếp  tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến MH Xác nhận <Tham khảo logic xử lý>

##### <MH2: Xác nhận giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin đặt lịch đã khởi tạo

 | 2 | Tài khoản nguồn | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 3 | Tài khoản thụ hưởng | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 4 | Tên người thụ hưởng | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 5 | Tần suất | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ đậm tần suất KH đã chọn

Nếu Tần suất = Không lặp lại → Hiển thị "Không lặp lại"

 | 6 | Số lần giao dịch | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ đậm số lần giao dịch KH đã chọn

Nếu Tần suất = Không lặp lại → Ẩn trường Số lần giao dịch

 | 7 | Ngày bắt đầu | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 8 | Ngày kết thúc | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nếu Tần suất = Không lặp lại → Ẩn trường Ngày kết thúc

 | 9 | Số tiền | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Số tiền bằng số + Số tiền bằng chữ

Bôi đỏ đậm số tiền bằng số

 | 10 | Nội dung giao dịch | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 11 | PTXT | 
Combobox
 | 
Select
 | 
Yes
 | 

 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 12 | Tiếp  tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến MH Xác thực <Tham khảo logic xử lý>

##### MH3: <Xác thực giao dịch>

Xem xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH6: <Kết quả giao dịch>
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Kết quả giao dịch

 | 
3
 | 
Logo Bank
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Đã đặt lịch thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền bằng số- VND

Bôi đỏ số tiền bằng số

 | 
7
 | 
Thời gian đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
9
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
10
 | 
Tên người thụ hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
11
 | 
Tần suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ

Nếu Tần suất = Không lặp lại → Hiển thị "Không lặp lại"

 | 
12
 | 
Số lần giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bôi đỏ

Nếu Tần suất = Không lặp lại → Ẩn trường Số lần giao dịch

 | 
13
 | 
Ngày bắt đầu
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
14
 | 
Ngày kết thúc
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nếu Tần suất = Không lặp lại → Ẩn trường Ngày kết thúc

 | 
15
 | 
Mã đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
16
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 
17
 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở lại màn hình khởi tạo Nội bộ khác chủ và Clear hết các thông tin của giao dịch trước

 | 
18
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
19
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý

---

##### 16.8.2.3. User Action Flow_Đặt lịch chuyển tiền

> **Page ID:** `196937030` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/196937030

Mục lục
none

### 1/ Luồng quy trình

---

##### 16.8.2.4. Detai logic flow_Đặt lịch chuyển tiền

> **Page ID:** `205456715` · **Version:** 19
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/205456715

Mục lục
none

### 1/ Truy cập chức năng

Theo luồng hiện tại

### 2/ Khởi tạo giao dịch

Khai báo service riêng 
 | Mã dịch vụ | Tên dịch vụ | Mã loại dịch vụ | Loại dịch vụ | Tên nhóm 630 | Mã nhóm 630
 | 0217 | Đặt lịch chuyển tiền nội bộ cùng chủ | 02 | Chuyển tiền | Dịch vụ khác | 05
 | 0218 | Đặt lịch chuyển tiền nội bộ khác chủ | 02 | Chuyển tiền | Dịch vụ khác | 05

(Quản lý mã dịch vụ tập trung xem tại )
 | 
 | Tác nhân | Mô tả
 | 
##### 1
 | 
##### KH bật ON chức năng Đặt lịch chuyển tiền tại màn hình CK nội bộ cùng chủ và khác chủ và nhập thông tin Số tài khoản thụ hưởng

 | 
 | MB Client | 
Khi KH bật ON chức năng Đặt lịch chuyển tiền. Client thực hiện kiểm tra ngay:

• Không hợp lệ | 
 | Trường hợp | Mô tả | Xử lý
 | 1 | Chưa nhập thông tin người hưởng | 
Hiển thị thông báo:

{Trường bắt buộc không được bỏ trống}. Quý khách vui lòng kiểm tra lại!
 | 
Tắt thông báo:

• Focus vào ô nhập thông tin người hưởng
• Chức năng đặt lịch = OFF
 | 2 | 
Nếu thông tin người hưởng đã nhập thì kiểm tra:

• Nếu chuỗi ký tự là số có độ dài khác 16
• Nhập chuỗi bắt đầu = 970446
• Nếu chuỗi ký tự có chứa chữ
(Mục đích: Chặn không cho đặt lịch chuyển tiền với số điện thoại, số thẻ, số tài khoản Alias)
 | 
Hiển thị thông báo:

Vui lòng nhập Thông tin thụ hưởng là số tài khoản để sử dụng chức năng Đặt lịch.

 | 
Tắt thông báo

• Focus vào ô nhập thông tin người hưởng
• Chức năng đặt lịch = OFF
 | 3 | 
Nhập đúng 16 ký tự số nhưng STK truy vấn sang Bank không tồn tại
 | Tài khoản thụ hưởng không hợp lệ. Quý khách vui lòng kiểm tra lại | Thông báo chung theo Server trả của luồng hiện tại truy vấn STK sang Bank không tồn tại

• Hợp lệ: Cho phép bật ON chức năng Đặt lịch. Hiển thị khối thông tin Đặt lịch chuyển tiền
 | 2 | KH chọn danh sách tần suất tại màn hình CK nội bộ cùng chủ và khác chủ
 | 
 | MB Client | 
Gửi yêu cầu lấy danh sách tần suất (được cấu hình ở BE, chỉ lấy danh sách các tần suất có trạng thái = Hoạt động)

 | 
 | MB Server | 
Trả kết quả lấy danh sách tần suất

 | 
 | MB Client | 
1/ Nhận kết quả do MB Server trả, gồm:

• Loại tần suất (Client dùng để quy đổi ra ngày kết thúc)
• Tần suất: (Client dùng để hiển thị danh sách tần suất và quy đổi ra ngày kết thúc)
• Mô tả (Nếu có Mô tả thì hiển thị theo mô tả)
• Thứ tự (Client dùng để sắp xếp thứ tự hiển thị trong danh sách)
• Số lần giao dịch tối đa (Client dùng để so sánh với số lần giao dịch KH đã nhập)
2/ Hiển thị danh sách tần suất do Server trả về

• Mặc định: Không lặp lại (Fix ở Client)
• Danh sách tần suất sắp xếp theo thứ tự cấu hình theo thứ tự tăng dần)
 | 3 | 
KH nhập số lần giao dịch tại màn hình CK nội bộ cùng chủ và khác chủ

 | 
 | MB Client | 
Sau khi thoát focus. Client kiểm tra số lần giao dịch KH đã nhập với số lần giao dịch tối đa Server đã trả ở bước 2

• Không hợp lệ: Nếu số KH nhập > Số lần giao dịch tối đa → Hiển thị thông báo “Số lần giao dịch không được vượt quá {n} lần” . Đóng thông báo giữ nguyên số lần giao dịch vừa nhập, n là số lần GD tối đa
• Hợp lệ: Nếu số KH nhập =< Số lần giao dịch tối đa → Không hiển thị thông báo
 | 4 | 
KH chọn ngày bắt đầu tại màn hình CK nội bộ cùng chủ và khác chủ

 | 
 | MB Client | 
Dựa vào các thông tin về tần suất MB Server đã trả về ở bước. Client tự tính ra Ngày kết thúc theo công thức đã mô tả tại để hiển thị tại MH khởi tạo

 | 5 | KH bấm Tiếp tục tại màn hình CK nội bộ cùng chủ và khác chủ
 | 
 | MB Client | 
Thực hiện Validate

• Không hợp lệ | 
 | Trường hợp | Mô tả | Xử lý | 

 | 1 | 
Nếu thông tin người hưởng đã nhập thì kiểm tra:

• Nếu chuỗi ký tự là số có độ dài khác 16
• Nhập chuỗi bắt đầu = 970446
• Nếu chuỗi ký tự có chứa chữ
(Mục đích: Chặn không cho đặt lịch chuyển tiền với số điện thoại, số thẻ, số tài khoản Alias)
 | 
Hiển thị thông báo:

Vui lòng nhập Thông tin thụ hưởng là số tài khoản để sử dụng chức năng Đặt lịch.

 | 
Tắt thông báo, giữ nguyên màn hình hiện tại

• Focus vào ô nhập thông tin người hưởng | 

 | 2 | 
Không nhập trường bắt buộc
 | 
{Trường bắt buộc không được bỏ trống}. Quý khách vui lòng kiểm tra lại!
 | 

 | 

• Nếu hợp lệ: Gửi yêu cầu khởi tạo đặt lịch theo dịch vụ tương ứng 
 | 
 | MB Server | 
1/ Kiểm tra lại Số lần giao dịch tối đa theo từng loại tần suất đã cấu hình tại BE 

2/ Gửi yêu cần truy vấn số tài khoản sang HT Bank (API: queryCustomerByAcc). Nếu STK không hợp lệ, trả lỗi "Tài khoản thụ hưởng không hợp lệ. Quý khách vui lòng kiểm tra lại"

3/ STK hợp lệ. Kiểm tra Hạn mức/ phí/PTXT/ Số dư khả dụng như sau
 | | 
STT
 | 
Loại hạn mức/ phí giao dịch
 | 
Yêu cầu

 | 1 | Số dư khả dụng | Không kiểm tra
 | 2 | Hạn mức tối thiểu/ Giao dịch | Có kiểm tra theo quy tắc hiện tại
 | 3 | Hạn mức tối đa/ Giao dịch | Có kiểm tra theo quy tắc hiện tại
 | 4 | Hạn mức về số lần giao dịch/ ngày | Có kiểm tra theo quy tắc hiện tại
 | 5 | Hạn mức theo nhóm chuyển tiền/ ngày (Cài đặt trên App) | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 6 | 
Phí giao dịch 
 | Không kiểm tra
 | 7 | Hạn mức theo nhóm dịch vụ 630/ngày | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 8 | Phương thức xác thực | PTXT dựa theo số tiền đã nhập tại trường Số tiền theo quy tắc hiện tại 

4/ Server tính lại Ngày kết thúc theo công thức đã mô tả tại 

5/Trả kết quả cho MB Client bao gồm toàn bộ thông tin tại MH xác nhận

 | 
 | MB Client | 
Nhận kết quả phản hồi từ MB server :

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng. Đóng thông báo, giữ nguyên màn hình hiện tại. <Tham khảo bảng thông báo lỗi cấu hình tại server>
• Hợp lệ: Chuyển sang màn hình Xác nhận giao dịch với thông tin server trả (Thời gian đặt lịch, Tài khoản nguồn, Số tiền, Tần suất, Số lần giao dịch, Ngày bắt đầu, Ngày kết thúc, PTXT ...)

### 3/ Xác nhận giao dịch

##### Màn hình xác nhận giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Xác nhận"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

Lưu ý: Đặt lịch chuyển tiền nội bộ cùng chủ không có chọn PTXT và xác thực

### 4/ Xác thực giao dịch
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập thông tin xác thực và nhấn "Tiếp tục"

 | MB Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang MB Server
 | MB Server | 
1/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

2/ Gửi yêu cầu Tạo lệnh đặt lịch chuyển tiền sang Bank Server (API:  createScheduleFundsTransfer)

Input: 
 | 
 | 
 | Mô tả | Ghi chú
 | 1 | 
referenceNo
 | Mã giao dịch do MB server sinh | 

 | 2 | 
mobileNo
 | Số điện thoại đăng nhập MB | 

 | 3 | 
accountNo
 | Số tài khoản nguồn KH đã chọn | 

 | 4 | 
toAccount
 | Số tài khoản thụ hưởng KH đã nhập | 

 | 5 | 
amount
 | 
Số tiền giao dịch 
 | 

 | 6 | 
noofSchedule
 | 
Số lần giao dịch KH đã nhập
 | 
• Nếu Tần suất = Không lặp lại, truyền noofSchedule = 1
 | 7 | 
frequency
 | 
Tần suất chuyển
 | 
• Nếu Tần suất = Không lặp lại, truyền frequency= 1D
• Tần suất = Hàng ngày→ Truyền 1D
• Tần suất = 2 ngày/ lần → Truyền 2D
• Tần suất = Hàng tuần → Truyền 7D
• Tần suất = Hàng tháng → Truyền 1M
• Tần suất = 2 tháng/ lần → Truyền 2M
• Tần suất = Hàng quý → Truyền 1Q
• Tần suất= Hàng năm → Truyền 1Y
• ...
 | 8 | 
schStartDate
 | 
Ngày bắt đầu chuyển tiền
 | 

 | 9 | 
schEndDate
 | 
Ngày kết thúc chuyển tiền
 | 
• Nếu tần suất = Không lặp lại, truyền Ngày kết thúc = Ngày bắt đầu
 | 10 | 
createdDate
 | 
Ngày tạo lịch chuyển tiền
 | 

 | 11 | 
remark
 | 
Nội dung chuyển tiền
 | 

 | 12 | 
type
 | 
Loại chuyển tiền
 | 
0: Cùng chủ

1: Khác chủ

3/ MB Server lưu toàn bộ dữ liệu trên (mục đích để lấy báo cáo BE)

 | HT Bank | 
1/ Ghi nhận lệnh đặt tiền trên hệ thống của Bank (Chưa hạch toán trừ tiền KH)

2/ Phản hồi lại kết quả cho MB Server

 | MB server | 
Nhận, kiểm tra kết quả:

• Thành công: Cập nhật trạng thái giao dịch thành công, lưu lại mã giao dịch đặt lịch của KH
• Không thành công: Cập nhật trạng thái giao dịch thất bại và phản hồi mã lỗi về cho Client
• Time-out: Cập nhật trạng thái time-out và phàn hồi về cho Client
 | MB Client | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng (mã lỗi do bank trả về)
• Thành công: Chuyển sang màn hình kết quả giao dịch

### 5/ Kết quả
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình Home như đã mô tả

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút Tạo giao dịch mới
 | 
Client MB
 | 
Trở lại màn hình khởi tạo giao dịch chuyển tiền nội bộ khác chủ/ cùng chủ tương ứng

---

#### 16.8.3. Danh sách đặt lịch chuyển tiền

> **Page ID:** `206178722` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/206178722

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

##### 16.8.3.1. Flow & Action screen_Danh sách đặt lịch

> **Page ID:** `206831886` · **Version:** 18
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/206831886

Mục lục
none

### 1/ Danh sách màn hình

##### <MH1 Truy cập chức năng>

##### <MH2.1 Truy cập chức năng> Nếu chưa có GD hoạt động nào

##### <MH2.2 Truy cập chức năng> Nếu có GD trạng thái Hoạt động

##### <MH2.3 Bộ lọc>

##### <MH3.1: Chi tiết giao dịch đặt lịch chuyển tiền>

##### <MH3.2: Poup Giao dịch đã thực hiện>

##### 

##### <MH 5.1 Xác nhận Tạm dừng lệnh

##### <MH 5.2 Xác nhận Tiếp tục lệnh>

##### <MH 5.3 Xác nhận hủy lệnh>

##### 

### 3/ Mô tả màn hình

##### <MH 1 Truy cập chức năng>  

Tại màn hình chuyển tiền chung, bổ sung icon chức năng "Danh sách đặt lịch chuyển tiền"

##### <MH2: Danh sách đặt lịch chuyển tiền>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Back về MH trước đó

 | 
2
 | 
Tiêu đề 
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Danh sách đặt lịch chuyển tiền

 | 
3
 | 
Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Home quay về trang chủ

 | 

 | 
Mỗi giao dịch đặt lịch bao gồm các thông tin sau

 | 
4
 | 
Tên người hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường toAccountName

 | 
5
 | 
Tần suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường  "frequency"

Client thực hiện quy đổi hiển thị như sau

• frequency = xD, xM, xQ, xY → Hiển thị "x ngày/ lần", "x tháng/ lần", "x quý/ lần", "x năm/lần"
• (frequency = 1 và noofSchedule = 1) → Hiển thị Không lặp lại
 | 
6
 | 
Ngày thực hiện tiếp theo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường "nextSchDueDate" (Nếu có)

 | 
7
 | 
Trạng thái đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bao gồm các giá trị:

• Hoạt động: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus (Chữ màu xanh) (mặc định chỉ hiển thị Hoạt động)
• Tạm dừng: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus (Chữ màu cam)
• Hủy: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus (Chữ màu đỏ)
• 
Hết hạn: Hiển thị Hết hạn nếu dữ liệu do Bank trả về tại trường schEndDate < ngày hiện tại (Chữ màu xanh lá)

 | 
8
 | 
Số tiền giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường "amount"

 | 
9
 | 
Nếu không có giao dịch Hoạt động nào
 | 
--
 | 
--
 | 
--
 | 
--
 | 
Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc truy vấn các giao dịch đặt lịch chuyển tiền có trạng thái khác

 | 

 | 
Bộ lọc. Click vào icon Bộ lọc mở ra các thông tin sau

 | 
10
 | Loại tìm kiếm | Radio Button | Select | -- | -- | 
Bao gồm 2 giá trị:

• Theo trạng thái lệnh (Mặc định)
• Theo thời gian
 | 
11
 | 
Loại chuyển tiền
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn 1 trong các giá trị:

• Tất cả (Mặc định)
• Chuyển tiền định kỳ nội bộ khác chủ
• Chuyển tiền định kỳ nội bộ cùng chủ
 | 
12
 | 
Trạng thái lệnh
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Chỉ hiển thị khi loại tìm kiếm là "Theo trạng thái lệnh"

Cho phép chọn 1 trong các giá trị:

• Tất cả 
• Hoạt động (Mặc định)
• Tạm dừng
• Hủy
• Hết hạn
 | 
13
 | 
Từ ngày
 | 
Calendar
 | 
Textbox
 | 
--
 | 
--
 | 
Chỉ hiển thị khi loại tìm kiếm là "Theo thời gian"

• Là ngày thực hiện lệnh tiếp theo (theo dữ liệu ngày bank trả)
• Mặc định: Ngày hiện tại, không cho chọn ngày quá khứ
• Từ ngày phải nhỏ hơn hoặc bằng Đến ngày
• Định dạng dd/MM/yyyy
 | 
14
 | 
Đến ngày
 | 
Calendar
 | 
Textbox
 | 
--
 | 
--
 | 
Chỉ hiển thị khi loại tìm kiếm là "Theo thời gian"

• Là ngày thực hiện lệnh tiếp theo (theo dữ liệu ngày bank trả)
• Mặc định: Ngày hiện tại, không cho chọn ngày quá khứ
• Từ ngày phải nhỏ hơn hoặc bằng Đến ngày
• Định dạng dd/MM/yyyy
 | 
15
 | Ghi chú | Label | ReadOnly | -- | -- | 
Chỉ hiển thị ghi chú khi loại tìm kiếm = Theo thời gian

Truy vấn các lệnh đặt lịch chuyển tiền có Ngày hiệu lực tiếp theo trong khoảng thời gian tìm kiếm

 | 
16
 | 
Tìm kiếm
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Thực hiện tìm kiếm theo các tiêu chí đã chọn <Tham khảo logic xử lý>

 | 
17
 | 
Sắp xếp thứ tự hiển thị danh sách lệnh
 | 

 | 

 | 

 | 

 | 
• Ở MH mặc định khi bắt đầu vào chức năng Danh sách đặt lịch chuyển tiền (Chỉ hiển thị các lệnh có trạng thái Hoạt động) → Sắp xếp theo ngày thực hiện tiếp theo mới nhất lên đầu danh sách. Do Bank không trả định dạng giờ trong trường "nextSchDueDate" nên nếu các lệnh có cùng ngày nextSchDueDate thì sẽ kiểm tra thêm trường "CreateDate" mới nhất lên đầu danh sách   → Client lọc

• Ở MH danh sách kết quả lọc theo tiêu chí ngày -->Sắp xếp theo ngày thực hiện tiếp theo mới nhất lên đầu danh sách
Do Bank không trả định dạng giờ trong trường "nextSchDueDate" nên nếu các lệnh có cùng ngày nextSchDueDate thì sẽ kiểm tra thêm trường "CreateDate" mới nhất lên đầu danh sách   → Client lọc

( Các lệnh đã hủy, đã hết hạn sẽ không hiển thị) → Client lọc

• Ở MH danh sách kết quả lọc theo tiêu chí trạng thái lệnh → Sắp xếp theo ngày tạo lệnh mới nhất lên đầu (Các lệnh đã hủy, đã hết hạn có hiển thị)→ Client lọc
 | 

 | 
Click vào mỗi dòng giao dịch hiển thị màn hình Chi tiết giao dịch chuyển tiền như mô tả dưới đây

##### MH3: <Chi tiết giao dịch đặt lịch chuyển tiền>
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Chi tiết giao dịch đặt lịch chuyển tiền

 | 
3
 | 
Back
 | 

 | 

 | 

 | 

 | 
• Nếu KH trước đó ko thực hiện filter → Back về MH danh sách mặc định  gồm trạng thái Hoạt động
• Nếu KH trước đó có filter → Back về MH danh sách kết quả filter trước đó
 | 
4
 | 
Ngày đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do Bank trả về trong API  queryScheduleAccount

Trường createdDate

Hiển thị định dạng dd/mm/yyyy

 | 
5
 | 
Trạng thái đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bao gồm các giá trị:

• Hoạt động: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus,
• Tạm dừng: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus,
• Hủy: Hiển thị tương ứng dữ liệu do bank trả về  tại trường schStatus,
• 
Hết hạn: Hiển thị Hết hạn nếu dữ liệu do Bank trả về tại trường schEndDate < ngày hiện tại

 | 
6
 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
accountNo

 | 
7
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
toAccount

 | 
8
 | 
Tên người thụ hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
toAccountName

 | 
9
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường "amount"

 | 
10
 | 
Ngày thực hiện tiếp theo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường "nextSchDueDate"

Nếu trạng thái = Hủy và Đã hết hạn → Ẩn trường Ngày thực hiện tiếp theo

 | 
11
 | 
Loại chuyển tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
type

0: cùng chủ
1: khác chủ

 | 
12
 | 
Tần suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Dữ liệu do bank trả về trường  "frequency"

Client thực hiện quy đổi hiển thị như sau

• frequency = xD, xM, xQ, xY → Hiển thị "x ngày/ lần", "x tháng/ lần", "x quý/ lần", "x năm/lần"
• frequency = 1 và noofSchedule = 1 → Hiển thị Không lặp lại
 | 
13
 | 
Số lần giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
noofSchedule

 | 
14
 | 
Ngày bắt đầu
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
schStartDate

 | 
15
 | 
Ngày kết thúc
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
schEndDate

 | 
16
 | 
Nội dung giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
remark

 | 
17
 | 
Mã đặt lịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
referenceNo

 | 
18
 | 
Danh sách giao dịch
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Click Xem các giao dịch đã thực hiện, mở đến Popup Giao dịch đã thực hiện

Dữ liệu do Bank trả về (Trong tài liệu API Table A.10) (Popup này sẽ hiển thị các giao dịch chuyển tiền đã được thực hiện trên hệ thống Bank), gồm:

• 
Ngày thực hiện : 

- Trạng thái Bank trả là: Không thành công/ Thành công  → map API:  realDate 

- Trạng thái Bank trả là: Chưa thực thi/ Tạm dừng → map API : schDate

• 
Trạng thái chuyển tiền: schStatus

S: Thành công
F: Không thành công
N: Chưa thực thi
P: Tạm dừng

      C: Hủy

• 
Mã giao dịch: transRefNo (Nếu Bank trả  = 0 hoặc NULL thì không hiển thị trường này)

• Phí giao dịch và thuế: Giá trị tổng của trường fee+VAT (Nếu Bank trả  = 0 hoặc NULL thì không hiển thị trường này)
 | 

 | 
Các chức năng:

• Tạm dừng
• Tiếp tục
• Hủy | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị các button chức năng tương ứng với trạng thái đặt lệnh

• Trạng thái "Hoạt động": Hiển thị button "Tạm dừng", "Hủy lệnh"
• Trạng thái  "Tạm dừng: Hiển thị button "Tiếp tục", "Hủy lệnh"
• Trạng thái "Hủy": Không hiển thị icon các chức năng trên
• 
Trạng thái "Hết hạn: Không hiển thị icon các chức năng trên

Click vào chức năng "Tạm dừng" , "Tiếp tục", "Hủy lệnh" < Tham khảo logic xử lý>

##### MH 4,5: <Xác nhận Hủy/ Tạm dừng/ Tiếp tục>

<Tham khảo logic xử lý>

---

##### 16.8.3.2. Detail Logic Flow Danh sách đặt lịch

> **Page ID:** `206833471` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/206833471

Mục lục
none

### 1/ Truy cập chức năng
 | Tác nhân | Mô tả
 | 
KH chọn chức năng "Danh sách đặt lịch chuyển tiền"

 | MB Client | 
Gửi yêu cầu lấy danh sách đặt lịch chuyển tiền đến MB Server

 | MB Server | 
Gửi yêu cầu lấy danh sách đặt lịch sang Bank ( API:  queryScheduleAccount)

Input:

• Số điện thoại
 | HT Bank | 
Trả kết quả 

 | MB Server | 
Nhận kết quả và trả kết quả về cho Client

• Thành công:
- Trả danh sách đặt lịch của các lệnh có  tiêu chí: Trạng thái = Hoạt động, Loại giao dịch: Tất cả cho Client hiển thị 

• Không thành công/ Timeout: Phản hồi mã lỗi về cho Client
 | MB Client | 
Nhận kết quả danh sách đặt lịch do Server trả

 | 
KH chọn lại bộ lọc tìm kiếm

 | MB Client | 
1/ Chọn tiêu chí lọc

2/ Bấm tìm kiếm → Gửi yêu cầu lấy danh sách đặt lịch tới MB server theo tiêu chí đã chọn tại bộ lọc

Input:

• Kiểu tìm kiếm (Gồm 1 trong 2 giá trị :Theo trạng thái lệnh/ Theo thời gian)
• Loại chuyển tiền
• Trạng thái lệnh (Chỉ bắt buộc với kiểu tìm kiếm: Theo trạng thái lệnh)
• Thời gian... Từ ngày ... Đến ngày (Chỉ bắt buộc với kiểu tìm kiếm là Theo thời gian)
 | MB Server | 
Gửi yêu cầu lấy danh sách đặt lịch sang Bank ( API:  queryScheduleAccount)

Input:

• Số điện thoại
 | HT Bank | 
Trả kết quả 

 | MB Server | 
Nhận kết quả và trả kết quả về cho Client

• Thành công:
- Trả danh sách đặt lịch của các lệnh có tiêu chí đã chọn tại Client

• Không thành công/ Timeout: Phản hồi mã lỗi về cho Client
 | MB Client | 
Hiển thị MH danh sách đặt lịch, bao gồm các lệnh theo tiêu chí server đã trả

### 2/ MH danh sách đặt lịch
 | Tác nhân | Mô tả
 | 
KH bấm vào vùng thông tin của 1 bản ghi bất kỳ

 | MB Client | 
Gửi yêu cầu lấy chi tiết của bản ghi đó

 | MB Server | 
Gửi yêu cầu lấy chi tiết đặt lịch của bản ghi đó sang HT Bank ( API:  queryScheduleAccountSum)

Input:

• Mã đặt lệnh
• Số điện thoại
 | HT Bank | 
Trả kết quả chi tiết lệnh chuyển tiền , kèm listschedule (danh sách các giao dịch chuyển tiền đã thực hiện tại Core Bank- nếu có)

 | MB Server | 
Nhận kết quả và trả kết quả về cho Client

• Thành công: Trả kết quả  gồm:
- Chi tiết của bản ghi, kèm listschedule (danh sách các giao dịch chuyển tiền đã thực hiện tại Core Bank- nếu có)

- Nếu dữ liệu do Bank trả về tại trường schEndDate < ngày hiện tại → Trả KQ trạng thái lệnh cho Client: Đã hết hạn (Các trạng thái khác lấy theo Bank trả)

• Không thành công/ Timeout: Phản hồi mã lỗi về cho Client
 | MB Client | 
Hiển thị MH chi tiết giao dịch đặt lịch chuyển tiền như đã mô tả

 | 
KH bấm vào Xem các giao dịch đã thực hiện

 | MB Client | 
Hiển thị listschedule (danh sách các giao dịch chuyển tiền đã thực hiện tại Core Bank- nếu có) như đã mô tả

### 3/ MH Chi tiết đặt lịch -->Cập nhật trạng thái đặt lịch
 | 
KH click vào icon tác vụ

 | MB App | 
Gửi yêu cầu kiểm tra giờ KH đang thực hiện với giờ chạy Batch đang cấu hình ở BE (Mid 467)

 | MB Server | 
Kiểm tra và trả kết quả (Giờ chạy batch được cấu hình tại tham số TIME_BATCH_TRANSFER, định dạng hh:mm- hh:mm)

 | MB App | 
1/ Nhận kết quả kiểm tra giờ chạy Batch

• Không hợp lệ | 
 | Trường hợp | Mô tả | Xử lý
 | 1 | 
Nếu thời gian đang thực hiện trong khoảng thời gian cấu hình chạy batch 
 | 
• Hiển thị thông báo "Hệ thống đang trong thời gian xử lý dữ liệu, quý khách vui lòng quay lại sau hh:mm (hh:mm -  là thời gian cuối của khoảng thời gian cấu hình) | 
Đóng Popup giữ nguyên màn hình chi tiết đặt lịch

• Hợp lệ: Nếu thời gian KH thực hiện thay đổi trạng thái lệnh ngoài khoảng thời gian cấu hình chạy Batch → Chuyển bước 2
2/ Hiển thị Popup chức năng Tạm dừng/ Tiếp tục/ Hủy lệnh tương ứng với trạng thái đặt lịch như đã mô tả
 | 
 | Trường hợp | Mô tả | Xử lý
 | 1 | 
Click vào chức năng "Tạm dừng"
 | 
Hiển thị thông báo Quý khách có muốn Tạm dừng giao dịch đặt lịch chuyển tiền không? 
 | 
Và 2 lựa chọn

• Hủy: Đóng Popup giữ nguyên màn hình
• Đồng ý: Gửi yêu cầu xác thực tạm dừng giao dịch đặt lịch sang MB Server
 | 2 | Click vào chức năng "Tiếp tục" | Hiển thị thông báo "Quý khách có muốn Tiếp tục giao dịch đặt lịch chuyển tiền không? | 
Và 2 lựa chọn

• Hủy: Đóng Popup giữ nguyên màn hình
• Đồng ý: Gửi yêu cầu xác thực tiếp tục giao dịch đặt lịch sang MB Server
 | 3 | Click vào chức năng "Hủy lệnh" | Hiển thị thông báo "Quý khách có chắc chắn muốn hủy giao dịch đặt lịch này? Việc hủy sẽ không thể hoàn tác" | 
Và 2 lựa chọn

• Hủy: Đóng Popup giữ nguyên màn hình
• Đồng ý: Gửi yêu cầu xác thực Hủy lệnh giao dịch đặt lịch sang MB Server

 | MB Server | 
MB Server thực hiện kiểm tra và lấy ra PTXT của loại giao dịch Phi tài chính theo quy tắc chung (Chỉ bao gồm PTXT Soft OTP hoặc SMS) và trả kết quả cho MB Client

Tham khảo tại 

 | MB Client | 
Hiển thị 1 PTXT do Server trả

Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | MB Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu Tạm dừng/ Tiếp tục/ Hủy lệnh sang HT MB server
Input:

• Mã đặt lệnh
• SĐT
• Trạng thái cần cập nhật
- Tạm dừng: 0

- Tiếp tục: 1

- Hủy đặt lịch: 2

 | MB Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Gửi yêu cầu Tạm dừng/ Tiếp tục/ Hủy lệnh sang HT Bank

Input:

• Mã đặt lệnh
• SĐT
• Trạng thái cần cập nhật
- Tạm dừng: 0

- Tiếp tục: 1

- Hủy đặt lịch: 2

 | HT Bank | Xử lý cập nhật lệnh chuyển tiền và trả kết quả cho MB server
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Trả kết quả thành công cho Client
• Không thành công: Trả về thông báo lỗi cho Client
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị thông báo tương ứng 
• Tạm dừng đặt lịch chuyển tiền thành công. Để tiếp tục lại, quý khách vui lòng chọn Tiếp tục tại "Danh sách đặt lịch chuyển tiền"
• Quý khách đã Tiếp tục lại lệnh đặt lịch chuyển tiền. Giao dịch sẽ được thực hiện theo thời gian quý khách đã tạo trước đó
• Quý khách đã Hủy giao dịch đặt lịch thành công
Đóng thông báo Gửi yêu cầu lấy chi tiết của bản ghi đó để cập nhật trạng thái mới nhất của lệnh

Xác thực bằng Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn "Xác nhận"
 | MB Client/MB Server/ Soft OTP | 
Tham khảo logic xử lý tại < Xác thực bằng Soft OTP>

Soft OTP Server trả kết quả xác thực cho MB Server → MB server trả kết quả xác thực cho MB Client

 | 
 | 

 | MB Server | 
Gửi yêu cầu Tạm dừng/ Tiếp tục/ Hủy lệnh sang HT Bank

Input:

• Mã đặt lệnh
• SĐT
• Trạng thái cần cập nhật
- Tạm dừng: 0

- Tiếp tục: 1

- Hủy đặt lịch: 2

 | 
 | 

 | HT Bank | Xử lý cập nhật lệnh chuyển tiền và trả kết quả cho MB server
 | 
 | 

 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Trả kết quả thành công cho Client
• Không thành công: Trả về thông báo lỗi cho Client
 | 
 | 

 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị thông báo tương ứng 
• Tạm dừng đặt lịch chuyển tiền thành công. Để tiếp tục lại, quý khách vui lòng chọn Tiếp tục tại "Danh sách đặt lịch chuyển tiền"
• Quý khách đã Tiếp tục lại lệnh đặt lịch chuyển tiền. Giao dịch sẽ được thực hiện theo thời gian quý khách đã tạo trước đó
• Quý khách đã Hủy giao dịch đặt lịch thành công

---


