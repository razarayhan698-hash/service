import os
import telebot
from flask import Flask
from threading import Thread

# আপনার সঠিক টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# বোটের রিপ্লাই ফাংশন
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো স্যার! বোটটি এখন সচল আছে। 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজটি অপারেটর দেখছে। ✨")

# বোট চালানোর সঠিক পদ্ধতি (Polling)
def run_bot():
    bot.remove_webhook()
    print("Bot is starting to poll...")
    bot.infinity_polling(none_stop=True, interval=0, timeout=20)

@app.route('/')
def home():
    return "<h1>xCare Server is Live!</h1>"

if __name__ == "__main__":
    # বোটকে আলাদা থ্রেডে চালু করা
    Thread(target=run_bot, daemon=True).start()
    
    # Render পোর্টের জন্য ফ্লাস্ক চালু করা
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
