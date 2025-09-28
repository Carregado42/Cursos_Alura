#Organizar os nomes dos alunos e dividir pelas salas
import random

def distribuiçao(nome, salas):
    sala = random.choice(salas)
    dic={
        "nome":" ".join(nome.lower().split()),
        "sala":sala
    }
    
    print(dic)


texto1 = "   jOãO      filipe   sIlvA   "
salas_de_aula=["sala 1", "sala 2", "sala 3"]

distribuiçao(texto1,salas_de_aula)