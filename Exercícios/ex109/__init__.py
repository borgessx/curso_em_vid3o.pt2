def aumentando(n=0, porc=0, formato=False):
    res = n + (n * porc/100)
    return res if formato is False else moeda(res)

def diminuindo(n=0, porc=0,formato=False):
    res= n - (n * (porc / 100))
    return res if formato is False else moeda(res)

def metade(n=0,formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0,formato=False):
    res = n * 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
# deixa = 0 porque se nada for declarado vai ser 0
    return f'{moeda}{preco:.2f}'.replace('.',',') # vai trocar ponto por virgula