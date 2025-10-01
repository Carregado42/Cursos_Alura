

def menu():
    print("""
    1- Registo
    2- Ativar conta
    3- sair \n""")

def efetuar_registo():
    nome_utilizador=input("Nome de utilizador: ")
    palavra_pass=input("Palavra-passe:")

    print(f"Olá {nome_utilizador}!")

def finalizar_programa():
    print("Nenhuma das funcionalidades foi escolhida")



def escolher_opcoes():
    escolha_opcao=(int(input("Escolha a sua opçao: ")))

    if escolha_opcao == 1:
        efetuar_registo()
    elif escolha_opcao == 2:
        print("Ativar a conta")
    elif escolha_opcao==3:
        print("vamos sair")
    else:
        finalizar_programa()


def main():
    menu()
    escolher_opcoes()


if __name__ == '__main__':
    main()