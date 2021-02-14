def maior(a, b):
    maior = 0
    if a > b:
        maior = a
    elif a == b:
        maior = a
    else:
        maior = b
    return maior

def main():
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    resultado = maior(n1, n2)
    print(f'o maior numero é {resultado}')

if __name__ == '__main__':
    main()