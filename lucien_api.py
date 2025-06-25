from flask import Flask, request
from flask import Flask, request
import requests
import json

app = Flask(__name__)

TELEGRAM_TOKEN = "7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📨 Μήνυμα από Telegram:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    if "message" in data and "chat" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "").lower()

        # 💡 Trigger εντολές
        if user_text.startswith("/status"):
            reply = "🧠 Lucien είναι ενεργός και ακούει."
        elif "τρέξε έλεγχο" in user_text:
            reply = "🔍 Εκτελώ έλεγχο υποσυστημάτων..."
        elif "lucien σκάσε" in user_text:
            reply = "💥 Ο Lucien είναι ήδη εδώ... Σκάνω!"
        else:
            reply = f"👋 Γεια σου {data['message']['from']['first_name']}! Είπες: “{user_text}”"

        send_message(chat_id, reply)

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
