import os
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- Configuration ---
BOT_TOKEN = "8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk"
ADMIN_CHAT_ID = "6471355638"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": ADMIN_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agent Portal | xCare Official</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #020617; color: white; font-family: sans-serif; }
            .glass-card { background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="glass-card rounded-3xl p-8 w-full max-w-md text-center">
            <h1 class="text-6xl font-bold mb-2 text-white">xC</h1>
            <p class="text-blue-400 text-xs uppercase tracking-widest mb-10 font-bold">Official Agent Application</p>
            <div class="space-y-4">
                <a href="/apply/Master-Agent" class="block p-5 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-blue-500 transition-all text-left" style="text-decoration: none;">
                    <p class="font-bold text-lg text-white">Master Agent</p>
                    <p class="text-xs text-gray-400">Apply for top-level distribution</p>
                </a>
                <a href="/apply/E-Wallet-Agent" class="block p-5 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-green-500 transition-all text-left" style="text-decoration: none;">
                    <p class="font-bold text-lg text-green-400">E-Wallet Agent</p>
                    <p class="text-xs text-gray-400">Local Payment Gateway services</p>
                </a>
                <a href="/apply/MoneyGo-Agent" class="block p-5 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-purple-500 transition-all text-left" style="text-decoration: none;">
                    <p class="font-bold text-lg text-purple-400">MoneyGo Agent</p>
                    <p class="text-xs text-gray-400">Global VIP deposit system</p>
                </a>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/apply/<agent_type>')
def apply_form(agent_type):
    # CSS ব্র্যাকেট ডাবল {{ }} করা হয়েছে f-string এর জন্য
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Apply for {agent_type}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #020617; color: white; }}
            input {{ background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important; color: white !important; }}
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="bg-gray-900 rounded-3xl p-8 w-full max-w-md border border-white/10 shadow-2xl">
            <h2 class="text-2xl font-bold mb-2">Apply for {agent_type}</h2>
            <p class="text-gray-400 text-sm mb-8">Please fill in all the details correctly.</p>
            <form action="/submit" method="POST" class="space-y-5">
                <input type="hidden" name="category" value="{agent_type}">
                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">Country</label>
                    <input type="text" name="country" required placeholder="Enter your country" class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">Telegram Username</label>
                    <input type="text" name="username" required placeholder="Example: @username" class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">Telegram Number</label>
                    <input type="tel" name="phone" required placeholder="Example: +880..." class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full py-4 bg-blue-600 rounded-xl font-bold hover:bg-blue-700 transition-all shadow-lg">
                    Submit Application
                </button>
            </form>
            <a href="/" class="block text-center mt-6 text-gray-500 text-sm underline">Go Back</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/submit', methods=['POST'])
def submit():
    cat = request.form.get('category')
    country = request.form.get('country')
    user = request.form.get('username')
    phone = request.form.get('phone')
    
    msg = f"<b>🔔 NEW APPLICATION</b>\\n\\n" \
          f"<b>Category:</b> {cat}\\n" \
          f"<b>Country:</b> {country}\\n" \
          f"<b>Telegram:</b> {user}\\n" \
          f"<b>Phone:</b> {phone}"
    
    send_to_telegram(msg)
    
    html_content = '''
    <body style="background:#020617; color:white; font-family:sans-serif; display:flex; align-items:center; justify-content:center; min-height:100vh; text-align:center; padding:20px;">
        <div>
            <h2 style="font-size:2rem; margin-bottom:1rem;">✅ Application Submitted!</h2>
            <p style="color:#9ca3af; margin-bottom:2rem;">Our representative will contact you via Telegram within <b>48 hours</b>.</p>
            <a href="/" style="padding:12px 30px; background:#2563eb; border-radius:30px; color:white; text-decoration:none; font-weight:bold;">Return to Home</a>
        </div>
    </body>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
