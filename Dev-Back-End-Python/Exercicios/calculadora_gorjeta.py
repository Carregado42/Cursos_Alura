"""
um programa que receba o valor total da conta e a porcentagem de gorjeta desejada 
e exiba o valor final que o cliente deverá pagar.

input:
    valor total da conta
    percentagem da gorjeta
"""

valor_conta = int(input("Valor da conta: "))
percentagem_gorjeta = int(input("percentagem da gorjeta: "))
valor_gorjeta_euros = (percentagem_gorjeta/ 100)*valor_conta

print(f"O valor da gorjeta é {valor_gorjeta_euros}€ e o total a pagar é {valor_gorjeta_euros + valor_conta }")