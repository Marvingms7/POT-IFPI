listA = []
listB = []
listC = []
indice = 0
for i in range(1, 11):
    n = int(input(f'Digite a quantidade de cada produto: '))
    listA.append(n)
for c in range(1, 11):
    n2 = int(input(f'Digite o Preço de cada produto: '))
    listB.append(n2)
while indice < len(listA):
    listC.append(listA[indice] * listB[indice])
    indice += 1
print(f'Preço de cada item:')
for i, v in enumerate(listB):
    print(f'item {i+1}: {v}R$.')
print(f'A quantidade de cada produto:')
for i, v in enumerate(listA):
    print(f'Produto {i+1} quantidade x{v}')
print(f'Soma de cada item:')
for i, v in enumerate(listC):
    print(f'item {i+1} igual a {v}R$')
total = 0
cont = 0
for i, v in enumerate(listC):
    total += v
    cont += 1
media = total / cont
contador2 = 0
for i, v in enumerate(listC):
    if v < media:
        contador2 =+ 1
print(f'O Faturamento total é de {total}R$\nA média é de {media}R$\nA quantidade que está abaixo da média é de {contador2}')
