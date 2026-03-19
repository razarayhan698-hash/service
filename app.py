import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার টেলিগ্রাম বোটের তথ্য ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
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
    # বোটকে সচল রাখার জন্য ইনফিটি পোলিং
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

# --- আপনার সেই চমৎকার নীল রঙের ডিজাইন ---
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
            .card-bg {{ background: #16243d; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); transition: 0.3s; }}
            .card-bg:hover {{ border-color: #3b82f6; }}
        </style>
    </head>
    <body class="p-6">
        <div class="max-w-md mx-auto space-y-6 text-center">
            <h1 class="text-4xl font-bold italic text-blue-500">xCare</h1>
            
            <a href="https://t.me/xcaresupport_bot" class="block">
                <div class="card-bg p-6 flex items-center justify-between">
                    <div class="flex items-center gap-4 text-left">
                        <span class="text-3xl">💬</span>
                        <div>
                            <p class="font-bold text-xl">Operator Chat</p>
                            <p class="text-xs text-gray-400">Talk to our live bot</p>
                        </div>
                    </div>
                    <span class="text-green-400 font-bold animate-pulse">Online</span>
                </div>
            </a>

            <div class="card-bg p-6 flex justify-between items-center text-left">
                <div>
                    <p class="text-xl font-bold">Master Agent</p>
                    <p class="text-xs text-gray-400">Distribution Management</p>
                </div>
                <span class="text-3xl">👑</span>
            </div>

            <footer class="pt-10 text-gray-600 text-[10px] uppercase tracking-widest">
                © 2026 xCare Professional Services
            </footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

# --- আপনার চাওয়া অংশটি এখানে যুক্ত করা হলো ---
if __name__ == "__main__":
    # বোট চালু করা
    Thread(target=run_bot, daemon=True).start()
    
    # লগের পোর্টের সাথে মিল রেখে সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
