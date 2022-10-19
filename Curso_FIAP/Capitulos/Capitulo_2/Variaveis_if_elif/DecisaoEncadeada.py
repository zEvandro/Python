nome = input('Por favor, insira o nome do paciente: ').upper()
idade = int(input('Por favor, insira a idade do paciente: '))
doenca_infecto = input('O paciente apresenta sintomas de doença infectocontagiosa?(S/N): ').upper()

if idade >= 65:
    if doenca_infecto == 'S':
        print(f'O paciente {nome}, tem prioridade por esta infectado.')
        print('Deverá ser encaminhado para uma sala de espera separada.')
    elif doenca_infecto == 'N':
        print(f'O paciente {nome} tem prioridade no atendimento por ter 65+ anos de idade.')
    else:
        print('Responda se o paciente está infectado ou não com: S/N')

else:
    if doenca_infecto == 'S':
        print(f'O paciente {nome} tem prioridade no atendimento, '
              f'por possuir sintomas de uma doença infectocontagiosa.')
        print('Deverá ser encaminhado para uma sala de espera separada.')
    elif doenca_infecto == 'N':
        genero = input('Qual o genero do paciente? ').upper()
        if genero == 'F' and idade > 10:
            gravidez = input('A paciente esta gravida? ').upper()
            if gravidez == 'S':
                print('a paciente tem prioridade por esta gravida')
            else:
                print('A paciente não tem prioridade')
        else:
            print('O paciente não tem prioridade')
    else:
        print('O paciente não tem prioridade')
