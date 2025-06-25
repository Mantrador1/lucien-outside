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
    print("ðŸ“¨ ÎœÎ®Î½Ï…Î¼Î± Î±Ï€ÏŒ Telegram:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    if "message" in data and "chat" in data["message"]:
        CHAT_ID = "1837395252"
        user_text = data["message"].get("text", "").lower()

        # ðŸ’¡ Trigger ÎµÎ½Ï„Î¿Î»Î­Ï‚
        if user_text.startswith("/status"):
            reply = "ðŸ§  Lucien ÎµÎ¯Î½Î±Î¹ ÎµÎ½ÎµÏÎ³ÏŒÏ‚ ÎºÎ±Î¹ Î±ÎºÎ¿ÏÎµÎ¹."
        elif "Ï„ÏÎ­Î¾Îµ Î­Î»ÎµÎ³Ï‡Î¿" in user_text:
            reply = "ðŸ” Î•ÎºÏ„ÎµÎ»ÏŽ Î­Î»ÎµÎ³Ï‡Î¿ Ï…Ï€Î¿ÏƒÏ…ÏƒÏ„Î·Î¼Î¬Ï„Ï‰Î½..."
        elif "lucien ÏƒÎºÎ¬ÏƒÎµ" in user_text:
            reply = "ðŸ’¥ ÎŸ Lucien ÎµÎ¯Î½Î±Î¹ Î®Î´Î· ÎµÎ´ÏŽ... Î£ÎºÎ¬Î½Ï‰!"
        else:
            reply = f"ðŸ‘‹ Î“ÎµÎ¹Î± ÏƒÎ¿Ï… {data['message']['from']['first_name']}! Î•Î¯Ï€ÎµÏ‚: â€œ{user_text}â€"

        send_message(chat_id, reply)

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
