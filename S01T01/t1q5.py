def peso(a, b):
    total = 0
    if b == '1':
        total = (62.1 * a) - 44.7
    if b == '2':
        total = (72.7 * a) - 58
    return total

altura = float(input("Digite sua altura: "))
sexo = input("Digite o seu sexo, [1] para feminino e [2] masculino: ")
resultado = peso(altura, sexo)
print(f'{resultado:.2f}')
