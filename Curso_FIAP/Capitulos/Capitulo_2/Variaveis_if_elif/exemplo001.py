estoque_alimento = 100
estoque_eletronico = 50
estoque_limpeza = 30
print('--------------------------------------------------------------------------------------')

produto = input('Qual o produto? ').upper()
if not produto or not produto.isalpha():
    print('ERROR: Preencha o campo Produto, corretamente.')
else:
    categoria = input('Qual categoria? ').upper()
    if not categoria or not categoria.isalpha():
        print('ERROR: Preencha o campo: Categoria, corretamente.')
    else:
        qtd_produtos = input('Qual a quantidade de produtos? ')
        if not qtd_produtos or not qtd_produtos.isnumeric():
            print('ERROR: Preencha o campo: Quantidade, corretamente.')
        else:
            qtd_produtos = int(qtd_produtos)
            if categoria == 'ALIMENTO':
                if qtd_produtos < estoque_alimento:
                    print(f'Solicitar o produto {produto} para o setor de compras.')
                    print(f'Possuimos apenas {qtd_produtos}/{estoque_alimento} unidades no estoque.')
                else:
                    print(f'O estoque do produto {produto}, esta ok. Possuimos '
                          f'{qtd_produtos} unidades.')
            elif categoria == 'ELETRONICO':
                if qtd_produtos < estoque_eletronico:
                    print(f'Solicitar o produto {produto} para o setor de compras.')
                    print(f'Possuimos apenas {qtd_produtos}/{estoque_alimento} unidades no estoque.')
                else:
                    print(f'O estoque do produto {produto}, esta ok. Possuimos '
                          f'{qtd_produtos} unidades.')
            elif categoria == 'LIMPEZA':
                if qtd_produtos < estoque_limpeza:
                    print(f'Solicitar o produto {produto} para o setor de compras.')
                    print(f'Possuimos apenas {qtd_produtos}/{estoque_limpeza} unidades no estoque.')
                else:
                    print(f'O estoque do produto {produto}, esta ok. Possuimos '
                          f'{qtd_produtos} unidades.')
            else:
                print('categoria não existe.')