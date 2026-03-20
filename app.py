import os
import telebot
import time
from flask import Flask
from threading import Thread

# আপনার সঠিক টোকেন বসান
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "বট এখন সচল আছে! 😊")

@app.route('/')
def home():
    return "xCare Server is Online!"

def run_bot():
    while True:
        try:
            bot.remove_webhook()
            bot.infinity_polling(none_stop=True)
        except Exception:
            time.sleep(5)

if __name__ == "__main__":
    # বোটকে আলাদা থ্রেডে চালানো
    Thread(target=run_bot, daemon=True).start()
    
    # Render-এর জন্য পোর্টের সঠিক সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
