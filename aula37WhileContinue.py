'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim

# BREAK - termina o loop
# CONTINUE - cuidado ao usar o continue pq pode fazer um loop infinito
# Serão usados para o while mais perto

'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6: # Pula o 6 na contagem e continua contando.. 
      print('Não vou mostrar o 6')
      continue
    
    # if contador == 10: # Pula o 10 na contagem e continua contando.. 
    #   print('Não vou mostrar o', contador) # print de acordo com o contador
    #   continue

    if contador >= 10 and contador <= 27: 
      print('Não vou mostrar o', contador) 
      continue

    print(contador)

    if contador == 40:
      break


print('Acabou')

