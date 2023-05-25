'''
Repetições
while (enquanto) = ( while = enquanto, if = se, else = se não)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
'''

condicao = True

#Loop infinito
# while condicao:
#     print(1)
#     print(2)
#     print(3)

# Sempre fica nessa condição
while condicao:
    nome = input('Qual seu nome?: ')
    print = (f'Seu nome é {nome}'),

    if nome == 'sair':
      break # isso faz o while parar ou seja o loop infito.

print('Acabou')