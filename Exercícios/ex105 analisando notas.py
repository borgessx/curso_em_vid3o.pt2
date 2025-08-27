def notas(*n, sit=False): # sit é uma condição, ele é opcional, por isso está recebendo false

    """
    -> Função para analisar notas.
        .n: recebe notas
        .sit: verifica a situação do aluno referente sua nota
        .return: retorna o dicionário
    """
    # vai incluir tudo no dicionário
    r = dict()
    r["qtde"]=len(n) # ler a quantidade de número na lista
    r["maior"]=max(n) # maior número da lista
    r["menor"]=min(n) # menor número da lista
    r["média"]=sum(n)/len(n) # sum é soma, dividido pela quantidade números da lista

    # utilizando o sit
    if sit: # só vai ser utilizado se o sit for TRUE.   "sit=True"
        if r["média"] >= 7:
            r["situação"]="BOA"
        elif r["média"] >= 5:
            r["situação"]="RAZOÁVEL"
        else:
            r["situação"]="RUIM"


    return r    # vai retorna o dicionário



resp=notas(5,3,4,9,4,3,sit=True)
print(resp)
help(notas)