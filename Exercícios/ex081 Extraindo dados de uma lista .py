lista = list()
tem ="n"
while True:
    lista.append(int(input("Digite um valor: ")))
    per = str(input("Quer continuar? "))
    if per == "n":
        break

lista.sort()
print(lista)
print(f"Foram digitado {len(lista)} números")
if 5 in lista: # se número 5 estiver na lista
    print("O número 5 se encontra na lista")
else:
    print("o valor 5 não foi encontrado na lista.")



