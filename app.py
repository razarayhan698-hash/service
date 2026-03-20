import os
import telebot
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

# আপনার লেটেস্ট টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- বোটের রিপ্লাই ফাংশন ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো স্যার! xCare বোট এখন সচল আছে। 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজটি অপারেটরের কাছে পৌঁছেছে। ✨")

# --- বোট চালানোর সঠিক পদ্ধতি ---
def run_bot():
    while True:
        try:
            # আগের সব জ্যাম ক্লিয়ার করার জন্য এটি জরুরি
            bot.remove_webhook() 
            print("Webhook removed, starting polling...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

@app.route('/')
def index():
    return "<h1>xCare Server is Online and Polling!</h1>"

if __name__ == "__main__":
    # বোটকে আলাদা থ্রেডে চালানো
    t = Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    # Render-এর জন্য পোর্ট সেটআপ
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
