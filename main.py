import os
import requests
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://lucien.localhost",
        "X-Title": "Lucien Proxy",
    }
    body = {
        "model": "mistral:7b-instruct",
        "messages": [
            {"role": "system", "content": "Είσαι ο Lucien. Έξυπνος, σύντομος και απόλυτος."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"⚠️ Σφάλμα AI: {str(e)}"
    resp = make_response(jsonify({"response": reply}))
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
