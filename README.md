# Website Nhật Minh Academy

## Overview
Website giới thiệu **Nhật Minh Academy** — học viện IT đào tạo theo lộ trình từ Tiểu học → THCS → THPT → Kỹ năng đi làm. Trang gồm: giới thiệu lộ trình, danh sách & chi tiết khóa học, học phí, blog (có trang đọc bài), giới thiệu giảng viên, và form đăng ký học thử.

Mục tiêu của gói này: giúp một lập trình viên **dựng lại thiết kế này trong một codebase thật** để phát triển, đăng lên GitHub và đưa online lâu dài.

## About the Design Files
Các file trong gói này là **bản tham chiếu thiết kế viết bằng HTML** — prototype thể hiện giao diện và hành vi mong muốn, **không phải code production để copy nguyên xi**.

- `nhat-minh-academy.dc.html` — file nguồn gốc. Nó là một "Design Component": HTML + CSS inline + một class JavaScript (logic) chạy trên **React** thông qua một runtime riêng của môi trường tạo ra nó (`support.js`). **Runtime này không phù hợp để phát triển production**, nên đừng cố build trực tiếp từ file này.
- `nhat-minh-academy-offline.html` — bản đã đóng gói để **xem demo offline** (mở bằng trình duyệt). Không dùng để chỉnh sửa (đã bị nén/gộp).

**Việc cần làm:** đọc README này + tham chiếu 2 file trên, rồi **xây dựng lại trang trong một framework chuẩn** (khuyến nghị Next.js + React + Tailwind, xem mục cuối). Toàn bộ giao diện đều có thể tái tạo bằng HTML/CSS thuần — không có thư viện UI độc quyền.

## Fidelity
**High-fidelity (hifi).** Màu, font, khoảng cách, bo góc, đổ bóng, và tương tác đều là bản cuối. Hãy tái tạo **pixel-perfect** theo các giá trị trong mục Design Tokens.

## Tech hiện tại (tóm tắt)
- **HTML + CSS inline + React** (logic ở class `Component`).
- Toàn bộ "ảnh" hiện là **đồ họa CSS** (gradient + hình khối) và **emoji** — chưa có ảnh thật. Thay bằng ảnh thật khi có.
- Không gọi API, không backend. Mọi dữ liệu (khóa học, bài blog, học phí, giảng viên) là **dữ liệu tĩnh trong code** (các mảng `COURSES`, `POSTS`, `levels`, `plans`, `teachers`).
- Điều hướng là **client-side** bằng một biến state `page` (không dùng URL router) — khi dựng lại nên chuyển sang router thật (route riêng cho từng trang).

## Screens / Views
Điều hướng qua state `page`: `home`, `roadmap`, `courses`, `course`, `post`, `register`.

### 1. Header (mọi trang)
- Sticky top, nền `rgba(245,248,253,0.82)` + `backdrop-filter: blur(12px)`, viền dưới `1px #E4EAF3`, cao `72px`, container `max-width:1180px`.
- Logo: ô vuông bo `12px` gradient `135deg #2E6BFF→#1746C4`, chữ "NM" trắng `font-weight:800`. Bên cạnh: "Nhật Minh" (`#0B1E3F`, 700) + "Academy" (`#1E56E3`, 700), size `19px`.
- Menu: Trang chủ · Lộ trình · Khóa học · Học phí · Blog (Học phí/Blog cuộn tới section trên Home). Link active màu `#1E56E3`, mặc định `#46536E`.
- Nút CTA "Đăng ký học thử": nền `#1E56E3`, chữ trắng, bo `10px`, shadow `0 6px 16px rgba(30,86,227,.28)`.

### 2. Home (`home`)
Thứ tự section:
1. **Hero** — nền gradient navy `#0B1E3F→#0E2A55` + pattern chấm. Lưới 2 cột: trái = badge "🎓 Lộ trình IT liền mạch", H1 serif `50px` ("Học công nghệ **đúng lộ trình** theo từng cấp lớp", chữ nhấn `#6FA0FF`), mô tả, 2 nút, 3 chỉ số (4 cấp độ / 15+ khóa / 100% học qua dự án). Phải = **đồ họa cửa sổ code Python** (window dark, 3 chấm đỏ/vàng/xanh, code có syntax màu) + 2 chip nổi ("Chạy thành công ⭐", "▶ Học qua dự án").
2. **Trust strip** — nền trắng, dòng "Đào tạo theo chuẩn:" + Scratch · Python · GitHub · AI·ML · Jira.
3. **Lộ trình 4 cấp** — 4 thẻ bấm được (Tiểu học/THCS/THPT/Đi làm), mỗi thẻ có icon, màu cấp, mô tả ngắn, "Xem chi tiết →".
4. **Khóa học nổi bật** — nền trắng, 4 thẻ khóa (Scratch, Python Khởi Đầu, AI nhập môn, Săn việc IT).
5. **Vì sao chọn** — lưới 2 cột: trái = **thẻ timeline lộ trình** (4 cấp + thanh tiến độ màu), phải = 4 điểm mạnh.
6. **Học phí** (`#pricing`) — nền navy, 3 gói (xem Pricing bên dưới), gói giữa nổi bật ("Phổ biến nhất").
7. **Blog** (`#blog`) — 3 thẻ bài viết bấm được (banner gradient + icon), "Đọc tiếp →".
8. **Giáo viên** (`#teachers`) — thẻ giảng viên căn giữa (xem Teachers).
9. **CTA cuối** — banner gradient xanh "Đăng ký học thử miễn phí".

