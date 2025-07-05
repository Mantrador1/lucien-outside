from flask import Flask, request, jsonify
from router import route_request

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        if not prompt:
            return jsonify({'response': '?? No prompt provided.'}), 400

        response = route_request(prompt)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'response': f'? Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
