'''4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).'''

def media(a, b):
    med = (a + b) / 2
    return med

nota1 = float(input("Digite a nota da sua primeira avaliação: "))
nota2 = float(input("Digite a nota da sua segunda avaliação: "))
resultado = media(nota1, nota2)
if resultado >= 6:
    print(f'Sua média ficou {resultado}\nPARABÉNS! Você foi aprovado!')
else:
    print(f'Sua média ficou {resultado}\nInfelizmente você foi Reprovado!')