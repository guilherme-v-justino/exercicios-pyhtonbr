"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. """

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

print(f'O resultado do produto do dobro do primeiro com metade do segundo é: {(num1 * 2) * (num2 / 2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(3 * num1) + num3}')
print(f'O terceiro número elevado ao cubo é: {num3 ** 3:.2f}')
