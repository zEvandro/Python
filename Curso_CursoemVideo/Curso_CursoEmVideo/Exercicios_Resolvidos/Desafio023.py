# Desafio 023

"""
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados.
"""

# CODIGO:

# 1ª RESOLUÇÃO
num = str(input('Digite um número entre 0 e 9999: ')).zfill(4)

print('unidade:', num[3])
print('dezena:', num[2])
print('centena:', num[1])
print('Milhar:', num[0])

print('-' * 40)

# 2ª RESOLUÇÃO
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'unidade: {u}\ndezena: {d}\ncentena: {c}\nmilhar: {m}')
