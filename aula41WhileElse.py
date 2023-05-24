''' While/else'''
# O otavio fala que quase não usa isso

string = 'Valor Qualquer'
 
i = 0

while i <  len(string):
    letra = string[i]

    print(letra)

    i += 1
else:
    print('O else foi executado.')
print('Fora do While')