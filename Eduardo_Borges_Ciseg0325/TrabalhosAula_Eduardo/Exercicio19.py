# Exercicio 19
# Escreva um programa que mostre os primeiros 60 números da serie bonatchi.

def fibonacci(n):
    a, b = 1, 1
    
    fibonacci_sequence = [a, b]

    for i in range(2, n):
        a, b = b, a + b
        fibonacci_sequence.append(b)

    for i in range(n):
        if i == 0:
            print(f"{fibonacci_sequence[i]}")
        elif i == 1:
            print(f"    {fibonacci_sequence[i]}")
        else:
            print(f"        {fibonacci_sequence[i]}")

fibonacci(60)
