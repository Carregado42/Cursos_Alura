#Totodo o texto para minusculas 
texto="      MANIPULANDO E alterar O TIpo     da frase COM QUe     se esta a TRAbalhar        "
#print(texto)
#Print tudo em minusculas
#print(texto.lower())

#Print tudo em maisculas 
#print(texto.upper())

#Tirar espaços em branco inicio e fim
#print(texto.strip())

#Substituir 
#print(texto.replace("alterar","modificar"))

#Separar as palavras
lista_de_palavras=texto.lower().split()

#Junta as palavras depois de lhes fazer um split
print(" ".join(lista_de_palavras))

#Podemos juntar todos os metodos
#print(texto.lower().strip().replace("alterar","modificar"))
