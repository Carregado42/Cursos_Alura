''' Desafio
1. Pedir para uma ia ferar uma lista de 20 emails
2. Criar uma função que vai receber como parametro a lista de emails, percorrer a lista 
e para cada email da lista chamar a ia do gemini pedir para resumir toodos os email em apenas 1 linha 
definindo o que cada pessoa queria no email
'''
emails = [
    "Olá, gostaria de saber mais informações sobre o vosso produto X.",
    "Preciso de ajuda para recuperar a minha palavra-passe.",
    "Quais são os planos e preços disponíveis atualmente?",
    "O meu pedido ainda não chegou, podem verificar?",
    "Gostaria de marcar uma reunião para discutir uma parceria.",
    "Podem enviar-me a fatura referente ao mês passado?",
    "Têm descontos para compras em grande quantidade?",
    "Estou interessado em fazer parte da vossa equipa, como me posso candidatar?",
    "Recebi um produto defeituoso, como posso proceder à troca?",
    "Queria cancelar a minha subscrição, como faço?",
    "Podem recomendar-me a melhor solução para pequenas empresas?",
    "Gostava de saber os horários de funcionamento da loja.",
    "É possível fazer o upgrade do meu plano atual?",
    "Qual o prazo de entrega médio para Portugal?",
    "Podem confirmar a receção do pagamento?",
    "Estou a ter dificuldades em aceder à minha conta.",
    "Gostava de obter um orçamento para os vossos serviços.",
    "Existe algum manual de utilização disponível?",
    "Quais os métodos de pagamento que aceitam?",
    "Gostava de ser notificado quando houver novidades."
]

import os
from google import genai
from dotenv import load_dotenv

# Carrega chave do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Cria o cliente
client = genai.Client(api_key=api_key)

def resumidor_de_emails(lista_de_emails):
  for email in lista_de_emails:
    resposta = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=f"""Vou te mandar o corpo de um e-mail. Quero que você o resuma em apenas 3 palavras,
passando o intuito daquele e-mail. Segue o e-mail: {email}"""
    )
    print(resposta.text)

email_bodies = [
    "Olá, gostaria de saber mais informações sobre o vosso produto X.",
    "Preciso de ajuda para recuperar a minha palavra-passe.",
    "Quais são os planos e preços disponíveis atualmente?",
    "O meu pedido ainda não chegou, podem verificar?",
    "Gostaria de marcar uma reunião para discutir uma parceria.",
    "Podem enviar-me a fatura referente ao mês passado?",
]

resumidor_de_emails(email_bodies)