"""Упражнение 10. Арифметика"""
from math import log10, pow
num_a = int(input('Введите целое число a: '))
num_b = int(input('Введите целое число b: '))
print(f'Сумма: {num_a + num_b}')
print(f'Разность: {num_a - num_b}')
print(f'Произведение: {num_a * num_b}')
print(f'Частное от деления a на b: {num_a / num_b}')
print(f'Остаток от деления a на b: {num_a % num_b}')
print(f'Десятичный логарифм числа a: {log10(num_a)}')
print(f'Результат возведения числа a в степень b: {pow(num_a, num_b)}')
