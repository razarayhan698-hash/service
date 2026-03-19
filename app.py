import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার বোট তথ্য ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "agent" in text:
        bot.reply_to(message, "মাস্টার এজেন্ট হতে চাইলে আমাদের ওয়েবসাইটে বিস্তারিত দেখুন।")
    else:
        bot.reply_to(message, "স্বাগতম! xCare সাপোর্ট আপনার মেসেজটি পেয়েছে।")

def run_bot():
    bot.polling(none_stop=True)

# --- আপনার আগের সেই চমৎকার পেজ ডিজাইন ---
@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare | Customer Support & Agent Program</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #0b1528; color: white; font-family: sans-serif; }}
            .card-bg {{ background: #16243d; border-radius: 12px; transition: 0.3s; }}
            .card-bg:hover {{ background: #1c2e4d; }}
        </style>
    </head>
    <body class="p-6">
        <div class="max-w-md mx-auto space-y-8">
            <div class="flex justify-between items-center">
                <h1 class="text-3xl font-bold italic">xCare</h1>
                <div class="space-x-2">
                    <button class="bg-blue-600 px-4 py-1 rounded">Log in</button>
                    <button class="bg-green-500 px-4 py-1 rounded">Registration</button>
                </div>
            </div>

            <section>
                <h2 class="text-blue-400 font-bold mb-4">Customer Support</h2>
                <div class="space-y-4">
                    <div class="card-bg p-4 flex items-center justify-between">
                        <div class="flex items-center gap-4">
                            <span class="text-2xl">💬</span>
                            <div><p class="font-bold">Operator Chat</p><p class="text-xs text-gray-400">Direct text chat</p></div>
                        </div>
                        <span class="text-green-400 text-xs">Online</span>
                    </div>
                    
                    <a href="https://t.me/xcaresupport_bot" class="block">
                        <div class="card-bg p-4 flex items-center justify-between">
                            <div class="flex items-center gap-4">
                                <span class="text-2xl">🤖</span>
                                <div><p class="font-bold">Telegram Bot</p><p class="text-xs text-gray-400">Auto-support services</p></div>
                            </div>
                            <span>></span>
                        </div>
                    </a>
                </div>
            </section>

            <section>
                <h2 class="text-blue-400 font-bold mb-4 uppercase text-sm tracking-widest">Official Agent Program</h2>
                <div class="space-y-4">
                    <div class="card-bg p-6 flex justify-between items-center">
                        <div><p class="text-xl font-bold">Master Agent</p><p class="text-xs text-gray-400">Distribution Management</p></div>
                        <span class="text-2xl">👑</span>
                    </div>
                    <div class="card-bg p-6 flex justify-between items-center text-green-400">
                        <div><p class="text-xl font-bold">E-Wallet Agent</p><p class="text-xs text-gray-400">Payment Processing</p></div>
                        <span class="text-2xl">৳</span>
                    </div>
                    <div class="card-bg p-6 flex justify-between items-center text-purple-400">
                        <div><p class="text-xl font-bold">MoneyGo Agent</p><p class="text-xs text-gray-400">VIP Deposit Elite</p></div>
                        <span class="text-2xl">💎</span>
                    </div>
                </div>
            </section>

            <footer class="text-center text-gray-500 text-xs space-y-1">
                <p>VERIFIED SUPPORT PARTNER</p>
                <p>© 2026 xCare Professional Services</p>
            </footer>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
