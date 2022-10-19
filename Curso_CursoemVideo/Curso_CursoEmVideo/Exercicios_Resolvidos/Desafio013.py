# Desafio 013

"""
Faça um algoritmo que leia o salário de uma funcionário
e mostre seu novo salário com 15% de aumento.
"""

# CODIGO:

nome = input('Qual o nome do funcionário? ').upper()
salario = float(input('Qual o salário? '))

aumento = salario * 15/100

novo_salario = salario + aumento
print('--------------------------------------')
print(f'Funcionário: {nome}')
print(f'Salário: R$ {salario} reais.')
print(f'Salário com aumento de 15%: R$ {novo_salario} reais.')
print('--------------------------------------')
