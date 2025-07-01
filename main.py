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
    cmd = data.get("command", "")
    
    if cmd == "ping":
        return jsonify({"response": "pong"}), 200
    else:
        return jsonify({"error": "Unknown command"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)


