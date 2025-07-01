from flask import Flask, request
import os
import requests

app = Flask(__name__)

# Health check route
@app.route("/", methods=["GET"])
def index():
    return "Lucien Proxy is live", 200

# Webhook receiver
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received data:", data)

    # Optional: forward to your bot or handler
    TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("ADMIN_CHAT_ID")
    
    if TELEGRAM_TOKEN and CHAT_ID and data:
        msg = data.get("message", {}).get("text", "No text")
        payload = {
            "chat_id": CHAT_ID,
            "text": f"Lucien Proxy received: {msg}"
        }
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json=payload)

    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
