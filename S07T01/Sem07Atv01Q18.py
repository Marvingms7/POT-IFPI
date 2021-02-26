"""LISTA02_Q18 Ler uma lista X de 10 elementos.
A seguir copiar todos os valores negativos da lista X para uma lista R,
sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R."""
from random import randint
X = []
R = []
def copiar():
    for n in range(0, 10):
        elementos = randint(-20, 20)
        X.append(elementos)
    print(f"{X} - LISTA ORIGINAL")
    print()
    for v in X:
        if v < 0:
            R.append(v)
    print(f"{R} - LISTA SOMENTE DOS NEGATIVOS COPIADOS")
    for i in R:
        if v in X:
            X.pop(X.index(i))
    print(f"\n{X} - LISTA APÓS A EXCLUSÃO DOS NEGATIVOS")
copiar()