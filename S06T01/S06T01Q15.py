'''15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''
from random import randint
max_lista = 10
D = list(range(max_lista))
E = []
def gravar_lista(a):
    for i in range(max_lista):
        a[i] = randint(1,100)
    return a

def inverter(a, b):
    cont = -1
    for i in a:
        E.insert(cont,i)
        cont -= 1
    return E

resultado1 = gravar_lista(D)
resultado2 = inverter(D, E)
print(f'Lista D: {resultado1}')
print(f'Lista E: {resultado2}')

