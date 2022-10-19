inventario = []
resposta = "S"
while resposta == "S":
# ADICIONAR ITEM NO INVENTÁRIO:
    equipamento = [str(input("Equipamento: ")).upper().strip(), float(input('Valor: ').strip()),
                   str(input('Número Serial: ').upper().strip()), input('Departamento: ').upper().strip(),
                   input('Responsavel: ').strip().upper()]
    inventario.append(equipamento)
    resposta = input('Digite "S" para continuar: ').upper()

# EXIBIR DADOS DO INVENTÁRIO
for elemento in inventario:
    print('Nome............: ', elemento[0])
    print('Valor...........: ', elemento[1])
    print('Serial..........: ', elemento[2])
    print('Departamento....: ', elemento[3])
    print('Responsável.....: ', elemento[4])

# LOCALIZAR UM ITEM NO INVENTÁRIO
busca = str(input('Digite o nome ou o nº de série do equipamento: ')).upper().strip()
for elemento in inventario:
    if busca == elemento[0] or busca == elemento[2]:
        print('Nome.........: ', elemento[0])
        print('Serial.......: ', elemento[2])
        print('Valor........: ', elemento[1])
        print('Responsável..: ', elemento[4])

# DEPRECIAR ITENS NO INVENTÁRIO
depreciacao = str(input('Digite o nome ou nº de série do equipamento que será depreciado: ')).upper().strip()
for elemento in inventario:
    if depreciacao == elemento[0] or depreciacao == elemento[2]:
        print('Equipamento...: ', elemento[0])
        print('Serial........: ', elemento[2])
        print('Valor antigo..: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Novo valor....: ', elemento[1])

# EXCLUIR UM ITEM DO INVENTÁRIO
excluir = str(input('Digite o nome ou nº de série do equipamento que deseja excluir: ')).upper().strip()
for elemento in inventario:
    if elemento[0] == excluir or elemento[2] == excluir:
        inventario.remove(elemento)

# EXIBIR DADOS DO INVENTÁRIO
for elemento in inventario:
    print('Nome............: ', elemento[0])
    print('Valor...........: ', elemento[1])
    print('Serial..........: ', elemento[2])
    print('Departamento....: ', elemento[3])
    print('Responsável.....: ', elemento[4])

# RESUMO DE VALORES DO INVENTÁRIO
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O total de equipamentos é de: ', sum(valores))