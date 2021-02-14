def divisor(a):
    contador = 0
    for i in range(1, a+1):
        if a % i == 0:
            contador += 1
    return contador

def main():
    num = int(input("Digite um numero para saber quantos divisores ele possui: "))
    resultado = divisor(num)
    print(f'O numero {num} possui {resultado} divisores')

if __name__ == '__main__':
    main()