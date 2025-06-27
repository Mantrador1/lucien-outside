from flask import Flask, request
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# 🔁 Φόρτωση .env μεταβλητών
load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
AUTHORIZED_CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "logs/lucien_commands.log"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

def log_command(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] | {text}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Νέο μήνυμα από Telegram:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    if "message" in data and "chat" in data["message"]:
        chat_id = str(data["message"]["chat"]["id"])
        user_text = data["message"].get("text", "").lower()
        log_command(user_text)

        if chat_id != AUTHORIZED_CHAT_ID:
            send_message(chat_id, "⛔ Unauthorized access.")
            return "unauthorized", 403

        # 🔁 Επεξεργασία trigger εντολών
        if user_text.startswith("/status"):
            reply = "✅ Ο Lucien είναι ενεργός και ακούει."
        elif "τρέξε έλεγχο" in user_text:
            reply = "🔍 Εκτελώ έλεγχο υποσυστημάτων..."
        elif "lucien ακόμα" in user_text:
            reply = "🔴 Ο Lucien είναι ήδη εδώ… Σκάναρε!"
        else:
            fname = data["message"]["from"].get("first_name", "φίλε")
            reply = f"👋 Γεια σου {fname}! Είπες: “{user_text}”"

        send_message(chat_id, reply)

    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
