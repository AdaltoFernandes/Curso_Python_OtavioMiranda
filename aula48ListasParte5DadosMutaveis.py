"""
Cuidado com os dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'

# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # retorna uma nova lista com os mesmos valores para lista b

# Jogando o valor Qualquer coisa no indice do Luiz
lista_a[0] = 'Qualquer coisa'
print(lista_a) # printou ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b) # printou ['Luiz', 'Maria', 1, True, 1.2]

