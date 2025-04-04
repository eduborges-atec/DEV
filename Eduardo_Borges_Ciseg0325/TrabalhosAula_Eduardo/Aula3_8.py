# Exercicio 8

notas = []

for i in range(10):
    nota = float(input(f"Introduza a nota do {i+1}º Aluno: "))

    while nota < 0 or nota > 20:
        print("A nota deve ser entre 0 e 20 !")
        nota = float(input(f"Introduza a nota do {i+1}º Aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

alunos_acima_da_media = sum(1 for nota in notas if nota >= media)

print(f"\nA média das notas dos Alunos é: {media:.2f}")
print(f"Quantidade de Alunos com a nota igual ou açima da média: {alunos_acima_da_media}")