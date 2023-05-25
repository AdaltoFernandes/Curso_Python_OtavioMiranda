frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma.' \
        'Python foi criado por Guido van Rossum.'

# Qual a letra apareceu mais vezes nessa frase
# print(frase.count('frase')) # Faz a contagem de quantas vezes ela apareceu na frase.

# Criou indice

i = 0
qtd_atual = 0
letra_apareceu_mais_vezes = ''

# Essa Condição é o i é quem controla essa condição

while i < len(frase): # Quem controla essa condição é o i - e o i += 1 é  
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_atual < qtd_apareceu_mais_vezes_atual:
        qtd_atual = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
      'A letra que apareceu mais vezes foi' 
      f'{letra_apareceu_mais_vezes} que apareceu '
      f'{qtd_atual}x'
)