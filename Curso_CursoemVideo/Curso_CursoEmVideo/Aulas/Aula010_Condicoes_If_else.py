"""
Nessa aula, vamos aprender como utilizar estruturas condicionais
simples e compostas nos seus programas em Python.
"""

# CONDIÇÕES if , else

"""

se carro.esquerda()
    bloco verdadeiro
senão
    bloco falso


if carro.esquerda():
    bloco True
else:
    bloco False

"""

# EXEMPLO 1

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:  # --> condição simples: só com if
    print('Carro novo')
else:  # --> condição composta: com if e else
    print('Carro velho')

# EXEMPLO 2

dinheiro = float(input('Quanto dinheiro você tem? '))
print('rico'if dinheiro >= 1000 else'pobre')  # --> condição simplificada.
print('--FIM--')


