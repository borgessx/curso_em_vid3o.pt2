matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap=somat=maiors=0
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c]=int(input(f"Digite um número para [{l},{c}]: "))
        if l == 0:
            maiors = matriz [1][c]
        elif matriz [1][c] > maiors:
            maiors = matriz [1][c]





print("#"*30)

for l in range (0,3):
    somat+=matriz[l][2]
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz [l][c] % 2 == 0:
            somap+=matriz[l][c]
    print()
print("#"*30)
print(f"A soma dos valores pares é {somap}")
print(f"A soma dos valores da terceira coluna é {somat}")
print(f"O maior valor da segunda linha é {maiors}")

         