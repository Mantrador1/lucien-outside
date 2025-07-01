from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "✅ Lucien Proxy is alive!"

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.json
    print(f"📩 Received update: {data}")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

