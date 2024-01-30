"""Упражнение 7. Сумма первых n положительных чисел"""
from math import ceil
inp_num = ceil(float(input('Введите число: ')) - 1)
result_sum = (inp_num * (inp_num + 1)) / 2
print(f'Итоговая сумма: {result_sum}')
