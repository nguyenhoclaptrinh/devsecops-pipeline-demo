from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

# LỖI BẢO MẬT 1: HARDCODED SECRET (Cố ý)
# HƯỚNG DẪN FIX: Comment hoặc xóa 2 dòng bên dưới
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q", "")

    # --- CHỌN 1 TRONG 2 LUỒNG DƯỚI ĐÂY ĐỂ DEMO ---

    # LUỒNG 1: LỖI BẢO MẬT XSS (Đang kích hoạt)
    # HƯỚNG DẪN FIX: Comment dòng bên dưới và bỏ comment LUỒNG 2
    return render_template_string(f"<h1>Results for: {q}</h1><a href='/'>Back</a>")

    # LUỒNG 2: PHIÊN BẢN AN TOÀN (Đang bị tắt)
    # return render_template("search.html", query=q)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
