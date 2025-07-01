from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set in environment variables!")

print("✅ Loaded BOT_TOKEN:", BOT_TOKEN)

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/')
def index():
    return 'Lucien Proxy is alive!', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Received data:", data)  # 🔍 Εμφανίζει τα δεδομένα που έρχονται από Telegram

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        reply = f"🧠 Lucien Proxy says: '{text}' received."
        print(f"📤 Sending reply to {chat_id}: {reply}")  # 🔍 Εμφανίζει τι θα σταλεί
        send_message(chat_id, reply)

    return "ok", 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, json=payload)
    print("📬 Telegram response:", response.status_code, response.text)  # 🔍 Εμφανίζει απάντηση από Telegram
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

