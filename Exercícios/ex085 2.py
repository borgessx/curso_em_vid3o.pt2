num=[[],[]] # primeiro quadro é o parte 0 e segundo 1
valor=0
for c in range(1,8):
    valor=int(input(f"Digite o {c}o. valor: "))
    if valor % 2 == 0:
        num[0].append(valor) # vai ser adicionado na parte 0
    else:
        num[1].append(valor) # vai ser adicionado na parte 1

num[0].sort() #deixa os números em ordem númerica
num[1].sort() 
print(f"Os valores ímpares digitados foram: {num[1]}")
print(f"Os valores pares digitados foram: {num[0]}")
