# Exercicio 10
# Elabore um programa que lê um número e escreve quantos divisores ele possui.
# Lê o número do utilizador

numero = int(input("Introduz um número inteiro: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

print(f"O número {numero} possui {divisores} divisores.")
