# chatbot.py

def get_response(message):
    message = message.lower()

    # Saudações
    if "olá" in message or "oi" in message:
        return "Olá! 👋 Como posso te ajudar hoje?"

    # Pedidos de ajuda ou explicação
    if "/help" in message or "o que você pode fazer" in message or "ajuda" in message or "comandos" in message:
        return (
            "🛠️ Eu posso te ajudar com:\n"
            "- Informações sobre a equipe FURIA 🎯\n"
            "- Jogadores e lineup atual 👊\n"
            "- Campeonatos e títulos 🏆\n"
            "- Curiosidades sobre o CS2 ⚡\n"
            "Também posso fazer animações de torcida usando o comando /torcida! 🔥"
        )

    # Sobre a FURIA
    if "furia" in message:
        return "A FURIA é uma organização brasileira de esports, destaque em CS2, Valorant, R6 e mais! 💛🖤"

    # Campeonatos
    if "campeonato" in message or "torneio" in message:
        return "A FURIA participa de campeonatos como ESL Pro League, BLAST Premier e Majors! 🚀"

    # Torcida
    if "/torcida" in message:
        return "🔥 VAMO FURIAAAAA!! 🔥"

    return "Desculpe, não entendi. Pode perguntar de outra forma? 🤔"
