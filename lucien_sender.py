import os
import requests
from dotenv import load_dotenv

# Î¦ÏŒÏÏ„Ï‰ÏƒÎ· Î¼ÎµÏ„Î±Î²Î»Î·Ï„ÏŽÎ½ Ï€ÎµÏÎ¹Î²Î¬Î»Î»Î¿Î½Ï„Î¿Ï‚ Î±Ï€ÏŒ .env
load_dotenv()

# Î›Î®ÏˆÎ· Ï„Î¿Ï… BOT_TOKEN ÎºÎ±Î¹ CHAT_ID Î±Ï€ÏŒ Ï„Î¿ .env
BOT_TOKEN = "7933465622:AAEUmAMT5YCJEA9EKT3wdiJ2FfG2xbh3_iw"
CHAT_ID = "1837395252"

# âœ… Î”Î¹Î±Î³Î½Ï‰ÏƒÏ„Î¹ÎºÎ¬ prints Î³Î¹Î± Î½Î± Î´ÎµÎ¹Ï‚ Ï„Î¹ Ï†Î¿ÏÏ„ÏŽÎ½ÎµÎ¹
print(f"BOT_TOKEN: {BOT_TOKEN}")
print(f"CHAT_ID: {CHAT_ID}")

# ÎˆÎ»ÎµÎ³Ï‡Î¿Ï‚ Î±Î½ Î­Ï‡Î¿Ï…Î½ Ï†Î¿ÏÏ„Ï‰Î¸ÎµÎ¯ ÏƒÏ‰ÏƒÏ„Î¬
if not BOT_TOKEN or not CHAT_ID:
    print("âŒ Î”ÎµÎ½ Î²ÏÎ­Î¸Î·ÎºÎµ BOT_TOKEN Î® CHAT_ID. ÎˆÎ»ÎµÎ³Î¾Îµ Ï„Î¿ Î±ÏÏ‡ÎµÎ¯Î¿ .env")
    exit(1)

# ÎœÎ®Î½Ï…Î¼Î± Ï€Î¿Ï… Î¸Î± ÏƒÏ„Î±Î»ÎµÎ¯
message = "ðŸš€ Lucien Proxy ÎµÎ½ÎµÏÎ³Î¿Ï€Î¿Î¹Î®Î¸Î·ÎºÎµ ÎµÏ€Î¹Ï„Ï…Ï‡ÏŽÏ‚."

# Î”Î·Î¼Î¹Î¿Ï…ÏÎ³Î¯Î± URL Î³Î¹Î± Ï„Î¿ Telegram API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Î£ÏŽÎ¼Î± Ï„Î¿Ï… Î±Î¹Ï„Î®Î¼Î±Ï„Î¿Ï‚
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

# Î‘Ï€Î¿ÏƒÏ„Î¿Î»Î® Î±Î¹Ï„Î®Î¼Î±Ï„Î¿Ï‚
try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print("âœ… ÎœÎ®Î½Ï…Î¼Î± ÏƒÏ„Î¬Î»Î¸Î·ÎºÎµ ÎµÏ€Î¹Ï„Ï…Ï‡ÏŽÏ‚.")
except requests.exceptions.RequestException as e:
    print(f"âŒ Î£Ï†Î¬Î»Î¼Î± ÎºÎ±Ï„Î¬ Ï„Î·Î½ Î±Ï€Î¿ÏƒÏ„Î¿Î»Î®: {e}")
    print(f"ðŸ” Response content: {response.text}")
