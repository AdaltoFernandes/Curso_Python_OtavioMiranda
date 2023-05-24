'''
Iterando strings com while
'''
#       012345678910 <- INDICE
nome = 'Luiz Otávio' # Iteráveis
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[3])

# fazer nova string com while
# nova_string += '*L*u*i*z *O*t*á*v*i*o'

# Exercicio - Otavio
nome = 'Luiz Otávio'
indice = 0
novo_nome = ''
# Condição indice menor que nome
while indice < len(nome):
    letra = nome[indice]
    # precisar adicionar + 1 ao indice se não vai sempre 0 e o 0 é L apenas
    # Ou seja vai ficar flodando L.. e não o nome todo. por isso o =+ 1 
    # O novo_nome agora, fica colocando a letra na string vazia, pega o valor antigo L +
    # o valor atual U, na proxima ele pega o I, na proxima o Z, e vai juntando. 
    # o while percorre o indice e a letra vai sendo inserida em novo nome, a cada loop
    novo_nome += f'*{letra}' # comando que adiciona as letras de acordo com o while (para adicionar
    # o asteristico é usando o f'{letra}')
    indice += 1

# novo_nome += '*' # Isso tbm já adiciona o caractere
print(novo_nome)



##### Exercicio com o print executando 1 letra por linha #####
# nome = 'Luiz Otávio'
# indice = 0
# while indice < len(nome):
#     print(nome[indice])
#     # precisar adicionar + 1 ao indice se não vai sempre 0 e o 0 é L apenas
#     # Ou seja vai ficar flodando L.. e não o nome todo. por isso o =+ 1 
#     indice += 1


