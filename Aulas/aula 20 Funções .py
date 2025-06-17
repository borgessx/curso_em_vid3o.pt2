def lin():
    print("-"*30)


#programa principal
lin()
print("Curso em vídeo")
lin()
lin()
print("Aprenda python")


def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


#Programa principal
titulo("    CURSO EM VÍDEO  ")  #ARGUMENTO (TXT)
titulo("    APRENDA PYTHON  ")  #ARGUMENTO (txt)
titulo("    GUSTAVO GUANABARA   ")  #argumento (txt)


#-->>> Parte Pratica ...

def soma(a,b):
    s = a + b
    print(s)


soma(4,5)
soma(14,8)
soma(a=1,b=20)
soma(b=67,a=4)

# * arg (tupla)
def contador(*núm):
    print(núm)


contador(2,1,7)
contador(8,0)
contador(15,3,6,9,4,8,7,2,6)

# usando for
def contador(*núm):
    for v in núm:
        print(f"{v} ",end="")
    print("FIM!")


contador(2,1,7)
contador(8,0)
contador(15,3,6,9,4,8,7,2,6)

# len
def contador(*núm):
    tam = len(núm)
    print(f"Recebi os valores {núm} e são ao todo {tam} números.")


contador(2,1,7)
contador(8,0)
contador(15,3,6,9,4,8,7,2,6)

# lista 
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos+=1


valores = [2,5,9,6,1,4,7]
dobra(valores)
print(valores)

#desempacotamento
def som(*valores):
    s = 0
    for n in valores:
        s += n
    print(f"Somando os valores {valores} temos {s}")


soma(5,6)
soma(8,2)