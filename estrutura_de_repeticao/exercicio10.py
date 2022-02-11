"""Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido por eles. """

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

for n in range(num1, num2 + 1):
    print(n)
