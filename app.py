from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# আপনার নির্দিষ্ট তথ্য
MY_PROMO_CODE = "1x_2006981" 
BOT_TOKEN = "8540257283:AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
MY_CHAT_ID = "6529319833"

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
            .btn-nav { padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 13px; border: none; }
            .btn-login { background: #34495e; color: white; }
            .btn-reg { background: #60a12e; color: white; }
            .container { padding: 20px; text-align: center; }
            .custom-logo { width: 75px; height: 75px; background: #1976d2; border-radius: 18px; display: flex; align-items: center; justify-content: center; margin: 25px auto; font-size: 30px; font-weight: bold; box-shadow: 0 0 20px rgba(25, 118, 210, 0.4); }
            .card { background: #162641; padding: 18px; border-radius: 12px; display: flex; align-items: center; margin-bottom: 12px; text-decoration: none; color: white; border: 1px solid #1c2e4a; text-align: left; transition: 0.3s; }
            .card:active { transform: scale(0.98); }
            .card-icon { width: 44px; height: 44px; background: rgba(25, 118, 210, 0.1); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; border: 1px solid #1976d2; color: #1976d2; font-weight: bold; }
            .bonus-tag { font-size: 10px; color: #4caf50; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
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
            <div class="custom-logo">xC</div>
            <p class="bonus-tag">● 130% BONUS ACTIVATED BY PROMO CODE</p>
            
            <a href="{{ reg_url }}" class="card">
                <div class="card-icon">1X</div>
                <div><b>Official Partner Link</b><br><small>Get up to 15,000 BDT Welcome Bonus</small></div>
            </a>
            
            <a href="https://t.me/Your_Link" class="card">
                <div class="card-icon">TG</div>
                <div><b>24/7 Agent Support</b><br><small>Click for instant withdrawal/deposit help</small></div>
            </a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, reg_url=reg_url, login_url=login_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
