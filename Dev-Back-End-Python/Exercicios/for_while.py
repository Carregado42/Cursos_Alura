def exibir_mensagem_x_vezes():
    numero_de_vezes=int(input("quantas vezes que imprimir a mensagem de bem vindo?" ))

    n=0
    while n < numero_de_vezes:
        print("Bem vindo !")
        n=n+1



def soma_de_numeros():
    valores =[10,20,30,40,50]
    resultado=0
    for i in valores:
        resultado += i
    print(resultado)









menu =int (input(""" 
1 - Exibir mensagem de bem vindo 
2 - Soma de valores de uma lista
                 
Escolha uma exercicio:"""))

if menu == 1:
    exibir_mensagem_x_vezes()
elif menu ==2:
    soma_de_numeros()
elif menu ==3:
    pass

