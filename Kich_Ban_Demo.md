# KỊCH BẢN DEMO: HỆ THỐNG DEVSECOPS PIPELINE

Tài liệu này hướng dẫn các bước trình diễn hệ thống DevSecOps pipeline cho dự án Flask Demo.

## MỤC TIÊU DEMO
1. Cho thấy cách pipeline tự động phát hiện lỗi bảo mật ngay khi code được đẩy lên (Shift-left).
2. Minh họa sức mạnh của các công cụ SAST, SCA, và DAST.
3. Chứng minh việc ngăn chặn deploy mã nguồn không an toàn.

---

## BƯỚC 1: GIỚI THIỆU MÃ NGUỒN (SHIFT-LEFT)
- **Hành động:** Mở file `app.py`.
- **Nội dung trình bày:**
    - "Chúng tôi đã cố ý chèn các lỗ hổng bảo mật phổ biến để kiểm tra hệ thống."
    - **Reflected XSS:** Tại route `/search`, biến `q` từ người dùng được trả về trực tiếp mà không qua lọc.
    - **Hardcoded Secret:** Một mã AWS API Key giả được khai báo trực tiếp trong mã nguồn.
    - "Theo triết lý Shift-left, những lỗi này cần được phát hiện sớm nhất có thể."

## BƯỚC 2: THỰC HIỆN COMMIT VÀ PUSH
- **Hành động:** Chỉnh sửa nhẹ một file (ví dụ: thêm comment) -> Commit -> Push lên branch `main`.
- **Nội dung trình bày:**
    - "Ngay khi lập trình viên thực hiện `git push`, GitHub Actions sẽ tự động kích hoạt pipeline bảo mật."

## BƯỚC 3: PHÂN TÍCH PIPELINE (GITHUB ACTIONS)
- **Hành động:** Mở tab **Actions** trên GitHub và chọn run mới nhất.
- **Nội dung trình bày:**
    - **Job: security-scan (SAST - Semgrep):**
        - Giải thích: "Semgrep quét mã nguồn tĩnh. Kết quả cho thấy job bị **Failed** vì phát hiện XSS và Secret Key."
        - Show log: Chỉ vào dòng thông báo lỗi của Semgrep.
    - **Job: docker-build-scan & dast-scan:**
        - Giải thích: "Vì bước bảo mật đầu tiên thất bại, hệ thống tự động ngắt (abort) các bước sau để đảm bảo an toàn. Không có Docker image nào được build từ mã nguồn lỗi này."

## BƯỚC 4: XEM KẾT QUẢ TỔNG HỢP (GITHUB SECURITY)
- **Hành động:** Mở tab **Security** -> **Code scanning alerts**.
- **Nội dung trình bày:**
    - "GitHub cung cấp một bảng điều khiển tập trung cho các cảnh báo bảo mật. Tại đây, chúng ta có thể thấy chi tiết vị trí dòng code bị lỗi và hướng dẫn khắc phục."

## BƯỚC 5: KẾT LUẬN
- **Nội dung trình bày:**
    - "Hệ thống đã hoàn thành tốt nhiệm vụ: Tự động hóa việc kiểm tra, phát hiện lỗi sớm và ngăn chặn rủi ro trước khi ứng dụng được triển khai thực tế."
