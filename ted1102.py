import random

A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

soma_A = sum(sum(linha) for linha in A)

print("Matriz A:")
for linha in A:
    print(linha)
print(f"\nSoma de todos os valores da matriz A: {soma_A}")

B = [[elemento * 3 for elemento in linha] for linha in A]

print("\nMatriz B (cada elemento da matriz A multiplicado por 3):")
for linha in B:
    print(linha)