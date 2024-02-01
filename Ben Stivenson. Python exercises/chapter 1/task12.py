"""Упражнение 12. Расстояние между точками на Земле"""
from math import radians, acos, sin, cos
first_coordinate_x = radians(float(input('Первая координата х: ')))
first_coordinate_y = radians(float(input('Первая координата y: ')))
second_coordinate_x = radians(float(input('Первая координата х: ')))
second_coordinate_y = radians(float(input('Первая координата y: ')))
distance = round(6371.01 * acos(sin(first_coordinate_x) * sin(second_coordinate_x) +
                                cos(first_coordinate_x) * cos(second_coordinate_x) * cos(first_coordinate_y - second_coordinate_y)))
print(f'Расстояние между двумя точками планеты: {distance}км')
