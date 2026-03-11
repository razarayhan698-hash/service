import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- আপনার সঠিক তথ্য ---
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot" 
# ---------------------

@app.route('/')
def home():
    # নিচের কোডটি সাবধানে পুরোটা কপি করুন
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Master Agent Card | xCare</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
        <style>
            * {{ font-family: 'Inter', sans-serif; }}
            h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', serif; }}
            .master-card {{
                background: linear-gradient(135deg, #1a1f2e 0%, #141922 50%, #0f1419 100%);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            .shadow-premium {{
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(20, 160, 255, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            }}
            .badge-glow {{ box-shadow: 0 0 20px rgba(34, 197, 94, 0.6); }}
            .card-hover:hover {{
                transform: translateY(-8px);
                box-shadow: 0 35px 60px -12px rgba(0, 0, 0, 0.6), 0 0 50px rgba(20, 160, 255, 0.25);
            }}
            .accent-gradient {{ background: linear-gradient(135deg, #14A0FF 0%, #0C8BCC 100%); }}
        </style>
    </head>
    <body class="bg-gray-950">
        <div class="flex items-center justify-center min-h-screen p-4">
            <div class="master-card shadow-premium card-hover rounded-2xl p-8 w-full max-w-md transition-all duration-300">
                <div class="flex items-start justify-between mb-6">
                    <div class="flex-1">
                        <h2 class="text-3xl font-bold text-white mb-1">Master Agent</h2>
                        <p class="text-sm text-gray-400">Elite Partnership Program</p>
                    </div>
                    <div class="badge-glow w-10 h-10 bg-gradient-to-br from-green-400 to-green-600 rounded-full flex items-center justify-center">
                        <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                        </svg>
                    </div>
                </div>
                <div class="space-y-4 mb-8">
                    <div class="flex items-center gap-3">
                        <div class="w-1 h-6 accent-gradient rounded-full flex-shrink-0"></div>
                        <div>
                            <p class="text-sm text-gray-300 font-medium">Commission Rate</p>
                            <p class="text-lg font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-400">Up to 45%</p>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-3 gap-4 mb-8">
                    <div class="text-center p-3 rounded-lg bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700">
                        <p class="text-xs text-gray-400 mb-1">Active Users</p>
