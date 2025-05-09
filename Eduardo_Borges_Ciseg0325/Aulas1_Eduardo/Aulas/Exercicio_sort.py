def nome_valido(nome):
    if not nome:
        return False
    partes = nome.split()
    for parte in partes:
        if not parte[0].isupper():
            return False
        if not all(c.islower() or not c.isalpha() for c in parte[1:]):
            return False
    return True


def obter_input_nome():
    while True:
        nome_completo = input("Introduza o nome completo (Primeiro e Último): ").strip()
        if nome_valido(nome_completo):
            return nome_completo
        else:
            print("Nome inválido. Use letras, com a primeira maiúscula e restantes minúsculas. Ex: João Silva")


def obter_input_idade():
    while True:
        try:
            idade = int(input("Introduza a idade: "))
            if idade > 0:
                return idade
            else:
                print("Idade deve ser positiva.")
        except ValueError:
            print("Idade inválida. Introduza um número inteiro.")


def ordenar_por_ascii(lista, por="primeiro"):
    def chave_ascii(item):
        nome = item[0].split()
        alvo = nome[0] if por == "primeiro" else nome[-1]
        return [ord(c) for c in alvo]

    return sorted(lista, key=chave_ascii)


def remover_nome(lista, por="primeiro"):
    alvo = input(f"Introduza o nome {'primeiro' if por == 'primeiro' else 'último'} a remover: ").strip()
    nova_lista = []
    encontrado = False
    for nome, idade in lista:
        nome_split = nome.split()
        if (por == "primeiro" and nome_split[0] == alvo) or (por == "último" and nome_split[-1] == alvo):
            print(f"{nome} removido com sucesso.")
            encontrado = True
        else:
            nova_lista.append((nome, idade))
    if not encontrado:
        print("Nome não encontrado.")
    return nova_lista


def menu():
    lista = []
    while True:
        print("\nMenu:")
        print("1. Adicionar nome")
        print("2. Listar por primeiro nome")
        print("3. Listar por último nome")
        print("4. Remover por primeiro nome")
        print("5. Remover por último nome")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = obter_input_nome()
            idade = obter_input_idade()
            lista.append((nome, idade))
        elif escolha == "2":
            print("\nOrdenado por Primeiro Nome:")
            for nome, idade in ordenar_por_ascii(lista, por="primeiro"):
                print(f"{nome}, {idade} anos")
        elif escolha == "3":
            print("\nOrdenado por Último Nome:")
            for nome, idade in ordenar_por_ascii(lista, por="último"):
                print(f"{nome}, {idade} anos")
        elif escolha == "4":
            lista = remover_nome(lista, por="primeiro")
        elif escolha == "5":
            lista = remover_nome(lista, por="último")
        elif escolha == "6":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida.")

menu()
