import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Lucien Proxy is running."

@app.route("/command", methods=["POST"])
def command_handler():
    try:
        data = request.get_json(force=True)
        command = data.get("command", "").strip().lower()

        if command == "ping":
            return jsonify({"status": "success", "response": "pong"}), 200
        else:
            return jsonify({"status": "error", "message": "Unknown command"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Railway αναθέτει αυτόματα το PORT
    app.run(host="0.0.0.0", port=port)





