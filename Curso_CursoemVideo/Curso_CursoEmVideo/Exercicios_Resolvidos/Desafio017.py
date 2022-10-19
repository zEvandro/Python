# Desafio 017

"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa.
"""

# CODIGO:

# 1ª Resolução
from math import hypot

cat_op = float(input('Valor do cateto oposto: '))
cat_ad = float(input('valor do cateto adjacente: '))
hipotenusa = hypot(cat_op, cat_ad)  # --> usando a biblioteca math: math.hypot para calcular

print(f'cateto oposto: {cat_op} m')
print(f'cateto adjacente: {cat_ad} m')
print(f'hipotenusa: {hipotenusa:.2f}')
print(f'A área do triângulo retângulo é: {cat_op * cat_ad / 2:.2f} m² ')

print('-' * 30)

# 2ª Resolução
from math import sqrt

hipotenusa = sqrt(cat_op ** 2 + cat_ad ** 2)
print(f'O cateto oposto vai medir: {cat_op}\nO cateto adjacente vai medir: {cat_ad}\n'
      f'A hipotenusa vai medir: {hipotenusa:.2f}')
