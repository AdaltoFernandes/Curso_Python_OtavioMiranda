# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0 
    ['Luiz', 'João', 'Eduarda'] # 2  
]

# print(*salas, end='\n')
print(*salas, sep='\n')

# a, b, c = lista
# print(a, c)

#p, b, *_, ap, u = lista
#print(p, u, ap)
# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# print(*salas, end='\n')


# for nome in lista:
#     print(nome, end=' ', )