# Exercicio 17
# Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência

for numero in range(1, 1001):
    if numero % 5 == 0 and numero % 3 != 0:
        print(numero)
