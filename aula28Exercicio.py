'''
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nomeinvertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba " Desculpe, voce deixou campos vazios."
'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nomeprint = nome 
numeroletras = len(nome)
nome_invertido = nome[::-1]
p_letra = nome[0:1] # A primeira letra do seu nome é {letra}
u_letra = nome[-1:] # A ultima letra do seu nome

if nome and idade: # Verificador se nome e idade estão preenchidos.
  print(f'Seu nome é {nome}') # Meu nome é
  print(f'Seu nome invertido é {nome_invertido}') #nome invertido

  if ' ' in nome: # O nome contém ou não espaços
    print('Seu nome contém espaços')
  else:
    print('Seu nome NÃO contém espaços')
      # O nome contém ou não espaços


  print(f'Seu nome tem {numeroletras} letras') # O nome contém ou não espaços
  print(f'A primeira letra do seu nome é {p_letra}') # A primeira letra do seu nome é {letra}
  print(f'A ultima letra do seu nome é {u_letra}') # A ultima letra do seu nome é {letra}
else:
  print('Desculpe, voce deixou campos vazios.')
