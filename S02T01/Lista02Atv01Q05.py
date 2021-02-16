listA = []
listB = []
listC = []
indice = 0
for i in range(1, 11):
    n = int(input("Digite um Numero para ser adicionado na lista A: "))
    listA.append(n)
for c in range(1, 11):
    n2 = int(input("Digite um numero para ser adicionado na lista B: "))
    listB.append(n2)
while indice < len(listA):
    listC.append(listA[indice])
    listC.append(listB[indice])
    indice += 1
print(f'ListaA:{listA}\nListaB:{listB}\nListaC{listC}')