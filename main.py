import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
OPENROUTER_API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/ask', methods=['POST'])
def ask():
    if not request.is_json:
        return jsonify({'error': 'Invalid JSON payload'}), 400

    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided.'}), 400

    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        return jsonify({'error': 'OPENROUTER_API_KEY not set.'}), 503

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': prompt}]
    }

    response = requests.post(OPENROUTER_API_ENDPOINT, headers=headers, json=payload)

    if response.status_code != 200:
        return jsonify({'error': f'OpenRouter error {response.status_code}', 'details': response.text}), 502

    result = response.json()
    reply = result.get('choices', [{}])[0].get('message', {}).get('content', '')

    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
