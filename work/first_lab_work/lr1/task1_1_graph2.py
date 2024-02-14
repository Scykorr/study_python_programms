import numpy as np
import matplotlib.pyplot as plt
plt.title(r'$Задание 1.1. График: g = 3sin(x) - cos^2x. x<=0; 3*sqrt(1+x^2), x>0$')
x = np.linspace(-2, 0, 200)
g = 3 * np.sin(x) - pow(np.cos(x), 2)
x1 = np.linspace(0, 2, 200)
g1 = 3 * np.sqrt(1 + x1**2)
x2 = [0, 0]
y2 = [(3 * np.sin(0) - pow(np.cos(0), 2)), (3 * np.sqrt(1 + 0**2))]
plt.plot(x, g, x1, g1, x2, y2)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$g$')
plt.show()
