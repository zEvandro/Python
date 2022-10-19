tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):  # --> começa do 1; vai ate a casa 11 mas não incluir ela; de 1 em 1.
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

print('\033[31m--=--\033[m' * 25)


# Códigos:

# Gerando uma sequência de 0 à 9
lista = list(range(10))
print(lista)
# resposta: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Gerando uma sequência de 1 à 11
lista = list(range(1, 11))
print(lista)
# resposta: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Gerando uma sequência de 0 à 30 com step=5
lista = list(range(0, 30, 5))
print(lista)
# resposta: [0, 5, 10, 15, 20, 25]

# Gerando uma sequência os 5 primeiros números da tabuada de 3
lista = list(range(0, 10, 3))
print(lista)
# resposta: [0, 3, 6, 9]

# Gerando uma sequência numérica negativa
lista = list(range(0, -10, -1))
print(lista)
# resposta: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# Gerando uma sequência numérica vazia
lista = list(range(0))
print(lista)
# resposta: []

""" Gerando uma sequência numérica vazia,
onde o interval inicial é maior do que o final
por essa razão, há lista é nula """

lista = list(range(1, 0))
print(lista)
# resposta: []