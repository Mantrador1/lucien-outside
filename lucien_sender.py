import os
import requests
from dotenv import load_dotenv

# Φόρτωση μεταβλητών περιβάλλοντος από .env
load_dotenv()

# Λήψη του BOT_TOKEN και CHAT_ID από το .env
BOT_TOKEN = "7933465622:AAFhHCGp4xxEn5KGvPmrbmdrDqkX-9XYRU0"
CHAT_ID = os.getenv("CHAT_ID")

# ✅ Διαγνωστικά prints για να δεις τι φορτώνει
print(f"BOT_TOKEN: {BOT_TOKEN}")
print(f"CHAT_ID: {CHAT_ID}")

# Έλεγχος αν έχουν φορτωθεί σωστά
if not BOT_TOKEN or not CHAT_ID:
    print("❌ Δεν βρέθηκε BOT_TOKEN ή CHAT_ID. Έλεγξε το αρχείο .env")
    exit(1)

# Μήνυμα που θα σταλεί
message = "🚀 Lucien Proxy ενεργοποιήθηκε επιτυχώς."

# Δημιουργία URL για το Telegram API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Σώμα του αιτήματος
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

# Αποστολή αιτήματος
try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print("✅ Μήνυμα στάλθηκε επιτυχώς.")
except requests.exceptions.RequestException as e:
    print(f"❌ Σφάλμα κατά την αποστολή: {e}")
    print(f"🔁 Response content: {response.text}")
