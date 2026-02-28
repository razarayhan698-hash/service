from flask import Flask
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
        <style>
            body { font-family: sans-serif; background-color: #f4f7f9; margin: 0; padding: 20px; }
            .header { color: #517da2; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 25px; }
            .support-title { font-size: 20px; color: #1a3a5a; margin-bottom: 15px; }
            .card { background: white; border-radius: 12px; padding: 15px; margin-bottom: 10px; display: flex; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .icon { font-size: 22px; margin-right: 15px; color: #517da2; width: 30px; text-align: center; }
            .text-content b { display: block; color: #333; }
            .text-content span { color: #888; font-size: 12px; }
            .btn-login { background: #4a90e2; color: white; border: none; padding: 15px; width: 100%; border-radius: 25px; font-size: 18px; margin-top: 20px; cursor: pointer; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header">xCare</div>
        <div class="support-title">Support</div>
        <div class="card"><div class="icon">💬</div><div class="text-content"><b>Operator chat</b><span>Text chat</span></div></div>
        <div class="card"><div class="icon">🎧</div><div class="text-content"><b>Call back</b><span>Order callback</span></div></div>
        <div class="card"><div class="icon">🎤</div><div class="text-content"><b>Online call</b><span>IP call</span></div></div>
        <div class="card"><div class="icon">📱</div><div class="text-content"><b>Contacts</b><span>E-mail, phone, etc</span></div></div>
        <button class="btn-login">Log in</button>
    </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
