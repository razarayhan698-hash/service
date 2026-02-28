from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xCare Support</title>
        <link rel="manifest" href="/manifest.json">
        <meta name="theme-color" content="#004793">
        <style>
            /* Splash Screen Styling */
            #splash {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: #004793; display: flex; flex-direction: column;
                justify-content: center; align-items: center; z-index: 9999;
            }
            .splash-logo { width: 150px; margin-bottom: 20px; }
            
            /* Loading Dots Animation (আপনার ভিডিওর মতো) */
            .loader { display: flex; gap: 8px; }
            .dot { width: 12px; height: 12px; background: rgba(255,255,255,0.4); border-radius: 50%; animation: load 1.2s infinite ease-in-out; }
            .dot:nth-child(2) { animation-delay: 0.2s; }
            .dot:nth-child(3) { animation-delay: 0.4s; }
            .dot:nth-child(4) { animation-delay: 0.6s; }
            .dot:nth-child(5) { animation-delay: 0.8s; }
            @keyframes load { 0%, 100% { background: rgba(255,255,255,0.4); transform: scale(1); } 50% { background: #fff; transform: scale(1.3); } }

            /* Main UI Styling */
            body { font-family: sans-serif; background-color: #f4f7f9; margin: 0; padding: 20px; color: #333; }
            .header { color: #004793; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 25px; }
            .card { background: white; border-radius: 12px; padding: 18px; margin-bottom: 12px; display: flex; align-items: center; text-decoration: none; color: inherit; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
            .icon { font-size: 24px; margin-right: 15px; color: #004793; width: 35px; text-align: center; }
            .text-content b { display: block; font-size: 16px; }
            .text-content span { color: #888; font-size: 13px; }
            .btn-login { background: #4a90e2; color: white; padding: 15px; width: 100%; border-radius: 30px; font-size: 18px; margin-top: 30px; text-align: center; display: block; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div id="splash">
            <img src="https://i.imgur.com/your_logo_link.png" class="splash-logo"> <div class="loader">
                <div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div>
            </div>
        </div>

        <div class="header">xCare</div>
        <div style="font-size: 20px; margin-bottom: 15px; font-weight: bold;">Support</div>
        
        <a href="https://t.me/YOUR_USERNAME" class="card">
            <div class="icon">💬</div>
            <div class="text-content"><b>Operator chat</b><span>Text chat</span></div>
        </a>
        <a href="tel:+8801XXXXXXXXX" class="card">
            <div class="icon">🎧</div>
            <div class="text-content"><b>Call back</b><span>Order callback</span></div>
        </a>
        <div class="card"><div class="icon">🎤</div><div class="text-content"><b>Online call</b><span>IP call</span></div></div>
        <div class="card"><div class="icon">📱</div><div class="text-content"><b>Contacts</b><span>E-mail, phone, etc</span></div></div>
        
        <a href="#" class="btn-login">Log in</a>

        <script>
            // ২ সেকেন্ড পর Splash Screen সরিয়ে অ্যাপ দেখাবে
            setTimeout(() => {
                document.getElementById('splash').style.display = 'none';
            }, 2500);

            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/sw.js');
            }
        </script>
    </body>
    </html>
    '''

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory(os.getcwd(), 'sw.js')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
