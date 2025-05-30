from datetime import datetime #data de atual, data do computador
dados = dict()
dados["nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = datetime.now().year - nasc # ano atual
dados["ctps"] = int(input("Carteira de trabalho (digite 0 se não tem): "))
if dados['ctps'] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salario"] = float(input("Salario:"))
    dados["aposentadoria"] = (dados["Contratação"] - nasc ) + 35


print("-="*30)                    
for k,v in dados.items():
    print(f"- {k} tem o valor {v}")                                   
