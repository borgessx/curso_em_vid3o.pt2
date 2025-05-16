ficha = list()
while True:
    nome=str(input("Nome Aluno: "))
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input("Quer continuar? [s/n]"))
    if resp in "Nn":
        break

print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') 
# :<4 alinha a esquerda 4, :>8 alinhada a direita 8
print("-"*30)
for i,a in enumerate(ficha): # i é a contagem dos números, e A é as info dentro da lista
    print(f"{i+1:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*30)
    mostrar=int(input("Mostrar nota de qual aluno (não,digite 0)? No."))
    if mostrar ==0:
        print("FINALIZADO...")
        break
    if mostrar > 0:
        mostrar+=1
        print(f"Aluno {ficha[mostrar][0]}, Notas {ficha[mostrar][0]}")
print(a)
print(i)