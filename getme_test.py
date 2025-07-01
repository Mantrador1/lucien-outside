import requests

TOKEN = "7387302970:AAFaL3pjJy3LVVnzBkmQrykDvDsGyTpC3SVg"

def get_me():
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

get_me()
