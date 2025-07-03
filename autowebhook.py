import subprocess
import time
import requests
import json
import os

# === ÃŽÂ¡Ãâ€¦ÃŽÂ¸ÃŽÂ¼ÃŽÂ¯ÃÆ’ÃŽÂµÃŽÂ¹Ãâ€š ===
TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")
NGROK_PATH = "C:/lucien_proxy/ngrok.exe"
FLASK_SCRIPT = "lucien_api.py"

# === ÃŽâ€¢ÃŽÂºÃŽÂºÃŽÂ¯ÃŽÂ½ÃŽÂ·ÃÆ’ÃŽÂ· Ngrok ===
print("Ã°Å¸Å¡â‚¬ ÃŽâ€¢ÃŽÂºÃŽÂºÃŽÂ¹ÃŽÂ½ÃÅ½ Ngrok...")
try:
    ngrok_proc = subprocess.Popen([NGROK_PATH, "http", "5000"])
except FileNotFoundError:
    print(f"Ã¢ÂÅ’ ÃŽâ€ÃŽÂµÃŽÂ½ ÃŽÂ²ÃÂÃŽÂ­ÃŽÂ¸ÃŽÂ·ÃŽÂºÃŽÂµ Ãâ€žÃŽÂ¿ ngrok ÃÆ’Ãâ€žÃŽÂ¿: {NGROK_PATH}")
    exit(1)

time.sleep(3)

# === ÃŽâ€˜ÃŽÂ½ÃŽÂ¬ÃŽÂºÃâ€žÃŽÂ·ÃÆ’ÃŽÂ· Public URL ===
try:
    res = requests.get("http://localhost:4040/api/tunnels")
    tunnels = res.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"Ã°Å¸Å’Â Public URL: {public_url}")
except Exception as e:
    print("Ã¢ÂÅ’ ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± ÃŽÂ±Ãâ‚¬ÃÅ’ Ãâ€žÃŽÂ¿ Ngrok:", e)
    ngrok_proc.kill()
    exit(1)

# === ÃŽÅ¸ÃÂÃŽÂ¹ÃÆ’ÃŽÂ¼ÃÅ’Ãâ€š webhook ÃÆ’Ãâ€žÃŽÂ¿ Telegram ===
print("Ã°Å¸â€â€” ÃŽÂ£ÃÂÃŽÂ½ÃŽÂ´ÃŽÂµÃÆ’ÃŽÂ· webhook...")
webhook_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
payload = {"url": public_url}
r = requests.post(webhook_url, data=payload)
print("Ã°Å¸â€œÂ¡ Telegram Response:", r.text)

# === ÃŽâ€¢ÃŽÂºÃŽÂºÃŽÂ¯ÃŽÂ½ÃŽÂ·ÃÆ’ÃŽÂ· Flask bot ===
print("Ã°Å¸Â¤â€“ ÃŽâ€¢ÃŽÂºÃŽÂºÃŽÂ¯ÃŽÂ½ÃŽÂ·ÃÆ’ÃŽÂ· Flask bot...")
subprocess.Popen(["python", FLASK_SCRIPT])

print("Ã¢Å“â€¦ ÃŽÅ¸ Lucien ÃŽÂµÃŽÂ¯ÃŽÂ½ÃŽÂ±ÃŽÂ¹ online ÃŽÂºÃŽÂ±ÃŽÂ¹ ÃÆ’ÃŽÂµ ÃŽÂ±ÃŽÂºÃŽÂ¿ÃÂÃŽÂµÃŽÂ¹.")
