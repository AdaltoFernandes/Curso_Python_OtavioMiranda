import random # para coisas aleatorias
import sys

# nove_digitos = '' fazendo 1 por vez
# # Fazer o For para chamar isso varias vezes chamando de 0 a 9 
# for i in range(9): # 9 digitos 
#     nove_digitos += str(random.randint(0, 9)) # concatenar um random e formatar para string

for _ in range(100): # gerar 100 cpf
    nove_digitos = ''
    # Fazer o For para chamar isso varias vezes chamando de 0 a 9 
    for i in range(9): # 9 digitos 
        nove_digitos += str(random.randint(0, 9)) # concatenar um random e formatar para string


    # Randint (numero aleatorio inteiro (Numero aleatorio entre 0 e 9))
    # print(nove_digitos)
    # sys.exit()

    # nove_digitos = cpf_enviado_usuario[:9] # 9 primeiros digitos
    # nove_digitos = '34551232360'
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

    print(cpf_gerado_pelo_calculo)
        