from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# টেলিগ্রাম কনফিগ (নিরাপদভাবে বিভক্ত)
T1 = "8540257283"
T2 = "AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
TELEGRAM_BOT_TOKEN = f"{T1}:{T2}"
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
            body { font-family: sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .header { padding: 15px; display: flex; justify-content: space-between; border-bottom: 1px solid #1c2e4a; font-size: 11px; }
            .status { color: #4caf50; font-weight: bold; }
            .container { padding: 20px; }
            .label { font-size: 10px; color: #8fa3bf; text-transform: uppercase; margin: 20px 0 10px 0; display: block; }
            .card { background: #162641; padding: 15px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 10px; cursor: pointer; border: 1px solid #1c2e4a; text-decoration: none; color: white; }
            .logo-icon { width: 40px; height: 40px; background: rgba(25, 118, 210, 0.1); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid #1976d2; color: #1976d2; font-weight: bold; }
            .info b { display: block; font-size: 14px; }
            .info span { font-size: 10px; color: #4caf50; }
            .arrow { margin-left: auto; color: #1976d2; }
            .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 100; }
            .sheet { position: fixed; bottom: -100%; left: 0; width: 100%; background: #0b162c; border-radius: 20px 20px 0 0; padding: 25px; box-sizing: border-box; z-index: 200; border-top: 2px solid #1976d2; transition: 0.4s; }
            .sheet.show { bottom: 0; }
            .input-box { margin-bottom: 15px; }
            .input-box label { display: block; font-size: 10px; color: #8fa3bf; margin-bottom: 5px; }
            .input-box input { width: 100%; padding: 12px; background: #162641; border: 1px solid #253959; border-radius: 8px; color: white; outline: none; box-sizing: border-box; }
            .btn { background: #1976d2; color: white; border: none; padding: 15px; width: 100%; border-radius: 10px; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="header"><span class="status">● GATEWAY: ONLINE</span><span>ID: 1XB-PARTNERS</span></div>
        <div class="container">
            <span class="label">Services</span>
            <div class="card" onclick="openS('1xBet Master Agent')">
                <div class="logo-icon">xC</div>
                <div class="info"><b>1xBet Master Agent</b><span>Click to apply</span></div>
                <div class="arrow">➔</div>
            </div>
            <span class="label">1xbet affiliated program</span>
            <a href="https://t.me/Your_Support_Link" class="card">
                <div class="logo-icon">TG</div>
                <div class="info"><b>Affiliated Support</b><span>Telegram Support Team</span></div>
                <div class="arrow">↗</div>
            </a>
            <a href="mailto:support@1xpartners.com" class="card">
                <div class="logo-icon">@</div>
                <div class="info"><b>Email Support</b><span>Official Mailbox</span></div>
                <div class="arrow">↗</div>
            </a>
        </div>
        <div class="overlay" id="ov" onclick="closeS()"></div>
        <div class="sheet" id="sh">
            <h3 id="tit" style="color:#1976d2; margin-top:0;">FORM</h3>
            <form id="f">
                <input type="hidden" name="type" id="tp">
                <div class="input-box"><label>NAME</label><input type="text" name="n" required></div>
                <div class="input-box"><label>TELEGRAM</label><input type="text" name="t" required></div>
                <div class="input-box"><label>PHONE</label><input type="text" name="p" required></div>
                <button type="submit" class="btn" id="b">SUBMIT REQUEST</button>
            </form>
        </div>
        <script>
            function openS(v){ document.getElementById('tp').value=v; document.getElementById('tit').innerText=v; document.getElementById('ov').style.display='block'; document.getElementById('sh').classList.add('show'); }
            function closeS(){ document.getElementById('sh').classList.remove('show'); setTimeout(()=>{document.getElementById('ov').style.display='none'},400); }
            document.getElementById('f').onsubmit = async (e) => {
                e.preventDefault();
                document.getElementById('b').innerText = 'SENDING...';
                const d = Object.fromEntries(new FormData(e.target));
                const r = await fetch('/api/send', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(d) });
                if(r.ok) { alert('Done!'); location.reload(); }
            };
        </script>
    </body>
    </html>
    ''')

@app.route('/api/send', methods=['POST'])
def send():
    d = request.json
    m = f"🚀 **New App**\nType: {d.get('type')}\nName: {d.get('n')}\nTG: {d.get('t')}\nPh: {d.get('p')}"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", json={"chat_id": MY_CHAT_ID, "text": m, "parse_mode": "Markdown"})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
