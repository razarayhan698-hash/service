import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- আপনার টেলিগ্রাম লিঙ্ক (সব বাটনের জন্য একই লিঙ্ক রাখা হয়েছে) ---
TELEGRAM_BOT_URL = "https://t.me/Instantpayment24_bot"

@app.route('/')
def home():
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agent Portal | xCare Official</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
        <style>
            body {{ background-color: #020617; color: white; font-family: 'Inter', sans-serif; }}
            .glass-card {{
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.08);
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            }}
            .btn-master {{ background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }}
            .btn-wallet {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); }}
            .btn-moneygo {{ background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); }}
            .status-dot {{
                width: 8px;
                height: 8px;
                background-color: #22c55e;
                border-radius: 50%;
                display: inline-block;
                margin-right: 6px;
                box-shadow: 0 0 8px #22c55e;
                animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
                0% {{ opacity: 1; }}
                50% {{ opacity: 0.5; }}
                100% {{ opacity: 1; }}
            }}
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-6">
        <div class="glass-card rounded-3xl p-8 w-full max-w-md text-center">
            <!-- Logo Area -->
            <div class="mb-6">
                <h1 style="font-family: 'Playfair Display', serif;" class="text-5xl font-bold tracking-tighter text-white">xC</h1>
                <div class="mt-2 text-[10px] uppercase tracking-[0.3em] text-blue-400 font-semibold">Official Support System</div>
            </div>

            <h2 class="text-xl font-semibold mb-8 text-gray-200">Select Agent Category</h2>
            
            <!-- Info Labels -->
            <div class="flex justify-between mb-8 px-2">
                <div class="text-left">
                    <p class="text-[10px] text-gray-500 uppercase font-bold">System Status</p>
                    <p class="text-sm font-medium text-white"><span class="status-dot"></span>Online</p>
                </div>
                <div class="text-right">
                    <p class="text-[10px] text-gray-500 uppercase font-bold">Response Time</p>
                    <p class="text-sm font-medium text-white">Instant</p>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="space-y-4">
                <!-- Master Agent Button -->
                <a href="{TELEGRAM_BOT_URL}" class="btn-master flex items-center justify-between p-4 rounded-2xl transition hover:scale-[1.02] active:scale-95 shadow-lg group" style="text-decoration: none;">
                    <div class="text-left">
                        <p class="text-white font-bold text-lg">Master Agent</p>
                        <p class="text-blue-100 text-xs">Full distribution control</p>
                    </div>
                    <span class="text-2xl group-hover:translate-x-1 transition-transform">👑</span>
                </a>

                <!-- E-Wallet Agent Button -->
                <a href="{TELEGRAM_BOT_URL}" class="btn-wallet flex items-center justify-between p-4 rounded-2xl transition hover:scale-[1.02] active:scale-95 shadow-lg group" style="text-decoration: none;">
                    <div class="text-left">
                        <p class="text-white font-bold text-lg">E-Wallet Agent</p>
                        <p class="text-green-100 text-xs">Bkash, Nagad, Rocket local</p>
                    </div>
                    <span class="text-2xl group-hover:translate-x-1 transition-transform">৳</span>
                </a>

                <!-- MoneyGo Agent Button -->
                <a href="{TELEGRAM_BOT_URL}" class="btn-moneygo flex items-center justify-between p-4 rounded-2xl transition hover:scale-[1.02] active:scale-95 shadow-lg group" style="text-decoration: none;">
                    <div class="text-left">
                        <p class="text-white font-bold text-lg">MoneyGo Agent</p>
                        <p class="text-purple-100 text-xs">Global VIP deposit system</p>
                    </div>
                    <span class="text-2xl group-hover:translate-x-1 transition-transform">💎</span>
                </a>
            </div>
            
            <div class="mt-8 pt-6 border-t border-white/5">
                <p class="text-[10px] text-gray-500 uppercase tracking-widest font-bold mb-1">Official Verification</p>
                <p class="text-xs text-blue-400/80 italic">Verified Partner | Premium Elite Support Tier</p>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
