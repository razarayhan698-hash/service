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
        <title>xCare Support | Agent Selection</title>
        <style>
            body { font-family: sans-serif; background: #0b162c; color: white; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
            .header { width: 100%; background: #162641; padding: 15px; display: flex; justify-content: space-between; border-bottom: 1px solid #253959; font-size: 12px; box-sizing: border-box; position: sticky; top: 0; z-index: 100; }
            .main-content { width: 95%; max-width: 450px; margin-top: 15px; }
            
            /* Agent List Styling */
            .list-title { font-size: 14px; color: #8fa3bf; margin-bottom: 10px; padding-left: 5px; }
            .agent-card { background: #162641; border: 1px solid #253959; border-radius: 12px; padding: 15px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; transition: 0.3s; }
            .agent-card:hover { background: #1c2d4d; border-color: #1976d2; }
            .agent-info { display: flex; align-items: center; gap: 12px; }
            .agent-icon { background: #0b162c; padding: 10px; border-radius: 50%; font-size: 20px; }
            .agent-details b { display: block; font-size: 15px; margin-bottom: 2px; }
            .agent-details span { font-size: 11px; color: #4caf50; }
            .arrow { color: #8fa3bf; font-weight: bold; }

            /* Form Overlay (Initially Hidden) */
            #overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(11, 22, 44, 0.95); z-index: 200; overflow-y: auto; padding-top: 30px; }
            .form-box { width: 90%; max-width: 380px; background: #162641; padding: 25px; border-radius: 20px; border: 1px solid #253959; margin: 0 auto; box-sizing: border-box; }
            .input { width: 100%; padding: 12px; margin: 10px 0; background: #0b162c; border: 1px solid #253959; border-radius: 8px; color: white; box-sizing: border-box; }
            .submit-btn { background: #1976d2; color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 15px; }
            .close-btn { color: #8fa3bf; text-align: center; margin-top: 20px; cursor: pointer; font-size: 13px; text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="header"><span>🌐 Gateway: Online</span><span>ID: 1XB-7729-MS</span></div>
        
        <div class="main-content" id="listPage">
            <div class="list-title">এজেন্ট নেওয়ার জন্য নিচের অপশনে ক্লিক করুন:</div>
            
            <div class="agent-card" onclick="openForm('Master Agent')">
                <div class="agent-info">
                    <div class="agent-icon">👑</div>
                    <div class="agent-details"><b>Master Agent</b><span>Available Now</span></div>
                </div>
                <div class="arrow">➔</div>
            </div>

            <div class="agent-card" onclick="openForm('Local Agent')">
                <div class="agent-info">
                    <div class="agent-icon">📍</div>
                    <div class="agent-details"><b>Local Agent</b><span>Available Now</span></div>
                </div>
                <div class="arrow">➔</div>
            </div>

            <div class="agent-card" onclick="openForm('Sub Agent')">
                <div class="agent-info">
                    <div class="agent-icon">💼</div>
                    <div class="agent-details"><b>Sub Agent</b><span>Available Now</span></div>
                </div>
                <div class="arrow">➔</div>
            </div>
        </div>

        <div id="overlay">
            <div class="form-box">
                <h3 style="margin: 0 0 5px 0; text-align: center;" id="formTitle">Agent Application</h3>
                <p style="text-align: center; color: #8fa3bf; font-size: 12px; margin-bottom: 20px;">আপনার সঠিক তথ্য দিয়ে ফরমটি পূরণ করুন</p>
                <form id="vForm">
                    <input type="hidden" name="type" id="agentType">
                    <input type="text" name="name" class="input" placeholder="Full Name" required>
                    <input type="text" name="user" class="input" placeholder="Telegram @username" required>
                    <input type="text" name="phone" class="input" placeholder="WhatsApp Number" required>
                    <button type="submit" class="submit-btn" id="sBtn">LINK ACCOUNT</button>
                </form>
                <div class="close-btn" onclick="closeForm()">Back to List</div>
            </div>
        </div>

        <script>
            function openForm(type) {
                document.getElementById('agentType').value = type;
                document.getElementById('formTitle').innerText = type + " Request";
                document.getElementById('overlay').style.display = 'block';
            }

            function closeForm() {
                document.getElementById('overlay').style.display = 'none';
            }

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
                    alert('সফলভাবে তথ্য পাঠানো হয়েছে! আমাদের টিম আপনার সাথে যোগাযোগ করবে।'); 
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
    msg = f"🚀 **New Agent Request**\n\n🎯 Type: {d.get('type')}\n👤 Name: {d.get('name')}\n🆔 User: {d.get('user')}\n📞 Phone: {d.get('phone')}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
