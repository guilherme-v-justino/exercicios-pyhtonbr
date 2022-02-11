"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que
os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
    quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00"""

valor_hora = int(input("Qual o valor da hora trabalhada? :"))
qtd_horas = int(input("Quantas horas você trabalhou neste mês? :"))

salario_bruto = valor_hora * qtd_horas
sindicato = 0.03 * salario_bruto
inss = 0.1 * salario_bruto
fgts = 0.11 * salario_bruto
ir = 0
desconto_ir = 0
if salario_bruto <= 900:
    ir = 0
    desconto_ir = salario_bruto * ir
if 900 < salario_bruto <= 1500:
    ir = 0.05
    desconto_ir = salario_bruto * ir
if 1500 < salario_bruto <= 2500:
    ir = 0.1
    desconto_ir = salario_bruto * ir
if salario_bruto > 2500:
    ir = 0.2
    desconto_ir = salario_bruto * ir
total_descontos = sindicato + inss + desconto_ir
salario_liquido = salario_bruto - total_descontos

print('########## Tabela de Salário e Descontos ##########')
print(f'(+) Salário bruto:     R${salario_bruto:.2f}')
print(f'(-) IR ({ir * 100}%):         R${desconto_ir:.2f}')
print(f'(-) INSS (10%):        R${inss}')
print(f'(-) Sindicato (3%):    R${sindicato}')
print(f'FGTS (11%):            R${fgts}')
print(f'Total de Descontos:    R${total_descontos}')
print(f'Salário Líquido:       R${salario_liquido}')




