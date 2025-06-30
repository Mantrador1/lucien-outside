import requests
import time
import logging

BOT_TOKEN = "7933465622:AAFhHCGp4xxEn5KGvPmrbmdrDqkX-9XYRU0"
CHAT_ID = "1837395252"
CHECK_INTERVAL = 60  # έλεγχος κάθε 60 δευτερόλεπτα

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
            logging.warning("[TOKEN EXPIRED] 🔥 Το Telegram Bot Token φαίνεται invalid!")
            send_alert("⚠️ Το Telegram Bot Token έπαψε να ισχύει! Χρειάζεται νέο.")
        else:
            logging.info("[TOKEN VALID] ✅ Το token είναι έγκυρο.")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
