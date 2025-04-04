# Exercicio 6

nome = input("introduza o seu nome: ")
valor_compra = float(input("Introduza o valor da compra (€):"))

if valor_compra <= 200:
    desconto = 10
elif valor_compra <= 500:
    desconto = 15
else:
    desconto = 20

desconto_valor = (desconto / 100) * valor_compra
total = valor_compra - desconto

print("\n=== Resumo da sua compra ===")
print(f"Nome do Cliente: {nome}")
print(f"Valor da sua compra: {valor_compra:.2f}€")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor do desconto: {desconto_valor:.2f}€")
print(f"Total a pagar: {total:.2f}€")