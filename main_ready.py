import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7821174026:AAFTVtiYtG24mjUvK_h3ahF4MmpbILRmQ3Q"
CHAT_ID = "8079328122"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data or "message" not in data:
        return {"status": "ignored"}, 200

    message = data["message"]
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(telegram_url, json=payload)

    return {"status": "sent"}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))