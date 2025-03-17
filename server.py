from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/process_audio", methods=["POST"])
def process_audio():
    # Placeholder for audio-to-text conversion (use Google Speech-to-Text API)
    text = "Hello, how can I help you?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return jsonify(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
