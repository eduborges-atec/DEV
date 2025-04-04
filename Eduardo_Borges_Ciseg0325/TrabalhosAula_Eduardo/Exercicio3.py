# Exercicio 3
# Ler a nota de 10 alunos, calcular a media e mostrar essa média.

soma = 0

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota  # Soma as notas

media = soma / 10

print(f"\nA média das notas dos 10 alunos é: {media:.2f}")
