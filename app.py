import os
import telebot
from flask import Flask, render_template_string

# --- আপনার তথ্য ---
TOKEN = "6479485230:AAF-Rw-M24vgZD98kkYUUVncz-iwU881lDY"
MY_PROMO_CODE = "1x_2006981"
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot"
# -----------------

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

# --- ১. পোর্টাল ইন্টারফেস ---
@app.route('/')
def home():
    reg_url = f"https://1xbet-bangladesh.com/en/registration/?tag={MY_PROMO_CODE}"
    
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Official Support</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; text-align: center; }
            .container { padding: 20px; max-width: 500px; margin: auto; }
            .main-logo { width: 80px; height: 80px; background: #1976d2; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 20px auto; font-size: 32px; font-weight: bold; }
            .live-chat-card { background: linear-gradient(135deg, #1e3c72, #2a5298); padding: 20px; border-radius: 18px; display: flex; align-items: center; margin-bottom: 20px; text-decoration: none; color: white; border: 1px solid #3a7bd5; }
            .chat-dot { width: 12px; height: 12px; background: #00ff00; border-radius: 50%; margin-right: 15px; box-shadow: 0 0 10px #00ff00; }
            .text-box { text-align: left; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="main-logo">xC</div>
            <p style="color: #4caf50;">● SUPPORT ONLINE</p>
            
            <a href="{{ tg_link }}" class="live-chat-card">
                <div class="chat-dot"></div>
                <div class="text-box">
                    <b>Live Support Chat</b><br>
                    <small>সরাসরি আমাদের বটের সাথে কথা বলুন</small>
                </div>
            </a>
            
            <a href="{{ reg_url }}" style="color: #60a12e; text-decoration: none; font-weight: bold;">Create New Account</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content, reg_url=reg_url, tg_link=TELEGRAM_BOT_URL)

# --- ২. বটের অটো-রিপ্লাই লজিক ---
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, f"xC Official সাপোর্টে স্বাগতম! 😊\\n\\nসিগন্যাল পেতে 'Signal' লিখুন।\\nআমাদের প্রোমো কোড: {MY_PROMO_CODE}")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    user_msg = message.text.lower()
    if 'signal' in user_msg:
        bot.reply_to(message, "🚀 পরবর্তী গেমে ১.৮x এ ক্যাশআউট করার চেষ্টা করুন।\\nএটি একটি এআই প্রেডিকশন।")
    elif 'deposit' in user_msg:
        bot.reply_to(message, "ডিপোজিট করতে আপনার বিকাশ বা নগদ নম্বর লিখে পাঠান।")
    else:
        bot.reply_to(message, "ধন্যবাদ! আপনার মেসেজটি আমরা পেয়েছি। আমাদের এজেন্ট শীঘ্রই আপনার সাথে যোগাযোগ করবে।")

# সার্ভার এবং বট একসাথে চালানোর জন্য
if __name__ == "__main__":
    # বটকে আলাদা থ্রেডে চালানো উচিত, তবে সহজ করার জন্য পোলিং দেওয়া হলো
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
