"""LISTA02_Q09 Dada uma lista X numérica contendo 5 elementos,
fazer um programa que crie e exiba na tela uma lista Y.
A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa."""
X = []
Y = []
def inverso(x, y):
    Y = y[::-1]
    print(f"{x}\n{Y}")

for c in range(0, 5):
    numero = int(input(f"Digite um numero: "))
    X.append(numero)
    Y.append(numero)
inverso(X, Y)