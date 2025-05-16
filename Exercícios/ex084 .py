dados = []
analise= []
maior = []
menor = []
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(analise) == 0:
        maior = menor= dados[1]
    else:
        if dados[1] > maior:
            maior= dados[1]
        if dados[1] < menor:
            menor= dados[1]

    analise.append(dados[:])
    dados.clear() 
    pgt=str(input("Continuar? "))
    if pgt == "n":
        break
print("-_-"*20)    
print(analise)
print(f"Ao total, foram cadstrados {len(analise)} pessoas.")

print(f"O maior peso foi {maior}kg.",end="")
#falar o nome do individuo
for p in analise:
    if p[1] == maior:
        print(f"[{p[0]}]",end="")
print()

print(f"O menor peso foi {menor}kg.",end="")
for p in analise:
    if p[1] == menor:
        print(f"[{p[0]}]",end="")
print()



