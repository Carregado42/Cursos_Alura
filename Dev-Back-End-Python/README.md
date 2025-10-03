## Main guard
#### É uma convenção em Python para marcar o ponto de entrada de um programa

    def main():  #Funções do fluxo, o que o programa faz quando é iniciado

    if __name__ == '__main__': 
        main()

## Estruturaçao do codigo 
    - snake_case para variáveis, funções e métodos;
    - PascalCase para classes;
    - SCREAMING_SNAKE_CASE para constantes.


## Arredondar casas decimais
    pi=3.14159
    print(f"{pi:.2f}")


## Condicionais
    if condiçao :
        o que vai ser realizado
    elif condiçao :
        o que vai ser realizado 
    else:
        se nenhuma das outras for efetuada é executada esta
    

    match opçao
        case opçao:
            o que vai ser realizado 


# Estruturas de dados

### Listas identificadas com [ ]
    lista = [ ] 
    
    As listas começam sempre por 0
    
    lista[2]                            - Vai buscar o segundo elemento que corresponde ao 3  

    len(lista)                          - Faz a contagem dos elementos da lista  

    lista[1:3]                          - Imprime do elemento 1 até 3 , o ultimo elemento nao é lido 

    lista[:3]                           - Do inicio até ao 3

    ------------------------------------------------------- Adicionar elementos ---------------------------------------------------
        lista = ["um", "pedro"]
        lista2 = ["items de outra lista" ]

        lista.append("novo")                - Adiciona um elemento novo na lista        # ["um", "pedro", "novo"]
    
        lista.append(["item1","item2"])     - Adiciona uma lista dentro de outra        # ["um", "dois", ['item1','item2']]
    
        lista.extend(lista2)                - Adicionar elementos de uma lista a outra  # ["um", "pedro", "items de outra lista" ]
    
    ------------------------------------------------------- Remove elementos -----------------------------------------------------
        lista = [1, 2, 3, 4, 5]

        lista.remove("3")   - Remove um elemento defenido # [1, 2, 4, 5]

        lista.pop(2)        - Remove uma posição # [1, 2, 4, 5]
        
        lista.remove(2)     - Remove o primeiro valor defenido # [1, 3, 4, 5] 

        lista.clear()       - Apaga toda a lista  # [] 
### Tuplas identificadas com ( )
    Tuplas nao podem ser alteradas mantem sempre os mesmos elementos com que foi defenida

### Dicionarios identificados por {} , podemos inserir dicionarios dentro de listas
    Dicionario = [chave:value]
    dicionario = {"pedro":10, "monica":14, "joao":18} 

    ----------------------------------- Procurar -----------------------------------   
    dicionario[chave]           # Value referente á chave procurada

    dicionario.get(joao)        # Se estiver na lista retorna o value referente

    dicionario.items()          # Mostra todos os items 
    
    dicionario.keys()           # Mostra todos as chaves 

    dicionario.values()         # Mostra todos as values 

    ----------------------------------- Remover -----------------------------------  
    dicionario.pop("value") #Remove TODOS os elementos em que a chave seja joao

# Docstring """ documentação """
    
    Usada logo a baixo de uma class ou funçao 
    Serve para documentar a funcionalidade 