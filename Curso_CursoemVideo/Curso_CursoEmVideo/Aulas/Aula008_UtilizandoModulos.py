"""
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos
import e from/import no Python.Veja como carregar bibliotecas de funções e utilizar
vários recursos adicionais nos seus programas utilizando módulos built-in e módulos
externos, oferecidos no Pypi.
"""

# TRABALHANDO COM MÓDULOS:

# Comando para importar bibliotecas

"""
import + biblioteca = importará toda as funcionalidades de um módulo.
from + biblioteca + import + módulo = importará apenas a funcionalidade desejada.
"""


import emoji
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'a raiz de {num} é igual a {raiz}')
print(emoji.emojize('Python is :dog:'))

