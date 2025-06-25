import requests

BOT_TOKEN = "7933465622:AAEUmAMT5YCJEA9EKT3wdiJ2FfG2xbh3_iw"
WEBHOOK_URL = "https://lucien-proxy-production.up.railway.app/webhook"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
response = requests.get(url, params={"url": WEBHOOK_URL})

print(response.status_code)
print(response.json())

