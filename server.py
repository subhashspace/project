from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

@app.route("/process_audio", methods=["POST"])
def process_audio():
    text = "Hello, how can I help you?"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-3-8B-Instruct",
        "messages": [{"role": "user", "content": text}]
    }
    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
    return jsonify(response.json()["choices"][0]["message"]["content"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
