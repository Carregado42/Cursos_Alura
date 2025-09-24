import os
from google import genai
from dotenv import load_dotenv

# Carrega chave do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Cria o cliente
client = genai.Client(api_key=api_key)

# Escolhe o modelo
chat = client.chats.create(model="gemini-2.5-flash")


# Faz uma pergunta
resposta = chat.send_message("Quanto é 2 + 5 * 3")

print(resposta.text)



