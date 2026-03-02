from flask import Flask, render_template_string, request, send_from_directory, jsonify
import os
import requests

app = Flask(__name__)

# --- আপনার টেলিগ্রাম বটের তথ্য ---
TELEGRAM_BOT_TOKEN = '8540257283:AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw'
MY_CHAT_ID = '6529319833'

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
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f4f7; margin: 0; padding: 0; }
            .header { background: #fff; padding: 18px; text-align: center; font-size: 22px; font-weight: bold; color: #2b5d8c; border-bottom: 2px solid #e1e8ed; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
            .container { padding: 25px; max-width: 450px; margin: auto; }
            .card { background: white; border-radius: 18px; padding: 20px; margin-bottom: 15px; display: flex; align-items: center; cursor: pointer; transition: 0.3s; border: 1px solid #e1e8ed; }
            .card:active { transform: scale(0.97); }
            .icon-bg { width: 50px; height: 50px; background: #edf2f7; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 18px; font-size: 24px; }
            
            /* Modal Design */
            #overlay { display: none; position: fixed; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 999; backdrop-filter: blur(4px); }
            .modal { display: none; position: fixed; bottom: 0; width: 100%; background: white; border-radius: 30px 30px 0 0; padding: 30px; box-sizing: border-box; z-index: 1000; box-shadow: 0 -5px 25px rgba(0,0,0,0.1); }
            
            /* Form Style */
            .form-title { margin-top: 0; color: #1a3a5a; font-size: 20px; text-align: center; margin-bottom: 20px; }
            .form-input { width: 100%; padding: 14px; margin-bottom: 15px; border: 1.5px solid #dbe3eb; border-radius: 12px; box-sizing: border-box; font-size: 15px; outline: none; transition: 0.3s; }
            .form-input:focus { border-color: #2b5d8c; background: #f9fbff; }
            .submit-btn { background: #2b5d8c; color: white; padding: 16px; width: 100%; border: none; border-radius: 12px; font-weight: bold; font-size: 16px; cursor: pointer; transition: 0.3s; }
            .submit-btn:hover { background: #1e4468; }

            /* Success Message Style */
            #successState { display: none; text-align: center; padding: 20px; }
            .success-icon { font-size: 60px; color: #4caf50; margin-bottom: 15px; }
            .success-text { color: #2c3e50; font-size: 18px; font-weight: bold; margin-bottom: 10px; }
            .wait-text { color: #7f8c8d; font-size: 14px; line-height: 1.5; }
        </style>
    </head>
    <body>
        <div class="header">xCare Support</div>
        
        <div class="container">
            <div class="card" onclick="showModal('contactModal')">
                <div class="icon-bg">📱</div>
                <div><b>Agent Application</b><br><span style="color:#888; font-size:13px">1xBet & E-wallet Agent</span></div>
            </div>
        </div>

        <div id="overlay" onclick="hideModals()"></div>

        <div id="contactModal" class="modal">
            <h3 class="form-title">আবেদন ক্যাটাগরি বেছে নিন</h3>
            <div style="background:#f1f5f9; padding:15px; border-radius:12px; margin-bottom:10px; cursor:pointer; font-weight:bold" onclick="openForm('1xBet Master Agent')">👑 1xBet Master Agent</div>
            <div style="background:#f1f5f9; padding:15px; border-radius:12px; margin-bottom:10px; cursor:pointer; font-weight:bold" onclick="openForm('E-wallet Agent')">💳 E-wallet Agent</div>
            <div onclick="hideModals()" style="text-align:center; margin-top:15px; color:#999; cursor:pointer">বন্ধ করুন</div>
        </div>

        <div id="formModal" class="modal">
            <div id="formState">
                <h3 id="formTitle" class="form-title">Application</h3>
                <form id="agentForm">
                    <input type="hidden" id="applyType" name="applyType">
                    <input type="text" name="country" class="form-input" placeholder="Your Country" required>
                    <input type="text" name="tg_num" class="form-input" placeholder="Your Telegram Number" required>
                    <input type="text" name="tg_user" class="form-input" placeholder="Your Telegram Username" required>
                    <button type="submit" class="submit-btn" id="subBtn">সাবমিট করুন</button>
                </form>
            </div>

            <div id="successState">
                <div class="success-icon">✅</div>
                <div class="success-text">আবেদন সফল হয়েছে!</div>
                <p class="wait-text">
                    আপনার তথ্য গ্রহণ করা হয়েছে। দয়া করে অপেক্ষা করুন, <br>
                    <b>৪৮ ঘণ্টার মধ্যে</b> আমরা আপনার টেলিগ্রামে মেসেজ দেব।
                </p>
                <button class="submit-btn" style="background:#f0f2f5; color:#333; margin-top:10px" onclick="hideModals()">ঠিক আছে</button>
            </div>
        </div>

        <script>
            function showModal(id) {
                document.getElementById(id).style.display = 'block';
                document.getElementById('overlay').style.display = 'block';
            }
            function hideModals() {
                document.querySelectorAll('.modal').forEach(m => m.style.display = 'none');
                document.getElementById('overlay').style.display = 'none';
                setTimeout(() => {
                    document.getElementById('formState').style.display = 'block';
                    document.getElementById('successState').style.display = 'none';
                }, 500);
            }
            function openForm(type) {
                document.getElementById('contactModal').style.display = 'none';
                document.getElementById('formTitle').innerText = type + " Application";
                document.getElementById('applyType').value = type;
                showModal('formModal');
            }

            document.getElementById('agentForm').onsubmit = async (e) => {
                e.preventDefault();
                const subBtn = document.getElementById('subBtn');
                subBtn.innerText = 'প্রসেসিং...';
                subBtn.disabled = true;

                const formData = new FormData(e.target);
                const data = Object.fromEntries(formData.entries());

                try {
                    const res = await fetch('/send-to-tg', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(data)
                    });
                    if(res.ok) {
                        document.getElementById('formState').style.display = 'none';
                        document.getElementById('successState').style.display = 'block';
                        e.target.reset();
                    } else { alert('Error sending data!'); }
                } catch (err) { alert('Server error!'); }
                
                subBtn.innerText = 'সাবমিট করুন';
                subBtn.disabled = false;
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/send-to-tg', methods=['POST'])
def send_to_tg():
    data = request.json
    text = (
        f"🌟 **New Agent Request** 🌟\n\n"
        f"💼 Type: {data.get('applyType')}\n"
        f"🌍 Country: {data.get('country')}\n"
        f"📞 TG Number: {data.get('tg_num')}\n"
        f"✈️ TG Username: {data.get('tg_user')}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": MY_CHAT_ID, "text": text, "parse_mode": "Markdown"})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
