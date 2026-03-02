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
            body { font-family: sans-serif; background-color: #f0f4f7; margin: 0; display: flex; flex-direction: column; align-items: center; }
            .top-bar { width: 100%; padding: 20px; background: white; text-align: center; border-bottom: 1px solid #ddd; }
            .top-bar h2 { color: #2b5d8c; margin: 0; }
            .content { width: 90%; max-width: 400px; padding: 20px; }
            .card { background: white; border-radius: 15px; padding: 20px; margin-bottom: 15px; display: flex; align-items: center; text-decoration: none; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .icon { font-size: 24px; margin-right: 15px; }
            .btn-login { background: #4a90e2; color: white; padding: 15px; width: 100%; border-radius: 15px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 20px; display: block; }
        </style>
        <script>
            if ('serviceWorker' in navigator) { navigator.serviceWorker.register('/sw.js'); }
        </script>
    </head>
    <body>
        <div class="top-bar"><h2>xCare</h2></div>
        <div class="content">
            <a href="#" class="card"><span class="icon">💬</span><b>Operator chat</b></a>
            <a href="#" class="card"><span class="icon">🎧</span><b>Call back</b></a>
            <a href="#" class="card"><span class="icon">📱</span><b>Contacts</b></a>
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
