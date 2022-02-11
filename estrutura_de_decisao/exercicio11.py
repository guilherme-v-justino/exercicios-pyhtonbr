"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%

    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento."""

salario_atual = float(input("Qual o seu salário atual? : "))
salario_reajuste = 0
reajuste = 0
valor_aumento = salario_reajuste - salario_atual

if salario_atual < 280:
    reajuste = 0.2
    salario_reajuste = salario_atual + (salario_atual * reajuste)
if 280 <= salario_atual < 700:
    reajuste = 0.15
    salario_reajuste = salario_atual + (salario_atual * reajuste)
if 700 <= salario_atual < 1500:
    reajuste = 0.1
    salario_reajuste = salario_atual + (salario_atual * reajuste)
if salario_atual >= 1500:
    reajuste = 0.05
    salario_reajuste = salario_atual + (salario_atual * reajuste)

print("########## Atualização de Salário #########")
print(f'Seu salário atual é de R${salario_atual:.2f}')
print(f'O percentual de aumento foi de {reajuste * 100:.0f}%')
print(f'O valor do reajuste foi de R${valor_aumento:.2f}')
print(f'Seu novo salário é de R${salario_reajuste:.2f}')


