import requests

TOKEN = "7548930151:AAHARRlyNcLiLUFXeoSXWnwt-LKRE0mF7c"

def delete_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

delete_webhook()
