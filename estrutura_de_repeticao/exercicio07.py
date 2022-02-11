"""Faça um programa que leia 5 números e informe o maior número. """

lista = []
for n in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)
print(f'O maior número é {max(lista)}')
