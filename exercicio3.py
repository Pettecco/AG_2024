from sympy import Integral, Symbol, N, Rational

# Utilizando Rational da biblioteca sympy para facilitar a escrita da função
# c = 1894 % 10 = 4

def calcula_f(x):
    return 5*x**3 + (x/3)**3**(Rational(1, 5)) + Rational(3, 4)*x - 12

x = Symbol('x')

# trabalho de uma força variável se da pela área do gráfico, que pode ser calculada através de uma integral definida

trabalho = Integral(calcula_f(x), (x, 3, 8)).doit()

print (u'\n Integral definida da função calcula_f para x entre 3 e 8. Representando o trabalho')
print (N(trabalho))  # Resultado em ponto flutuante.
