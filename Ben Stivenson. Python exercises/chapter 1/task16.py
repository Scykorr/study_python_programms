"""Упражнение 16. Площадь и объем"""
from math import pi

def calc_square_and_volume(input_radius: float) -> None:
    sqr_circle = pi * pow(input_radius, 2)
    v_ball = 4 / 3 * pi * pow(input_radius, 3)
    print(f'Площадь круга: {sqr_circle}\nОбъем шара: {v_ball}')

if __name__ == '__main__':
    input_radius = float(input('Введите радиус: '))
    calc_square_and_volume(input_radius=input_radius)