"""Упражнение 21. Площадь треугольника"""


def calc_sqr_triangle(base_triangle: float, height_triangle: float) -> None:
    print(f'Площадь треугольника: {base_triangle * height_triangle / 2}')


if __name__ == '__main__':
    base = float(input('Введите основание треугольника: '))
    height = float(input('Введите высоту треугольника: '))
    calc_sqr_triangle(base_triangle=base, height_triangle=height)
