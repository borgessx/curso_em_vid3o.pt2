jg = {}
jogos=[]
jg["nome"] = str(input("Nome do jogador? "))
part = int(input("Quantas partidas ele jogou? "))
for c in range(1,part+1):
    jogos.append(int(input(f"       - Quantos gols na partida {c}*? ")))
jg["gols"] = jogos[:]
jg["total"] = sum(jogos) #fazer soma do dicionario
print("-="*30)
print(jg)
print("-="*30)
for k,v in jg.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jg['nome']} jogou {part} partidas.")

for i, v in enumerate(jg["gols"]):
    print(f"        => Na {i+1}* partida, fez {v} gols.")
print(f"Foi um total de {jg['total']} gols.")