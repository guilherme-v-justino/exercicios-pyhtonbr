"""Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 """

altura = float(input("Digite sua altura: "))
sexo = input("Você é homem (h) ou mulher (m)? : ")
if sexo.lower() == 'h':
    print(f'Seu peso ideal é: {(72.7 * altura) - 58:.1f}kg')
if sexo.lower() == 'm':
    print(f'Seu peso ideal é: {(62.1 * altura) - 44.7:.1f}kg')
if sexo != 'h' and sexo != 'm':
    print("Sexo não identificado")







