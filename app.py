import os
import telebot
import threading
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
    # এখানে আপনার আগের সুন্দর ডিজাইনটি ফিরিয়ে আনা হয়েছে
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ background-color: #0b162c; color: white; text-align: center; font-family: sans-serif; margin-top: 50px; }}
            .card {{ background: linear-gradient(135deg, #1e3c72, #2a5298); padding: 25px; border-radius: 20px; display: inline-block; text-decoration: none; color: white; border: 1px solid #3a7bd5; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }}
            .logo {{ width: 70px; height: 70px; background: #1976d2; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 28px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="logo">xC</div>
        <h2>xC Official Support</h2>
        <p style="color: #4caf50;">● SYSTEM ONLINE</p><br>
        <a href="{TELEGRAM_BOT_URL}" class="card">
            <b style="font-size: 18px;">💬 Live Support Chat</b><br>
            <small>সরাসরি বটের সাথে কথা বলুন</small>
        </a>
    </body>
    </html>
    '''
    return render_template_string(html_content)

# বটের অটো-রিপ্লাই ফাংশন
def run_bot():
    @bot.message_handler(commands=['start'])
    def welcome(message):
        bot.reply_to(message, "xC Official সাপোর্টে স্বাগতম! 😊\\nআপনার প্রশ্নটি লিখুন।")
    
    bot.infinity_polling()

if __name__ == "__main__":
    # বটকে আলাদাভাবে চালানোর জন্য থ্রেডিং ব্যবহার করা হয়েছে
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # ফ্ল্যাস্ক সার্ভার চালানো
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
