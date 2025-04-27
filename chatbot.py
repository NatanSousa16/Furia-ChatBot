import requests
from dotenv import load_dotenv
import os

# Carregar a chave da API do arquivo .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.openai.com/v1"

def get_response(user_message):
    conversation_history = [
        {"role": "system", "content": "Você é um assistente atencioso."},
        {"role": "user", "content": user_message}
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": conversation_history
    }

    try:
        response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        assistant_response = response.json()['choices'][0]['message']['content']
        return assistant_response
    except requests.RequestException as e:
        return f"Erro ao se comunicar com a API: {e}"

