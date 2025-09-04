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

def resumo(p=0, porc=10, porcred=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'PREÇO ANALISADO: {moeda(p)}')
    print('-'*30)
    print(f"Metade \t{metade(p, True)}")
    print(f"Dobro \t{dobro(p, True)}")
    print(f"{porc}% de aumento \t{aumentando(p, 10, True)}")
    print(f"{porcred}% de redução \t{diminuindo(p, 13, True)}")