from flask import Flask, request, render_template_string

app = Flask(__name__)

# Giao diện HTML đơn giản để demo
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps Demo</title>
    <style>
        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; background: #f0f2f5; }
        .container { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input[type="text"] { padding: 10px; width: 300px; border: 1px solid #ddd; border-radius: 4px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .warning { color: red; font-size: 0.8rem; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Search Engine</h1>
        <form action="/search" method="GET">
            <input type="text" name="q" placeholder="Enter keyword..." required>
            <button type="submit">Search</button>
        </form>
        <p class="warning">Warning: This app is intentionally vulnerable for security demo.</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/search")
def search():
    # --- VULNERABILITY DEMO START ---
    
    # LỖI BẢO MẬT: REFLECTED XSS (Cố ý)
    # Mô tả: Dữ liệu người dùng từ query parameter 'q' được render trực tiếp vào HTML mà không qua escape.
    # Mục tiêu: Để công cụ SAST (Semgrep) và DAST (OWASP ZAP) có thể phát hiện.
    q = request.args.get("q", "")
    
    # HARDCODED SECRET (Cố ý)
    # Mô tả: Một chuỗi giả lập API Key của AWS để kiểm tra tính năng Secret Scanning.
    # Mục tiêu: Để công cụ SCA/Secret Scanning (Trivy/Github Secrets) có thể bắt được.
    secret_key = "AWS_AKIA_EXAMPLE_KEY_123456" 
    
    # --- VULNERABILITY DEMO END ---

    return f"<html><body><h1>Results for: {q}</h1><p style='display:none'>Debug Info: {secret_key}</p><a href='/'>Back</a></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
