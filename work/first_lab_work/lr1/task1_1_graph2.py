import numpy as np
import matplotlib.pyplot as plt
plt.title(r'$Задание 1.1. График: g = 3sin(x) - cos^2x. x<=0; 3*sqrt(1+x^2), x>0$')
x = np.linspace(-2, 0, 200)
g = 3 * np.sin(x) - pow(np.cos(x), 2)
x1 = np.linspace(0.000000001, 2, 200)
g1 = 3 * np.sqrt(1 + x1**2)
plt.plot(x, g, x1, g1)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$g$')
plt.show()
