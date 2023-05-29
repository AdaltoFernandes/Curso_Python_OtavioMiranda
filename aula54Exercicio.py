"""
Faça uma lista de comprar com listas
O usuario deve ter a possibilidade de inserir, 
apagar e listar valores de sua lista
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de ìndices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Seleciona uma opção') # Usa print para falar para o usuario escolher
    opcao = input('[i]nserir [a]pagar [l]istar: ') # 3 opções no input

# Aqui ele faz as condições com if dentro de while mesmo.
    if opcao == 'i': # ele coloca aqui como string o if ' '
        os.system('cls') # limpando o console
        valor = input('Valor: ') # Input para guardar o valor na variavel
        lista.append(valor) # Inserindo valor do input na lista

    elif opcao == 'a':
        # os.system('cls')
        indice_str = input('Escolha o indice para apagar: ')
      
        try: 
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este índice.')
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar')

        for produtos in enumerate(lista):
          indice, nome = produtos
          print(indice, nome)




#### MINHA TENTATIVA ####
# entrada = input('Digite uma opção [i]nserir [a]pagar [l]istar: ').lower()

# lista_de_compra = ['Ovo', 'Pão' ]

# alternativa_i = ['i', 'inserir']
# alternativa_l = ['l', 'listar']
# alternativa_a = ['a', 'apagar']

# if entrada in alternativa_i:
#     inserido = input('Produto: ') 
#     lista_de_compra += inserido
#     lista_de_compra.append(inserido)

# if entrada == alternativa_l :
#     for item in enumerate(lista_de_compra):
#       indice, nome = item
#       print(indice, nome)
# elif entrada == alternativa_a:
#     ...

