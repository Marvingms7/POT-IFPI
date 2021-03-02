'''Lista3_q02 Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra.
Se a letra for A o procedimento calcula a média aritmética das notas do aluno,
se for P, a sua média ponderada (pesos: 5, 3 e 2).
A função deve retornar a média calculada.'''
def media(n1, n2, n3, letra):
    if letra == 'A':
       média = (n1+n2+n3)/3
    elif letra == 'P':
        média = (n1*5 + n2*3 + n3*2)/5+3+2
    return f"A média é: {média:.2f}"
while True:
    try:
        nota1 = float(input("Digite a {1}º nota do aluno: "))
        nota2 = float(input("Digite a {2}º nota do aluno: "))
        nota3 = float(input("Digite a {3}º nota do aluno: "))
        letras = input("\n[A] - Média Aritmética\n[P] - Média Ponderada\nDigita uma letra para saber a média desejada: ").upper()
        while letras != 'A' and letras != 'P':
            letras = input("\n[A] - Média Aritmética\n[P] - Média Ponderada\nDigita uma letra para saber a média desejada: ").upper()
        else:
            print(media(nota1, nota2, nota3, letras))
            break
    except:
        print("Valor inválido. Digite novamente!")