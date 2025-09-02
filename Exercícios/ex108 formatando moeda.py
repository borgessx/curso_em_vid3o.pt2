import ex108 as ex


preco = float(input("Digite o preço: "))
print(f"A metade de R${ex.moeda(preco)} é {ex.moeda(ex.metade(preco))}")
print(f"A dobro de R${ex.moeda(preco)} é {ex.moeda(ex.dobro(preco))}")
print(f"Aumentando 10% de R${ex.moeda(preco)} é {ex.moeda(ex.aumentando(preco,10))}")

