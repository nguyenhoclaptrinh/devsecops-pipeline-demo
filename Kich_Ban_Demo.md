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

## BƯỚC 6: TRÌNH DIỄN LUỒNG THÀNH CÔNG (SECURE FLOW)
- **Hành động:** 
    1. Chuyển sang branch `fix/secure-app`.
    2. Cho xem code đã được fix:
        - Sử dụng `render_template("search.html")` thay vì `render_template_string` để tận dụng cơ chế auto-escape của Jinja2.
        - Xóa bỏ **Hardcoded Secret**.
        - Đổi host từ `0.0.0.0` thành `127.0.0.1`.
    3. Cho xem **Dockerfile** đã được tối ưu:
        - Sử dụng lệnh `chown` để đảm bảo user non-root sở hữu mã nguồn (Hardening).
        - Thêm `HEALTHCHECK` giúp hệ thống tự giám sát trạng thái container.
    4. Thực hiện Push branch này lên.
- **Nội dung trình bày:**
    - "Sau khi phát hiện lỗi, lập trình viên sẽ tiến hành sửa lỗi theo hướng dẫn của hệ thống."
    - "Tại branch `fix/secure-app`, chúng tôi đã sử dụng cơ chế auto-escape của Jinja2 và loại bỏ mã bí mật."
    - "Khi mã nguồn đã sạch, hệ thống sẽ tự động thực hiện các bước tiếp theo trong chu trình CD (Continuous Deployment)."

## BƯỚC 7: KIỂM TRA CHU TRÌNH CD (CONTINUOUS DEPLOYMENT)
- **Hành động:** Mở tab **Actions** trên GitHub và xem workflow của branch `fix/secure-app`.
- **Nội dung trình bày:**
    - "Quan sát pipeline: Sau khi các bước Scan (CI) thành công, hệ thống đã mở khóa các bước tiếp theo."
    - "Bước **Push to Docker Hub**: Image sạch sẽ được đóng gói và đẩy lên registry tập trung."
    - "Bước **Deploy Simulation**: Sau cùng, ứng dụng sẽ được tự động triển khai lên môi trường sản phẩm."
    - "=> Đây chính là cốt lõi của DevSecOps: Bảo mật không còn là một rào cản, mà là một phần tích hợp sâu vào tốc độ triển khai phần mềm."
    - "Khi push code sạch, pipeline sẽ chạy vượt qua (Pass) tất cả các bước SAST, SCA, DAST và sẵn sàng cho việc deployment."

## BƯỚC 7: KẾT LUẬN CUỐI CÙNG
- **Nội dung trình bày:**
    - "DevSecOps không chỉ là để 'chặn', mà là để tạo ra một chu kỳ phản hồi nhanh, giúp phần mềm trở nên an toàn hơn một cách bền vững."
