# импортируем библиотеки
import matplotlib.pyplot as plt
import numpy as np
# прорисовываем график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# задаем требуемые границы
X = np.arange(-1, 1, 0.01)
Y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(X, Y)
Z = 3 * pow(X, 2) - 2 * pow(Y, 2)
# прорисовываем график
ax.plot_surface(X, Y, Z)
# называем график
plt.title('Задание 1.3')
# отображаем график
plt.show()
