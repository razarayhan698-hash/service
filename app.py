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
            /* Loading Screen */
            #loader {
                position: fixed; width: 100%; height: 100%; background: #2b5d8c;
                display: flex; flex-direction: column; justify-content: center; align-items: center;
                z-index: 9999; transition: opacity 0.5s ease;
            }
            .dots span {
                width: 15px; height: 15px; margin: 0 5px; background: white;
                border-radius: 50%; display: inline-block;
                animation: loading 0.6s infinite alternate;
            }
            .dots span:nth-child(2) { animation-delay: 0.2s; }
            .dots span:nth-child(3) { animation-delay: 0.4s; }
            @keyframes loading { from { opacity: 1; transform: scale(1); } to { opacity: 0.3; transform: scale(0.5); } }

            /* Main Style */
            body { font-family: sans-serif; background-color: #f5f8fa; margin: 0; padding: 0; }
            .header { background: white; padding: 15px; text-align: center; font-size: 20px; font-weight: bold; color: #2b5d8c; border-bottom: 1px solid #eee; position: relative; }
            .header .settings-icon { position: absolute; right: 20px; top: 18px; color: #5f7d95; font-size: 20px; }
            .container { padding: 20px; max-width: 500px; margin: auto; }
            .section-title { font-size: 22px; font-weight: bold; color: #1a3a5a; margin-bottom: 20px; }
            .card { background: white; border-radius: 15px; padding: 15px; margin-bottom: 12px; display: flex; align-items: center; text-decoration: none; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.05); cursor: pointer; }
            .icon-bg { width: 45px; height: 45px; background: #e8f1f8; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 22px; color: #2b5d8c; }
            .text-content { flex-grow: 1; }
            .text-content b { display: block; font-size: 16px; color: #1a3a5a; }
            .text-content span { font-size: 13px; color: #8a99a8; }
            .badge { background: #dce6ed; color: #5f7d95; font-size: 12px; font-weight: bold; padding: 4px 10px; border-radius: 12px; }
            .btn-login { background: #4a90e2; color: white; padding: 16px; width: 100%; border-radius: 12px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 25px; display: block; }

            /* Modal Style */
            #contactModal {
                display: none; position: fixed; bottom: 0; width: 100%; background: white;
                border-radius: 25px 25px 0 0; padding: 20px; box-shadow: 0 -5px 20px rgba(0,0,0,0.1);
                z-index: 10000; box-sizing: border-box; max-height: 85vh; overflow-y: auto;
            }
            .modal-overlay { display: none; position: fixed; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; }
            .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
            .modal-header h3 { margin: 0; color: #2b5d8c; }
            .contact-group { margin-bottom: 25px; }
            .contact-group h4 { margin: 0 0 10px 0; color: #5f7d95; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; }
            .contact-link { display: flex; align-items: center; background: #f8fafd; padding: 12px; border-radius: 10px; text-decoration: none; color: #1a3a5a; font-weight: bold; margin-bottom: 10px; border: 1px solid #eef2f6; }
            .contact-link span { margin-right: 10px; font-size: 18px; }
            .close-btn { background: #f0f2f5; color: #333; padding: 15px; width: 100%; border-radius: 12px; text-align: center; cursor: pointer; font-weight: bold; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div id="loader">
            <div class="dots"><span></span><span></span><span></span></div>
            <h1 style="color: white; margin-top: 20px;">xCare</h1>
        </div>

        <div class="header">xCare <span class="settings-icon">⚙️</span></div>
        <div class="container">
            <div class="section-title">Support</div>
            <a href="#" class="card"><div class="icon-bg">💬</div><div class="text-content"><b>Operator chat</b><span>Text chat</span></div><div class="badge">1</div></a>
            <a href="#" class="card"><div class="icon-bg">🎧</div><div class="text-content"><b>Call back</b><span>Order callback</span></div></a>
            <a href="#" class="card"><div class="icon-bg">🎙️</div><div class="text-content"><b>Online call</b><span>IP call</span></div></a>
            
            <div class="card" onclick="openContacts()">
                <div class="icon-bg">📱</div>
                <div class="text-content"><b>Contacts</b><span>E-mail, phone, etc</span></div>
            </div>

            <a href="#" class="btn-login">Log in</a>
        </div>

        <div class="modal-overlay" id="overlay" onclick="closeContacts()"></div>
        <div id="contactModal">
            <div class="modal-header">
                <h3>Contact & Support</h3>
                <span onclick="closeContacts()" style="cursor:pointer; font-size: 20px; color: #999;">✕</span>
            </div>
            
            <div class="contact-group">
                <h4>Agent Application</h4>
                <a href="https://t.me/YourMasterAgent" class="contact-link"><span>👑</span> 1xBet Master Agent</a>
                <a href="https://t.me/YourEwalletAgent" class="contact-link"><span>💳</span> E-wallet Agent</a>
            </div>

            <div class="contact-group">
                <h4>1xBet App Issues</h4>
                <a href="https://t.me/YourSupportLink" class="contact-link"><span>🛠️</span> Report App Problem</a>
                <a href="mailto:support@yourlink.com" class="contact-link"><span>📧</span> Email Support</a>
            </div>

            <div class="contact-group">
                <h4>Direct Communication</h4>
                <a href="tel:+8801XXXXXXXXX" class="contact-link"><span>📞</span> Official Phone Call</a>
                <a href="https://wa.me/880XXXXXXXXXX" class="contact-link"><span>💬</span> WhatsApp Support</a>
            </div>

            <div class="close-btn" onclick="closeContacts()">Close</div>
        </div>

        <script>
            window.addEventListener('load', function() {
                setTimeout(() => {
                    document.getElementById('loader').style.opacity = '0';
                    setTimeout(() => document.getElementById('loader').style.display = 'none', 500);
                }, 1500);
            });

            function openContacts() {
                document.getElementById('contactModal').style.display = 'block';
                document.getElementById('overlay').style.display = 'block';
            }
            function closeContacts() {
                document.getElementById('contactModal').style.display = 'none';
                document.getElementById('overlay').style.display = 'none';
            }
        </script>
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
