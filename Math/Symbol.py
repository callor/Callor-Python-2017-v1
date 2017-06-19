from sympy import Symbol, symbols, expand, factor
from sympy.interactive.printing import init_printing
from sympy.printing.pretty.pretty import pprint

# 심볼 선언
x = Symbol('x')


print('x에 대한 다항식:',x + x + 3)

x, y = symbols('x, y') 
print('x,y에 대한 다항식',x * y + x * y + x * y)


print('전개식:',expand((x + 1) * (x + 2)))
print('인수분해:',factor(x**2 + 3*x + 2))

# 오름차순 정렬
init_printing(order='rev-lex')

print('pprint:',end='')
pprint(expand((x + 1) * (x + 2)))

polynomial = 2 + 3*x + x**2
print('polynomial:', end='')
pprint(polynomial)


polynomial = x**2 + 2*x*y + y**2
print('다항식대입:',polynomial.subs({x:2, y:1}))


