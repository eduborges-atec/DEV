# Exercicio 15
# Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. 
# Dispor de 20 em 20 com a condição de continuação ou saída do programa.


def exibir_ascii():
    i = 0
    while i <= 255:
        for j in range(i, i + 20):
            if j <= 255:
                print(f"Código ASCII: {j} -> Carácter: {chr(j)}")
        
        i += 20
        resposta = input("\nDeseja continuar? (s para continuar, qualquer outra tecla para sair): ")
        if resposta.lower() != 's':
            print("Programa terminado.")
            break

exibir_ascii()
