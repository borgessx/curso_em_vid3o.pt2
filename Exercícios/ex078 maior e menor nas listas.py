val=[]
maior = 0
menor = 0
for c in range (0,5):
    val.append(int(input(f"Digite o {c}* valor:")))
    if c == 0:
        maior=menor=val[c]
    else:
        if val[c] > maior:
            maior = val[c]
        if val[c] < menor:
            menor = val[c]

print("Voce digitou os seguintes valores",val)

print(f" O maior número foi {maior} nas posições", end=" ")
for pos, v in enumerate(val):
    if v==maior:
        print(f"{pos} ", end="")
print()       

print(f" O menor número foi {menor} nas posições", end=" ")
for pos, v in enumerate(val):
    if v==menor:
        print(f"{pos} ", end="")
print()


