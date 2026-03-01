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
        <meta name="theme-color" content="#2b5d8c">
        <style>
            * { box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', sans-serif; 
                background-color: #f0f4f7; 
                margin: 0; padding: 0; 
                display: flex; flex-direction: column; align-items: center;
                min-height: 100vh;
            }
            #splash {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background-color: #2b5d8c; display: flex; flex-direction: column;
                justify-content: center; align-items: center; z-index: 9999;
                transition: opacity 0.6s ease;
            }
            #splash h1 { color: white; font-size: 50px; font-weight: bold; margin: 0; font-style: italic; }
            .loader-dots { margin-top: 20px; display: flex; gap: 8px; }
            .dot { width: 10px; height: 10px; background: rgba(255,255,255,0.4); border-radius: 50%; animation: blink 1.4s infinite; }
            .dot:nth-child(2) { animation-delay: 0.2s; }
            .dot:nth-child(3) { animation-delay: 0.4s; }
            @keyframes blink { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; background: white; } }

            .top-bar { 
                width: 100%; padding: 15px 20px; display: flex; 
                justify-content: space-between; align-items: center; 
                background: white; border-bottom: 1px solid #e0e0e0;
            }
            .top-bar h2 { color: #2b5d8c; margin: 0; font-size: 22px; flex-grow: 1; text-align: center; margin-left: 30px; }
            .settings-icon { font-size: 24px; color: #2b5d8c; cursor: pointer; }

            .content { width: 100%; max-width: 450px; padding: 20px; flex-grow: 1; }
            .support-label { color: #1a3a5a; font-size: 24px; font-weight: bold; margin-bottom: 20px; }
            
            .card { 
                background: white; border-radius: 20px; padding: 18px; margin-bottom: 15px; 
                display: flex; align-items: center; text-decoration: none; 
                box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f0f0f0;
            }
            .icon-circle { 
                width: 50px; height: 50px; background: #e8f0f7; 
                border-radius: 50%; display: flex; justify-content: center; 
                align-items: center; margin-right: 15px; font-size: 24px; color: #2b5d8c;
            }
            .text-box { flex-grow: 1; }
            .text-box b { display: block; font-size: 17px; color: #1a3a5a; }
            .text-box span { font-size: 14px; color: #7a8b9a; }
            .badge { background: #e1e8f0; color: #7a8b9a; padding: 2px 10px; border-radius: 12px; font-size: 14px; }

            .footer { width: 100%; max-width: 450px; padding: 20px; }
            .btn-login { 
                background: #4a90e2; color: white; border: none; padding: 18px; 
                width: 100%; border-radius: 20px; font-size: 18px; font-weight: bold;
                text-align: center; display: block; text-decoration: none;
            }
        </style>
        <script>
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/sw.js');
            }
            window.onload = () => {
                setTimeout(() => {
                    const s = document.getElementById('splash');
                    if(s) {
                        s.style.opacity = '0';
                        setTimeout(() => { s.style.display = 'none'; }, 600);
                    }
                }, 2500);
            };
        </script>
    </head>
    <body>
        <div id="splash">
            <h1>xCare</h1>
            <div class="loader-dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
        </div>
        <div class="top-bar">
            <h2>xCare</h2>
            <div class="settings-icon">⚙️</div>
        </div>
        <div class="content">
            <div class="support-label">Support</div>
            <a href="#" class="card">
                <div class="icon-circle">💬</div>
                <div class="text-box"><b>Operator chat</b><span>Text chat</span></div>
                <div class="badge">1</div>
            </a>
            <a href="#" class="card">
                <div class="icon-circle">🎧</div>
                <div class="text-box"><b>Call back</b><span>Order callback</span></div>
            </a>
            <a href="#" class="card">
                <div class="icon-circle">🎤</div>
                <div class="text-box"><b>Online call</b><span>IP call</span></div>
            </a>
            <a href="#" class="card">
                <div class="icon-circle">📱</div>
                <div class="text-box"><b>Contacts</b><span>E-mail, phone, etc</span></div>
            </a>
        </div>
        <div class="footer">
            <a href="#" class="btn-login">Log in</a>
        </div>
    </body>
    </html>
    '''

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory(os.getcwd(), 'sw.js')

@app.route('/logo.png')
def serve_logo():
    return send_from_directory(os.getcwd(), 'logo.png')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
