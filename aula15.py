# Como coletar dados do usuario em python INPUT
# input('Qual seu nome? ')
# O input feito acima não faz nada no código, ela só é exibida no terminal
# Usando input para guardar a informações na variavel
# nome = input('Qual o seu nome? ')

# numero_1 = input('Digite um numero: ')
# numero_2 = input('Digite um numero: ')

# print(f'A soma dos números é: {numero_1 + numero_2}')
# Input torna uma string e o resultado da errado pq é feito uma concatenação

# O modo correto tratando a string para int
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite um numero: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
