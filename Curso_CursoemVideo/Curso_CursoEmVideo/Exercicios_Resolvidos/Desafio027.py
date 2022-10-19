# Desafio 027

"""
Faça um programa qe leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

# CODIGO:
nome = str(input('Digite seu nome completo: ')).strip().upper().split()
print(nome)

print('Primeiro nome:',nome[0])
print('Último nome:',nome[-1])