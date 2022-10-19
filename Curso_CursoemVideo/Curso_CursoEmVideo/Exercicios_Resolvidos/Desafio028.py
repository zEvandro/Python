# Desafio 028

"""
Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# CODIGO:
from random import randint
from time import sleep


n = randint(0, 5)

x = int(input('insira um numero entre 0 e 5: '))
print('huuuuuuuuum. . . ')
sleep(2)
if x == n:
    print('YOU WIN! Você conseguiu me vencer :( ')
else:
    print(f' YOU LOSER! Pensei no número {n} HahAhahAHaHa')


