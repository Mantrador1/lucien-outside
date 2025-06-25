import requests

BOT_TOKEN = '7942409058:AAGphqehGWT3W9MIZ7xqZrgJAR3JbogFo5M'
CHAT_ID = '670585523'

def send_message_to_user(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    return response.json()

# ✅ Παράδειγμα χρήσης
if __name__ == '__main__':
    response = send_message_to_user("🔐 Ο Λυσιέν λέει: *Η σύνδεση είναι ενεργή. Στείλε μου εντολές*.")
    print(response)
