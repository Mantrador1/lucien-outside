# -*- coding: utf-8 -*-
from flask import Flask, request, jsonifyapp = Flask(__name__)@app.route("/ask", methods=["POST"])def ask():    data = request.get_json()    prompt = data.get("prompt", "")    response = f"?? Lucien ed? � �?? e?pe?: '{prompt}'"    return jsonify({"response": response})if __name__ == "__main__":    import os`nport = int(os.getenv("PORT", 0))`napp.run(host="0.0.0.0", port=port)

