"""Altere o programa anterior para mostrar no final a soma dos números."""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

for n in range(num1, num2 + 1):
    print(n)
print(f'A soma dos números mostrados é: {sum(range(num1, num2 + 1))}')





