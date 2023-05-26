"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extende +
# Só funciona com string .upper() para deixar em Maisculo
"""
#         01234 
#        -54321
string = 'ABCDE' # 5 Caracteres (len)

# 1° Forma de criar lista - não é muito comum criar lista assim
# lista = list()
# 2° Forma de criar lista 
lista = [123, True, 'Luiz Otávio', 1.2, []] # 0 = 123, 1 = True, 2 = Luiz Otávio, 3 = 1.2, 4 = [].
lista[-3] = 'Maria' # Trocando Luiz Otávio por Maria na lista.
print(lista[2], type(lista[2]))


# print(bool(lista)) # falsy
# print(lista, type(lista))
