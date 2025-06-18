def maior(*bigger):
    #>>>>>> gracinha, o famoso "fru fru" >>>>>>
    from time import sleep
    print("_-"*30)
    print("Analisando os valores passados", end="")

    # para ficar aparencendo um ponto de cada vez
    for c in range(0,4):
        print(".",end="",flush=True)
        sleep(1)
    print()

    # para aparecer um número de cada vez
    for v in bigger:
        print(f"{v} ", end="",flush=True)
        sleep(0.5)
    print(f"    Foram informados {len(bigger)} valores ao todo.")


    # programa para verificar o maior número
    big = count = 0 
    for n in bigger:
        if count == 0:
            big = n
        else:
            if n > big:
                big = n
        count += 1     


    print(f"O maior valor informado foi {big}")
    print("_-"*30)

maior(1,2,3,4,5,6,9,7)

