"""
try:
    operação
except:
    falhou
else:
    deu certo
finally:
    certo/falha
"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Problema encontrado foi {erro}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado.')