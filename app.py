import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# টেলিগ্রাম বোট টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# অটো-রিপ্লাই লজিক
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "hi" in text or "hello" in text or "হাই" in text or "হ্যালো" in text:
        bot.reply_to(message, "হ্যালো স্যার! 👋 xCare সাপোর্ট লাইনে আপনাকে স্বাগতম। 😊")
    elif "agent" in text or "এজেন্ট" in text:
        bot.reply_to(message, "👑 আমাদের মাস্টার এজেন্ট হতে চাইলে আপনার ফোন নম্বরটি এখানে দিন।")
    else:
        bot.reply_to(message, "আপনার মেসেজটি আমাদের অপারেটরের কাছে পৌঁছেছে। অনুগ্রহ করে কিছুক্ষণ অপেক্ষা করুন। ✨")

def run_bot():
    # বোটকে সচল রাখার জন্য এটি সবচেয়ে ভালো উপায়
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

@app.route('/')
def home():
    # আপনার ওয়েবসাইটের ইন্টারফেস
    return render_template_string("<h1>xCare Bot Service is Live!</h1>")

if __name__ == "__main__":
    # বোটকে আলাদাভাবে চালানো
    Thread(target=run_bot, daemon=True).start()
    
    # রেন্ডার সার্ভারের জন্য এই পোর্টটি সেট করা আবশ্যক
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
