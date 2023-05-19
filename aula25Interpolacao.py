"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""


nome = 'Luiz'
preco = 1000.95897643
# variavel = 'Luiz, o preço total foi R$1000.95'
# variavel = '%s, o preço total foi R$%f' % (nome,preco)
# arrumando o R$ com 2 casas decimais.
# No final mostra as variveis que estou usando em ordem (..,..)
variavel = '%s, o preço total foi R$%.2f' % (nome,preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))
