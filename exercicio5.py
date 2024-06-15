from sympy import Symbol, solve, sin, exp

def calcula_f1(x):
    return exp(x - 3) + exp(x - 1) + exp(x) - 5

def calcula_f2(x):
    return (x**4) - 4*(x** 3) + 3*x - 4

def calcula_f3(x):
    return 4 * sin(5 * x) - 2

x = Symbol('x')
y = calcula_f1(x)
resultado = solve(y)

print (u'\n Resultado da equação exp(x-3) + exp(x-1) + exp(x) - 5 = 0.')
print ('x =', resultado)

y = calcula_f2(x)
resultado = solve(y)

print (u'\n Resultado da equação x**4 - 4*x**3 + 3*x - 4 = 0.')
print ('x =', resultado)

y = calcula_f3(x)
resultado = solve(y)

print (u'\n Resultado da equação 4*sin(5*x) -2 = 0.')
print ('x =', resultado)


