💬 ChatFURIA: Chatbot de Fãs da FURIA
Este projeto é uma aplicação Flask que oferece uma interface de chat interativa com um chatbot especializado no universo da FURIA Esports. Os usuários podem conversar com o bot sobre a equipe, seus jogadores, campeonatos e mais.

🚀 Funcionalidades
Interface web para conversas em tempo real

Respostas geradas por IA com base no contexto da FURIA

Rota /message para receber mensagens do usuário e responder via GPT-4

Arquitetura simples e modular para fácil expansão

🧠 Tecnologias Utilizadas
Python 3.8.10

Flask

HTML + CSS (para o front-end do chat)

Modelo de IA 

📁 Organização do Projeto
php
Copiar
Editar
chatfuria/
├── app.py                 # Aplicação principal Flask
├── chatbot.py             # Lógica do chatbot (get_response)
├── templates/
│   └── chat.html          # Interface web do chat
├── static/
│   ├── style.css          # Estilo visual (opcional)

🔒 Segurança e Privacidade
O chat não armazena histórico das conversas

Nenhuma informação pessoal do usuário é solicitada

Estrutura preparada para futura integração com login seguro e API

⚙️ Como Executar Localmente
Clone o repositório:
git clone https://github.com/seuusuario/chatfuria.git
cd chatfuria

Execute a aplicação:
python3 app.py

Acesse via navegador:
http://127.0.0.1:5000
