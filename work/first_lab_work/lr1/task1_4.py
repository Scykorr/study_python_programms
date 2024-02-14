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
