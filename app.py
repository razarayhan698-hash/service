from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম কনফিগারেশন (নিরাপদভাবে বিভক্ত)
P1 = "8540257283"
P2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
BOT_TOKEN = f"{P1}:{P2}"
MY_CHAT_ID = "6529319833"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Gateway</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            
            /* লোগো সেকশন */
            .logo-header { text-align: center; padding: 25px 0 15px 0; border-bottom: 1px solid #1c2e4a; background: #0b162c; }
            .main-logo { width: 85px; height: 85px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); border: 2px solid #1976d2; }
            .brand-name { display: block; margin-top: 10px; font-weight: bold; font-size: 18px; letter-spacing: 1px; color: #fff; }
            
            .container { padding: 20px; }
            .status-bar { display: flex; justify-content: space-between; font-size: 10px; color: #8fa3bf; margin-bottom: 20px; text-transform: uppercase; }
            .online { color: #4caf50; font-weight: bold; }
            
            .section-label { font-size: 11px; color: #8fa3bf; text-transform: uppercase; margin: 25px 0 12px 0; display: block; letter-spacing: 1px; }
            
            /* স্টাইলিশ কার্ড */
            .card { background: #162641; padding: 18px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; cursor: pointer; border: 1px solid #1c2e4a; text-decoration: none; color: white; transition: 0.3s; }
            .card:active { transform: scale(0.96); background: #1c2e4a; }
            .card-icon { width: 40px; height: 40px; background: rgba(25, 118, 210, 0.1); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid #1976d2; color: #1976d2; font-weight: bold; }
            .card-info b { display: block; font-size: 15px; margin-bottom: 2px; }
            .card-info span { font-size: 11px; color: #4caf50; }
            .arrow { margin-left: auto; color: #1976d2; font-size: 18px; }

            /* ফর্ম মডাল */
            .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 100; backdrop-filter: blur(4px); }
            .bottom-sheet { position: fixed; bottom: -100%; left: 0; width: 100%; background: #0b162c; border-radius: 25px 25px 0 0; padding: 30px 20px; box-sizing: border-box; z-index: 200; border-top: 3px solid #1976d2; transition: 0.4s cubic-bezier(0.17, 0.67, 0.83, 0.67); }
            .bottom-sheet.show { bottom: 0; }
            
            .preview-box { background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 20px; border-radius: 15px; margin-bottom: 20px; text-align: left; }
            .input-box { margin-bottom: 15px; }
            .input-box label { display: block; font-size: 11px; color: #8fa3bf; margin-bottom: 8px; }
            .input-box input { width: 100%; padding: 14px; background: #162641; border: 1px solid #253959; border-radius: 10px; color: white; box-sizing: border-box; outline: none; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 16px; width: 100%; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 10px; box-shadow: 0 4px 12px rgba(25, 118, 210, 0.3); }
        </style>
    </head>
    <body>
        <div class="logo-header">
            <img src="https://i.imgur.com/G5Zk3fG.png" alt="xC Logo" class="main-logo">
            <span class="brand-name">xCare Official</span>
        </div>

        <div class="container">
            <div class="status-bar">
                <span class="online">● System: Live</span>
                <span>ID: 1XB-7729-MS</span>
            </div>

            <span class="section-label">Agent Application</span>
            <div class="card" onclick="openForm('1xBet Master Agent')">
                <div class="card-icon">xC</div>
                <div class="card-info"><b>Apply for Agent</b><span>Link your account now</span></div>
                <div class="arrow">➔</div>
            </div>

            <span class="section-label">1xbet affiliated program</span>
            <a href="https://t.me/Your_Affiliate_Support" class="card">
                <div class="card-icon">TG</div>
                <div class="card-info"><b>Affiliated Support</b><span>Telegram Support Team</span></div>
                <div class="arrow">↗</div>
            </a>

            <a href="mailto:support@1xpartners.com" class="card">
                <div class="card-icon">@</div>
                <div class="card-info"><b>Email Helpdesk</b><span>support@1xpartners.com</span></div>
                <div class="arrow">↗</div>
            </a>
        </div>

        <div class="overlay" id="overlay" onclick="closeForm()"></div>
        <div class="bottom-sheet" id="sheet">
            <div class="preview-box">
                <small style="opacity:0.8; font-size:10px;">CREDIT LIMIT ESTIMATE</small>
                <h2 style="margin:5px 0; font-size: 26px;">৳ 5,450.00</h2>
            </div>
            
            <h4 id="f_title" style="color: #1976d2; margin-bottom: 20px;">FORM</h4>
            <form id="reqForm">
                <input type="hidden" name="type" id="f_type">
                <div class="input-box"><label>FULL NAME</label><input type="text" name="name" required></div>
                <div class="input-box"><label>TELEGRAM USER</label><input type="text" name="tg" required></div>
                <div class="input-box"><label>PHONE NUMBER</label><input type="text" name="ph" required></div>
                <button type="submit" class="submit-btn" id="s_btn">SUBMIT REQUEST</button>
            </form>
        </div>

        <script>
            function openForm(v) {
                document.getElementById('f_type').value = v;
                document.getElementById('f_title').innerText = v.toUpperCase();
                document.getElementById('overlay').style.display = 'block';
                document.getElementById('sheet').classList.add('show');
            }
            function closeForm() {
                document.getElementById('sheet').classList.remove('show');
                setTimeout(() => { document.getElementById('overlay').style.display = 'none'; }, 400);
            }
            document.getElementById('reqForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('s_btn').innerText = 'WAITING...';
                const d = Object.fromEntries(new FormData(e.target));
                const res = await fetch('/api/request', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(d)
                });
                if(res.ok) { alert('Success!'); location.reload(); }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/request', methods=['POST'])
def request_api():
    d = request.json
    msg = f"🚀 **New Application**\n\n📌 Service: {d.get('type')}\n👤 Name: {d.get('name')}\n🆔 TG: {d.get('tg')}\n📱 Ph: {d.get('ph')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": MY_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
