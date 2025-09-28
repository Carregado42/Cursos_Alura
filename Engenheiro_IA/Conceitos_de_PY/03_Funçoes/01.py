texto1 = "   jOãO      filipe   sIlvA   "
texto2 = "mArIa     isabel.    FeRnAnDeS   "
texto3 = "   pEdRo      CoStA"

def formatacao(texto):
    lista_palavras=texto.lower().split()
    print(" ".join(lista_palavras))

    #ou
    
    print(" ".join(texto.lower().split()))

formatacao(texto1)



salas_de_aula=["sala1", "sala2", "sala3"]