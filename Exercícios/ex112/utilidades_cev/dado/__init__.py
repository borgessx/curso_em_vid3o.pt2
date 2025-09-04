def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',','.') #substitui todas as virgulas por ponto
        if entrada.isalpha() or entrada == '':
            """
            .isalpha()
            é usado para verificar se todos os caracteres de uma string são letras do alfabeto (sem números, sem espaços, sem símbolos).

            👉 Funcionamento:

            Retorna True se todos os caracteres da string forem letras.
            
            Retorna False se existir qualquer número, espaço ou caractere especial.
            """
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[0m')
        else:
            valido = True
            return float(entrada)
    return None
