from sympy import Integral, Symbol,pprint
x = Symbol('x')
f = x**2 + x + 1
print(Integral(f, x).doit())
pprint(Integral(f, x).doit())

