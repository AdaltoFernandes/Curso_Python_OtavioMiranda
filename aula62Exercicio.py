'''
Calculo do Segundo digito do CPF
CPF: 746.824.890-7(0) <-- calculo desse
Coleta a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores 
por uma contagem regressiva começando de 11 <-- AGORA É 11 não 10.. 


Ex.:  746.824.890-70 (7468248907) (INCLUIDO O PRIMEIRO DIGITO 7 NO FINAL)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7  < -- INCLUSÃO
   70  36 48 56 12 20 32 27 0  14

   
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo digito do CPF é 0
'''
# CONTA PARA O SEGUNDO DIGITO

cpf_enviado_usuario = '15611198732'
nove_digitos = cpf_enviado_usuario[:9] # 9 primeiros digitos
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1 
    contador_regressivo_1 -= 1  
digito_1 = (resultado_digito_1 * 10 % 11) 
digito_1 = digito_1 if digito_1 <= 9 else 0 


dez_digitos = nove_digitos + str(digito_1) # 10 primeiros digitos
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2 # passou para inteiro pois era string
    contador_regressivo_2 -= 1  # aqui vai fazendo a contagem regressiva para ajudar a multiplicar
digito_2 = (resultado_digito_2 * 10) % 11 
digito_2 = digito_2 if digito_2 <= 9 else 0 


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
# print(cpf_gerado_pelo_calculo)
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'O CPF: {cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

    