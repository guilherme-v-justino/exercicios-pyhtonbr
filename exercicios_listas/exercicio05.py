"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores"""

lista = []
par = []
impar = []

for n in range(1, 21):
    num = int(input(f'Digite um número {n}/20: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('\nOs números recebidos foram:')
print(*lista, sep=', ')
print('\nOs números pares são:')
print(*par, sep=', ')
print('\nOs números ímpares são:')
print(*impar, sep=', ')
