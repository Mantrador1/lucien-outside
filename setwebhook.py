import requests

BOT_TOKEN = "7933465622:AAFhHCGp4xxEn5KGvPmrbmdrDqkX-9XYRU0"
WEBHOOK_URL = "https://lucien-proxy-production.up.railway.app/webhook"

response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

print("🔗 Webhook Set Response:")
print(response.json())
