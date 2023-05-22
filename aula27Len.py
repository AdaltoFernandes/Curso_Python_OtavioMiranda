"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])  # Mundo (: vai até o final )
print(variavel[4:7]) # Mun
print(variavel[0:5]) # Olá m

print(len(variavel)) #9 caracteres na variavel - O len é para contar caracteres

