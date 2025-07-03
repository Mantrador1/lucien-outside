import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = "https://lucien-proxy-production.up.railway.app/webhook"

response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

print("Ã°Å¸â€â€” Webhook Set Response:")
print(response.json())
