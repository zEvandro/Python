nome = "Humberto Delgado"  # Variavel tipo String (str)
empresa = 'FIAP'  # Variavel tipo String (str)
qtde_funcionarios = 500  # Variavel tipo Inteiro (int)
mediaMensal = 856.50  # Variavel tipo Float (float)

#  Para que possamos exibir o conteudo de cada variavel, utilizaremos a função print():
print(nome + ' trabalha na empresa ' + empresa)
print('possui: ', qtde_funcionarios, 'funcionarios.')
print('A média da mensalidade é de : ' + str(mediaMensal))
print('------------------------------------------------------------------------------------------')
#   A função input()
# A função input() permitirá que o usuário final possa digitar um conteúdo em tempo de execução.

nome = input('Insira um nome: ')
empresa = input('Insira a instituição: ')
qtde_funcionarios = int(input('Insira a quantidade de funcionarios: '))
mediaMensal = float(input('Insira a média mensal: '))

print(nome + ' trabalha na empresa ' + empresa + '.')
print('possui: ', qtde_funcionarios, 'funcionarios.')
print('A média da mensalidade é de : ' + str(mediaMensal))
print('------------------------------------------------------------------------------------------')
#   A função type()
# Esta função retorna o tipo do dado que estiver dentro dos seus parenteses, para saber o tipo de dado da variavel.
print('verifique os tipos de dados abaixo: ')
print('O tipo de dado da variavel [nome] é: ',type(nome))
print('O tipo de dado da variavel [empresa] é: ',type(empresa))
print('O tipo de dado da variavel [qtde_fundionarios] é: ',type(qtde_funcionarios))
print('O tipo de dado da variavel [mediaMensal] é: ',type(mediaMensal))
print('------------------------------------------------------------------------------------------')

responsavel = input('Insira o nome do responsavel: ')
funcionario = input('Insira o nome do funcionario: ')
evento = input('Insira o evento: ')
valor = float(input('Insira o valor gasto: '))

print(f'Declaro para o senhor {responsavel}, que o senhor {funcionario},'
            f' esteve presente no evento {evento} e gastou o valor de R$ {valor} reais com a entrada.')
print('------------------------------------------------------------------------------------------')
