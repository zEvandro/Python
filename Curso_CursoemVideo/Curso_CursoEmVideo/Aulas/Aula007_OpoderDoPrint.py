"""
O PODER DO PRINT()
"""

# EXEMPLOS DE FORMATAÇÃO:

nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer {}!'.format(nome))
# Resultado: prazer em te conhecer evandro!  -->

print('Prazer em te conhecer {:20}!'.format(nome))
# Resultado: Prazer em te conhecer evandro             !
# --> Escreve o resultado no total de espaços.

print('Prazer em te conhecer {:>20}!'.format(nome))
# Resultado: Prazer em te conhecer              evandro!
# --> Escreve o resultado alinhado para a direita.

print('Prazer em te conhecer {:<20}!'.format(nome))
# Resultado: Prazer em te conhecer evandro             !
# --> Escreve o resultado alinhado para a esquerda.

print('Prazer em te conhecer {:^20}!'.format(nome))
# Resultado: Prazer em te conhecer       evandro       !
# --> Escreve o resultado centralizado.

print('Prazer em te conhecer {:=^20}!'.format(nome))
# Resultado: Prazer em te conhecer ======evandro=======!
# --> Escreve o resultado centralizado,cercado de "=".

# OUTROS EXEMPLOS:

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))

soma = n1 + n2
multip = n1 * n2
divi = n1 / n2
divi_in = n1 // n2
expo = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multip, divi))
# Explicação: {:.3f} --> determina o numero de casas decimais

print('Divisão inteira é {} e potência é {}'.format(divi_in, expo))

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multip, divi),end=' ')
print('Divisão inteira é {} e potência é {}'.format(divi_in, expo))
# Explicação: ,end='' --> significa para não pular linhas entre um print e outro.

print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}'.format(soma, multip, divi),end=' ')
print('Divisão inteira é {} e potência é {}'.format(divi_in, expo))
# Explicação: \n --> usado para quebrar linhas dentro de um print()


# PARA DA PRINT EM TEXTOS LONGOS

print('''ola jisahdkdiahihadjihdiafaf
afasfasfsafasfsafasfasfasfasfasfasfas
fasfasfasfasfasfasfsafasfasfas
fsafasfsafasfasfafasfasfasfasfasf
asfasfsafsafasfasfasfasfasfasfasf
fsafasfasfasfasfasfasfasfasfasfasfasfasfasf
afasfasfasfasfasfasfasfasfsafasfsaf''')