# COMANDO def:
"""
Para criarmos funções , utilizaremos o comando "def", e a estrutura básica de uma função é a seguinte:

------------------------------------------------------------------------------------------------------
SINTAXE:

def <identificador da funcao> (<parametro(s)>):
	<código que será executado>
	return <Dado que será retornado, caso seja necessário>

-----------------------------------------------------------------------------------------------------
ONDE:

>> O identificador da função deve seguir as mesmas regras e padronizações dos identificadores
das variáveis e listas. As funções representam "ações" como: inserir, exibir, consultar, apagar, calcular, então
é de bom-tom utilizar um verbo no identificador da função.

>> O parâmetro é um dado que será fornecido para que a função possa executar o seu bloco de códigos. è como se
fossem os ingredientes de uma receita, por exemplo, para que uma função possa calcular uma média aritmética,
entre duas notas, você deverá fornecer as duas notas ou ainda para que uma função calcule o salário líquido
de um colaborador, precisará informar para a função, no mínimo, o salário bruto.

>> O código a ser executado representa o conjunto de códigos que possuem uma mesma finalidade dentro da aplicação

>> A última linha de "return" é opcional e deve ser usada somente quando você desejar que a função retorne um valor
para o módulo principal.

"""


def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input(str("Equipamento: ").upper().strip()),
                       float(input("Valor: ")),
                       str(input("Número Serial: ")),
                       input("Departamento: ").upper().strip()]
        lista.append(equipamento)
        resp = input("Digite 'S' para continuar: ").upper()


def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])


def localizarPorNome(lista):
    busca = str(input('Digite o nome ou nº de série do equipamento: ').upper().strip())
    for elemento in lista:
        if busca == elemento[0] or busca == elemento[2]:
            print('Nome..........: ', elemento[0])
            print('Serial........: ', elemento[2])
            print('Valor.........: ', elemento[1])
            print('Departamento..: ', elemento[3])


def depreciarPorNome(lista, porc):
    depreciacao = str(input('Digite o nome ou nº de série do equipamento para depreciação: '))
    for elemento in lista:
        if depreciacao == elemento[0] or depreciacao == elemento[2]:
            print('Nome..........: ', elemento[0])
            print('Serial........: ', elemento[2])
            print('Departamento..: ', elemento[3])
            print('Valor Antigo..: ', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('Novo valor....: ', elemento[1])

def excluirPorSerial(lista):
    serial = str(input('Digite o nome ou o nº de série do equipamento que deseja excluir: '))
    for elemento in lista:
        if serial == elemento[0] or serial == elemento[2]:
            lista.remove(elemento)
    return 'itens excluidos.'

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print('O equipamento mais caro custa: ', max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('A soma de todos os equipamentos é: ', sum(valores))
