'''
Flag (Bandeira) - Marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True # Só vai ser TRUE se entrar na condição do IF.
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) # Retorna false se não for None
print(passou_no_if, passou_no_if is not None) # Retorna true se não for None


if passou_no_if is None:
   print('Passou no IF')
else:
    print('Não passou no IF')