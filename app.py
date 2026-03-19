import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# আপনার সঠিক বোট টোকেন
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক যা আপনার সমস্যার সমাধান করবে ---
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()
    if "hi" in text or "hello" in text or "হাই" in text or "হ্যালো" in text:
        bot.reply_to(message, "হ্যালো স্যার! 👋 xCare সাপোর্ট লাইনে আপনাকে স্বাগতম। 😊")
    elif "agent" in text or "এজেন্ট" in text:
        bot.reply_to(message, "👑 মাস্টার এজেন্ট হতে চাইলে আপনার ফোন নম্বরটি এখানে দিন।")
    else:
        bot.reply_to(message, "আপনার মেসেজটি আমাদের অপারেটরের কাছে পৌঁছেছে। ✨")

def run_bot():
    # এটি আপনার বোটকে সবসময় সচল রাখবে
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

# --- আপনার সেই চমৎকার নীল রঙের পেজ ---
@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #0b1528; color: white; }}
            .card-bg {{ background: #16243d; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); }}
        </style>
    </head>
    <body class="p-6">
        <div class="max-w-md mx-auto space-y-6">
            <h1 class="text-3xl font-bold italic text-center">xCare</h1>
            <a href="https://t.me/xcaresupport_bot" class="block">
                <div class="card-bg p-6 flex items-center justify-between">
                    <div class="flex items-center gap-4">
                        <span class="text-3xl">💬</span>
                        <div><p class="font-bold">Operator Chat</p><p class="text-xs text-gray-400">Direct bot support</p></div>
                    </div>
                    <span class="text-green-400 font-bold animate-pulse">Online</span>
                </div>
            </a>
            <div class="card-bg p-6 flex justify-between items-center text-white">
                <div><p class="text-xl font-bold">Master Agent</p><p class="text-xs text-gray-400">Distribution Management</p></div>
                <span class="text-3xl">👑</span>
            </div>
            <footer class="text-center pt-8 text-gray-600 text-[10px]">
                © 2026 xCare Professional Services
            </footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    # বোটকে আলাদাভাবে চালু করা
    Thread(target=run_bot, daemon=True).start()
    
    # আপনার লগের পোর্টের সাথে মিল রেখে সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
