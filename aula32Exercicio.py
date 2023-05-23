'''
Faça um programa que peça ao usuário para digitar um número interio, informe
se este número é par ou impar. Caso o usuario não digite número inteiro, informe 
que não é um numero inteiro.
'''
##### RESOLUÇÃO 1 OTAVIO ####
# entrada = input('Digite um número inteiro: ')
# if entrada.isdigit():
#   entrada_int = int(entrada)
#   par_impar = entrada_int % 2 == 0
#   par_impar_texto = 'impar'
  
#   if par_impar:
#     par_impar_texto = 'par'


#   print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#   print('Voce não digitou um número inteiro')

############# O QUE EU TINHA FEITO ##############
# numero = int(input('Digite um número inteiro: '))

# if (numero%2) == 0: # Codigo para verificar se o codigo é impar ou par.
#   print ("Par")
# else:
#   print("Ímpar")

# if numero != int(numero): # Código para verificar se o número é inteiro.
#   print('Voce não digitou um número inteiro')
################################################

# EXERCICIO 2 ====
'''
Faça um programa que pergunte o hora ao usuario e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
# MINHA RESOLUÇÃO #
horario = int(input('Que horas são? Digite o horário em números inteiros: '))

if horario == 0 or horario == 1 or horario == 2 or horario == 3 or horario == 4 or horario == 5 \
  or horario == 6 or horario == 7 or horario == 8 or horario == 9 or horario == 10 \
    or horario == 11:
  print('Bom dia!')
elif horario == 12 or horario == 13 or horario == 14 or horario == 15 or horario == 16 \
  or horario == 17:
  print('Boa Tarde!')
elif horario == 18 or horario == 19 or horario == 20 or horario == 21 or horario == 22 \
  or horario == 23:
  print('Boa Noite!')
else:
  print('Digite um horario correto.')

# Resolução do OTAVIO #  
entrada = input('Digite a hora em números inteiros: ')

try:
  hora = int(entrada)

  if hora >= 0 and hora <=11:
      print('Bom dia!')
  elif hora >= 12 and hora <= 17:
      print('Boa Tarde!')
  elif hora >= 18 and hora <= 23:
      print('Boa Noite!')
  else: 
    print('Não conheço essa hora')
except:
  print('Digite apenas numeros inteiros')


'''
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "seu nome é muito grande".
'''
# MINHA RESOLUÇÃO #
primeiro_nome = input('Digite seu primeiro nome: ')
nome = len(primeiro_nome) # Contagem dos Caracteres 

if nome <= 4:
  print('Seu nome é curto')
elif nome == 5 or nome == 6:
  print('Seu nome é normal')
elif nome >= 7:
  print('Seu nome é grande')


##### RESOLUÇÃO DO OTAVIO #####
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
       print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
       print('Seu nome é normal')
    else:
       print('Seu nome é grande')
else:
   print('Digite mais de uma letra.')