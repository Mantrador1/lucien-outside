import os
import requests
from flask import Flask, request

app = Flask(__name__)

OLLAMA_URL = os.environ.get("LLM_ENDPOINT", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.environ.get("LLM_MODEL", "llama3:8b")

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.get_json().get("prompt", "")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload)
        return res.text
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

# ?? Trigger redeploy
