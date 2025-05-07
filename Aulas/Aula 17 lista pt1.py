
"""
obs:

*para ser uma lista tem que utilizar chaves []

*para adicionar elementos novos - append - ex: lanche.append("bolacha") 

*para adicionar elementos em outras posições - insert - ex: lanche.insert("0,bolacha") estou adicionando uma bolacha na posição 0.


*apagar elemento - del lanche - ex: del lanche[3]
>outro, ex: lanche.pop(3), se lanche.pop() - ele vai eliminar o ultimo elemento
>outro, ex: lanche.remove("bolacha"), se quiser eliminar pelo o que está escrito, utilizar remove. Se quiser pelo número da chave use del e pop.



*função IN em lista
*if bolacha in lanche:
    lanche.remove("bolacha")
essa função vai procuraR A BOLACHA no lanche, se estiver, vai excluir.


"""
valores=list(range(4,11))#ele cria uma lista de 4 a 10. O último número não conta que é o 11
print(valores)

valores1=[3,1,6,5,9,8,7,2,0]
valores1.sort()#ele coloca os valores em ordem númerica
print(valores1)

valores2=[3,1,6,5,9,8,7,2,0]
valores2.sort(reverse=True)#deixa em ordem decrescente
print(valores2)

print(len(valores2))#diz a quantidade de elementos
print("\n\n")
"""
Prática


"""
num=[9,4,2,7,6,1,0]
num[0]=5 #elemento na posição 0 vira 5
num.append(4)
num.sort(reverse=True) #true decrescente, e false crescente 
num.insert(1,8)# 1 a posição, e 8 substitui 
num.append(6)
num.remove(6)#ele vai remover o número seis, só que tem dois números seis, ele vai remover o primeiro. Porque ele começa da esquerda para direita.

print(num,"\n")

#novo exemplo, criar lista vazia.
print("________5555555_____________________")
val = []
val.append(5) # alt + shift + seta pra cima
val.append(9)
val.append(4)

#outra forma de mostrar os valores
for  valores in val:
    print(f"{valores}...",end="")
print("\n")

for c, v in enumerate(val):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")
print("\n\n")

#adicionar valores, outra forma
"""
val2 = []
for cont in range(0,5):
    val2.append(int(input("Adicione um número:")))
print(val2)
"""

#Utilizar duas lista, se alterar em uma, altera em outra. Isso é ligação de lista
a =[1,2,3,4]
b = a
b[2]=8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

print("\n\nCópia")
#como fazer uma copia
a =[1,2,3,4]
b = a [:]#ele vai fazer uma cópia, pegar todos valores de A e colocar em B
b[2]=8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
#no A continua 3 e no B vira 8
