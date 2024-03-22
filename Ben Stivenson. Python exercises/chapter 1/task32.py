"""Упражнение 32. Сумма цифр в числе"""


def get_sum(curr_num: int) -> None:
    first_num = curr_num % 10
    second_num = curr_num % 100 // 10
    third_num = curr_num % 1000 // 100
    fourth_num = curr_num // 1000
    num_summ = first_num + second_num + third_num + fourth_num
    print(f'{fourth_num} + {third_num} + {second_num} + {first_num} = {num_summ}')


if __name__ == '__main__':
    inp_num = int(input('Введите целое четырехзначное число: '))
    get_sum(curr_num=inp_num)
