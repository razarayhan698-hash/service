import os
import telebot
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার বোট তথ্য ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! xCare অটো-সাপোর্ট এখন চালু আছে।")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "agent" in text:
        bot.reply_to(message, "মাস্টার এজেন্ট হতে চাইলে আমাদের ওয়েবসাইটে ফরমটি দেখুন।")
    else:
        bot.reply_to(message, "আপনার মেসেজটি পেয়েছি। দ্রুতই রিপ্লাই দেওয়া হবে।")

def run_bot():
    bot.polling(none_stop=True)

# --- আপনার প্রিমিয়াম ডিজাইন ---
@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare | Professional Support</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #030712; color: white; }}
            .premium-card {{ background: linear-gradient(135deg, #1a1f2e 0%, #0f1419 100%); border: 1px solid rgba(255, 255, 255, 0.1); }}
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen">
        <div class="premium-card p-10 rounded-2xl shadow-2xl text-center max-w-sm">
            <h1 class="text-4xl font-bold text-blue-400 mb-4">xCare</h1>
            <p class="text-gray-400 mb-6">Bot Service is active & responding</p>
            <a href="https://t.me/xcaresupport_bot" class="bg-blue-600 px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition">Open Telegram Bot</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
