def aumentando(n, porc):
    return n + (n * (porc / 100))


def metade(n):
    return n / 2


def dobro(n):
    return n * 2

def moeda(preco = 0, moeda = 'R$'):
# deixa = 0 porque se nada for declarado vai ser 0
    return f'{moeda}{preco:.2f}'.replace('.',',') # vai trocar ponto por virgula