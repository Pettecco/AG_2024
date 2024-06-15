from sympy import Limit, Symbol, S

def calcula_f(x):
    return (2 * x**2 - 7) / (7 * x**5 - 2)

x = Symbol('x')
c = (1894 % 10)

resultado = Limit(calcula_f(x), x, 1).doit()
print (u'\n Limite da função calcula_f para x -> 1.')
print(resultado * (c + 1))

resultado = Limit(calcula_f(x), x, S.Infinity).doit()
print (u'\n Limite da função calcula_f para x -> oo.')
print(resultado * (c + 1))

resultado = Limit(calcula_f(x), x, -S.Infinity).doit()
print (u'\n Limite da função calcula_f para x -> -oo.')
print (resultado + (c + 1))
