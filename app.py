import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার বোট তথ্য ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটোমেটিক রিপ্লাই সেট করা ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম xCare সাপোর্ট বোটে! আমরা আপনাকে কীভাবে সাহায্য করতে পারি?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    
    # এখানে আপনি আপনার পছন্দমতো প্রশ্ন ও উত্তর সাজাতে পারেন
    if "agent" in text:
        bot.reply_to(message, "আমাদের মাস্টার এজেন্ট হতে চাইলে নিচের লিঙ্কে ক্লিক করুন।")
    elif "hi" in text or "hello" in text:
        bot.reply_to(message, "হ্যালো! xCare-এ আপনাকে স্বাগতম।")
    else:
        bot.reply_to(message, "আপনার মেসেজটি আমরা পেয়েছি। আমাদের একজন প্রতিনিধি শীঘ্রই আপনার সাথে যোগাযোগ করবেন।")

# বোট রান করার ফাংশন
def run_bot():
    bot.polling(none_stop=True)

# --- ওয়েবসাইট অংশ (Render পোর্টের জন্য) ---
@app.route('/')
def home():
    # আপনার সেই চমৎকার ডিজাইনটি এখানে থাকবে
    return "<h1>xCare Bot Service is Running!</h1>"

if __name__ == "__main__":
    # বোটকে আলাদা থ্রেডে চালানো যাতে ওয়েবসাইটও চালু থাকে
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
