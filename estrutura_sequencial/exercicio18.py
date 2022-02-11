"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

tam_arq = int(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_link = int(input("Qual a velocidade do link de Internet em Mbps: "))
tempo = (tam_arq / (velocidade_link / 8)) / 60

print(f"O tempo estimado de download para um arquivo de {tam_arq}MB na velocidade "
      f"de {velocidade_link}Mbps é igual a {tempo:.0f} minutos")
