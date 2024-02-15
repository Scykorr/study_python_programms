from sympy import Eq, symbols, solve
import numpy as np
from matplotlib import pyplot as plt
from math import pi

x, y = symbols("x y")

eq1 = Eq(5 * pow(x, 2) + 6 * pow(y, 2), 3)
eq2 = Eq(7 * x + 3 * y, 1)

solution = solve((eq1, eq2), (x, y))
print(solution)


u=0     #x-position of the center
v=0    #y-position of the center
a=np.sqrt(3/5)     #radius on the x-axis
b=np.sqrt(3/6)    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
x = np.linspace(-1, 1, 200)
plt.title(r'$Задание 1.7$')
plt.plot(x, ((1 - 7 * x) / 3))
plt.plot( u+a*np.cos(t) , v+b*np.sin(t))
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$g$')
plt.show()




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
