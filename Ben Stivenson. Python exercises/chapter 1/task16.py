"""Упражнение 16. Площадь и объем"""
from math import pi
input_radius = float(input('Введите радиус: '))
sqr_circle = pi * pow(input_radius, 2)
v_ball = 4 / 3 * pi * pow(input_radius, 3)
print(f'Площадь круга: {sqr_circle}\nОбъем шара: {v_ball}')
