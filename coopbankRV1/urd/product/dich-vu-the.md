# 📋 Dịch vụ thẻ

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 36. DỊCH VỤ THẺ

> **Page ID:** `766315098` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/766315098

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*11 trang con:*

### 36.1. SOW_Dịch vụ thẻ

> **Page ID:** `778241198` · **Version:** 42
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/778241198

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V0.0.1 | 

Mục lục

### 1/ Thông tin chung

• 
Tên dự án: Triển khai chức năng quản lý thẻ nội địa (debit + credit) trên app Co-opBank

• 
Loại dự án: Phát triển mới

• 
Thời gian thực hiện: 

### 2/ Mục đích

 Cung cấp cho khách hàng khả năng sử dụng các chức năng chính của thẻ nội địa (ghi nợ và tín dụng) thông qua Mobile Banking

### 3/ Phạm vi 
 | Phase | Nội dung
 | Phase 1: Chỉ làm thẻ Credit | 
• Dịch vụ thẻ
• Kích hoạt thẻ
• Cài đặt PIN thẻ
• Thông tin thẻ
• Sao kê
• Thanh toán thẻ tín dụng
• Lịch sử giao dịch

### 4/ Danh sách chức năng chi tiết 

#### 4.1/ Ma trận chức năng
 | 
 | 
 | 
Chờ kích hoạt

(trạng thái phát hành là

"Đã bàn giao cho khách hàng") 
 | Hoạt động | Khóa do khách hàng | Khóa bởi GDV
 | 
 | 
 | 
Thẻ chính
 | 
Thẻ phụ
 | 
Thẻ chính
 | 
Thẻ phụ
 | 
Thẻ chính
 | 
Thẻ phụ
 | 
Thẻ chính
 | 
Thẻ phụ

 | 1 | Kích hoạt thẻ | x | x | 
 | 
 | 
 | 
 | 
 | 

 | 2 | Cài đặt PIN thẻ | 
 | 
 | x | x | 
 | 
 | 
 | 

 | 3 | Thông tin thẻ | 
 | 
 | x | x | x | x | x | x
 | 4 | Sao kê | 
 | 
 | x | 
 | x | 
 | x | 

 | 5 | Thanh toán thẻ tín dụng | 
 | 
 | x | 
 | x | 
 | x | 

 | 6 | Lịch sử giao dịch | 
 | 
 | x | x | x | x | x | x

#### 4.2/ Danh sách chức năng

Business rule chung: 

• MB Server không lưu trữ các dữ liệu quan trọng của thẻ như số thẻ, số CVV, PIN,...
• MB Server được phép lưu trữ các dữ liệu để đảm bảo xử lý hiển thị dữ liệu ở các tính năng BO 

 | 
 | Chức năng | Mục đích | Loại thẻ | Loại tài liệu | Tác nhân | Luồng chính | API cần bank cung cấp | Business Rule | Assigne | Timeline
 | 1 | 
Dịch vụ thẻ
 | 
Hiển thị toàn bộ danh sách thẻ của khách hàng, bao gồm thẻ tín dụng và thẻ ghi nợ (giai đoạn này chỉ làm thẻ tín dụng). Đây là điểm truy cập chính để quản lý các thao tác liên quan đến từng thẻ
 | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn chức năng "Dịch vụ thẻ" → Mặc định chọn tab "Thẻ tín dụng"

2/ Hệ thống hiển thị danh sách thẻ tín dụng

• Nếu không có thẻ nào → Hiển thị thông báo "Quý khách chưa có thẻ tín dụng nội địa tại Co-opBank. Vui lòng mở thẻ để sử dụng." | 
• API Lấy danh sách thẻ | | 
 | Mã | Nội dung
 | 1 | BR1 | 
Danh sách thẻ hiển thị từ trước đến sau theo quy tắc kiểm tra: Trạng thái thẻ → Loại thẻ → Thời gian phát hành thẻ 

 | LinhTH | 
 

+ Gồm Bàn giao chức năng BO Quản lý phôi thẻ

 | 2 | 
Thông tin thẻ
 | Cung cấp cho khách hàng thông tin chi tiết của thẻ như số thẻ, ngày hiệu lực, trạng thái thẻ,.... | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn 1 thẻ từ danh sách

2/ Hệ thống hiển thị thông tin thẻ, có một số trường thông tin bị mask
 | 
• API Truy vấn thông tin chi tiết thẻ | | 
 | Mã | Nội dung
 | 1 | BR1 | 
Chỉ hiển thị chức năng Thông tin thẻ nếu thẻ có trạng thái:

• Chờ kích hoạt và trạng thái phát hành là Đã bàn giao cho khách hàng
• Hoạt động
• Khóa do khách hàng
• Khóa bởi GDV
 | 2 | BR2 | 
Hiển thị với cả thẻ chính và thẻ phụ

 | LinhTH | 
 

 | 3 | 
Kích hoạt thẻ
 | 
Cho phép khách hàng kích hoạt thẻ sau khi nhận thẻ vật lý. Thao tác này là bắt buộc trước khi sử dụng thẻ cho các giao dịch tài chính
 | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/  KH vào mục "Dịch vụ thẻ" → Chọn thẻ chưa kích hoạt 

2/ Chọn button "Kích hoạt thẻ" → Hệ thống hiển thị màn hình nhập 8 số cuối của thẻ

3/  KH nhập đúng 8 số cuối, nhấn "Xác nhận" 

4/ Hệ thống hiển thị popup  xác thực OTP theo thứ tự ưu tiên (Soft OTP, SMS OTP) 

5/ KH xác nhận OTP thành công → Hiển thị popup Kích hoạt thành công + button "Cài đặt PIN"

• KH chọn "Cài đặt PIN" → Chuyển sang màn hình đặt PIN 
• KH chọn "Bỏ qua" → Đóng popup, về màn hình Dịch vụ thẻ | 
• API Kích hoạt thẻ
• API cài đặt PIN thẻ | | 
 | Mã | Nội dung
 | 1 | BR1 | Chỉ hiển thị chức năng Kích hoạt thẻ nếu trạng thái thẻ là "Chờ kích hoạt" và trạng thái phát hành là "Đã bàn giao cho khách hàng"
 | 2 | BR2 | Hiển thị với cả thẻ chính và thẻ phụ
 | 3 | BR3 | PTXT theo thứ tự ưu tiên: Soft OTP → SMS OTP tùy theo PTXT KH cài đặt
 | HoaNK | 

 

 | 4 | 
Cài đặt PIN thẻ
 | Hỗ trợ khách hàng đặt mã PIN mới để sử dụng. Bao gồm đổi PIN để tăng bảo mật hoặc khôi phục PIN khi quên | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn thẻ Hoạt động 

2/ KH nhấn "Cài đặt PIN"

3/ Hệ thống hiển thị màn hình Cài đặt PIN 

4/ KH nhập PIN mới

5/ KH thực hiện xác nhận FacePay + SMSOTP/ Soft OTP thành công → Hiển thị popup thông báo thành công

6/ KH đóng thông báo, quay về mà hình Dịch vụ thẻ
 | 
• API cài đặt PIN thẻ | | 
 | Mã | Nội dung
 | 1 | BR1 | Chỉ hiển thị chức năng Cài đặt PIN thẻ với thẻ có trạng thái là Hoạt động
 | 2 | BR2 | 
Hiển thị với cả thẻ chính và thẻ phụ

 | 3 | BR3 | Không giới hạn số lần cài đặt lại số PIN trong ngày
 | 4 | BR4 | 
Mã PIN gồm 06 chữ số, phải thỏa mãn điều kiện:

• Không được là dãy số liên tiếp 
• Không được là dãy số giống nhau
 | 5 | BR5 | 
PTXT theo thứ tự ưu tiên: Soft OTP → SMS OTP tùy theo PTXT KH cài đặt + Kết hợp FacePay

 | HoaNK | 
  

 | 5 | 
Thanh toán thẻ tín dụng
 | Cho phép khách hàng thanh toán dư nợ thẻ tín dụng bằng cách trích tiền từ tài khoản thanh toán | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn thẻ Hoạt động/ Khóa

2/ KH chọn Thanh toán thẻ tín dụng

3/ Hệ thống hiển thị màn hình Thanh toán thẻ tín dụng

4/ KH nhập các thông tin → chọn Tiếp tục

5/ Hệ thống hiển thị màn hình xác nhận

6./ KH chọn Xác nhận

7/ Hệ thống hiển thị popup  xác thực OTP theo thứ tự ưu tiên (Soft OTP, SMS OTP) 

8/ KH xác nhận OTP thành công 

9/ Hệ thống hiển thị màn hình kết quả
 | 
• API thông tin thẻ (có trả thông tin dư nợ hiện tại, dư nội tối thiểu, toàn bộ dư nợ)
• API thanh toán dư nợ thẻ tín dụng | | 
 | Mã | Nội dung
 | 1 | BR1 | Chức năng Thanh toán thẻ tín dụng được thực hiện với thẻ có trạng thái Hoạt động, Khóa do khách hàng, Khóa bởi GDV
 | 2 | BR2 | Chỉ hiển thị với thẻ chính
 | 3 | BR3 | Khi thực hiện giao dịch, không check module 2345, không check hạn mức
 | 4 | BR4 | Chỉ được thanh toán cho chính chủ thẻ
 | 5 | BR5 | Cho phép thanh toán Dư nợ tối thiểu của kỳ sao kê hoặc Toàn bộ dư nợ của kỳ sao kê hoặc theo số tiền bất kỳ
 | 6 | BR6 | Cho phép thanh toán số tiền vượt quá dư nợ hiện tại, không vượt quá số dư tài khoản nguồn
 | 7 | BR7 | Không được dùng thấu chi để thanh toán thẻ tín dụng
 | 8 | BR8 | Không cho phép trả vượt dư nợ trên kênh mobile banking ( nhưng kênh khác vẫn có thể trả thừa)
 | Linh TH | 
 

 | 6 | 
Sao kê
 | 
Hiển thị danh sách chi tiết các giao dịch theo từng kỳ sao kê để khách hàng nắm bắt được tổng số tiền đã chi tiêu, quản lý tài chính và kiểm tra tính chính xác trước khi thanh toán dư nợ
 | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn thẻ Hoạt động/ Khóa

2/ KH chọn "Sao kê"

3/ Hệ thống hiển thị màn hình Sao kê

4/ KH chọn kỳ sao kê (theo tháng) và thực hiện Tìm kiếm

5/ KH chọn 1 kỳ sao kê → Hiển thị thông tin sao kê giao dịch dạng file PDF

Note: Mẫu file PDF đã thiết kế sẵn → Bank đẩy lên SFTP server → MB server vào lấy và trả cho Client hiển thị (Client không cần thiết kế lại mẫu) 
 | 
• API lấy danh sách kỳ sao kê
• API chi tiết giao dịch của kỳ sao kê
→ Bank chưa cung cấp API
 | | 
 | Mã | Nội dung
 | 1 | BR1 | Chức năng sao kê được thực hiện với thẻ có trạng thái Hoạt động, Khóa do khách hàng, Khóa bởi GDV
 | 2 | BR2 | Chỉ hiển thị với thẻ chính
 | 3 | BR3 | Hiển thị toàn bộ giao dịch trên Sao kê của cả thẻ chính và thẻ phụ
 | LinhTH | 
 

 | 7 | 
Lịch sử giao dịch
 | Hiển thị tất cả các giao dịch phát sinh, cho phép khách hàng theo dõi biến động thẻ chi tiết ngoài kỳ sao kê | Credit | 
RedThêm mới
 | 
MB Client 

MB Server

Bank
 | 
1/ KH chọn thẻ Hoạt động/ Khóa

2/ KH chọn Lịch sử giao dịch 

3/ Hệ thống hiển thị màn hình Lịch sử giao dịch

4/ KH thực hiện tra cứu giao dịch theo thời gian: 1 tháng, 2 tháng, 3 tháng hoặc theo khoảng thời gian tùy chọn 

5/ Hệ thống hiển thị danh sách giao dịch 

6/ KH nhấn vào 1 giao dịch 

7/ Hệ thống hiển thị màn hình chi tiết giao dịch

→ Tham khảo tài liệu Lịch sử giao dịch của Tài khoản Tại đây
 | 
• API lấy danh sách giao dịch phát sinh theo khoảng thời gian
• API lấy chi tiết giao dịch | | 
 | Mã | Nội dung
 | 1 | BR1 | Chức năng lịch sử giao dịch được thực hiện với thẻ có trạng thái Hoạt động, Khóa do khách hàng, Khóa bởi GDV
 | 2 | BR2 | 
Hiển thị với cả thẻ chính và thẻ phụ

 | 3 | BR3 | Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 01 năm
 | 4 | BR4 | Lãi thu trên tài khoản sẽ được đưa vào Lịch sử giao dịch của thẻ chính
 | 5 | BR5 | Phí thường niên và phí giao dịch tương ứng của Thẻ chính/Thẻ phụ sẽ được đưa vào Lịch sử giao dịch của thẻ đó
 | Đức TL | 
  

 | 8 | 
Báo cáo giao dịch trên app 
 | Bổ sung báo cáo giao dịch thanh toán thẻ tín dụng trên app | 
 | 
BlueCẬP NHẬT
 | 
MB App Client

MB App Server
 | 
Hiển thị báo cáo giao dịch thanh toán thẻ 
 | 
 | 
 | 
 
 | 

### 5/ Chức năng trên BO
 | 
 | Chức năng | Loại | Mô tả cơ bản | Assigne | Timeline
 | 1 | 
Quản lý phôi thẻ
 | 
RedThêm mới
 | 
Cấu hình các tham số cố định trển thẻ:

• Tên sản phẩm thẻ
• Mã BIN
• Ảnh thẻ... | 
LinhTH
 | 
 

 | 2 | Báo cáo Thanh toán thẻ tín dụng | 
RedThêm mới
 | 
Gồm các thông tin:

• STT
• Số tham chiếu
• Số CIF
• Tên khách hàng
• Tên đăng nhập
• Đơn vị đăng ký
• Đơn vị ghi nợ
• Tài khoản nguồn
• Số thẻ thụ hưởng
• Tên chủ thẻ
• Hình thức thanh toán
• Số tiền
• Phí giao dịch
• Thuế
• Mã lỗi
• Mô tả mã lỗi
• Mã giao dịch
• PTXT
• Thời gian giao dịch
• Gói dịch vụ
• Trạng thái | 
LinhTH
 | 
 

 | 3 | Báo cáo quản lý thẻ | 
RedThêm mới
 | 
Quản lý thông tin chi tiết của 2 giao dịch liên quan đến Thẻ do khách hàng thực hiện: Kích hoạt thẻ, Cài đặt mã PIN. Gồm các thông tin:

• STT
• Số tham chiếu
• Số CIF
• Tên khách hàng
• Tên đăng nhập
• Đơn vị đăng kí
• Số thẻ
• Dịch vụ
• Mã lỗi
• Mô tả mã lỗi
• PTXT
• Thời gian giao dịch
• Trạng thái | 
ĐứcTL
 | 
  

### 6/ Phạm vi ảnh hưởng
 | STT | Chức năng | Mô tả ảnh hưởng | Tham chiếu tài liệu
 | 1 | Tổng hợp giao dịch | Bổ sung dịch vụ 1311- Thanh toán dư nợ thẻ tín dụng  | 
 | 2 | Chi tiêt giao dịch | Bổ sung dịch vụ 1311 - Thanh toán dư nợ thẻ tín dụng | 
 | 3 | Lịch sử giao dịch  | Bổ sung dịch vụ 1311 - Thanh toán dư nợ thẻ tín dụng | 

 | 4 | Dịch vụ  | Bổ sung khai báo dịch vụ Thẻ bao gồm: cài đặt mã pin, thanh toán dư nợ thẻ tín dụng | 

### 7 Q&A

Link Q&A: https://docs.google.com/spreadsheets/d/1qO6NySRG0WQEkjsBh1AB11zipwaLAB7cc-V7TfDs5TE/edit?gid=211508683#gid=211508683

---

### 36.2. 1. Danh sách thẻ

> **Page ID:** `891585026` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/891585026

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.2.1. Flow&Action screen - Danh sách thẻ

> **Page ID:** `896732240` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/896732240

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A |   | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Tạo mới tài liệu
 | V1 | 

Muc lục
none

### 1/ Danh sách màn hình

Dưới đây là màn hình Danh sách thẻ được chia theo từng trường hợp 

##### MH1.1: <Danh sách thẻ - Thẻ chính hoạt động >

##### MH1.2: <Danh sách thẻ - Thẻ chính chờ kích hoạt>

##### MH1.3: <Danh sách thẻ - Thẻ chính khóa do GDV>

##### MH1.4: <Danh sách thẻ - Thẻ chính khóa do khách hàng>

##### MH1.5: <Danh sách thẻ - Thẻ phụ>

##### MH1.6: <Danh sách thẻ - Chưa có thẻ >

### 2/ Mô tả màn hình

##### MH1: <Danh sách thẻ>
 | TT | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nút quay lại | Icon Button | Nhấn | Không | N/A | Điều hướng quay về màn hình trước đó.

 | 2 | Dịch vụ thẻ  | Label | N/A | N/A | N/A | 
Tiêu đề màn hình 

 | 3 | Tab Thẻ tín dụng | Tab | Chọn | Có | N/A | 
• Tab thẻ tín dụng được hiển thị mặc định 
• Hiển thị số lượng thẻ tín dụng (Bao gồm thẻ chính + thẻ phụ)
• Trường hợp khách hàng không có thẻ tín dụng: Hiển thị thông bão "Quý khách chưa có thẻ tín dụng tại Co-opBank. Vui lòng mở thẻ để sử dụng
• Trường hợp khách hàng có thẻ tín dụng, hiển thị danh sách thẻ tín dụng của khác hàng theo quy tắc được mô tả trong tài liệu 
 | 4 | Tab Thẻ ghi nợ | Tab | Chọn | Có | N/A | 
Giai đoạn này không hiển thị tab thẻ ghi nợ (đẩy sang giai đoạn sau xử lý)

 | 5 | Thẻ hiển thị thông tin thẻ | Image | Chọn  | Không | N/A | 
• Khách hàng chạm vào mũi tên để chuyển sang thẻ khác
• Cho phép khách hàng xem lần lượt từng thẻ từ đầu đến cuối (không xoay vòng)
• Hình ảnh phôi thẻ được cấu hình ở tính năng 
 | 
Cụm danh sách tính năng (Hiển thị tương ứng với từng thẻ, tham chiếu logic hiển thị tính năng trong tài liệu )

 | 6 | Sao kê | Icon Button | Nhấn | Không | N/A | 
Điều hướng tới màn hình sao kê thẻ tín dụng.

 | 7 | Thanh toán thẻ tín dụng | Icon Button | Nhấn | Không | N/A | Điều hướng tới chức năng thanh toán dư nợ thẻ tín dụng.
 | 8 | Lịch sử giao dịch | Icon Button | Nhấn | Không | N/A | Điều hướng đến màn hình lịch sử giao dịch 
 | 9 | Cài đặt PIN thẻ | Icon Button | Nhấn | Không | N/A | Điều hướng đến màn hình cài đặt PIN thẻ 
 | Cụm thông tin chung 
 | 
 | 
