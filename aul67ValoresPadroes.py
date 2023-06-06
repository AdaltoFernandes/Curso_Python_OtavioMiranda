'''
Valores padrão para parâmetros podem 
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=0):
    
    print(f'{x=} + {y=} + {z=}', x + y + z)


soma(1, 2)
soma(3, 5)
soma(100, 200)

