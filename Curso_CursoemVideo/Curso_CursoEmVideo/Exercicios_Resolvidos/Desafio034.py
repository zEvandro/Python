# Desafio 034

"""
Escreva um programa que pergunte o salário de uma funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

# CODIGO:
salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f'O funcionário receberá o aumento de R${aumento:.2f} reais.'
      f' Seu salário agora é de R${salario + aumento:.2f} reais')