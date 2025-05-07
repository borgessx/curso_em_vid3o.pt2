num = list()
imp=list()
par=list()

while True:
    num.append(int(input("Digite um valor: ")))
    resp=str(input("Quer continuar?"))
    if resp in "Nn":
        break
print("\n\n")   
print("-="*30)

print(f"A lista completa:{num}")
"""
for p, n in enumerate(num):  p e o n são letras aleatorias, pode colocar qualquer letra após o for.
    #na primeira letra(p) vai ser a posição dos valores, e a segunda letra (n) vai ser os valores que estão na lista
    print(p,n)
"""
for p, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v %2 == 1:
        imp.append(v)

print(f"Essa é a lista de númerso pares {par}")
print(f"Essa é a lista de númerso ímpares {imp}")
