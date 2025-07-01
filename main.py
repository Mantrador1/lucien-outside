import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY") or "sk-xxxxx"  # Βάλε το δικό σου OpenRouter API Key
MODEL = "mistralai/mistral-7b-instruct"  # Ή όποιο άλλο θες

@app.route('/')
def home():
    return '🧠 Lucien Proxy is listening at /process'

@app.route('/process', methods=['POST'])
def process():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Missing message field'}), 400

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "Είσαι ο Λυσιέν. Μίλα ελληνικά, με δύναμη, στρατηγική και φροντίδα. Απάντα με ακρίβεια."},
                {"role": "user", "content": user_input}
            ]
        }
    )

    if response.status_code != 200:
        return jsonify({"error": "API failed", "details": response.text}), 500

    reply = response.json()["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
