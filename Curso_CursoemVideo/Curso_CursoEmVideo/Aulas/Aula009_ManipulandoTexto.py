"""
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().
"""

# Toda cadeia de caractere/String esta entre aspas simples:'' ou duplas ""
# Exemplo: 'ola mundo' , "ola mundo"


# FATIAMENTO DA STRING

"""

frase = 'setembro'
  ↓           ↓
variável    String


# FATIAMENTO DA STRING:   cada caractere recebe uma posição na memoria.        

frase = 's e t e m b r o'
         ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
         0 1 2 3 4 5 6 7 

"""
# Exemplo:

frase = 'setembro'
print(frase)
# Resultado: setembro

# Exemplos de Fatiamento:

frase = 'setembro'
print(frase[2])
# Resultado:t

print(frase[1:6])  # --> Começa na casa 1 e termina na casa 5* *(sempre Busca -1)
# Resultado:etemb

print(frase[0:7:2])  # --> Começa do 0 vai ate 6 , pulando de 2 em 2
# Resultado:stmr

print(frase[:5])  # --> É a mesma coisa que escrever [0:5], começa do zero e vai ate o 5-1
# Resultado:setem

print(frase[3:])  # --> indica o início , até o final.
# Resultado:embro

print(frase[1::2])  # --> Começa do 1 vai ate o final , pulando de 2 em 2
# Resultado:eebo


# ANÁLISE DE STRING

"""
frase = 's e t e m b r o'
         ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
         0 1 2 3 4 5 6 7
"""
# FUNÇÃO len() --> Sabendo quantos caracteres tem na string.
frase = 'setembro'
print(len(frase))
# Resultado:8

# FUNÇÃO .count() --> Saber quantas vezes aparece o caractere selecionado dentro da string
frase = 'otorrinolaringologista'
print(frase.count('o'))
# Resultado:5

# FUNÇÃO .find() --> Saber quando ele encontra e qual a posição inicial
frase = 'vida'
print(frase.find('da'))
# Resultado:2

# OPERADOR in --> verifica se dentro da variável existe a palavra ou caractere
frase = ' a radio é feliz'
print('radio' in frase)
# Resposta: True



# TRANSFORMAÇÃO DA STRING

"""
frase = 's e t e m b r o'
         ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
         0 1 2 3 4 5 6 7
"""

# FUNCIONALIDADE .replace() --> usado para trocar
frase = 'Bora bill'
print(frase.replace('bill', 'mulher do bill'))
# Resultado:Bora mulher do bill

# FUNCIONALIDADE .upper() --> Usado para deixar toda a string em Maiúsculo.
# FUNCIONALIDADE .lower() --> Usado para deixar toda a string em Minúsculo.

frase = 'python é legal'
print(frase.upper())
# Resultado:PYTHON É LEGAL

frase = 'PYTHON É LEGAL'
print(frase.lower())
# Resultado:python é legal

# FUNCIONALIDADE .capitalize() --> Usado para deixar toda a String minuscula exceto a primeira letra
frase = 'a Cachorra da Vizinha Morreu Hoje.'
print(frase.capitalize())
# Resultado:A cachorra da vizinha morreu hoje.

# FUNCIONALIDADE .title() --> Usado para deixar cada letra inicial das palavras em maiusculo
frase = 'a vida de geraldo mazzenato é incrível.'
print(frase.title())
# Resultado:A Vida De Geraldo Mazzenato É Incrível.

# FUNCIONALIDADE .strip() --> Usado para remover os espaços excedentes do inicio e final da cadeia
# FUNCIONALIDADE .rstrip() --> remover somente do lado direito.
# FUNCIONALIDADE .lstrip() --> Remover somente do lado esquerdo.

"""
frase = '  gato  '
         ↓↓↓↓↓↓↓↓
         01234567
"""
frase = '   caramba olha    '
print(frase.strip())
# Resultado:caramba olha

print(frase.rstrip())
# Resultado:   caramba olha

print(frase.lstrip())
# Resultado:caramba olha    .


# DIVISÃO DA STRING

# FUNCIONALIDADE .split() --> Divide a String, colocando indexação nova para cada uma delas, gerando uma lista
frase = 'cada palavra na lista'
print(frase.split())
# Resultado:['cada', 'palavra', 'na', 'lista']

# JUNÇÃO DA STRING

# FUNCIONALIDADE '-'.join() --> Usado para juntar uma lista com '-'.
frase = ['cada', 'palavra', 'na', 'lista']
print('-'.join(frase))  # --> você pode trocar o '-' por qualquer coisa : 'p' ,'@', '='
# Resultado:cada-palavra-na-lista
print('='.join(frase))
# Resultado:cada=palavra=na=lista
print('@'.join(frase))
# Resultado:cada@palavra@na@lista

# FUNCIONALIDADE .zfill() --> O método adiciona zeros (0) no início da cadeia, até atingir o comprimento especificado.
# Sintaxe: string.zfill(len)
txt = "50"
x = txt.zfill(10)
print(x)
# Resultado: 0000000050

