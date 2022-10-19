# Desafio 012

"""
Faça um algoritmo que leia o preço de uma produto e mostre seu preço
com 5% de desconto.
"""

# CODIGO:

nome = input('Qual o produto? ').upper()
preco = float(input('Qual o preço? '))

desconto = preco * 5/100

novo_preco = preco - desconto

print('-------------------------------------')
print(f'Produto: {nome}')
print(f'Preço: R$ {preco} reais')
print(f'preço com desconto de 5%: R$ {novo_preco} reais')
print('-------------------------------------')