'''
For + Range
range -> range(start, stop, step)
'''
# Segundo iteravel que vamos intender é range.
# A função range não depende do for e nem for dele.
# É apenas exemplos para demonstrar como ele pode ser usado.

### Pegando todos numeros pares de 0 a 100 com range ###
### numeros = range (0, 100, 2) Começa no 0 e de 2 em 2 vai mostrando os numeros pares até 100. ###

numeros = range(0,10,2) # numeros de 0 a 10 
# Em python na maioria das vezes o numero final não é mostrado (aqui vamos ver até o 9)
# Para ir até 10 é necessario colocar o range em (11).

# Para cada numero em numeros, ele vai jogar 1 na variavel numero
for numero in numeros:
    print(numero)