### 3. Lộ trình (`roadmap`)
Header navy + 4 thẻ lớn (mỗi cấp 1 thẻ): cột trái màu cấp (icon, tên cấp, lớp, mục tiêu), cột phải = lưới nội dung học (đánh số) + nút "Xem khóa học cấp này →" (lọc danh sách khóa theo cấp).

### 4. Danh sách khóa học (`courses`)
Header + bộ lọc dạng pill (Tất cả / Tiểu học / THCS / THPT / Đi làm). Lưới 3 cột thẻ khóa: banner màu cấp + icon + badge cấp, tên, mô tả, thời lượng/số buổi, "Học phí chỉ từ {x}/tháng", "Chi tiết →".

### 5. Chi tiết khóa học (`course`)
Header navy 2 cột: trái = badge cấp, tên khóa, mô tả dài, 4 thông số (thời lượng/số buổi/độ tuổi/hình thức); phải = card giá (icon, "Học phí chỉ từ {x}/tháng", ghi chú trọn khóa, nút đăng ký, danh sách "bao gồm"). Dưới: "Bạn sẽ học được gì" (lưới 2 cột) + "Chương trình chi tiết" (các module đánh số) + sidebar "Phù hợp với bạn nếu...".

### 6. Trang đọc bài blog (`post`)
Container `max-width:760px`. Nút "← Tất cả bài viết", tag, H1 serif, dòng tác giả (avatar "HN" + tên + ngày + thời gian đọc), banner gradient, đoạn lead `19px`, các mục `h2 + p`, box CTA cuối bài.

### 7. Đăng ký / Liên hệ (`register`)
Lưới 2 cột: trái = giới thiệu + thông tin liên hệ (hotline/email/địa chỉ) + khối "Kết nối" (Zalo/Messenger/Facebook) + **bản đồ cách điệu** (CSS). Phải = form (Họ tên phụ huynh*, Họ tên học viên, Cấp/Lớp, SĐT*, Email, Khóa quan tâm, Lời nhắn) + nút gửi. Có **màn hình thành công** sau khi gửi.

### 8. Floating contact (mọi trang)
Góc phải dưới, cột 3 nút tròn `54px`: Gọi (`#1E9E6A`, icon SVG điện thoại, có vòng pulse), Zalo (`#0068FF`, chữ "Zalo"), Messenger (gradient tím `#9B4DFF→#7B2FF7`, icon SVG bong bóng chat).

### 9. Footer (mọi trang)
Nền `#081730`. 4 cột: thương hiệu + mô tả + icon mạng xã hội; Chương trình; Khám phá; Liên hệ (hotline 0984 883 750, email huynh2102@gmail.com, địa chỉ). Dòng cuối: "© 2026 Nhật Minh Academy..." + "Cùng các em chinh phục công nghệ ❤️".

## Interactions & Behavior
- **Điều hướng:** click logo/menu/nút → đổi `page` + `window.scrollTo(0,0)`. "Học phí"/"Blog" cuộn mượt tới section trên Home (`scrollIntoView`, không dùng cho việc khác).
- **Lọc khóa học:** click pill → lọc theo `level.id`; pill active nền `#1E56E3` chữ trắng.
- **Mở khóa/bài:** click thẻ → set id active + chuyển trang `course`/`post`.
- **Hover thẻ:** `transform:translateY(-4px)` + shadow `0 18px 34px rgba(16,42,76,.1)`, transition `.18s`.
- **Form validation:** Họ tên phụ huynh bắt buộc; SĐT bắt buộc + regex `^[0-9+\s().-]{8,}$`. Lỗi: viền `#E89BAB` + text `#D14D6B`. Hợp lệ → màn hình thành công (icon ✓, nút "Đăng ký thêm" reset form).
- **Animation nền:** chip hero và con trỏ code nhấp nháy (keyframes `nmFloat`, `nmFloat2`); nút gọi có `nmPulse`. *(Lưu ý: KHÔNG dùng animation kiểu fade-in opacity 0→1 cho nội dung chính — bản gốc từng bị ẩn nội dung khi đóng gói.)*

