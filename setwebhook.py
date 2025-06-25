import requests

TOKEN = "7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0"
NGROK_URL = "https://1d43-2a02-85f-e05d-76a9-803b-df02-9e68-ec18.ngrok-free.app/"

URL = f"https://api.telegram.org/bot{TOKEN}/setWebhook"

payload = {"url": NGROK_URL}
response = requests.post(URL, data=payload)

print(response.status_code)
print(response.text)
