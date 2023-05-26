"""
enumerate - enumera iteráveis (índices)
O enumerate - Enumera cada item da lista 
"""
#[(0, 'Maria'), (1, 'João'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'João', 'Luiz']
lista.append('João')

### Exemplo: Para cada valor declarado na tupla, ele separa indice e nome, indice e nome.. ###
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# for item in enumerate(lista):
#   print('FOR da Tupla:')
#   for valor in item:
#     print(f'\t{valor}') # o comando -> \t é um tab de espaço.

# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)
# lista_enumerada = enumerate(lista)
# print(lista_enumerada) # vai retornar enumerate object at .....
# print(next(lista_enumerada)) # pega o primeiro valor, com o comando next ( 0, Maria)

# Mostrando a lista enumerada. Ex: 0 - Maria, 1 - João, 2 - Luiz ...
# for item in lista_enumerada:
#     print(item)

# Só conseguimos a exibição uma vez do enumerate, aqui já restorna object.. 
# print('O que tem nesta lista: ', lista_enumerada)

#Sempre criar um iterator (enumerate), o enumerate só tem "1 bala" ou seja só retorna o valor de 
# lista_enumerada = enumerate(lista) 1x apenas. Se necessitar dos dados novamente 
# é bom fazer outro enumerate. 