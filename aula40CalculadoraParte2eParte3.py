while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+, -, / ou *): ')

    numeros_validos = None # Criando uma Flag 
    num_1_float = 0
    num_2_float = 0

    # Condição para tratar o numero para float
    try:
        num_1_float = float(numero_1)  # tentando converter o numero para float
        num_2_float = float(numero_2)  # tentando converter o numero para float
        numeros_validos = True # não dando erro da true e muda o valor da FLAG
    except:
        numeros_validos = None # deu erro cai aqui deixando o valor None da FLAG

    if numeros_validos is None: # Se os numeros forem None - não são validos
        print('Um ou ambos números digitados são inválidos.')
        continue # para o laço e continua do começo, fazendo digitar os numeros novamente

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ### Basico ###
    # print('Realizando sua conta. Confira o Resultado abaixo:')
    # if operador == '+':
    #     print(num_1_float + num_2_float)
    # elif operador == '-':
    #     print(num_1_float - num_2_float)
    # elif operador == '/':
    #     print(num_1_float / num_2_float)
    # elif operador == '*':
    #     print(num_1_float * num_2_float)

    # else: 
    #     print('Nunca Deveria chegar aqui.')
    ###### Mais bonitinho #####
    print('Realizando sua conta. Confira o Resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)

    else: 
        print('Nunca Deveria chegar aqui.')

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
