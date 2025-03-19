from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Fetch API Key securely from Render environment variables
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

@app.route('/')
def home():
    return "AI Chatbot Server is Running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8B-Instruct",
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post("https://api.together.xyz/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    else:
        return jsonify({"error": "Failed to fetch response"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
