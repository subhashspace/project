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
