import subprocess
import time
import requests
import json
import os

# === Î¡Ï…Î¸Î¼Î¯ÏƒÎµÎ¹Ï‚ ===
TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")
NGROK_PATH = "C:/lucien_proxy/ngrok.exe"
FLASK_SCRIPT = "lucien_api.py"

# === Î•ÎºÎºÎ¯Î½Î·ÏƒÎ· Ngrok ===
print("ðŸš€ Î•ÎºÎºÎ¹Î½ÏŽ Ngrok...")
try:
    ngrok_proc = subprocess.Popen([NGROK_PATH, "http", "5000"])
except FileNotFoundError:
    print(f"âŒ Î”ÎµÎ½ Î²ÏÎ­Î¸Î·ÎºÎµ Ï„Î¿ ngrok ÏƒÏ„Î¿: {NGROK_PATH}")
    exit(1)

time.sleep(3)

# === Î‘Î½Î¬ÎºÏ„Î·ÏƒÎ· Public URL ===
try:
    res = requests.get("http://localhost:4040/api/tunnels")
    tunnels = res.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"ðŸŒ Public URL: {public_url}")
except Exception as e:
    print("âŒ Î£Ï†Î¬Î»Î¼Î± Î±Ï€ÏŒ Ï„Î¿ Ngrok:", e)
    ngrok_proc.kill()
    exit(1)

# === ÎŸÏÎ¹ÏƒÎ¼ÏŒÏ‚ webhook ÏƒÏ„Î¿ Telegram ===
print("ðŸ”— Î£ÏÎ½Î´ÎµÏƒÎ· webhook...")
webhook_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
payload = {"url": public_url}
r = requests.post(webhook_url, data=payload)
print("ðŸ“¡ Telegram Response:", r.text)

# === Î•ÎºÎºÎ¯Î½Î·ÏƒÎ· Flask bot ===
print("ðŸ¤– Î•ÎºÎºÎ¯Î½Î·ÏƒÎ· Flask bot...")
subprocess.Popen(["python", FLASK_SCRIPT])

print("âœ… ÎŸ Lucien ÎµÎ¯Î½Î±Î¹ online ÎºÎ±Î¹ ÏƒÎµ Î±ÎºÎ¿ÏÎµÎ¹.")