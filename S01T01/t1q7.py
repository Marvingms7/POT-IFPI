def fatorial(a):
    total = 1
    for i in range(1, a+1):
        total *= i
    return total

def main():
    num = int(input("Digite um numero para ser calculado seu fatorial: "))
    resultado = fatorial(num)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
