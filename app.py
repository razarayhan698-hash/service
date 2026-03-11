import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- আপনার সঠিক তথ্য ---
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot" 
# ---------------------

@app.route('/')
def home():
    # এখানে f''' শুরু হয়েছে, তাই CSS ব্র্যাকেটগুলো {{ }} হতে হবে
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Master Agent Portal | xCare</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
        <style>
            body {{ background-color: #030712; color: white; font-family: 'Inter', sans-serif; }}
            .master-card {{
                background: linear-gradient(135deg, #1a1f2e 0%, #0f1419 100%);
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            }}
            .accent-gradient {{ background: linear-gradient(135deg, #14A0FF 0%, #0C8BCC 100%); }}
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-4">
        <div class="master-card rounded-2xl p-8 w-full max-w-md text-center">
            <h1 style="font-family: 'Playfair Display', serif;" class="text-4xl font-bold mb-2">xC</h1>
            <h2 class="text-2xl font-bold mb-6">Master Agent Portal</h2>
            
            <div class="space-y-4 mb-8 text-left">
                <div class="p-4 bg-gray-900 rounded-lg border border-gray-800">
                    <p class="text-sm text-gray-400">Commission Rate</p>
                    <p class="text-xl font-bold text-blue-400">Up to 45%</p>
                </div>
                <div class="p-4 bg-gray-900 rounded-lg border border-gray-800">
                    <p class="text-sm text-gray-400">Support Status</p>
                    <p class="text-xl font-bold text-green-400">● 24/7 Online</p>
                </div>
            </div>

            <a href="{TELEGRAM_BOT_URL}" class="block w-full accent-gradient text-white font-bold py-4 rounded-xl transition hover:scale-105 active:scale-95 shadow-lg" style="text-decoration: none;">
                Become a Master Agent
            </a>
            
            <p class="text-xs text-gray-500 mt-6 italic">Verified Partner | Premium Elite Tier</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    # Render-এর জন্য ডিফল্ট পোর্ট ১০০০০ ব্যবহার করা নিরাপদ
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
