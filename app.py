import os
import telebot
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

# আপনার সঠিক টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো স্যার! xCare সাপোর্ট বোট এখন সচল। 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজটি অপারেটরের কাছে পৌঁছেছে। ✨")

def run_bot():
    while True:
        try:
            bot.remove_webhook()
            bot.infinity_polling(timeout=20)
        except Exception:
            time.sleep(5)

@app.route('/')
def index():
    return "xCare Server is Online!"

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
