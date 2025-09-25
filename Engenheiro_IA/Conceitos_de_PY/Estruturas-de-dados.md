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





