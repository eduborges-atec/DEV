# Exercicio 4
# Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

numero = int(input("Introduz um número inteiro: "))

if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    primo = True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
