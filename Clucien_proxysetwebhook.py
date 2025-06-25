import requests

TOKEN = "7547818090:AAHvBBkve3uRVASQcZofVO66O6nzwr5V_AI"
URL = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
NGROK_URL = "https://9af2-2a02-85f-e05d-76a9-803b-df02-9e68-ec18.ngrok-free.app"

response = requests.post(URL, data={"url": NGROK_URL})
print(response.text)
