"""Упражнение 10. Арифметика"""
from math import log10

def simple_operations(num_a: int, num_b: int) -> None:
    print(f'Сумма: {num_a + num_b}')
    print(f'Разность: {num_a - num_b}')
    print(f'Произведение: {num_a * num_b}')
    print(f'Частное от деления a на b: {num_a / num_b}')
    print(f'Остаток от деления a на b: {num_a % num_b}')
    print(f'Десятичный логарифм числа a: {log10(num_a)}')
    print(f'Результат возведения числа a в степень b: {pow(num_a, num_b)}')


if __name__ == '__main__':
    num_a = int(input('Введите целое число a: '))
    num_b = int(input('Введите целое число b: '))
    simple_operations(num_a=num_a, num_b=num_b)