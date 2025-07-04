import requests
import time
import logging

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
CHECK_INTERVAL = 60  # ÃŽÂ­ÃŽÂ»ÃŽÂµÃŽÂ³Ãâ€¡ÃŽÂ¿Ãâ€š ÃŽÂºÃŽÂ¬ÃŽÂ¸ÃŽÂµ 60 ÃŽÂ´ÃŽÂµÃâ€¦Ãâ€žÃŽÂµÃÂÃÅ’ÃŽÂ»ÃŽÂµÃâ‚¬Ãâ€žÃŽÂ±

logging.basicConfig(level=logging.INFO)

def is_token_valid():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("ok", False)
    except Exception as e:
        logging.error(f"[Watchdog Error] {e}")
        return False

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except:
        pass

def main():
    while True:
        valid = is_token_valid()
        if not valid:
            logging.warning("[TOKEN EXPIRED] Ã°Å¸â€Â¥ ÃŽÂ¤ÃŽÂ¿ Telegram Bot Token Ãâ€ ÃŽÂ±ÃŽÂ¯ÃŽÂ½ÃŽÂµÃâ€žÃŽÂ±ÃŽÂ¹ invalid!")
            send_alert("Ã¢Å¡Â Ã¯Â¸Â ÃŽÂ¤ÃŽÂ¿ Telegram Bot Token ÃŽÂ­Ãâ‚¬ÃŽÂ±ÃË†ÃŽÂµ ÃŽÂ½ÃŽÂ± ÃŽÂ¹ÃÆ’Ãâ€¡ÃÂÃŽÂµÃŽÂ¹! ÃŽÂ§ÃÂÃŽÂµÃŽÂ¹ÃŽÂ¬ÃŽÂ¶ÃŽÂµÃâ€žÃŽÂ±ÃŽÂ¹ ÃŽÂ½ÃŽÂ­ÃŽÂ¿.")
        else:
            logging.info("[TOKEN VALID] Ã¢Å“â€¦ ÃŽÂ¤ÃŽÂ¿ token ÃŽÂµÃŽÂ¯ÃŽÂ½ÃŽÂ±ÃŽÂ¹ ÃŽÂ­ÃŽÂ³ÃŽÂºÃâ€¦ÃÂÃŽÂ¿.")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
