import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার টেলিগ্রাম বোটের তথ্য ---
# Bot ID/Token: 8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "hi" in text or "hello" in text or "হাই" in text:
        bot.reply_to(message, "হ্যালো! xCare সাপোর্ট লাইনে আপনাকে স্বাগতম। 😊")
    elif "agent" in text or "এজেন্ট" in text:
        bot.reply_to(message, "👑 আমাদের মাস্টার এজেন্ট হতে চাইলে আপনার ফোন নম্বরটি এখানে দিন।")
    else:
        bot.reply_to(message, "আপনার মেসেজটি আমাদের অপারেটরের কাছে পৌঁছেছে। ✨")

def run_bot():
    # বোটকে সচল রাখার জন্য
    bot.infinity_polling()

# --- আপনার ওয়েবসাইট ডিজাইন ---
@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare | Support & Agent</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #0b1528; color: white; font-family: sans-serif; }}
            .card-bg {{ background: #16243d; border-radius: 12px; transition: 0.3s; border: 1px solid rgba(255,255,255,0.05); }}
            .card-bg:hover {{ background: #1c2e4d; border-color: #3b82f6; }}
        </style>
    </head>
    <body class="p-6">
        <div class="max-w-md mx-auto space-y-8">
            <div class="flex justify-between items-center">
                <h1 class="text-3xl font-bold italic">xCare</h1>
                <div class="space-x-2">
                    <button class="bg-blue-600 px-4 py-1 rounded text-sm font-bold">Log in</button>
                    <button class="bg-green-500 px-4 py-1 rounded text-sm font-bold">Registration</button>
                </div>
            </div>
            <section>
                <h2 class="text-blue-400 font-bold mb-4 text-sm">CUSTOMER SUPPORT</h2>
                <div class="space-y-4">
                    <a href="https://t.me/xcaresupport_bot" class="block">
                        <div class="card-bg p-4 flex items-center justify-between">
                            <div class="flex items-center gap-4">
                                <div class="bg-blue-900/50 p-3 rounded-full text-2xl">💬</div>
                                <div><p class="font-bold">Operator Chat</p><p class="text-xs text-gray-400">Direct text chat</p></div>
                            </div>
                            <span class="text-green-400 text-xs font-bold animate-pulse">Online</span>
                        </div>
                    </a>
                </div>
            </section>
            <section>
                <h2 class="text-blue-400 font-bold mb-4 uppercase text-xs tracking-widest">OFFICIAL AGENT PROGRAM</h2>
                <div class="space-y-4">
                    <div class="card-bg p-6 flex justify-between items-center">
                        <div><p class="text-xl font-bold text-white">Master Agent</p><p class="text-xs text-gray-400 text-white">Distribution Management</p></div>
                        <span class="text-3xl">👑</span>
                    </div>
                </div>
            </section>
            <footer class="text-center pt-8">
                <p class="text-gray-500 text-[10px] uppercase font-bold">Verified Support Partner</p>
                <p class="text-gray-600 text-[10px]">© 2026 xCare Professional Services</p>
            </footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    # বোটকে ব্যাকগ্রাউন্ডে চালানো
    Thread(target=run_bot, daemon=True).start()
    
    # Render পোর্টের জন্য ফিক্স
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
