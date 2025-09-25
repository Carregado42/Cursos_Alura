'''
Uma cafeteria deseja automatizar o atendimento no balcão. 
O sistema deve permitir que o atendente registre os pedidos de cada cliente, calcule o valor total e aplique um desconto de 10% para clientes cadastrados.

O processo deve funcionar da seguinte forma:
    - O atendente informa quantos itens o cliente vai pedir.
    - Para cada item, o sistema solicita o nome e o preço.
    - Ao final, o sistema pergunta se o cliente é cadastrado.
    - Se for, aplica o desconto e exibe o valor com desconto.
    - Caso contrário, exibe o valor cheio.

'''

#Lista vazia com o pedido
pedido=[]
#Quntos items vai querer
quantidade=int(input("Quantos items vao ser:"))

#Ciclo para a quantidade de items que existem nome e valor 
for i in range(quantidade):
    #nome=input("nome: ")
    preço=float(input("preço: "))
    pedido.append(preço)

#Total de todos os items     
total=sum(pedido)

#Saber se se aplica ou nao o descont
cadastrado=input("É cadastrado? y/n ")

#Calculo do desconto
if cadastrado=="y":
    print(f"Desconto de 10% ficando a {total*0.9} euros")
else:
    print(f"Total do pedido: {total} euros")