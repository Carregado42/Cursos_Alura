


def vendas_no_comercio():
    """Crie um programa que receba o número de vendas dos dois produtos,
    exiba uma mensagem indicando qual deles vendeu mais.
    Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
    """

    try:
        produto_1 =int(input("Quantas maças foram vendidas: "))
        produto_2 =int(input("Quantas bananas foram vendidas: "))

        if produto_1==produto_2:
            print("Ambas tiveram as mesmas vendas")
        elif produto_1 > produto_2:
            print("As maças tiveram mais vendas")
        elif produto_2 > produto_1:
            print("As bananas tiveram mais vendas")

    except: 
        print("Erro ao inserir valor")
        vendas_no_comercio()


def tempo_total_projeto ():
    """Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto.
    Se algum valor for negativo, mostre uma mensagem informando o erro.
    """
    atividade_A = int(input("dias atividade A: "))
    atividade_B = int(input("dias atividade B: "))
    atividade_C = int(input("dias atividade C: "))

    if atividade_A < 0:
        print("os dias nao podem ser negativos!")
    elif atividade_B < 0:
        print("os dias nao podem ser negativos!")
    elif atividade_C < 0:
        print("os dias nao podem ser negativos!")
    else:
        print(atividade_A + atividade_B + atividade_C)


def classificar_categorias():
    idade=int(input("Qual a idade? "))

    if 0 < idade <=12:
        print("Criança")
    elif  13>= idade < 18:
        print("adolescente")
    elif idade >=18 :
        print("adulto")
    else:
        print("valor invalido")

def par_impar():
    numero = int(input("Escreva o numero para saber se é par ou impar: "))
    if numero % 2 ==0:
        print("Par")
    else:
        print("Impar")


menu =int (input(""" 
Escolha uma exercicio
1 - Vendas no comercio
2 - Tempo total projeto
3 - Classificar Categorias
4 - Par impar
"""))

if menu == 1:
    vendas_no_comercio()
elif menu ==2:
    tempo_total_projeto()
elif menu ==3:
    classificar_categorias()
elif menu == 4:
    par_impar()
