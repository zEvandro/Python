# Desafio 015

"""
Escreva uma programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que:
o carro custa:R$60/dia e R$ 0.15 Km/rodado.
"""

# CODIGO:

km = float(input('Quantidade de Km percorrido:Km '))
dia = float(input('Quantidade de dias alugados:Dias '))

pre_km = km * 0.15
pre_dia = dia * 60

print('-' * 40)
print(f'Quilômetros rodados: {km} km')
print(f'Dias de aluguel: {dia} dias')
print('-' * 40)
print(f'Pagará por Km/rodado: R$ {pre_km} reais')
print(f'Pagará por dias de aluguel: R$ {pre_dia} reais')
print(f'-' * 40)
print(f'TOTAL À PAGAR: R$ {pre_km + pre_dia} reais.')