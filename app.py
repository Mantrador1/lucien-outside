from flask import Flask, request
import subprocess
import os
from dotenv import load_dotenv

# 🔁 Φόρτωσε .env για local ή fallback
load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
AUTHORIZED_CHAT_ID = os.getenv("CHAT_ID")

print("🔐 BOT_TOKEN loaded:", BOT_TOKEN)
print("🆔 CHAT_ID loaded:", AUTHORIZED_CHAT_ID)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data or 'message' not in data:
        return 'no message', 400

    chat_id = str(data['message']['chat']['id'])
    message_text = data['message'].get('text', '')

    if chat_id != AUTHORIZED_CHAT_ID:
        return 'unauthorized', 403

    if message_text.startswith('/run '):
        code = message_text[len('/run '):]
        try:
            result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True, timeout=10)
        except subprocess.CalledProcessError as e:
            result = f"❌ Error:\n{e.output}"
        except Exception as ex:
            result = f"⚠️ Exception: {str(ex)}"
        send_message(result)

    elif message_text.startswith('/code '):
        try:
            parts = message_text[len('/code '):].split(' ', 1)
            filename = parts[0]
            content = parts[1]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            send_message(f"✅ File {filename} saved.")
        except Exception as ex:
            send_message(f"❌ Error saving file: {str(ex)}")

    elif message_text == '/memory':
        send_message("🧠 Memory layer not implemented yet.")

    elif message_text == '/deploy':
        try:
            subprocess.Popen(["git", "pull"])
            subprocess.Popen(["nixpacks", "build", "."])
            send_message("🚀 Deploying latest version...")
        except Exception as ex:
            send_message(f"❌ Deploy error: {str(ex)}")

    else:
        send_message("❓ Unknown command.")

    return 'ok', 200

def send_message(text):
    import requests
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": AUTHORIZED_CHAT_ID,
        "text": text
    }
    r = requests.post(url, json=payload)
    print("📤 send_message result:", r.status_code, r.text)

if __name__ == '__main__':
    app.run(port=5000)
