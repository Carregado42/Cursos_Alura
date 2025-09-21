import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("API carregada:", api_key[:8], "...")  # só pra conferir

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.5-flash")
resp = chat.send_message("Diga apenas: funcionando")
print(resp.text)
