"""Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes. """

caracteres = None
consoantes = []
for n in range(1, 11):
    caracteres = input(f'Digite um caracter {n}/10: ')
    if caracteres.lower() != 'a' and caracteres.lower() != 'e' and caracteres.lower() != 'i' \
            and caracteres.lower() != 'o' and caracteres.lower() != 'u':
        consoantes.append(caracteres)
print(f'Foram lida(s) {len(consoantes)} consoantes e as mesmas são: ')
print(*consoantes, sep=', ')
