"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. """

lista = []
num = None
for n in range(1, 6):
    num = int(input(f"Digite um número inteiro {n}/5: "))
    lista.append(num)
print(*lista, sep=',')


