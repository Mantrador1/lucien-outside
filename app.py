from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return 'Lucien Proxy Online', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        text = data['message'].get('text', '')
        if text:
            reply = f"📬 Λήφθηκε: {text}"
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": reply}
            )
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
