dic_nomes_medias = {"pedro":10, "monica":15, "joao":17}

# Procurar 
print("a media do joao é: ", dic_nomes_medias["joao"])
print("a media da monica é: ", dic_nomes_medias.get("monica"))
print("todos os items : ", dic_nomes_medias.items())
print("todos as chaves : ", dic_nomes_medias.keys())
print("todos as values : ", dic_nomes_medias.values())


# Remover
dic_nomes_medias.pop("joao")
print(dic_nomes_medias)

