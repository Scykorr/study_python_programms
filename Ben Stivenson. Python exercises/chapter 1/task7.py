"""Упражнение 7. Сумма первых n положительных чисел"""
from math import ceil

def count_sum_n_nums(inp_num: float) -> None:
    print(f'Итоговая сумма: {(inp_num * (inp_num + 1)) / 2}')


if __name__ == '__main__':
    inp_num = ceil(float(input('Введите число: ')) - 1)
    count_sum_n_nums(inp_num=inp_num)
