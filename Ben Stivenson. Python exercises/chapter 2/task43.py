"""Упражнение 43. Узнать ноту по частоте"""


def main():
    freq = float(input_freq())
    if 260.63 <= freq <= 262.63:
        print('Нота C4')
    elif 292.66 <= freq <= 294.66:
        print('Нота D4')
    elif 328.63 <= freq <= 330.63:
        print('Нота E4')
    elif 348.23 <= freq <= 350.23:
        print('Нота F4')
    elif 391 <= freq <= 393:
        print('Нота G4')
    elif 439 <= freq <= 441:
        print('Нота A4')
    elif 492.88 <= freq <= 494.88:
        print('Нота B4')
    else:
        print('Ноты, соответствующей введенной частоте не существует')


def input_freq():
    return input('Введите частоту: ')


if __name__ == '__main__':
    main()
