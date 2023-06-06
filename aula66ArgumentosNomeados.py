'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado receb apenas o argumento (valor)
'''
# def soma (paramentros)



def soma(x, y, z):
    # Definição 
    print(f'{x=} + y={y} + {z=}', '|', 'x + y + z = ', x + y + z)


# Ou usar não nomeado, ou tudo nomeado.
# Argumento NÃO NOMEADO (POSICIONAL)
soma(1, 2, 3)
# Argumento NOMEADO (Não prcisa de posição)
soma(y=2, z=3, x=1)



print(1,2,3, sep='-')