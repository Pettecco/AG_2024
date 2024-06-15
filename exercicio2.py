from sympy import Derivative, Symbol, N, Rational

# Utilizando Rational da biblioteca sympy para facilitar a escrita da função
# c = 1894 % 10 = 4

def calcula_f(x):
    return 20 + 7*x**4 + x**Rational(1, 3) - 12*x**3

x = Symbol('x')

resultado = Derivative(calcula_f(x), x).doit()
print (u'\n Equação do deslocamento da função calcula_f.')
print (N(resultado))

deslocamento_7 = Derivative(calcula_f(x), x).doit().subs({x: 7})
descolamento_1 = Derivative(calcula_f(x), x).doit().subs({x: 1})
descolamento = deslocamento_7 - descolamento_1

print (u'\n Descolacemento de t = 1s a t = 7s.')
print (N(descolamento))

aceleracao = Derivative(calcula_f(x), x, 2).doit()
print (u'\n Equação da aceleração da função calcula_f.')
print (N(aceleracao))

