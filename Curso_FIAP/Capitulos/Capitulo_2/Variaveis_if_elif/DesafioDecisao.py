
modulo = input('Qual seu nível de acesso? ').upper()
if not modulo:
    print('Error: preencha o campo: usuario.')
elif not modulo.isalpha():
    print('Error: preencha apenas com caracteres: letras')
else:
    genero = input('insira o genero do usuario? ').upper()
    if not genero:
        print('Error: Preencha o campo: genero.')
    elif not genero.isalpha():
        print('Error: preencha apenas com caracteres: ( M / F ) ')
    else:
        if modulo == 'ADM' and genero == 'M':
            print('Olá administrador.')
        elif modulo == 'ADM' and genero == 'F':
            print('Olá administradora.')
        elif modulo == 'USR' and genero == 'M':
            print('Olá usuário.')
        elif modulo == 'USR' and genero == 'F':
            print('Olá usuária.')
        elif modulo == 'GUEST':
            print('Olá visitante.')
        else:
            print('Digite um usuario valido')
print('-----------------------------------------------------------------------------------------')

modulo = input('Qual seu nível de acesso? ').upper()
if not modulo:
    print('Error: preencha o campo: usuario.')
elif not modulo.isalpha():
    print('Error: preencha apenas com caracteres: letras')
else:
    genero = input('insira o genero do usuario? ').upper()
    if not genero:
        print('Error: Preencha o campo: genero.')
    elif not genero.isalpha():
        print('Error: preencha apenas com caracteres: ( M / F ) ')
    else:
       if modulo == 'ADM' or modulo == 'USR':
           if modulo == 'ADM':
               if genero == 'M':
                   print('Ola admninistrador')
               else:
                   print('Ola administradora')
           else:
               if genero == 'M':
                   print('Ola usuario')
               else:
                   print('Ola usuária.')
       elif modulo =='GUEST':
           print('Ola visitante.')
       else:
           print('Olá desconhecido.')