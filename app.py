from flask import Flask, render_template_string, request, jsonify
import os, requests

app = Flask(__name__)

# আপনার নির্দিষ্ট করা প্রোমো কোড
MY_PROMO_CODE = "1x_2006981" 

# টেলিগ্রাম কনফিগারেশন (আপনার দেওয়া আইডি ও টোকেন)
BOT_TOKEN = "8540257283:AAEqTBD6kJSVozsKmWtZf_l-QQtkJtUuTw"
MY_CHAT_ID = "6529319833"

@app.route('/')
def home():
    # প্রোমো কোড সহ ট্র্যাকিং লিঙ্ক
    reg_url = f"https://1xbet.com/en/registration/?tag={MY_PROMO_CODE}"
    login_url = "https://1xbet.com/en/user/login"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>1xBet Official Partner</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b162c; color: white; margin: 0; padding: 0; }
            
            /* অফিসিয়াল টপ নেভিগেশন */
            .top-nav {
                display: flex; justify-content: space-between; align-items: center;
                padding: 12px 20px; background: #162641; border-bottom: 1px solid #253959;
                position: sticky; top: 0; z-index: 1000;
            }
            .nav-buttons { display: flex; gap: 8px; }
            
            .btn-nav {
                padding: 8px 16px; border-radius:
