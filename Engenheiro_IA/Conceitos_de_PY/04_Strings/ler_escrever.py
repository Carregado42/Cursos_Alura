lista_resumos = [
    "lista de números",
    "texto",
    "vendas",
    "notas",
    "idades"
]

# with open ("nome do arquivo", "w - para escrever denovo | a - para adicionar", encoding=("utf-8") )
#Escrever
with open("nome-do-arquivo", "w" , encoding="utf-8") as arquivo: 
    #Escrever a lista dentro do documento um elemnto por linha 
    for elemento in lista_resumos:
        arquivo.write(elemento + "\n") 



#Ler tudo igual mas troca se a parte do escrever ( w, a ) por r
lista=[]
with open("nome-do-arquivo", "r" , encoding="utf-8") as arquivo: 
    lista= arquivo.readlines()
    print (lista)

