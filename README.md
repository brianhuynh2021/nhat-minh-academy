# Nhật Minh Academy

Trang giới thiệu tin học thực hành cho học sinh lớp 3–12 và người đi làm. Dự án là website tĩnh, không cần framework, máy chủ ứng dụng hay cài thư viện. Nội dung và thời lượng trên trang là lộ trình dự kiến, cần xác nhận khi tổ chức lớp.

## Cấu trúc

- `index.html`: nội dung trang và cấu trúc HTML.
- `assets/styles.css`: giao diện và bố cục cho điện thoại, máy tính.
- `scripts/build.py`: tạo bản HTML độc lập và file ZIP để triển khai.
- `dist/`: kết quả build, không đưa vào Git.
- `nhat-minh-academy-offline.html`, `nhat-minh-academy.dc.html`: tài liệu thiết kế cũ được giữ lại để tham khảo, không tham gia build.

## Chạy trên máy

Cần Python 3. Trong thư mục dự án, chạy:

```sh
python3 -m http.server 8000
```

Mở `http://localhost:8000`. Có thể sửa trực tiếp HTML và CSS rồi tải lại trang.

## Đóng gói

```sh
python3 scripts/build.py
```

Lệnh tạo `dist/index.html` (HTML độc lập có CSS nhúng) và `dist/nhat-minh-academy.zip`. Mở file HTML để xem offline hoặc giải nén ZIP lên hosting tĩnh. Không có bước cài package hay bundle JavaScript.

## Triển khai sau này

Với GitHub Pages, chọn nhánh chứa `index.html` và `assets/` làm nguồn xuất bản (ví dụ `main` và thư mục `/root`). Với hosting tĩnh khác, đưa `index.html` cùng thư mục `assets/` lên máy chủ, hoặc tải nội dung ZIP trong `dist` lên thư mục gốc của website. Cập nhật địa chỉ, số điện thoại, lộ trình và nội dung trước khi công bố nếu có thay đổi.

Các nút liên hệ mở ứng dụng điện thoại hoặc Zalo; trang không có biểu mẫu gửi dữ liệu và không có backend. Thời lượng học chỉ là dự kiến tư vấn, không đại diện lịch khai giảng hoặc cam kết đầu ra.
