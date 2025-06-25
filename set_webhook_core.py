import requests

TOKEN = "7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0"
NGROK_URL = "https://a98a-2a02-85f-e05d-76a9-803b-df02-9e68-ec18.ngrok-free.app"

URL = f"https://api.telegram.org/bot{TOKEN}/setWebhook"

response = requests.post(URL, data={"url": NGROK_URL})
print(response.text)
