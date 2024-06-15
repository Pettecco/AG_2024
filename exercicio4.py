from sympy import Symbol, solve

# v1 = 27 V, v2 = 12 V, v3 = 19 V
# Define duas novas funções.
def calcula_f1(i1, i2):
    return 20000 * i1 + 5000 * i2 - 15

def calcula_f2(i1, i2):
    return -5000 * i1 - 15000 * i2 + 7

# Define i1 e i2 como variáveis.
i1 = Symbol('i1')
i2 = Symbol('i2')

g = calcula_f1(i1, i2)
h = calcula_f2(i1, i2)

resultado = solve((g, h))
print (u'\n Resultado do sistema de equações.')
print (resultado)

