from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

# Ã¢Å“â€¦ ÃŽÅ“ÃŽÂ½ÃŽÂ®ÃŽÂ¼ÃŽÂ· ÃŽÂ±ÃŽÂ½ÃŽÂ¬ IP (ÃŽÂ±Ãâ‚¬ÃŽÂ»ÃÅ’ dictionary Ãâ‚¬ÃÂÃŽÂ¿ÃÆ’Ãâ€°ÃÂÃŽÂ¹ÃŽÂ½ÃŽÂ¬)
memory = {}

# Ã°Å¸â€Â OpenRouter API Key
OPENROUTER_API_KEY = "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"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('prompt', '')
    user_ip = request.remote_addr

    if user_ip not in memory:
        memory[user_ip] = []

    memory[user_ip].append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "dolphin-mixtral-8x7b",
        "messages": memory[user_ip],
        "max_tokens": 500
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        memory[user_ip].append({"role": "assistant", "content": reply})
        return jsonify({"response": reply})
    else:
        return jsonify({"response": "Ã¢Å¡Â Ã¯Â¸Â ÃŽÂ£Ãâ€ ÃŽÂ¬ÃŽÂ»ÃŽÂ¼ÃŽÂ± ÃŽÂ¼ÃŽÂµ OpenRouter API."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5050)
