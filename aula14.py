a = 'A'
b = 'B'
c = 1.1
# formato1 = 'a={} b={} c={}'.format(a, b, c)

# string = 'a={} b={} c{}'
# formato2 = string.format(a, b, c)

# string = 'b={1} a={0} a={0} a={0} c{2:.2f}'
# formato3 = string.format(a, b, c)

# Parametro nomeado (nome3)
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c{nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c)


print(formato)

