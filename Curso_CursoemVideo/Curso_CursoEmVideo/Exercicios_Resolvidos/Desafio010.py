# Desafio 010

"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
"""

valor = float(input('Insira uma valor em Real: R$ '))

dolar = 5.25
Dinar_kuwaitiano = 16.96
Rupia_indiana = 0.066
euro = 5.19
peso_argentino = 0.037

print('-' * 20)
print(f'Com R$ {valor:.2f}, podemos comprar:')
print('-' * 20)
print(f'Dolar: {valor/dolar:.2f}')
print(f'Rupia indiana: {valor/Rupia_indiana:.2f}')
print(f'Dinar Kuwaitiano: {valor/Dinar_kuwaitiano:.2f}')
print(f'Euro: {valor/euro:.2f}')
print(f'peso Argentino: {valor/peso_argentino:.2f}')
print('-' * 20)