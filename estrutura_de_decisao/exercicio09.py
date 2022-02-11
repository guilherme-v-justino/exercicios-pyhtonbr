"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
lista = []
for n in range(1, 4):
    num = int(input(f"Digite um número ({n}/3) :"))
    lista.append(num)
    lista.sort(reverse=True)
print('Em ordem numérica decrescente: ')
print(*lista, sep=',')
