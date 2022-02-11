"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela. """

lista = []
notas = 0
for n in range(1, 5):
    notas = float(input(f'Digite a {n}º nota: '))
    lista.append(notas)
print(f'Nota da prova 1 = {lista[0]}')
print(f'Nota da prova 2 = {lista[1]}')
print(f'Nota da prova 3 = {lista[2]}')
print(f'Nota da prova 4 = {lista[3]}')

media = sum(lista) / 4
print(f'A média das notas é igual a {media}')


