import requests
import subprocess
import time

# === ÃŽÂ¡ÃŽÂ¥ÃŽËœÃŽÅ“ÃŽâ„¢ÃŽÂ£ÃŽâ€¢ÃŽâ„¢ÃŽÂ£ ===
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = f"https://api.telegram.org/bot{TOKEN}/"
last_update_id = 0

def send_message(text):
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(URL + "sendMessage", data=data)

def get_updates():
    global last_update_id
    try:
        params = {"offset": last_update_id + 1, "timeout": 10}
        response = requests.get(URL + "getUpdates", params=params)
        result = response.json()["result"]
        return result
    except Exception as e:
        print("ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± ÃÆ’Ãâ€žÃŽÂ¿ get_updates:", e)
        return []

def execute_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")
    except Exception as e:
        return f"ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ±: {str(e)}"

# === MAIN LOOP ===
print("Ã°Å¸â€ºÂ° Lucien Command Listener ÃŽÂµÃŽÂ½ÃŽÂµÃÂÃŽÂ³ÃÅ’Ãâ€š.")
send_message("Ã°Å¸â€ºÂ° Lucien Command Listener ÃŽÂµÃŽÂ½ÃŽÂµÃÂÃŽÂ³ÃÅ’Ãâ€š.")

while True:
    updates = get_updates()
    for update in updates:
        last_update_id = update["update_id"]
        message = update.get("message", {})
        text = message.get("text", "")
        sender_id = message.get("from", {}).get("id", 0)

        print(f"[{sender_id}] -> {text}")  # DEBUG

        if sender_id != CHAT_ID:
            send_message("Ã¢â€ºâ€ ÃŽâ€ ÃÂÃŽÂ½ÃŽÂ·ÃÆ’ÃŽÂ· Ãâ‚¬ÃÂÃÅ’ÃÆ’ÃŽÂ²ÃŽÂ±ÃÆ’ÃŽÂ·Ãâ€š.")
            continue

        if not text:
            continue

        result = execute_command(text)
        if not result.strip():
            result = "Ã¢Å“â€¦ ÃŽâ€¢ÃŽÂ½Ãâ€žÃŽÂ¿ÃŽÂ»ÃŽÂ® ÃŽÂµÃŽÂºÃâ€žÃŽÂµÃŽÂ»ÃŽÂ­ÃÆ’Ãâ€žÃŽÂ·ÃŽÂºÃŽÂµ Ãâ€¡Ãâ€°ÃÂÃŽÂ¯Ãâ€š ÃŽÂ­ÃŽÂ¾ÃŽÂ¿ÃŽÂ´ÃŽÂ¿."
        elif len(result) > 4000:
            result = result[:4000] + "\n...ÃŽÂ±Ãâ‚¬ÃŽÂ¬ÃŽÂ½Ãâ€žÃŽÂ·ÃÆ’ÃŽÂ· Ãâ‚¬ÃŽÂµÃÂÃŽÂ¹ÃŽÂºÃÅ’Ãâ‚¬ÃŽÂ·ÃŽÂºÃŽÂµ."

        send_message(f"Ã°Å¸â€œÂ¤ ÃŽâ€˜Ãâ‚¬ÃŽÂ¬ÃŽÂ½Ãâ€žÃŽÂ·ÃÆ’ÃŽÂ·:\n{result}")
    time.sleep(2)
