"""Упражнение 23. Площадь правильного многоугольника"""
from math import tan, pi


def sqr_figure(side_len: float, side_amount: int) -> None:
    print(f'Площадь правильного многоугольника: {
          side_amount * pow(side_len, 2) / (4 * tan(pi / side_amount))}')


if __name__ == '__main__':
    inp_side_len = float(
        input('Введите длину стороны правильного многоугольника: '))
    inp_side_amount = int(
        input('Введите количество сторон правильного многоугольника: '))
    sqr_figure(side_len=inp_side_len, side_amount=inp_side_amount)
