"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. """

lista = []
num = 0
for n in range(1, 11):
    num = float(input(f'Digite um número real {n}/10: '))
    lista.append(num)
lista.reverse()
print(*lista, sep=', ')


