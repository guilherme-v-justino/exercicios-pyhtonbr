"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = []
for n in range(1, 6):
    num = int(input(f'Digite um número {n}/5: '))
    lista.append(num)
print(f'A soma dos valores indicados é: {sum(lista)}')
print(f'A média dos valores indicados é: {sum(lista) / 5}')
