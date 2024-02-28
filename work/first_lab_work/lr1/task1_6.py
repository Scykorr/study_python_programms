# импортируем библиотеки
import numpy as np
from sklearn.linear_model import LinearRegression

"""Есть два массива: вход x и выход y. Нужно вызвать .reshape()на x,
 потому что этот массив должен быть двумерным или более точным – иметь одну колонку
 и необходимое количество рядов. Это как раз то, что определяет аргумент (-1, 1)."""

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((-1, 1))
y = np.array([7, 17, 19, 28, 35, 42, 41, 52, 57])

"""С помощью .fit() вычисляются оптимальные значение весов b₀ и b₁, 
используя существующие вход и выход (x и y) в качестве аргументов.
Другими словами, .fit() совмещает модель. Она возвращает self - переменную model.
Поэтому можно заменить две последние операции на:"""
model = LinearRegression().fit(x, y)

"""Можно получить определения (R²) с помощью .score(), вызванной на model"""
r_sq = model.score(x, y)

print('коэффициент детерминации:', r_sq)

""".score() принимает в качестве аргументов предсказатель x и регрессор y, и возвращает значение R².
model содержит атрибуты .intercept_, который представляет собой коэффициент, и b₀ с .coef_, которые представляют b₁:"""

print('коэффициент регрессии b0:', model.intercept_)

print('коэффициент регрессии b1:', model.coef_)

"""Когда нас устраивает модель, мы можем использовать её для прогнозов с текущими или другими данными."""

y_pred = model.predict(x)
print('прогнозируемые значения:', y_pred, sep='\n')

input("\nДля завершения, нажмите клавишу 'Enter'")
