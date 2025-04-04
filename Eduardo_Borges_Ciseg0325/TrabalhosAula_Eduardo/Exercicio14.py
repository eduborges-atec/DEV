# Exercicio 14  
# Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for). 

for numero in range(1, 101):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
