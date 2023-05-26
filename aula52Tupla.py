"""
Tipo Tupla - Uma lista imutável ou seja não recebe .append() por ser imutável
# A tupla é pouco mais eficiente que a lista
"""
# Como criar uma tupla? abaixo a criação só não colocar []
# Ex: nomes = 'Maria', 'Helena', 'Luiz'
# Ex2: nomes = ('Maria', 'Helena', 'Luiz')

nomes = 'Maria', 'Helena', 'Luiz'
# nomes[1] = 'outro'
print(nomes[-1])

### EXEMPLOS ###
# As vezes voce tem uma lista e quer converter em tupla
nomes = tuple(nomes)
#fazendo o inverso
nomes = list(nomes)
