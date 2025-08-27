def leiaInt(núm):
    ok = False
    valor = 0
    while True:
        n = str(input(núm))# está como str porque recebe qualquer coisa.
        if n.isnumeric(): # se for número
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok: # se ok estiver True
            print(f"Você digitou o número inteiro {valor}.")
            break

        # como é o valor que tranformou o número em inteiro, ele que vai retorna o resultado
    return valor



leiaInt("Digite um número: ")