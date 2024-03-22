"""Упражнение 35. Чет или нечет?"""


def get_answer(num: int) -> None:
    print('--------------------------')
    if num % 2 == 0:
        print('Введенное число является четным')
    else:
        print('Введенное число является нечетным')


if __name__ == '__main__':
    inp_num = int(input('Введите целове число: '))
    get_answer(num=inp_num)
