import os
import telebot
import time
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার নতুন টোকেনটি এখানে বসানো হয়েছে ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
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
    while True: # বোট ক্রাশ করলে যেন অটো আবার চালু হয়
        try:
            bot.remove_webhook()
            time.sleep(1) # ছোট বিরতি কানেকশন ক্লিয়ার করার জন্য
            print("Telegram Bot is starting...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(5) # এরর হলে ৫ সেকেন্ড পর আবার চেষ্টা করবে

# --- আপনার সেই চমৎকার xCare ওয়েব ডিজাইন ---
@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #0b1528; color: white; font-family: sans-serif; }
            .card-bg { background: #16243d; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen">
        <div class="text-center space-y-4">
            <h1 class="text-5xl font-bold italic text-blue-500 mb-6">xCare</h1>
            <div class="card-bg p-8 shadow-2xl">
                <p class="text-green-400 font-bold animate-pulse text-xl">SYSTEM ONLINE</p>
                <p class="text-xs text-gray-400 mt-2 italic">Bot connected to Telegram API successfully</p>
                <div class="mt-6">
                    <a href="https://t.me/xcaresupport_bot" class="bg-blue-600 px-6 py-2 rounded-lg font-bold hover:bg-blue-700 transition">Open Bot</a>
                </div>
            </div>
            <p class="text-gray-600 text-[10px] uppercase">© 2026 xCare Professional Services</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    # বোট আলাদা থ্রেডে চালানো
    Thread(target=run_bot, daemon=True).start()
    
    # Render পোর্ট সেটিংস (আপনার লগ অনুযায়ী ১০০০০)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
