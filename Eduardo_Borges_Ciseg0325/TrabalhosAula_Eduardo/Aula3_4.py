# Exercício 4 
# Esta versão serve para a pessoa que está a dar o cheque ( Vou criar outro script para o que está a receber noutro ficheiro 4.1)
saldo = float(input("Introduza o saldo inicial: "))

cheque = float(input("Introduza o valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado com sucesso. Novo saldo: {saldo:.2f}€ ")
else:
    print("Saldo não é suficiente! Cheque não pode ser aceite")
