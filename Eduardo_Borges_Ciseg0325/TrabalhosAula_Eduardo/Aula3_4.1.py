# Exercício 4.1
# Esta versão serve para a pessoa que está a receber o cheque
saldo_deposito = float(input("Introduza o saldo da sua conta: "))

cheque = float(input("Introduza o valor do cheque: "))

saldo_deposito += cheque

print(f"Cheque depositado com sucesso!")
print(f"Saldo Atualizado! Novo saldo: {saldo_deposito:.2f}€")
