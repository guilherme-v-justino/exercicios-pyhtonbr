"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """

turno = input("Em que turno você estuda? (M-Matutino, V-Vespertino, N-Noturno): ")
if turno.lower() == 'm' or turno.lower() == 'v' or turno.lower() == 'n':
    if turno.lower() == 'm':
        print("Bom Dia!")
    if turno.lower() == 'v':
        print("Boa Tarde!")
    if turno.lower() == 'n':
        print("Boa Noite!")

else:
    print("Valor inválido!")

