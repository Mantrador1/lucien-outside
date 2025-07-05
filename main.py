from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "anthropic/claude-3-opus",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        result = response.json()
        if "choices" in result and result["choices"]:
            return jsonify({"response": result["choices"][0]["message"]["content"]})
        else:
            return jsonify({"response": f"⚠️ AI Error: {result}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def index():
    return "Lucien is alive!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
