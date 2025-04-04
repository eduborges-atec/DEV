# Exercicio 7

nota1 = float(input("Introduz a nota do primeiro teste: "))
nota2 = float(input("Introduz a nota do segundo teste: "))
nota3 = float(input("Introduz a nota do terceiro teste: "))

teste1 = 2
teste2 = 3
teste3 = 5

media_final = (nota1 * teste1 + nota2 * teste2 + nota3 * teste3) / (teste1 + teste2 + teste3)

print(f"Média final: {media_final:.2f}")

if media_final >= 6:
    print("Foi aprovado. Muitos Parabéns!")
else:
    print("Está reprovado. Estuda mais cangalho...")