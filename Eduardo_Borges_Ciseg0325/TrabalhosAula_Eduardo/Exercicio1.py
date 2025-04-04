# Exercicio 1 
# Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

pares = []
impares = []

numero = 1

while len(pares) < 30 or len(impares) < 30:
    if numero % 2 == 0:
        if len(pares) < 30:
            pares.append(numero)
    else:
        if len(impares) < 30:
            impares.append(numero)
    numero += 1
    
print("30 primeiros números pares:")
print(pares)

print("\n30 primeiros números ímpares:")
print(impares)
