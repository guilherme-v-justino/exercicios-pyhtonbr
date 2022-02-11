"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; """

lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))
if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    print("Podemos formar um triângulo com estes números!")
    if lado1 == lado2 and lado2 == lado3:
        print("Estes números formariam um triângulo EQUILÁTERO")
    if lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado3 != lado2 and lado2 == lado3 and lado3 != lado1:
        print("Estes números formariam um triângulo ISÓSCELES")
    if lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        print("Estes números formariam um triângulo ESCALENO")
else:
    print("Não se pode construir um triângulo com estes números!")




