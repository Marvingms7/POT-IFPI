'''12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.'''

def somatorio(a):
    for i in range(1, a+1):
        a = a + i
    return a
def main():
    while True:
        try:
            n = int(input("Digite um número inteiro para saber seu somatorio: "))
            resultado  = somatorio(n)
            if n > 0:
                print(f'{resultado}')
            else:
                print(f'O número digitado é negativo!')
        except:
            print(f'O número digitado é invalido!')


if __name__ == '__main__':
    main()