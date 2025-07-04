from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.route("/")
def home():
    return "Lucien is running."

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Missing 'prompt'"}), 400

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-4",
            "messages": [
                {"role": "system", "content": "Απαντάς στα ελληνικά, είσαι ο Λυσιέν, ένας ήρεμος, έξυπνος, στρατηγικός AI."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            return jsonify({"error": f"OpenRouter API error: {response.text}"}), 500

        result = response.json()
        answer = result["choices"][0]["message"]["content"]

        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
