from sympy import Eq, symbols, solve

x, y = symbols("x y")

eq1 = Eq(5 * pow(x, 2) + 6 * pow(y, 2), 3)
eq2 = Eq(7 * x + 3 * y, 1)

solution = solve((eq1, eq2), (x, y))
print(solution)

# import numpy as np
# from scipy.optimize import fsolve


# def eq1(p):
#     x, y = p
#     return (5 * x**2 + 6*y**2 - 3, 7*x + 3*y - 1)


# x, y = fsolve(eq1, (1, 0))
# x, y
# p = (x, y)
# print(eq1(p))


# """for 3"""
# from scipy.optimize import fsolve
# def equations(p):
# x,y,z = p
# return (x**2+y*x-10, x*y + y**2 +z*x+5,z**2+3*x*z-5)
# x, y,z = fsolve(equations, (0, 0,0))
# print(x,y,z)
# print(equations((x, y,z)))