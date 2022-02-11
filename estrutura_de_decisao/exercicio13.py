"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

num = int(input("Digite um número de 1 a 7: "))
if 0 < num <= 7:
    if num == 1:
        print("1 - Domingo")
    if num == 2:
        print("2 - Segunda-feira")
    if num == 3:
        print("3 - Terça-feira")
    if num == 4:
        print("4 - Quarta-feira")
    if num == 5:
        print("5 - Quinta-feira")
    if num == 6:
        print("6 - Sexta-feira")
    if num == 7:
        print("7 -  Sábado")
else:
    print("Número Inválido")
