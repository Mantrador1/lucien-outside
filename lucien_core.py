import os
from flask import Flask, request
from command_router import route_command

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" not in data:
        return {"ok": True}

    CHAT_ID = os.getenv("CHAT_ID")
    text = data["message"].get("text", "")

    print(f"Ã°Å¸â€œÂ¥ Incoming message from {chat_id}: {text}")

    if text.startswith("/"):
        response = route_command(chat_id, text)
    else:
        response = f"Ã¢â‚¬Â¢ ÃŽË†ÃŽÂ»ÃŽÂ±ÃŽÂ²ÃŽÂ± Ãâ€žÃŽÂ¿ ÃŽÂ¼ÃŽÂ®ÃŽÂ½Ãâ€¦ÃŽÂ¼ÃŽÂ¬ ÃÆ’ÃŽÂ¿Ãâ€¦: \"{text}\""

    # ÃŽâ€¢ÃŽÂ´ÃÅ½ ÃŽÂ¼Ãâ‚¬ÃŽÂ¿ÃÂÃŽÂµÃŽÂ¯Ãâ€š ÃŽÂ½ÃŽÂ± ÃÆ’Ãâ€žÃŽÂµÃŽÂ¯ÃŽÂ»ÃŽÂµÃŽÂ¹Ãâ€š ÃŽÂ±Ãâ‚¬ÃŽÂ¬ÃŽÂ½Ãâ€žÃŽÂ·ÃÆ’ÃŽÂ· ÃÆ’Ãâ€žÃŽÂ¿ Telegram ÃŽÂ±ÃŽÂ½ ÃŽÂ¸ÃŽÂ­ÃŽÂ»ÃŽÂµÃŽÂ¹Ãâ€š
    print(f"Ã°Å¸â€œÂ¤ Response: {response}")
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
