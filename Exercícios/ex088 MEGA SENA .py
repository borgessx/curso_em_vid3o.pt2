from time import sleep
from random import randint

lista = list()
jogos = list()
perg=int(input("Quantos jogos sorteiar:"))
tot=1

while tot <= perg:
    cont= 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont  >= 6:
            break
    tot+=1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print("-="*3,f"Sorteando {perg} jogos","-="*3)
sleep(2)
for n,c in enumerate(jogos):
    print(f"Jogo {n+1}: {c}")