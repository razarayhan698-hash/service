import os
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- আপনার টেলিগ্রাম বোটের তথ্য এখানে দিন ---
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # @BotFather থেকে পাওয়া টোকেন দিন
ADMIN_CHAT_ID = "YOUR_CHAT_ID_HERE" # আপনার টেলিগ্রাম চ্যাট আইডি দিন

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": ADMIN_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

@app.route('/')
def home():
    # মূল হোম পেজ যেখানে তিনটি ক্যাটাগরি আছে
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
            .btn-apply { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="glass-card rounded-3xl p-8 w-full max-w-md text-center">
            <h1 class="text-5xl font-bold mb-2">xC</h1>
            <p class="text-blue-400 text-xs uppercase tracking-widest mb-8">Official Agent Application</p>
            
            <div class="space-y-4">
                <a href="/apply/Master-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-blue-500 transition-all text-left group">
                    <p class="font-bold text-lg">Master Agent</p>
                    <p class="text-xs text-gray-400">Apply for top-level distribution</p>
                </a>
                <a href="/apply/E-Wallet-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-green-500 transition-all text-left">
                    <p class="font-bold text-lg text-green-400">E-Wallet Agent</p>
                    <p class="text-xs text-gray-400">Local Bkash/Nagad/Rocket services</p>
                </a>
                <a href="/apply/MoneyGo-Agent" class="block p-4 rounded-2xl bg-gray-800/50 border border-white/5 hover:border-purple-500 transition-all text-left">
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
    # অ্যাপ্লিকেশন ফর্ম পেজ
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Apply for {agent_type}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #020617; color: white; font-family: 'Inter', sans-serif; }}
            input {{ background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important; color: white !important; }}
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="bg-gray-900 rounded-3xl p-8 w-full max-w-md border border-white/10 shadow-2xl">
            <h2 class="text-2xl font-bold mb-2">Apply for {agent_type}</h2>
            <p class="text-gray-400 text-sm mb-8">সবগুলো তথ্য সঠিকভাবে পূরণ করুন।</p>
            
            <form action="/submit" method="POST" class="space-y-5">
                <input type="hidden" name="category" value="{agent_type}">
                
                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">আপনার দেশ (Country)</label>
                    <input type="text" name="country" required placeholder="Ex: Bangladesh" class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>

                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">টেলিগ্রাম ইউজারনেম (Telegram Username)</label>
                    <input type="text" name="username" required placeholder="Ex: @username" class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>

                <div>
                    <label class="block text-xs font-bold text-gray-500 uppercase mb-2">টেলিগ্রাম নাম্বার (Telegram Number)</label>
                    <input type="tel" name="phone" required placeholder="Ex: +88017..." class="w-full p-4 rounded-xl focus:outline-none focus:border-blue-500">
                </div>

                <button type="submit" class="w-full py-4 bg-blue-600 rounded-xl font-bold hover:bg-blue-700 transition-all shadow-lg shadow-blue-500/20">
                    আবেদন জমা দিন (Submit Application)
                </button>
            </form>
            
            <a href="/" class="block text-center mt-6 text-gray-500 text-sm underline">পিছনে যান</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/submit', methods=['POST'])
def submit():
    # ফর্ম সাবমিট করার পর কাজ
    category = request.form.get('category')
    country = request.form.get('country')
    username = request.form.get('username')
    phone = request.form.get('phone')

    # টেলিগ্রামে মেসেজ পাঠানো
    msg = f"<b>🔔 New Agent Application</b>\n\n" \
          f"<b>Type:</b> {category}\n" \
          f"<b>Country:</b> {country}\n" \
          f"<b>Username:</b> {username}\n" \
          f"<b>Phone:</b> {phone}"
    
    send_to_telegram(msg)

    # ইউজারকে ধন্যবাদ জানানো
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-950 flex items-center justify-center min-h-screen p-6 text-white text-center">
        <div class="max-w-md">
            <div class="text-6xl mb-6">✅</div>
            <h2 class="text-3xl font-bold mb-4">আবেদন সফল হয়েছে!</h2>
            <p class="text-gray-400 leading-relaxed mb-8">
                আপনার তথ্য আমাদের কাছে পৌঁছেছে। আমাদের অফিসিয়াল পতিনিধি আগামী <b>৪৮ ঘন্টার</b> ভিতরে আপনার টেলিগ্রামে মেসেজ দিবে। অনুগ্রহ করে অপেক্ষা করুন।
            </p>
            <a href="/" class="px-8 py-3 bg-blue-600 rounded-full font-bold">হোম পেজে ফিরুন</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
