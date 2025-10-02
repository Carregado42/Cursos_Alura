idade=int(input("Qual a idade? "))

if 0 < idade <=12:
    print("Criança")
elif  13>= idade < 18:
    print("adolescente")
elif idade >=18 :
    print("adulto")
else:
    print("valor invalido")