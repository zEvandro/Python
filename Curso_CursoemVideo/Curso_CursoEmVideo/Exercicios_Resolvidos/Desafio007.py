# Desafio 007

"""
Desenvolva um programa que leia as notas de um aluno,
calcule e mostre a sua média.
"""

# CODIGO:

nome = input('Digite o nome do aluno: ').upper()
nt_mat = float(input('Nota de Matemática: '))
nt_his = float(input('Nota de História: '))
nt_cie = float(input('nota de Ciências: '))
nt_por = float(input('Nota de Português: '))

media = (nt_mat + nt_his + nt_cie + nt_por) / 4

if media >= 6:
    sit = 'APROVADO'
else:
    sit = 'REPROVADO'
print(f'O aluno {nome}, tirou média: {media:.1f}\nSituação:{sit}')

