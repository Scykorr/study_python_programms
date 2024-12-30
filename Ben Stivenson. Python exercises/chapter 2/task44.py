"""Упражнение 44. Портреты на банкнотах"""


def main():
    num = int(input_num())
    if num == 1:
        print('Джордж Вашингтон')
    elif num == 2:
        print('Томас Джефферсон')
    elif num == 5:
        print('Авраам Линкольн')
    elif num == 10:
        print('Александр Гамильтон')
    elif num == 20:
        print('Эндрю Джексон')
    elif num == 50:
        print('Улисс Грант')
    elif num == 100:
        print('Бенджамин Франклин')
    else:
        print('Банкноты данного номинала не существует')


def input_num():
    return input('Введите номинал банкноты США: ')


if __name__ == '__main__':
    main()
