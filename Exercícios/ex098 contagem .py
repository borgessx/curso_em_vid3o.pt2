from time import sleep


def contador(inicio,fim,passo):
    # caso coloquem 0 no passo, como não é possível contar de 0 em 0, então recebe 1.
    if passo == 0:
        passo = 1
    """
    se for número negativo, mutiplicar para que os números virem negativos.
    Para que cada laço do while os números virem negativos.

    if passo < 0:
        #passo *= -1

    Mas o meu nem preciso utilizar essa multiplicação
    """
    print(f">> Contagem de {inicio} até {fim}, de {passo} em {passo}.")
    if inicio < fim: # esse if foi criado para contagem decrescente
        # contador
        cont = inicio
        while cont <=fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += passo
        print("  FIM!")
    # contador contagem decrescente
    else:
        cont= inicio
        while cont >= fim:
            print(f"{cont} ", end="",flush=True)
            sleep(0.5)
            cont-=passo
        print("  FIM!")

# contador(1,500,14)

#contagem personalizada
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)