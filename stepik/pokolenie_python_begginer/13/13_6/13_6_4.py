from math import pi


# объявление функции
def get_circle(radius):
    result_c = 2 * pi * radius
    result_s = pi * pow(radius, 2)
    return result_c, result_s


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
