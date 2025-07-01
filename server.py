from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Lucien Proxy is alive!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook: {data}")
    return {"status": "ok"}

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)


