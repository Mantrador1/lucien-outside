from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    return jsonify({"response": f"🤖 Ερώτηση: {prompt}"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
