# def sign(x):  # вроде бы есть в numpy, но и написать несложно...
#     if x > 0:
#         return 1
#     elif x < 0:
#         return -1
#     else:
#         return 0


# def dicho(f, a, b, eps=1.0e-14):  # Дихотомия. Один вещественный корень у кубического полинома
#     fa = f(a)                               # есть всегда. Его и найдем...
#     fb = f(b)
#     while True:
#         c = 0.5*(a+b)
#         if abs(b-a) < eps:
#             return c
#         fc = f(c)
#         if abs(fc) <= eps:
#             return c
#         if sign(fa)*sign(fc) < 0:
#             b = c
#             fb = fc
#         else:
#             a = c
#             fa = fc


# def div_poly(p, a):  # делим исходный полином на (x-a) и получаем квадратный
#     r = [0, 0, 0]          # трехчлен, поставляющий два недостающих корня
#     r[2] = p[3]
#     r[1] = p[2]+a*p[3]
#     r[0] = (p[1]+a*(p[2]+a*p[3]))
#     return tuple(r)


# def solve_qube(p):  # парадная функция
#     q = max(p)
#     left = -abs(q)/abs(p[3])  # границы вещественного корня
#     right = -left
#     x1 = dicho(lambda x: p[3]*x**3+p[2]*x**2+p[1]*x+p[0], left, right)
#     (c, b, a) = div_poly(p, x1)
#     d = b**2-4*a*c
#     x2 = (-b+d**0.5)/(2*a)
#     x3 = (-b-d**0.5)/(2*a)
#     return (x1, x2, x3)


# print(solve_qube([1, -1.5, 1.32, 6.39]))
import numpy as np
import matplotlib.pyplot as plt

x = x = np.linspace(-1.35, -1.25, 200)

plt.figure(figsize=(10, 5))
plt.plot(x, (pow(x, 3)),
         label=r'$y1 = x^3$')
plt.plot(x, (1.5 * pow(x, 2) - 1.32 * x - 6.39),
         label=r'$y2 = 1,5x^2 -1,32x-6,39$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y1, y2$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.title('Задание 1.2')
plt.show()
# выдавать приблизительное значение х
