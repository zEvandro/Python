# Desafio 035

"""
Desenvolva uma programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não forma um triângulo.
"""

# CODIGO:

a = float(input('digite o comprimento da reta: '))
b = float(input('digite o comprimento da segunda reta: '))
c = float(input('digite o comprimento da terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')


x = 'prova de python'
print(len(x))