Số thẻ masked

cardNo
 | Text | Không thao tác | Có | N/A | Masked theo quy tắc: Hiển thị 6 số đầu và 4 số cuối, mask các số ở giữa 
 | 
 | 
Icon eye
 | Button | Nhấn | N/A | N/A | 
Bấm vào icon eye → điều hướng khách hàng đi xác thực 

Tham chiếu logic xử lý: 

 | 
 | 
Tên chủ thẻ 
cardName | Text | Không thao tác | Có | N/A | Tên chủ thẻ 
 | 11 | 
Loại thẻ

cardType
 | Text | Không thao tác | Có | N/A | 
Gồm 2 loại:

• Thẻ chính
• Thẻ phụ
 | 12 | 
Hạn mức khả dụng 

availAmount
 | Text | Không thao tác | Có | N/A | 
• Hiển thị hạn mức khả dụng của thẻ 
• Số tiền masked
• Định dạng tiền tệ VND.
• Icon eye cạnh số tiền masked. Bấm vào icon eyes → Hiển thị số tiền full 
 | 13 | 
Trạng thái

cardStatus
 | Label | Không thao tác | Có | N/A | 
Hiển thị trạng thái thẻ, bao gồm: 

• Chờ kích hoạt: Màu đen 
• Khóa do khách hàng: Màu đỏ
• Khóa do giao dịch viên: Màu đỏ
• Hoạt động: Màu xanh lá 
 | 14 | Nút Chi tiết thẻ  | Button | Nhấn | Không | N/A | Điều hướng tới màn hình chi tiết thẻ 
 | Pop-up Hiển thị thông tin thẻ
 | 
 | 
Số thẻ full
 | Text | Không thao tác | Có | N/A | Hiển thị số thẻ full của khách hàng 
 | 
 | 
Nút copy
 | Button | Nhấn | Không | N/A | Cho phép KH copy số thẻ 
 | 
 |  Tên chủ thẻ | Text | Không thao tác | Có | N/A | Hiển thị tên chủ thẻ 
 | 
 |  Ngày phát hành  | Text | Không thao tác | Có | N/A | Hiển thị ngày phát hành 
 | 
 | Ngày hết hạn  | Text | Không thao tác | Có | N/A | Hiển thị ngày hết hạn

---

#### 36.2.2. User Action Flow - Danh sách thẻ

> **Page ID:** `895173942` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/895173942

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A |   | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Tạo mới tài liệu 
 | V1 | 

Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Danh sách thẻ 
 | Use Case ID | UC_CardList
 | Use Case Description | 
Là người dùng, tôi muốn xem danh sách thẻ tín dụng, thẻ ghi nợ, thẻ kép mà tôi đã phát hành tại ngân hàng Coopbank 

Lưu ý: Ở giai đoạn 1 chỉ hiển thị danh sách thẻ tín dụng, không xử lý phạm vi thẻ ghi nợ và thẻ kép 

 | Actor | 
Khách hàng, MB App Client, MB App Server, Bank Server 

 | Priority | High
 | Trigger | 
Khách hàng truy cập vào dịch vụ thẻ trên màn hình Home 

 | 
Pre-Condition
 | 
• Khách hàng đã phát hành thẻ tín dụng, thẻ ghi nợ hoặc thẻ kép tại ngân hàng Coopbank 
• Khách hàng đăng nhập Coop-bank Mobile Banking thành công 
1. KH đăng nhập thành công ứng dụng; 2. KH có tài khoản nguồn hợp lệ để thực hiện giao dịch; 3. Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch

 | Post-Condition | 
• Khách hàng xem danh sách thẻ thành công
• Danh sách thẻ hiển thị đầy đủ các thẻ mà khách hàng đã phát hành 
• Danh sách thẻ hiển thị các tính năng tương ứng với từng loại thẻ 
1. KH thực hiện lệnh chuyển tiền nội bộ thành công; 2. Tài khoản nguồn của KH bị trừ số tiền giao dịch (bao gồm phí nếu có); 3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng (trừ phí nếu có); 4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]; 5. Hệ thống MB ghi nhận giao dịch chuyển tiền nội bộ vào [Transaction History]

 | Basic Flow | 
• Khách hàng truy cập Dịch vụ thẻ trên màn hình home 
• Hệ thống thực hiện truy vấn và hiển thị danh sách thẻ 
 | Alternative Flow | 
--

 | Exception Flow | 
• Khách hàng không có thẻ tồn tại trên hệ thống → Thông báo lỗi: "Quý khách chưa có thẻ tín dụng nội địa tại Co-opBank. Vui lòng mở thẻ để sử dụng"
• Lỗi khi truy vấn danh sách thẻ → Thông báo lỗi: "Lỗi hệ thống. Quý khách vui lòng truy cập lại dịch vụ thẻ" 
 | Bussiness Rules | 
• BR-01: Danh sách thẻ hiển thị từ trước đến sau theo quy tắc kiểm tra: Trạng thái thẻ → Loại thẻ → Thời gian phát hành thẻ 
• BR-02: Thẻ kép được hiển thị ở cả tab thẻ tín dụng và thẻ ghi nợ. Khi thẻ kép hiển thị ở tab nào thì sẽ hiển thị tương ứng các tính năng của thẻ tín dụng/ thẻ ghi nợ ở tab đó (Giai đoạn 1 chưa làm phần thẻ kép → Check lại khi làm sang giai đoạn sau)
• BR-03: Hiển thị số thẻ theo quy tắc 6 số đầu, 4 số cuối và mask các số ở giữa 
• BR-04: Hiển thị các tính năng tương ứng của từng thẻ dựa vào trạng thái thẻ và loại thẻ 
 | Non-Funtional Requiremnt | 
--

### 1/ Luồng xử lý

##### Truy cập chức năng
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
Truy cập dịch vụ thẻ tại màn hình Home

 
 | Khách hàng  | 
Khách hàng truy cập dịch vụ thẻ tại màn hình Home 

 | 

 | Mobile App | 
Gửi yêu cầu lấy danh sách thẻ đến Bank Server API queryCardSum (Tổng hợp thẻ)
Mô tả API | Trường dữ liệu | Mô tả | Sample
 | Request 
 | systemID | - | {
  "systemID": "VNPAY",
  “requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144"  
}
 | requestId | -
 | cifNo | CIFNo của khách hàng, được trả về sau khi đăng nhập thành công 
 | Response
 | requestId | - | 
{

  "requestId": "xxxx",

  "referenceID": "xxx",

  "cifNo": "0100000000144",

  

  "subcard": [

    {

      "cardNo": "970446xxxx7899",

      "cardId": "xxx",

  "cardStatus": "A",

  "cardName": "NGUYENVAN B",

  "cardType": "MainCard",

  "issueDate": "31/01/2025",

  "expireDate": "31/12/2025",

  "product": "Debit"

    },

 {

      "cardNo": "70446xxxx7891",

      "cardId": "xxx",

  "cardStatus": "A",

  "cardName": "NGUYENVAN B",

  "cardType": "MainCard",

  "issueDate": "31/01/2025",

  "expireDate": "31/12/2025",

  "product": "Credit"

    },

 {

"cardNo": "70446xxxx7892",

      "cardId": "xxx",

  "cardStatus": "A",

  "cardName": "NGUYENVAN B",

  "cardType": "SubCard",

  "issueDate": "31/01/2025",

  "expireDate": "31/12/2025",

  "product": "Debit"

    }

  ],

  "resCode": "000",

  "resDesc": "Success"

}

 | referenceID | -
 | cifNo | CIFNo của khách hàng
 | cardNo | Số thẻ (Bank trả số thẻ full, MB App Server thực hiện mã hóa số thẻ) 
 | cardId | -
 | cardStatus | 
Trạng thái thẻ, bao gồm:

• Standby (S): Chờ kích hoạt
• Lock by Customer (C): Khỏa bởi khách hàng
• Lock by Teller (T): Khóa bởi GDV
• Active (A): Kích hoạt 
 | cardName | Tên chủ thẻ 
 | cardType | 
Loại thẻ, bao gồm:

• MainCard: Thẻ chính
• SubCard: Thẻ phụ 
 | issueDate | Ngày phát hành
 | expireDate | Ngày hết hạn 
 | product | 
Sản phẩm thẻ, bao gồm: 

• Credit: Thẻ tín dụng 
• Debit: Thẻ ghi nợ 
• Dual: Thẻ kép 

 | 

 | 
 
 | Bank Server | 
Nhận yêu cầu, xử lý và phản hồi kết quả tương ứng 

• Không hợp lệ: Phản hồi thông báo lỗi tương ứng 
• Hợp lệ: Phản hồi kết quả hợp lệ 
 | 

 | 
 
 | Mobile App | 
Nhận phản hồi từ Bank Server và xử lý tương ứng

• Không hợp lệ:  | Trường hợp | Thông báo lỗi | Xử lý 
 | Chưa có thẻ tín dụng | Quý khách chưa có thẻ tín dụng nội địa tại Co-opBank. Vui lòng mở thẻ để sử dụng | Bấm Đóng → Tắt pop-up lỗi 
 | 
resCode<>000
 | Thông báo lỗi tương ứng với mã lỗi do bank trả về

• Hợp lệ:
1/ Kiểm tra các điều kiện để thực hiện chia thẻ vào tab tín dụng hoặc ghi nợ tương ứng: 
 | Kiểm tra điều kiện  | 
 | Xử lý 

 | Tab thẻ tín dụng (Hiển thị mặc định) | Tab thẻ ghi nợ (Không xử lý trong giai đoạn này)
 | Product  | 
- Credit
- Dual | 
- Debit
- Dual | 
• Nếu thẻ đủ điều kiện nằm trong tab thẻ tín dụng → Trả cờ đánh dấu thẻ nằm trong tab thẻ tín dụng
• Nếu thẻ đủ điều kiện nằm trong tab thẻ ghi nợ → Trả cờ đánh dấu thẻ nằm trong tab thẻ ghi nợ

 

2/ Kiểm tra lần lượt các điều kiện để sắp xếp các thẻ trong tab thẻ tín dụng 
 | STT | Điều kiện  | Thứ tự sắp xếp  | Xử lý 
 | 1 | Card Status  | 
StandBy (S) → Active (A) → Lock by Customer (C) → Lock by Teller (T)

(Chờ kích hoạt → Kích hoạt → Khóa bởi khách hàng → Khóa bởi giao dịch viên)
 | 
Sắp xếp thẻ theo thứ tự hiển thị để 

• Thẻ hiển thị trước sắp xếp trước
• Thẻ hiển thị sau sắp xếp sau

Ví dụ: 

• Thẻ phụ B có trạng thái chờ kích hoạt 
• Thẻ chính A có trạng thái hoạt động 
• Thẻ chính A được phát hành trước thẻ phụ B 
=> Hiển thì thẻ B trước thẻ A 

 | 2 | Card Type | 
MainCard →  SubCard

(Thẻ chính → Thẻ phụ)

 | 3 | IssueDate  | 
Thẻ phát hành trước → Thẻ phát hành sau 

Lưu ý: Đối với trường hợp hiển thị thẻ phụ 

• Case 1: KH A có thẻ chính A và mở thẻ phụ cho KH B (KH B chưa có thẻ) =>  Trên App của KH A hiển thị cả thẻ chính A và thẻ phụ của KH B, trên App KH B không hiển thị thẻ phụ của KH B
• Case 2: KH A có thẻ chính A và thẻ phụ cho KH B (KH B đã có thẻ chính B) =>  Trên App của KH A hiển thị cả thẻ chính A và thẻ phụ B, trên App của KH B chỉ hiển thị thẻ chính B
=> Bank đã xử lý logic để đáp ứng nghiệp vụ này. Bank trả về type thẻ phụ → App hiển thị thẻ phụ, không cần xử lý gì thêm 

Tester cần test 2 cases trên để đảm bảo bank xử lý đúng 

3/ Kiểm tra các điều kiện để hiển thị các dịch vụ tương ứng của thẻ tín dụng, chi tiết trong bảng sau: 
 | Dịch vụ  | 
CardStatus = S (Chờ kích hoạt)

 | CardStatus = A (Hoạt động) | CardStatus = C (Khóa bởi khách hàng) | CardStatus = T (Khóa bởi GDV) | Xử lý 

 | 
CardType = MainCard (Thẻ chính)
 | 
CardType = SubCard (Thẻ phụ)
 | 
CardType = MainCard (Thẻ chính)
 | 
CardType = SubCard (Thẻ phụ)
 | 
CardType = MainCard (Thẻ chính)
 | 
CardType = SubCard (Thẻ phụ)
 | 
CardType = MainCard (Thẻ chính)
 | 
CardType = SubCard (Thẻ phụ)

 | Kích hoạt thẻ | x | x | 
 | 
 | 
 | 
 | 
 | 
 | 
• Cờ đánh dấu hiển thị tính năng: Hiển thị tính năng 
• Cờ đánh dấu không hiển thị tính năng: Ẩn tính năng. không cho phép khách hàng sử dụng 
 | Cài đặt PIN thẻ | 
 | 
 | x | x | 
 | 
 | 
 | 

 | Thông tin thẻ | 
 | 
 | x | x | x | x | x | x
 | Sao kê | 
 | 
 | x | 
 | x | 
 | x | 

 | Thanh toán thẻ tín dụng | 
 | 
 | x | 
 | x | 
 | x | 

 | Lịch sử giao dịch | 
 | 
 | x | x | x | x | x | x

=> Sau khi xử lý các logic trên, mobile app hiển thị danh sách thẻ và các tính năng tương ứng với thẻ 

 | 2 | Bấm vào nút eye | 
Khách hàng
 | 
Khách hàng bấm vào icon "eye" trên thẻ 

 | 
 | 
 | 
Mobile App 
 | 
Kiểm tra PTXT hợp lệ và trả 1 PTXT ưu tiên theo luồng PTXT chung của gd phi tài chính < tham khảo tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ

• SMS OTP
• Soft OTP 
Hiển thị màn hình xác thực tương ứng 

 | 3 | Khách hàng thực hiện xác thực | 
Khách hàng
 | 
Khách hàng thực hiện xác thực

 | 
 | 
 | 
Mobile App 
 | 
Xác thực và xử lý tương ứng: 

• Không hợp lệ: Hiển thị thông bão lỗi 
• Hợp lệ: Gửi yêu cầu lấy thông tin thẻ đến Bank Server

Mô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
 | {
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144"  
"cardId": "xxx",
}
 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | cardId | -
 | Response | 
 | 
{

"requestId": "xxxx",
  "referenceID": "xxx",
"cif": "0100000000144",
"cardNo": "970446345667899",

      "cardId": "xxx",

"accountCardNo": "01000xxxxxxx",

"accountNo": "01000xxxxxxx",
"statusCard": "A",

"deliveryStatus":"5",
"cardName": " NGUYENVAN B",
"cardType": "MainCard",

"product": "Credit",

cardProduct": "Thẻ Vip",
"limitAmount": "8000000",
"availAmount": "7000000",
"currentAmount":"1000000",

"amountStatement":"200000",
"minAmountDue":"100000",

"unpaidMinAmountDue":"100000",

"unpaidStatementAmount ":"100000",

"AutoCreditPaymentType":"A",
"branchIssName": "CN So giao dich",
"branchIssue": "01000",
"issueDate": "31/01/2025",
"expireDate": "31/12/2025",
"statementDate": "24/07/2025",
"dueDate": "31/07/2025",

"startDate": "21/09/2025",

"invoiceDate": "20/10/2025",
  "resCode": "000",
  "resDesc": "Success"

}

 | requestId | -
 | referenceID | -
 | cif | CIFNo của khách hàng
 | cardNo | Số thẻ không masked
 | cardId | -
 | accountCardNo | Tài khoản thẻ 
 | accountNo | Tài khoản thanh toán liên kết (chỉ trả về khi là debit card hoặc dual card)
 | statusCard | 
Trạng thái thẻ, bao gồm:

• Standby (S): Chờ kích hoạt
• Lock by Customer (C): Khỏa bởi khách hàng
• Lock by Teller (T): Khóa bởi GDV
• Active (A): Kích hoạt 
 | deliveryStatus | 
, bao gồm các giá trị: 

• 1
• 2
• 3
• 4
• 5
 | cardName | Tên chủ thẻ 
 | cardType | 
Loại thẻ, bao gồm:

• MainCard: Thẻ chính
• SubCard: Thẻ phụ 
 | product | 
Sản phẩm thẻ, bao gồm: 

• Credit: Thẻ tín dụng 
• Debit: Thẻ ghi nợ 
• Dual: Thẻ kép 
 | cardProduct | Sản phểm thẻ, bao gồm thẻ VIP, thường, thẻ QTDND,...
 | limitAmount | Tổng hạn mức tín dụng 
 | availAmount | Hạn mức còn lại 
 | currentAmount | Dư nợ hiện tại 
 | amountStatement | Dư nợ sao kê kỳ gần nhất 
 | minAmountDue | 
Số tiền thanh toán tối thiểu trên sao kê (MB ko dùng)

 | unpaidMinAmountDue | Số tiền min amount phải trả còn lại (thông tin show khi thanh toán thẻ)
 | unpaidStatementAmount | 
Số tiền phải trả còn lại trên sao kê (show khi tra cứu thông tin thẻ và hiện khi thanh toán thẻ)

 | AutoCreditPaymentType | 
Loại thanh toán thẻ tín dụng, bao gồm: 

• Auto (A): Tự động thanh toán 
• Manual (M): Thanh toán thủ công 
 | branchIssName | Đơn vị cấp hạn mức thẻ
 | branchIssue | Mã Đơn vị cấp hạn mức thẻ
 | issueDate | Ngày phát hành thẻ 
 | expireDate | Ngày hết hạn thẻ 
 | statementDate | Ngày sao kê gần nhất 
 | dueDate | Ngày hết hạn thanh toán sao kê gần nhất 
 | startDate | Ngày bắt đầu tính sao kê 
 | invoiceDate | Ngày chốt sao kê
 | resCode | resCode<>000
 | resDesc | 
The corresponding error message for the returned code

 | 
 | 
 | 
Bank Server
 | 
Nhận yêu cầu từ Mobile App, truy vấn thông tin và phản hồi kết quả 

 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi từ Bank Server:

• Không hợp lệ: Hiển thị thông báo lỗi  | Trường hợp | Thông báo lỗi | Xử lý 
 | 
resCode<>000
 | Thông báo lỗi tương ứng với mã lỗi do bank trả về | Bấm Đóng → Tắt pop-up lỗi 

• Hợp lệ: Hiển thị pop-up bao gồm các thông tin 
• Tiêu đề: Thông tin thẻ
• Tên chủ thẻ
• Số thẻ full không mask 
• Ngày phát hành thẻ 
• Ngày hết hạn thẻ 
• Button Đóng → Khách hàng bấm đóng, tắt pop-up hiển thị màn hình Danh sách thẻ 

