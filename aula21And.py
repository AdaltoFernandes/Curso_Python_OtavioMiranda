# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras. 
# se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor
# São considerados falsy (QUE VC JA VIU)
# 0 ,0.0 ,'' <- Tipos falsy (Não é falso mais é considerado falso no Python)
# Também existe o tipo None que é usado para representar um não valor

# para entender a logica

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
  print('Entrar')
elif entrada == 'S':
  print('Sair')
else:
  print('Digite corretamente')


# Avaliação de curto circuito #
print(True and False and True)
print(bool(''))
print(True and 0 and True)

