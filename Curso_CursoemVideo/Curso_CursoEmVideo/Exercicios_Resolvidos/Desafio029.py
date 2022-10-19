# Desafio 029

"""
Escreva um programa que leia a velocidade de uma carro.

se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$ 7,00 por cada km acima do limite.
"""

# CODIGO:

velocidade = float(input('Qual a velocidade do carro em km/h? '))
if velocidade > 80:
    print(f'Você ultrapassou a velocidade maxima permitida em {velocidade - 80:.2f}kmh,'
          f' pagará R${(velocidade - 80) * 7:.2f} reais de multa.')
print('---Dirija com cuidado---')
