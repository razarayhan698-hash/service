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
        <meta name="theme-color" content="#517da2">
        <style>
            body { font-family: sans-serif; background-color: #f4f7f9; margin: 0; padding: 20px; }
            .header { color: #517da2; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 25px; }
            .support-title { font-size: 20px; color: #1a3a5a; margin-bottom: 15px; }
            .card { background: white; border-radius: 12px; padding: 15px; margin-bottom: 10px; display: flex; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-decoration: none; color: inherit; }
            .icon { font-size: 22px; margin-right: 15px; color: #517da2; width: 30px; text-align: center; }
            .text-content b { display: block; color: #333; }
            .text-content span { color: #888; font-size: 12px; }
            .btn-login { background: #4a90e2; color: white; border: none; padding: 15px; width: 100%; border-radius: 25px; font-size: 18px; margin-top: 20px; cursor: pointer; font-weight: bold; text-align: center; display: block; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="header">xCare</div>
        <div class="support-title">Support</div>
        
        <div class="card"><div class="icon">💬</div><div class="text-content"><b>Operator chat</b><span>Text chat</span></div></div>
        <div class="card"><div class="icon">🎧</div><div class="text-content"><b>Call back</b><span>Order callback</span></div></div>
        <div class="card"><div class="icon">🎤</div><div class="text-content"><b>Online call</b><span>IP call</span></div></div>
        <div class="card"><div class="icon">📱</div><div class="text-content"><b>Contacts</b><span>E-mail, phone, etc</span></div></div>
        
        <a href="#" class="btn-login">Log in</a>
    </body>
    </html>
    '''

# ম্যানিফেস্ট ফাইলটি সার্ভ করার জন্য এই রুটটি প্রয়োজন
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
