# импортируем библиотеки
from sympy import Eq, symbols, solve

# задаем наименования осей
x, y = symbols("x y")
# задаем систему уравнений
eq1 = Eq(5 * pow(x, 2) + 6 * pow(y, 2), 3)
eq2 = Eq(7 * x + 3 * y, 1)
# вычисляем решение и выводим ответ в консоль
solution = solve((eq1, eq2), (x, y))
print(solution)
input("\nДля завершения, нажмите клавишу 'Enter'")

