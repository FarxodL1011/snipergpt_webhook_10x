
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)
    message = data.get("message", "No message provided")
    # Здесь логика обработки сигнала
    return {"status": "received", "message": message}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
