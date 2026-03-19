import os
import telebot
import time
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# আপনার টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        text = message.text.lower()
        if any(word in text for word in ["hi", "hello", "হাই", "হ্যালো"]):
            bot.reply_to(message, "হ্যালো! xCare সাপোর্টে আপনাকে স্বাগতম। 😊")
        else:
            bot.reply_to(message, "আপনার মেসেজটি আমাদের কাছে পৌঁছেছে। ✨")
    except Exception as e:
        print(f"Error: {e}")

def run_bot():
    while True:
        try:
            # আগের সব আটকে থাকা সেশন ডিলিট করার জন্য এই লাইনটি জরুরি
            bot.remove_webhook(drop_pending_updates=True)
            time.sleep(1)
            print("Bot is starting fresh...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Bot Error: {e}")
            time.sleep(5)

@app.route('/')
def home():
    return render_template_string('''
        <body style="background:#0b1528; color:white; text-align:center; padding-top:100px; font-family:sans-serif;">
            <h1 style="color:#3b82f6; font-size:50px;">xCare</h1>
            <p style="color:#4ade80;">SERVER IS LIVE & BOT IS CONNECTING...</p>
            <br>
            <a href="https://t.me/xcaresupport_bot" style="background:#2563eb; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Message Bot Now</a>
        </body>
    ''')

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
