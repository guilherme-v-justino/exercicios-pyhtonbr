"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
 sabendo que a decisão é sempre pelo mais barato. """

produto = 0
mais_barato = 999
lista = [0]
for n in range(1, 4):
    produto = float(input(f"Digite o valor do produto {n}/3: "))
    if mais_barato > produto:
        mais_barato = produto
        lista.append(mais_barato)

print(f'Sua decisão deve ser pelo produto número {lista.index(mais_barato)} por ser o mais '
      f'barato com o valor de R${mais_barato:.2f}')







