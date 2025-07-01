from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Lucien Proxy is running.', 200

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command')

    if command == 'ping':
        return jsonify({"response": "pong"}), 200
    else:
        return jsonify({"response": f"Unknown command: {command}"}), 400

if __name__ == '__main__':
    from waitress import serve
    port = int(os.environ.get('PORT', 8080))
    print(f"🔧 Serving on 0.0.0.0:{port}")
    serve(app, host='0.0.0.0', port=port)




