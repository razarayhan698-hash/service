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
            body { font-family: sans-serif; background-color: #004793; margin: 0; padding: 20px; color: white; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
            .header-container { text-align: center; margin-bottom: 30px; }
            .app-logo { width: 80px; height: 80px; border-radius: 15px; margin-bottom: 10px; }
            .header-title { font-size: 26px; font-weight: bold; margin: 0; }
            .card { background: rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 18px; margin-bottom: 12px; display: flex; align-items: center; text-decoration: none; color: white; width: 100%; max-width: 400px; box-sizing: border-box; border: 1px solid rgba(255, 255, 255, 0.1); }
            .icon { font-size: 24px; margin-right: 15px; width: 30px; text-align: center; }
            .text-content b { display: block; font-size: 16px; }
            .btn-login { background: white; color: #004793; border: none; padding: 15px; width: 100%; max-width: 400px; border-radius: 25px; font-size: 18px; margin-top: auto; margin-bottom: 20px; font-weight: bold; text-align: center; display: block; text-decoration: none; box-sizing: border-box; }
        </style>
        <script>
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/sw.js');
            }
        </script>
    </head>
    <body>
        <div class="header-container">
            <img src="https://i.imgur.com/uRovL7C.png" alt="xC Logo" class="app-logo">
            <div class="header-title">xCare</div>
        </div>
        <a href="#" class="card"><div class="icon">💬</div><div class="text-content"><b>Operator chat</b></div></a>
        <a href="#" class="card"><div class="icon">🎧</div><div class="text-content"><b>Call back</b></div></a>
        <a href="#" class="btn-login">Log in</a>
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
