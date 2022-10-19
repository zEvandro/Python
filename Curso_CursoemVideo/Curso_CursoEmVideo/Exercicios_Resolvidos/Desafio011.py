# Desafio 011

"""
Faça um programa que leia a largura e a altura de uma parede em metros
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que a cada litro de tinta, pinta uma área de 2m².
"""

# CODIGO:

largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))

area = largura * altura

tinta = area / 2

print(f'A area da parede: {area:.2f} m².')
print(f'A Quantidade de tinta necessária será: {tinta} litros')

