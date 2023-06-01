"""
Introdução as função (def) em Python
Funções são trechos de códigos usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) (a, b, c)
e retornar um valor específico.
Por padrão, funções em Python retornam None (Nada)
"""

# def Print(a, b, c):
#     print('Opa1')
#     print('Opa2')
#     print('Opa3')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


# def saudacao(nome):
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

