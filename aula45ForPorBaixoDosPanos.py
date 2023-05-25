'''
Iterável -> str , range , etc (__iter__) <- metodo
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entregue seu iterador
'''
# texto = iter('Luiz') #.__iter__

# for letra in texto - acaba chamando o iter do meu texto, já solicita o obj iterador dele.
# dentro do for 
texto = 'Luiz' # iterável
iterator = iter(texto) # iterator

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
    
###### O for abaixo faz isso ai tudo que está em cima ######
for letra in texto:
    print(letra)

# # Isso  pode ser chamado de outro modo
# print(texto.__next__())
# # Desse modo
# print(next(texto))
# Quando esgotam os valores da um erro de StopIteration

