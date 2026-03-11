import os
import telebot
import threading
from flask import Flask, render_template_string

# --- আপনার সঠিক তথ্য ---
TOKEN = "6479485230:AAF-Rw-M24vgZD98kkYUUVncz-iwU881lDY"
MY_PROMO_CODE = "1x_2006981"
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot"
# ---------------------

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

# ১. ওয়েবসাইট ইন্টারফেস
@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <style>
            body {{ background-color: #0b162c; color: white; text-align: center; font-family: sans-serif; margin-top: 80px; }}
            .card {{ background: linear-gradient(135deg, #1e3c72, #2a5298); padding: 25px; border-radius: 20px; display: inline-block; text-decoration: none; color: white; border: 1px solid #3a7bd5; }}
            .logo {{ width: 60px; height: 60px; background: #1976d2; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 24px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="logo">xC</div>
        <h2>xCare Official</h2>
        <p style="color: #4caf50;">● SYSTEM ONLINE</p><br>
        <a href="{TELEGRAM_BOT_URL}" class="card">
            <b style="font-size: 18px;">💬 Live Support Chat</b><br>
            <small>সরাসরি বটের সাথে কথা বলুন</small>
        </a>
    </body>
    </html>
    '''
    return render_template_string(html_content)

# ২. বট পোলিং ফাংশন (যা ওয়েবসাইটকে জ্যাম করবে না)
def start_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "xC Official সাপোর্টে স্বাগতম! 😊")
    
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except:
        pass

if __name__ == "__main__":
    # বটকে আলাদা একটি থ্রেডে চালানো (এটিই সমাধান)
    threading.Thread(target=start_bot, daemon=True).start()
    
    # মেইন সার্ভার
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
