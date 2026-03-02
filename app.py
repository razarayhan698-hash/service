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
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #f5f8fa; margin: 0; padding: 0; }
            .header { background: white; padding: 15px; text-align: center; font-size: 20px; font-weight: bold; color: #2b5d8c; position: relative; border-bottom: 1px solid #eee; }
            .header .settings-icon { position: absolute; right: 20px; top: 18px; color: #5f7d95; font-size: 20px; }
            .container { padding: 20px; max-width: 500px; margin: auto; }
            .section-title { font-size: 22px; font-weight: bold; color: #1a3a5a; margin-bottom: 20px; }
            .card { background: white; border-radius: 15px; padding: 15px; margin-bottom: 12px; display: flex; align-items: center; text-decoration: none; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
            .icon-bg { width: 45px; height: 45px; background: #e8f1f8; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 22px; color: #2b5d8c; }
            .text-content { flex-grow: 1; }
            .text-content b { display: block; font-size: 16px; color: #1a3a5a; }
            .text-content span { font-size: 13px; color: #8a99a8; }
            .badge { background: #e1e8ed; color: #5f7d95; font-size: 12px; font-weight: bold; padding: 4px 8px; border-radius: 10px; }
            .btn-login { background: #4a90e2; color: white; padding: 16px; width: 100%; border-radius: 12px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 25px; display: block; font-size: 16px; }
        </style>
        <script> if ('serviceWorker' in navigator) { navigator.serviceWorker.register('/sw.js'); } </script>
    </head>
    <body>
        <div class="header">xCare <span class="settings-icon">⚙️</span></div>
        <div class="container">
            <div class="section-title">Support</div>
            <a href="#" class="card"><div class="icon-bg">💬</div><div class="text-content"><b>Operator chat</b><span>Text chat</span></div><div class="badge">1</div></a>
            <a href="#" class="card"><div class="icon-bg">🎧</div><div class="text-content"><b>Call back</b><span>Order callback</span></div></a>
            <a href="#" class="card"><div class="icon-bg">🎙️</div><div class="text-content"><b>Online call</b><span>IP call</span></div></a>
            <a href="#" class="card"><div class="icon-bg">📱</div><div class="text-content"><b>Contacts</b><span>E-mail, phone, etc</span></div></a>
            <a href="#" class="btn-login">Log in</a>
        </div>
    </body>
    </html>
    '''

@app.route('/manifest.json')
def manifest(): return send_from_directory(os.getcwd(), 'manifest.json')
@app.route('/sw.js')
def sw(): return send_from_directory(os.getcwd(), 'sw.js')
@app.route('/logo.png')
def logo(): return send_from_directory(os.getcwd(), 'logo.png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
