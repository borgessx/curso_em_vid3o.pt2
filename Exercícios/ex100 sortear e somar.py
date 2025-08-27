def sorteia(lista):
    from time import sleep
    from random import randint
    print("Sorteando 5 valores da lista: ", end="")
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print(" PRONTO!")

def somarPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma+=v
    print(f"Somando os valores pares {lista}, total: {soma}")

números = list()
sorteia(números)
somarPar(números)