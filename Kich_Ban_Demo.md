# KỊCH BẢN DEMO DEVSECOPS PIPELINE (QUICK FIX)

Tài liệu này hướng dẫn bạn cách demo nhanh chu trình DevSecOps trực tiếp trên nhánh `main`.

## BƯỚC 1: GIỚI THIỆU TRẠNG THÁI HIỆN TẠI
- **Hành động:** Mở file `app.py`.
- **Nội dung trình bày:**
    - "Hiện tại, file `app.py` của chúng tôi đang chứa 2 lỗi bảo mật nghiêm trọng mà lập trình viên vô tình bỏ quên."
    - "1. **Hardcoded Secret**: Một API Key nhạy cảm bị để lộ ngay trong code."
    - "2. **Reflected XSS**: Sử dụng `render_template_string` kết hợp với f-string, cho phép hacker chèn mã script độc hại."

## BƯỚC 2: KÍCH HOẠT PIPELINE (THẤT BẠI)
- **Hành động:** Thực hiện một thay đổi nhỏ (ví dụ thêm dấu cách) và Push lên `main`.
- **Nội dung trình bày:**
    - "Khi tôi push code này lên, hệ thống CI/CD sẽ tự động kích hoạt các công cụ quét bảo mật."
    - "Vào tab **Actions**, chúng ta sẽ thấy Pipeline bị **FAILED** ngay tại bước **Security Scan**."
    - "Semgrep đã phát hiện ra cả Secret Key và lỗi XSS, ngăn chặn việc deploy mã nguồn không an toàn."

## BƯỚC 3: THỰC HIỆN "QUICK FIX" TRỰC TIẾP
- **Hành động:** Quay lại `app.py` và thực hiện:
    1. Comment dòng `API_KEY`.
    2. Comment luồng code XSS và bỏ comment luồng `render_template` an toàn.
- **Nội dung trình bày:**
    - "Bây giờ, là một DevSecOps engineer, tôi sẽ fix lỗi ngay lập tức dựa trên cảnh báo."
    - "Tôi loại bỏ Secret và chuyển sang sử dụng template an toàn (Jinja2 auto-escape)."

## BƯỚC 4: PIPELINE BÁO XANH & AUTO DEPLOY
- **Hành động:** Push code đã fix lên `main`.
- **Nội dung trình bày:**
    - "Lần này, Pipeline sẽ vượt qua tất cả các bài test (Pass)."
    - "Hệ thống sẽ tự động tiến hành các bước tiếp theo: Build image, Scan Image và cuối cùng là **Deploy Simulation**."
    - "=> Đây là minh chứng cho một quy trình phát triển phần mềm an toàn, tự động và tin cậy."

---

## MỤC TIÊU DEMO
1. Cho thấy cách pipeline tự động phát hiện lỗi bảo mật ngay khi code được đẩy lên (Shift-left).
2. Minh họa sức mạnh của các công cụ SAST, SCA, và DAST.
3. Chứng minh việc ngăn chặn deploy mã nguồn không an toàn.

## KẾT LUẬN CUỐI CÙNG
- **Nội dung trình bày:**
    - "DevSecOps không chỉ là để 'chặn', mà là để tạo ra một chu kỳ phản hồi nhanh, giúp phần mềm trở nên an toàn hơn một cách bền vững."
