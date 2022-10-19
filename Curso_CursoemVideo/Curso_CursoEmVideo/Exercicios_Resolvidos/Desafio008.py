# Desafio 008

"""
Escreva um programa que leia um valor em metros eo exiba convertido em:
centímetros e milímetros.
"""

# CODIGO:

valor = float(input('Insira o valor: '))
cent = valor * 100
mili = valor * 1000

print(f'Metros: {valor}\nEm centímetros: {cent:.0f} centímetros\nEm milímetros: {mili:.0f} milímetros')