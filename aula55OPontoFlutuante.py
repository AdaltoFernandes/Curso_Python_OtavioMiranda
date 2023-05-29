"""
Impressão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal # 3° 

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) #0.799999 - Numero impreciso

# 1° Forma de corrigir isso
print(f'{numero_3:.2f}') # Formatando desse modo, sai o 0.8 corretamente

# 2° - Função Round -> Arredonda o numero 
print(round(numero_3, 1)) # (variavel, quantas casas mostrar)

# 3° Modulo Decimal - Quando precisar daquele 00.000002911 lá do final usar ele.
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)



