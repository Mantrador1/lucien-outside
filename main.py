import os
from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 8080  # Σταθερή πόρτα, όπως το δείχνουν τα logs του Railway

@app.route('/', methods=['GET'])
def home():
    return "Lucien Proxy is running."

@app.route('/command', methods=['POST'])
def command():
    try:
        data = request.json
        command = data.get('command', '')

        if command == 'ping':
            return jsonify({'status': 'success', 'response': 'pong'})
        else:
            return jsonify({'status': 'error', 'message': 'Unknown command'}), 400

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

