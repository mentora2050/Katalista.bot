from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API Key from Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "app": "Katalista Bot Backend"
    })

@app.route("/ai", methods=["POST"])
def ai_response():
    data = request.json

    user_prompt = data.get("prompt")

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are Katalista AI. Give smart, clear, practical advice in simple Arabic."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        max_tokens=500
    )

    reply = response.choices[0].message.content

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run()
