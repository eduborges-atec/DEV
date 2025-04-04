# Exercicio 13
# Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10) 

numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
