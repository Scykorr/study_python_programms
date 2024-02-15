import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-1, 1, 0.01)
Y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(X, Y)
Z = 3 * pow(X, 2) - 2 * pow(Y, 2)

ax.plot_surface(X, Y, Z)
plt.title('Задание 1.3')
plt.show()
