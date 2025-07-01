import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Lucien Proxy is running', 200

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()

    if not data or 'command' not in data:
        return jsonify({'status': 'error', 'message': 'Missing command field'}), 400

    command = data['command']

    # Dummy example: respond with pong
    if command == 'ping':
        return jsonify({'status': 'success', 'response': 'pong'}), 200

    # You can add more commands here
    return jsonify({'status': 'error', 'message': 'Unknown command'}), 400

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
