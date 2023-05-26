"""
Exercicio
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista)) 
# Números de indices na lista
# numeros = range(0, indice_len) # Contagem de numeros dos indices na lista

# for numero in indices:
#      print(numero)

# for nome in lista:
#     print(nome) 

for indice in indices:
     print(indice, lista[indice])