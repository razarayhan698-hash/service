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
    bot.reply_to(message, "হ্যালো স্যার! আপনার বোট এখন লাইভ আছে। 😊")

@bot.message_handler(func=lambda message: True)
def all_messages(message):
    bot.reply_to(message, "আমি আপনার মেসেজটি পেয়েছি! ✨")

def run_bot():
    while True:
        try:
            bot.remove_webhook() # এটি পুরনো সব কানেকশন কেটে নতুন করে শুরু করবে
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

@app.route('/')
def home():
    return "xCare Server is Online!"

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
