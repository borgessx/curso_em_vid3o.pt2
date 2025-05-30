# são identificados por chaves {}
# dados = dict()  vazio
# dados = {}
# como colocar dados
"""
dados = {"nome":"Pedro"} o índice é nome, e o valor é Pedro
dados = {"nome":"Pedro","idade":25} o índice é nome e idade, e os valores são os que estão depois da :
print(dados["nome"])     Pedro
print(dados["idade"])    25
"""
# como adicionar elementos
"""
dados["sexo"]="M"       O dicionário vai adicionar esse índice e valor
print(dados)
vai receber isso 
{"nome":"Pedro","idade":25,"sexo":"M"}
"""
# eliminar elemento
"""
del dados["idade"]
"""
# outra forma de criar um dicionário
"""
Posso criar um que posso abrir chave em uma linha, e fechar na outra linha
filme = {"titulo":"Star Wars",
"ano":1977,
"diretor":"George Lucas"
}
o Python chama esse elementos de keys (chaves)

print(filme.values()) vai printar apenas os valores
que seria: Star wars, 1977 e George Lucas

print(filme.keys()) vai printar apenas os índices
que seria: titulo, ano e diretor

print(filme.items()) vai printar tudo
"""
# usar o for em dicionário
"""
for k,v in filme.items():   # k é as keys, os índices. v é os valores.
    print(f"O {k} é {v})
vai mostrar isso:
O titulo é Star wars
O ano é 1977
O diretor é George Lucas
"""
#fazer soma
#sum(nome do dicionario)

# Exemplo 2: Usando enumerate para mostrar uma lista de tarefas
"""
tarefas = ["Estudar Python", "Fazer exercícios", "Ler um livro", "Beber água"]

# O enumerate vai te dar o número da tarefa (índice) e o nome da tarefa
for numero, tarefa in enumerate(tarefas, start=1):  # start=1 faz começar do 1 em vez de 0
    print(f"Tarefa {numero}: {tarefa}")

# Prática:
# 1. Crie sua própria lista com tarefas do dia ou objetivos da semana.
# 2. Use o enumerate com start=1 para numerar e exibir cada item da lista.
"""



# Parte Prática

pessoas = {"nome":"Gabriel","idade":18,"sexo":"M"}
print(pessoas)
print(pessoas["nome"])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.") 
#INFORMAÇÃO IMPORTNATE
# SE USAR ESSAS "", NOS COLCHETES VAI USAR ESSA ' ', E MESMO PARA SE USAR ESSA ' ', NOS COLCHETES VAI USAR ESSA ""
print(pessoas.values()) # printa valores
print(pessoas.keys()) # apenas chaves
print(pessoas.items()) # printa tudo

# Usando for
for k in pessoas.keys():
    print(k) # vai mostrar apenas as chaves
for k in pessoas.values():
    print(k)
for k, v in pessoas.items(): # k dmostar as chave e o v vai mostar os valores.
    print(f"{k} = {v}")

print("\n\ndel apaga chaves")
del pessoas["sexo"] # ele vai apagar essa chave
for k, v in pessoas.items(): 
    print(f"{k} = {v}")

print("\n\nsubstituir elementos")
pessoas["nome"]="Paulo"
for k, v in pessoas.items(): 
    print(f"{k} = {v}")

print("\n\nadicionar elementos")
pessoas["peso"]=98.5
for k, v in pessoas.items(): 
    print(f"{k} = {v}")

#Criar dicionário dentro de uma lista
print("\n\nDicionário dentro de uma lista\n")
brasil = []
estado={"uf":"Rio de Janeiro","sigla":"SP"}
estado1={"uf":"São Paulo","sigla":"SP"}
brasil.append(estado)
brasil.append(estado1)

print(brasil)
print(brasil[0]) # é a primeiro dicionário adicionado
print(brasil[1])# segundo """"
print(brasil[0]["uf"])# 0 - primeiro dicionário, uf - a chave do primeiro dicionário
print(brasil[1]["sigla"]) # 1 - posição na lista, # sigla - chave do dicionário

# Como copiar um dicionário para lista
# outra explicação do Guanabara
print("\n\n-------------------------.copy()-----------------------------------\n")
estado3= dict()
brasil = list()
for c in range(0,3):
    estado3["uf"] = str(input("Unidade Federativa: "))
    estado3["sigla"] = str(input("Sigla: "))
    brasil.append(estado3.copy()) # para copiar um dicionário para lista, só tem apenas um jeito que é .copy()
print(brasil)
# para cada estado na lista brasil eu mostro
for e in brasil: # o "e" é da lista, vai mostrar a lista
    print(e)

for e in brasil:
    for k, v in e.items(): # k é de chave do dicionário e v de valor do dicionário. # e.items() é a lista
       print(f"O campo {k} tem o valor {v}.") 
"""
Retorna isso:

O campo uf tem o valor são.
O campo sigla tem o valor sp.
O campo uf tem o valor rio.
O campo sigla tem o valor rj.
O campo uf tem o valor minas.
O campo sigla tem o valor mg.
"""
# posso mostar apenas os valores
print()
for e in brasil:    
    for v in e.values(): # apenas os valores do dicionário
        print(v, end=" ")
    print() # para cada for ele pular uma linha
