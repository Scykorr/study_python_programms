""" Упражнение 42. Узнать частоту по ноте"""


def main():
    sound = input_sound()
    letter = sound[0].lower()
    value = int(sound[1])
    if letter == 'с':
        print('Частота:', round(16.35 * (2 ** value), 2))
    elif letter == 'd':
        print('Частота:', round(18.35 * (2 ** value), 2))
    elif letter == 'e':
        print('Частота:', round(20.6 * (2 ** value), 2))
    elif letter == 'f':
        print('Частота:', round(21.83 * (2 ** value), 2))
    elif letter == 'g':
        print('Частота:', round(24.5 * (2 ** value), 2))
    elif letter == 'a':
        print('Частота:', round(27.5 * (2 ** value), 2))
    elif letter == 'b':
        print('Частота:', round(30.87 * (2 ** value), 2))


def input_sound():
    return input('Введите ноту: ')


if __name__ == '__main__':
    main()
