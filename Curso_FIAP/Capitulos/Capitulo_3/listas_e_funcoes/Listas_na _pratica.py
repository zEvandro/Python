# TIPOS DE LISTAS

# lista preenchida estaticamente
lista_estatica =['xpto', True]

# >>>> lista preenchida dinamicamente
lista_dinamica = [input('Digite o usuário: '), bool(int(input('Está logado? ')))]

# Comentário: Na 'Lista_dinamica', o segundo item está passando por duas converções.
# Isso ocorreu porque desejamos um dado do tipo 'boolean', ou seja, uma dado booleano que
# pode possuir  apenas os valores 'True' ou 'False'. Este tipo de dado é usado normalmente para tipos de perguntas
# que possam ter com respostas somente os valores 'sim' ou 'não', como é o caso do nosso exemplo
# 'Está logado?', somente pode ter resposta sim ou não.

# como o input() retorna o dado com uma string, devemos converter o dado para um inteiro int(),
# Para então, posteriormente, conerte-lo para bool(booleano)


# lista vazia
lista_vazia = []