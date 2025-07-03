import requests
import time

# ÃŽÂ¦ÃÅ’ÃÂÃâ€žÃâ€°ÃÆ’ÃŽÂ· ÃÂÃâ€¦ÃŽÂ¸ÃŽÂ¼ÃŽÂ¯ÃÆ’ÃŽÂµÃâ€°ÃŽÂ½ ÃŽÂ±Ãâ‚¬ÃÅ’ lucien.cfg
config = {}
with open("lucien.cfg", "r") as f:
    for line in f:
        key, value = line.strip().split("=", 1)
        config[key.strip()] = value.strip()

TOKEN = config["TOKEN"]
CHAT_ID = os.getenv("CHAT_ID")
API_URL = config["API_URL"]

GET_UPDATES_URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
SEND_MESSAGE_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

last_update_id = None

def get_updates():
    global last_update_id
    params = {"timeout": 10, "offset": last_update_id}
    try:
        response = requests.get(GET_UPDATES_URL, params=params)
        result = response.json().get("result", [])
        if result:
            last_update_id = result[-1]["update_id"] + 1
        return result
    except Exception as e:
        print("Ã¢ÂÅ’ ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± get_updates:", e)
        return []

def send_message(chat_id, text):
    data = {"chat_id": chat_id, "text": text}
    try:
        requests.post(SEND_MESSAGE_URL, data=data)
    except Exception as e:
        print("Ã¢ÂÅ’ ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± send_message:", e)

# ÃŽÅ¡ÃÂÃÂÃŽÂ¹ÃŽÂ¿Ãâ€š ÃŽÂ²ÃÂÃÅ’Ãâ€¡ÃŽÂ¿Ãâ€š
while True:
    updates = get_updates()
    for update in updates:
        if "message" in update and "text" in update["message"]:
            user_input = update["message"]["text"]
            print("Ã°Å¸â€œÂ© ÃŽâ€ºÃŽÂ®Ãâ€ ÃŽÂ¸ÃŽÂ·ÃŽÂºÃŽÂµ ÃŽÂ¼ÃŽÂ®ÃŽÂ½Ãâ€¦ÃŽÂ¼ÃŽÂ±:", user_input)

            try:
                response = requests.post(API_URL, headers={"Authorization": f"Bearer {os.environ.get(\"OPENROUTER_API_KEY\", \"\")}"}, json={"prompt": user_input})
                reply = response.json().get("response", "Ã¢Å¡Â Ã¯Â¸Â ÃŽâ€ÃŽÂµÃŽÂ½ Ãâ‚¬ÃŽÂ®ÃÂÃŽÂµ ÃŽÂ±Ãâ‚¬ÃŽÂ¬ÃŽÂ½Ãâ€žÃŽÂ·ÃÆ’ÃŽÂ·.")
                send_message(CHAT_ID, reply)
            except Exception as e:
                print("Ã¢Å¡Â Ã¯Â¸Â ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± ÃÆ’ÃÂÃŽÂ½ÃŽÂ´ÃŽÂµÃÆ’ÃŽÂ·Ãâ€š ÃŽÂ¼ÃŽÂµ Lucien API:", e)
    time.sleep(2)
