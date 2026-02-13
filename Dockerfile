FROM python:3.9-slim

WORKDIR /app

# Copy requirements và cài đặt trước để tận dụng Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tạo user non-root trước khi copy code
RUN useradd -m myuser

# Copy mã nguồn và templates vào container
COPY app.py .
COPY templates/ ./templates/

# Đảm bảo myuser sở hữu mọi file trong thư mục app (Security Hardening)
RUN chown -R myuser:myuser /app

# Chuyển sang user non-root
USER myuser

# Cảnh báo cho DevSecOps: Healthcheck để giám sát trạng thái ứng dụng
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/ || exit 1

EXPOSE 5000

CMD ["python", "app.py"]
