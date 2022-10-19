# Desafio 026

"""
Faça um programa que leia uma frase pelo teclado e mostre:
1º Quantas vezes aparece a letra "A".
2º Em que posição ela aparece a primeira vez.
3º Em que posição ela aparece a última vez.
"""

# CODIGO:
frase = input("Digite uma frase: ").upper().strip()

# 1ºQuantas vezes aparece a letra "A".
print(frase.count('A'))

# 2ºEm que posição ela aparece a primeira vez.
print(frase.find("A"))

# 3ºEm que posição ela aparece a última vez.
print(frase.rfind("A"))