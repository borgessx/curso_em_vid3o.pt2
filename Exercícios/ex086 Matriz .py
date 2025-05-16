matriz = [[0,0,0],[0,0,0],[0,0,0]]
# estrutura para alimentar a lista
for l in range(0,3): # ele vai contar as lista que estão dentro da composta
    for c in range(0,3): # contar elemento dentro das lista. ex lista 0, elementos 1 2 3, lista 1, elemento 1 2 3
       matriz [l] [c] = int(input(f"Digite um número:"))    
print("-="*30)
#estrutura para printar na tela
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        # :^5 da um espaço de cinco caracteres, e o ^ centraliza eles.
    print() # esse print está sendo usado para quebrar a linha, a cada tres repetições a linha quebra, para ficar um embaixo do outro.

