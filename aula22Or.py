# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras. 
# se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor
# São considerados falsy (QUE VC JA VIU)
# 0 ,0.0 ,'' <- Tipos falsy (Não é falso mais é considerado falso no Python)
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
  print('Entrar')
elif entrada == 'S':
  print('Sair')
else:
  print('Digite corretamente')

# Avaliação de curto circuito #

senha = input('Senha: ') or 'Sem senha'
print(senha)
# print(0 or False or 0 or 'abc' or True)