### 5/ Bảng dữ liệu

#### 5.1/ Bảng dữ liệu sử dụng

Bao gồm tất cả các bảng dữ liệu có sử dụng trong nghiệp vụ phân tích
 | TT | Table Name | Description | Create | Reference | Update | Delete
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập mô tả mục đích của Table | Gõ "x" nếu nghiệp vụ có thao tác "Create" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Reference" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Update" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Delete" đến Table

5.2/ Thông tin cập nhật vào bảng dữ liệu

Áp dụng cho các bảng dữ liệu có sử dụng thao tác "Create", "Update"
 | TT | Table Name | Field | Value | Note
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập trường dữ liệu (thuộc tính) có cập nhật giá trị dữ liệu | Nhập giá trị dữ liệu cập nhật | Nhập ghi chú thêm (nếu có)

---

### 36.3. 2. Thông tin thẻ

> **Page ID:** `891585028` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/891585028

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.3.1. Flow&Action screen - Thông tin thẻ

> **Page ID:** `897976208` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/897976208

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người thay đổi  | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A |   | 
 | 
Tạo mới tài liệu
 | V1
 | 
 
 | M | 
 
 | V1 | 
Đổi tên trường "Số tiền phải trả còn lại trên sao kê" thành "Số tiền tối thiểu phải trả còn lại trên sao kê"
 | V2
Muc lục
none

### 1/ Danh sách màn hình

##### MH1: <Thông tin thẻ>

### 2/ Mô tả màn hình

##### MH1: <Tên màn hình>
 | STT | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nút quay lại | Icon Button | Nhấn | - | - | Điều hướng quay lại màn hình trước đó.
 | 2 | Tiêu đề màn hình | Label  | Read Only | - | - | Hiển thị tên màn hình: Thông tin thẻ.
 | 
Cụm thông tin thẻ 

 | 3 | 
Số tài khoản thẻ

accountCardNo
 | Label  | Read Only | - | - | Số tài khoản gắn với thẻ tín dụng 
 | 4 | 
Sản phẩm thẻ

cardProduct
 | Label  | Read Only | - | - | 
Cho biết tên sản phẩm thẻ. Ví dụ thẻ VIP, thẻ premium,...

 | 5 | 
Loại thẻ

 | Label  | Read Only | - | - | 
Loại thẻ, bao gồm:

• MainCard: Thẻ chính
• SubCard: Thẻ phụ 
 | 6 | 
Đơn vị quản lý

branchIssName
 | Label  | Read Only | - | - | Chi nhánh quản lý thẻ 
 | 
Cụm thông tin dư nợ 

 | 7 | 
Thông tin dư nợ

(Cần cofirm lại)
 | Label  | Read Only | - | - | Tổng dư nợ thẻ hiện tại.
Định dạng tiền tệ VND, có phân tách hàng nghìn.
 | 8 | 
Hạn mức tín dụng

limitAmount
 | Label  | Read Only | - | - | Hạn mức tín dụng tối đa được cấp cho thẻ.
 | 9 | 
Hạn mức còn lại hiện tại

availAmount
 | Label  | Read Only | - | - | Số tiền còn có thể chi tiêu.
Logic: Hạn mức tín dụng - Dư nợ hiện tại = Hạn mức còn lại hiện tại 
 | 10 | 
Dư nợ hiện tại

currentAmount
 | Label  | Read Only | - | - | Tổng số tiền đang nợ tại thời điểm hiện tại.
 | 11 | 
Dư nợ kỳ sao kê gần nhất

amountStatement
 | Label  | Read Only | - | - | Số dư nợ được ghi nhận tại kỳ sao kê gần nhất.
 | 12 | 
Số tiền thanh toán tối thiểu trên sao kê

minAmountDue
 | Label  | Read Only | - | - | Số tiền tối thiểu khách hàng cần thanh toán trong kỳ.
Nếu không thanh toán đủ sẽ phát sinh phí/phạt theo quy định.
 | 13 | 
Số tiền tối thiểu phải trả còn lại trên sao kê

unpaidMinAmountDue
 | Label  | Read Only | - | - | Tổng số tiền còn phải thanh toán cho kỳ sao kê.
 | 14 | 
Ngày đến hạn thanh toán

dueDate
 | Label  | Read Only | - | - | Ngày cuối cùng khách hàng cần hoàn tất thanh toán để tránh phí phạt.
 | 15 | 
Ngày sao kê gần nhất

statementDate
 | Label  | Read Only | - | - | Ngày hệ thống chốt sao kê gần nhất.

---

#### 36.3.2. User Action Flow - Thông tin thẻ

> **Page ID:** `897979071` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/897979071

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A |   | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Tạo mới tài liệu 
 | V1 | 

Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Thông tin thẻ
 | Use Case ID | UC_CARD_INFO
 | Use Case Description | 
Là người dùng, tôi muốn xem thông tin chi tiết của thẻ tín dụng 

Lưu ý: Phạm vi của giai đoạn 1 là thẻ tín dụng, chưa xử lý phần thẻ ghi nợ và thẻ kép 

 | Actor | 
Khách hàng, MB App Client, MB App Server, Bank Server

 | Priority | Medium
 | Trigger | 
Khách hàng nhấn nút "Chi tiết thẻ" trên màn dịch vụ thẻ 

 | 
Pre-Condition
 | 
• Khách hàng đăng nhập Mobile App thành công
• Khách hàng có tồn tại thẻ tín dụng trên hệ thống Co-opBank 
1. KH đăng nhập thành công ứng dụng; 2. KH có tài khoản nguồn hợp lệ để thực hiện giao dịch; 3. Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch

 | Post-Condition | 
• Hệ thống truy vấn thông tin thẻ thành công và hiển thị dữ liệu thông tin thẻ trên giao diện mobile app 
• Khách hàng xem thông tin thẻ thành công 
1. KH thực hiện lệnh chuyển tiền nội bộ thành công; 2. Tài khoản nguồn của KH bị trừ số tiền giao dịch (bao gồm phí nếu có); 3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng (trừ phí nếu có); 4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]; 5. Hệ thống MB ghi nhận giao dịch chuyển tiền nội bộ vào [Transaction History]

 | Basic Flow | 
• Khách hàng đăng nhập mobile app Co-opBank 
• Khách hàng truy cập dịch vụ thẻ trên màn hình Home 
• Hệ thống thực hiện truy vấn danh sách thẻ tín dụng của khách hàng và hiển thị danh sách thẻ cùng các tính năng trên giao diện mobile app
• Khách hàng bấm nút "Chi tiết" 
• Hệ thống thực hiện truy vấn chi tiêt thẻ tín dụng và hiển thị chi tiết thẻ trên giao diện mobile app 
 | Alternative Flow | 
--

 | Exception Flow | 
• Truy vấn chi tiết thẻ không thành công → Hiển thị thông báo lỗi "Lỗi hệ thống, quý khách vui lòng thử lại" 
 | Bussiness Rules | 
• BR-01: Chỉ hiển thị thông tin chi tiết thẻ đối với thẻ có trạng thái hoạt động, khóa do khách hàng và khóa bởi giao dịch viên 
• BR-02: Hiển thị thông tin chi tiết thẻ đối với cả thẻ chính và thẻ phụ 
 | Non-Funtional Requiremnt | 
--

### 2/ Luồng xử lý

##### Truy cập chức năng

##### MH1: <Tên màn hình>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Khởi tạo màn hình  | Khách hàng | Khách hàng bấm nút "Chi tiết" trên màn hình Dịch vụ thẻ
 | 
 | 
 | 
Mobile App 
 | 
Kiểm tra thông tin khách hàng và gửi yêu cầu lấy chi tiết thẻ đến Bank Server API queryCard (Thông tin thẻ)
Mô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
 | {
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144"  
"cardId": "xxx",
}
 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | cardId | -
 | Response | 
 | 
{

"requestId": "xxxx",
  "referenceID": "xxx",
"cif": "0100000000144",
"cardNo": "970446345667899",

      "cardId": "xxx",

"accountCardNo": "01000xxxxxxx",

"accountNo": "01000xxxxxxx",
"statusCard": "A",

"deliveryStatus":"5",
"cardName": " NGUYENVAN B",
"cardType": "MainCard",

"product": "Credit",

cardProduct": "Thẻ Vip",
"limitAmount": "8000000",
"availAmount": "7000000",
"currentAmount":"1000000",

"amountStatement":"200000",
"minAmountDue":"100000",

"unpaidMinAmountDue":"100000",

"unpaidStatementAmount ":"100000",

"AutoCreditPaymentType":"A",
"branchIssName": "CN So giao dich",
"branchIssue": "01000",
"issueDate": "31/01/2025",
"expireDate": "31/12/2025",
"statementDate": "24/07/2025",
"dueDate": "31/07/2025",

"startDate": "21/09/2025",

"invoiceDate": "20/10/2025",
  "resCode": "000",
  "resDesc": "Success"

}

 | requestId | -
 | referenceID | -
 | cif | CIFNo của khách hàng
 | cardNo | Số thẻ không masked
 | cardId | -
 | accountCardNo | Tài khoản thẻ 
 | accountNo | Tài khoản thanh toán liên kết (chỉ trả về khi là debit card hoặc dual card)
 | statusCard | 
Trạng thái thẻ, bao gồm:

• Standby (S): Chờ kích hoạt
• Lock by Customer (C): Khỏa bởi khách hàng
• Lock by Teller (T): Khóa bởi GDV
• Active (A): Kích hoạt 
 | deliveryStatus | 
, bao gồm các giá trị: 

• 1
• 2
• 3
• 4
• 5
 | cardName | Tên chủ thẻ 
 | cardType | 
Loại thẻ, bao gồm:

• MainCard: Thẻ chính
• SubCard: Thẻ phụ 
 | product | 
Sản phẩm thẻ, bao gồm: 

• Credit: Thẻ tín dụng 
• Debit: Thẻ ghi nợ 
• Dual: Thẻ kép 
 | cardProduct | Sản phểm thẻ, bao gồm thẻ VIP, thường, thẻ QTDND,...
 | limitAmount | Tổng hạn mức tín dụng 
 | availAmount | Hạn mức còn lại 
 | currentAmount | Dư nợ hiện tại 
 | amountStatement | Dư nợ sao kê kỳ gần nhất 
 | minAmountDue | 
Số tiền thanh toán tối thiểu trên sao kê (MB ko dùng)

 | unpaidMinAmountDue | Số tiền min amount phải trả còn lại (thông tin show khi thanh toán thẻ)
 | unpaidStatementAmount | 
Số tiền phải trả còn lại trên sao kê (show khi tra cứu thông tin thẻ và hiện khi thanh toán thẻ)

 | AutoCreditPaymentType | 
Loại thanh toán thẻ tín dụng, bao gồm: 

• Auto (A): Tự động thanh toán 
• Manual (M): Thanh toán thủ công 
 | branchIssName | Đơn vị cấp hạn mức thẻ
 | branchIssue | Mã Đơn vị cấp hạn mức thẻ
 | issueDate | Ngày phát hành thẻ 
 | expireDate | Ngày hết hạn thẻ 
 | statementDate | Ngày sao kê gần nhất 
 | dueDate | Ngày hết hạn thanh toán sao kê gần nhất 
 | startDate | Ngày bắt đầu tính sao kê 
 | invoiceDate | Ngày chốt sao kê
 | resCode | resCode<>000
 | resDesc | 
The corresponding error message for the returned code

 | 
 | 
 | 
Bank Server
 | 
Nhận yêu cầu từ Mobile App, truy vấn thông tin và phản hồi kết quả 

 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi từ Bank Server:

• Không hợp lệ:  | Trường hợp | Thông báo lỗi | Xử lý 
 | 
resCode<>000
 | Thông báo lỗi tương ứng với mã lỗi do bank trả về | Bấm Đóng → Tắt pop-up lỗi 

• Hợp lệ: Hiển thị bottom sheet thông tin thẻ gồm các thông tin được mô tả chi tiết trong tài liệu 

### 5/ Bảng dữ liệu

#### 5.1/ Bảng dữ liệu sử dụng

Bao gồm tất cả các bảng dữ liệu có sử dụng trong nghiệp vụ phân tích
 | TT | Table Name | Description | Create | Reference | Update | Delete
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập mô tả mục đích của Table | Gõ "x" nếu nghiệp vụ có thao tác "Create" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Reference" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Update" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Delete" đến Table

5.2/ Thông tin cập nhật vào bảng dữ liệu

Áp dụng cho các bảng dữ liệu có sử dụng thao tác "Create", "Update"
 | TT | Table Name | Field | Value | Note
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập trường dữ liệu (thuộc tính) có cập nhật giá trị dữ liệu | Nhập giá trị dữ liệu cập nhật | Nhập ghi chú thêm (nếu có)

---

### 36.4. 3. Kích hoạt thẻ

> **Page ID:** `888445696` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/888445696

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.4.1. Flow&Action screen - Kích hoạt thẻ

> **Page ID:** `888445704` · **Version:** 29
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/888445704

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Link Jira
 | 
  
 | A | 
 
 | 
 | 
Tạo mới tài liệu
 | V.1.0.0 | 
VNPAY's Jira23316405-dc41-35f9-b977-f5027af0de71CNB-2632

Mục lục

### 1/ Luồng màn hình

T

### 2/ Danh sách màn hình
true100px
##### MH1. Danh sách thẻ (trạng thái thẻ = Chờ kích hoạt)

true100px
##### MH2. Nhập 8 số cuối của thẻ

true100px
##### MH2.1. Popup thông báo sai số thẻ

true100px
##### MH2.1.1. Popup thông báo nhập thiếu số thẻ/không nhập

true100px
##### MH2.2. Nhập mã PIN (PTXT = SoftOTP)

true100px
##### MH2.2.1. Xác thực giao dịch (PTXT = SoftOTP)

true100px
##### MH2.3. Xác thực giao dịch (PTXT = SMS OTP)

true100px
##### MH2.4. Popup thông báo Kích hoạt thẻ thành công 

true100px
##### MH3. MH cài đặt mã PIN (default)

true100px
##### MH3.1. TH1. Bỏ trống trường Nhập mã Pin

true100px
##### MH3.2. TH2. Bỏ trống trường Nhập lại mã Pin mới

true100px
##### MH3.3. TH3. Nhập không đủ 06 ký tự số của trường Nhập mã Pin

true100px
##### MH3.4. TH4. Nhập không đủ 06 ký tự số của trường Nhập lại mã Pin

true100px
##### MH3.5. TH5. Nhập 06 ký tự số không trùng nhau của 2 trường

true100px
##### MH3.6. TH6. Nhập 06 ký tự số là dãy số tiến liên tiếp

true100px
##### MH3.7. TH7. Nhập 06 ký tự số là dãy số trùng nhau

true100px
##### MH4. Popup cài mã Pin thành công

### 3/ Mô tả màn hình

##### MH1. Danh sách thẻ (trạng thái thẻ = Chờ kích hoạt)
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Các thông tin tại Danh sách thẻ (Tham khảo chức năng )
 | 2 | Kích hoạt thẻ | Button | Click | -- | -- | 
• Chỉ hiển thị đối với thẻ có trạng thái = Chờ kích hoạt
• Mặc định: enable
• Khi click: điều hướng sang MH2. Nhập 8 số cuối của thẻ

##### MH2. Nhập 8 số cuối của thẻ
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Quay lại | Button (icon) | Click | -- | -- | 
• Mặc định: enable
• Khi click: quay lại MH Danh sách thẻ
 | 2 | Tiêu đề màn hình | Label | Read Only | -- | -- | Hiển thị: Kích hoạt thẻ
 | 3 | Nhập 8 số cuối của thẻ | Textbox | Input | Có | 8 | 
• Place holder: Nhập 8 số cuối của thẻ
• Chặn nhập ký tự khác số
 | 4 | Tiêu đề phụ | Label | Read Only | -- | -- | Hiển thị: Quý khách vui lòng nhập 8 số cuối được in trên mặt trước của thẻ
 | 5 | 
Xác nhận

Tiếp tục
 | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: <Tham chiếu logic xử lý>

##### MH2.2. Nhập mã PIN (PTXT = SoftOTP)

##### MH2.2.1. Xác thực giao dịch (PTXT = SoftOTP)

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực bằng Soft OTP>

##### MH2.3. Xác thực giao dịch (PTXT = SMS OTP)

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực GD bằng SMS OTP>

##### MH2.4. Popup thông báo Kích hoạt thẻ thành công 
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Thông báo | Text | Read Only | -- | -- | 
Hiển thị thông báo: "Quý khách đã kích hoạt thẻ thành công. Vui lòng cài đặt mã PIN 06 số cho thẻ. Để đảm bảo an toàn, sau khi cài đặt mã PIN mới vui lòng bảo mật mã PIN, không chia sẻ cho bất kỳ ai để tránh bị lộ thông tin thẻ."

 | 2 | Bỏ qua | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: đóng popup, quay lại MH Danh sách thẻ (thẻ vừa kích hoạt chuyển trạng thái = Hoạt động) <Tham khảo logic xử lý>
 | 3 | Cài đặt mã Pin | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: điều hướng sang màn hình tạo mã pin thẻ (MH 3) <Tham khảo logic xử lý>

##### MH3. MH tạo mã PIN thẻ 
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Quay lại | Button (icon) | Click | -- | -- | 
• Mặc định: enable
• Khi click: quay lại MH Danh sách thẻ
 | 2 | Tiêu đề màn hình | Label | Read Only | -- | -- | Hiển thị: Cài đặt mã PIN 
 | 3 | Tiêu đề | Label | Read Only | -- | -- | Hiển thị: Quý khách vui lòng cài đặt mã PIN 6 số cho thẻ
 | 4 | Nhập mã PIN | Textbox | Input | Có | 6 | 
• Chặn nhập ký tự khác số
• Khi nhập: hệ thống hiển thị ký tự dạng dot (•) để ẩn mã PIN
 | 5 | Nhập lại mã PIN  | Textbox | Input | Có | 6 | 
• Chặn nhập ký tự khác số
• Khi nhập: hệ thống hiển thị ký tự dạng dot (•) để ẩn
 | 6 | Lưu ý | Alert | Read Only | -- | -- | 
Mục đích: Hiển thị các quy tắc và lưu ý về việc cài đặt và bảo mật mã PIN

Hiển thị:

• Để đảm bảo an toàn, sau khi đặt mã PIN mới vui lòng bảo mật mã Pin, không chia sẻ cho bất kỳ ai để tránh bị lộ thông tin thẻ
• mã Pin mới phải thỏa mãn các điều kiện sau: 
- Không được là dãy số tiến liên tiếp 
- Không được là dãy số giống nhau
 | 7 | Xác nhận | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: <Tham chiếu logic xử lý>

##### MH4. Popup cài mã Pin thành công
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Thông báo | Text | Read Only | -- | -- | 
Hiển thị thông báo: "Quý khách cài đặt mã Pin thẻ thành công."

 | 2 | Đóng | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: đóng popup, quay lại MH danh sách thẻ (thẻ vừa kích hoạt & cài đặt mã Pin, trạng thái thẻ = Hoạt động)

