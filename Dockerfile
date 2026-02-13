FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Tạo user non-root để đảm bảo an toàn (Best Practice)
RUN useradd -m myuser
USER myuser

EXPOSE 5000

CMD ["python", "app.py"]
