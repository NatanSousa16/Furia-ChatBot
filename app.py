from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    user_msg = request.json["message"]

    # Simulação de respostas do bot
    resposta = gerar_resposta(user_msg)
    return jsonify({"response": resposta})

def gerar_resposta(msg):
    msg = msg.lower()
    if "últimos jogos" in msg:
        return "🏆 Últimos jogos:\n- FURIA 16 x 10 NAVI\n- FURIA 12 x 16 G2"
    elif "kscerato" in msg:
        return "🎯 KSCERATO - Rifler 🇧🇷\nIdade: 24\nRating HLTV: 1.13"
    elif "próximo jogo" in msg:
        return "📅 Próxima partida: FURIA vs FaZe - Sexta, 20h"
    else:
        return "Desculpa, não entendi. Tente: 'últimos jogos', 'kscerato', 'próximo jogo'..."

if __name__ == "__main__":
    app.run(debug=True)
