# Desafio 005

"""
Crie um programa que leia um numero inteiro
e mostre na tela seu sucessor e seu antecessor.
"""

# CODIGO:
# 1ª Solução: usando variáveis

numero = int(input('Insira um numero: '))
suc = numero + 1
ant = numero - 1
print(f'O numero é: {numero}\nSeu antecessor é: {ant}\nSeu sucessor é: {suc}')

# CODIGO:
# 2ª Solução: não utilizando variáveis

numero = int(input('Insira um numero: '))

print(f'O numero é: {numero}\nSeu antecessor é:'
      f'{numero-1}\nSeu sucessor é: {numero+1}')