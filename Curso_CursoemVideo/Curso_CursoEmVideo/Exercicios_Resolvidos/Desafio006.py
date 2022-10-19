# Desafio 006

"""
Crie um algoritmo que leia um número e mostre:
O seu dobro, triplo e raiz quadrada.
"""

# CODIGO:
# 1ª Solução: usando variáveis

x = int(input('insira um número: '))
x2 = x * 2
x3 = x * 3
xx = x ** (1/2)

print(f'O número é: {x}\nO dobro dele é: {x2}\nO triplo dele é:'
      f' {x3}\nSua raiz é: {xx:.2f}')


# CODIGO:
# 2ª Solução: não utilizando variáveis

x = int(input('insira um número: '))

print(f'O número é: {x}\nO dobro dele é: {x*2}\nO triplo dele é:'
      f' {x*3}\nSua raiz é: {x**(1/2):.2f}')