---

#### 36.4.2. User Action Flow - Kích hoạt thẻ

> **Page ID:** `888445712` · **Version:** 25
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/888445712

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Link Jira
 | 
  
 | A | 
 
 | 
 | 
Tạo mới tài liệu
 | V.1.0 | 
VNPAY's Jira23316405-dc41-35f9-b977-f5027af0de71CNB-2632

 | 
 
 | M | 
 
 | V1.1 | 
Cập nhật

• Tại màn hình Cài đặt mã Pin, click icon Back: quay lại MH Danh sách thẻ | V.1.2 | 
VNPAY's Jira23316405-dc41-35f9-b977-f5027af0de71CB-1266

VNPAY's Jira23316405-dc41-35f9-b977-f5027af0de71CB-1265

Mục lục

### 1/ Mô tả Usecase
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn | Use Case Name | Kích hoạt thẻ
 | Use Case ID | --
 | Use Case Description | Khách hàng sử dụng Mobile Banking để thực hiện kích hoạt thẻ Credit. Hệ thống tiếp nhận, xác thực, lưu yêu cầu và hiển thị trên Báo cáo Quản lý thẻ để ghi nhận giao dịch Phi tài chính
 | Actor | Khách hàng (KH), Hệ thống MB, Bank, Back Office
 | Priority | High
 | Trigger | Khách hàng chọn chức năng "Dịch vụ thẻ" → chọn "Kích hoạt thẻ"
 | 
Pre-Condition
 | 
• Khách hàng đã đăng nhập Mobile Banking thành công
• Khách hàng đã được phát hành thẻ vật lý và giao hàng đến thành công
Đối với Kích hoạt thẻ:

• Thẻ ở trạng thái = Chờ kích hoạt (card status = Standby (S))+ Trạng thái phát hành = Đã bàn giao cho khách hàng (deliveryStatus =4)
• Khách hàng đã cài đặt phương thức xác thực (softOTP hoặc smsOTP)
Đối với Cài đặt mã PIN:

• Thẻ ở trạng thái = Hoạt động (card status = Active (A))
 | Post-Condition | 
• Khách hàng Kích hoạt thẻ thành công (trạng thái thẻ từ Chờ kích hoạt → Hoạt động)
• Hệ thống ghi nhận giao dịch giao dịch phi tài chính trên BackOffice
 | Exception Flow | 
• Khách hàng nhập sai 8 số cuối in trên mặt trước của thẻ
• Mã OTP sai hoặc đã hết hiệu lực
• Cài đặt mã PIN không hợp lệ (sai business rules)
• Thoát ứng dụng khi đang kích hoạt
 | Basic Flow | 
Kích hoạt thẻ:

1/ Khách hàng đăng nhập vào Mobile Banking → Chọn "Dịch vụ thẻ" 

2/ Khách hàng chọn thẻ tín dụng có trạng thái thẻ = Chờ kích hoạt → Chọn "Kích hoạt thẻ"

3/ Khách hàng nhập 8 số cuối được in trên mặt trước của thẻ vật lý → Chọn "Tiếp tục"

4/ Khách hàng xác nhận yêu cầu theo PTXT đã cài đặt gồm:

• SoftOTP
• SMT OTP
5/ Hệ thống ghi nhận yêu cầu kích hoạt thẻ trên BO 

Cài đặt mã PIN sau khi kích hoạt thẻ:

1/ Hệ thống ghi nhận Kích hoạt thẻ thành công → Khách hàng chọn "Cài đặt mã PIN"

2/ Khách hàng nhập mã PIN thẻ 6 số mới và nhập lại mã PIN để xác nhận → Chọn "Xác nhận"

3/ Hệ thống ghi nhận cài đặt mã PIN thẻ thành công

Lưu ý: tất cả các yêu cầu Kích hoạt thẻ, Cài đặt mã PIN đều được ghi nhận tại Báo cáo quản lý thẻ (BO)

(Tham khảo Báo cáo Quản lý thẻ - Link Update sau)

 | Bussiness rules | | 
 | Mã | Nội dung
 | 1 | BR1 | Chỉ hiển thị chức năng Kích hoạt thẻ nếu trạng thái thẻ là "Chờ kích hoạt" và trạng thái phát hành là "Đã bàn giao cho khách hàng"
 | 2 | BR2 | Hiển thị với cả thẻ chính và thẻ phụ
 | 3 | BR3 | PTXT theo thứ tự ưu tiên: Soft OTP → SMS OTP tùy theo PTXT KH cài đặt
 | 4 | BR4 | Cài đặt mã PIN trong cùng luồng kích hoạt: Không cần xác thực (Do đã xác thực trong luồng kích hoạt thẻ)
 | 5 | BR5 | Nếu Bỏ qua cài đặt mã PIN trong luồng Kích hoạt hoặc Kích hoạt xong thoát app  → Nếu muốn cài mã PIN thì đi vào luồng Cài đặt mã PIN (Tham khảo 4. Cài đặt PIN thẻ)

### 2/ Luồng sơ đồ

trueUntitled Diagram-1767671820186falseautotoptrue892200316

### 3/ Logic xử lý

#### 3.1. Kích hoạt thẻ

##### MH1. Danh sách thẻ (trạng thái thẻ = Chờ kích hoạt)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Gọi API lấy danh sách thẻ (Chi tiết logic tham khảo tài liệu )
 | 2 | Click "Kích hoạt thẻ" | Hệ thống MB | Gửi yêu cầu lấy thông tin thẻ (Gọi API querryCard)
 | 3 | 
 | Bank | Truy vấn thông tin thẻ & trả kết quả cho hệ thống MB
 | 4 | 
 | Hệ thống MB | Điều hướng đến MH Kích hoạt thẻ (MH2. Nhập 8 số cuối của thẻ)

##### MH2. Nhập 8 số cuối của thẻ
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Click "Xác nhận" "Tiếp tục" | Hệ thống MB | 
1/ Thực hiện kiểm tra thông tin khách hàng nhập trên màn hình:

• 
Không hợp lê:
 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Để trống số thẻ | 
Quý khách vui lòng nhập 8 số cuối của thẻ
 | 
Hiển thị popup thông báo

 | 2 | Nhập < 8 ký tự số

• Hợp lệ (Nhập = 8 ký tự số): chuyển sang 2
2/ Gửi yêu cầu Kích hoạt thẻ (truyền 8 số cuối của thẻ)

2.1/ Kiểm tra số thẻ với thông tin của khách hàng

• Số thẻ không khớp: Hiển thị popup thông báo: "8 số cuối của thẻ không chính xác. Quý khách vui lòng kiểm tra lại"
• Số thẻ khớp: chuyển sang 2
2.2/ Nhận yêu cầu và kiểm tra PTXT:

