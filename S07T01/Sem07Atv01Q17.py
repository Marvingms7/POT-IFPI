"""LISTA02_Q17 Ler uma lista W de 10 elementos, depois ler um valor V.
Contar e escrever quantas vezes o valor V ocorre na lista W
e escrever também em que posições (índices) da lista W o valor V aparece."""
from random import randint
W = []
def valor(v):
    c = 0
    p = []
    for n in range(0, 10):
        elementos = randint(1, 10)
        W.append(elementos)
        if v == W[n]:
            c = W.count(v)
            p.append(n)
    if v not in W:
        print("\nO número informado não consta na lista")
    else:
        print(f"\nO número: {v}\nQuantidade: {c}\nPosição(ões): {p}")

V = int(input("Digite um valor para saber se está na lista de [1-10]: "))
valor(V)
print(f"\n{W}")