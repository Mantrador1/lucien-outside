import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    if not request.is_json:
        return 'Invalid JSON payload', 400

    data = request.get_json()
    prompt = data.get('prompt', None)
    response = 'Hello from Lucien'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
