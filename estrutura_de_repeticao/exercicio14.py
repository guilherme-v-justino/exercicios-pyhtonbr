"""Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares. """

pares = 0
impares = 0

for n in range(1, 11):
    num = int(input(f'Digite um número {n}/10: '))
    if num % 2 == 0:
        pares = pares + 1
    if num % 2 != 0:
        impares = impares + 1

print(f'A quantidade de números pares é: {pares}')
print(f'A quantidade de números ímpares é: {impares}')



