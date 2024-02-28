# рисуем графики для наглядности полученного решения
from math import pi
from matplotlib import pyplot as plt
import numpy as np


u=0     #x-position of the center
v=0    #y-position of the center
a=np.sqrt(3/5)     #radius on the x-axis
b=np.sqrt(3/6)    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
x = np.linspace(-1, 1, 200)
plt.title(r'$Задание 1.7$')
plt.plot(x, ((1 - 7 * x) / 3))
plt.plot(u+a*np.cos(t), v+b*np.sin(t))
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$g$')
plt.show()
