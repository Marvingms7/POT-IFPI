'''8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.'''
def sim_nao(a):
    if a == 'S':
        print(f'S')
    elif a == 'N':
        print(f'N')
    return a
def main():
    caractere = input("Digite o caractere 'S' ou 'N': ").strip()
    while True:
        resultado = sim_nao(caractere).strip()
        if resultado == 'S':
            numero = int(input("Digite um numero para saber o valor do mesmo ao cubo: "))
            numero = numero ** 3
            print(f'{numero}')
            c = input("Deseja continuar? ")
            if c == 'N':
                break

        elif resultado == 'N':
            break
        elif resultado != 'S' or resultado != 'N':
            print(f'Caractere invalido. Digite novamente!')


if __name__ == '__main__':
    main()

