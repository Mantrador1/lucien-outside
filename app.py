import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "7933465622:AAEUmAMT5YCJEA9EKT3wdiJ2FfG2xbh3_iw"
CHAT_ID = "1837395252"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    result = send_message("LucienX Proxy Test: ✅ Το bot λειτουργεί!")
    print(result)
