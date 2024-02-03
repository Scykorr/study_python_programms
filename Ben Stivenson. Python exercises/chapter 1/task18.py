"""Упражнение 18. Объем цилиндра"""
from math import pi

def calc_cylinder_volume(inp_radius: float, inp_height: float) -> None:
    print(f'Площадь цилиндра: {round(pi * pow(inp_radius, 2) * inp_height, 1)}')


if __name__ == '__main__':
    inp_radius = float(input('Введите радиус основания цилиндра: '))
    inp_height = float(input('Введите высоту цилиндра: '))
    calc_cylinder_volume(inp_radius=inp_radius, inp_height=inp_height)