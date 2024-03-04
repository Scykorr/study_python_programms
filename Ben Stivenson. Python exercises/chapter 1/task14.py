"""Упражнение 14. Рост"""


def calc_height(input_height_foot: int, input_height_inch: int) -> None:
    print(
        f'Ваш рост в сантиметрах: {(input_height_foot * 12 + input_height_inch) * 2.54}')


if __name__ == '__main__':
    input_height_foot = int(input('Введите количество футов в Вашем росте: '))
    input_height_inch = int(input('Введите количество дюймов в Вашем росте: '))
    calc_height(input_height_foot=input_height_foot,
                input_height_inch=input_height_inch)
