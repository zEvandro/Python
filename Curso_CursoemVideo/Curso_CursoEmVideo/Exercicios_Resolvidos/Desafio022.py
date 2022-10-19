# Desafio 022

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1º O nome com todas as letras maiúsculas
2º O nome  com todas as letras minúsculas
3º Quantas letras ao todo (sem considerar os espaços)
4º Quantas letras tem o primeiro nome
"""

# CODIGO:

# 1ª RESOLUÇÃO
nome = str(input('Digite seu nome completo: '))
print(f'{nome}')

# 1º Seu nome em maiúsculo
print(nome.upper())

# 2º Seu nome em minúsculo
print(nome.lower())

# 3º Total de letras sem espaço
print(len(nome.replace(' ','')))

# 4º Total de letras dos seu primeiro nome
nomed = nome.split()
print(len(nomed[0]))

print('-' * 30)

# 2ª RESOLUÇÃO
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
# 1º
print(f'Seu nome em maiúsculas é {nome.upper()}')
# 2º
print(f'Seu nome em minúsculas é {nome.lower()}')
# 3º
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")}')
# 4º
print(f'Seu primeiro nome tem {nome.find(" ")}')
