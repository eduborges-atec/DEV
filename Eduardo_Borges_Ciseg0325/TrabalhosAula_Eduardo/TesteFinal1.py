# Teste Final 1

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_divisores(numero):
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    return divisores

def eh_perfeito(numero):
    soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return soma_divisores == numero

def tabuada(numero):
    for i in range(1, numero + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        if i % 20 == 0:
            continuar = input("\nDeseja continuar a ver a tabuada? (s para continuar, qualquer outra tecla para sair): ")
            if continuar.lower() != 's':
                break

def calculadora():
    while True:
        print("\n--- Calculadora ---")
        num1 = float(input("Introduza o primeiro número: "))
        operador = input("Introduza o operador (+, -, *, /): ")
        num2 = float(input("Introduza o segundo número: "))
        
        if operador == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operador == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operador == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operador == "/":
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Erro: Divisão por zero.")
        else:
            print("Operador inválido.")
        
        continuar = input("\nDeseja realizar outra operação? (s para continuar, qualquer outra tecla para sair): ")
        if continuar.lower() != 's':
            break

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Verificar números primos, divisores e perfeitos")
        print("2. Calculadora simples (+, -, *, /)")
        print("3. Tabuada")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            limite = int(input("Introduza um número entre 1 e 30000: "))
            if 1 <= limite <= 30000:
                for numero in range(1, limite + 1):
                    print(f"\nNúmero: {numero}")
                    if eh_primo(numero):
                        print(f"{numero} é um número primo.")
                    else:
                        print(f"{numero} não é um número primo.")
                    
                    divisores = contar_divisores(numero)
                    print(f"Quantidade de divisores: {divisores}")
                    
                    if eh_perfeito(numero):
                        print(f"{numero} é um número perfeito.")
                    else:
                        print(f"{numero} não é um número perfeito.")
                    
                    if numero % 10 == 0:
                        continuar = input("\nDeseja continuar verificando mais números? (s para continuar, qualquer outra tecla para sair): ")
                        if continuar.lower() != 's':
                            break
            else:
                print("Valor fora do intervalo. Por favor, introduza um número entre 1 e 30000.")

        elif opcao == '2':
            calculadora()

        elif opcao == '3':
            numero = int(input("Introduza um número para ver a tabuada (entre 1 e 1000): "))
            if 1 <= numero <= 1000:
                tabuada(numero)
            else:
                print("Número fora do intervalo. Por favor, introduza um número entre 1 e 1000.")

        elif opcao == '4':
            print("A sair do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
