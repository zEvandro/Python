resposta = 'SIM'
while resposta == "SIM":
    nome = input('Por favor, insira o nome do paciente: ').upper().strip()
    while nome == '' or not nome.isalpha():
        print('Por favor insira o nome do paciente corretamente.')
        nome = input('Por favor, insira o nome do paciente: ').upper().strip()
    idade = input('qual a idade do paciente? ').strip()
    while idade == '' or not idade.isnumeric():
        print('Por favor, insira a idade do paciente corretamente.')
        idade = input('qual a idade do paciente? ').strip()
    doenca_infecto = input('O paciente apresenta sintomas de doença infectocontagiosa?(S/N): ').upper().strip()
    while doenca_infecto != "S" and doenca_infecto != 'N':
        print('Digite S para sim ou N para não ')
        doenca_infecto = input('O paciente apresenta sintomas de doença infectocontagiosa?(S/N): ').upper().strip()
    idade = int(idade)
    if idade >= 65:
        if doenca_infecto == 'S':
            print(f'O paciente \033[1:31m{nome}\033[m, tem prioridade por esta infectado.')
            print('Deverá ser encaminhado para uma sala de espera separada.')
        else:
            print(f'O paciente \033[1:31m{nome}\033[m, tem prioridade no atendimento por ser 65+.')
    else:
        if doenca_infecto == 'S':
            print(f'O paciente \033[1:31m{nome}\033[m tem prioridade no atendimento, '
                  f'por possuir sintomas de uma doença infectocontagiosa.')
            print('Deverá ser encaminhado para uma sala de espera separada.')
        else:
            genero = input('Qual o genero do paciente? ').upper().strip()
            while genero != 'F' and genero != 'M':
                print('Responda com F para feminino ou M para masculino')
                genero = input('Qual o genero do paciente? ').upper().strip()
            if genero == 'F' and idade > 10:
                gravidez = input('A paciente esta gravida? ').upper().strip()
                while gravidez != "S" and gravidez != "N":
                    print('Responda S para sim ou N para não')
                    gravidez = input('A paciente esta gravida? ').upper().strip()
                if gravidez == 'S':
                    print('\033[31mA paciente tem prioridade por esta gravida\033[m')
                else:
                    print('A paciente não tem prioridade')
            else:
                print('O paciente não tem prioridade')
