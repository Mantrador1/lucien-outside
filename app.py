from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

last_prompt = None
last_response = None

@app.route('/ask', methods=['POST'])
def ask():
    global last_prompt, last_response

    data = request.get_json()
    user_input = data.get('prompt', '')

    if last_prompt and last_response:
        user_input = f"Previous:\n{last_prompt}\nPrevious response:\n{last_response}\nCurrent:\n{user_input}"

    prompt = f"You are a thinking agent. Follow this process:\n" \
             f"1. Understand the question.\n" \
             f"2. Break it down if needed.\n" \
             f"3. Give a reasoned, structured answer.\n\n" \
             f"User input:\n{user_input}"

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json={
            "model": "llama3:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    answer = result.get("response", "[â›” No response]")

    last_prompt = user_input
    last_response = answer

    return jsonify({"response": answer}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
