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
        <meta name="theme-color" content="#ffffff">
        <style>
            * { box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', sans-serif; 
                background-color: #f4f7f9; 
                margin: 0; padding: 20px; 
                display: flex; flex-direction: column; align-items: center;
            }
            /* Splash Screen Design */
            #splash {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background-color: #2c5e8c; display: flex; flex-direction: column;
                justify-content: center; align-items: center; z-index: 9999;
                transition: opacity 0.5s ease;
            }
            #splash img { width: 150px; margin-bottom: 20px; }
            .loader { border: 4px solid #f3f3f3; border-top: 4px solid #3498db; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

            /* Main Content Design */
            .header { width: 100%; text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2c5e8c; font-size: 28px; margin: 10px 0; }
            .support-label { align-self: flex-start; width: 100%; max-width: 400px; color: #555; font-size: 18px; margin-bottom: 15px; font-weight: bold; }
            
            .card { 
                background: white; border-radius: 15px; padding: 15px; margin-bottom: 15px; 
                display: flex; align-items: center; text-decoration: none; color: #333; 
                width: 100%; max-width: 400px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            }
            .icon-box { margin-right: 15px; color: #2c5e8c; font-size: 24px; }
            .text-box b { display: block; font-size: 16px; color: #333; }
            .text-box span { font-size: 13px; color: #888; }
            
            .btn-login { 
                background: #4a90e2; color: white; border: none; padding: 15px; 
                width: 100%; max-width: 400px; border-radius: 30px; 
                font-size: 18px; margin-top: 20px; font-weight: bold;
                text-align: center; display: block; text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div id="splash">
            <img src="https://i.imgur.com/uRovL7C.png" alt="xCare Logo">
            <div class="loader"></div>
        </div>

        <div class="header"><h1>xCare</h1></div>
        <div class="support-label">Support</div>

        <a href="https://t.me/your_telegram" class="card">
            <div class="icon-box">💬</div>
            <div class="text-box"><b>Operator chat</b><span>Text chat</span></div>
        </a>
        <a href="tel:+8801700000000" class="card">
            <div class="icon-box">🎧</div>
            <div class="text-box"><b>Call back</b><span>Order callback</span></div>
        </a>
        <div class="card">
            <div class="icon-box">🎤</div>
            <div class="text-box"><b>Online call</b><span>IP call</span></div>
        </div>
        <div class="card">
            <div class="icon-box">📱</div>
            <div class="text-box"><b>Contacts</b><span>E-mail, phone, etc</span></div>
        </div>

        <a href="#" class="btn-login">Log in</a>

        <script>
            // Splash screen hides after 2 seconds
            setTimeout(() => {
                document.getElementById('splash').style.opacity = '0';
                setTimeout(() => { document.getElementById('splash').style.display = 'none'; }, 500);
            }, 2000);

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
