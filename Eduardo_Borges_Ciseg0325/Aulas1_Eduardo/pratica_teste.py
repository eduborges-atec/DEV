def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Ver números")
        print("2 - Sair do Programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_numeros()
        elif opcao == "2":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

def ver_numeros():
    numeros = []
    count = 0
    while len(numeros) < 100:
        try:
            valor = int(input(f"Digite o {len(numeros)+1}º número (entre 1 e 1000): "))
            if 1 <= valor <= 1000:
                numeros.append(valor)
                analisar_numero(valor)
                count += 1
                if count % 10 == 0:
                    opcao = input("Deseja continuar a inserir? (s para sim / qualquer tecla para voltar ao menu): ").lower()
                    if opcao != 's':
                        break
            else:
                print("Número fora do intervalo permitido.")
        except ValueError:
            print("Entrada inválida. Introduza um número inteiro.")

def analisar_numero(n):
    divisores = [i for i in range(1, n+1) if n % i == 0]
    print(f"\nAnálise do número: {n}")
    print("Par" if n % 2 == 0 else "Ímpar")
    print("Primo" if len(divisores) == 2 else "Não é primo")
    print(f"Número de divisores: {len(divisores)} -> {divisores}")
    print("Número perfeito" if sum(divisores[:-1]) == n else "Não é número perfeito")

menu_principal()