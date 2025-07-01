
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

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
    port = os.getenv('PORT', default=5000, type=int)
    app.run(host='0.0.0.0', port=port)




