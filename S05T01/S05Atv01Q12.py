"""LISTA02_Q12 Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes.
A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas."""
gabprova = []
gabaluno = []
d = 0
print("GABARITO DA PROVA")
for c in range(0,30):
    d += 1
    resp = input(f"Resposta da questão {d}: ")
    gabprova.append(resp)
nome = input("\nNome do aluno: ")
d = 0
print("\nGABARITO DO ALUNO")
for c in range(0, 30):
    d += 1
    resposta = input(f"Resposta da questão {d}: ")
    gabaluno.append(resposta)

a = b = 0
for c in range(0, 30):
    if gabprova[c] == gabaluno[c]:
        a += 1
    else:
        b += 1
print(f"\nO aluno {nome} teve:\n{a} Acertos\n{b} Erros.")