# Exercicio 12
# Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, 
# divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas.

numero = int(input("Introduza um número: "))

contador = 0

for i in range(1, numero):
    soma = numero + i
    print(f"{numero} + {i} = {soma}")
    contador += 1
    
    subtracao = numero - i
    print(f"{numero} - {i} = {subtracao}")
    contador += 1
    
    multiplicacao = numero * i
    print(f"{numero} * {i} = {multiplicacao}")
    contador += 1
    
    if i != 0:
        divisao = numero / i
        print(f"{numero} / {i} = {divisao:.2f}")
        contador += 1

print(f"\nTotal de operações realizadas: {contador}")
