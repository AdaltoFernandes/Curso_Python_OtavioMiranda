"""
Listas em Python
Tipo list - Mutável (Dados Mutaveis)
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extende +
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Indice 0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # Comando para deletar o item no indice 2 (o 30)
""" Com o comando del ---
O python apaga o 2 item da lista, que é o numero 30. 
O python tem que mover os indices todos os elementos da lista para frente, isso em um lista grande
ex: Lista com 10k de indice apagando o indice 10 o programa teria que mover 9990 indices para frente
isso vai pesar muito, o programa vai ficar lento.
Ou seja, devemos evitar o indice ser reescrito, evitar mover muita coisa de um lado para o outro.

O que é indicado para Lista? Adicionar ou Retirar coisas do final da lista.
"""
# Esse adicionar no final da lista é super rapido, diferente do del no inicio de uma grande lista.
lista.append(50) # adiciona 50 ao final da lista.
# lista.pop() # Remove o ultimo elemento da minha lista
lista.pop()
lista.append(60) # adiciona 60 ao final da lista.
lista.append('bbb') # adiciona 70 ao final da lista. 
ultimo_valor = lista.pop(3) # remove o valor desse indice

print(lista, 'Removido', ultimo_valor)

