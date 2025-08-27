def ficha(nome="<desconhecido>",gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

jg=str(input("Nome do jogador: ")).strip()  # usando o strip para tirar os espaços, para usar o if, if == a nada.
gl=str(input("Número de gols: ")).strip() # colocou string, porque se for int não deixa ficar vazio.
if gl.isnumeric():  # se a variável gl for número
    # se for número, vai receber int. Porque no input ele é STR
    gl = int(gl)
else:
    # se não tiver nada, ele recebe 0
    gl = 0

if jg == "": # poderia fazer assim também >>> if jg.strip() == "": <<<
    ficha(gols=gl) # se o jg que é nome não receber nada, ele vai mostrar apenas os gols.
else:
    ficha(jg,gl)  # tudo está completo, ele vai mostrar os dois.

    