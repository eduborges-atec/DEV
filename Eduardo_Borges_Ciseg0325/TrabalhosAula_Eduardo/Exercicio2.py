# Exercicio 2
# Ler 10 números, e determinar se o número par e número impar.

for i in range(10):
    numero = int(input(f"Introduza o {i+1}º número: "))
    
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
