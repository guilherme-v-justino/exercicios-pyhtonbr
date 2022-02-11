"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
    sempre arredonde os valores para cima, isto é, considere latas cheias"""
import math

print("########## Loja de Tintas ##########")

area = int(input("Digite a área em m2 a ser pintada ----> :"))

litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
valor_lata = latas * 80
galao = math.ceil(litros / 3.6)
valor_galao = galao * 25

mix_latas = round(litros / 18)
mix_galoes = round((litros - mix_latas * 18) / 3.6)

if litros - (mix_latas * 18) % 3.6 != 0:
    mix_galoes += 1
total_mix = (mix_latas * 80) + (mix_galoes * 25)
print(f'Se for comprar apenas latas, serão necessárias {latas} latas e custará R${valor_lata:.2f}.')
print(f'Se for comprar apenas galões, serão necessários {galao} galões e custará R${valor_galao:.2f}.')
print(f'Se deseja mesclar os produtos para melhor economia, irá precisar de {mix_latas} latas e '
      f'{mix_galoes} galões, totalizando R${total_mix}.')
