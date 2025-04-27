from flask import Flask, render_template, request, jsonify
from chatbot import get_response  # Agora a importação de get_response deve funcionar

app = Flask(__name__)

@app.route("/")
def chat():
    return render_template("chat.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    user_message = data.get("message")
    if not user_message:
        return jsonify({"response": "Mensagem vazia."})

    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
