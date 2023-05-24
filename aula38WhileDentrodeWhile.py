'''
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim

While dentro de While
'''
# Condição
qtd_linhas = 5
qtd_colunas = 5

linha = 1 #contador
#Roda 1x e a while dentro dela roda 5x
while linha <= qtd_linhas:
    coluna = 1
    print(linha)
    # Roda 5x
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')