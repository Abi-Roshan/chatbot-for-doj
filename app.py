from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import chat  # import your function from chatbot.py

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests for frontend

@app.route('/chat', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chat(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
