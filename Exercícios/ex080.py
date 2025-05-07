lista = list()
maior = 0
meio = 0
menor = 0
for c in range (0,5):
    n = int(input("Digite o valor: "))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:# o -1 seria o último elemento. Então lista último elemento.
        lista.append(n)
    
    else:
        pos =0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos= pos + 1 # pode ser ultilizar também pos += 1
            # esse +1 é para que cada vez que while for usado a posição aumente 1
print("-="*30)
print(f"Os valores digitados em ordem foram {lista}")          
    

print(lista)


"""
Dica para se usar no lugar do IF e ELIF .

    Ou podemos simplificar, o if e elif. Usar apenas um if. seguinte:

    if c == 0 or n > lista[-1]:
        lista.append(n)

    # então, se ele for o primeiro número ( c== 0, significa o primeiro número), ou(que é o or) se o n digitado for maior que o últimmo número.
    """ 