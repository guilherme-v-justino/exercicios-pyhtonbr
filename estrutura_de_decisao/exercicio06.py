"""Faça um Programa que leia três números e mostre o maior deles."""
num = 0
maior = -999
for n in range(0, 3):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
print(f'O maior número é {maior}')


