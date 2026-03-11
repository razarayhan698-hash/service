from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# আপনার তথ্য
MY_PROMO_CODE = "1x_2006981" 
BOT_TOKEN = "8540257283:AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
MY_CHAT_ID = "6529319833"

@app.route('/')
def home():
    reg_url = f"https://1xbet-bangladesh.com/en/registration/?tag={MY_PROMO_CODE}"
    login_url = "https://1xbet-bangladesh.com/en/user/login"

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xC Official Agent Portal</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .top-nav { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: #162641; border-bottom: 1px solid #253959; }
            .btn-nav { padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 13px; color: white; }
            .btn-login { background: #34495e; }
            .btn-reg { background: #60a12e; }
            .container { padding: 20px; text-align: center; }
            
            /* লোগো স্টাইল */
            .main-logo { width: 75px; height: 75px; background: #1976d2; border-radius: 18px; display: flex; align-items: center; justify-content: center; margin: 20px auto; font-size: 30px; font-weight: bold; box-shadow: 0 0 20px rgba(25, 118, 210, 0.4); }
            
            .section-title { text-align: left; font-size: 12px; color: #8a9ab5; margin: 20px 0 10px 5px; text-transform: uppercase; letter-spacing: 1px; }
            
            /* এজেন্ট কার্ড স্টাইল */
            .card { background: #162641; padding: 15px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; text-decoration: none; color: white; border: 1px solid #1c2e4a; transition: 0.3s; position: relative; overflow: hidden; }
            .card:active { transform: scale(0.98); background: #1c2e4a; }
            
            .card-icon { width: 45px; height: 45px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold; font-size: 20px; }
            
            /* MoneyGo এর বিশেষ রঙ */
            .moneygo-icon { background: #ff006e; color: white; } 
            .vip-badge { position: absolute; top: 0; right: 0; background: #f39c12; color: #000; font-size: 9px; padding: 2px 8px; font-weight: bold; border-bottom-left-radius: 8px; }
            
            .card-info b { font-size: 15px; display: block; margin-bottom: 2px; }
            .card-info small { color: #8a9ab5; font-size: 11px; }
        </style>
    </head>
    <body>
        <div class="top-nav">
            <div style="font-weight: 900; font-size: 20px;">1XBET</div>
            <div class="nav-buttons">
                <a href="{{ login_url }}" class="btn-nav btn-login">Log in</a>
                <a href="{{ reg_url }}" class="btn-nav btn-reg">Registration</a>
            </div>
        </div>

        <div class="container">
            <div class="main-logo">xC</div>
            <p style="font-size: 11px; color: #4caf50;">● SYSTEM: LIVE | ID: 1XB-7729-MS</p>

            <div class="section-title">VIP AGENT APPLICATION</div>
            
            <a href="https://t.me/Your_Link" class="card">
                <div class="vip-badge">VIP</div>
                <div class="card-icon moneygo-icon">M</div> <div class="card-info" style="text-align: left;">
                    <b>1xbet MoneyGo Agent</b>
                    <small>Apply for official VIP Agent status</small>
                </div>
            </a>

            <div class="section-title">SUPPORT SERVICES</div>
            
            <a href="https://t.me/Your_Link" class="card">
                <div class="card-icon" style="background: rgba(25, 118, 210, 0.1); color: #1976d2;">TG</div>
                <div class="card-info" style="text-align: left;">
                    <b>Live Support</b>
                    <small>Contact official admin 24/7</small>
                </div>
            </a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, reg_url=reg_url, login_url=login_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
