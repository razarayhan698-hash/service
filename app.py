from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Running 24/7!"

if __name__ == "__main__":
    # Render-এর জন্য পোর্ট সেটআপ
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
