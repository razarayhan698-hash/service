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
    # এই অংশটি আপনার ওয়েবসাইট দেখাবে
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <style>
            body {{ background-color: #0b162c; color: white; text-align: center; font-family: sans-serif; margin-top: 100px; }}
            .btn {{ background: #1e3c72; color: white; padding: 20px 40px; border-radius: 15px; text-decoration: none; font-weight: bold; font-size: 20px; border: 1px solid #3a7bd5; }}
        </style>
    </head>
    <body>
        <div style="font-size: 50px; font-weight: bold; margin-bottom: 20px;">xC</div>
        <h2 style="margin-bottom: 40px;">xCare Official Support</h2>
        <a href="{TELEGRAM_BOT_URL}" class="btn">💬 Live Support Chat</a>
        <p style="margin-top: 50px; color: #4caf50;">● SYSTEM STATUS: ONLINE</p>
    </body>
    </html>
    '''
    return render_template_string(html_content)

# বটের জন্য আলাদা ফাংশন যাতে ওয়েবসাইট জ্যাম না হয়
def start_bot():
    @bot.message_handler(commands=['start'])
    def welcome(message):
        bot.reply_to(message, "xC Official সাপোর্টে স্বাগতম! 😊\\nআপনার প্রশ্নটি এখানে লিখুন।")
    
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except:
        pass

if __name__ == "__main__":
    # বটকে ব্যাকগ্রাউন্ডে চালানোর জন্য থ্রেডিং
    threading.Thread(target=start_bot, daemon=True).start()
    
    # মেইন সার্ভার চালু করা
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
