import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

@app.route("/")
def index():
    return "Lucien is alive!"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        prompt = request.json.get("prompt", "")
        data = {
            "model": "anthropic/claude-3-opus",
            "messages": [{"role": "user", "content": prompt}]
        }
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res.raise_for_status()
        return jsonify({"response": res.json()["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
