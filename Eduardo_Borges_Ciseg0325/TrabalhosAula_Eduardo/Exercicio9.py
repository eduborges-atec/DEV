# Exercicio 9
# Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. 
#(Use o ciclo do ... while) 

# Simula um ciclo do...while para garantir que o número está entre 1 e 100

while True:
    numero = int(input("Introduz  um número entre 1 e 100: "))
    
    if 1 <= numero <= 100:
        print(f"Número válido: {numero}")
        break
    else:
        print("Valor inválido. Tenta novamente.")
