import os
import telebot
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

# আপনার টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- বোটের রিপ্লাই লজিক ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো স্যার! xCare সাপোর্ট বোট এখন আপনার জন্য প্রস্তুত। 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_msg = message.text.lower()
    if "hi" in user_msg or "হ্যালো" in user_msg:
        bot.reply_to(message, "হ্যালো! আপনাকে কীভাবে সাহায্য করতে পারি? ✨")
    else:
        bot.reply_to(message, "আপনার মেসেজটি আমাদের টিমের কাছে পৌঁছেছে।")

# --- বোট রান করার ফাংশন ---
def run_bot():
    while True:
        try:
            bot.remove_webhook() # পুরনো জ্যাম ক্লিয়ার করা
            print("Bot is Polling...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

# --- ওয়েবসাইট রুট (Cron-job এর জন্য) ---
@app.route('/')
def index():
    return "xCare Server is Online and Polling!"

if __name__ == "__main__":
    # বোটকে আলাদা থ্রেডে চালানো যাতে ওয়েবসাইটও চালু থাকে
    t = Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    # Render পোর্টের সঠিক কনফিগারেশন
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
