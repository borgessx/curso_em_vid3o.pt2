num= list()#o num recebe lista vazia, isso é utilizado para receber números.

while True:#'enquanto' em portugues
    # while True é um çoop infinito, só para com o BREAK
    n=int(input("Digite um valor: "))
    if n not in num:
        num.append(n)#ele vai adicionar o valor, o append adiciona valor, o N vai ser o número recebido no input.
        print("Valor adicionado.")
    else:
        print("Valor duplicado! Não será adicionado.")
    r=str(input("Quer continuar? "))
    if r in "NaoNAONÃOnão":
        num.sort(reverse=False)
        print(f"Os valores adicionados foram {num}")
        
        print("PROGRAMA FINALIZADO!!")

        break

