# импортируем библиотеки
import numpy as np
import matplotlib.pyplot as plt
# называем график
plt.title(r'$Задание 1.1. График: y = (1 + x^2) / (1 + 2x^2).$')
# формируем последовательности координат х и у
x = np.linspace(-2, 2, 200)
y = (1 + pow(x, 2)) / (1 + 2 * pow(x, 2))
# прорисовываем график
plt.plot(x, y)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
# отображаем график
plt.show()
