"""
Split e join com list e str
.split - divide uma string - retornando uma lista (list)
.join - une uma string
.strip - corta os espaços no começo e no fim
.rstrip corta o espaço da direita ->
.lstrip corta o espaço da esquerda <-
"""
frase = '   Olha só que  , coisa interessante   '
# Vai pegar todas as espaços que divem a palavra e retirar. quando o split() está puro = .split()
# Dentro do split pode colocar para dividir pela virgula .split(',') vai separar em lista.
lista_frases_cruas = frase.split(',')


lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())  # .strip corta os espaços no começo e no fim <->
    # .rstrip corta o espaço da direita ->
    # .lstrip corta o espaço da esquerda <-

# print(lista_frases_cruas)
# print(lista_frases)

#### METODO JOIN ### UNE UMA STRING
# frases_unidas = ''.join('abc') # print = abc
# frases_unidas = '-'.join('abc') # print = a-b-c
frases_unidas = '-'.join(lista_frases)
print(frases_unidas) # Olha só que-coisa interessante. O join trocou a virgula e o espaço pelo -



# Vai pegar todas as palavras o que divide a frase são os espaços. quando o split() está puro
# Dentro do split pode colocar para dividir pela virgula .split(,) vai separar em lista.
