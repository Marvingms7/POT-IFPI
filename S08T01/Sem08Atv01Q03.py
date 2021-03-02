'''Lista3_q03 Faça uma função que recebe por parâmetro um valor inteiro e
positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.'''
def primo(num):
    e_primo = "verdadeiro"
    if (num % 2) == 0:
        e_primo = "falso"

    return f"O valor é {e_primo}"

while True:
    try:
        numero = int(input("Digite um valor: "))
        if numero < 0:
            print("Valor digitado negativo. Digite novamente um valor positivo!")
        else:
            print(primo(numero))
            break
    except:
        print("Valor digitado negativo. Digite novamente um valor positivo!")