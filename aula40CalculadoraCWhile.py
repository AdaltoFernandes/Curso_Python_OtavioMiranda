''' Calculadora com while '''



while True:
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break






# Rascunho.. #

# entrada1 = int(input('Digite o primeiro numero: '))
# entrada2 = int(input('Digite o segundo numero: '))
# operador = int(input('Escolha o operador: 1 Adicão, 2 - Subtração, 3 - Divisão ou 4 Multiplicacão. '))



# if operador == 1:


# adicao = 1
# subtracao = 2
# divisao = 3
# multiplicacao = 4

# while True:
#     sair = input('Quer sair? [S]im: ')
#     sair = sair.lower() # A função .lower converte tudo que esta maisculo para minusculo.
#     sair = sair.startswith('s') # Mostra se a palavra começa com a primeira letra. no Ex é s.
#     print(sair)
