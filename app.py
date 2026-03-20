import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার টেলিগ্রাম বোটের নতুন টোকেন ---
# BotFather থেকে পাওয়া নতুন টোকেনটি এখানে বসান
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
        print(f"Error: {e}")

def run_bot():
    try:
        bot.remove_webhook()
        print("Bot is starting...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Polling error: {e}")

# --- xCare ওয়েব ডিজাইন (লিংক ফিক্সড) ---
@app.route('/')
def home():
    # সরাসরি টেলিগ্রাম অ্যাপ ওপেন করার জন্য 'tg://resolve' লিংক ব্যবহার করা হয়েছে
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #0b1528; color: white; font-family: sans-serif; margin: 0; }
            .card-bg { background: #16243d; border-radius: 16px; border: 1px solid rgba(255,255,255,0.15); transition: 0.4s; cursor: pointer; }
            .card-bg:active { transform: scale(0.95); }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="max-w-sm w-full space-y-8 text-center">
            <h1 class="text-5xl font-black italic text-blue-500 tracking-tighter">xCare</h1>
            
            <div class="space-y-4">
                <a href="tg://resolve?domain=xcaresupport_bot" class="block no-underline">
                    <div class="card-bg p-6 flex items-center justify-between">
                        <div class="flex items-center gap-4 text-left">
                            <span class="text-3xl">💬</span>
                            <div>
                                <p class="font-bold text-xl text-white">Operator Chat</p>
                                <p class="text-xs text-gray-400">Direct bot support</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                             <span class="w-2 h-2 bg-green-500 rounded-full animate-ping"></span>
                             <span class="text-green-400 font-bold uppercase text-xs">Online</span>
                        </div>
                    </div>
                </a>

                <div class="card-bg p-6 flex justify-between items-center text-left opacity-70">
                    <div class="flex items-center gap-4">
                        <span class="text-3xl">👑</span>
                        <div>
                            <p class="text-xl font-bold leading-none">Master Agent</p>
                            <p class="text-xs text-gray-400 mt-1">Management</p>
                        </div>
                    </div>
                </div>
            </div>

            <footer class="pt-8 text-gray-600 text-[10px] uppercase tracking-widest">
                © 2026 xCare Professional Services
            </footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    # বোট আলাদা থ্রেডে চালু
    Thread(target=run_bot, daemon=True).start()
    
    # Render পোর্ট সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
