import subprocess
import time
import requests
import json
import os

# === Ρυθμίσεις ===
TELEGRAM_TOKEN = "7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0"
NGROK_PATH = "C:/lucien_proxy/ngrok.exe"
FLASK_SCRIPT = "lucien_api.py"

# === Εκκίνηση Ngrok ===
print("🚀 Εκκινώ Ngrok...")
try:
    ngrok_proc = subprocess.Popen([NGROK_PATH, "http", "5000"])
except FileNotFoundError:
    print(f"❌ Δεν βρέθηκε το ngrok στο: {NGROK_PATH}")
    exit(1)

time.sleep(3)

# === Ανάκτηση Public URL ===
try:
    res = requests.get("http://localhost:4040/api/tunnels")
    tunnels = res.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"🌐 Public URL: {public_url}")
except Exception as e:
    print("❌ Σφάλμα από το Ngrok:", e)
    ngrok_proc.kill()
    exit(1)

# === Ορισμός webhook στο Telegram ===
print("🔗 Σύνδεση webhook...")
webhook_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
payload = {"url": public_url}
r = requests.post(webhook_url, data=payload)
print("📡 Telegram Response:", r.text)

# === Εκκίνηση Flask bot ===
print("🤖 Εκκίνηση Flask bot...")
subprocess.Popen(["python", FLASK_SCRIPT])

print("✅ Ο Lucien είναι online και σε ακούει.")
