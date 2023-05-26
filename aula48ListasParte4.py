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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Concatenação das listas A e B.

# Esse metodo extend, não retorna nada
lista_d = lista_a.extend(lista_b)
# Esse metodo sim, ele mexe diretamente na lista A. 
# Por isso, não conseguimos pegar esse valor e jogar em uma outra variavl.
lista_a.extend(lista_b) 
print(lista_a)