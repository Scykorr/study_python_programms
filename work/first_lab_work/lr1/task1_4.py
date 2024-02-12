import numpy as np
import matplotlib.pyplot as plt
plt.title(r'$Задание 1.4. График: x^3 - 1.5x^2 +1.32x + 6.39 = 0.$')
x = np.linspace(-2, 2, 200)
y = (1 + pow(x, 2)) / (1 + 2 * pow(x, 2))
plt.plot(x, y)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()
