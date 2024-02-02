"""Упражнение 18. Объем цилиндра"""
from math import pi
inp_radius = float(input('Введите радиус основания цилиндра: '))
inp_height = float(input('Введите высоту цилиндра: '))
result_value = round(pi * pow(inp_radius, 2) * inp_height, 1)
print(f'Площадь цилиндра: {result_value}')