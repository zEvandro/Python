# Desafio 033

"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

# CODIGO:

primeiro = int(input('Digite uma número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))

print('---MAIOR NÚMERO---')
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print(f'O maior número é: {maior}')

print('---MENOR NÚMERO---')
menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro
print(f'O menor número é: {menor}')
