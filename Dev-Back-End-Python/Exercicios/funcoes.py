def quantidade_caracteres():
    palavra=(input("digite a palavra: "))
    print (f"a palavra tem {len(palavra)} caracteres")





menu =int (input(""" 
Escolha uma exercicio
1 - Quantidade de caracteres numa palavra
2 - Tempo total projeto
3 - Classificar Categorias
4 - Par impar
"""))

if menu == 1:
    quantidade_caracteres()
