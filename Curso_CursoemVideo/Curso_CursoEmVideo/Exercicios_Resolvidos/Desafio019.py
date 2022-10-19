# Desafio 019

"""
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome escolhido.
"""

# CODIGO:

import emoji
import random

aluno_1 = input('Qual o nome do 1º aluno? ').upper()
aluno_2 = input('Qual o nome do 2º aluno? ').upper()
aluno_3 = input('Qual o nome do 3º aluno? ').upper()
aluno_4 = input('Qual o nome do 4º aluno? ').upper()
print('-' * 30)
sorteado = random.choice([aluno_1, aluno_2, aluno_3, aluno_4])
print(emoji.emojize(f'O aluno sorteado para apaga o quadro foi . . . 🎉 {sorteado} 🎉'))
