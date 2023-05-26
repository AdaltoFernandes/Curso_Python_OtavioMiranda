''' 
Faça um jogo para o usuário advinha qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar possibilidade
para o usuario digitar apenas uma letra.
- Quando o usuário digitar uma letra, voce vai conferir se a letra 
digitada está na palavra secreta.
  - Se a letra digitar estiver na palavra secreta; exiba a letra;
  - Se a letra digitada não estiver na palavra secreta; exiba *.

 Faça a contagem de tentativas do seu usuario. 

'''
# Resolução do Otavio 
# Começa fazendo um loop para rodar o jogo inteiro.
# A gente pode quebrar o laço, voltar 

#importando modulo
import os # Importe feito para o comando limpar o terminal funcionar. -> os.system('cls')

palavra_secreta = 'peixe'
letras_acertadas = ''
numero_tentativas = 0



while True:
  letra_digitada = input('Digite uma letra: ')
  numero_tentativas += 1

  # Primeiro bloqueio - saber se ele digitou apenas 1 letra, se digitou apenas 1 (continue) 
  if len(letra_digitada) > 1:
    print('Digite apenas uma letra.')
    continue

  # Função para saber se a letra digitada está na palavra secreta
  if letra_digitada in palavra_secreta:
      letras_acertadas += letra_digitada # Função para guardar a letra certa nas letras acertadas

  # função para guardar as letras uma do lado da outra com a inserção do += letra_secreta
  palavra_formada = ''
  # Condição que vai mostrar a letra acertada, ou * quando a letra não for correta
  # Lógica do jogo
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
        palavra_formada += letra_secreta
    else:
      palavra_formada += '*'
  print('Palavra formada: ', palavra_formada)

  if palavra_formada == palavra_secreta:
    os.system('cls')
    print('VOCÊ GANHOU!! PARABÉNS!')
    print('A palavra era', palavra_formada)
    print('Tentativas:', numero_tentativas)



### MINHA SOLUÇÃO que estava tentando ###
# letra_digitada = input('Digite apenas uma letra: ')
# letra_secreta = 'peixe'
# letra_acertada += ''


# while letra_digitada < 1:
#   print('Digite apenas uma letra.')

#   if letra_digitada == letra_secreta:
#     letra_secreta += letra_acertada

#   if letra_digitada 
