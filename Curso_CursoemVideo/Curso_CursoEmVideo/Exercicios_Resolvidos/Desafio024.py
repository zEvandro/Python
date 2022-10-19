# Desafio 024

"""
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "santo".
"""

# CODIGO:

# 1ª RESOLUÇÃO
cidade = input('Digite o nome de uma cidade: ').upper()
cidaded = cidade.split()
print("SANTO" in cidaded[0])

# 2ª RESOLUÇÃO
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == "SANTO")