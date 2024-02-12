import numpy as np
import matplotlib.pyplot as plt
plt.title(r'$Задание 1.1. График: g = 3sin(x) - cos^2x. x<=0$')
x = np.linspace(-2, 0, 200)
g = 3 * np.sin(x) - pow(np.cos(x), 2)
plt.plot(x, g)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$g$')
plt.show()
