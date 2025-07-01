from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Προαιρετικό: logging για έλεγχο στο Railway
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "Lucien Proxy API is live", 200

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
        logging.exception("Error handling command")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




