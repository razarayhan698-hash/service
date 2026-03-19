import os
import telebot
import time
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার নতুন টোকেনটি এখানে বসানো হয়েছে ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- বোটের রিপ্লাই লজিক ---
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        if not message.text:
            return
            
        text = message.text.lower()
        if any(word in text for word in ["hi", "hello", "হাই", "হ্যালো"]):
            bot.reply_to(message, "হ্যালো স্যার! 👋 xCare সাপোর্ট লাইনে আপনাকে স্বাগতম। 😊")
        elif any(word in text for word in ["agent", "এজেন্ট"]):
            bot.reply_to(message, "👑 মাস্টার এজেন্ট হতে চাইলে আপনার ফোন নম্বরটি এখানে দিন।")
        else:
            bot.reply_to(message, "আপনার মেসেজটি আমাদের অপারেটরের কাছে পৌঁছেছে। ✨")
            
    except Exception as e:
        print(f"Error handling message: {e}")

def run_bot():
    while True:
        try:
            # পুরনো সব সেশন ক্লিয়ার করে বোট চালু করা
            bot.remove_webhook(drop_pending_updates=True)
            time.sleep(1)
            print("Telegram Bot is starting with NEW TOKEN...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(5)

# --- ওয়েব ভিউ ডিজাইন ---
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>xCare Support</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#0b1528] text-white flex items-center justify-center min-h-screen">
        <div class="text-center p-8 bg-[#16243d] rounded-xl border border-blue-500/30 shadow-2xl">
            <h1 class="text-5xl font-bold italic text-blue-500 mb-4">xCare</h1>
            <p class="text-green-400 font-bold animate-pulse text-lg">SYSTEM ONLINE</p>
            <p class="text-gray-400 mt-2 text-sm italic">New Bot Token Connected Successfully</p>
            <div class="mt-8">
                <a href="https://t.me/xcaresupport_bot" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-full font-bold transition duration-300">
                    START CHAT
                </a>
            </div>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    # বোট আলাদা থ্রেডে চালানো
    Thread(target=run_bot, daemon=True).start()
    
    # Render-এর পোর্ট সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
