# Exercicio 18
# Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. 

def perfeito(numero):
    divisores = 0
    # Encontrar divisores próprios de "numero"
    for i in range(1, numero):
        if numero % i == 0:
            divisores += i
    return divisores == numero

limite = int(input("Digite um número até o qual verificar números perfeitos: "))

contador = 0
for num in range(1, limite + 1):
    if perfeito(num):
        print(f"{num} é um número perfeito.")
        contador += 1

print(f"\nExistem {contador} números perfeitos até {limite}.")
