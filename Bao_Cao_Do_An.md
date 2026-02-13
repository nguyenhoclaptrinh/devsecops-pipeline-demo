# BÁO CÁO ĐỒ ÁN: TRIỂN KHAI HỆ THỐNG DEVSECOPS PIPELINE

## CHƯƠNG 1: TỔNG QUAN VỀ DEVSECOPS
### 1.1. Khái niệm DevSecOps
DevSecOps là sự mở rộng của DevOps, tích hợp các biện pháp bảo mật vào mọi giai đoạn của vòng đời phát triển phần mềm (SDLC).
### 1.2. Triết lý Shift-Left Security
Di chuyển các hoạt động kiểm tra bảo mật về phía bên trái của pipeline (giai đoạn lập trình và build) để phát hiện và sửa lỗi sớm nhất có thể, giảm thiểu chi phí và rủi ro.

## CHƯƠNG 2: THIẾT KẾ HỆ THỐNG
### 2.1. Kiến trúc Pipeline
Hệ thống sử dụng GitHub Actions làm bộ điều phối chính (Orchestrator).
### 2.2. Các công nghệ sử dụng
- **Mã nguồn:** Python Flask (App demo lỗ hổng bảo mật).
- **SAST:** Semgrep (Quét lỗi Python hiệu quả).
- **SCA:** Trivy (Quét thư viện trong `requirements.txt`).
- **Container Security:** Trivy (Image scan).
- **DAST:** OWASP ZAP.

## CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM
### 3.1. Cấu hình SAST & SCA
Sử dụng **Semgrep** để quét mã nguồn Python tìm các lỗi như XSS, lộ lọt Secret Key.
Sử dụng **Trivy** để quét thư viện và container image.
### 3.2. Cấu hình DAST
Thiết lập ZAP quét ứng dụng Flask chạy trên Docker tại `http://localhost:5000`.
### 3.3. Dockerization
Xây dựng Docker image chuẩn (multistage build) và lưu trữ trên Docker Hub.

## CHƯƠNG 4: KẾT QUẢ VÀ THẢO LUẬN
### 4.1. Khả năng phát hiện lỗi
- **SAST:** Phát hiện lỗi sử dụng hàm `eval()` và lộ mã bí mật (Secret).
- **SCA:** Phát hiện các thư viện lỗi thời có mã CVE cao.
- **DAST:** Phát hiện các thiếu sót về Security Headers.
### 4.2. Kết quả Pipeline
Mọi kết quả được tổng hợp tự động tại tab **Security** của GitHub.

## CHƯƠNG 5: ĐÁNH GIÁ VÀ KẾT LUẬN
### 5.1. Ưu điểm
- Tự động hóa hoàn toàn, không cần can thiệp thủ công.
- Tích hợp sâu vào hệ sinh thái GitHub.
### 5.2. Hướng phát triển
- Tích hợp thêm Slack/Mail notification khi pipeline fail do lỗi bảo mật nghiêm trọng.
