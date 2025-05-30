from random import randint
from time import sleep
from operator import itemgetter #Ele é útil, por exemplo, para ordenar uma lista com base em um valor específico sem precisar escrever uma função manualmente.
jogo = {"Jogador1": randint(1,6),
        "Jogador2": randint(1,6),
        "Jogador3": randint(1,6),
        "Jogador4": randint(1,6)}
rank = {}
print("Valores sorteados")
for k,v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
rank = sorted(jogo.items(),key=itemgetter(1), reverse=True)# vai ordenar na chave 1
# o sorted para deixar em ordem crescente
# e o reverse = True para deixar decrescente
#deixou em formato de lista, e tuplas dentro. Então pode usar funções de lista, tipo enumerate
print("-___-"*30)
for i,v in enumerate(rank):
    print(f"{i+1} lugar: {v[0]} com {v[1]}.")
    sleep(1)

