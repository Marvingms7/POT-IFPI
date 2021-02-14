
def soma(a, b):
    total = 0
    for i in range(a, b):
        total += i
    return total
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
som = n1 + n2
resultado = soma(n1, n2)
inter = resultado - som
print(f'{inter}')
