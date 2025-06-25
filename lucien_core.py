import os
from flask import Flask, request
from command_router import route_command

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" not in data:
        return {"ok": True}

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    print(f"📥 Incoming message from {chat_id}: {text}")

    if text.startswith("/"):
        response = route_command(chat_id, text)
    else:
        response = f"• Έλαβα το μήνυμά σου: \"{text}\""

    # Εδώ μπορείς να στείλεις απάντηση στο Telegram αν θέλεις
    print(f"📤 Response: {response}")
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
