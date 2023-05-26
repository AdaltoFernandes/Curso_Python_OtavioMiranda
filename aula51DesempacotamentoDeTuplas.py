"""
Introdução ao desempacotamento + tuples (tuplas)
"""
# Criar variaveis tirando os valores da lista.

# === Exemplo 1 ===
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2) # Helena
# Foi gerado em ordem

# === Exemplo 2 ===
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# Para desempacotar sem erros devemos ter a mesma quantidade de valores e variaveis.
# Ou seja nome1, nome2 (variaveis) = ['Oi, Tim'] (valor) (2/2) Ai não da erro.

# === Exemplo 3 ===
# Pegar só o primeiro valor e deixar o resto em outra variavel. 
# Deixar o resto numa variavel e não usar não é legal em Python

#nome1 vai receber: Maria
      #Resto vai receber: ['Helena', 'Luiz']  
# nome1, *resto = ['Maria', 'Helena', 'Luiz']

# === Exemplo 4 ===
  # Para pegar o primeiro valor e deixar o resto é bom deixar numa variavel comum a _  <-
  # porque outro desenvolvedor vai saber que não vou usar ela através da variavel underline _
#Exemplo: nome1, *_ = ['Maria', 'Helena', 'Luiz']
        # print(nome1)

# === Exemplo 5 ===
# para pegar só o valor2
_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)


# === Exemplo 6 ===
# pegando só o valor 3 do indice.
_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']
print(nome3)

