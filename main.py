from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Lucien is alive!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()
        response = f"🔮 Ερώτηση που έλαβα: {prompt}"
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
