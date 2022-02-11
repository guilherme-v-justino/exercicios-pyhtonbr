"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
 Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

sexo = input('Digite o sexo (M/F): ')

if sexo.lower() == 'f':
    print('F - Feminino')
if sexo.lower() == 'm':
    print('M - Masculino')
elif sexo.lower() != 'f' and 'm':
    print('Sexo inválido')
