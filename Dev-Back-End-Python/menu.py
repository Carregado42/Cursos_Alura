import os

utilizadores=["pedro", "Filipe"]

def efetuar_registo():
    """Isto é uma docstring
    Função que efetua o registo do utilizador  

        Input:
            - Nome Utilizador

        Output:
    """
    nome_utilizador=input("\nNome de utilizador: ")
    print(f"Olá {nome_utilizador}!\n")
    utilizadores.append(nome_utilizador)
    voltar_menu_principal()

def visualizar_utilizadores():
    """Função qpara verificar os utilizadores registados 
        Input:

        Output:
            Utilizadores
    """
    print(utilizadores)
    voltar_menu_principal()

def finalizar_programa():

    print("A sair do programa")

def opcao_invalida():
    input("Opcao invalida\n")
    voltar_menu_principal()




def menu():
    print("""
    1- Registo
    2- Ver utilizadores
    3- Sair
    \n""")

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


def voltar_menu_principal ():

    input("\nClique numa tecla para voltar ao menu ")
    main()




def main():
    #os.system("cls") #windows
    os.system("clear") #Mac
    menu()

if __name__ == '__main__':
    main()