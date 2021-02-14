"""Escreva uma função que recebe por parâmetro um valor inteiro e positivo X
e retorna o valor de S.
S = 1 + 1/1! + 1/2! + 1/3! + 1/x! """

def fatorial(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    return f



def soma(x):
    s = 1
    for d in range(1, x+1):
        s = s + 1 / fatorial(d)
    return s

def main():
    while True:
        try:
            x = int(input("Digite um número inteiro e positivo: "))
            resultado = soma(x)
            if x >= 0:
                print(f'A soma é {resultado}')
                break
            else:
                print("Número negativo!")
        except:
            print("Número inválido!")

if __name__ == '__main__':
    main()