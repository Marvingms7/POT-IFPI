max_lista = 15
lista1 = list(range(max_lista))
maior = menor = 0
for i in range(0, max_lista):
    lista1[i] = (int(input(f'Digite um numero para ficar na posição {i+1}: ')))
    if i == 0:
        maior = menor = lista1[i]
    else:
        if lista1[i] > maior:
            maior = lista1[i]
        if lista1[i] < menor:
            menor = lista1[i]
print(f'Voce digitou {lista1}')
print(f'O maior valor digitado foi {maior} na posição:', end='')
for i, v in enumerate(lista1):
    if v == maior:
        print(f'{i+1}', end='...')
print(f'\nO menor valor digitado foi {menor} na posição:', end='')
for i, v in enumerate(lista1):
    if v == menor:
        print(f'{i+1}', end='...')








