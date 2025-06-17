pessoa = dict()
galera = list()
mulheres = list()
soma = media = 0
while True: 
    pessoa.clear() # excluiu o dicionario
    pessoa["nome"] = str(input("Nome: "))
    # validação, só vai aceitar se digitar m ou f, masculino ou feminino.   
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
            if pessoa["sexo"] == "F":
                mulheres.append(pessoa["nome"])
            break
        print("ERRO! Por favor digite novamente, apenas M ou F")
        
    pessoa["idade"] = int(input("Idade: "))
    soma+= pessoa["idade"]
    galera.append(pessoa.copy()) # a lista está copiando o dicionário

    #validação
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N ")
    if resp == "N":
        break
print("-="*30)
print(f"- Ao todo temos {len(galera)} pessoas cadastradas.") # len vai contar o tamanho da lista.
media = soma / len(galera)
print(f"- A média de idade é {media:.0f}")
print(f"- As mulheres cadastradas são {mulheres}")

"""
outra forma de fazer as mulheres cadastradas

for p in galera:
    if p["sexo] in "F":
        print(f"{p["nome]}", end='')
"""
print("- Lista de pessoas com a idade acima da média.")
for p in galera:
    if p["idade"] >= media:
        print(f"    *{p['nome']} com {p['idade']} anos.")
