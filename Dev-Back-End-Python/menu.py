import os

utilizadores=[]


def menu():
    print("""
    1- Registo
    2- Ver utilizadores
    3- Sair \n""")

def efetuar_registo():
    nome_utilizador=input("Nome de utilizador: ")
    print(f"Olá {nome_utilizador}!")
    utilizadores.append(nome_utilizador)
    input("Clique numa tecla para voltar ao menu")
    main()

def visualizar_utilizadores():
    print(utilizadores)

def finalizar_programa():
    print("A sair do programa")

def opcao_invalida():
    input("Opcao invalida\nClique numa tecla para voltar ao menu")
    main()


def escolher_opcoes():
    try:
        escolha_opcao=(int(input("Escolha a sua opçao: ")))

        if escolha_opcao == 1:
            efetuar_registo()
        elif escolha_opcao == 2:
            visualizar_utilizadores()
        elif escolha_opcao==3:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system("cls")
    # os.system(clear) #Mac
    menu()
    escolher_opcoes()

if __name__ == '__main__':
    main()