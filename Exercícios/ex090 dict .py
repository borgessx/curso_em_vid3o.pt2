info = dict()

info["nome"]=str(input("Nome: "))
info["média"]=float(input("Média: "))
info["situação"]="nada"
if info["média"] <5 :
    info["situação"]= "Reprovado"
elif info["média"] >5 and info["média"]<7:
    info["situação"]= "Recuperação"
elif info["média"] >7:
    info["situação"]= "Aprovado"
print("-"*30)
for k,v in info.items():
    print(f"{k} é igual a {v}")

