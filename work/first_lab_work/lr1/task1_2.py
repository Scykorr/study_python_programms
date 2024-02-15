import numpy as np
import matplotlib.pyplot as plt

x = x = np.linspace(-2, 2, 200)
plt.figure(figsize=(10, 5))
plt.plot(x, (2 * np.sin(np.pi * x) - 5 * np.cos(np.pi * x)),
         label=r'$y = 2sin(πx) - 5cos(πx)$')
plt.plot(x, (pow(np.cos(2 * np.pi * x), 2) - 3 * np.sin(3 * np.pi * x)),
         label=r'$z = cos^2(2πx) - 3sin(3πx)$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y,z$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.title('Задание 1.2')
plt.show()
