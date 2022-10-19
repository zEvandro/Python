equipamentos = []
valores = []
codigos = []
departamentos = []

resposta = "S"
while resposta == "S":
    equipamentos.append(str(input('Equipamento: ').strip().upper()))
    valores.append(float(input('Valor: ').strip()))
    codigos.append(int(input('Código de identificação: ').strip()))
    departamentos.append(str(input('Departamento: ').strip().upper()))
    resposta = input('digite "S" se deseja continuar adicionando itens.').upper().strip()
print(' ')

#  USADO PARA EXIBIR A LISTA COM A AJUDA DO FOR DE FORMA SEPARADA
print('>>> LISTA DE EQUIPAMENTOS <<<')
for indice in range(0, len(equipamentos)):
    print("\033[1:32mEquipamento..:\033[m ", (indice+1))
    print('Nome.............: ', equipamentos[indice])
    print('valor............: ', valores[indice])
    print('Código...........: ', codigos[indice])
    print('Departamento.....: ', departamentos[indice])
    print(' ')
print(' ')

# BUSCADOR: usamos um buscador para pesquisar certo equipamento e recebe algumas informações.
busca = str(input('Digite o nome do equipamento que deseja buscar: ')).upper().strip()
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print(' ')
        print(f'Você pesquisou por: \033[1:35m{busca}\033[m')
        print('Valor.........: ', valores[indice])
        print('Código........: ', codigos[indice])
        print('Departamento..:', departamentos[indice])
print(' ')

# 1ª SITUAÇÃO: Os equipamentos buscados receberão uma depreciação de 10% no seu valor.
depreciacao = str(input('Digite o nome do equipamento que será depreciado: ')).upper().strip()
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print(f'O equipamento: \033[31m{depreciacao}\033[m sofreu uma depreciação de 10% no seu valor.')
        print(' ')
        print('valor antigo..: ', valores[indice])
        valores[indice] = valores[indice] * 0.9
        print('Novo valor...: ', valores[indice])
print(' ')
# 2ª SITUAÇÃO: Um equipamento com determinado código foi danificado e será descartado. precisamos elimina-lo.
remocao = int(input('Digite o código do equipamento que será descartado: ').strip())
for indice in range(0, len(equipamentos)):
    if codigos[indice] == remocao:
        del equipamentos[indice]
        del valores[indice]
        del codigos[indice]
        del departamentos[indice]
        break
print('O item foi removido da lista...')
print(' ')

#  USADO PARA EXIBIR A LISTA COM A AJUDA DO FOR DE FORMA SEPARADA
print('>>> LISTA ATUALIZADA DE EQUIPAMENTOS <<<')
for indice in range(0, len(equipamentos)):
    print('\033[1:32mEquipamentos..:\033[m ', (indice+1))
    print('Valor..........: ', valores[indice])
    print('Código.........: ', codigos[indice])
    print('Departamento...: ', departamentos[indice])
    print(' ')