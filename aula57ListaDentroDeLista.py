'''
Lista de listas e seus índices
'''
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0 
    ['Luiz', 'João', 'Eduarda'] # 2  
]
#     ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2  
# ]

# # buscando a Lista 1 e vendo o valor 0 = Elaine 
# print(salas[1][0])

# # buscando a helena 
# print(salas[0][1])

# # Buscando a eduarda
# print(salas[2][2])

# # Buscando o 20
# print(salas[2][3][2])

# Fazendo for interno

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)