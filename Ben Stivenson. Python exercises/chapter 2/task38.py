"Упражнение 38. Угадайте фигуру"


def guess_figure(side_amount) -> None:
    if side_amount == 3:
        print("Треугольник")
    elif side_amount == 4:
        print("Четырехугольник")
    elif side_amount == 5:
        print("Пятиугольник")
    elif side_amount == 6:
        print("Шестиугольник")
    elif side_amount == 7:
        print("Семиугольник")
    elif side_amount == 8:
        print("Восьмиугольник")
    elif side_amount == 9:
        print("Девятиугольник")
    elif side_amount == 10:
        print("Десятиугольник")
    else:
        print("Введенное Вами число выходит за рамки требуемого диапазона")


if __name__ == '__main__':
    inp_side_amount = int(input('Введите количество сторон'))
    guess_figure(side_amount=inp_side_amount)
