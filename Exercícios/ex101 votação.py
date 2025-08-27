from datetime import datetime
def votoObrigatorio(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade >= 18:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    else:
        return f"Com {idade} anos: NÃO VOTA"



print("-"*30)
datanasc = int(input("Em que ano voce nasceu: "))
print(votoObrigatorio(datanasc))
print("-"*30)