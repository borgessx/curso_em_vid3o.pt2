exp = str(input("Digite a expressão:"))
pilha= []
for simb in exp: #ele vai mostrar os caracteres que estão na lista.
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:#se já tiver algum elemento
            pilha.pop()# quando digitar esse ), vai remover esses (
        else:
            pilha.append(")")# se não tiver nada na lista, vai adicionar esse )
            break
if len(pilha) == 0: # como os ), vai eliminar esses (. Então a lista vai ficar vazia.
    print("Expressão válida!")
else:
    print("Expressão Inválida!")