"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação"""

populacao_a = int(input("Digite a população do país A: "))
while populacao_a <= 0:
    print("Número inválido!")
    populacao_a = int(input("Digite a população do país A: "))

populacao_b = int(input("Digite a população do país B: "))
while populacao_b <= 0:
    print("Número inválido!")
    populacao_b = int(input("Digite a população do país B: "))
while populacao_b <= populacao_a:
    print("Para este programa, a população do país B deve ser maior que a população do país A")
    populacao_b = int(input("Digite a população do país B: "))

taxa_crescimento_a = float(input("Digite a taxa de crescimento do país A em %: "))
while taxa_crescimento_a <= 0:
    print("Taxa de crescimento inválida!")
    taxa_crescimento_a = float(input("Digite a taxa de crescimento do país A em %: "))

taxa_crescimento_b = float(input("Digite a taxa de crescimento do país B em %: "))
while taxa_crescimento_a <= 0:
    print("Taxa de crescimento inválida!")
    taxa_crescimento_b = float(input("Digite a taxa de crescimento do país B em %: "))
while taxa_crescimento_a <= taxa_crescimento_b:
    print("Taxa de crescimento inválida! Neste programa, a taxa de crescimento do país A deve ser maior "
          "que a taxa de crescimento do país B")
    taxa_crescimento_b = float(input("Digite a taxa de crescimento do país B em %: "))

anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a * ((taxa_crescimento_a / 100) + 1)
    populacao_b = populacao_b * ((taxa_crescimento_b / 100) + 1)
    anos = anos + 1

print(f'Serão necessários {anos} anos para a população do país A igualar ou ultrapassar a população do país B')