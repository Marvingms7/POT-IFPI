lista = []
cont = 0
while cont < 10:
    cont += 1
    num = int(input(f'Digite 10 numeros para ser adicionado na lista: '))
    if num not in lista:
        lista.append(num)
        print(f'Numero adicionado com sucesso!')
    else:
        print(f'Numero não adicionado, pois ja possui na lista!')




