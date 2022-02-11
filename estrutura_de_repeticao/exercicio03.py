"""Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; """

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("O nome precisa ter mais que 3 caracteres!")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida! Idade deve estar entre 0 e 150 anos!")
    idade = input("Digite sua idade: ")

salario = float(input("Digite seu salário: "))
while salario < 0:
    print("Salário inválido!")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (f/m): ")
while sexo.lower() != 'f' and sexo.lower() != 'm':
    print("Sexo inválido!")
    sexo = input("Digite seu sexo (f/m): ")

estado_civil = input("Qual o seu estado civil (s - solteiro, c - casado, v - viúvo ou d - divorciado)?")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Estado civil inválido!")
    estado_civil = input("Qual o seu estado civil (s - solteiro, c - casado, v - viúvo ou d - divorciado)?")

if sexo == 'f':
    sexo = 'FEMININO'
if sexo == 'm':
    sexo = 'MASCULINO'
if estado_civil == 's':
    estado_civil = 'SOLTEIRO'
if estado_civil == 'c':
    estado_civil = 'CASADO'
if estado_civil == 'v':
    estado_civil = 'VIÚVO'
if estado_civil == 'd':
    estado_civil = 'DIVORCIADO'

print("########### DADOS DO USUÁRIO ##########")
print(f'Nome: {nome}')
print(f'Idade: {idade} anos de idade')
print(f'Salário: R${salario:.2f}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estado_civil}')












