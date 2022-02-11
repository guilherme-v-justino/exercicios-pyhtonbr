"""Faça um Programa que leia três números e mostre o maior e o menor deles. """
num = 0
maior = -999
menor = 999
for n in range(0, 3):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior número é {maior} e o menor número é {menor}')
