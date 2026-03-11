import os
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- Configuration (Your Credentials) ---
BOT_TOKEN = "8615529799:AAEK6NoKaghTS8CoReD_RqzugLwHoxUahNk"
ADMIN_CHAT_ID = "6471355638"
TELEGRAM_SUPPORT_LINK = "https://t.me/xcaresupport_bot" # Your Support Bot link

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": ADMIN_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Support Hub | xCare Official</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {{ background-color: #0d2137; color: white; font-family: 'Inter', sans-serif; }}
            .header-bg {{ background-color: #0b1a2a; border-bottom: 1px solid #1e3a5a; }}
            .card-bg {{ background-color: #1a2c4e; border: 1px solid #2a416a; }}
            .btn-login {{ background-color: #3b82f6; }}
            .btn-reg {{ background-color: #22c55e; }}
            .support-icon {{ background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3); }}
        </style>
    </head>
    <body>
        <!-- Header -->
        <header class="header-bg p-4 flex justify-between items-center sticky top-0 z-50">
            <h1 class="text-2xl font-black tracking-tighter text-white">xCare</h1>
            <div class="flex gap-2">
                <button class="btn-login px-4 py-1.5 rounded font-bold text-sm">Log in</button>
                <button class="btn-reg px-4 py-1.5 rounded font-bold text-sm text-gray-900">Registration</button>
            </div>
        </header>

        <main class="p-6 max-w-lg mx-auto">
            <h2 class="text-xl font-bold mb-6 text-blue-400">Customer Support</h2>
            
            <!-- Support Channels -->
            <div class="space-y-3 mb-10">
                <div class="card-bg p-4 rounded-xl flex items-center justify-between cursor-pointer hover:bg-[#21375a] transition">
                    <div class="flex items-center gap-4">
                        <div class="support-icon w-12 h-12 rounded-full flex items-center justify-center text-xl">💬</div>
                        <div>
                            <p class="font-bold">Operator Chat</p>
                            <p class="text-xs text-gray-400">Direct text chat</p>
                        </div>
                    </div>
                    <span class="text-green-500 text-xs font-bold">Online</span>
                </div>

                <a href="{TELEGRAM_SUPPORT_LINK}" class="card-bg p-4 rounded-xl flex items-center justify-between hover:bg-[#21375a] transition block" style="text-decoration: none;">
                    <div class="flex items-center gap-4">
                        <div class="support-icon w-12 h-12 rounded-full flex items-center justify-center text-xl text-white">🤖</div>
                        <div class="text-white">
                            <p class="font-bold">Telegram Bot</p>
                            <p class="text-xs text-gray-400">Auto-support services</p>
                        </div>
                    </div>
                    <span class="text-gray-400 text-lg">›</span>
                </a>
            </div>

            <!-- Agent Section -->
            <h2 class="text-xl font-bold mb-6 text-blue-400 uppercase tracking-wider text-sm">Official Agent Program</h2>
            <div class="grid grid-cols-1 gap-3">
                <a href="/apply/Master-Agent" class="card-bg p-5 rounded-2xl flex items-center justify-between group" style="text-decoration: none;">
                    <div>
                        <p class="font-bold text-lg text-white">Master Agent</p>
                        <p class="text-xs text-gray-400">Distribution Management</p>
                    </div>
                    <span class="text-2xl opacity-50 group-hover:opacity-100 transition">👑</span>
                </a>
                
                <a href="/apply/E-Wallet-Agent" class="card-bg p-5 rounded-2xl flex items-center justify-between group" style="text-decoration: none;">
                    <div>
                        <p class="font-bold text-lg text-green-400">E-Wallet Agent</p>
                        <p class="text-xs text-gray-400">Payment Processing</p>
                    </div>
                    <span class="text-2xl opacity-50 group-hover:opacity-100 transition">৳</span>
                </a>

                <a href="/apply/MoneyGo-Agent" class="card-bg p-5 rounded-2xl flex items-center justify-between group" style="text-decoration: none;">
                    <div>
                        <p class="font-bold text-lg text-purple-400">MoneyGo Agent</p>
                        <p class="text-xs text-gray-400">VIP Deposit Elite</p>
                    </div>
                    <span class="text-2xl opacity-50 group-hover:opacity-100 transition">💎</span>
                </a>
            </div>

            <footer class="mt-12 text-center border-t border-gray-800 pt-6">
                <p class="text-[10px] text-gray-500 font-bold uppercase tracking-[3px] mb-2">Verified Support Partner</p>
                <p class="text-xs text-gray-600">© 2026 xCare Professional Services</p>
            </footer>
        </main>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/apply/<agent_type>')
def apply_form(agent_type):
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Apply - {agent_type}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #0d2137; color: white; font-family: 'Inter', sans-serif; }}
            input {{ background: #1a2c4e !important; border: 1px solid #2a416a !important; color: white !important; }}
        </style>
    </head>
    <body class="p-6 flex items-center justify-center min-h-screen">
        <div class="bg-[#111f32] p-8 rounded-3xl w-full max-w-md border border-gray-800">
            <h2 class="text-2xl font-bold mb-2">Apply for {agent_type}</h2>
            <p class="text-gray-400 text-sm mb-8">Official recruitment department</p>
            
            <form action="/submit" method="POST" class="space-y-5">
                <input type="hidden" name="category" value="{agent_type}">
                <div>
                    <label class="text-[10px] font-bold text-gray-500 uppercase block mb-1">Country</label>
                    <input type="text" name="country" required class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="text-[10px] font-bold text-gray-500 uppercase block mb-1">Telegram Username</label>
                    <input type="text" name="username" required placeholder="@username" class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="text-[10px] font-bold text-gray-500 uppercase block mb-1">Telegram Number</label>
                    <input type="tel" name="phone" required placeholder="+880..." class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full py-4 bg-blue-600 rounded-xl font-bold hover:bg-blue-700 transition shadow-xl">
                    Submit Application
                </button>
            </form>
            <a href="/" class="block text-center mt-6 text-gray-500 text-sm underline">Cancel</a>
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
    
    msg = f"<b>🔔 NEW AGENT APPLICATION</b>\\n\\n" \
          f"<b>Category:</b> {cat}\\n" \
          f"<b>Country:</b> {country}\\n" \
          f"<b>Telegram:</b> {user}\\n" \
          f"<b>Phone:</b> {phone}"
    
    send_to_telegram(msg)
    
    html_content = '''
    <body style="background:#0d2137; color:white; font-family:sans-serif; display:flex; align-items:center; justify-content:center; min-height:100vh; text-align:center; padding:20px;">
        <div>
            <div style="font-size:4rem; margin-bottom:1rem;">✅</div>
            <h2 style="font-size:1.8rem; margin-bottom:1rem; font-weight:bold;">Application Received!</h2>
            <p style="color:#94a3b8; line-height:1.6; margin-bottom:2rem;">Our official representative will contact you via Telegram within <b>48 hours</b>. Please keep your profile active.</p>
            <a href="/" style="padding:12px 35px; background:#22c55e; border-radius:10px; color:black; text-decoration:none; font-weight:bold;">Return to Home</a>
        </div>
    </body>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
