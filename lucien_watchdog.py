import os
import time
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "logs/lucien_commands.log"
CHECK_INTERVAL = 1800  # 30 λεπτά
INACTIVITY_THRESHOLD_HOURS = 24

def get_last_activity():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                return None
            last_line = lines[-1]
            timestamp_str = last_line.split(" | ")[0].strip()
            return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except:
        return None

def send_alert():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "⚠️ Lucien inactivity alert: No interaction in the last 24h."
    }
    requests.post(url, json=payload)

def monitor():
    print("👁️ Lucien Watchdog Started")
    while True:
        last = get_last_activity()
        now = datetime.now()

        if not last or now - last > timedelta(hours=INACTIVITY_THRESHOLD_HOURS):
            print("⚠️ Inactivity detected.")
            send_alert()
        else:
            print("✅ Activity within limits.")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
