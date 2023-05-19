nome = 'Adalto Fernandes'
altura = 1.89
peso = 102
imc = peso / (altura ** altura)

# Formatação de strings
linha_01 = f'{nome} tem {altura} de altura, pesa {peso} quilos e seu imc é: {imc:.2f}'
print(linha_01)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print()

# print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é:', imc)
# # Adalto tem 1.89 de altura,
# Pesa 102 quilos e seu imc é
# 30.625794345447417

