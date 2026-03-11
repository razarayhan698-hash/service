import os
import telebot
from flask import Flask, render_template_string

# আপনার তথ্য
TOKEN = "6479485230:AAF-Rw-M24vgZD98kkYUUVncz-iwU881lDY"
MY_PROMO_CODE = "1x_2006981"
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot"

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    reg_url = f"https://1xbet-bangladesh.com/en/registration/?tag={MY_PROMO_CODE}"
    html_content = f'''
    <html>
    <body style="background-color: #0b162c; color: white; text-align: center; font-family: sans-serif;">
        <h1>xC Official Support</h1>
        <a href="{TELEGRAM_BOT_URL}" style="display: inline-block; padding: 20px; background: #1e3c72; color: white; border-radius: 15px; text-decoration: none;">💬 Live Support Chat</a>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
