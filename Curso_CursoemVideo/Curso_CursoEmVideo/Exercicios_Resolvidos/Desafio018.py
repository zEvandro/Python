# Desafio 018

"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo
"""

# CODIGO:
# 1ª Resolução

import math
ang = float(input('Qual o valor do ângulo? '))
# IMPORTANTE: Como se trata de um ângulo temos que converter
# o valor para RADIANOS antes de calcular o SENO, COSSENO e TANGENTE.

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O ângulo: {ang}º')
print(f'O seno do ângulo {ang}º é: {sen:.2f}')
print(f'O cosseno do ângulo {ang}º é: {cos:.2f}')
print(f'A tangente do ângulo {ang}º é: {tang:.2f}')

print('-' * 30)


# 2ª Resolução

from math import sin, tan, cos, radians
# DICA IMPORTANTE: importando somente as ferramentas, não é necessário usar o 'math.'
# como podemos ver no itens marcados com **

ang = float(input('Qual o valor do ângulo? '))
cos = cos(radians(ang))  # **
sen = sin(radians(ang))  # **
tang = tan(radians(ang))  # **
print(f'O ângulo: {ang}º')
print(f'O seno do ângulo {ang}º é: {sen:.2f}')
print(f'O cosseno do ângulo {ang}º é: {cos:.2f}')
print(f'A tangente do ângulo {ang}º é: {tang:.2f}')