## State Management
- `page` (string): trang hiện tại.
- `activeCourseId`, `activePostId`: id khóa/bài đang xem.
- `filter`: cấp đang lọc (`all` hoặc id cấp).
- `form` (object): các trường form; `errors` (object); `submitted` (boolean).
- Khi dựng lại: nên thay `page` bằng **router** (Next.js App Router), và form nên gửi tới một endpoint/email thật (hiện chỉ hiển thị màn hình thành công, chưa gửi đi đâu).

## Design Tokens
**Màu nền & mực**
- Nền trang: `#F5F8FD` · Thẻ/section trắng: `#FFFFFF` · Nền tối (hero/pricing): `#0B1E3F`, `#0F2752` · Footer: `#081730`
- Mực chính: `#102A4C` / `#0B1E3F` · Mực phụ: `#55617A`, `#46536E`, `#8593AD` · Viền: `#E4EAF3`

**Màu thương hiệu (xanh dương)**
- Primary: `#1E56E3` · hover `#1746C4` · gradient `135deg #2E6BFF→#1746C4` · nhấn trên nền tối `#6FA0FF`

**Màu theo cấp học (badge/tint)**
- Tiểu học: `#D9802E` / tint `#FBEEDF`
- THCS: `#1E9E6A` / tint `#E1F3EB`
- THPT: `#5B53D6` / tint `#E9E7FB`
- Đi làm: `#D14D6B` / tint `#FAE6EB`

**Màu kênh liên hệ:** Zalo `#0068FF` · Messenger `#9B4DFF→#7B2FF7` · Facebook `#1877F2` · Gọi `#1E9E6A`

**Typography**
- Tiêu đề (serif): **Lora** 500/600/700 — H1 hero 50px, H2 section 40px.
- Nội dung/UI (sans): **Be Vietnam Pro** 400/500/600/700.
- Cả hai từ Google Fonts. (Có thể đổi sang font khác hỗ trợ tiếng Việt tốt khi dựng lại.)

**Spacing / Radius / Shadow**
- Padding section: `88px 0` · container `max-width:1180px; padding:0 24px`
- Bo góc: nút `10–12px`, thẻ `18px`, thẻ lớn/banner `20–22px`, pill `100px`
- Shadow thẻ: `0 1px 3px rgba(16,42,76,.05)`; hover `0 18px 34px rgba(16,42,76,.1)`; nút primary `0 6px 16px rgba(30,86,227,.28)`

## Học phí (Pricing)
Mô hình **theo tháng**, 2 buổi/tuần (8 buổi/tháng). Mức/tháng theo cấp: Tiểu học 1.000.000đ · THCS 1.200.000đ · THPT 1.400.000đ · Đi làm 1.500.000đ. Giá khóa = mức/tháng × (số tuần ÷ 4).
3 gói: **Đóng theo tháng** (1tr/tháng, linh hoạt) · **Combo học kỳ 4 tháng** (từ 3.8tr, −5%, *Phổ biến nhất*) · **Combo cả năm 9 tháng** (từ 8.1tr, −10%).

## Assets
- **Chưa có ảnh thật.** Tất cả hình minh họa là đồ họa CSS (gradient + khối) và emoji. Khi dựng lại nên chuẩn bị: logo thật, ảnh lớp học/hoạt động, ảnh chân dung giảng viên, ảnh minh họa blog.
- Icon SVG dùng trong floating contact (điện thoại, messenger) là path đơn giản — có thể thay bằng thư viện icon (lucide, heroicons).

## Files
- `nhat-minh-academy.dc.html` — nguồn thiết kế (HTML + CSS inline + logic React). Tham chiếu chính cho mọi giá trị.
- `nhat-minh-academy-offline.html` — bản demo offline để xem nhanh.

---

## Khuyến nghị dựng lại & đưa lên GitHub
**Stack đề xuất:** Next.js (App Router) + React + TypeScript + Tailwind CSS. Mỗi `page` → một route. Dữ liệu tĩnh tách ra `data/` (courses, posts, levels, plans, teachers). Blog có thể nâng cấp dùng Markdown/MDX hoặc một CMS (Sanity, Contentful, Strapi) để tự đăng bài. Form đăng ký nối tới email/Google Sheet/DB.

**Các bước đưa lên GitHub (làm trên máy bạn):**
```bash
# 1. Tạo thư mục dự án và copy gói này vào
cd duong-dan/du-an-nhat-minh
git init
git add .
git commit -m "Initial: thiết kế Nhật Minh Academy"

# 2. Tạo repo rỗng trên github.com (vd: nhat-minh-academy), rồi:
git remote add origin https://github.com/<tai-khoan>/nhat-minh-academy.git
git branch -M main
git push -u origin main
```
Sau đó mở dự án (hoặc giao cho lập trình viên) kèm README này để dựng lại bằng Next.js và phát triển tiếp (đăng nhập, CMS, hosting...). Deploy nhanh: **Vercel** (kết nối thẳng repo GitHub).
