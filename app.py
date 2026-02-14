from flask import Flask, request, render_template

app = Flask(__name__)

# --- BẢN SẠCH (SECURE VERSION) ---

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    # FIX LỖI XSS: Sử dụng cơ chế auto-escape của Jinja2 khi dùng render_template
    q = request.args.get("q", "")
    
    # KHÔNG CÒN HARDCODED SECRET
    # Dữ liệu nhạy cảm thực tế nên được lưu ở biến môi trường hoặc Vault

    return render_template("search.html", query=q)

if __name__ == "__main__":
    # Thay đổi host sang 127.0.0.1 để đảm bảo an toàn cục bộ
    app.run(host="127.0.0.1", port=5000)
