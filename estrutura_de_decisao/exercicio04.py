"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input('Digite uma letra: ')

if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(f'{letra.upper()} é uma vogal!')
else:
    print(f'{letra.upper()} é uma consoante!')




