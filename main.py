from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Optional: Για δοκιμές μπορείς να βάλεις χειροκίνητα

@app.route('/')
def home():
    return 'Lucien Proxy is active!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Λογική αποστολής πίσω μηνύματος στο Telegram
    if 'message' in data and 'text' in data['message']:
        text = data['message']['text']
        chat_id = data['message']['chat']['id']

        reply = f"💬 Lucien Proxy says: You said '{text}'"
        send_message(chat_id, reply)

    return jsonify({'status': 'ok'})

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', po
