""" Упражнение 46. Какого цвета клетка?"""


def main():
    coord = input_coord()
    inp_letter = coord[0]
    inp_num = coord[1]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    # if date == '1 января':
    #     print('Новый год')
    # elif date == '1 июля':
    #     print('День Канады')
    # elif date == '25 декабря':
    #     print('Рождество')
    # else:
    #     print('На заданную дату праздник не приходится')


def input_coord():
    return input('Введите координату клетки на шахматной доске: ')


if __name__ == '__main__':
    main()
