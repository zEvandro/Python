# Desafio 004

"""
Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possiveis sobre ele.
"""

# CODIGO:

s = input('digite algo: ')

print('O tipo primitivo desse valor é', type(s))
print('Só tem espaços? ',s.isspace())
print('É um número? ',s.isnumeric())
print('É alfabético? ',s.isalpha())
print('É alfanumérico? ',s.isalnum() )
print('Está em maiúsculas? ',s.isupper())
print('Está em minúsculas? ',s.islower())
print('Está capitalizada? ',s.istitle())