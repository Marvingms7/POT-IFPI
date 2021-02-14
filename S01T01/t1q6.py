'''6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''

def medidor(a, b):
    perimetro = area = 0
    if a == 3:
        perimetro = b + b + b
        print(f'TRIÂNGULO {perimetro} cm de perímetro')
    if a == 4:
        area = b ** 2
        print(f'QUADRADO {area} cm de área')
    if a == 5:
        print(f'PENTÁGONO')
def main():
    lados = int(input("Digite a quantidade de lados do seu poligono regular: "))
    medida = float(input("Digite a medida do lado em cm: "))
    medidor(lados, medida)


if __name__ == '__main__':
    main()
