'''
Usando o Replace para alterar a string. Ou seja retirar os pontos, espaços e virgulas.
Como usar o replace
1° - escolher o que vai sair o ponto, 2° depois o que eu quero '' <- nada(ou seja vai tira o espaço)
'156.187.162.12' .replace(1°'.',2°'') # coloquei assim para ilustrar.
o correto é .replace('o que vai sair', 'valor que eu quero')
ou seja: '156.187.162.12'.replace('.', '')


'''
### REPLACE ###
# cpf_enviado_usuario = '746.824.890-70'.replace('.', '') \
#   .replace('-', '') \
#   .replace(' ', '')
  # Replace para tirar o ponto, replace para tirar o traço - , replace para tirar espaço. 

# Expressão Regular - Substituir
# modulo re - import re
import re

# Também pode colocar esse tratamento direto no input.
entrada = input('Digite o CPF: ')

### o re.sub substitui tudo que não for de 0-9 por vazio.###
cpf_enviado_usuario = re.sub(
    r'[^0-9]', # O ^ da uma filtragem de tudo que não é um numero
    '', # vai substituir tudo que não for numero por isso. ou seja nada
    entrada # tratando direto a resposta do input
    
    )

# Vendo se a entrada é sequencial Ex: 11111111
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você mandou dados sequencias.')
    sys.exit()

# primeiro_caractere_entrada = entrada[0]
# primeiro_caractere_entrada_repetido = primeiro_caractere_entrada * len(entrada)
# print(entrada, primeiro_caractere_entrada_repetido)

# string 
# ssssss



nove_digitos = cpf_enviado_usuario[:9] # 9 primeiros digitos
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1 
    contador_regressivo_1 -= 1  
digito_1 = (resultado_digito_1 * 10 % 11) 
digito_1 = digito_1 if digito_1 <= 9 else 0 


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2 
    contador_regressivo_2 -= 1  
digito_2 = (resultado_digito_2 * 10) % 11 
digito_2 = digito_2 if digito_2 <= 9 else 0 


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'O CPF: {cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

    