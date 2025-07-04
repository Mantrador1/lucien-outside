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
    requests.post(url, headers={"Authorization": f"Bearer {os.environ.get(\"OPENROUTER_API_KEY\", \"\")}"}, json=payload)

def log_command(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {text}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Ã¢Å¾Â¡ ÃŽÂÃŽÂ­ÃŽÂ¿ ÃŽÂ¼ÃŽÂ®ÃŽÂ½Ãâ€¦ÃŽÂ¼ÃŽÂ± ÃŽÂ±Ãâ‚¬ÃÅ’ Telegram:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    if "message" in data and "chat" in data["message"]:
        chat_id = str(data["message"]["chat"]["id"])
        user_text = data["message"].get("text", "").lower()
        log_command(user_text)

        if chat_id != AUTHORIZED_CHAT_ID:
            send_message(chat_id, "Ã°Å¸Å¡Â« Unauthorized access.")
            return "unauthorized", 403

        if "status" in user_text:
            reply = "Ã°Å¸â€œÂ¡ ÃŽÅ¸ Lucien ÃŽÂµÃŽÂ¯ÃŽÂ½ÃŽÂ±ÃŽÂ¹ ÃŽÂµÃŽÂ½ÃŽÂµÃÂÃŽÂ³ÃÅ’Ãâ€š ÃŽÂºÃŽÂ±ÃŽÂ¹ ÃŽÂ±ÃŽÂºÃŽÂ¿ÃÂÃŽÂµÃŽÂ¹."
        elif "ÃŽÂ­ÃŽÂ»ÃŽÂµÃŽÂ³Ãâ€¡ÃŽÂ¿" in user_text:
            reply = "Ã°Å¸Â§Â  ÃŽâ€¢ÃŽÂºÃâ€žÃŽÂµÃŽÂ»ÃÅ½ ÃŽÂ­ÃŽÂ»ÃŽÂµÃŽÂ³Ãâ€¡ÃŽÂ¿ Ãâ€¦Ãâ‚¬ÃŽÂ¿ÃÆ’Ãâ€¦ÃÆ’Ãâ€žÃŽÂ·ÃŽÂ¼ÃŽÂ¬Ãâ€žÃâ€°ÃŽÂ½..."
        elif "ÃŽÂµÃŽÂ¯ÃÆ’ÃŽÂ±ÃŽÂ¹ ok" in user_text:
            reply = "Ã¢Å“â€¦ ÃŽÅ¸ Lucien ÃŽÂµÃŽÂ¯ÃŽÂ½ÃŽÂ±ÃŽÂ¹ ÃÅ’ÃŽÂ»ÃŽÂ± ÃŽÂºÃŽÂ±ÃŽÂ»ÃŽÂ¬. ÃŽÂ£Ãâ€¡ÃŽÂ¬ÃÂÃŽÂ±ÃŽÂ¼ÃŽÂµ!"
        else:
            fname = data["message"]["from"].get("first_name", "ÃŽÂ¦ÃŽÂ¯ÃŽÂ»ÃŽÂµ")
            reply = f"Ã°Å¸â€˜â€¹ ÃŽâ€œÃŽÂµÃŽÂ¹ÃŽÂ± ÃÆ’ÃŽÂ¿Ãâ€¦ {fname}! ÃŽâ€¢ÃŽÂ¯Ãâ‚¬ÃŽÂµÃâ€š: Ã¢â‚¬Å“{user_text}Ã¢â‚¬Â"

        send_message(chat_id, reply)

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
