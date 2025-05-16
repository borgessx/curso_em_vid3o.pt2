impar= list()
par=list()



for c in range(1,8):
    num=int(input(f"Digite o {c}o. valor:"))
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

print(f"Os números pares foram {par}")
print(f"Os números ímpares foram {impar}")