"""
[:] isso significa um fatiamento completo
utilizar para fazer cópias em lista



"""

dados = ["pedro",25]
print(dados[0]) # pedro
print(dados[1]) # 25
print(dados[:]) # lista inteira

# outro exemplo

dados1 = ["ana","maria","Raquel","kayke","Geh","Gabriel"]
print(dados1[0:2]) # ele vai ter saída do 0 ao 1, que é ana e maria. Sempre vai um número a menos no final.
print(dados1[2:5]) # vai sair do 2 ao 4, raquel,kayke e geh.
print(dados1[:]) # lista inteira

# adicionar uma lista na outra
copia = list()
copia.append(dados[:])#copie o que estava na lista dados
print(copia)

#lista composta
testef=list()
teste1=["Maria", 19]
teste2=["João",15]
teste3=["Ednaldo",50]

testef.append(teste1[:]) #0
testef.append(teste2[:]) #1
testef.append(teste3[:]) #1
print(testef)
print(testef[0]) # ele vai mostrar a primeira lista que estar dentro da testef, que é teste1.
print(testef[0][0])# ele vai na primeira lista, e primeiro elemento dessa lista, então o segundo zero é maria.
print(testef[0][1]) # ele vai na primeira lista, e segundo elemento dessa lista

#outro exemplo de composta

pessoa = [["Maria", 19],["João",15],["Ednaldo",50]]
print(pessoa[0][1])# 19
#quero apenas os nomes
for nome in pessoa: # o nome vai pegar cada lista dentro dessa lista composta
    print(nome[0])# vai printa cada elemento 0 de cada lista
    print(nome)# cada lista dentro da composta
    print(f"{nome[0]} tem {nome[1]} anos")# nome[1] vai pegar o elemento 1 de cada lista

print("\n\n\Copia e depois excluir\n")
galera = []
dados2 = []
men=mai=0
for c in range(0,3):
    dados2.append(str(input("Nome: ")))
    dados2.append(int(input("Idade: ")))
    galera.append(dados2[:])
    dados2.clear()
print(galera)

#idade

for p in galera:
    if p[1]>=18:
        print(f"{p[0]} é maior de idade.")
        mai+=1
    else:
        print(f"{p[0]} é menor de idade, ele tem {p[1]} anos.")
        men+=1
print(f"Temos {men} menores de idade, e {mai} maiores de idade.")

