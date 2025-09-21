import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega chave do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configura o cliente com a chave
genai.configure(api_key=api_key)

# cria o cliente
client = genai.Client(api_key=api_key)

# Escolhe o modelo
model = genai.GenerativeModel("gemini-2.5-flash")


# Faz uma pergunta
resposta = model.generate_content("Quanto é 2 + 5 * 3")

print(resposta.text)



