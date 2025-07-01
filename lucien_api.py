from flask import Flask, request
import requests
import datetime
import json

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
AUTHORIZED_CHAT_ID = os.environ.get("CHAT_ID")
LOG_FILE = "logs/lucien_commands.log"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

def log_command(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {text}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("➡ Νέο μήνυμα από Telegram:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    if "message" in data and "chat" in data["message"]:
        chat_id = str(data["message"]["chat"]["id"])
        user_text = data["message"].get("text", "").lower()
        log_command(user_text)

        if chat_id != AUTHORIZED_CHAT_ID:
            send_message(chat_id, "🚫 Unauthorized access.")
            return "unauthorized", 403

        if "status" in user_text:
            reply = "📡 Ο Lucien είναι ενεργός και ακούει."
        elif "έλεγχο" in user_text:
            reply = "🧠 Εκτελώ έλεγχο υποσυστημάτων..."
        elif "είσαι ok" in user_text:
            reply = "✅ Ο Lucien είναι όλα καλά. Σχάραμε!"
        else:
            fname = data["message"]["from"].get("first_name", "Φίλε")
            reply = f"👋 Γεια σου {fname}! Είπες: “{user_text}”"

        send_message(chat_id, reply)

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
