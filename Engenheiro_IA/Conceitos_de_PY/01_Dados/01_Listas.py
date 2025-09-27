lista=["python", "código", "segurança", "rede", "criptografia", "dados"]
lista2=["ze","miguel"]
# Len contagem de elementos da lista 
print("O comando len diz nos o tamanhano da lista. ", len(lista))

print("Para saber o ultimo elemento podemos apenas usar (lista[len(lista)-1]) ou lista[-1] o resultado é: ", (lista[len(lista)-1]), lista[-1])

#Dividindo a lista 
print(f"Primeira forma: {lista[1:3]} segunda forma {lista[:3]}")

print("\n## Adiciona ## \n")
#Adicionar elementos na lista 
lista.append("novoitem")
print(lista)

#Adicionar uma lista noutra lista extend
lista.extend(lista2)
print(lista)

#Adiciona uma lista no elemento de outra lista 
lista.append(["novoitem","isto e uma lista dentro de outra lista"])

#Adiciona um elemento a uma posiçao especifica 
lista.insert(5, "novo elemento na posiçao 5")
print(lista)

#Procura dentro da lista que esta dentro da lista 
print(lista[10][1])

print("\n## Remover ## \n")
lista_remover=["python", "código", "segurança","lista remover"]

#Remover elementos defenidos 
lista_remover.remove("código")
print(lista_remover)

#Remove posiçoes da lista 
lista_remover.pop(2)
print(lista_remover)

#Limpa toda a lista 
lista_remover.clear()  
print(lista_remover)




