import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার নতুন টেলিগ্রাম টোকেন ---
# BotFather থেকে পাওয়া লেটেস্ট টোকেনটি এখানে বসান
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
        print(f"Message Error: {e}")

def run_bot():
    while True:
        try:
            bot.remove_webhook()
            print("Bot is starting to poll...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Polling error: {e}")
            import time
            time.sleep(5) # এরর হলে ৫ সেকেন্ড পর আবার চেষ্টা করবে

# --- xCare ওয়েব ভিউ ---
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
            .card-bg { background: #16243d; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen">
        <div class="text-center space-y-6">
            <h1 class="text-5xl font-bold italic text-blue-500">xCare</h1>
            <a href="tg://resolve?domain=xcaresupport_bot" class="block">
                <div class="card-bg p-6 flex items-center justify-between gap-10">
                    <div class="text-left">
                        <p class="font-bold text-xl">Operator Chat</p>
                        <p class="text-xs text-gray-400">Direct Support</p>
                    </div>
                    <span class="text-green-400 font-bold animate-pulse">● ONLINE</span>
                </div>
            </a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
