"""Упражнение 21. Площадь треугольника"""

def calc_sqr_triangle(base: float, height: float) -> None:
    print(f'Площадь треугольника: {base * height / 2}')

if __name__ == '__main__':
    base = float(input('Введите основание треугольника: '))
    height = float(input('Введите высоту треугольника: '))
    calc_sqr_triangle(base=base, height=height)

