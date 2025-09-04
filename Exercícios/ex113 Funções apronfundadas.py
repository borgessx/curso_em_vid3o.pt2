def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[033mUsuário preferiu não digitar esse número.\033[0m')
            return None
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[033mUsuário preferiu não digitar esse número.\033[0m')
            return None
        else:
            return n


num = leiaInt('Digite um valor Inteiro: ')
numr = leiaFloat('Digite um valor Real: ')
print(f'O valor Inteiro digitado foi {num} e o Real {numr}')