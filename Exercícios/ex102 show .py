def fatorial(n, conta=False):
    """
    -> Calcular fatorial de um número.
        .n = O número a ser fatorado
        .show = (opcional) Se True mostra a conta, se False não mostra.
        .return = Retorna o resultado da fatorial.
    """
    resultado = 1
    for c in range(n,0,-1):
        if conta:
            print(c, end="")
            if c > 1:
                print(" X ", end="")
            else:
                print(" = ", end="")
        resultado *= c

    return resultado


print(fatorial(2, True)) 
help(fatorial)