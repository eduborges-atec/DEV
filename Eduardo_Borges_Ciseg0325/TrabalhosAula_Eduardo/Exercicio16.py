# Exercicio 16
# Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. 
# Validando a entrada de números inteiros entre 1 e 50.

def obter_numero_par():
    while True:
        try:
            numero = int(input("Introduz um número par entre 1 e 50: "))
            if 1 <= numero <= 50 and numero % 2 == 0:
                return numero
            else:
                print("Número inválido. O número deve ser par e entre 1 e 50.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

soma = 0
contador = 0

while contador < 30:
    numero = obter_numero_par()
    soma += numero
    contador += 1

media = soma / 30

print(f"\nA média dos 30 números pares é: {media:.2f}")
