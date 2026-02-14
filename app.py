from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Sử dụng render_template thay vì render_template_string để tránh cảnh báo SSTI của Semgrep
    return render_template("index.html")

@app.route("/search")
def search():
    # --- PHIÊN BẢN ĐÃ FIX LỖI BẢO MẬT ---
    
    # FIX LỖI XSS: Sử dụng cơ chế auto-escape của Jinja2 khi dùng render_template
    q = request.args.get("q", "")
    
    # KHÔNG CÒN HARDCODED SECRET
    # Dữ liệu nhạy cảm nên được lưu ở biến môi trường hoặc Vault

    return render_template("search.html", query=q)

if __name__ == "__main__":
    # Thay đổi host từ 0.0.0.0 sang 127.0.0.1 để tránh cảnh báo bảo mật về việc public server vô ý
    # Trong môi trường Docker, host sẽ được ghi đè bằng CMD hoặc biến môi trường nếu cần
    app.run(host="127.0.0.1", port=5000)
