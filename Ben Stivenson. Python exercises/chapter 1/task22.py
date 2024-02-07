"""Упражнение 22. Площадь треугольника (снова)"""
from math import sqrt


def calc_sqr_triangle(first_side: float, second_side: float, third_side: float):
    half_perimetr = (first_side + second_side + third_side) / 2
    print(f'Площадь треугольника: {sqrt(half_perimetr * (half_perimetr - first_side)*(
        half_perimetr - second_side)*(half_perimetr - third_side))}')


if __name__ == '__main__':
    first_side_triangle = float(
        input('Введите длину первой стороны треугольника: '))
    second_side_triangle = float(
        input('Введите длину второй стороны треугольника: '))
    third_side_triangle = float(
        input('Введите длину третьей стороны треугольника: '))
    calc_sqr_triangle(first_side=first_side_triangle,
                      second_side=second_side_triangle,
                      third_side=third_side_triangle)
