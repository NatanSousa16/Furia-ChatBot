import requests
from dotenv import load_dotenv
import os

# Carregar a chave da API do arquivo .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.openai.com/v1"

def get_response(user_message):
    # Respostas personalizadas para saudações
    saudações = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "oi, assistente"]
    
    # Verifica se a mensagem do usuário é uma saudação
    if any(saudação in user_message.lower() for saudação in saudações):
        return "Olá! Como posso ajudar você hoje? 😊"

    # Atualizar o contexto com o foco em FURIA e CS2
    conversation_history = [
        {"role": "system", "content": "Você é um assistente especializado em CS2 e na equipe FURIA. Responda apenas sobre o time FURIA, dicas de CS2, jogos, resultados, títulos e simulação de torcida."},
        {"role": "user", "content": user_message}
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",  # Use o modelo desejado
        "messages": conversation_history
    }

    try:
        response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()  # Verifica se a resposta da API foi bem-sucedida
        assistant_response = response.json()['choices'][0]['message']['content']
        return assistant_response
    except requests.RequestException as e:
        return f"Erro ao se comunicar com a API: {e}"

