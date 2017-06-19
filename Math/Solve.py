"""
방정식 풀이
"""


from sympy import Symbol, solve,symbol,symbols, pprint


x=Symbol('x')
equation = 2 * x - 6
print('2*x-6의 근(리스트형식):',solve(equation))

equation = x ** 2 + 3 * x + 2
print('x ** 2 + 3 * x + 2의 근(리스트형식):',solve(equation))
print('x ** 2 + 3 * x + 2의 근(사전형식):',solve(equation, dict=True))

equation = x ** 2 + x + 1
print('x ** 2 + x + 1의 근(허근):',solve(equation, dict=True))



a, b, c = symbols('a, b, c')
equation = a * x ** 2 + b * x + c
"""
x에 대한 방정식임을 알려줘야 한다.
solve(equation) 이렇게 할 경우 a에 대한 방정식으로 인식하여
    결과를 이렇게 돌려준다 => [{a: -(b*x + c)/x**2}]
"""
print('a * x ** 2 + b * x + c 의 근:',solve(equation, x, dict=True))
pprint(solve(equation, x, dict=True))


"""
연립방정식 풀이
"""
y = Symbol('y')
equation1 = x + 2 * y - 3
equation2 = 3 * x - y + 2
print(solve((equation1, equation2), dict=True))






