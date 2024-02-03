"""Упражнение 12. Расстояние между точками на Земле"""
from math import radians, acos, sin, cos

def calc_distance(first_coordinate_x: float, 
                  second_coordinate_x: float, 
                  first_coordinate_y: float, 
                  second_coordinate_y: float) -> None:
    print(f'Расстояние между двумя точками планеты: {round(6371.01 * acos(sin(first_coordinate_x) * sin(second_coordinate_x)
           + cos(first_coordinate_x) * cos(second_coordinate_x) * cos(first_coordinate_y - second_coordinate_y)))}км')


if __name__ == '__main__':
    first_coordinate_x = radians(float(input('Первая координата х: ')))
    first_coordinate_y = radians(float(input('Первая координата y: ')))
    second_coordinate_x = radians(float(input('Первая координата х: ')))
    second_coordinate_y = radians(float(input('Первая координата y: ')))
    calc_distance(first_coordinate_x=first_coordinate_x,
                   first_coordinate_y=first_coordinate_y,
                     second_coordinate_x=second_coordinate_x,
                       second_coordinate_y=second_coordinate_y)