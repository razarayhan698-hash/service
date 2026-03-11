from flask import Flask, render_template_string, os

app = Flask(__name__)

# আপনার তথ্য
MY_PROMO_CODE = "1x_2006981" 
TELEGRAM_BOT_URL = "https://t.me/Your_Link" # আপনার টেলিগ্রাম লিঙ্ক এখানে দিন

@app.route('/')
def home():
    # বাংলাদেশে কার্যকরী মিরর লিঙ্ক
    reg_url = f"https://1xbet-bangladesh.com/en/registration/?tag={MY_PROMO_CODE}"
    login_url = "https://1xbet-bangladesh.com/en/user/login"

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xC Official Portal</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            .top-nav { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: #162641; border-bottom: 1px solid #253959; }
            .btn-nav { padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 13px; color: white; }
            .btn-login { background: #34495e; }
            .btn-reg { background: #60a12e; }
            .container { padding: 20px; max-width: 500px; margin: auto; text-align: center; }
            .main-logo { width: 80px; height: 80px; background: #1976d2; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 20px auto; font-size: 32px; font-weight: bold; box-shadow: 0 0 25px rgba(25, 118, 210, 0.4); }
            .section-header { text-align: left; font-size: 11px; color: #8a9ab5; margin: 25px 0 12px 5px; text-transform: uppercase; letter-spacing: 1.5px; border-left: 3px solid #1976d2; padding-left: 10px; }
            .card { background: #162641; padding: 16px; border-radius: 15px; display: flex; align-items: center; margin-bottom: 12px; text-decoration: none; color: white; border: 1px solid #1c2e4a; transition: 0.3s; position: relative; }
            .card-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 22px; flex-shrink: 0; }
            .icon-moneygo { background: #ff006e; color: white; }
            .icon-bot { background: linear-gradient(135deg, #2980b9, #3498db); color: white; }
            .card-info { text-align: left; }
            .card-info b { font-size: 15px; display: block; color: #fff; }
            .card-info small { color: #8a9ab5; font-size: 11px; }
            .guide-box { background: rgba(255, 204, 0, 0.1); border: 1px dashed #ffcc00; padding: 10px; border-radius: 10px; margin-top: 8px; font-size: 10px; color: #ffcc00; display: block; }
            .badge { position: absolute; top: 10px; right: 15px; font-size: 9px; padding: 2px 7px; border-radius: 4px; font-weight: bold; background: #e74c3c; }
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
            <p style="font-size: 11px; color: #4caf50;">● SYSTEM STATUS: ONLINE</p>
            <div class="section-header">Deposit Agents</div>
            <a href="{{ telegram_url }}" class="card">
                <div class="card-icon icon-moneygo">M</div>
                <div class="card-info">
                    <b>1xbet MoneyGo Agent</b>
                    <small>Official VIP Agent for fast Cash-in/out.</small>
                </div>
            </a>
            <div class="section-header">Automated Prediction</div>
            <a href="{{ telegram_url }}" class="card">
                <span class="badge">LIVE AI</span>
                <div class="card-icon icon-bot">🤖</div>
                <div class="card-info">
                    <b>Signal & Prediction Bot</b>
                    <small>Get 99% accurate AI game signals.</small>
                    <span class="guide-box">
                        📢 <b>How to Use:</b> ক্লিক করে টেলিগ্রামে 'Start' দিন। আমাদের সিগন্যাল পেতে প্রোমো কোড <b>{{ promo }}</b> দিয়ে একাউন্ট থাকতে হবে।
                    </span>
                </div>
            </a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, reg_url=reg_url, login_url=login_url, telegram_url=TELEGRAM_BOT_URL, promo=MY_PROMO_CODE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
