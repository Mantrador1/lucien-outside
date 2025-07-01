import os
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return "Lucien Proxy is alive"

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()

    # Αν δεν έχει έρθει JSON, γύρνα λάθος
    if not data or "command" not in data:
        return jsonify({"error": "Missing 'command' field"}), 400

    # Λάβε το περιεχόμενο του command
    cmd = data["command"]

    # Επιστρέφουμε απάντηση χωρίς να το εκτελούμε
    if cmd.lower() == "ping":
        return jsonify({"response": "pong"}), 200
    else:
        return jsonify({"response": f"Command '{cmd}' received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)



