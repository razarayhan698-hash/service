import os
import telebot
import time
from flask import Flask, render_template_string
from threading import Thread

app = Flask(__name__)

# --- আপনার নতুন সঠিক টোকেন ---
API_TOKEN = '8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk'
bot = telebot.TeleBot(API_TOKEN)

# --- অটো-রিপ্লাই লজিক ---
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        if not message.text: return
        text = message.text.lower()
        
        if any(word in text for word in ["hi", "hello", "হাই", "হ্যালো"]):
            bot.reply_to(message, "হ্যালো স্যার! 👋 xCare সাপোর্ট লাইনে আপনাকে স্বাগতম। 😊")
        elif any(word in text for word in ["agent", "এজেন্ট"]):
            bot.reply_to(message, "👑 মাস্টার এজেন্ট হতে চাইলে আপনার ফোন নম্বরটি এখানে দিন।")
        else:
            bot.reply_to(message, "আপনার মেসেজটি আমাদের অপারেটরের কাছে পৌঁছেছে। ✨")
    except Exception as e:
        print(f"Bot Reply Error: {e}")

def run_bot():
    while True:
        try:
            bot.remove_webhook(drop_pending_updates=True) # পুরনো জ্যাম পরিষ্কার করা
            time.sleep(1)
            print("Telegram Bot is active...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Connection Error: {e}")
            time.sleep(5)

# --- আপনার সেই ডার্ক ব্লু ওয়েব ডিজাইন ---
@app.route('/')
def home():
    return render_template_string('''
    <body style="background-color:#0b1528; color:white; font-family:sans-serif; text-align:center; padding-top:100px;">
        <h1 style="color:#3b82f6; font-size:48px; font-style:italic;">xCare</h1>
        <div style="background:#16243d; border:1px solid #3b82f6; border-radius:15px; width:300px; margin:20px auto; padding:30px;">
            <p style="color:#4ade80; font-weight:bold;">SYSTEM ONLINE</p>
            <p style="font-size:12px; color:#9ca3af;">Bot Token: Connected</p>
            <br>
            <a href="https://t.me/xcaresupport_bot" style="background:#2563eb; color:white; padding:12px 25px; text-decoration:none; border-radius:8px; font-weight:bold;">START BOT</a>
        </div>
        <p style="color:#4b5563; font-size:10px; margin-top:50px;">© 2026 xCare Professional Services</p>
    </body>
    ''')

if __name__ == "__main__":
    # বোটকে আলাদাভাবে চালু করা
    Thread(target=run_bot, daemon=True).start()
    
    # Render-এর জন্য সঠিক পোর্ট সেটিংস
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
