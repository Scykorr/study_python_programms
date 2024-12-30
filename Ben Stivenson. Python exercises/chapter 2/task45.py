"""Упражнение 45. Даты праздников"""


def main():
    date = input_date()
    if date == '1 января':
        print('Новый год')
    elif date == '1 июля':
        print('День Канады')
    elif date == '25 декабря':
        print('Рождество')
    else:
        print('На заданную дату праздник не приходится')


def input_date():
    return input('Введите дату: ')


if __name__ == '__main__':
    main()
