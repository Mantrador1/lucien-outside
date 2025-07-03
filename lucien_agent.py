import requests

PROXY_URL = "https://lucien-proxy-production.up.railway.app/ask"

def ask_lucien(prompt):
    payload = {
        "prompt": prompt,
        "model": "dolphin-mixtral-8x7b"
    }

    response = requests.post(PROXY_URL, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("âŒ Error:", response.text)
        return None

if __name__ == "__main__":
    while True:
        prompt = input("ðŸ‘¤ Î•ÏƒÏ: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        reply = ask_lucien(prompt)
        print("ðŸ¤– Lucien:", reply)