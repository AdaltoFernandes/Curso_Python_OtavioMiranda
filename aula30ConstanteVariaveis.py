'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 101 #KM local em que o carro esta na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega
##### USAR LETRAS MAISCULAS PARA COISAS QUE NÃO VÃO MUDAR NO CODIGO #####
##### EX: Velocidade maxima coisa que não vai mudar #####

# # passou da velocidade permitida
# if velocidade > RADAR_1:
#     print(f'O carro passou acima da velocidade permitida, cerda de {velocidade}kmh')
# else:
#     print('Velocidade permitida')

vel_carro_pass_radar_1 = velocidade > RADAR_1
multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE)


#\ para continuar o codigo na linha abaixo
if vel_carro_pass_radar_1:
    print(f'O carro multado no {local_carro}km ')
else:
    print('Velocidade Permitida!')

if multado_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado no radar 1')