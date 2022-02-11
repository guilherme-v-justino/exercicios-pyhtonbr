"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)."""

graus_f = float(input("Digite a temperatura em Fahrenheit: "))
graus_c = 5 * ((graus_f - 32) / 9)

print(f'A temperatura indicada transformada em Celsius é: {graus_c:.1f}')

