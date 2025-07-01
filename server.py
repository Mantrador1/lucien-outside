from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return "Lucien Proxy is alive"

if __name__ == "__main__":
    print("Running locally on http://127.0.0.1:8080")
    serve(app, host="0.0.0.0", port=8080)


