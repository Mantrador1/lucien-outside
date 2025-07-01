#!/bin/bash

# 1. Ενημέρωση πακέτων
sudo apt update

# 2. Εγκατάσταση Python και pip
sudo apt install python3-pip -y

# 3. Ορισμός Telegram BOT Token (ήδη ενσωματωμένος)
BOT_TOKEN="7387302970:AAFaL3pjJy3LVVnzBkmQrykDvDsGyTpC3SVg"

# 4. Δημιουργία Python script
cat <<EOF > bot.py
import requests

TOKEN = "${BOT_TOKEN}"

def get_me():
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

get_me()
EOF

# 5. Εκτέλεση του script
python3 bot.py
