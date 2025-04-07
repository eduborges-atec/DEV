# Teste Final 2

# Lista de clientes

clientes = []

def calcular_desconto(compra):
    if 100 <= compra <= 200:
        return 0.05 * compra
    elif 200 < compra < 500:
        return 0.10 * compra
    elif compra >= 500:
        return 0.15 * compra
    return 0

def inserir_cliente():
    numcli = len(clientes) + 1
    nomcli = input("Nome do cliente: ")
    morada = input("Morada: ")
    tel = input("Telefone: ")
    nif = input("NIF: ")
    
    while True:
        try:
            compra = float(input("Valor da compra: "))
            if compra <= 0:
                print("Valor inválido. A compra deve ser um valor positivo.")
            else:
                break
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido para a compra.")
    
    desconto = calcular_desconto(compra)
    divfin = compra - desconto

    cliente = {
        "numcli": numcli,
        "nomcli": nomcli,
        "morada": morada,
        "tel": tel,
        "nif": nif,
        "compra": compra,
        "divfin": divfin
    }
    
    clientes.append(cliente)
    print(f"Cliente {nomcli} inserido com sucesso!\n")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return

    for cliente in clientes:
        print(f"\nCliente #{cliente['numcli']}:")
        print(f"Nome: {cliente['nomcli']}")
        print(f"Morada: {cliente['morada']}")
        print(f"Telefone: {cliente['tel']}")
        print(f"NIF: {cliente['nif']}")
        print(f"Compra: {cliente['compra']:.2f}")
        print(f"Desconto: {cliente['compra'] - cliente['divfin']:.2f}")
        print(f"Divida Final (com desconto): {cliente['divfin']:.2f}")
        continuar = input("\nPressione qualquer tecla para continuar para o próximo cliente ou 'q' para sair: ")
        if continuar.lower() == 'q':
            break

def buscar_cliente():
    while True:
        try:
            numcli = int(input("Digite o número do cliente para busca: "))
            if 1 <= numcli <= len(clientes):
                cliente = clientes[numcli - 1]
                print(f"\nCliente #{cliente['numcli']}:")
                print(f"Nome: {cliente['nomcli']}")
                print(f"Morada: {cliente['morada']}")
                print(f"Telefone: {cliente['tel']}")
                print(f"NIF: {cliente['nif']}")
                print(f"Compra: {cliente['compra']:.2f}")
                print(f"Desconto: {cliente['compra'] - cliente['divfin']:.2f}")
                print(f"Divida Final (com desconto): {cliente['divfin']:.2f}")
                break
            else:
                print("Número de cliente inválido. Tente novamente.")
        except ValueError:
            print("Número de cliente inválido. Por favor, insira um número válido.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Inserir novo cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente por número")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()