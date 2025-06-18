jg = {}
jogos=[]
time = []

while True:
    jg.clear() # vai apagar o dicionário, para que cada laço a lista receba uma informação nova.
    jogos.clear()
    jg["nome"] = str(input("Nome do jogador? "))
    part = int(input("Quantas partidas ele jogou? "))
    for c in range(1,part+1):
        jogos.append(int(input(f"       - Quantos gols na partida {c}*? ")))
    jg["gols"] = jogos[:]
    jg["total"] = sum(jogos) #fazer soma do dicionario
    time.append(jg.copy()) # lista que vai receber os dados.

    #validação
    while True:
        resp = str(input("Quer continuar?")).upper()[0]
        if resp in "SN":
            break
        print("Erro! Responda apenas Sim e Não.")
    if resp == "N":
        break
print("-="*30)
print("cod", end="")
for k in jg.keys():
    print(f"{k:<15}", end="")
print()
print("--"*30)
for i, v in enumerate(time):
    print(f"{i:>3}", end="")
    for d in v.values():
        print(f" {str(d):<15}", end="")
    print()
print("=-"*30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 PARAR)"))
    if busca== 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com esse código {busca}")
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}') # time é a lista, o número que receber BUSCA vai ser o indice na lista, então exemplo indice 1 procure por "nome"
        for i,g in enumerate(time[busca]["gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")
