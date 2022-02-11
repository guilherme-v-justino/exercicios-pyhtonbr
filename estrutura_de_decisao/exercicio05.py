"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. """

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (nota1 + nota2) / 2

if 7 <= media < 10:
    print(f"Média = {media} - Aluno aprovado!")
if media < 7:
    print(f"Média = {media} - Aluno reprovado")
if media == 10:
    print(f"Média = {media} - Aluno aprovado com Distinção! Parabéns!")


