import ex109 as ex


preco = float(input("Digite o preço: "))
print(f"A metade de R${ex.moeda(preco)} é {ex.metade(preco,True)}")
print(f"A dobro de R${ex.moeda(preco)} é {ex.dobro(preco,True)}")
print(f"Aumentando 10%, temos {ex.aumentando(preco,10,True)}")
print(f"Reduzindo 13%, temos {ex.diminuindo(preco,13,True)}")

