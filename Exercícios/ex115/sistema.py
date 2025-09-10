from lib.interface import *
from time import sleep
from lib.arquivo import *

# nome do arquivo
arq = 'gabrielborges.txt'

# usar if para ver se ele existe
if arquivoExiste(arq):
    print('Arquivo Encontrado com sucesso!')
# se não existi criar um
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

# menu
while True:
    # lista das opções do menu
    resposta = menu(['Ler pessoas cadastradas','Cadsatrar nova pessoa','Sair do sistema'])

    # escolha de opção
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)


    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[0m')
    sleep(2)