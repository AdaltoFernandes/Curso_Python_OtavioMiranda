'''
Calculo do Primeiro Digito do CPF depois do traço - 
CPF: 746.824.890-70
Coleta a soma dos 9 primeiros digitos do CPF multiplicando cada um 
dos valores por uma contagem regressiva começando de 10 

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0  

   
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7 
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
'''

"""
Ex:  162.473.877-09
   10  9  8  7  6  5  4  3  2
*  1   6  2  4  7  3  8  7  7 # Multiplica 
   10  54 16 28 42 15 32 21 14 # SOMA TUDO 
Total da Soma 
(10+54+16+28+42+15+32+21+14) = 232
Multiplicar o total por dez 
232 * 10 = 2320
Obter o resto da divisçao da conta anterior por 11
2320 % 11 = 10
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

    RESPOSTA \/
O primeiro digito do cpf é 0
   """

# # Conta
# print(2320 % 11)

# cpf = input('Digite seu CPF: ')

cpf = '74682489070'
nove_digitos = cpf[:9] # 9 primeiros digitos
contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    #Declara a variavel resultado novamente somando o resultado da multiplicação
    #Dessa forma ja faz a multiplicação e depois soma o resultado.. A regra conta primeiro
    #A multiplicação depois a soma 
    resultado += int(digito) * contador_regressivo_1 # passou para inteiro pois era string
    # print(digito, contador_regressivo) # digito os numero do cpf, o contador é a regressão de 10.. 
    contador_regressivo_1 -= 1  # aqui vai fazendo a contagem regressiva para ajudar a multiplicar
digito_1 = (resultado * 10 % 11) # O Resultado é a soma de toda multiplicação, agora é * 10 e resto da div 11
# Condição - O primeiro_digito é = a primeiro_digito se(if) primeiro digito for maior ou igual
# a 9 se não o digito é 0.
digito_1 = digito_1 if digito_1 <= 9 else 0 

print(digito_1)