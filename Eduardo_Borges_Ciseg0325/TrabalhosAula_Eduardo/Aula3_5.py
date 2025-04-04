# Exercicio 5

num1 = int(input("Introduz o primeiro número: "))
num2 = int(input("Introduz o segundo número: "))
num3 = int(input("Introduz o terceiro número: "))

numeros =[num1, num2, num3]
numero_crescente = sorted(numeros)
numero_decrescente = sorted(numeros, reverse=True)

print(f"Ordem crescente: {numero_crescente[0]}, {numero_crescente[1]}, {numero_crescente[2]}")
print(f"Ordem decrescente: {numero_decrescente[0]}, {numero_decrescente[1]}, {numero_decrescente[2]}")