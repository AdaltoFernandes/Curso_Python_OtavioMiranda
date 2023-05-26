# Laço de repetição for
# for = para
### CODIGO ABAIXOO ###


#### EXEMPLO 1 #### WHILE AINDA ##
# # Antes com o While, por exemplo a gente tina que fazer oq?
# texto = 'Python s2'
# # 1° Cria o indice
# i = 0
# # Pegar o tamanho da string
# tamanho_string = len(texto)

# # Usar o While (Enquanto)
# while i < tamanho_string:
#     print (texto[i], i)
    
#     i += 1

#### EXEMPLO 2 #### WHILE AINDA ##
# senha_salva = '123456' # senha salva no banco de dados
# senha_digitada = '' # 
# repeticoes = 0  # indice

# # While é utilizado - quando não sei precisamente quantas repetições vamos ter.
# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    
#     repeticoes += 1

# print('Aquele laço acima pode ter repetições infinitas')


# Começo do FOR - explicação e codigo.
texto = 'Python'
novo_texto = ''
# FOR = PARA
# Para cada letra no texto -> vai fazer um interação (printar letra)
for letra in texto:
    novo_texto += f'*{letra}' # Colocando * entre as letras
    # print(letra)
print(novo_texto)
# Da onde veio essa variavel letra? Foi criada por min (Otavio)
# Como ela retorna as letras de texto? 
# A string é Iteravel e te entrega 1 valor por vez. E só podemos acessar 1 elemento
# dela por vez, através do seu iterador -> string( no ex é :letra)
# O for solicita para string(meu iterador)(letra) e coloca cada um dos elementos
# na ordem