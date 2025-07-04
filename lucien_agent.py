# -*- coding: utf-8 -*-
import requests

PROXY_URL = "https://lucien-proxy-production.up.railway.app/ask"

def ask_lucien(prompt):
    payload = {
        "prompt": prompt,
        "model": "dolphin-mixtral-8x7b"
    }

    response = requests.post(PROXY_URL, headers={"Authorization": f"Bearer {os.environ.get(\"OPENROUTER_API_KEY\", \"\")}"}, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("ÃƒÂ¢Ã‚ÂÃ…â€™ Error:", response.text)
        return None

if __name__ == "__main__":
    while True:
        prompt = input("ÃƒÂ°Ã…Â¸Ã¢â‚¬ËœÃ‚Â¤ ÃƒÅ½Ã¢â‚¬Â¢ÃƒÂÃ†â€™ÃƒÂÃ‚Â: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        reply = ask_lucien(prompt)
        print("ÃƒÂ°Ã…Â¸Ã‚Â¤Ã¢â‚¬â€œ Lucien:", reply)
