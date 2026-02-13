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
        <hr>
        <p>Try RCE demo: <a href="/eval?cmd=1+1">/eval?cmd=1+1</a></p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/search")
def search():
    # LỖI BẢO MẬT: REFLECTED XSS
    q = request.args.get("q", "")
    return f"<html><body><h1>Results for: {q}</h1><a href='/'>Back</a></body></html>"

@app.route("/eval")
def dangerous_eval():
    # LỖI BẢO MẬT: REMOTE CODE EXECUTION (RCE)
    cmd = request.args.get("cmd", "")
    try:
        # HARDCODED SECRET để demo Secret Scanning
        secret_key = "AWS_AKIA_EXAMPLE_KEY_123456" 
        result = eval(cmd)
        return f"Result: {result} (Secret: {secret_key})"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
