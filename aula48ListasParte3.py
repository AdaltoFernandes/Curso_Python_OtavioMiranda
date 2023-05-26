"""
Listas em Python
Tipo list - Mutável (Dados Mutaveis)
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Indice 0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1] # Deletando o ultimo item da minha lista -1 sempre vai ser o ultimo da minha lista
# lista.clear() # Limpa a lista toda fica só []
# O .insert(indice, valordesejado)
lista.insert(100, 5) # 1 valor inserir o indice, Se coloca virgula para por o que vamos inserir (valor)
print(lista)
