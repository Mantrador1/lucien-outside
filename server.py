from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    return 'Webhook received', 200

@app.route('/', methods=['GET'])
def index():
    return 'Lucien Proxy is alive.', 200