• 1/ Kiểm tra trạng thái Soft OTP của user
• Nếu KH đã kích hoạt Soft OTP → Chuyển sang 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
• 2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó
• Nếu số lần xác thực SMS OTP < (n) → Server xác định PTXT là SMS OTP
• Nếu số lần xác thực SMS OTP >= (n) → Server xác định PTXT ưu tiên nhất so Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/AutoLock → Server xác định PTXT là SMS OTP
(Tham khảo Logic xác định PTXT của GD phi tài chính tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

3/ Hiển thị màn hình xác thực với PTXT tương ứng

##### MH2.2. Nhập mã PIN (PTXT = SoftOTP)

##### MH2.2.1. Xác thực giao dịch (PTXT = SoftOTP)

##### MH2.3. Xác thực giao dịch (PTXT = SMS OTP)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhập OTP và Click "Xác nhận" | Hệ thống MB | 
1/ Thực hiện xác thực giao dịch

• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
• Nội dung SMS OTP gửi về SĐT khách hàng: Xac thuc Kich hoat the co ma OTP la {ma OTP}, co hieu luc trong {n} phut. 
(VD: Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc kich hoat the co ma OTP là 123456, co hieu luc trong 1 phut)

• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
Validate thông tin:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: chuyển sang 2
2/ Kiểm tra OTP:

• Không hợp lệ: Trả kết quả lỗi cho MB Client
• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
• Hợp lệ: chuyển sang 3
3/ Chuyển tiếp yêu cầu kích hoạt thẻ sang Bank
 (API activateCard) 

 | 2 | 
 | Bank | Thực hiện kích hoạt thẻ & trả kết quả
 | 3 |   | Hệ thống MB | 
Nhận kết quả và xử lý:

• 
Không thành công:
 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi    | Xử lý (nếu có)
 | 1 | 
Nhập sai 8 số cuối của thẻ
 | 
8 số cuối của thẻ không chính xác. Quý khách vui lòng kiểm tra lại.
 | 
resCode <> 000       
 | 
Ghi nhận giao dịch với trạng thái = Thất bại

(Báo cáo quản lý thẻ)

 | 2 | 
Time out

(Tham khảo )
 | Hệ thống tạm thời gián đoạn, xin quý khách vui lòng thử lại sau. | 
 
 | 
Ghi nhận giao dịch với trạng thái = Time out

(Báo cáo quản lý thẻ)

 | 3 | 
Lỗi khác

(Tham khảo )
 | Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau. | 
     
 | 
Ghi nhận giao dịch với trạng thái = Thất bại

(Báo cáo quản lý thẻ)

• Thành công: ghi nhận giao dịch thành công & hiển thị thông báo: "Quý khách đã kích hoạt thẻ thành công"
Lưu ý: Các trường hợp đều ghi nhận vào Báo cáo quản lý thẻ - Giao dịch Kích hoạt thẻ

Trạng thái giao dịch gồm:

• Thành công
• Thất bại
• Time out

##### MH2.4. Popup thông báo Kích hoạt thẻ thành công
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click "Bỏ qua" | Hệ thống MB | 
Thực hiện đóng popup, quay lại Màn hình Danh sách thẻ

 | 2 | Click "Cài đặt mã PIN" | Hệ thống MB | 
Điều hướng sang màn hình cài đặt mã PIN (MH3. MH tạo mã PIN thẻ)

#### 3.2. Cài đặt mã PIN thẻ

##### MH3. MH tạo mã PIN thẻ

Lưu ý: Đây là trường hợp cài đặt mã PIN ngay sau khi kích hoạt thẻ thành công nên không cần kiểm tra PTXT
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | 
Quay về màn hình thao tác trước đó

Quay về màn hình Danh sách thẻ

 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Click "Xác nhận" | Hệ thống MB | 
1/ Thực hiện kiểm tra mã PIN khách hàng nhập trên màn hình:

• 
Không hợp lệ:
 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống trường Nhập mã Pin | 
Quý khách vui lòng nhập mã Pin
 | 
Hiển thị dưới ô input

 

 

 

 

 

 

 | 2 | Bỏ trống trường Nhập lại mã Pin | 
Quý khách vui lòng nhập lại mã Pin

 | 3 | Nhập không đủ 06 ký tự số của trường Nhập mã Pin | 
Quý khách vui lòng nhập mã Pin bao gồm 6 ký tự số

 | 4 | Nhập không đủ 06 ký tự số của trường Nhập lại mã Pin | 
Quý khách vui lòng nhập lại mã Pin bao gồm 6 ký tự số

 | 5 | Nhập 06 ký tự số không trùng nhau của 2 trường | 
Mã Pin không trùng nhau. Quý khách vui lòng kiểm tra lại

 | 6 | Nhập 06 ký tự số là dãy số tiến liên tiếp | 
Mã Pin không được phép là các ký tự liên tiếp. Quý khách vui lòng kiểm tra lại

 | 7 | Nhập 06 ký tự số là dãy số trùng nhau | 
Mã Pin không được phép là các ký tự trùng nhau. Quý khách vui lòng kiểm tra lại

• Hợp lệ: chuyển sang 2
2/ Gửi yêu cầu tạo mã PIN (API pinCardSetUp)

 | 4 | 
 | Bank  | 
Nhận yêu cầu, kiểm tra & thực hiện cài đặt mã PIN thẻ

 | 5 | 
 | Hệ thống MB | 
Nhận kết quả và xử lý:

• 
Không thành công:
 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi    | Xử lý (nếu có)
 | 1 | 
Time out

(Tham khảo case 8 tại )
 | Hệ thống tạm thời gián đoạn, xin quý khách vui lòng thử lại sau | 
 
 | 
Ghi nhận giao dịch với trạng thái = Time out

(Báo cáo quản lý thẻ)

 | 2 | 
Lỗi khác

(Tham khảo case 9 tại )
 | Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau. | 
 resCode <> "000"     
 | 
Ghi nhận giao dịch với trạng thái = Thất bại

(Báo cáo quản lý thẻ)

• Thành công: ghi nhận giao dịch thành công (Báo cáo quản lý thẻ) & hiển thị thông báo: "Quý khách cài đặt mã PIN thẻ thành công."
Lưu ý: Các trường hợp đều ghi nhận vào Báo cáo quản lý thẻ - Giao dịch Cài đặt PIN thẻ

• 
Trạng thái giao dịch gồm:

• Thành công
• Thất bại
• Time out

---

### 36.5. 4. Cài đặt PIN thẻ

> **Page ID:** `888445698` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/888445698

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.5.1. Flow&Action screen - Cài đặt PIN thẻ

> **Page ID:** `895168965` · **Version:** 19
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/895168965

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Link Jira
 | 
  
 | A | 
 
 | 
 | 
Tạo mới tài liệu
 | V.1.0.0 | 
VNPAY's Jira23316405-dc41-35f9-b977-f5027af0de71CNB-2635

Mục lục

### 1/ Luồng màn hình

#### 1.1. Sơ đồ luồng màn hình

trueCài đặt mã PIN_Flowfalseautotoptrue16686396

#### 1.2. Luồng màn hình

### 2/ Danh sách màn hình
true100px
##### MH1. Danh sách thẻ (trạng thái thẻ = Hoạt động)

true100px
##### MH2. Cài đặt mã PIN

true100px
##### MH3. MH xác thực Facepay

#### 2.1. Xác thực Facepay kết hợp SoftOTP
true100px
##### MH3.1. MH nhập mã PIN softOTP (PTXT = SoftOTP)

true100px
##### MH3.2. Xác thực giao dịch (PTXT = SoftOTP)

#### 2.2. Xác thực Facepay kết hợp SMS OTP
true100px
##### MH4.1. MH nhập mã OTP (PTXT = SMS OTP) (default)

true100px
##### MH4.2. MH nhập mã OTP (PTXT = SMS OTP)

#### 2.3. Xác thực Facepay khi KH chưa có dữ liệu STH C06/Đã có dữ liệu STH C06 + GTTT hết hạn
true100px
##### MH5.1. Trường hợp Đã thu thập STH + GTTT hết hạn

true100px
##### MH5.2. Trường hợp Chưa thu thập STH 

true100px
##### MH6. Điều khoản thu thập STH

true100px
##### MH7. Vào luồng của SDK thu thập STH

true100px
##### MH8. Kết quả

### 3/ Mô tả màn hình

##### MH1. Danh sách thẻ (trạng thái thẻ = Hoạt động)
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Các thông tin tại Danh sách thẻ (Tham khảo chức năng 1. Danh sách thẻ)
 | 2 | Cài đặt PIN thẻ | Button | Click | -- | -- | 
• Chỉ hiển thị đối với thẻ có trạng thái = Hoạt động
• Mặc định: enable
• Khi click: điều hướng sang MH2. Cài đặt mã PIN

##### MH2. Cài đặt mã PIN
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Quay lại | Button (icon) | Click | -- | -- | 
• Mặc định: enable
• Khi click: quay lại MH1. Danh sách thẻ
 | 2 | Tiêu đề màn hình | Label | Read Only | -- | -- | Hiển thị: Cài đặt mã PIN 
 | 3 | Tiêu đề | Label | Read Only | -- | -- | Hiển thị: Quý khách vui lòng cài đặt mã PIN 6 số cho thẻ
 | 4 | Nhập mã PIN | Textbox | Input | Có | 6 | 
• Chặn nhập ký tự khác số
• Khi nhập: hệ thống hiển thị ký tự dạng dot (•) để ẩn mã PIN
 | 5 | Nhập lại mã PIN  | Textbox | Input | Có | 6 | 
• Chặn nhập ký tự khác số
• Khi nhập: hệ thống hiển thị ký tự dạng dot (•) để ẩn
 | 6 | Lưu ý | Alert | Read Only | -- | -- | 
Mục đích: Hiển thị các quy tắc và lưu ý về việc cài đặt và bảo mật mã PIN

Hiển thị:

• Để đảm bảo an toàn, sau khi đặt mã PIN mới vui lòng bảo mật mã PIN, không chia sẻ cho bất kỳ ai để tránh bị lộ thông tin thẻ
• Mã Pin mới phải thỏa mãn các điều kiện sau: 
- Không được là dãy số tiến liên tiếp 
- Không được là dãy số giống nhau
 | 7 | 
Xác nhận

Tiếp tục
 | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: <Tham chiếu logic xử lý>

##### MH3. MH xác thực Facepay 

(Hiển thị với trường hợp Đã thu thập STH + GTTT chưa hết hạn)
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Xác thực Facepay thành công
 | 2 | Quay lại | Button (icon) | Click | -- | -- | 
• Mặc định: enable
• Khi click: quay lại MH2. Cài đặt mã PIN
 | 3 | Tiêu đề  | Label | ReadOnly | -- | -- | Hiển thị: Xác thực khuôn mặt
 | 4 | Hướng dẫn  | 
Label
 | 
Auto action
 | 
--
 | 
--
 | 
Hướng dẫn xác thực: 

• Nội dung được fix tại Client: "Đưa mặt vào giữa khung hình"
 | 5 | Vùng chụp ảnh và % hoàn thành | 
Capture
 | 
View
 | 
--
 | 
--
 | 
• Tự động thực hiện quét ảnh khuôn mặt theo hướng dẫn thực hiện
• Hiển thị vòng tròn xanh tương ứng với % hoàn tất
• Trong quá trình chụp ảnh, nếu khuôn mặt thoát khỏi vùng định vị khuôn mặt (vòng tròn) thì reset quá trình khuôn mặt và lấy ngẫu nhiên các hướng dẫn khác để thực hiện xác thực khuôn mặt
• Yêu cầu chụp 1 ảnh xa
 | 6 | Hướng dẫn hành động cần thực hiện | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• 
Hiển thị theo nhận diện khuôn mặt, thông báo động theo lỗi SDK nhận diện 

• Đưa khuôn mặt vào giữa khung hình
• Giữ thiết bị ổn định 
• ...
• Hoàn thành 
 | 7 | Hoàn thành | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Hiển thị khi Facepay thành công
• Tự động chuyển sang MH4/MH 3.1 (tùy vào PTXT của khách hàng)
 | 8 | Xác thực Facepay thất bại
 | 9 | Quay lại | Button (icon) | Click | -- | -- | 
• Mặc định: enable
• Khi click: quay lại MH2. Cài đặt mã PIN
 | 10 | Tiêu đề  | Label | ReadOnly | -- | -- | Hiển thị: Kết quả xác thực
 | 11 | 
Nội dung
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
• Fix Client
• Ảnh chân dung không hợp lệ. Vui lòng thực hiện lại 
 | 12 | 
Ảnh chụp thẳng khuôn mặt
 | 
Picture/ icon
 | 
Readonly
 | 
--
 | 
--
 | 
• Icon lỗi và hình ảnh chụp chân dung do SDK trả
• Cho phép click xem ảnh đã chụp 
 | 13 | 
Ghi chú
 | 
Label
 | 
Click
 | 
--
 | 

 | 
• Xác thực không thành công.
• Trả mã lỗi tương ứng từ FacePay server trả về.
 | 14 | 
Thực hiện lại
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình chụp khuôn mặt

##### MH3.1. MH nhập mã PIN softOTP (PTXT = SoftOTP)

##### MH3.2. Xác thực giao dịch (PTXT = SoftOTP)

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực bằng Soft OTP>

##### MH4.1. MH nhập mã OTP (PTXT = SMS OTP) (default)

##### MH4.2. MH nhập mã OTP (PTXT = SMS OTP)

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực GD bằng SMS OTP>

##### MH5.1. Trường hợp Đã thu thập STH + GTTT hết hạn
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Thông báo | Text | Read Only | -- | -- | Hiển thị thông báo: "Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học để tiếp tục thực hiện giao dịch."
 | 2 | Hủy | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: đóng popup, quay lại MH cài đặt mã Pin
 | 3 | Đồng ý | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: điều hướng vào luồng thu thập STH - MH7. Vào luồng của SDK thu thập STH
 (tham khảo )

##### MH5.2. Trường hợp Chưa thu thập STH 
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Thông báo | Text | Read Only | -- | -- | Hiển thị thông báo: "Yêu cầu cài đặt mã Pin cần được xác thực bằng Facepay. Quý khách vui lòng đăng ký “Thu thập sinh trắc học” để tiếp tục thực hiện giao dịch"
 | 2 | Hủy | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: đóng popup, quay lại MH cài đặt mã Pin
 | 3 | Đồng ý | Button | Click | -- | -- | 
• Mặc định: enable
• Khi click: điều hướng vào luồng thu thập STH - MH7. Vào luồng của SDK thu thập STH
 (tham khảo )

##### MH8. Kết quả
 | 1 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | Hiển thị: Quý khách cài đặt mã PIN thẻ thành công.
 | 3 | Đóng | Button | 
Click
 | 
--
 | 
--
 | Khi click: Đóng popup, điều hướng về MH Danh sách thẻ

---

#### 36.5.2. User Action Flow - Cài đặt PIN thẻ

> **Page ID:** `895168969` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/895168969

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Link Jira
 | 
  
 | A | 
 
 | 
 | 
Tạo mới tài liệu
 | V.1.0 | 

Mục lục

### 1/ Mô tả Usecase
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn | Use Case Name | Cài đặt mã Pin
 | Use Case ID | --
 | Use Case Description | Khách hàng sử dụng Mobile Banking để thực hiện cấp mới hoặc đổi mã PIN thẻ Credit. Hệ thống tiếp nhận, xác thực khác hàng (Facepay + SMS OTP/Facepay + Soft OTP), xử lý yêu cầu và ghi nhận giao dịch cài đặt mã Pin thẻ trên Báo cáo Quản lý thẻ 
 | Actor | Khách hàng (KH), MB App, MB server, Backoffice, Bank
 | Priority | Medium
 | Trigger | Khách hàng chọn chức năng "Dịch vụ thẻ" → chọn "Cài đặt mã Pin"
 | 
Pre-Condition
 | 
• Khách hàng đã đăng nhập Mobile Banking thành công
• Khách hàng đã Kích hoạt thẻ thành công trên Mobile Banking
• Thẻ ở trạng thái = Hoạt động (card status = Active (A))
 | Post-Condition | 
• Khách hàng cài đặt mã Pin thẻ thành công
• Hệ thống ghi nhận giao dịch giao dịch Cài đặt mã Pin thẻ trên BackOffice
 | Exception Flow | 
• Cài đặt mã Pin không hợp lệ (lỗi validate)
• Khách hàng chưa thu thập STH 
• Khách hàng đã thu thập STH nhưng GTTT đã hết hạn
• Xác thực thất bại
• Lỗi hệ thống (không kết nối được/Timeout)
• STH: Sinh trắc học
• GTTT: Giấy tờ tùy thân
 | Basic Flow | 
1/ Khách hàng đăng nhập vào Mobile Banking → Chọn "Dịch vụ thẻ" 

2/ Khách hàng chọn thẻ tín dụng có trạng thái thẻ = Hoạt động → Chọn "Cài đặt mã Pin"

2/ Khách hàng nhập mã PIN thẻ 6 số và nhập lại mã PIN để xác nhận → Chọn "Tiếp tục"

3/ Hệ thống thực hiện xác thực yêu cầu Facepay kết hợp PTXT đã cài đặt gồm:

• Soft OTP
• SMT OTP
(Thứ tự ưu tiên PTXT luồng phi tài chính: tham khảo Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

4/ Hệ thống ghi nhận kết quả xử lý

Lưu ý: 

• Các yêu cầu Cài đặt mã PIN đều được ghi nhận tại Báo cáo quản lý thẻ (BO) (Tham khảo Báo cáo Quản lý thẻ - Link Update sau)
• Sau khi Facepay thành công: ghi nhận vào Báo cáo xác thực giao dịch Facepay (Tham khảo )
 | Bussiness rules | | 
 | ID BR | Nội dung
 | 1 | BR_01 | 
• Chỉ hiển thị chức năng Cài đặt mã Pin nếu trạng thái thẻ = "Hoạt động"
• 
card_status = Active (A)

 | 2 | BR_02 | Xác thực yêu cầu kết hợp với Facepay
 | 3 | BR_03 | Masking (Ẩn ký tự): Ký tự Pin phải được ẩn ngay lập tức dưới dạng dấu chấm (●) hoặc sao (*)
 | 4 | BR_04 | Kiểm tra trạng thái STH & trạng thái GTTT trước khi Facepay. Nếu chưa thu thập STH/Đã thu thập + GTTT hết hạn:
→ Yêu cầu thu thập lại STH mới đi tiếp cài đặt mã Pin

### 2/ Luồng sơ đồ

trueCài đặt mã Pinfalseautotoptrue1521169014

### 3/ Logic xử lý

##### MH1. Danh sách thẻ (trạng thái thẻ = Hoạt động)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Gọi API lấy danh sách thẻ (Chi tiết logic tham khảo tài liệu )
 | 2 | Click "Cài đặt mã Pin" | Hệ thống MB | Điều hướng đến MH Cài đặt mã Pin

##### MH2. Cài đặt mã PIN
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Click "Xác nhận" "Tiếp tục" | Hệ thống MB | 
1/ Thực hiện kiểm tra mã PIN khách hàng nhập trên màn hình:

• 
Không hợp lệ:
 | 1 | Trường hợp | 
Nội dung thông báo 
 | 
Xử lý (nếu có)          

 | 1 | Bỏ trống trường Nhập mã Pin | 
Quý khách vui lòng nhập mã Pin
 | 
 Hiển thị dưới ô input

 

 

 

 

 

 | 2 | Bỏ trống trường Nhập lại mã Pin | 
Quý khách vui lòng nhập lại mã Pin

 | 3 | Nhập không đủ 06 ký tự số của trường Nhập mã Pin | 
Quý khách vui lòng nhập mã Pin bao gồm 6 ký tự số

 | 4 | Nhập không đủ 06 ký tự số của trường Nhập lại mã Pin | 
Quý khách vui lòng nhập lại mã Pin bao gồm 6 ký tự số

 | 5 | Nhập 06 ký tự số không trùng nhau của 2 trường | 
Mã Pin không trùng nhau. Quý khách vui lòng kiểm tra lại

 | 6 | Nhập 06 ký tự số là dãy số tiến liên tiếp | 
Mã Pin không được phép là các ký tự liên tiếp. Quý khách vui lòng kiểm tra lại

 | 7 | Nhập 06 ký tự số là dãy số trùng nhau | 
Mã Pin không được phép là các ký tự trùng nhau. Quý khách vui lòng kiểm tra lại

• Hợp lệ: chuyển sang 2
2/ Kiểm tra tham số REQUIRE_FACEPAY (ON/OFF): (dùng để xác định loại giao dịch của khách hàng có cần phải thực hiện Facepay hay không. Áp dụng cho mọi giao dịch trên MB (GD Tài chính/Phi tài chính)

• Nếu REQUIRE_FACEPAY = OFF → Trả client cờ Require_facepay = 0
• Nếu REQUIRE_FACEPAY = ON → Trả client cờ Require_facepay = 1
3/ Kiểm tra PTXT:

• Trường hợp KH có cài đặt Soft OTP
• Nếu KH đã xác thực đủ (n) GD tài chính bằng SMS OTP → Trả PTXT Soft OTP
• Nếu KH chưa xác thực đủ (n) GD tài chính bằng SMS OTP → Trả PTXT SMS OTP
• Nếu Soft OTP của KH đang bị Lock/Auto Lock → Trả PTXT SMS OTP
• Trường hợp KH không cài đặt Soft OTP → Trả PTXT SMS OTP
 | 4 | 
TH1: Require_facepay = 0

Không yêu cầu xác thực giao dịch bằng FacePay

 | 5 | 
 | Hệ thống MB | Điều hướng đến MH xác thực với PTXT tương ứng của khách hàng
 | 6 | 
TH2: Require_facepay = 1

Yêu cầu xác thực giao dịch bằng FacePay

 | 7 | 
 | Hệ thống MB | 
1/ Bật gọi ngầm SDK Facepay

2/ Gửi yêu cầu kiểm tra trạng thái STH đến SDK Facepay (Tham chiếu tài liệu )

3/ Nhận kết quả check trạng thái STH gồm các trường hợp sau:
 | 
 | Trường hợp | Xử lý
 | 1 | Đã thu thập STH + GTTT chưa hết hạn      | 
1/ Bật SDK Facepay (MH3. MH xác thực Facepay)

2/ Thực hiện Facepay & kiểm tra kết quả:

• Không thành công: Hiển thị thông báo tương ứng & không cho đi tiếp. Khi tắt thông báo, quay lại MH Cài đặt mã Pin thẻ
• Thành công: Hiển thị màn hình theo PTXT tương ứng 
 | 2 | Đã thu thập STH + Giấy tờ hết hạn | 
1/ Hiển thị popup thông báo: "Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học để tiếp tục thực hiện giao dịch"

• Hủy: Tắt popup, quay lại màn hình Cài đặt mã Pin
• Đồng ý: điều hướng đến SDK thu thập (Tham chiếu tài liệu 
2/ Thực hiện thu thập STH & kiểm tra kết quả:

• Không thành công: Hiển thị thông báo tương ứng & không cho đi tiếp. Khi tắt thông báo, quay lại MH Cài đặt mã Pin thẻ
• Thành công: Hiển thị thông báo tương ứng & quay lại MH Cài đặt mã Pin thẻ
 | 3 | Chưa thu thập STH | 
1/ Hiển thị popup thông báo: "Yêu cầu cài đặt mã Pin cần được xác thực bằng Facepay. Quý khách vui lòng đăng ký “Thu thập sinh trắc học” để tiếp tục thực hiện giao dịch"

• Hủy: Tắt popup, quay lại màn hình Cài đặt mã Pin 
• Đồng ý: điều hướng đến SDK thu thập (Tham chiếu tài liệu )
2/ Thực hiện thu thập STH & kiểm tra kết quả:

• Không thành công: Hiển thị thông báo tương ứng & không cho đi tiếp. Khi tắt thông báo, quay lại MH Cài đặt mã Pin
• Thành công: Hiển thị thông báo tương ứng & quay lại MH Cài đặt mã Pin 

##### MH3.1. MH nhập mã PIN softOTP (PTXT = SoftOTP)

##### MH3.2. Xác thực giao dịch (PTXT = SoftOTP)

##### MH4.1. MH nhập mã OTP (PTXT = SMS OTP) (default)

##### MH4.2. MH nhập mã OTP (PTXT = SMS OTP)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhập OTP và Click "Xác nhận" | Hệ thống MB | 
1/ Thực hiện xác thực giao dịch:

• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
• Nội dung SMS OTP gửi về SĐT khách hàng: Xac thuc Cài đặt mã Pin co ma OTP la {ma OTP}, co hieu luc trong {n} phut. 
(VD: Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc Cài đặt mã Pin co ma OTP là 123456, co hieu luc trong 1 phut)

• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
Validate thông tin:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: chuyển sang 2
2/ Kiểm tra OTP:

• Không hợp lệ: Trả kết quả lỗi cho MB Client
• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
• Hợp lệ: chuyển sang 3Ghi chú
Các trường hợp đã thực hiện Facepay thành công nhưng không đi hết luồng OTP (SoftOTP/SMS OTP):
 | 
 | Trường hợp | Xử lý (nếu có)
 | 1 | 
Không thực hiện xác thực SoftOTP/SMS OTP
 | 
• Không lưu log giao dịch
• Ghi nhận vào BC xác thực giao dịch Facepay (GD = Phi tài chính)
 | 2 | 
Gọi sang Bank lỗi gồm:

• Timeout
• Lỗi khác | 
Ghi nhận vào BC Quản lý thẻ gồm trạng thái:

• Time out
• Thất bại

2/ Chuyển tiếp yêu cầu cài đặt mã Pin thẻ sang bank (API pinCardSetUp)

 | 2 | 
 | Bank | 
Nhận yêu cầu, kiểm tra & thực hiện cài đặt mã PIN thẻ

Trả kết quả cho MB Server

 | 3 |   | Hệ thống MB | 
Nhận kết quả và xử lý:

• 
Không thành công:
 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi    | Xử lý (nếu có)
 | 1 | 
Time out

(Tham khảo )
 | Hệ thống tạm thời gián đoạn, xin quý khách vui lòng thử lại sau. | 
 
 | 
Ghi nhận giao dịch với trạng thái = Time out

 | 2 | 
Lỗi khác

(Tham khảo )
 | Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau. | 
resCode <> "000"          
 | 
Ghi nhận giao dịch với trạng thái = Thất bại

• Thành công: ghi nhận giao dịch thành công & hiển thị thông báo: "Quý khách cài đặt mã PIN thẻ thành công." 
Lưu ý: Các trường hợp đều ghi nhận vào Báo cáo quản lý thẻ - Giao dịch Cài đặt mã Pin

Trạng thái giao dịch gồm:

• Thành công
• Thất bại
• Time out

---

### 36.6. 5. Lịch sử giao dịch Credit

> **Page ID:** `895156679` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/895156679

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.6.1. 5.2. Flow and Screen Action Flow - Lịch sử giao dịch Credit

> **Page ID:** `895166081` · **Version:** 26
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/895166081

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader review
 | 
 
 | A |   | 
 | Tạo mới tài liệu | V1.0 | 

Mục lục

### 1/ Luồng màn hình

Link Mock-up:  

### 2/ Danh sách màn hình

##### MH1. Danh sách thẻ 

##### MH2. Lịch sử giao dịch thẻ tín dụng

##### MH3. Chi tiết 01 giao dịch

 

### 3/ Mô tả màn hình

##### MH1. Danh sách thẻ

Xem mô tả tại 1. Danh sách thẻ

##### MH2. Lịch sử giao dịch thẻ tín dụng
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Readonly
 | 
--
 | 
--
 | Lịch sử giao dịch
 | 2 | Nút back | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 3 | 
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

 | 4 | 
Hình ảnh thẻ
 | 
Image
 | 
Readonly
 | 
--
 | 
--
 | 
Mã thẻ được lựa chọn

Bao gồm thông tin: 

• Loại thẻ (Tín dụng / Ghi nợ)
• Mã thẻ
• Tên người dùng
• Eye-mask () → xem thông tin chi tiết thẻ
 | 5 | 
Tiêu đề thẻ
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
<Loại thẻ>

<Mã thẻ được lựa chọn>

Tiêu đề thẻ bao gồm thông tin:

• Logo thẻ
• Số thẻ
• Tên chủ thẻ
 | 6 | 
Tiêu đề loại thẻ chính / phụ
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
<Thẻ chính/phụ> / <Trạng thái thẻ>

 | 7 | Khoảng thời gian | Label | ReadOnly | 
 | 
 | 

 | 8 | Ghi chú | Label | ReadOnly | -- | -- | Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 1 năm
 | 9 | Dữ liệu thời gian | Button | Click | -- | -- | 
Bao gồm:

• 1 tháng
• 2 tháng
• 3 tháng
• Khác
Nhấn "Khác": Hiển thị vùng tìm kiếm, cho phép chọn khoảng thời gian từ ngày, đến ngày

Cho phép chọn Button khác

Mặc định ban đầu chọn button 1 tháng

 | 10 | Vùng tìm kiếm từ ngày - đến ngày
 | 11 | Từ ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Từ ngày phải nhỏ hơn hoặc bằng Đến ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng (không được chọn thời điểm quá 01 năm, tức dữ liệu lưu trữ có thể tra cứu luôn nằm trong khoảng T-365 đến T (thời điểm hiện tại). 

Ví dụ: nếu thời điểm ngày hiện tại T = 31/07/2025 thì dữ liệu có thể tra cứu không lùi quá 31/07/2024 (T-365). Nếu lựa chọn Từ ngày: 31/07/2025, Đến ngày không được chọn quá 31/10/2025 (3 tháng))

Định dạng dd/MM/yyyy

Mặc định ngày T-1 

 | 12 | Đến ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Đến ngày phải lớn hơn hoặc bằng Từ ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng 

(không được chọn thời điểm quá 01 năm, tức dữ liệu lưu trữ có thể tra cứu luôn nằm trong khoảng T-365 đến T (thời điểm hiện tại). 

Ví dụ: nếu thời điểm ngày hiện tại T = 31/07/2025 thì dữ liệu có thể tra cứu không lùi quá 31/07/2024 (T-365). Nếu lựa chọn Từ ngày: 31/07/2025, Đến ngày không được chọn quá 31/10/2025 (3 tháng))

Định dạng dd/MM/yyyy

Mặc định ngày T

 | 13 | Tìm kiếm | Button | Click | -- | -- | Nhấn button Tìm kiếm sẽ ẩn/đóng vùng tìm kiếm theo ngày
 | 14 | Lịch sử | Label | Readonly | 
 | 
 | 

 | 15 | 
Tab dữ liệu
 | 
Tab
 | 
Select
 | 
--
 | 
--
 | 
Có 3 tab: Toàn bộ, Tiền vào, Tiền ra. Dữ liệu hiển thị gồm các thông tin sau:

• Thời gian giao dịch: Hiển thị thời gian tương ứng thực hiện giao dịch. Định dạng hiển thị dd/mm/yyyy hh:mm
• Nội dung giao dịch: Hiển thị cắt chuỗi trong nội dung giao dịch (Hiển thị đảm bảo trên 1 dòng dữ liệu, dữ liệu thiếu hiển thị bằng dấu “…”)
• Số tiền giao dịch: Tương ứng với số tiền thực hiện trong giao dịch. Định dạng tiền vào: màu xanh và hiển thị dấu cộng đằng trước; Định dạng tiền ra: màu đỏ và hiển thị dấu trừ đằng trước.
• Khi nhấn vào 1 giao dịch bất kì, hiển thị màn hình chi tiết giao dịch
Mặc định tại tab: Toàn bộ.

Cho phép chọn tab khác. 

• Tab Tiền vào: Tổng hợp danh sách các giao dịch có định dạng tiền vào → Map API trường tiền vào: "operationDirection":" credit "
• Tab Tiền ra: Tổng hợp danh sách các giao dịch có định dạng tiền ra → Map API trường tiền ra "operationDirection":"debit"
 | 16 | 
Danh sách giao dịch
 | 
List
 | 
View
 | 
--
 | 
--
 | 
Mặc định hiển thị danh sách giao dịch trong 1 tháng gần nhất (30 ngày gần nhất)

Hiển thị danh sách các giao dịch sắp xếp dữ liệu mới nhất lên đầu. Phân trang 10 bản ghi/ trang 

(Map API trường số bản ghi - 

"limitRecord":’ "10’

"pos":"0") 

Cho phép KH xem dữ liệu dạng loadmore (chi tiết tham khảo logic xử lý)

Cho phép chọn lại khoảng thời gian hiển thị lịch sử giao dịch.

Trường hợp không có giao dịch nào, hiển thị label thông báo: Chưa có giao dịch phát sinh

##### MH3. Chi tiết 01 giao dịch
 | 
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

 | 1 | 
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

 | 2 | 
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
Quay trở lại màn hình lịch sử giao dịch

 | 3 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Trường "Ultrano"

 | 4 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Trường "transDate"

 | 5 | 
Số tiền giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Trường "amount"

 | 6 | 
Tiền vào/Tiền ra
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Trường Tiền vào: "operationDirection: credit"

Định dạng Tiền vào: hiển thị dấu cộng đằng trước số tiền giao dịch

Trường Tiền ra: "operationDirection: debit"

Định dạng Tiền ra: hiển thị dấu trừ đằng trước số tiền giao dịch.

 | 7 | 
Nội dung giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Trường "transRemark"

---

#### 36.6.2. 5.3. User Action Flow - Lịch sử giao dịch Credit

> **Page ID:** `896729458` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/896729458

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader review
 | 
 
 | A |   | 
 | Tạo mới tài liệu | V1.0 | 

Mục lục

### 1/ Tóm tắt Use Case

 | Use Case Name | Lịch sử giao dịch Credit
 | Use Case ID | UC-CardHistory
 | Use Case Description | 
Là người dùng, tôi muốn thực hiện tra cứu lịch sử giao dịch thẻ tín dụng, thẻ ghi nợ

 | Actor | 
Khách hàng, MB App Client, MB App Server, Bank Server 

 | Priority | Medium
 | Trigger | 
Khách hàng thực hiện truy cập chức năng Lịch sử giao dịch tại thẻ tín dụng đang được chọn

 | 
Pre-Condition
 | 
• Khách hàng đã phát hành thẻ tín dụng, thẻ ghi nợ hoặc thẻ kép tại ngân hàng Coopbank 
• Khách hàng đăng nhập Coop-bank Mobile Banking thành công
• Khách hàng lựa chọn thẻ tín dụng cần xem lịch sử giao dịch
 | Post-Condition | 
Khách hàng thực hiện tra cứu các giao dịch qua thẻ tín dụng đã lựa chọn thành công

 | Basic Flow | 
1/ Khách hàng chọn thẻ Hoạt động/ Khóa

2/ Khách hàng chọn Lịch sử giao dịch 

3/ Hệ thống hiển thị màn hình Lịch sử giao dịch

4/ Khách hàng thực hiện tra cứu giao dịch theo thời gian: 1 tháng, 2 tháng, 3 tháng hoặc theo khoảng thời gian tùy chọn 

5/ Hệ thống hiển thị danh sách giao dịch 

6/ Khách hàng nhấn vào 1 giao dịch 

7/ Hệ thống hiển thị màn hình chi tiết giao dịch

 | Alternative Flow | 
<Không có>

 | Exception Flow | 
• Lỗi khi truy vấn danh sách / chi tiết giao dịch → 
• Thông báo lỗi: "Lỗi hệ thống. Quý khách vui lòng thực hiện lại tra cứu giao dịch"
• Nếu không có dữ liệu từ truy vấn, hiện màn hình với thông báo: "Chưa có dữ liệu phát sinh"
• Nếu Khách hàng truy vấn không đúng quy định giới hạn thời gian tìm kiếm, thông báo: "Thời gian tra cứu không hợp lệ"
 | Bussiness Rules | 
BR1: Chức năng lịch sử giao dịch được thực hiện với thẻ có trạng thái Hoạt động, Khóa do khách hàng, Khóa bởi GDV

BR2: Hiển thị với cả thẻ chính và thẻ phụ

BR3: Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 01 năm

BR4: Lãi thu trên tài khoản sẽ được đưa vào Lịch sử giao dịch của thẻ chính

BR5: Phí thường niên và phí giao dịch tương ứng của Thẻ chính/Thẻ phụ sẽ được đưa vào Lịch sử giao dịch của thẻ đó

 | Non-Funtional Requiremnt | 
<Không có>

### 2/ Luồng xử lý
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
Truy cập Lịch sử giao dịch thẻ được chọn

 

 

 

 
 | Khách hàng  | 
Khách hàng truy cập chức năng Lịch sử giao dịch tại thẻ được chọn 

 | Hệ thống MB | Gửi yêu cầu lấy danh sách giao dịch ở thẻ được chọn
 | Bank  | Nhận yêu cầu, xử lý và phản hồi kết quả tương ứng, ngoài các giao dịch của Khách hàng, bao gồm cả các giao dịch:
- Lãi thu trên tài khoản 
- Phí thường niên và phí giao dịch tương ứng của Thẻ chính/Thẻ phụ

 | Hệ thống MB | 
Nhận phản hồi từ Bank và xử lý tương ứng

• Không hợp lệ: | Trường hợp | Thông báo lỗi | Ghi chú
 | Lỗi hệ thống | Lỗi hệ thống. Quý khách vui lòng thực hiện lại tra cứu giao dịch | 

 | Chưa có dữ liệu giao dịch | Chưa có dữ liệu giao dịch phát sinh | 

• Hợp lệ: Phản hồi kết quả hợp lệ 
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
2

 | 
Tra cứu lịch sử giao dịch theo khoảng thời gian nhất định

 

 

 

 
 | Khách hàng  | 
Khách hàng chọn thời gian để tra cứu trên các tab lọc hoặc điền khoảng thời gian nhất định (Không được quá 03 tháng và thời gian chọn không được quá 01 năm)

 | Hệ thống MB | Gửi yêu cầu lấy danh sách giao dịch ở thẻ được chọn theo thời gian tra cứu
 | Bank  | 
Nhận yêu cầu, xử lý và phản hồi kết quả tương ứng, ngoài các giao dịch của Khách hàng, bao gồm cả các giao dịch:

- Lãi thu trên tài khoản 
- Phí thường niên và phí giao dịch tương ứng của Thẻ chính/Thẻ phụ

• Không hợp lệ: | Trường hợp | Thông báo lỗi | Xử lý
 | Lỗi hệ thống | Lỗi hệ thống. Quý khách vui lòng thực hiện lại tra cứu giao dịch | 

 | Chưa có dữ liệu giao dịch | Chưa có dữ liệu giao dịch phát sinh | 

 | Tra cứu không hợp lệ theo quy định | Thời gian tra cứu không hợp lệ | 
Thông báo xuất hiện dưới các trường Từ ngày ... Đến ngày

• Hợp lệ: Phản hồi kết quả hợp lệ
 | Hệ thống MB | 
Nhận phản hồi từ Bank và xử lý tương ứng

• Không hợp lệ: Phản hồi thông báo lỗi tương ứng 
• Hợp lệ: Phản hồi danh sách giao dịch của thẻ được chọn theo thời gian tra cứu đến MB App Client 
• Hiển thị: 10 bản ghi/ trang
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
3

 | 
Chọn xem chi tiết 01 giao dịch chi tiết

 

 

 

 
 | Khách hàng  | 
Khách hàng chọn 01 giao dịch chi tiết trong danh sách

 | Hệ thống MB | 
Điều hướng đến MH3. Chi tiết 01 giao dịch

---

### 36.7. 6. Thanh toán dư nợ

> **Page ID:** `899055669` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/899055669

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

#### 36.7.1. Định nghĩa Trạng thái Phase giao dịch và Trạng thái giao dịch thanh toán dư nợ thẻ tín dụng

> **Page ID:** `905380587` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/905380587

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A |   | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Tạo mới tài liệu
 | V1 | 

Mục lục
none

### 1/ Sơ đồ trạng thái phase và trạng thái giao dịch 

### 2/ Mô tả chi tiết
 | TT | Trigger | Mô tả xử lý  | Trạng thái giao dịch cuối cùng 
 | Giai đoạn Khởi tạo  |  
 | 1 | 
Khách hàng nhập thông tin giao dịch trên mobile app và bấm Tiếp tục
 | 
Ghi nhận giao dịch với trạng thái: Khởi tạo thành công (Giai đoạn khởi tạo đã được hoàn thành và đến màn hình xác nhận giao dịch)
 | 
Khởi tạo thành công

 | Giai đoạn Xác thực  |  
 | 2 | Khách hàng thực hiện kiểm tra thông tin trên màn hình và bấm Xác nhận  | 
Ghi nhận trạng thái giao dịch: Chờ xác thực (Thời điểm KH đang ở màn hình xác thực giao dịch)

Khách hàng thực hiện xác thực giao dịch thành công, MB App Server gọi API createCardPayment (5)
 | 
Chờ xác thực

 | 
Giai đoạn Hạch toán 
 | 
 

 | 3 | MB App Server gọi API createCardPayment (5). Nhận mã lỗi thành công | 
Ghi nhận giao dịch với trạng thái: Giao dịch thành công (Giao dịch hạch toán trừ tiền thàn công tại bank)

MB App Server gọi API createCardPaymentSV (6), chuyển sang giai đoạn gạch nợ 
 | 
Giao dịch thành công

 | 4 | MB App Server gọi API createCardPayment (5). Nhận mã lỗi thất bại  | 
Ghi nhận giao dịch với trạng thái: Hạch toán thất bại (Thất bại trong việc bank hạch toán trừ tiền tk nguồn)
 | 
Hạch toán thất bại

 | 5 | MB App Server gọi API createCardPayment (5). Nhận mã lỗi TO | 
MB App Server gọi API createCardPaymentRevl (7), chuyển sang giai đoạn hoàn tiền 
 | 
--

 | 
Giai đoạn Gạch nợ 
 | 
 

 | 6 | MB App Server gọi API createCardPaymentSV (6). Nhận mã lỗi thành công | 
Ghi nhận giao dịch với trạng thái: Gạch nợ thành công (Gạch nợ thành công cho khách hàng)
 | 
Gạch nợ thành công

 | 7 | MB App Server gọi API createCardPaymentSV (6). Nhận mã lỗi thất bại  | 
Ghi nhận giao dịch với trạng thái: Gạch nợ thất bại (Thất bại trong việc gạch nợ tại hệ thống)
 | 
Gạch nợ thất bại

 | 8 | MB App Server gọi API createCardPaymentSV (6). Nhận mã lỗi TO | 
Ghi nhận giao dịch với trạng thái: Giao dịch nghi vấn (Không nhận được kết quả của phase giao dịch là thành công hay thất bại)
 | 
Giao dịch nghi vấn

 | 
 Giai đoạn Hoàn tiền 
 | 
 

 | 9 | MB App Server gọi API createCardPaymentRevl (7). Nhận mã lỗi thành công | 
 Ghi nhận giao dịch với trạng thái: Hoàn tiền thành công (Giao dịch đã trừ tiền tại bank nhưng chưa gạch nợ được cho KH, tiến hành hoàn tiền cho KH thành công )
 | 
Hoàn tiền thành công

 | 10 | MB App Server gọi API createCardPaymentRevl (7). Nhận mã lỗi thất bại | 
 Ghi nhận giao dịch với trạng thái: Hoàn tiền thất bại (Giao dịch đã trừ tiền tại bank nhưng chưa gạch nợ được cho KH, tiến hành hoàn tiền cho KH thất bại )
 | 
Hoàn tiền thất bại

 | 11 | MB App Server gọi API createCardPaymentRevl (7). Nhận mã lỗi TO | 
Ghi nhận giao dịch với trạng thái: Giao dịch nghi vấn (Không nhận được kết quả của phase giao dịch là thành công hay thất bại)
 | 
Giao dịch nghi vấn

---

#### 36.7.2. Flow&Action screen - Thanh toán dư nợ thẻ tín dụng

> **Page ID:** `899055683` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/899055683

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A |   | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Tạo mới tài liệu
 | V1 | 

 | 
 
 | M | 
 
 | V1 | 
Điều chỉnh giao diện: 

• Màn hình khởi tạo
• "Thông tin thụ hưởng" → "Thông tin thẻ tín dụng
• Label Dư nợ hiện tại trong cụm thông tin thẻ tín dụng 
• Màn hình Xác nhận giao dịch: Hiển thị drop-down list PTXT cho khách hàng lựa chọn 
• Màn hình kết quả: Bổ sung lưu ý: "Giao dịch của quý khách sẽ được cập nhật trong n giờ". (n được cấu hình trên BO) | V2 | 

Muc lục
none

### 1/ Danh sách màn hình

##### MH1: <Màn hình khởi tạo giao dịch thanh toán thẻ tín dụng>

##### MH2: <Màn hình xác nhân giao dịch thanh toán thẻ tín dụng>

##### MH3: <Màn hình xác thực giao dịch thanh toán thẻ tín dụng>

##### MH4: <Màn hình kết quả giao dịch thanh toán thẻ tín dụng> 

### 2/ Mô tả màn hình

##### MH1: <Màn hình khởi tạo giao dịch thanh toán thẻ tín dụng>
 | TT | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nút quay lại | Button  | Nhấn | -- | -- | Điều hướng về màn hình trước đó
 | 2 | Tiêu đề màn hình | Label  | ReadOnly | -- | -- | Hiển thị tên chức năng hiện tại: Thanh toán thẻ tín dụng.
 | 3 | Tài khoản nguồn | Dropdown | Chọn | Có  | -- | 
• Hiển thị mặc định tài khoản thanh toán mặc định 
• Nếu không có tài khoản than toán mặc định thì hiển thị mặc định tài khoản than toán đầu tiên trong danh sách do bank trả về 
• Hiển thị thông tin gồm: 
• Số tài khoản
• Số dư = Số dư khả dụng - Hạn mức thấu chi được cấp cho KH (Lưu ý hiển thị số dư = availBalance - todAmount)
• Đơn vị tiền tệ 
Lưu ý: Xử lý như nghiệp vụ lấy danh sách tài khoản nguồn hiện tại trên app (phần chuyển tiền, thanh toán,....)

 | 
Thông tin thẻ tín dụng 

 | 4 | Số thẻ thụ hưởng | Label  | ReadOnly | -- | -- | 
Chỉ hiển thị 6 số đầu và 4 số cuối, mask các số ở giữa

 | 5 | Tên chủ thẻ | Label  | ReadOnly | -- | -- | Hiển thị tên chủ thẻ tương ứng với số thẻ.
 | 6 | 
Dư nợ hiện tại

currentAmount
 | Label  | ReadOnly | -- | -- | Hiển thị tổng dư nợ hiện tại của thẻ (VND).
 | 
Thông tin thanh toán 

Lưu ý: 

Nghiệp vụ bank yêu cầu ẩn/hiện các lựa chọn thanh toán theo tham số cấu hình trên BO. MB App Client gọi mid 559 Lấy danh sách cấu hình (gọi sau login), truyền tên tham số → MB App Server trả về giá trị tương ứng của tham số 

 | 7 | 
Dư nợ tối thiểu kỳ sao kê

unpaidMinAmountDue
 | Radio Button | Chọn | Có | N/A | 
Hiển thị số tiền tối thiểu đang nợ trong kỳ (Số tiền do Bank trả về)

Ẩn/hiện option theo tham số được cấu hình tại mục Hệ thống → Tham số → Cấu hình tham số trên BO (Tham chiếu tài liệu: )

Tên tham số: CARD_UNPAID_MIN_AMOUNT_DUE bao gồm 2 giá trị: 1: hiển thị, 0: không hiển thị 

 | 8 | 
Toàn bộ dư nợ kỳ sao kê

unpaidStatementAmount
 | Radio Button | Chọn | Có | N/A | 
Hiển thị số tiền đang nợ trong kỳ (Số tiền do Bank trả về)

Ẩn/hiện option này theo tham số được cấu hình tại mục Hệ thống → Tham số → Cấu hình tham số trên BO (Tham chiếu tài liệu: )

Tên tham số: CARD_UNPAID_STATEMENT_AMOUNT  bao gồm 2 giá trị: 1: hiển thị, 0: không hiển thị 

 | 9 | 
Toàn bộ dư nợ hiện tại

currentAmount
 | Radio Button | Chọn | Có | N/A | 
Hiển thị toàn bộ dư nợ hiện tại (Số tiền do Bank trả về)

Ẩn/hiện option này theo tham số được cấu hình tại mục Hệ thống → Tham số → Cấu hình tham số trên BO (Tham chiếu tài liệu: )

Tên tham số: CARD_CURRENT_AMOUNT bao gồm 2 giá trị: 1: hiển thị, 0: không hiển thị 

 | 10 | Số tiền khác | Radio Button + Textbox | Chọn + Nhập | Có  | 15 | 
• Cho phép nhập số tiền thanh toán khác.
• 
Hiển thị ngăn cách hàng nghìn bằng dấu “,”

• Độ dài 15 ký tự bao gồm cả dấu “, “
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Không nhập số bắt đầu bằng số 0
• Focus ô Số tiền → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
• Số tiền lớn hơn dư nợ hiện tại → Thông báo lỗi: Số tiền không được vượt quá dư nợ hiện tại, vui lòng nhập lại" 
Ẩn/hiện option này theo tham số được cấu hình tại mục Hệ thống → Tham số → Cấu hình tham số trên BO (Tham chiếu tài liệu: ) 

Tên tham số: CARD_OTHER_AMOUNT bao gồm 2 giá trị: 1: hiển thị, 0: không hiển thị 

Hiển thị note Tối đa: Số tiền = Toàn bộ dư nợ hiện tại

 | 11 | Nội dung giao dịch | Textbox | ReadOnly | -- | -- | Mặc định: Thanh toan the tin dung và không cho phép sửa
 | 12 | Nút Tiếp tục | Button | Nhấn | Có | N/A | 
• Kiểm tra hợp lệ dữ liệu trước khi chuyển sang màn hình xác nhận.
• Khách hàng bắt buộc phải chọn một option thanh toán thẻ tín dụng trên giao diện. Nếu bỏ trống cả 04 hình thức thanh toán →  Thông báo lỗi: "Vui lòng chọn một hình thức thanh toán"

##### MH2: <Màn hình xác nhân giao dịch thanh toán thẻ tín dụng>
 | STT | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nút quay lại | Button / Icon | Nhấn | Không | - | Cho phép người dùng quay lại màn hình trước đó.
 | 2 | Tiêu đề màn hình | Label  | ReadOnly | -- | -- | Hiển thị tên màn hình: "Xác nhận giao dịch".
 | 3 | Thông báo hướng dẫn | Label  | ReadOnly | -- | -- | 
Hướng dẫn người dùng kiểm tra lại thông tin giao dịch trước khi xác nhận: "Quý khách vui lòng kiểm tra thông tin giao dich đã khởi tạo" 

 | 4 | Tài khoản nguồn | Label  | ReadOnly | -- | -- | 
• Hiển thị số tài khoản dùng để trích tiền.
• Dữ liệu lấy từ màn hình trước, không cho chỉnh sửa.
 | 5 | Số thẻ thụ hưởng | Label  | ReadOnly | -- | -- | 
• Dữ liệu được lấy từ màn hình trước đó 
• Hiển thị số thẻ người nhận, được mask (****) để bảo mật.
• Chỉ hiển thị 6 số đầu và 4 số cuối. Mask các ký tự còn lại 
 | 6 | Tên chủ thẻ | Label  | ReadOnly | -- | -- | 
• Hiển thị tên chủ thẻ tương ứng với số thẻ thụ hưởng.
• Dữ liệu được lấy từ màn hình trước, không cho chỉnh sửa
 | 7 | Số tiền | Label  | ReadOnly | -- | -- | 
• Hiển thị số tiền giao dịch.
• Dữ liệu được lấy từ màn hình trước, không cho chỉnh sửa
 | 8 | Nội dung giao dịch | Label  | ReadOnly | -- | -- | 
• Mô tả nội dung chuyển tiền/thanh toán.
• Dữ liệu kế thừa từ màn hình trước.
 | 
 | Chọn phương thức xac thực | Drop-down list | Click | -- | -- | 
Cho phép khách hàng chọn 1 phương thức xác thực giao dịch trong danh sách PTXT 

Danh sách PTXT hiển thị dựa theo PTXT KH đã cài đặt 

Ví dụ: 

• Khách hàng đã cài đặt SMS OTP và TouchID → Hiển thị 2 lựa chọn này
• Khách hàng đã cài đặt SMS OTP, soft OTP, FaceID → Hiển thị 3 lựa chọn này
 | 9 | Nút Xác nhận | Button | Nhấn | -- | - | 
• Người dùng xác nhận thực hiện giao dịch.
• Chuyển sang bước xác thực

##### MH3: <Màn hình xác thực giao dịch thanh toán thẻ tín dụng>

Tham chiếu tài liệu:

• Soft OTP: 
• SMS OTP: 
• TouchID/FaceID: 
##### MH4: <Màn hình kết quả giao dịch thanh toán thẻ tín dụng> 
 | STT | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nút Trang chủ | Button / Icon | Nhấn | Không | - | Điều hướng nhanh về màn hình Home 
 | 2 | Tiêu đề màn hình | Label  | ReadOnly | -- | -- | Hiển thị tiêu đề: "Kết quả giao dịch".
 | 3 | Logo / Banner | Image | Không thao tác | Không | - | Hiển thị logo ngân hàng Coopbank
 | 4 | Icon trạng thái thành công | Icon / Image | ReadOnly | -- | -- | 
• Biểu tượng "Check" (màu xanh lá) thể hiện giao dịch thành công
• Biểu tượng "Cross" (màu đỏ) thể hiện giao dịch thất bại 
 | 5 | Thông báo trạng thái | Text | Không thao tác | Có | - | 
Thông báo kết quả giao dịch và lưu ý

Giao dịch của quý khách sẽ được cập nhật trong n giờ (n được cấu bình trên BO)

PAY_CARD_TIME: giá trị tham số n là số tự nhiên, đơn vị giờ 

 | 6 | Số tiền giao dịch | Label  | ReadOnly | -- | -- | 
• Hiển thị số tiền giao dịch
• Dữ liệu được lấy từ màn hình trước 
 | 7 | 
Thời gian giao dịch

transDate
 | Label  | ReadOnly | -- | -- | 
• Thời điểm hệ thống ghi nhận giao dịch thành công.
• Định dạng: dd/MM/yyyy HH:mm.
 | 8 | Số thẻ thụ hưởng | Label  | ReadOnly | -- | -- | 
• Hiển thị số thẻ người nhận (được mask).
• Dữ liệu được lấy từ màn hình trước 
 | 9 | Tên chủ thẻ | Label  | ReadOnly | -- | -- | 
• Tên chủ thẻ tương ứng với số thẻ thụ hưởng
• Dữ liệu được lấy từ màn hình trước
 | 10 | 
Mã giao dịch

transRefNo
 | Label  | ReadOnly | -- | -- | 
• Mã định danh duy nhất của giao dịch.
• Dữ liệu do bank trả về 
 | 11 | Nội dung giao dịch | Label  | ReadOnly | -- | -- | 
• Hiển thị nội dung giao dịch 
• Dữ liệu được lấy từ màn hình trước
 | 12 | Nút Chia sẻ | Button / Icon | Nhấn | Không | - | Cho phép chia sẻ kết quả giao dịch qua các ứng dụng khác.
Tham chiếu xử lý: 
 | 13 | Nút Lưu ảnh | Button / Icon | Nhấn | Không | - | Lưu ảnh chụp màn hình biên lai giao dịch.
Tham chiếu xử lý: 
 | 14 | Nút Tạo giao dịch mới | Button | Nhấn | Có | - | Điều hướng về màn hình khởi tạo giao dịch

---

#### 36.7.3. User Action Flow - Thanh toán dư nợ thẻ tín dụng

> **Page ID:** `899055686` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/899055686

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A | 
 
 | 
 | 
Tạo mới tài liệu 
 | V1 | 

Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Thanh toán dư nợ thẻ tín dụng
 | Use Case ID | UC_TTDUNO
 | Use Case Description | 
Là người dùng, tôi muốn thực hiện thanh toán dư nợ thẻ tín dụng thành công 

 | Actor | 
Khách hàng, MB App Client , MB App Server, Bank Server

 | Priority | Medium 
 | Trigger | 
Khách hàng truy cập tính năng Thanh toán thẻ ở màn hình dịch vụ thẻ 

 | 
Pre-Condition
 | 
• Khách hàng đăng nhập thành công 
• Khách hàng tồn tại thẻ tín dụng có dư nợ trên hệ thống
• Tài khoản nguồn của khách hàng có đủ số dư để thực hiện giao dịch
• Thẻ của khách hàng phải là thẻ chính có trạng thái hoạt động, khóa 
• Số dư tài khoản nguồn không được bao gồm thấu chi 
 | Post-Condition | 
1/ Khách hàng thực hiện thanh toán thẻ tín dụng thành công 

2/ Hệ thống hạch toán chính xác và ghi nhận giao dịch thanh toán thẻ tín dụng 

3/ Tài khoản nguồn bị trừ đúng số tiền giao dịch 

1. KH thực hiện lệnh chuyển tiền nội bộ thành công; 2. Tài khoản nguồn của KH bị trừ số tiền giao dịch (bao gồm phí nếu có); 3. Tài khoản thụ hưởng nhận được số tiền chuyển tương ứng (trừ phí nếu có); 4. Hệ thống MB ghi nhận hoạt động chuyển tiền vào [Activity Log]; 5. Hệ thống MB ghi nhận giao dịch chuyển tiền nội bộ vào [Transaction History]

 | Basic Flow | 
1/ Khách hàng truy cập vào tính năng thanh toán thẻ trên màn hình dịch vụ thẻ 

2/ Mobile App hiển thị thông tin thanh toán thẻ 

3/ Khách hàng thực hiện chọn/nhập thông tin thanh toán thẻ và bấm tiếp tục 

4/ Mobile App hiển thị màn hình xác nhận giao dịch 

5/ Khách hàng kiểm tra thông tin thanh toán và bấm Xác nhận giao dịch 

6/ Mobile App hiển thị màn hình xác thực giao dịch tương ứng mà khách hàng đã cài đặt trước đó 

7/ Khách hàng thực hiện xác thực giao dịch 

8/ Mobile App hiển thị màn hình kết quả giao dịch 

 | Alternative Flow | 
--

 | Exception Flow | 
• Tài khoản nguồn không đủ số dư → Thông báo lỗi: "Tài khoản không đủ số dư, quý khách vui lòng chọn tài khoản khác"
• Khách hàng nhập số tiền vượt quá dư nợ hiện tại → Thông báo lỗi: "Số tiền vượt quá dư nợ hiện tại, vui lòng nhập số tiền nhỏ hơn dư nợ hiện tại"
• Xác thực không hợp lệ → Thông báo lỗi: "OTP không hợp lệ, quý khách vui lòng thử lại"
• Lỗi hệ thống → Thông báo lỗi: "Lỗi hệ thống, quý khách vui lòng thử lại"
 | Bussiness Rules | 
• BR-01: Chỉ hiển thị tính năng Thanh toán thẻ dụng đối với các thẻ đủ điều kiện:
• Thẻ chính 
• Trạng thái thẻ Hoạt động, khóa do khách hàng và khóa do giao dịch viên 
• BR-02: Không dùng thấu chi để thanh toán thẻ tín dụng 
• BR-03: Đối với gia dịch thanh toán thẻ, không check module 2345 và không check hạn mức giao dịch 
• BR-04: Chỉ được phép thanh toán thẻ tín dụng cho chính mình 
• BR-05: Trường hợp khách hàng lựa chọn nhập số tiền khác. Cho phép nhập số tiền nhỏ hơn dư nợ tối thiểu của kỳ sao kê, không cho nhập số tiền lớn hơn dư nợ hiện tại 
• BR-06: Yêu cầu khách hàng xác thực theo PTXT đã được khách hàng cài đặt trước đó 
 | Non-Funtional Requiremnt | 
--

### 2/ Luồng xử lý

##### MH1: <Màn hình khởi tạo giao dịch thanh toán thẻ tín dụng>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Khởi tạo màn hình | 
Khách hàng
 | 
Khách hàng bấm vào tính năng Thanh toán thẻ tín dụng ở màn hình dịch vụ thẻ 

 | 
 | 
 | 
Mobile App 
 | 
Gửi yêu cầu lấy thông tin thẻ đến Bank Server API queryCard (Thông tin thẻ)
Mô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
 | {
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144"  
"cardId": "xxx",
}
 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | cardId | -
 | Response | 
 | 
{

"requestId": "xxxx",
  "referenceID": "xxx",
"cif": "0100000000144",
"cardNo": "970446345667899",

      "cardId": "xxx",

"accountCardNo": "01000xxxxxxx",

"accountNo": "01000xxxxxxx",
"statusCard": "A",

"deliveryStatus":"5",
"cardName": " NGUYENVAN B",
"cardType": "MainCard",

"product": "Credit",

cardProduct": "Thẻ Vip",
"limitAmount": "8000000",
"availAmount": "7000000",
"currentAmount":"1000000",

"amountStatement":"200000",
"minAmountDue":"100000",

"unpaidMinAmountDue":"100000",

"unpaidStatementAmount ":"100000",

"AutoCreditPaymentType":"A",
"branchIssName": "CN So giao dich",
"branchIssue": "01000",
"issueDate": "31/01/2025",
"expireDate": "31/12/2025",
"statementDate": "24/07/2025",
"dueDate": "31/07/2025",

"startDate": "21/09/2025",

"invoiceDate": "20/10/2025",
  "resCode": "000",
  "resDesc": "Success"

}

 | requestId | -
 | referenceID | -
 | cif | CIFNo của khách hàng
 | cardNo | Số thẻ không masked
 | cardId | -
 | accountCardNo | Tài khoản thẻ 
 | accountNo | Tài khoản thanh toán liên kết (chỉ trả về khi là debit card hoặc dual card)
 | statusCard | 
Trạng thái thẻ, bao gồm:

• Standby (S): Chờ kích hoạt
• Lock by Customer (C): Khỏa bởi khách hàng
• Lock by Teller (T): Khóa bởi GDV
• Active (A): Kích hoạt 
 | deliveryStatus | 
, bao gồm các giá trị: 

• 1
• 2
• 3
• 4
• 5
 | cardName | Tên chủ thẻ 
 | cardType | 
Loại thẻ, bao gồm:

• MainCard: Thẻ chính
• SubCard: Thẻ phụ 
 | product | 
Sản phẩm thẻ, bao gồm: 

• Credit: Thẻ tín dụng 
• Debit: Thẻ ghi nợ 
• Dual: Thẻ kép 
 | cardProduct | Sản phểm thẻ, bao gồm thẻ VIP, thường, thẻ QTDND,...
 | limitAmount | Tổng hạn mức tín dụng 
 | availAmount | Hạn mức còn lại 
 | currentAmount | Dư nợ hiện tại 
 | amountStatement | Dư nợ sao kê kỳ gần nhất 
 | minAmountDue | 
Số tiền thanh toán tối thiểu trên sao kê (MB ko dùng)

 | unpaidMinAmountDue | Số tiền min amount phải trả còn lại (thông tin show khi thanh toán thẻ)
 | unpaidStatementAmount | 
Số tiền phải trả còn lại trên sao kê (show khi tra cứu thông tin thẻ và hiện khi thanh toán thẻ)

 | AutoCreditPaymentType | 
Loại thanh toán thẻ tín dụng, bao gồm: 

• Auto (A): Tự động thanh toán 
• Manual (M): Thanh toán thủ công 
 | branchIssName | Đơn vị cấp hạn mức thẻ
 | branchIssue | Mã Đơn vị cấp hạn mức thẻ
 | issueDate | Ngày phát hành thẻ 
 | expireDate | Ngày hết hạn thẻ 
 | statementDate | Ngày sao kê gần nhất 
 | dueDate | Ngày hết hạn thanh toán sao kê gần nhất 
 | startDate | Ngày bắt đầu tính sao kê 
 | invoiceDate | Ngày chốt sao kê
 | resCode | resCode<>000
 | resDesc | 
The corresponding error message for the returned code

 | 
 | 
 | 
Bank Server
 | 
Nhận yêu cầu, thực hiện truy vấn thông tin thẻ và phản hồi kết quả 

 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi từ Bank Server:

• Không hợp lệ:  | Trường hợp | Thông báo lỗi | Xử lý 
 | 
resCode<>000
 | Thông báo lỗi tương ứng với mã lỗi do bank trả về | Bấm Đóng → Tắt pop-up lỗi 

• Hợp lệ: Hiển thị màn hình khởi tạo giao dịch thanh toán thẻ gồm các thông tin được mô tả trong tài liệu: Link
 | 2 | Nhập hoặc chọn thông tin, bấm Tiếp tục | 
Khách hàng 
 | 
Nhập hoặc chọn thông tin trên màn hình khởi tạo giao dịch, bấm nút Tiếp tục 

 | 
 | 
 | 
Mobile App 
 | 
Kiểm tra validate:

• Không hợp lệ: Hiển thị thông báo lỗiDanh sách lỗi | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Không chọn option thông tin thanh toán ở trên màn hình | Vui lòng chọn một loại thanh toán thẻ tín dụng  | 
Hiển thị pop-up thông báo lỗi

Khách hàng bấm tắt pop-up → Hiển thị màn hình hiện tại 

 | 2 | 
Tài khoản nguồn không đủ số dư (tùy theo option khách hàng lựa chọn)

• Số dư nhỏ hơn dư nợ tối thiểu của kỳ sao kê 
• Số dư nhỏ hơn toàn bộ dư nợ của kỳ sao kê 
• Số dư nhỏ hơn toàn bộ dư nợ hiện tại 
• Số dư nhỏ hơn số tiền khách hàng nhập  | Tài khoản không đủ số dư, quý khách vui lòng chọn tài khoản khác
 | 3 | 
Khách hàng nhập số tiền lớn hơn dư nợ hiện tại
 | Số tiền vượt quá dư nợ hiện tại, vui lòng nhập số tiền nhỏ hơn dư nợ hiện tại

• Hợp lệ: Điều hướng đến màn hình xác nhận giao dịch (MH2)

##### MH2: <Màn hình xác nhân giao dịch thanh toán thẻ tín dụng>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Kiểm tra thông tin và bấm xác nhận  | 
Khách hàng
 | 
Khách hàng kiểm tra thông tin trên màn hình xác nhận giao dịch, bấm nút Xác nhận 

 | 
 | 
 | 
Mobile App
 | 
Kiểm tra PTXT hợp lệ mà khách hàng đã cài đặt: 

• SMS OTP
• Soft OTP 
• FaceID hoặc TouchID 
Lưu ý: 

Để đảm bảo quy định về an toàn bảo mật, sau khi xác định ra phương thực xác thực, cần kiểm tra PTXT đó có hợp lệ hay không (ví dụ: trước khi sử dụng SoftOTP, FaceID hoặc TouchID thì phải thực hiện xác thực SMS OTP đủ số lần quy định)

Hiển thị màn hình xác thực tương ứng 

 | 2 | Khách hàng thực hiện xác thực | 
Khách hàng
 | 
Khách hàng thực hiện xác thực

 | 
 | 
 | 
Mobile App 
 | 
Thực hiện xác thực. Chi tiết được mô tả ở các tài liệu tương ứng dưới đây:

• 
• 
• 
• 
• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: Gửi yêu cầu thanh toán thẻ tín dụng đến Bank Server API createCardPayment (Thanh toán thẻ)Mô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
{
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144", 

"accountNo": "0100000000256011",

cardId": "xxx",

"branchIssue ": "01000",

  "amount":"1000000",

  "transFee": "",

  "transVAT": "",

  "transRemark": "Thanh toan du no the tin dung tren Mobile",

  "traceAuditNumber": "123456"

}

 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | accountNo | Số tài khoản nguồn 
 | cardId | 
-

 | branchIssue | Chi nhanh phát hành thẻ 
 | amount | Số tiền thanh toán thẻ tín dụng 
 | transFee | Phí (nếu không có thì truyền null)
 | transVAT | Phí (nếu không có thì truyền null)
 | transRemark | Nội dung giao dịch 
 | traceAuditNumber | Số trace do MB App Server sinh 
 | Response | 
{
  "requestId": "xxxx",
  "referenceID": "xxx",
"cifNo": "0100000000144",
"accountNo": "0100000000256011",

cardId": "xxx",

 "transRefNo ": "xxx",
"amount":"1000000",

  "transFee": "",

  "transVAT": "",

"valueDate": "dd/mm/yyyy",

"transDate": "dd/mm/yyyy",
"transRemark ": " Thanh toan du no the tin dung tren Mobile ",
  "resCode": "000",
  "resDesc": "Success"}

 | requestId | -
 | referenceID | -
 | cifNo | CIFNo của khách hàng
 | accountNo | Tài khoản nguồn 
 | cardId | -
 | transRefNo | Tài khoản thẻ 
 | amount | Số tiền khách hàng thanh toán 
 | transFee | 
-

 | transVAT | 
-

 | valueDate | 
-

 | transDate | 
-

 | transRemark | 
Nội dung giao dịch 

 | resCode | -
 | resDesc | -

 | 
 | 
 | 
Bank Server
 | 
Nhận yêu cầu, xử lý và phản hồi kết quả

 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi từ Bank Server:

• Không hợp lệ:  | Trường hợp | Thông báo lỗi | Xử lý 
 | 
resCode<>000
 | Thông báo lỗi tương ứng với mã lỗi do bank trả về | Bấm Đóng → Tắt pop-up lỗi 

• Hợp lệ: Gọi ngầm API createCardPaymentSV đến Bank severMô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
{
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144", 

      "cardId": "xxx",

"accountCardNo": "xxx",
"amount":"1000000",
  "traceAuditNumber": "123456"
}

 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | cardId | -
 | accountCardNo | Số tài khoản thẻ 
 | amount | Số tiền khách hàng thanh toán 
 | traceAuditNumber | traceAuditNumber của GD gốc đc gọi ở API createCardPayment
 | Response | 
{
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,

cifNo:"0100000000144", 

      "cardId": "xxx",

"transDate": "dd/mm/yyyy",

"ultrano": "000058265815", 

" amount ": 1000000

  "resCode": "000",
  "resDesc": "Success"}

 | systemID | 

 | requestId | -
 | cifNo | CIFNo của khách hàng
 | cardId | -
 | transDate | Thời gian thực hiện giao dịch 
 | ultrano | Mã giao dịch của hệ thống thẻ
 | amount | 
Số tiền thanh toán 

 | resCode | 
-

 | resDesc | -

 | 
 | 
 | 
Bank Server 
 | 
Nhận yêu cầu, xử lý và phản hồi kết quả

 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi và xử lý: 

• Không hợp lệ: Gọi ngầm API crAeditCardPaymentRevl đến Bank ServerMô tả API | Trường dữ liệu | Mô tả | Sample
 | Request | 
{
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144",

"accountNo": "0100000000256011",

"transDate": "dd/mm/yyyy",

" amount ": "1000000",

cardId": "xxx",

  "transRemark": "Dieu chinh but toan thanh toan the_123456",

  "orgTraceAuditNumber": "123456"

  "traceAuditNumber": "123456"

}

 | systemID | -
 | requestId | -
 | cifNo | CIFNo của khách hàng
 | accountCardNo | Số tài khoản thẻ 
 | cardId | -
 | transRemark | Dieu chinh but toan thanh toan the_[số trace]
 | amount | Số tiền khách hàng thanh toán 
 | orgTraceAuditNumber | traceAuditNumber của GD gốc đc gọi ở API createCardPayment
 | traceAuditNumber | transRefNo đc trả ở api createCardPayment
 | transDate | Thời gian thực hiện  | 
 

 | amount | Số tiền giao dịch  | 
 

 | Response | 
{
  "requestId": "xxxx",
  "referenceID": "xxx",
"cifNo": "0100000000144",
"accountNo": "0100000000256011",

cardId": "xxx",

"transRefNo ": "xxx",
"amount":"-1000000",

  "transFee": "",

  "transVAT": "",

"valueDate": "dd/mm/yyyy",

"transDate": "dd/mm/yyyy",
"transRemark ": " Dieu chinh but toan thanh toan the_orgXref ",
  "resCode": "000",
  "resDesc": "Success"}

 | requestId | -
 | referenceID | -
 | cifNo | CIFNo của khách hàng
 | accountNo | Số tài khoản nguồn
 | cardId | -
 | transRefNo | -
 | amount  | 
Số tiền thanh toán 

 | transFee | 
-

 | transVAT | 
-

 | valueDate | 
-

 | transDate | Thời gian thực hiện giao dịch 
 | transRemark | Dieu chinh but toan thanh toan the_orgXref
 | resCode | 
-

 | resDesc | -

• Hợp lệ: Dừng luồng xử lý 
 | 
 | 
 | 
Bank Server
 | 
Nhận yêu cầu từ MB App Server, xử lý và phản hồi kết quả 

• Không hợp lệ: Phản hồi lỗi
• Hợp lệ: Phản hồi kết quả thành công
 | 
 | 
 | 
Mobile App 
 | 
Nhận phản hồi, ghi nhận kết quả giao dịch và dừng luồng 

#####  MH4: <Màn hình kết quả giao dịch thanh toán thẻ tín dụng> 
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Khởi tạo màn hình  | 
Mobile App 
 | 
Hiển thị màn hình kết quả giao dịch thanh toán thẻ tín dụng bao gồm các thông tin được mô tả chi tiết trong tài liệu: 

 | 2 | Bấm nút Chia sẻ | 
Khách hàng
 | 
Khách hàng bấm nút chia sẻ

 | 
 | 
 | 
Mobile App 
 | 
Chia sẻ kết quả giao dịch qua các ứng dụng khác 

 | 3 | Bấm nút Lưu ảnh  | 
Khách hàng
 | 
Khách hàng bấm nút Lưu ảnh

 | 
 | 
 | 
Mobile App 
 | Xử lý lưu ảnh màn hình kết quả giao dịch vào thiết bị

### 5/ Bảng dữ liệu

#### 5.1/ Bảng dữ liệu sử dụng

Bao gồm tất cả các bảng dữ liệu có sử dụng trong nghiệp vụ phân tích
 | TT | Table Name | Description | Create | Reference | Update | Delete
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập mô tả mục đích của Table | Gõ "x" nếu nghiệp vụ có thao tác "Create" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Reference" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Update" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Delete" đến Table

5.2/ Thông tin cập nhật vào bảng dữ liệu

Áp dụng cho các bảng dữ liệu có sử dụng thao tác "Create", "Update"
 | TT | Table Name | Field | Value | Note
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ De

> ⚠️ *Nội dung đã cắt ngắn (15131 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 36.8. 7. Sao kê thẻ

> **Page ID:** `901058762` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/901058762

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 36.8.1. Flow & Action Sreen - Sao kê thẻ

> **Page ID:** `901058771` · **Version:** 5
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/901058771

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người thay đổi  | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | V1
Muc lục
none

### 1/ Danh sách màn hình

##### MH1: Danh sách thẻ

##### MH2: Sao kê thẻ

##### MH3: Xem sao kê thẻ

##### MH4: Không có kỳ sao kê

### 2/ Mô tả màn hình

##### MH1: Danh sách thẻ

<Tham chiếu tài liệu >

##### MH2: Sao kê thẻ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 2 | Tiêu đề | Label | ReadOnly | - | - | Sao kê thẻ
 | 3 | Danh sách kỳ sao kê | Card | Clickable area | - | - | 
Hiển thị danh sách kỳ sao kê (Tối đa 3 kỳ, do MB server giới hạn và trả về)

Click để xem chi tiết sao kê

 | 4 | 
Cấu trúc mỗi item Kỳ sao kê

 | 5 | Icon  | Icon | Click | - | - | 
Hiển thị icon biểu thị file sao kê

Click để xem chi tiết sao kê

 | 6 | 
Tên kỳ sao kê

invoice_date
 | Label | Click | - | - | 
Hiển thị tên kỳ sao kê 

Định dạng: Sao kê tháng mm/yyyyy 

Click để xem chi tiết sao kê

##### MH3: Xem sao kê thẻ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | 
Hiển thị tên kỳ sao kê tương ứng 

 | 2 | Button "Xong" | Button | Click | - | - | 
Đóng màn hình xem chi tiết, quay lại danh sách sao kê

 | 3 | Nội dung sao kê | PDF | ReadOnly | - | - | 
Hiển thị PDF sao kê 

Scroll dọc 

Có thể zoom

Hỗ trợ multi-page

 | 4 | Icon chia sẻ | Icon | Click | - | - | 
Mở system share sheet của OS

##### MH4: Không có kỳ sao kê
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 2 | Tiêu đề | Label | ReadOnly | - | - | Sao kê thẻ
 | 3 | Thông báo | Label | ReadOnly | - | - | 
Nội dung: "Chưa có sao kê cho thẻ này. Sao kê sẽ được phát hành sau khi kết thúc kỳ sao kê đầu tiên."

---

#### 36.8.2. User Action Flow - Sao kê thẻ

> **Page ID:** `901061734` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/901061734

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người thay đổi  | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
  
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | V1
Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Sao kê thẻ
 | Use Case ID | UC_CARD_STATEMENT
 | Use Case Description | 
Là người dùng, tôi muốn xem thông 

 | Actor | 
Khách hàng, Hệ thống MB, FTP Server

 | Priority | Medium
 | Trigger | 
Khách hàng nhấn nút "Sao kê thẻ" trên màn dịch vụ thẻ 

 | 
Pre-Condition
 | 
• Khách hàng đăng nhập Mobile App thành công
• Khách hàng có tồn tại thẻ tín dụng trên hệ thống Co-opBank
• Thẻ là thẻ chính với trạng thái Hoạt động/ Khóa do khách hàng / Khóa bởi GDV
 | Post-Condition | 
• KH xem sao kê thẻ thành công
 | Basic Flow | 
• Khách hàng đăng nhập mobile app Co-opBank 
• Khách hàng truy cập dịch vụ thẻ trên màn hình Home 
• Hệ thống thực hiện truy vấn danh sách thẻ tín dụng của khách hàng và hiển thị danh sách thẻ cùng các tính năng trên giao diện mobile app
• Khách hàng bấm nút "Sao kê thẻ" 
• Hệ thống truy vấn danh sách kỳ sao kê và hiển thị màn hình Sao kê thẻ
• KH chọn 1 kỳ sao kê 
• Hệ thống hiển thị thông tin sao kê giao dịch dưới file PDF trên app
 | Alternative Flow | 
--

 | Exception Flow | --
 | Bussiness Rules | 
• BR-01: Chỉ hiển thị hiển thị Sao kê thẻ với thẻ chính, có trạng thái Hoạt động/ Khóa do khách hàng / Khóa bởi GDV
• BR-02: Thông tin trong file sao kê là toàn bộ giao dịch của Thẻ chính và Thẻ phụ
• BR-03: MB server chạy job quét mỗi tháng 1 lần, remove các file có thời gian >= 6 tháng trên MinIO

### 2/ Luồng sơ đồ

 trueUntitled Diagram-1768814340944falseautotoptrue7326622

### 3/ Logic xử lý

##### MH1: Danh sách thẻ
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon "Sao kê thẻ" | Hệ thống MB | 
Gửi yêu cầu lấy danh sách kỳ sao kê Bank qua API getInvoices
Input | Trường dữ liệu | Mô tả | Sample
 | systemID | - | 
{
  "systemID": "VNPAY",
“requestId”: “00000000-0000-xxx”,
  "cifNo": "0100000000144",
"cardId": "xxx",
"fromDate":"01/07/2025","toDate": "31/07/2025"

}
 | requestId | -
 | cifNo | Số CIF của KH
 | cardId | Do App Client truyền
 | fromDate | fromDate = Sysdate - 12 tháng
 | toDate | toDate = Sysdate

 | Bank | 
Truy vấn và trả kết quả kỳ sao kê:

• Không hợp lệ: Trả thông báo lỗi tương ứng
• Hợp lệ: Trả dữ liệu về Hệ thống MBOutput | Trường dữ liệu | Mô tả | Sample
 | referenceID | - | 
"referenceID": "xxx",

  "cifNo": "0100000000144",

cardNo:"970446xxxx7899",

      "cardId": "xxx", 

 limit[

    {

      " serial_number": "xxx",

      " invoice_date": " dd/MM/yyyy"

    }

{

      " serial_number": "xxx",

      " invoice_date": " MM/yyyy"

{

      " serial_number": "xxx",

      " invoice_date": " MM/yyyy"

    }

  "resCode": "000",

  "resDesc

 | cifNo | -
 | cardNo | -
 | cardId | -
 | limit | Danh sách kỳ sao kê
 | serial_number | ID kỳ sao kê
 | invoice_date | Thời gian sao kê

 | Hệ thống MB | 
Nhận kết quả

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng
• Hợp lệ:
• TH1: Có dữ liệu kỳ sao kê
• 1/ Render danh sách kỳ sao kê theo định dạng: Sao kê tháng <invoice_date>
• 2/ Hiển thị tối đa 03 kỳ sao kê gần nhất, sắp xếp theo thứ tự kỳ sao kê gần nhất lên đầu
• TH2: Chưa phát sinh sao kê
• Hiển thị Empty State: "Chưa có sao kê cho thẻ này. Sao kê sẽ được phát hành sau khi kết thúc kỳ sao kê đầu tiên."

##### MH2: Sao kê thẻ
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Điều hướng về màn hình Dịch vụ thẻ
 | 2 | Chọn 1 kỳ sao kê | Hệ thống MB | 
1/ Dựa vào Tên file, xác định: COB_Saoke_mm_yyyy_cardid_cardno(6)_IDInvoice.pdf

• Kỳ sao kê: mm_yyyy
• File sao kê của user: Dựa vào cardId
2/ Kiểm tra

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng | 
 | Trường hợp | Nội dung thông báo | Xử lý <nếu có>
 | 1 | File không tồn tại (Không tìm thấy file tương ứng với kỳ sao kê) | Sao kê chưa được phát hành. Vui lòng thử lại sau. | 

• Hợp lệ: Tạo link truy cập file trên MinIO
Lưu ý: Luồng đồng bộ file từ FTP về MB Server được mô tả tại Mục 4 - Job đồng bộ

3/ Hiển thị

• Truy cập MinIO qua link 
• Hiển thị file sao kê (MH3)

##### MH3: Xem sao kê thẻ
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Xong" | Hệ thống MB | Điều hướng về màn hình Sao kê thẻ
 | 2 | Chọn icon Chia sẻ | Hệ thống MB | Mở system share sheet của OS

### 4/ Job đồng bộ

#### 4.1/ Bank phát hành sao kê và đẩy lên FTP <Dùng để tham khảo>

1/ Tác nhân

• Bank Core/ Card System
• FTP Server 
##### 2/ Mô tả nghiệp vụ

• Kết thúc kỳ sao kê → Bank chạy batch
• Tổng hợp dữ liệu giao dịch
• Generate file sao kê PDF theo mẫu chuẩn
• Bank đẩy file sao kê lên FTP server 
• Theo cấu trúc thư mục đã thống nhất 
• File được coi là đã phát hành (Sau khi file xuất hiện trên FTP → sao kê được coi là đã sẵn sàng cho KH)
#### 4.2/ MB Server chạy job lấy file từ FTP

1/ Tác nhân

• MB Server
• MinIO
• FTP Server
2/ Khởi chạy 

• Quy định về tần suất jon quét: job quét liên tục, mỗi lần cách nhau n tiếng (n được cấu hình tại tham số JOB_SCAN_STATEMENT_PREIODIC) 
• Đến chu kỳ ngày, giờ được quy định. Job thực hiện khởi chạy để lấy file từ FTP server về MinIO (hệ thống lưu trữ file thuộc hệ thống MB)
3/ Xử lý logic

• Bước 1: Xác định danh sách sao kê cần lấy
• Dựa trên:
• Danh sách các file sao kê đã lấy về
• Tên file
• → Chỉ lấy ra các file có mm_yyyy chưa tồn tại
• Bước 2: Truy xuất file từ FTP Server
• Cấu trúc thư mục: /home/weblogic/iofiles/outgoing/Credit_Statement 
• Tên file: COB_Saoke_mm_yyyy_cardid_cardno(6)_IDInvoice.pdf
• Không thành công:

• Ghi log
• Thành công:
• Lấy danh sách file có mm_yyyy chưa tồn tại
• Lưu ý:
• Trường hợp kỳ sao kê không phát sinh giao dịch, Bank vẫn tạo file sao kê và đẩy lên FTP 
• Bước 4: Lưu trữ file
• Lưu file sao kê vào hệ thống lưu trữ nội bộ (MinIO)

---

### 36.9. PRD Overview Dịch vụ thẻ

> **Page ID:** `920978109` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/920978109

Glossary — Thuật ngữ chung

📌 Mục đích: Bảng thuật ngữ thống nhất giữa Business, Product, BA và Development.
 | | 
Thuật ngữ
 | 
Định nghĩa
 | 
Tiếng Anh
 | 
Biệt danh / Liên quan

 | 
Thẻ tín dụng
 | 
Thẻ Credit do Co-opBank phát hành cho phép chi tiêu trước, trả sau
 | 
Credit Card
 | 
Thẻ Credit

 | 
Thẻ chính
 | 
Thẻ được phát hành cho chủ thẻ đăng ký ban đầu
 | 
Primary Card
 | 
Main Card

 | 
Thẻ phụ
 | 
Thẻ phát hành thêm theo yêu cầu của chủ thẻ chính
 | 
Supplementary Card
 | 
Sub Card

 | 
Kích hoạt thẻ
 | 
Thao tác bắt buộc trước khi sử dụng thẻ sau khi nhận thẻ vật lý
 | 
Card Activation
 | 
Activate

 | 
PIN thẻ
 | 
Mã số cá nhân 6 chữ số dùng xác thực giao dịch thẻ
 | 
Personal Identification Number
 | 
Mã PIN

 | 
Sao kê
 | 
Danh sách tổng hợp giao dịch theo kỳ thanh toán
 | 
Statement
 | 
Billing Statement

 | 
Dư nợ
 | 
Tổng số tiền KH đang nợ ngân hàng trên thẻ tín dụng
 | 
Outstanding Balance
 | 
Balance

 | 
Dư nợ tối thiểu
 | 
Số tiền tối thiểu KH cần thanh toán trong kỳ sao kê
 | 
Minimum Payment Due
 | 
Min Payment

 | 
OTP
 | 
Mật khẩu dùng một lần dùng xác thực giao dịch
 | 
One-Time Password
 | 
Soft OTP / SMS OTP

 | 
FacePay
 | 
Xác thực bằng khuôn mặt tích hợp trong App
 | 
Face Authentication
 | 
Biometrics

 | 
GDV
 | 
Giao dịch viên — nhân viên ngân hàng thực hiện nghiệp vụ tại quầy
 | 
Teller
 | 
Banker

 | 
MB Server
 | 
Server phía Mobile Banking của Co-opBank
 | 
Mobile Banking Server
 | 
MBS

 | 
SFTP
 | 
Giao thức truyền file bảo mật dùng để trao đổi file PDF sao kê
 | 
Secure File Transfer Protocol
 | 
—

 | 
Trạng thái thẻ
 | 
Trạng thái vận hành của thẻ: Chờ kích hoạt / Hoạt động / Khóa
 | 
Card Status
 | 
Card State


