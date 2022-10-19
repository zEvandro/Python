# Desafio 020

"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação
dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a ordem sorteada.
"""

# CODIGO:

from random import shuffle
alunos = ['Ana', 'Pedro', 'Joyce', 'Paulo', 'Gustavo']
shuffle(alunos)
print('A ordem de apresentação será:')
print(alunos)

# shuffle --> significa embaralhar