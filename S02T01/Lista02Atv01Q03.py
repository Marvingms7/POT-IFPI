def inverter_lista(a):
    lista1 = []
    for i in range(1, a+1):
        num = int(input("Digite um numero: "))
        lista1.insert(-i, num )
    return lista1
def main():
    n = int(input("Digite a quantidade de numeros que deseja imprimir: "))
    resultado = inverter_lista(n)
    print(f'Você digitou {n} numeros e a ordem deles invertida é {resultado}')

if __name__ == '__main__':
    main()