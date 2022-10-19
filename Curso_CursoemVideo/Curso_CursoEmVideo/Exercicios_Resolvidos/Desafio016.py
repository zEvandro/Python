# Desafio 016

"""
Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção inteira
"""

# CODIGO:
# 1ª Resolução
"""
math.trunc(x)
Retorna x com a parte fracionada removida, deixando a parte inteira.
"""
import math
num = float(input('Insira um número Real: '))
num1 = math.trunc(num)
print(f'Número real: {num}')
print(f'Número inteiro: {num1}')

print('-' * 30)

# 2ª Resolução
from math import trunc

print(f'valor digitado: {num} ')
print(f'valor inteiro: {trunc(num)}')

print('-'* 30)

# 3ª Resolução

print(f'valor digitado: {num}')
print(f'valor inteiro: {int(num)}')

