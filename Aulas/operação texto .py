Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> nome = "Gabriel"
>>> nome
'Gabriel'
>>> #string - sequência de caractere
>>> nome [1]
'a'
>>> nome [0] # 0 é o índice
'G'
>>> nome[1:3]
'ab'
>>> nome[2:4] # intervalo 2 ao 4
'br'
>>> #esse intervalo é chamado de slice que é ":"
>>> nome[1:]#intervalo vazio, apenas temos que escrever o começo
'abriel'
>>> #concatenação
>>> nome + "Borges"
'GabrielBorges'
nome + " Borges"
'Gabriel Borges'
len(nome)
7
#como fazer slice, separar e cortar
slice1 = nome[0:2]
slice1
'Ga'
slice2=nome[len(slice1):len(slice1)+2]# len de slice1 é 0 e 1
slice2
'br'
slice3=nome[-3:]
slice3
'iel'
slice1+slice2+slice3
'Gabriel'
#Na versão 3 python sempre que divide um inteiro por outro o resultado é um número decimsl.
(4+8)/2
6.0
