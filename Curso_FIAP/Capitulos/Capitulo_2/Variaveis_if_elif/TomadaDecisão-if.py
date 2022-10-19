# 'if' --> Este comando será responsavel por acrescentarmos
# ao nosso bloco de codigo a inteligencia da tomada de decisão, tornando-o mais independente.

# 'if' sua sintaxe(forma de utilizar o comando):
# if <condição>:
#    <o que você quer que aconteça caso a condição seja verdadeira>
print('------------------------------------------------------------------------------------------')

print('>>>> Decisões simples com if <<<<')
nome = input('Insira Nome: ')
idade = int(input('Insira idade: '))
prioridade = 'não'
idadePreferencial = 65

if idade >= idadePreferencial:
    prioridade = 'sim'
print(f'O paciente, {nome}, possui atendimento prioritário? {prioridade}')
print('------------------------------------------------------------------------------------------')

print('>>>> Decisões Compostas com if, else: <<<<')
nome = input('Insira Nome: ')
idade = int(input('Insira idade: '))

if idade >= idadePreferencial:
    print(f'O paciente, {nome}, possui atendimento prioritário.')
else:
    print(f'O paciente, {nome}, não possui atendimento prioritário.')
print('------------------------------------------------------------------------------------------')
print('>>>> Decisões Compostas com if, elif e else: <<<<')
# elif -> mais de uma condição.

nome = input('Insira Nome: ')
idade = int(input('Insira idade: '))
doenca_infecto = input('O paciente apresenta sintomas de doença infectoContagiosa? ').upper()

if idade >= 65:
    print(f'O paciente {nome}, possui atendimento prioritário.')
elif doenca_infecto == 'S':
    print(f'O paciente, {nome}, deve ser direcionado para uma sala reservada.')
else:
    print(f'O paciente, {nome}, não possui atendimento prioritário e pode aguardar na sala comum.')
print('------------------------------------------------------------------------------------------')

print('>>>> Uso dos operadores AND e OR <<<<')
nome = input('Insira Nome: ')
idade = int(input('Insira idade: '))
doenca_infecto = input('O paciente apresenta sintomas de doença infectoContagiosa? ').upper()

if idade >= 65 and doenca_infecto == 'S':
    print(f'O paciente {nome}, deverar ser direcionado para a sala: Amarela - com prioridade.')
elif idade >= 65 and doenca_infecto =='N':
    print(f'O paciente, {nome} devera ser encaminhado para a sala Branca - com prioridade.')
elif idade < 65 and doenca_infecto =='S':
    print(f'O paciente, {nome} deverá ser encaminhado para a sala Amarela - sem prioridade.')
elif idade < 65 and doenca_infecto == 'N':
    print(f'O paciente, {nome} deverá ser encaminhado para a sala Branca - sem prioridade.')
else:
    print('Responda a suspeita de doença infectocontagiosa com S ou N')
print('------------------------------------------------------------------------------------------')

print('>>>> Decisões Encadeadas <<<< ')
nome = input('Insira Nome: ')
idade = int(input('Insira idade: '))
doenca_infecto = input('O paciente apresenta sintomas de doença infectoContagiosa? ').upper()

if idade >= 65:
    print(f'O paciente, {nome} tem prioridade no atendimento.')
    if doenca_infecto == 'S':
        print(f'Encaminhe o paciente, {nome} para a sala AMARELA.')
    elif doenca_infecto == 'N':
        print(f'Encaminhe o paciente, {nome} para a sala BRANCA.')
    else:
        print('Responda a suspeita de doença infectocontagiosa com: S ou N.')
else:
    print(f'O paciente, {nome} não tem prioridade no atendimento.')
    if doenca_infecto == 'S':
        print(f'Encaminhe o paciente, {nome} para a sala AMARELA.')
    elif doenca_infecto == 'N':
        print(f'Encaminhe o paciente, {nome} para a sala BRANCA.')
    else:
        print('Responda a suspeita de doença infectocontagiosa com: S ou N.')
print('------------------------------------------------------------------------------------------')
