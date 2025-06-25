from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def index():
    return "Lucien Proxy is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📥 Received data:", data)

    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        reply = f"💬 Έλαβα το μήνυμά σου: \"{text}\""
        send_message(chat_id, reply)

    return jsonify({"status": "success"}), 200

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("✅ Sent message:", response.json())
    except Exception as e:
        print("❌ Error sending message:", str(e))
        print("📦 Payload was:", payload)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
