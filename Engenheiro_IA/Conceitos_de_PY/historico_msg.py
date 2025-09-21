import os
from google import genai
from dotenv import load_dotenv

# Carrega chave do .env e Cria o CLient necessario em todo os projetos 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


# Cria um chat com contexto
chat = client.chats.create(model="gemini-2.5-flash")


resposta = chat.send_message("O que é a inteligencia artificial em 10 palavras?")
print(resposta.text)