# >>> RETURN

def somar(a=0,b=0,c=0):
    s=a+b+c
    return s
# s vai retornar para a variável
#⬇️
resp = somar(3,2,5)
# então o resp vai passar a valer a soma

#ou podendo utilizar o print
print(somar(2,4))

#>>> teste

r1 = somar(1,6,5)
r2 = somar(4,6)
r3 = somar(9)

print(f"O resultados foram {r1}, {r2}, {r3}")


# ............. Prática ...................

"""
O que é Fatorial?

O fatorial de um número natural, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. 
Ou seja, é a multiplicação do número por todos os seus antecessores até 1. 


Por exemplo:
3! = 3 * 2 * 1 = 6
5! = 5 * 4 * 3 * 2 * 1 = 120
6! = 6 * 5 * 4 * 3 * 2 * 1 = 720 

"""


def fatorial(num=1):
    f = 1
    for c in range(num,1,-1):
        f *= c
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n}! é igual a {fatorial(n)}")

# Retorna booleano

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Digite um número: "))
if par(num):
    print("é par!")
else:
    print("não é par!")