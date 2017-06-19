"""
극한값 계산
"""
from sympy import Symbol, S, symbols, Limit,sin


x, a, h = symbols('x, a, h') 
fx = 3 * x ** 2 - 4 * x + 1 
# 함수 f(x) 를 정의 
fxa = fx.subs({x: a}) # 함수 f(x) 에 x=a 를 대입 
fxh = fx.subs({x: a + h}) # 함수 f(x) 에 x=a+h 를 대입 
print(Limit((fxh-fxa)/h, h, 0).doit()) # 정의를 이용하여 극한값(=미분계수) 계산 6*a - 4


x=Symbol('x')
print(Limit(1/x, x, S.Infinity)) 
print(Limit(1/x, x, S.Infinity).doit())

print(Limit(sin(x)/x, x, 0).doit())
print(Limit((a**x-1)/x, x, 0).doit())
print(Limit((1+x)**(1/x), x, 0).doit())



