#Exibir 1 por 1 a lista 
print("\n Exibe um elemento por linha de uma lista")

lista_dados=[
    {"nome":"joao","media":10},
    {"nome":"maria","media":15},
    ]

for i in lista_dados:
    print (i)


#Se for um dicionario apenas imprime as chaves sem os valores 
print("\nApenas imprimir chaves")

dic={"pedro":10,
     "filipe":20}

for i in dic:
    print(i)
    

# Possibilidade de serem passados dois valores 
print("\nPassar dois valores para o for")
for key, value in dic.items():
    print(f"a chave é {key} e o valor é {value}")


# Par ou impar 
print("\nPar ou impar")
for n in range(11):
    if n % 2 == 0:
        print(n) 