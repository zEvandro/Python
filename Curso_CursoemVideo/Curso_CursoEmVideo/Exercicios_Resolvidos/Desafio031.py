# Desafio 031

"""
Desenvolvar um programa que pergunte a distãncia de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagem até 200km
e R$0,45 para viagens mais longas.
"""

# CODIGO:

# 1ª RESOLUÇÃO
distancia = float(input("Qual a distância em km? "))
if distancia > 200:
    cobrar = (distancia * 0.45)
else:
    cobrar = (distancia * 0.5)
print(f'Você percorreu {distancia:.2f}km, terá que pagar R${cobrar:.2f} reais. ')

# 2ª RESOLUÇÃO
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.40
