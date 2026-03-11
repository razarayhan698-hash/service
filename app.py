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
        <title>xC Official Agent & Support</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .top-nav { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: #162641; border-bottom: 1px solid #253959; }
            .btn-nav { padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 13px; color: white; }
            .btn-login { background: #34495e; }
            .btn-reg { background: #60a12e; }
            
            .container { padding: 20px; max-width: 500px; margin: auto; }
            .main-logo { width: 80px; height: 80px; background: #1976d2; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 20px auto; font-size: 32px; font-weight: bold; box-shadow: 0 0 25px rgba(25, 118, 210, 0.4); border: 2px solid rgba(255,255,255,0.1); }
            
            .section-header { text-align: left; font-size: 11px; color: #8a9ab5; margin: 25px 0 12px 5px; text-transform: uppercase; letter-spacing: 1.5px; font-weight: bold; border-left: 3px solid #1976d2; padding-left: 10px; }
            
            .card { background: #162641; padding: 16px; border-radius: 15px; display: flex; align-items: center; margin-bottom: 12px; text-decoration: none; color: white; border: 1px solid #1c2e4a; transition: all 0.3s ease; position: relative; }
            .card:active { transform: scale(0.97); background: #1c2e4a; }
            
            .card-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 22px; flex-shrink: 0; }
            
            /* আইকন কালার থিম */
            .icon-master { background: linear-gradient(135deg, #f39c12, #d35400); color: white; }
            .icon-cash { background: linear-gradient(135deg, #27ae60, #2ecc71); color: white; }
            .icon-bot { background: linear-gradient(135deg, #2980b9, #3498db); color: white; }
            .icon-moneygo { background: #ff006e; color: white; }
            
            .card-info { text-align: left; }
            .card-info b { font-size: 15px; display: block; color: #fff; }
            .card-info small { color: #8a9ab5; font-size: 11px; line-height: 1.4; display: block; margin-top: 2px; }
            
            .badge { position: absolute; top: 10px; right: 15px; font-size: 9px; padding: 2px 7px; border-radius: 4px; font-weight: bold; }
            .badge-vip { background: #f1c40f; color: #000; }
            .badge-live { background: #e74c3c; color: #fff; }
        </style>
    </head>
    <body>
        <div class="top-nav">
            <div style="font-weight: 900; font-size: 20px; letter-spacing: 1px;">1XBET</div>
            <div class="nav-buttons">
                <a href="{{ login_url }}" class="btn-nav btn-login">Log in</a>
                <a href="{{ reg_url }}" class="btn-nav btn-reg">Registration</a>
            </div>
        </div>

        <div class="container">
            <div class="main-logo">xC</div>
            <p style="font-size: 11px; color: #4caf50; text-align: center; margin-top: -10px;">● SYSTEM STATUS: ONLINE</p>

            <div class="section-header">Top-Level Management</div>
            <a href="https://t.me/Your_Link" class="card">
                <span class="badge badge-vip">OFFICIAL</span>
                <div class="card-icon icon-master">👑</div>
                <div class="card-info">
                    <b>Master Agent (xC Master)</b>
                    <small>Top-level distribution & sub-agent control.</small>
                </div>
            </a>

            <div class="section-header">Deposit & Withdrawal Agents</div>
            <a href="https://t.me/Your_Link" class="card">
                <div class="card-icon icon-moneygo">M</div>
                <div class="card-info">
                    <b>1xbet MoneyGo Agent</b>
                    <small>Fastest deposit/withdraw for VIP players.</small>
                </div>
            </a>
            
            <a href="https://t.me/Your_Link" class="card">
                <div class="card-icon icon-cash">৳</div>
                <div class="card-info">
                    <b>E-Wallet / Cash Agent</b>
                    <small>Bkash, Nagad, Rocket local point load.</small>
                </div>
            </a>

            <div class="section-header">Automated Services & Signals</div>
            <a href="https://t.me/Your_Link" class="card">
                <span class="badge badge-live">NEW</span>
                <div class="card-icon icon-bot">🤖</div>
                <div class="card-info">
                    <b>Signal & Prediction Bot</b>
                    <small>Get AI-powered game result estimates.</small>
                </div>
            </a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, reg_url=reg_url, login_url=login_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
